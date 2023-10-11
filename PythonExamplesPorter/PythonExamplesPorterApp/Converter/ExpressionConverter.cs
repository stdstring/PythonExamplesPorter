using System.Globalization;
using System.Text;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;

namespace PythonExamplesPorterApp.Converter
{
    internal record ConvertResult(String Result, IDictionary<String, String> ImportData);

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
            IDictionary<String, String> importData = new Dictionary<String, String>();
            ExpressionConverterVisitor visitor = new ExpressionConverterVisitor(_model, buffer, importData, _appData);
            visitor.VisitExpression(expression);
            return new ConvertResult(buffer.ToString(), importData);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }

    internal class ExpressionConverterVisitor : CSharpSyntaxWalker
    {
        public ExpressionConverterVisitor(SemanticModel model, StringBuilder buffer, IDictionary<String, String> importData, AppData appData)
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
                default:
                    throw new UnsupportedSyntaxException($"Unsupported expression: {expression.Kind()}");
                    //_buffer.Append("<<<some expression>>>");
                    //break;
            }
        }

        public override void VisitObjectCreationExpression(ObjectCreationExpressionSyntax node)
        {
            CheckResult argumentsCheckResult = ArgumentListChecker.Check(node.ArgumentList.GetArguments());
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
            CheckResult argumentsCheckResult = ArgumentListChecker.Check(node.ArgumentList.GetArguments());
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
                // TODO (std_string) : there are problems with some unicode symbols - investigate their
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
                    AppendImportData(leftOperandResult.ImportData);
                    ConvertResult rightOperandResult = expressionConverter.Convert(node.Right);
                    AppendImportData(rightOperandResult.ImportData);
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
            AppendImportData(methodCallData.ModuleName, "");
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
            AppendImportData(result.ImportData);
            return result.Result;
        }

        private void AppendImportData(IDictionary<String, String> importData)
        {
            foreach (KeyValuePair<String, String> importEntry in importData)
            {
                if (!_importData.ContainsKey(importEntry.Key))
                    _importData.Add(importEntry);
            }
        }

        private void AppendImportData(String moduleName, String aliasName)
        {
            if (String.IsNullOrEmpty(moduleName))
                return;
            if (!_importData.ContainsKey(moduleName))
                _importData.Add(moduleName, aliasName);
        }

        private void ProcessTypeResolveData(TypeResolveData resolveData)
        {
            AppendImportData(resolveData.ModuleName, "");
            _buffer.Append($"{resolveData.ModuleName}.{resolveData.TypeName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExternalEntityResolver _externalEntityResolver;
        private readonly StringBuilder _buffer;
        private readonly IDictionary<String, String> _importData;
    }
}
