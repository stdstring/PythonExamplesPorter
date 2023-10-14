using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace PythonExamplesPorterApp.Checker
{
    internal static class ArgumentListChecker
    {
        public static CheckResult CheckForMethod(this IReadOnlyList<ArgumentSyntax> arguments)
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

        public static CheckResult CheckForElementAccess(this IReadOnlyList<ArgumentSyntax> arguments, SemanticModel model)
        {
            if (arguments.Count != 1)
                return new CheckResult(false, "Unsupported count of arguments for ElementAccessExpression");
            ExpressionSyntax expression = arguments[0].Expression;
            switch (expression)
            {
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() != SyntaxKind.NumericLiteralExpression:
                    return new CheckResult(false, "Unsupported non numerical ElementAccessExpression");
                case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                    return new CheckResult(true);
                default:
                    SymbolInfo symbolInfo = model.GetSymbolInfo(expression);
                    switch (symbolInfo.Symbol)
                    {
                        case null:
                            return new CheckResult(false, $"Unrecognizable type of ElementAccessExpression: \"{expression}\"");
                        case INamedTypeSymbol typeSymbol when typeSymbol.ToDisplayString() == "String.Int32":
                            return new CheckResult(true);
                        default:
                            return new CheckResult(false, $"Unsupported type of ElementAccessExpression: \"{expression}\"");
                    }
            }
        }
    }
}