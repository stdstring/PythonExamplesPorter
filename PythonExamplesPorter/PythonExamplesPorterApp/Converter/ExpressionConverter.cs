using System.Text;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;

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
            _buffer = buffer;
            _importData = importData;
            _appData = appData;
        }

        public void VisitExpression(ExpressionSyntax expression)
        {
            switch (expression)
            {
                case ObjectCreationExpressionSyntax node:
                    VisitObjectCreationExpression(node);
                    break;
                default:
                    _buffer.Append("<<<some expression>>>");
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
            TypeResolveResult resolveResult = new ExternalEntityResolver(_model, _appData).Resolve(type);
            _importData.Add(resolveResult.ModuleName, "");
            _buffer.Append($"{resolveResult.ModuleName}.{resolveResult.TypeName}(");
            IReadOnlyList<ArgumentSyntax> arguments = argumentList?.Arguments ?? new SeparatedSyntaxList<ArgumentSyntax>();
            for (Int32 index = 0; index < arguments.Count; ++index)
            {
                if (index > 0)
                    _buffer.Append(", ");
                ExpressionConverter argumentConverter = new ExpressionConverter(_model, _appData);
                ConvertResult argumentResult = argumentConverter.Convert(arguments[index].Expression);
                _buffer.Append(argumentResult.Result);
                AppendImportData(argumentResult.ImportData);
            }
            _buffer.Append(")");
        }

        private void AppendImportData(IDictionary<String, String> importData)
        {
            foreach (KeyValuePair<String, String> importEntry in importData)
            {
                if (!_importData.ContainsKey(importEntry.Key))
                    _importData.Add(importEntry);
            }
        }

        private readonly SemanticModel _model;
        private readonly StringBuilder _buffer;
        private readonly IDictionary<String, String> _importData;
        private readonly AppData _appData;
    }

    internal record TypeResolveResult(String TypeName, String ModuleName);

    // TODO (std_string) : we must implement this functionality via Strategy pattern
    internal class ExternalEntityResolver
    {
        public ExternalEntityResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public TypeResolveResult Resolve(TypeSyntax type)
        {
            // TODO (std_string) : think about check containing assemblies
            String[] supportedTypesByNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            SymbolInfo symbolInfo = _model.GetSymbolInfo(type);
            ISymbol? typeInfo = symbolInfo.Symbol;
            if (typeInfo == null)
                throw new UnsupportedSyntaxException($"Unrecognizable type: {type}");
            String sourceNamespaceName = typeInfo.ContainingNamespace.ToDisplayString();
            String sourceTypeName = typeInfo.Name;
            Boolean isSupportedType = supportedTypesByNamespaces.Any(sourceNamespaceName.StartsWith);
            if (!isSupportedType)
                throw new UnsupportedSyntaxException($"Unsupported type: {type}");
            String destModuleName = NameTransformer.TransformNamespaceName(sourceNamespaceName);
            String destTypeName = NameTransformer.TransformClassName(sourceTypeName);
            return new TypeResolveResult(destTypeName, destModuleName);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}
