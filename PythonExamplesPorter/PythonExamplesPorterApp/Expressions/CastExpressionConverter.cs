using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.ExternalEntities;

namespace PythonExamplesPorterApp.Expressions
{
    internal class CastExpressionConverter
    {
        public CastExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _expressionConverter = new ExpressionConverter(model, appData, settings);
            _externalEntityResolver = new ExternalEntityResolver(model, appData, settings);
        }

        public ConvertResult Convert(CastExpressionSyntax expression)
        {
            ImportData importData = new ImportData();
            ExpressionSyntax innerExpression = expression.Expression;
            ConvertResult innerResult = _expressionConverter.Convert(innerExpression);
            importData.Append(innerResult.ImportData);
            String sourceRepresentation = innerResult.Result;
            CastResolveData resolveData = _externalEntityResolver.ResolveCast(expression.Type, expression.Expression, sourceRepresentation).MustSuccess();
            importData.Append(resolveData.ImportData);
            return new ConvertResult(resolveData.Cast, importData);
        }

        private readonly ExpressionConverter _expressionConverter;
        private readonly ExternalEntityResolver _externalEntityResolver;
    }
}
