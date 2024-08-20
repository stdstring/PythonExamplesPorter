﻿using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.ExternalEntities;

namespace PythonExamplesPorterApp.Expressions
{
    internal class BinaryExpressionConverter
    {
        public BinaryExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _expressionConverter = new ExpressionConverter(model, appData, settings);
            _externalEntityResolver = new ExternalEntityResolver(model, appData, settings);
        }

        public ConvertResult Convert(BinaryExpressionSyntax expression)
        {
            ImportData importData = new ImportData();
            // TODO (std_string) : add check ability of applying binary expression for given arguments
            ConvertResult leftOperandResult = _expressionConverter.Convert(expression.Left);
            importData.Append(leftOperandResult.ImportData);
            ConvertResult rightOperandResult = _expressionConverter.Convert(expression.Right);
            importData.Append(rightOperandResult.ImportData);
            switch (expression.Kind())
            {
                case SyntaxKind.AddExpression:
                    return ProcessAddExpression(expression, leftOperandResult.Result, rightOperandResult.Result, importData);
                case SyntaxKind.SubtractExpression:
                    return new ConvertResult($"{leftOperandResult.Result} - {rightOperandResult.Result}", importData);
                case SyntaxKind.MultiplyExpression:
                    return new ConvertResult($"{leftOperandResult.Result} * {rightOperandResult.Result}", importData);
                case SyntaxKind.DivideExpression:
                    // TODO (std_string) : we must check type of arguments for choosing between float divide (/) and integer divide (//) operators
                    return new ConvertResult($"{leftOperandResult.Result} / {rightOperandResult.Result}", importData);
                case SyntaxKind.ModuloExpression:
                    return new ConvertResult($"{leftOperandResult.Result} % {rightOperandResult.Result}", importData);
                case SyntaxKind.EqualsExpression:
                    return new ConvertResult($"{leftOperandResult.Result} == {rightOperandResult.Result}", importData);
                case SyntaxKind.NotEqualsExpression:
                    return new ConvertResult($"{leftOperandResult.Result} != {rightOperandResult.Result}", importData);
                case SyntaxKind.LessThanExpression:
                    return new ConvertResult($"{leftOperandResult.Result} < {rightOperandResult.Result}", importData);
                case SyntaxKind.LessThanOrEqualExpression:
                    return new ConvertResult($"{leftOperandResult.Result} <= {rightOperandResult.Result}", importData);
                case SyntaxKind.GreaterThanExpression:
                    return new ConvertResult($"{leftOperandResult.Result} > {rightOperandResult.Result}", importData);
                case SyntaxKind.GreaterThanOrEqualExpression:
                    return new ConvertResult($"{leftOperandResult.Result} >= {rightOperandResult.Result}", importData);
                case SyntaxKind.BitwiseAndExpression:
                    return new ConvertResult($"{leftOperandResult.Result} & {rightOperandResult.Result}", importData);
                case SyntaxKind.BitwiseOrExpression:
                    return new ConvertResult($"{leftOperandResult.Result} | {rightOperandResult.Result}", importData);
                case SyntaxKind.LogicalAndExpression:
                    return new ConvertResult($"{leftOperandResult.Result} and {rightOperandResult.Result}", importData);
                case SyntaxKind.LogicalOrExpression:
                    return new ConvertResult($"{leftOperandResult.Result} or {rightOperandResult.Result}", importData);
                case SyntaxKind.AsExpression:
                    switch (expression.Right)
                    {
                        case TypeSyntax typeSyntax:
                            switch (_externalEntityResolver.ResolveCast(typeSyntax, expression.Left, leftOperandResult.Result))
                            {
                                case {Success: false, Reason: var reason}:
                                    throw new UnsupportedSyntaxException($"Bad binary as expression due to: {reason}");
                                case {Success: true, Data: var resolveData}:
                                    importData.Append(resolveData!.ImportData);
                                    return new ConvertResult(resolveData.Cast, importData);
                                default:
                                    throw new UnsupportedSyntaxException($"Unexpected control flow at binary as expression: {expression}");
                            }
                        default:
                            throw new UnsupportedSyntaxException($"Unsupported binary as expression: {expression}");
                    }
                default:
                    throw new UnsupportedSyntaxException($"Unsupported binary expression: {expression.Kind()}");
            }
        }

        private ConvertResult ProcessAddExpression(BinaryExpressionSyntax node, String leftOperand, String rightOperand, ImportData importData)
        {
            OperationResult<IMethodSymbol> operatorSymbol = node.GetMethodSymbol(_model);
            if (!operatorSymbol.Success)
                throw new UnsupportedSyntaxException(operatorSymbol.Reason);
            switch (operatorSymbol.Data!.ContainingType.GetTypeFullName())
            {
                case "System.String" when operatorSymbol.Data.Parameters.Length == 2:
                    String leftOperandType = operatorSymbol.Data.Parameters[0].Type.GetTypeFullName();
                    String rightOperandType = operatorSymbol.Data.Parameters[1].Type.GetTypeFullName();
                    switch (leftOperandType, rightOperandType)
                    {
                        case ("System.String", "System.String"):
                            return new ConvertResult($"{leftOperand} + {rightOperand}", importData);
                        case ("System.String", _):
                            return new ConvertResult($"{leftOperand} + str({rightOperand})", importData);
                        case (_, "System.String"):
                            return new ConvertResult($"str({leftOperand}) + {rightOperand}", importData);
                        default:
                            throw new UnsupportedSyntaxException($"Unsupported binary expression: node");
                    }
                default:
                    return new ConvertResult($"{leftOperand} + {rightOperand}", importData);
            }
        }

        private readonly SemanticModel _model;
        private readonly ExpressionConverter _expressionConverter;
        private readonly ExternalEntityResolver _externalEntityResolver;
    }
}
