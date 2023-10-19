using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;

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
    }
}
