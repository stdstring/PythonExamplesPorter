using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Expressions
{
    internal class ElementAccessExpressionConverter
    {
        public ElementAccessExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _expressionConverter = new ExpressionConverter(model, appData, settings);
        }

        public ConvertResult Convert(ElementAccessExpressionSyntax expression)
        {
            IReadOnlyList<ArgumentSyntax> arguments = expression.ArgumentList.Arguments;
            ImportData importData = new ImportData();
            if (arguments.Count != 1)
                throw new UnsupportedSyntaxException($"Unsupported count of arguments for ElementAccessExpression: {arguments.Count} arguments");
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                    return ProcessCommonCase(expression, arguments, importData);
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.StringLiteralExpression:
                    return ProcessSpecialCase(expression, arguments, importData);
                default:
                    ITypeSymbol typeSymbol = arguments[0].Expression.GetExpressionTypeSymbol(_model).MustSuccess();
                    switch (typeSymbol)
                    {
                        case var _ when typeSymbol.GetTypeFullName() == "System.Int32":
                            return ProcessCommonCase(expression, arguments, importData);
                        default:
                            return ProcessSpecialCase(expression, arguments, importData);
                    }
            }
        }

        private ConvertResult ProcessCommonCase(ElementAccessExpressionSyntax expression, IReadOnlyList<ArgumentSyntax> arguments, ImportData importData)
        {
            ConvertResult targetResult = _expressionConverter.Convert(expression.Expression);
            importData.Append(targetResult.ImportData);
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                    Int32 value = (Int32)literalExpression.Token.Value!;
                    return new ConvertResult($"{targetResult.Result}[{value}]", importData);
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() != SyntaxKind.NumericLiteralExpression:
                    throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                default:
                    ITypeSymbol typeSymbol = arguments[0].Expression.GetExpressionTypeSymbol(_model).MustSuccess();
                    switch (typeSymbol)
                    {
                        case var _ when typeSymbol.GetTypeFullName() == "System.Int32":
                            ConvertResult argumentResult = _expressionConverter.Convert(arguments[0].Expression);
                            importData.Append(argumentResult.ImportData);
                            return new ConvertResult($"{targetResult.Result}[{argumentResult.Result}]", importData);
                        default:
                            throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                    }
            }
        }

        // TODO (std_string) : think about location
        private ConvertResult ProcessSpecialCase(ElementAccessExpressionSyntax expression, IReadOnlyList<ArgumentSyntax> arguments, ImportData importData)
        {
            ConvertResult targetResult = _expressionConverter.Convert(expression.Expression);
            importData.Append(targetResult.ImportData);
            ITypeSymbol expressionType = expression.GetExpressionTypeSymbol(_model)
                .MustSuccess("Unsupported ElementAccessExpression expression: {0}");
            String sourceTypeFullName = expressionType.GetTypeFullName();
            String getByNameMethod = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, "GetByName");
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.StringLiteralExpression:
                {
                    String value = literalExpression.Token.Text;
                    return new ConvertResult($"{targetResult.Result}.{getByNameMethod}({value})", importData);
                }
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() != SyntaxKind.StringLiteralExpression:
                    throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                default:
                    ITypeSymbol typeSymbol = arguments[0].Expression.GetExpressionTypeSymbol(_model).MustSuccess();
                    switch (typeSymbol)
                    {
                        case var _ when typeSymbol.GetTypeFullName() == "System.String":
                        {
                            ConvertResult argumentResult = _expressionConverter.Convert(arguments[0].Expression);
                            importData.Append(argumentResult.ImportData);
                            return new ConvertResult($"{targetResult.Result}.{getByNameMethod}({argumentResult.Result})", importData);
                        }
                        case {TypeKind: TypeKind.Enum, Name: var enumName}:
                        {
                            ConvertResult argumentResult = _expressionConverter.Convert(arguments[0].Expression);
                            importData.Append(argumentResult.ImportData);
                            String getByEnumMethod = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, $"GetBy{enumName}");
                            return new ConvertResult($"{targetResult.Result}.{getByEnumMethod}({argumentResult.Result})", importData);
                        }
                        default:
                            throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                    }
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverter _expressionConverter;
    }
}