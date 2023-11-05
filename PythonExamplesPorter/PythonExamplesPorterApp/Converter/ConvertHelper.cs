using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;

namespace PythonExamplesPorterApp.Converter
{
    // TODO (std_string) : think about place
    internal static class ConvertHelper
    {
        public static Boolean ContainAttribute(this IReadOnlyList<AttributeListSyntax> attributes, SemanticModel model, String expectedFullName)
        {
            foreach (AttributeListSyntax attributeList in attributes)
            {
                foreach (AttributeSyntax attribute in attributeList.Attributes)
                {
                    ISymbol? symbol = model.GetSymbolInfo(attribute.Name).Symbol;
                    if (symbol == null)
                        return false;
                    if (symbol.Kind != SymbolKind.Method)
                        return false;
                    INamedTypeSymbol? symbolType = symbol.ContainingType;
                    if (symbolType == null)
                        return false;
                    if (symbolType.Kind != SymbolKind.NamedType)
                        return false;
                    // TODO (std_string) : think about using SymbolDisplayFormat
                    String attributeFullName = symbolType.ToDisplayString();
                    if (String.Equals(expectedFullName, attributeFullName))
                        return true;
                }
            }
            return false;
        }

        public static IReadOnlyList<ArgumentSyntax> GetArguments(this ArgumentListSyntax? argumentList)
        {
            if (argumentList == null)
                return Array.Empty<ArgumentSyntax>();
            return argumentList.Arguments;
        }

        public static String GetTypeFullName(this ITypeSymbol type)
        {
            // TODO (std_string) : think about using SymbolDisplayFormat
            return $"{type.ContainingNamespace.ToDisplayString()}.{type.Name}";
        }

        public static OperationResult<ITypeSymbol> GetExpressionTypeSymbol(this ExpressionSyntax expression, SemanticModel model)
        {
            ExpressionSyntax GetTargetExpression(ExpressionSyntax sourceExpression)
            {
                return sourceExpression switch
                {
                    ParenthesizedExpressionSyntax parenthesizedExpression => GetTargetExpression(parenthesizedExpression.Expression),
                    CastExpressionSyntax castExpression => castExpression.Type,
                    _ => sourceExpression
                };
            }
            ExpressionSyntax targetExpression = GetTargetExpression(expression);
            SymbolInfo symbolInfo = model.GetSymbolInfo(targetExpression);
            return symbolInfo.Symbol switch
            {
                null => new OperationResult<ITypeSymbol>(false, $"Unrecognizable type of expression: {expression}"),
                ILocalSymbol localSymbol => new OperationResult<ITypeSymbol>(true, "", localSymbol.Type),
                IPropertySymbol propertySymbol => new OperationResult<ITypeSymbol>(true, "", propertySymbol.Type),
                IMethodSymbol { MethodKind: MethodKind.Constructor } methodSymbol => new OperationResult<ITypeSymbol>(true, "", methodSymbol.ContainingType),
                IMethodSymbol { ReturnsVoid: true } => new OperationResult<ITypeSymbol>(false, $"Unsupported type (void) of expression: {expression}"),
                IMethodSymbol methodSymbol => new OperationResult<ITypeSymbol>(true, "", methodSymbol.ReturnType),
                IArrayTypeSymbol arrayTypeSymbol => new OperationResult<ITypeSymbol>(true, "", arrayTypeSymbol),
                ITypeSymbol typeSymbol => new OperationResult<ITypeSymbol>(true, "", typeSymbol),
                _ => new OperationResult<ITypeSymbol>(false, $"Unsupported type of expression: {expression}")
            };
        }
    }
}
