using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Utils
{
    internal static class CompilationChecker
    {
        public static Boolean CheckCompilationErrors(String filename, Compilation compilation, ILogger logger)
        {
            logger.LogInfo("Checking compilation for errors and warnings:");
            IList<Diagnostic> diagnostics = compilation.GetDiagnostics();
            Diagnostic[] diagnosticErrors = diagnostics.Where(d => d.Severity == DiagnosticSeverity.Error).ToArray();
            Diagnostic[] diagnosticWarnings = diagnostics.Where(d => d.Severity == DiagnosticSeverity.Warning).ToArray();
            Boolean hasErrors = false;
            logger.LogInfo($"Found {diagnosticErrors.Length} errors in the compilation");
            foreach (Diagnostic diagnostic in diagnosticErrors)
            {
                logger.LogError($"Found following error in the compilation of the {filename} entity: {diagnostic.GetMessage()}");
                hasErrors = true;
            }
            logger.LogInfo($"Found {diagnosticWarnings.Length} warnings in the compilation");
            foreach (Diagnostic diagnostic in diagnosticWarnings)
                logger.LogWarning($"Found following warning in the compilation: {diagnostic.GetMessage()}");
            return !hasErrors;
        }
    }
}
