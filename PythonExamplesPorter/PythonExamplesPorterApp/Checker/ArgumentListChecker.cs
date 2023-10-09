using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace PythonExamplesPorterApp.Checker
{
    internal static class ArgumentListChecker
    {
        public static CheckResult Check(IReadOnlyList<ArgumentSyntax> arguments)
        {
            foreach (ArgumentSyntax argument in arguments)
            {
                if (!argument.RefKindKeyword.IsKind(SyntaxKind.None))
                    return new CheckResult(false, "Unsupported argument kind: ref");
                if (!argument.RefOrOutKeyword.IsKind(SyntaxKind.None))
                    return new CheckResult(false, "Unsupported argument kind: out");
            }
            return new CheckResult(true);
        }
    }
}