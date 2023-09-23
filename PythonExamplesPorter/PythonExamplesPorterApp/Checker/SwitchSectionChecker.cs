using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;

namespace PythonExamplesPorterApp.Checker
{
    internal static class SwitchSectionChecker
    {
        public static CheckResult Check(SwitchSectionSyntax switchSection)
        {
            CheckResult labelsResult = Check(switchSection.Labels);
            if (!labelsResult.Result)
                return labelsResult;
            return Check(switchSection.Statements);
        }

        private static CheckResult Check(SyntaxList<SwitchLabelSyntax> labels)
        {
            foreach (SwitchLabelSyntax label in labels)
            {
                if (label is CasePatternSwitchLabelSyntax)
                    return new CheckResult(Result: false, Reason: "Unsupported type of expression: pattern matching");
            }
            return new CheckResult(Result: true);
        }

        private static CheckResult Check(SyntaxList<StatementSyntax> statements)
        {
            return CheckStatements(statements, true);
        }

        private static CheckResult Check(StatementSyntax statement, Boolean allowBreak)
        {
            switch (statement)
            {
                case BreakStatementSyntax _ when !allowBreak:
                    return new CheckResult(false, "Unsupported break statement usage");
                case BreakStatementSyntax _:
                case ForEachStatementSyntax _:
                case ForStatementSyntax _:
                case WhileStatementSyntax _:
                case DoStatementSyntax _:
                case LocalDeclarationStatementSyntax _:
                case ExpressionStatementSyntax _:
                case SwitchStatementSyntax _:
                    return new CheckResult(true);
                case BlockSyntax blockStatement:
                    return CheckStatements(blockStatement.Statements, false);
                case IfStatementSyntax ifStatement:
                    return CheckIfStatement(ifStatement);
                case ContinueStatementSyntax _:
                    throw new InvalidOperationException("Unexpected continue operator in compiled code");
                default:
                    return new CheckResult(false, $"Unsupported statement type: {statement.Kind()}");
            }
        }

        private static CheckResult CheckStatements(SyntaxList<StatementSyntax> statements, Boolean allowBreak)
        {
            foreach (StatementSyntax statement in statements)
            {
                CheckResult result = Check(statement, allowBreak);
                if (!result.Result)
                    return result;
            }
            return new CheckResult(true);
        }

        private static CheckResult CheckIfStatement(IfStatementSyntax ifStatement)
        {
            CheckResult thenResult = Check(ifStatement.Statement, false);
            if (!thenResult.Result)
                return thenResult;
            if (ifStatement.Else == null)
                return new CheckResult(true);
            return Check(ifStatement.Else.Statement, false);
        }
    }
}
