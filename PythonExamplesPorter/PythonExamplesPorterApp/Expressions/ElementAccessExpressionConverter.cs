using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Expressions
{
    internal class ElementAccessExpressionConverter
    {
        public ElementAccessExpressionConverter(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public ConvertResult Convert(ElementAccessExpressionSyntax expression)
        {
            IReadOnlyList<ArgumentSyntax> arguments = expression.ArgumentList.Arguments;
            if (arguments.Count != 1)
                throw new UnsupportedSyntaxException($"Unsupported count of arguments for ElementAccessExpression: {arguments.Count} arguments");
            ImportData importData = new ImportData();
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
            ConvertResult targetResult = expressionConverter.Convert(expression.Expression);
            importData.Append(targetResult.ImportData);
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                    Int32 value = (Int32)literalExpression.Token.Value!;
                    return new ConvertResult($"{targetResult.Result}[{value}]", importData);
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.StringLiteralExpression:
                    return ProcessStringArgSpecialCase(expression, literalExpression.Token.Text);
                default:
                    throw new UnsupportedSyntaxException($"Unsupported kind ({arguments[0].Expression.Kind()}) of ElementAccessExpression argument in expression: \"{expression}\"");
            }
        }

        private ConvertResult ProcessStringArgSpecialCase(ElementAccessExpressionSyntax expression, String arg)
        {
            throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression argument - System.String in expression: \"{expression}\"");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}