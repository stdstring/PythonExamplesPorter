using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Expressions
{
    internal class ArrayCreationConverter
    {
        public ArrayCreationConverter(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public ConvertResult Convert(ArrayCreationExpressionSyntax expression)
        {
            switch (expression.Initializer)
            {
                case null:
                    return ConvertArrayCreationWithSize(expression);
                case var initializer:
                    return Convert(initializer);
            }
        }

        public ConvertResult Convert(ImplicitArrayCreationExpressionSyntax expression)
        {
            return Convert(expression.Initializer);
        }

        public ConvertResult Convert(InitializerExpressionSyntax expression)
        {
            if (expression.Kind() != SyntaxKind.ArrayInitializerExpression)
                throw new UnsupportedSyntaxException($"Bad usage of ArrayCreationConverter for expression: \"{expression}\"");
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
            ConvertResult[] convertResults = expression.Expressions.Select(expressionConverter.Convert).ToArray();
            ImportData importData = new ImportData();
            convertResults.Foreach(result => importData.Append((ImportData)result.ImportData));
            String[] initExpressions = convertResults.Select(result => result.Result).ToArray();
            return new ConvertResult($"[{String.Join(", ", initExpressions)}]", importData);
        }

        private ConvertResult ConvertArrayCreationWithSize(ArrayCreationExpressionSyntax expression)
        {
            ImportData importData = new ImportData();
            switch (expression.Type.RankSpecifiers)
            {
                case [{Sizes: [LiteralExpressionSyntax {Token.Value: 0}]}]:
                    return new ConvertResult("[]", importData);
                case [{Sizes: [LiteralExpressionSyntax {Token.Value: Int32 value}]}]:
                    return new ConvertResult($"[None for i in range(0, {value})]", importData);
                default:
                    throw new UnsupportedSyntaxException($"Unsupported ranks in ArrayCreationExpression expression: \"{expression}\"");
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}