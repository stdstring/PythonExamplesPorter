using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using NUnit.Framework;

namespace PythonExamplesPorterAppTests.TestUtils;

internal static class PreparationHelper
{
    public static void CheckCompilationErrors(CSharpCompilation compilation)
    {
        Console.WriteLine("Checking compilation for errors, warnings and infos:");
        IList<Diagnostic> diagnostics = compilation.GetDiagnostics();
        /*IList<Diagnostic> declarationDiagnostics = compilation.GetDeclarationDiagnostics();
            IList<Diagnostic> methodDiagnostics = compilation.GetMethodBodyDiagnostics();
            IList<Diagnostic> parseDiagnostics = compilation.GetParseDiagnostics();*/
        bool hasErrors = false;
        foreach (Diagnostic diagnostic in diagnostics)
        {
            Console.WriteLine($"Diagnostic message: severity = {diagnostic.Severity}, message = \"{diagnostic.GetMessage()}\"");
            if (diagnostic.Severity == DiagnosticSeverity.Error)
                hasErrors = true;
        }
        Assert.That(hasErrors, Is.False);
        if (diagnostics.Count == 0)
            Console.WriteLine("No any errors, warnings and infos");
        Console.WriteLine();
    }

    public static SemanticModel Prepare(string source, string assemblyName)
    {
        SyntaxTree tree = CSharpSyntaxTree.ParseText(source);
        CSharpCompilation compilation = CSharpCompilation.Create(assemblyName)
            .AddReferences(MetadataReference.CreateFromFile(typeof(string).Assembly.Location))
            .AddReferences(MetadataReference.CreateFromFile(typeof(Assert).Assembly.Location))
            .AddSyntaxTrees(tree)
            .WithOptions(new CSharpCompilationOptions(OutputKind.DynamicallyLinkedLibrary));
        CheckCompilationErrors(compilation);
        return compilation.GetSemanticModel(tree);
    }
}