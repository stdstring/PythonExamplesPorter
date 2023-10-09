using Microsoft.CodeAnalysis;

namespace PythonExamplesPorterApp.Converter
{
    internal static class SemanticHelper
    {
        public static String GetTypeFullName(this ITypeSymbol type)
        {
            return $"{type.ContainingNamespace.ToDisplayString()}.{type.Name}";
        }
    }
}