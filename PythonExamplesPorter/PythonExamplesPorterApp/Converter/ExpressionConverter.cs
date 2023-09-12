using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace PythonExamplesPorterApp.Converter
{
    internal record ConvertResult(Boolean Result, String Value, String ErrorReason = "");

    internal class ExpressionConverter
    {
        public ConvertResult Convert(ExpressionSyntax expression)
        {
            return new ConvertResult(true, "<<<some expression>>>");
        }
    }

    internal class ExpressionConverterVisitor : CSharpSyntaxWalker
    {
    }
}
