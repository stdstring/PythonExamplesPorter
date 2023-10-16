﻿using Microsoft.CodeAnalysis;

namespace PythonExamplesPorterApp.Converter
{
    internal record SourceType(String NamespaceName, String TypeName)
    {
        public SourceType(ITypeSymbol typeSymbol) : this(typeSymbol.ContainingNamespace.ToDisplayString(), typeSymbol.Name)
        {
        }

        public String FullName { get; } = $"{NamespaceName}.{TypeName}";
    }
}