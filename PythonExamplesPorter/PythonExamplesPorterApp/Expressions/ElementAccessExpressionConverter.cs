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
            _settings = settings;
        }

        public ConvertResult Convert(ElementAccessExpressionSyntax expression)
        {
            IReadOnlyList<ArgumentSyntax> arguments = expression.ArgumentList.Arguments;
            if (arguments.Count != 1)
                throw new UnsupportedSyntaxException($"Unsupported count of arguments for ElementAccessExpression: {arguments.Count} arguments");
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                    return ProcessCommonCase(expression);
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.StringLiteralExpression:
                    return ProcessSpecialCase(expression);
                default:
                    switch (arguments[0].Expression.GetExpressionTypeSymbol(_model))
                    {
                        case { Success: false, Reason: var reason }:
                            throw new UnsupportedSyntaxException(reason);
                        case { Success: true, Data: var typeSymbol }:
                            switch (typeSymbol)
                            {
                                case var _ when typeSymbol!.GetTypeFullName() == "System.Int32":
                                    return ProcessCommonCase(expression);
                                default:
                                    return ProcessSpecialCase(expression);
                            }
                        default:
                            throw new UnsupportedSyntaxException($"Unexpected control flow at converting ElementAccessExpression expression: {expression}");
                    }
            }
        }

        private ConvertResult ProcessCommonCase(ElementAccessExpressionSyntax expression)
        {
            IReadOnlyList<ArgumentSyntax> arguments = expression.ArgumentList.Arguments;
            ImportData importData = new ImportData();
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData, _settings);
            ConvertResult targetResult = expressionConverter.Convert(expression.Expression);
            importData.Append(targetResult.ImportData);
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                    Int32 value = (Int32)literalExpression.Token.Value!;
                    return new ConvertResult($"{targetResult.Result}[{value}]", importData, new List<String>());
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() != SyntaxKind.NumericLiteralExpression:
                    throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                default:
                    switch (arguments[0].Expression.GetExpressionTypeSymbol(_model))
                    {
                        case {Success: false, Reason: var reason}:
                            throw new UnsupportedSyntaxException(reason);
                        case {Success: true, Data: var typeSymbol}:
                            switch (typeSymbol)
                            {
                                case var _ when typeSymbol!.GetTypeFullName() == "System.Int32":
                                    ConvertResult argumentResult = expressionConverter.Convert(arguments[0].Expression);
                                    importData.Append(argumentResult.ImportData);
                                    return new ConvertResult($"{targetResult.Result}[{argumentResult.Result}]", importData, new List<String>());
                                default:
                                    throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                            }
                        default:
                            throw new UnsupportedSyntaxException($"Unexpected control flow at converting ElementAccessExpression expression: {expression}");
                    }
            }
        }

        // TODO (std_string) : think about location
        private ConvertResult ProcessSpecialCase(ElementAccessExpressionSyntax expression)
        {
            IReadOnlyList<ArgumentSyntax> arguments = expression.ArgumentList.Arguments;
            ImportData importData = new ImportData();
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData, _settings);
            ConvertResult targetResult = expressionConverter.Convert(expression.Expression);
            importData.Append(targetResult.ImportData);
            String getByNameMethod = NameTransformer.TransformMethodName("GetByName");
            switch (arguments[0].Expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.StringLiteralExpression:
                {
                    String value = literalExpression.Token.Text;
                    return new ConvertResult($"{targetResult.Result}.{getByNameMethod}({value})", importData, new List<String>());
                }
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() != SyntaxKind.StringLiteralExpression:
                    throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                default:
                    switch (arguments[0].Expression.GetExpressionTypeSymbol(_model))
                    {
                        case {Success: false, Reason: var reason}:
                            throw new UnsupportedSyntaxException(reason);
                        case {Success: true, Data: var typeSymbol}:
                            switch (typeSymbol)
                            {
                                case var _ when typeSymbol!.GetTypeFullName() == "System.String":
                                {
                                    ConvertResult argumentResult = expressionConverter.Convert(arguments[0].Expression);
                                    importData.Append(argumentResult.ImportData);
                                    return new ConvertResult($"{targetResult.Result}.{getByNameMethod}({argumentResult.Result})", importData, new List<String>());
                                }
                                case {TypeKind: TypeKind.Enum, Name: var enumName}:
                                {
                                    ConvertResult argumentResult = expressionConverter.Convert(arguments[0].Expression);
                                    importData.Append(argumentResult.ImportData);
                                    String getByEnumMethod = NameTransformer.TransformMethodName($"GetBy{enumName}");
                                    return new ConvertResult($"{targetResult.Result}.{getByEnumMethod}({argumentResult.Result})", importData, new List<String>());
                                }
                                default:
                                    throw new UnsupportedSyntaxException($"Unsupported type of ElementAccessExpression expression: {expression}");
                            }
                        default:
                            throw new UnsupportedSyntaxException($"Unexpected control flow at converting ElementAccessExpression expression: {expression}");
                    }
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
    }
}