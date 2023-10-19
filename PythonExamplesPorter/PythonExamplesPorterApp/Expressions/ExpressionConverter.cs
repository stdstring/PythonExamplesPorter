using System.Globalization;
using System.Text;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Expressions
{
    internal class ImportData
    {
        public IDictionary<String, String> Data { get; } = new Dictionary<String, String>();

        public void Append(ImportData data)
        {
            Append(data.Data);
        }

        public void Append(IDictionary<String, String> data)
        {
            foreach (KeyValuePair<String, String> entry in data)
                Append(entry.Key, entry.Value);
        }

        public void Append(String moduleName, String aliasName)
        {
            if (String.IsNullOrEmpty(moduleName))
                return;
            if (!Data.ContainsKey(moduleName))
                Data.Add(moduleName, aliasName);
        }
    }

    internal record ConvertResult(String Result, ImportData ImportData);

    internal class ExpressionConverter
    {
        public ExpressionConverter(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public ConvertResult Convert(ExpressionSyntax expression)
        {
            StringBuilder buffer = new StringBuilder();
            ImportData importData = new ImportData();
            ExpressionConverterVisitor visitor = new ExpressionConverterVisitor(_model, buffer, importData, _appData);
            visitor.VisitExpression(expression);
            return new ConvertResult(buffer.ToString(), importData);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }

    internal class ExpressionConverterVisitor : CSharpSyntaxWalker
    {
        public ExpressionConverterVisitor(SemanticModel model, StringBuilder buffer, ImportData importData, AppData appData)
        {
            _model = model;
            _appData = appData;
            _externalEntityResolver = new ExternalEntityResolver(model, appData);
            _buffer = buffer;
            _importData = importData;
        }

        public void VisitExpression(ExpressionSyntax expression)
        {
            switch (expression)
            {
                case ObjectCreationExpressionSyntax node:
                    VisitObjectCreationExpression(node);
                    break;
                case InvocationExpressionSyntax node:
                    VisitInvocationExpression(node);
                    break;
                case IdentifierNameSyntax node:
                    VisitIdentifierName(node);
                    break;
                case LiteralExpressionSyntax node:
                    VisitLiteralExpression(node);
                    break;
                case BinaryExpressionSyntax node:
                    VisitBinaryExpression(node);
                    break;
                case MemberAccessExpressionSyntax node:
                    VisitMemberAccessExpression(node);
                    break;
                case AssignmentExpressionSyntax node:
                    VisitAssignmentExpression(node);
                    break;
                case ElementAccessExpressionSyntax node:
                    VisitElementAccessExpression(node);
                    break;
                case ArrayCreationExpressionSyntax node:
                    VisitArrayCreationExpression(node);
                    break;
                case ImplicitArrayCreationExpressionSyntax node:
                    VisitImplicitArrayCreationExpression(node);
                    break;
                case InitializerExpressionSyntax node:
                    VisitInitializerExpression(node);
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported expression: {expression.Kind()}");
            }
        }

        public override void VisitObjectCreationExpression(ObjectCreationExpressionSyntax node)
        {
            CheckResult argumentsCheckResult = node.ArgumentList.GetArguments().CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            TypeSyntax type = node.Type;
            OperationResult<TypeResolveData> resolveResult = _externalEntityResolver.ResolveType(type);
            if (!resolveResult.Success)
                throw new UnsupportedSyntaxException(resolveResult.Reason);
            TypeResolveData data = resolveResult.Data!;
            // TODO (std_string) : i return empty type for system type because we need in additional analysis - think about approach
            if (String.IsNullOrEmpty(data.TypeName))
                throw new UnsupportedSyntaxException($"Unsupported type: {type}");
            ProcessTypeResolveData(data);
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
            String[] arguments = ConvertArgumentList(expressionConverter, node.ArgumentList.GetArguments());
            _buffer.Append($"({String.Join(", ", arguments)})");
        }

        public override void VisitInvocationExpression(InvocationExpressionSyntax node)
        {
            CheckResult argumentsCheckResult = node.ArgumentList.GetArguments().CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            switch (node.Expression)
            {
                case MemberAccessExpressionSyntax memberAccessExpression:
                    VisitMemberAccessExpressionImpl(memberAccessExpression, node.ArgumentList);
                    break;
                case IdentifierNameSyntax identifierExpression:
                    throw new UnsupportedSyntaxException($"Unsupported call of method named {identifierExpression.Identifier.ValueText}");
                default:
                    throw new UnsupportedSyntaxException($"Unsupported invocation expression: {node.Expression.Kind()}");
            }
        }

        public override void VisitIdentifierName(IdentifierNameSyntax node)
        {
            SymbolInfo symbolInfo = _model.GetSymbolInfo(node);
            switch (symbolInfo.Symbol)
            {
                case null:
                    throw new UnsupportedSyntaxException($"Unrecognizable identifier: {node.Identifier}");
                case ILocalSymbol localSymbol:
                    _buffer.Append(NameTransformer.TransformLocalVariableName(localSymbol.Name));
                    break;
                case INamedTypeSymbol typeSymbol:
                    // TODO (std_string) ; think about ability of import rollback, e.g. in case of method from NUnit.Framework.Assert class
                    OperationResult<TypeResolveData> resolveResult = _externalEntityResolver.ResolveType(typeSymbol);
                    if (!resolveResult.Success)
                        throw new UnsupportedSyntaxException(resolveResult.Reason);
                    ProcessTypeResolveData(resolveResult.Data!);
                    break;
                case IPropertySymbol propertySymbol:
                    // TODO (std_string) : think about smart (not straightforward) solution
                    // TODO (std_string) : think about cases when property/method/etc in source type is absent in dest handmade type
                    String name = propertySymbol.Name;
                    SourceType containedType = new SourceType(propertySymbol.ContainingType);
                    if (!_appData.HandmadeManager.IsHandmadeType(containedType.FullName))
                        throw new UnsupportedSyntaxException($"Unsupported identifier with name = \"{node.Identifier}\" and kind = \"{node.Kind()}\"");
                    IDictionary<String, String> mapping = _appData.HandmadeManager.GetHandmadeTypeMapping(containedType.FullName);
                    if (mapping.ContainsKey(name))
                        name = mapping[name];
                    _buffer.Append(name);
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported identifier with name = \"{node.Identifier}\" and kind = \"{node.Kind()}\"");
            }
        }

        public override void VisitLiteralExpression(LiteralExpressionSyntax node)
        {
            String text = node.Token.Value switch
            {
                null => node.Token.Text,
                Double value => value.ToString(CultureInfo.InvariantCulture),
                Single value => value.ToString(CultureInfo.InvariantCulture),
                Boolean value => value ? "True" : "False",
                // TODO (std_string) : there are problems with some unicode symbols - investigate their
                String _ when node.Token.Text.StartsWith('@') => $"\"\"{node.Token.Text.Substring(1)}\"\"",
                String => node.Token.Text,
                var value => value.ToString() ?? node.Token.Text
            };
            _buffer.Append(text);
        }

        public override void VisitBinaryExpression(BinaryExpressionSyntax node)
        {
            // TODO (std_string) : add check ability of applying binary expression for given arguments
            switch (node.Kind())
            {
                case SyntaxKind.AddExpression:
                    ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
                    ConvertResult leftOperandResult = expressionConverter.Convert(node.Left);
                    _importData.Append(leftOperandResult.ImportData);
                    ConvertResult rightOperandResult = expressionConverter.Convert(node.Right);
                    _importData.Append(rightOperandResult.ImportData);
                    _buffer.Append($"{leftOperandResult.Result} + {rightOperandResult.Result}");
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported binary expression: \"{node.Kind()}\"");
            }
        }

        public override void VisitMemberAccessExpression(MemberAccessExpressionSyntax node)
        {
            VisitMemberAccessExpressionImpl(node, null);
        }

        public override void VisitAssignmentExpression(AssignmentExpressionSyntax node)
        {
            switch (node.Kind())
            {
                case SyntaxKind.SimpleAssignmentExpression:
                {
                    ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
                    ConvertResult leftAssignmentResult = expressionConverter.Convert(node.Left);
                    _importData.Append(leftAssignmentResult.ImportData);
                    ConvertResult rightAssignmentResult = expressionConverter.Convert(node.Right);
                    _importData.Append(rightAssignmentResult.ImportData);
                    _buffer.Append($"{leftAssignmentResult.Result} = {rightAssignmentResult.Result}");
                    break;
                }
                default:
                    throw new UnsupportedSyntaxException($"Unsupported assignment expression: \"{node.Kind()}\"");
            }
        }

        public override void VisitElementAccessExpression(ElementAccessExpressionSyntax node)
        {
            ElementAccessExpressionConverter converter = new ElementAccessExpressionConverter(_model, _appData);
            AppendResult(converter.Convert(node));
        }

        public override void VisitArrayCreationExpression(ArrayCreationExpressionSyntax node)
        {
            ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData);
            AppendResult(converter.Convert(node));
        }

        public override void VisitImplicitArrayCreationExpression(ImplicitArrayCreationExpressionSyntax node)
        {
            ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData);
            AppendResult(converter.Convert(node));
        }

        public override void VisitInitializerExpression(InitializerExpressionSyntax node)
        {
            switch (node.Kind())
            {
                case SyntaxKind.ArrayInitializerExpression:
                    ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData);
                    AppendResult(converter.Convert(node));
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported initializer expression: \"{node.Kind()}\"");
            }
        }

        private void VisitMemberAccessExpressionImpl(MemberAccessExpressionSyntax node, ArgumentListSyntax? argumentList)
        {
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
            String[] arguments = ConvertArgumentList(expressionConverter, argumentList.GetArguments());
            ExpressionSyntax target = node.Expression;
            String targetDest = ConvertExpression(expressionConverter, target);
            SimpleNameSyntax name = node.Name;
            MethodData methodData = new MethodData(target, name, argumentList.GetArguments());
            MethodRepresentation methodRepresentation = new MethodRepresentation(targetDest, arguments);
            OperationResult<MethodCallResolveData> resolveResult = _externalEntityResolver.ResolveMethodCall(methodData, methodRepresentation);
            if (!resolveResult.Success)
                throw new UnsupportedSyntaxException(resolveResult.Reason);
            MethodCallResolveData methodCallData = resolveResult.Data!;
            _buffer.Append(methodCallData.Call);
            _importData.Append(methodCallData.ModuleName, "");
        }

        private String[] ConvertArgumentList(ExpressionConverter expressionConverter, IReadOnlyList<ArgumentSyntax> arguments)
        {
            String[] dest = new String[arguments.Count];
            for (Int32 index = 0; index < arguments.Count; ++index)
                dest[index] = ConvertExpression(expressionConverter, arguments[index].Expression);
            return dest;
        }

        private String ConvertExpression(ExpressionConverter expressionConverter, ExpressionSyntax expression)
        {
            ConvertResult result = expressionConverter.Convert(expression);
            _importData.Append(result.ImportData);
            return result.Result;
        }

        private void ProcessTypeResolveData(TypeResolveData resolveData)
        {
            _importData.Append(resolveData.ModuleName, "");
            _buffer.Append($"{resolveData.ModuleName}.{resolveData.TypeName}");
        }

        private void AppendResult(ConvertResult result)
        {
            _buffer.Append(result.Result);
            _importData.Append(result.ImportData);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExternalEntityResolver _externalEntityResolver;
        private readonly StringBuilder _buffer;
        private readonly ImportData _importData;
    }
}
