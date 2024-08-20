using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace PythonExamplesPorterApp.Checker
{
    internal static class SwitchSectionChecker
    {
        public static CheckResult Check(SwitchSectionSyntax switchSection)
        {
            switch (Check(switchSection.Labels))
            {
                case CheckResult.Error error:
                    return error;
            }
            return Check(switchSection.Statements);
        }

        private static CheckResult Check(IReadOnlyList<SwitchLabelSyntax> labels)
        {
            foreach (SwitchLabelSyntax label in labels)
            {
                if (label is CasePatternSwitchLabelSyntax)
                    return new CheckResult.Error("Unsupported type of expression: pattern matching");
            }
            return new CheckResult.Ok();
        }

        private static CheckResult Check(IReadOnlyList<StatementSyntax> statements)
        {
            return CheckStatements(statements, true);
        }

        private static CheckResult Check(StatementSyntax statement, Boolean allowBreak)
        {
            switch (statement)
            {
                case BreakStatementSyntax _ when !allowBreak:
                    return new CheckResult.Error("Unsupported break statement usage");
                case BreakStatementSyntax _:
                case ForEachStatementSyntax _:
                case ForStatementSyntax _:
                case WhileStatementSyntax _:
                case DoStatementSyntax _:
                case LocalDeclarationStatementSyntax _:
                case ExpressionStatementSyntax _:
                case SwitchStatementSyntax _:
                    return new CheckResult.Ok();
                case BlockSyntax blockStatement:
                    return CheckStatements(blockStatement.Statements, false);
                case IfStatementSyntax ifStatement:
                    return CheckIfStatement(ifStatement);
                case ContinueStatementSyntax _:
                    throw new InvalidOperationException("Unexpected continue operator in compiled code");
                default:
                    return new CheckResult.Error($"Unsupported statement type: {statement.Kind()}");
            }
        }

        private static CheckResult CheckStatements(IReadOnlyList<StatementSyntax> statements, Boolean allowBreak)
        {
            foreach (StatementSyntax statement in statements)
            {
                switch (Check(statement, allowBreak))
                {
                    case CheckResult.Error error:
                        return error;
                }
            }
            return new CheckResult.Ok();
        }

        private static CheckResult CheckIfStatement(IfStatementSyntax ifStatement)
        {
            switch (Check(ifStatement.Statement, false))
            {
                case CheckResult.Error error:
                    return error;
            }
            return ifStatement.Else == null ? new CheckResult.Ok() : Check(ifStatement.Else.Statement, false);
        }
    }
}
