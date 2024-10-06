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

        public static AttributeSyntax[] GetAttributes(this IReadOnlyList<AttributeListSyntax> attributes, SemanticModel model, String expectedFullName)
        {
            IList<AttributeSyntax> result = new List<AttributeSyntax>();
            foreach (AttributeListSyntax attributeList in attributes)
            {
                foreach (AttributeSyntax attribute in attributeList.Attributes)
                {
                    ISymbol? symbol = model.GetSymbolInfo(attribute.Name).Symbol;
                    if (symbol == null)
                        continue;
                    if (symbol.Kind != SymbolKind.Method)
                        continue;
                    INamedTypeSymbol? symbolType = symbol.ContainingType;
                    if (symbolType == null)
                        continue;
                    if (symbolType.Kind != SymbolKind.NamedType)
                        continue;
                    // TODO (std_string) : think about using SymbolDisplayFormat
                    String attributeFullName = symbolType.ToDisplayString();
                    if (String.Equals(expectedFullName, attributeFullName))
                        result.Add(attribute);
                }
            }
            return result.ToArray();
        }

        public static IReadOnlyList<ArgumentSyntax> GetArguments(this ArgumentListSyntax? argumentList)
        {
            return argumentList == null ? Array.Empty<ArgumentSyntax>() : argumentList.Arguments;
        }

        public static String GetTypeFullName(this ITypeSymbol type)
        {
            // TODO (std_string) : think about using SymbolDisplayFormat
            return type switch
            {
                IArrayTypeSymbol arrayType => $"{arrayType.ElementType.ContainingNamespace.ToDisplayString()}.{arrayType.ElementType.Name}[]",
                _ => $"{type.ContainingNamespace.ToDisplayString()}.{type.Name}"
            };
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
                null => new OperationResult<ITypeSymbol>.Error($"Unrecognizable type of expression: {expression}"),
                ILocalSymbol localSymbol => new OperationResult<ITypeSymbol>.Ok(localSymbol.Type),
                IPropertySymbol propertySymbol => new OperationResult<ITypeSymbol>.Ok(propertySymbol.Type),
                IFieldSymbol fieldSymbol => new OperationResult<ITypeSymbol>.Ok(fieldSymbol.Type),
                IMethodSymbol {MethodKind: MethodKind.Constructor} methodSymbol => new OperationResult<ITypeSymbol>.Ok(methodSymbol.ContainingType),
                IMethodSymbol {ReturnsVoid: true} => new OperationResult<ITypeSymbol>.Error($"Unsupported type (void) of expression: {expression}"),
                IMethodSymbol methodSymbol => new OperationResult<ITypeSymbol>.Ok(methodSymbol.ReturnType),
                IArrayTypeSymbol arrayTypeSymbol => new OperationResult<ITypeSymbol>.Ok(arrayTypeSymbol),
                ITypeSymbol typeSymbol => new OperationResult<ITypeSymbol>.Ok(typeSymbol),
                _ => new OperationResult<ITypeSymbol>.Error($"Unsupported type of expression: {expression}")
            };
        }

        public static OperationResult<IMethodSymbol> GetMethodSymbol(this ExpressionSyntax expression, SemanticModel model)
        {
            SymbolInfo nodeInfo = model.GetSymbolInfo(expression);
            return nodeInfo.Symbol switch
            {
                null => new OperationResult<IMethodSymbol>.Error($"Unrecognizable type of expression: {expression}"),
                IMethodSymbol symbol => new OperationResult<IMethodSymbol>.Ok(symbol),
                _ => new OperationResult<IMethodSymbol>.Error($"Unexpected type of expression: {expression}")
            };
        }
    }
}
