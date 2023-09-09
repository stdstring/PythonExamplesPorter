using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Converter
{
    internal class StatementConverterVisitor : CSharpSyntaxWalker
    {
        public StatementConverterVisitor(SemanticModel model, MethodStorage currentMethod, ILogger logger)
        {
            _model = model;
            _currentMethod = currentMethod;
            _logger = logger;
        }

        public override void VisitBlock(BlockSyntax node)
        {
            VisitStatements(node.Statements, false);
        }

        public override void VisitLocalDeclarationStatement(LocalDeclarationStatementSyntax node)
        {
            foreach (VariableDeclaratorSyntax variable in node.Declaration.Variables)
                ProcessVariableDeclaration(variable);
        }

        public override void VisitExpressionStatement(ExpressionStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}<<<expression statement>>>");
        }

        public override void VisitForEachStatement(ForEachStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# for each loop begin");
            String enumerationVariable = NameTransformer.TransformLocalVariableName(node.Identifier.Text);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}for {enumerationVariable} in <<<collection>>>:");
            VisitStatement(node.Statement, true);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# for loop end");
        }

        public override void VisitForStatement(ForStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# for loop begin");
            if (node.Declaration != null)
            {
                foreach (VariableDeclaratorSyntax variable in node.Declaration.Variables)
                    ProcessVariableDeclaration(variable);
            }
            String condition = node.Condition == null ? "true" : "<<<condition>>>";
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while {condition}:");
            if (_currentMethod.HasError)
                return;
            VisitStatement(node.Statement, true);
            if (_currentMethod.HasError)
                return;
            _indentation += StorageDef.IndentationDelta;
            foreach (ExpressionSyntax incrementor in node.Incrementors)
                _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}<<<increment expression>>>");
            _indentation -= StorageDef.IndentationDelta;
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# for loop end");
        }

        public override void VisitIfStatement(IfStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# if begin");
            VisitIfStatementImpl(node, "if");
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# if end");
        }

        public override void VisitSwitchStatement(SwitchStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# switch begin");
            // TODO (std_string) : think about possible other definition of switchCondition variable
            const String switchConditionVariable = "switch_condition";
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{switchConditionVariable} = <<<condition>>>");
            SyntaxList<SwitchSectionSyntax> sections = node.Sections;
            for (Int32 index = 0; index < sections.Count; ++index)
            {
                CheckResult sectionResult = SwitchSectionChecker.Check(sections[index]);
                if (!sectionResult.Result)
                {
                    _logger.LogError(sectionResult.Reason);
                    _currentMethod.SetError(sectionResult.Reason);
                    return;
                }
                SyntaxList<SwitchLabelSyntax> labels = sections[index].Labels;
                SyntaxList<StatementSyntax> statements = sections[index].Statements;
                Boolean hasDefaultLabel = labels.Last() is DefaultSwitchLabelSyntax;
                if (hasDefaultLabel)
                {
                    _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}else:");
                    VisitSwitchSectionStatements(statements);
                }
                else
                {
                    String switchSectionCondition = CreateSwitchSectionCondition(labels, switchConditionVariable);
                    String ifOperator = index == 0 ? "if" : "elif";
                    _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{ifOperator} {switchSectionCondition}:");
                    VisitSwitchSectionStatements(statements);
                }
                if (_currentMethod.HasError)
                    return;
            }
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# switch end");
        }

        public override void VisitWhileStatement(WhileStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# while begin");
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while <<<condition>>>:");
            VisitStatement(node.Statement, true);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# while end");
        }

        public override void VisitDoStatement(DoStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# do ... while begin");
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while true:");
            VisitStatement(node.Statement, true);
            if (_currentMethod.HasError)
                return;
            _indentation += StorageDef.IndentationDelta;
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}if <<<condition>>>:");
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation + StorageDef.IndentationDelta)}break");
            _indentation -= StorageDef.IndentationDelta;
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# do ... while end");
        }

        public override void VisitBreakStatement(BreakStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}break");
        }

        public override void VisitContinueStatement(ContinueStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}continue");
        }

        public override void VisitReturnStatement(ReturnStatementSyntax node)
        {
            String delimiter = node.Expression == null ? "" : " ";
            String expression = node.Expression == null ? "" : "<<<expression>>>";
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}return{delimiter}{expression}");
        }

        private void VisitStatements(SyntaxList<StatementSyntax> statements, bool indent)
        {
            foreach (StatementSyntax statement in statements)
            {
                VisitStatement(statement, indent);
                if (_currentMethod.HasError)
                    return;
            }
        }

        private void VisitSwitchSectionStatements(SyntaxList<StatementSyntax> statements)
        {
            IEnumerable<StatementSyntax> filteredStatements = statements.Where(statement => !(statement is BreakStatementSyntax));
            VisitStatements(new SyntaxList<StatementSyntax>(filteredStatements), true);
        }

        private void VisitStatement(StatementSyntax statement, bool indent)
        {
            if (indent)
                _indentation += StorageDef.IndentationDelta;
            ISet<SyntaxKind> knownStatements = new HashSet<SyntaxKind>
            {
                SyntaxKind.LocalDeclarationStatement,
                SyntaxKind.ExpressionStatement,
                SyntaxKind.ForEachStatement,
                SyntaxKind.ForStatement,
                SyntaxKind.IfStatement,
                SyntaxKind.SwitchStatement,
                SyntaxKind.WhileStatement,
                SyntaxKind.DoStatement,
                SyntaxKind.BreakStatement,
                SyntaxKind.ContinueStatement,
                SyntaxKind.Block,
                SyntaxKind.ReturnStatement
            };
            if (!knownStatements.Contains(statement.Kind()))
            {
                _logger.LogError($"Unsupported statement type: {statement.Kind()}");
                _currentMethod.SetError($"unsupported statement type: {statement.Kind()}");
                return;
            }
            Visit(statement);
            if (indent)
                _indentation -= StorageDef.IndentationDelta;
        }

        private void VisitIfStatementImpl(IfStatementSyntax node, String ifOperator)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{ifOperator} <<<condition>>>:");
            VisitStatement(node.Statement, true);
            switch (node.Else)
            {
                case null:
                    break;
                case var _ when node.Else.Statement.Kind() == SyntaxKind.IfStatement:
                    VisitIfStatementImpl((IfStatementSyntax)node.Else.Statement, "elif");
                    break;
                default:
                    _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}else:");
                    VisitStatement(node.Else.Statement, true);
                    break;
            }
        }

        private void ProcessVariableDeclaration(VariableDeclaratorSyntax variable)
        {
            String name = NameTransformer.TransformLocalVariableName(variable.Identifier.Text);
            String initializer = variable.Initializer == null ? "None" : "<<<initializer expr>>>";
            if (_currentMethod.HasError)
                return;
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{name} = {initializer}");
        }

        private String CreateSwitchSectionCondition(SyntaxList<SwitchLabelSyntax> labels, String switchConditionVariable)
        {
            IList<String> conditions = new List<string>();
            foreach (SwitchLabelSyntax label in labels)
            {
                if (label is CasePatternSwitchLabelSyntax)
                    throw new InvalidOperationException($"Unexpected type of switch label: CasePatternSwitchLabelSyntax");
                conditions.Add($"{switchConditionVariable} == <<<switch label condition>>>");
            }
            if (conditions.Count == 1)
                return conditions[0];
            String totalCondition = String.Join(" and ", conditions.Select(condition => $"({condition})"));
            return totalCondition;
        }

        private Int32 _indentation;
        private readonly SemanticModel _model;
        private readonly MethodStorage _currentMethod;
        private readonly ILogger _logger;
    }

    internal record CheckResult(Boolean Result, String Reason = "");

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
