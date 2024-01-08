using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Expressions
{
    internal class CastExpressionConverter
    {
        public CastExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _expressionConverter = new ExpressionConverter(model, appData, settings);
            _externalEntityResolver = new ExternalEntityResolver(model, appData);
        }

        public ConvertResult Convert(CastExpressionSyntax expression)
        {
            ImportData importData = new ImportData();
            ExpressionSyntax innerExpression = expression.Expression;
            ConvertResult innerResult = _expressionConverter.Convert(innerExpression);
            importData.Append(innerResult.ImportData);
            String sourceRepresentation = innerResult.Result;
            OperationResult <CastResolveData> resolveResult = _externalEntityResolver.ResolveCast(expression.Type, expression.Expression, sourceRepresentation);
            if (!resolveResult.Success)
                throw new UnsupportedSyntaxException(resolveResult.Reason);
            CastResolveData castResolveData = resolveResult.Data!;
            importData.AddImport(castResolveData.ModuleName);
            return new ConvertResult(castResolveData.Cast, importData);
        }

        private readonly ExpressionConverter _expressionConverter;
        private readonly ExternalEntityResolver _externalEntityResolver;
    }
}
