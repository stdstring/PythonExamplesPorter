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
            {
                String name = NameTransformer.TransformLocalVariableName(variable.Identifier.Text);
                String initializer = variable.Initializer == null ? "None" : "<<<initializer expr>>>";
                if (_currentMethod.HasError)
                    return;
                _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{name} = {initializer}");
            }
        }

        public override void VisitExpressionStatement(ExpressionStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}<<expression statement>>");
        }

        public override void VisitForEachStatement(ForEachStatementSyntax node)
        {
            String enumerationVariable = NameTransformer.TransformLocalVariableName(node.Identifier.Text);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}for {enumerationVariable} in <<<collection>>>:");
            VisitStatement(node.Statement, true);
        }

        public override void VisitForStatement(ForStatementSyntax node)
        {
            //var loopVariables = node.Declaration.Variables;
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}for <<<var>>> in range(<<<from>>>, <<<to>>>, <<<step>>>):");
            VisitStatement(node.Statement, true);
        }

        public override void VisitIfStatement(IfStatementSyntax node)
        {
            VisitIfStatementImpl(node, "if");
        }

        public override void VisitSwitchStatement(SwitchStatementSyntax node)
        {
            // TODO (std_string) : think about possible other definition of switchCondition variable
            const String switchConditionVariable = "switch_condition";
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{switchConditionVariable} = <<<condition>>>");
            SyntaxList<SwitchSectionSyntax> sections = node.Sections;
            for (Int32 index = 0; index < sections.Count; ++index)
            {
                SyntaxList<SwitchLabelSyntax> labels = sections[index].Labels;
                Boolean hasDefaultLabel = labels.Last() is DefaultSwitchLabelSyntax;
                if (hasDefaultLabel)
                {
                    _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}else:");
                    VisitStatements(sections[index].Statements, true);
                }
                else
                {
                    Tuple<Boolean, String> switchSectionCondition = CreateSwitchSectionCondition(labels, switchConditionVariable);
                    if (!switchSectionCondition.Item1)
                    {
                        _logger.LogError("Unsupported type of switch label");
                        _currentMethod.SetError("unsupported type of switch label");
                        return;
                    }
                    String ifOperator = index == 0 ? "if" : "elif";
                    _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{ifOperator} {switchSectionCondition.Item2}:");
                    VisitStatements(sections[index].Statements, true);
                }
                if (_currentMethod.HasError)
                    return;
            }
        }

        public override void VisitWhileStatement(WhileStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while <<<condition>>>:");
            VisitStatement(node.Statement, true);
        }

        public override void VisitDoStatement(DoStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while true:");
            VisitStatement(node.Statement, true);
            if (_currentMethod.HasError)
                return;
            _indentation += StorageDef.IndentationDelta;
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}if <<<condition>>>:");
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation + StorageDef.IndentationDelta)}break");
            _indentation -= StorageDef.IndentationDelta;
        }

        public override void VisitBreakStatement(BreakStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}break");
        }

        public override void VisitContinueStatement(ContinueStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}continue");
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
                SyntaxKind.Block
            };
            if (!knownStatements.Contains(statement.Kind()))
            {
                _logger.LogError($"Unsupported statement type in block: {statement.Kind()}");
                _currentMethod.SetError($"unsupported statement type in block: {statement.Kind()}");
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

        private Tuple<Boolean, String> CreateSwitchSectionCondition(SyntaxList<SwitchLabelSyntax> labels, String switchConditionVariable)
        {
            IList<String> conditions = new List<string>();
            foreach (SwitchLabelSyntax label in labels)
            {
                if (label is CasePatternSwitchLabelSyntax)
                    return new Tuple<Boolean, String>(false, "");
                conditions.Add($"{switchConditionVariable} == <<<switch label condition>>>");
            }
            if (conditions.Count == 1)
                return new Tuple<Boolean, String>(true, conditions[0]);
            String totalCondition = String.Join(" and ", conditions.Select(condition => $"({condition})"));
            return new Tuple<Boolean, String>(true, totalCondition);
        }

        private Int32 _indentation = 0;
        private readonly SemanticModel _model;
        private readonly MethodStorage _currentMethod;
        private readonly ILogger _logger;
    }
}
