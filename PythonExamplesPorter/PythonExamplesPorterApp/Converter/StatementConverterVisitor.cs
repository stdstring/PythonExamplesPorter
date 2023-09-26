﻿using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Converter
{
    internal class StatementConverterVisitor : CSharpSyntaxWalker
    {
        public StatementConverterVisitor(SemanticModel model, MethodStorage currentMethod, AppData appData)
        {
            _model = model;
            _currentMethod = currentMethod;
            _appData = appData;
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
            String expression = ConvertExpression(node.Expression);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{expression}");
        }

        public override void VisitForEachStatement(ForEachStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# for each loop begin");
            String enumerationVariable = NameTransformer.TransformLocalVariableName(node.Identifier.Text);
            String forEachExpression = ConvertExpression(node.Expression);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}for {enumerationVariable} in {forEachExpression}:");
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
            String condition = node.Condition == null ? "true" : ConvertExpression(node.Condition);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while {condition}:");
            VisitStatement(node.Statement, true);
            _indentation += StorageDef.IndentationDelta;
            foreach (ExpressionSyntax incrementExpr in node.Incrementors)
            {
                String incrementExpression = ConvertExpression(incrementExpr);
                _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{incrementExpression}");
            }
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
            String switchCondition = ConvertExpression(node.Expression);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{switchConditionVariable} = {switchCondition}");
            SyntaxList<SwitchSectionSyntax> sections = node.Sections;
            for (Int32 index = 0; index < sections.Count; ++index)
            {
                CheckResult sectionResult = SwitchSectionChecker.Check(sections[index]);
                if (!sectionResult.Result)
                    throw new UnsupportedSyntaxException(sectionResult.Reason);
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
            }
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# switch end");
        }

        public override void VisitWhileStatement(WhileStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# while begin");
            String condition = ConvertExpression(node.Condition);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while {condition}:");
            VisitStatement(node.Statement, true);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# while end");
        }

        public override void VisitDoStatement(DoStatementSyntax node)
        {
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}# do ... while begin");
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}while true:");
            VisitStatement(node.Statement, true);
            _indentation += StorageDef.IndentationDelta;
            String condition = ConvertExpression(node.Condition);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}if {condition}:");
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
            String expression = node.Expression == null ? "" : ConvertExpression(node.Expression);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}return{delimiter}{expression}");
        }

        private void VisitStatements(SyntaxList<StatementSyntax> statements, bool indent)
        {
            foreach (StatementSyntax statement in statements)
                VisitStatement(statement, indent);
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
                throw new UnsupportedSyntaxException($"Unsupported statement type: {statement.Kind()}");
            Visit(statement);
            if (indent)
                _indentation -= StorageDef.IndentationDelta;
        }

        private void VisitIfStatementImpl(IfStatementSyntax node, String ifOperator)
        {
            String condition = ConvertExpression(node.Condition);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{ifOperator} {condition}:");
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
            String initializer = variable.Initializer == null ? "None" : ConvertExpression(variable.Initializer.Value);
            _currentMethod.AddBodyLine($"{IndentationUtils.Create(_indentation)}{name} = {initializer}");
        }

        private String CreateSwitchSectionCondition(SyntaxList<SwitchLabelSyntax> labels, String switchConditionVariable)
        {
            IList<String> conditions = new List<string>();
            foreach (SwitchLabelSyntax label in labels)
            {
                if (label is CasePatternSwitchLabelSyntax)
                    throw new InvalidOperationException($"Unexpected type of switch label: CasePatternSwitchLabelSyntax");
                if (label is DefaultSwitchLabelSyntax)
                    throw new InvalidOperationException("Wrong hierarchy of case labels");
                String value = label switch
                {
                    CaseSwitchLabelSyntax switchLabel => ConvertExpression(switchLabel.Value),
                    CasePatternSwitchLabelSyntax _ => throw new InvalidOperationException("Unexpected type of switch label: CasePatternSwitchLabelSyntax"),
                    DefaultSwitchLabelSyntax _ => throw new InvalidOperationException("Wrong hierarchy of case labels"),
                    _ => throw new InvalidOperationException($"Unexpected type of label: {label.Kind()}")
                };
                conditions.Add($"{switchConditionVariable} == {value}");
            }
            if (conditions.Count == 1)
                return conditions[0];
            String totalCondition = String.Join(" and ", conditions.Select(condition => $"({condition})"));
            return totalCondition;
        }

        private String ConvertExpression(ExpressionSyntax expression)
        {
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData);
            ConvertResult result = expressionConverter.Convert(expression);
            foreach (KeyValuePair<String, String> entry in result.ImportData)
            {
                if (String.IsNullOrEmpty(entry.Value))
                    _currentMethod.ImportStorage.AddImport(entry.Key);
                else
                    _currentMethod.ImportStorage.AddImportWithAlias(entry.Key, entry.Value);
            }
            return result.Result;
        }

        private Int32 _indentation;
        private readonly SemanticModel _model;
        private readonly MethodStorage _currentMethod;
        private readonly AppData _appData;
    }
}