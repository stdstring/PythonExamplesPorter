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
                default:
                    _buffer.Append("<<<some expression>>>");
                    //throw new UnsupportedSyntaxException($"Unsupported expression: {expression.Kind()}");
                    break;
            }
        }

        public override void VisitObjectCreationExpression(ObjectCreationExpressionSyntax node)
        {
            ArgumentListSyntax? argumentList = node.ArgumentList;
            CheckResult argumentsCheckResult = ArgumentListChecker.Check(argumentList);
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
            String[] arguments = ConvertArgumentList(expressionConverter, argumentList);
            _buffer.Append($"({String.Join(", ", arguments)})");
        }

        public override void VisitInvocationExpression(InvocationExpressionSyntax node)
        {
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
            String[] arguments = ConvertArgumentList(expressionConverter, node.ArgumentList);
            switch (node.Expression)
            {
                case MemberAccessExpressionSyntax memberAccessExpression:
                    ExpressionSyntax target = memberAccessExpression.Expression;
                    String targetDest = ConvertExpression(expressionConverter, target);
                    SimpleNameSyntax name = memberAccessExpression.Name;
                    OperationResult<MethodCallResolveData> resolveResult = _externalEntityResolver.ResolveMethodCall(target, targetDest, name, arguments);
                    if (!resolveResult.Success)
                        throw new UnsupportedSyntaxException(resolveResult.Reason);
                    MethodCallResolveData methodCallData = resolveResult.Data!;
                    _buffer.Append(methodCallData.Call);
                    if (!String.IsNullOrEmpty(methodCallData.ModuleName))
                        AppendImportData(methodCallData.ModuleName, "");
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

        private String[] ConvertArgumentList(ExpressionConverter expressionConverter, ArgumentListSyntax? argumentList)
        {
            if (argumentList == null)
                return Array.Empty<String>();
            String[] dest = new String[argumentList.Arguments.Count];
            for (Int32 index = 0; index < argumentList.Arguments.Count; ++index)
                dest[index] = ConvertExpression(expressionConverter, argumentList.Arguments[index].Expression);
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
            if (!_importData.ContainsKey(moduleName))
                _importData.Add(moduleName, aliasName);
        }

        private void ProcessTypeResolveData(TypeResolveData resolveData)
        {
            _importData.Add(resolveData.ModuleName, "");
            _buffer.Append($"{resolveData.ModuleName}.{resolveData.TypeName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExternalEntityResolver _externalEntityResolver;
        private readonly StringBuilder _buffer;
        private readonly IDictionary<String, String> _importData;
    }
}
