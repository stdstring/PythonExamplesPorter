using System.Globalization;
using System.Text;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Expressions
{
    internal record ConvertResult(String Result, ImportData ImportData, IList<String> AfterResults);

    internal class ExpressionConverterSettings
    {
        public ExpressionConverterSettings()
        {
        }

        public ExpressionConverterSettings(ExpressionConverterSettings other)
        {
            AllowIncrementDecrement = other.AllowIncrementDecrement;
            AllowObjectInitializer = other.AllowObjectInitializer;
        }

        public Boolean AllowIncrementDecrement { get; set; }

        public Boolean AllowObjectInitializer { get; set; }
    }

    // TODO (std_string) : think about more smart solution
    internal record ConvertedArguments(String[] Values, String[]? NamedValues)
    {
        public String[] GetArguments(Boolean canUseNamedArguments)
        {
            return canUseNamedArguments && NamedValues != null ? NamedValues : Values;
        }
    }

    internal class ExpressionConverter
    {
        public ExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _settings = settings;
        }

        public ConvertResult Convert(ExpressionSyntax expression)
        {
            ExpressionConverterVisitor visitor = new ExpressionConverterVisitor(_model, _appData, _settings);
            visitor.VisitExpression(expression);
            return new ConvertResult(visitor.Buffer.ToString(), visitor.ImportData, visitor.AfterResults);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
    }

    internal class ExpressionConverterVisitor : CSharpSyntaxWalker
    {
        public ExpressionConverterVisitor(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _externalEntityResolver = new ExternalEntityResolver(model, appData);
            _settings = settings;
        }

        public StringBuilder Buffer { get; } = new StringBuilder();

        public ImportData ImportData { get; } = new ImportData();

        public IList<String> AfterResults { get; } = new List<String>();

        public void VisitExpression(ExpressionSyntax expression)
        {
            if (ProcessPredefinedExpressions(expression))
                return;
            switch (expression)
            {
                case ObjectCreationExpressionSyntax node:
                    VisitObjectCreationExpression(node);
                    break;
                case InvocationExpressionSyntax node:
                    VisitInvocationExpression(node);
                    break;
                case IdentifierNameSyntax node:
                    VisitIdentifierName(node);
                    break;
                case LiteralExpressionSyntax node:
                    VisitLiteralExpression(node);
                    break;
                case BinaryExpressionSyntax node:
                    VisitBinaryExpression(node);
                    break;
                case PrefixUnaryExpressionSyntax node:
                    VisitPrefixUnaryExpression(node);
                    break;
                case PostfixUnaryExpressionSyntax node:
                    VisitPostfixUnaryExpression(node);
                    break;
                case MemberAccessExpressionSyntax node:
                    VisitMemberAccessExpression(node);
                    break;
                case AssignmentExpressionSyntax node:
                    VisitAssignmentExpression(node);
                    break;
                case ElementAccessExpressionSyntax node:
                    VisitElementAccessExpression(node);
                    break;
                case ArrayCreationExpressionSyntax node:
                    VisitArrayCreationExpression(node);
                    break;
                case ImplicitArrayCreationExpressionSyntax node:
                    VisitImplicitArrayCreationExpression(node);
                    break;
                case InitializerExpressionSyntax node:
                    VisitInitializerExpression(node);
                    break;
                case CastExpressionSyntax node:
                    VisitCastExpression(node);
                    break;
                case ParenthesizedExpressionSyntax node:
                    VisitParenthesizedExpression(node);
                    break;
                case PredefinedTypeSyntax node:
                    VisitPredefinedType(node);
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported expression: {expression.Kind()}");
            }
        }

        public override void VisitObjectCreationExpression(ObjectCreationExpressionSyntax node)
        {
            CheckResult argumentsCheckResult = node.ArgumentList.GetArguments().CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            if ((node.Initializer is {Expressions.Count: > 0}) && !_settings.AllowObjectInitializer)
                throw new UnsupportedSyntaxException("Forbidden object initializer");
            TypeSyntax type = node.Type;
            OperationResult<TypeResolveData> resolveResult = _externalEntityResolver.ResolveType(type);
            if (!resolveResult.Success)
                throw new UnsupportedSyntaxException(resolveResult.Reason);
            TypeResolveData data = resolveResult.Data!;
            // TODO (std_string) : i return empty type for system type because we need in additional analysis - think about approach
            if (String.IsNullOrEmpty(data.TypeName))
                throw new UnsupportedSyntaxException($"Unsupported type: {type}");
            ProcessTypeResolveData(data);
            ConvertedArguments arguments = ConvertArgumentList(CreateChildConverter(), node, node.ArgumentList.GetArguments());
            Buffer.Append($"({String.Join(", ", arguments.GetArguments(true))})");
            if (node.Initializer is {Expressions.Count: > 0})
                AfterResults.AddRange(ConvertObjectInitializerExpressions(node.Initializer.Expressions));
        }

        public override void VisitInvocationExpression(InvocationExpressionSyntax node)
        {
            CheckResult argumentsCheckResult = node.ArgumentList.GetArguments().CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            switch (node.Expression)
            {
                case MemberAccessExpressionSyntax memberAccessExpression:
                    VisitMemberAccessExpressionImpl(memberAccessExpression, node.ArgumentList);
                    break;
                case IdentifierNameSyntax identifierExpression:
                    throw new UnsupportedSyntaxException($"Unsupported call of method named {identifierExpression.Identifier.ValueText}");
                default:
                    throw new UnsupportedSyntaxException($"Unsupported invocation expression: {node.Expression.Kind()}");
            }
        }

        public override void VisitIdentifierName(IdentifierNameSyntax node)
        {
            SymbolInfo symbolInfo = _model.GetSymbolInfo(node);
            switch (symbolInfo.Symbol)
            {
                case null:
                    throw new UnsupportedSyntaxException($"Unrecognizable identifier: {node.Identifier}");
                case ILocalSymbol localSymbol:
                    Buffer.Append(_appData.NameTransformer.TransformLocalVariableName(localSymbol.Name));
                    break;
                case INamedTypeSymbol typeSymbol:
                    // TODO (std_string) ; think about ability of import rollback, e.g. in case of method from NUnit.Framework.Assert class
                    OperationResult<TypeResolveData> resolveResult = _externalEntityResolver.ResolveType(typeSymbol);
                    if (!resolveResult.Success)
                        throw new UnsupportedSyntaxException(resolveResult.Reason);
                    ProcessTypeResolveData(resolveResult.Data!);
                    break;
                case IPropertySymbol propertySymbol:
                    // TODO (std_string) : think about smart (not straightforward) solution
                    // TODO (std_string) : think about cases when property/method/etc in source type is absent in dest handmade type
                    String name = propertySymbol.Name;
                    String typeFullName = propertySymbol.ContainingType.GetTypeFullName();
                    if (!_appData.HandmadeManager.IsHandmadeType(typeFullName))
                        throw new UnsupportedSyntaxException($"Unsupported identifier with name = {node.Identifier} and kind = {node.Kind()}");
                    IDictionary<String, MappingData> mapping = _appData.HandmadeManager.GetHandmadeTypeMapping(typeFullName);
                    if (mapping.ContainsKey(name))
                    {
                        MappingData mappingData = mapping[name];
                        name = mappingData.Name;
                        if (mappingData.NeedImport)
                        {
                            String moduleName = _appData.HandmadeManager.CalcHandmadeTypeModuleName(typeFullName);
                            ImportData.AddEntity(moduleName, name);
                        }
                    }
                    Buffer.Append(name);
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported identifier with name = {node.Identifier} and kind = {node.Kind()}");
            }
        }

        public override void VisitLiteralExpression(LiteralExpressionSyntax node)
        {
            String text = node.Token.Value switch
            {
                null => node.Token.Text,
                Double value => value.ToString(CultureInfo.InvariantCulture),
                Single value => value.ToString(CultureInfo.InvariantCulture),
                Boolean value => value ? "True" : "False",
                // TODO (std_string) : there are problems with some unicode symbols - investigate their
                String _ when node.Token.Text.StartsWith('@') => $"\"\"{node.Token.Text.Substring(1)}\"\"",
                String => node.Token.Text,
                var value => value.ToString() ?? node.Token.Text
            };
            Buffer.Append(text);
        }

        public override void VisitBinaryExpression(BinaryExpressionSyntax node)
        {
            // TODO (std_string) : add check ability of applying binary expression for given arguments
            ExpressionConverter expressionConverter = CreateChildConverter();
            ConvertResult leftOperandResult = expressionConverter.Convert(node.Left);
            ImportData.Append(leftOperandResult.ImportData);
            ConvertResult rightOperandResult = expressionConverter.Convert(node.Right);
            ImportData.Append(rightOperandResult.ImportData);
            switch (node.Kind())
            {
                case SyntaxKind.AddExpression:
                    ProcessAddExpression(node, leftOperandResult.Result, rightOperandResult.Result);
                    break;
                case SyntaxKind.SubtractExpression:
                    Buffer.Append($"{leftOperandResult.Result} - {rightOperandResult.Result}");
                    break;
                case SyntaxKind.MultiplyExpression:
                    Buffer.Append($"{leftOperandResult.Result} * {rightOperandResult.Result}");
                    break;
                case SyntaxKind.DivideExpression:
                    // TODO (std_string) : we must check type of arguments for choosing between float divide (/) and integer divide (//) operators
                    Buffer.Append($"{leftOperandResult.Result} / {rightOperandResult.Result}");
                    break;
                case SyntaxKind.ModuloExpression:
                    Buffer.Append($"{leftOperandResult.Result} % {rightOperandResult.Result}");
                    break;
                case SyntaxKind.EqualsExpression:
                    Buffer.Append($"{leftOperandResult.Result} == {rightOperandResult.Result}");
                    break;
                case SyntaxKind.NotEqualsExpression:
                    Buffer.Append($"{leftOperandResult.Result} != {rightOperandResult.Result}");
                    break;
                case SyntaxKind.LessThanExpression:
                    Buffer.Append($"{leftOperandResult.Result} < {rightOperandResult.Result}");
                    break;
                case SyntaxKind.LessThanOrEqualExpression:
                    Buffer.Append($"{leftOperandResult.Result} <= {rightOperandResult.Result}");
                    break;
                case SyntaxKind.GreaterThanExpression:
                    Buffer.Append($"{leftOperandResult.Result} > {rightOperandResult.Result}");
                    break;
                case SyntaxKind.GreaterThanOrEqualExpression:
                    Buffer.Append($"{leftOperandResult.Result} >= {rightOperandResult.Result}");
                    break;
                case SyntaxKind.BitwiseAndExpression:
                    Buffer.Append($"{leftOperandResult.Result} & {rightOperandResult.Result}");
                    break;
                case SyntaxKind.BitwiseOrExpression:
                    Buffer.Append($"{leftOperandResult.Result} | {rightOperandResult.Result}");
                    break;
                case SyntaxKind.LogicalAndExpression:
                    Buffer.Append($"{leftOperandResult.Result} and {rightOperandResult.Result}");
                    break;
                case SyntaxKind.LogicalOrExpression:
                    Buffer.Append($"{leftOperandResult.Result} or {rightOperandResult.Result}");
                    break;
                case SyntaxKind.AsExpression:
                    switch (node.Right)
                    {
                        case TypeSyntax typeSyntax:
                            switch (_externalEntityResolver.ResolveCast(typeSyntax, node.Left, leftOperandResult.Result))
                            {
                                case {Success: false, Reason: var reason}:
                                    throw new UnsupportedSyntaxException($"Bad binary as expression due to: {reason}");
                                case {Success: true, Data: var resolveData}:
                                    Buffer.Append(resolveData!.Cast);
                                    ImportData.AddImport(resolveData.ModuleName);
                                    break;
                                default:
                                    throw new UnsupportedSyntaxException($"Unexpected control flow at binary as expression: {node}");
                            }
                            break;
                        default:
                            throw new UnsupportedSyntaxException($"Unsupported binary as expression: {node}");
                    }
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported binary expression: {node.Kind()}");
            }
        }

        private void ProcessAddExpression(BinaryExpressionSyntax node, String leftOperand, String rightOperand)
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
                            Buffer.Append($"{leftOperand} + {rightOperand}");
                            break;
                        case ("System.String", _):
                            Buffer.Append($"{leftOperand} + str({rightOperand})");
                            break;
                        case (_, "System.String"):
                            Buffer.Append($"str({leftOperand}) + {rightOperand}");
                            break;
                        default:
                            throw new UnsupportedSyntaxException($"Unsupported binary expression: node");
                    }
                    break;
                default:
                    Buffer.Append($"{leftOperand} + {rightOperand}");
                    break;
            }
        }

        public override void VisitPrefixUnaryExpression(PrefixUnaryExpressionSyntax node)
        {
            ExpressionConverter expressionConverter = CreateChildConverter();
            ConvertResult operandResult = expressionConverter.Convert(node.Operand);
            ImportData.Append(operandResult.ImportData);
            switch (node.Kind())
            {
                case SyntaxKind.UnaryPlusExpression:
                    Buffer.Append($"+{operandResult.Result}");
                    break;
                case SyntaxKind.UnaryMinusExpression:
                    Buffer.Append($"-{operandResult.Result}");
                    break;
                case SyntaxKind.LogicalNotExpression:
                    Buffer.Append($"not {operandResult.Result}");
                    break;
                case SyntaxKind.PreIncrementExpression when _settings.AllowIncrementDecrement:
                    Buffer.Append($"{operandResult.Result} += 1");
                    break;
                case SyntaxKind.PreDecrementExpression when _settings.AllowIncrementDecrement:
                    Buffer.Append($"{operandResult.Result} -= 1");
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported PrefixUnaryExpressionSyntax expression: {node.Kind()}");
            }
        }

        public override void VisitPostfixUnaryExpression(PostfixUnaryExpressionSyntax node)
        {
            ExpressionConverter expressionConverter = CreateChildConverter();
            ConvertResult operandResult = expressionConverter.Convert(node.Operand);
            ImportData.Append(operandResult.ImportData);
            switch (node.Kind())
            {
                case SyntaxKind.PostIncrementExpression when _settings.AllowIncrementDecrement:
                    Buffer.Append($"{operandResult.Result} += 1");
                    break;
                case SyntaxKind.PostDecrementExpression when _settings.AllowIncrementDecrement:
                    Buffer.Append($"{operandResult.Result} -= 1");
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported PostfixUnaryExpressionSyntax expression: {node.Kind()}");
            }
        }

        public override void VisitMemberAccessExpression(MemberAccessExpressionSyntax node)
        {
            VisitMemberAccessExpressionImpl(node, null);
        }

        public override void VisitAssignmentExpression(AssignmentExpressionSyntax node)
        {
            switch (node.Kind())
            {
                case SyntaxKind.SimpleAssignmentExpression:
                {
                    ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData, CreateChildSetting());
                    ConvertResult leftAssignmentResult = expressionConverter.Convert(node.Left);
                    ImportData.Append(leftAssignmentResult.ImportData);
                    ConvertResult rightAssignmentResult = expressionConverter.Convert(node.Right);
                    ImportData.Append(rightAssignmentResult.ImportData);
                    Buffer.Append($"{leftAssignmentResult.Result} = {rightAssignmentResult.Result}");
                    break;
                }
                default:
                    throw new UnsupportedSyntaxException($"Unsupported assignment expression: {node.Kind()}");
            }
        }

        public override void VisitElementAccessExpression(ElementAccessExpressionSyntax node)
        {
            ElementAccessExpressionConverter converter = new ElementAccessExpressionConverter(_model, _appData, CreateChildSetting());
            AppendResult(converter.Convert(node));
        }

        public override void VisitArrayCreationExpression(ArrayCreationExpressionSyntax node)
        {
            ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData, CreateChildSetting());
            AppendResult(converter.Convert(node));
        }

        public override void VisitImplicitArrayCreationExpression(ImplicitArrayCreationExpressionSyntax node)
        {
            ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData, CreateChildSetting());
            AppendResult(converter.Convert(node));
        }

        public override void VisitInitializerExpression(InitializerExpressionSyntax node)
        {
            switch (node.Kind())
            {
                case SyntaxKind.ArrayInitializerExpression:
                    ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData, CreateChildSetting());
                    AppendResult(converter.Convert(node));
                    break;
                default:
                    throw new UnsupportedSyntaxException($"Unsupported initializer expression: {node.Kind()}");
            }
        }

        public override void VisitCastExpression(CastExpressionSyntax node)
        {
            ExpressionConverter expressionConverter = CreateChildConverter();
            String sourceRepresentation = ConvertExpression(expressionConverter, node.Expression);
            OperationResult<CastResolveData> resolveResult = _externalEntityResolver.ResolveCast(node.Type, node.Expression, sourceRepresentation);
            if (!resolveResult.Success)
                throw new UnsupportedSyntaxException(resolveResult.Reason);
            CastResolveData castResolveData = resolveResult.Data!;
            Buffer.Append(castResolveData.Cast);
            ImportData.AddImport(castResolveData.ModuleName);
        }

        public override void VisitParenthesizedExpression(ParenthesizedExpressionSyntax node)
        {
            ExpressionConverter expressionConverter = CreateChildConverter();
            ConvertResult innerResult = expressionConverter.Convert(node.Expression);
            Buffer.Append($"({innerResult.Result})");
            ImportData.Append(innerResult.ImportData);
        }

        public override void VisitPredefinedType(PredefinedTypeSyntax node)
        {
            throw new UnsupportedSyntaxException($"Usage of predefined type {node.Keyword} is unsupported");
        }

        private void VisitMemberAccessExpressionImpl(MemberAccessExpressionSyntax node, ArgumentListSyntax? argumentList)
        {
            ExpressionConverter expressionConverter = CreateChildConverter();
            ConvertedArguments arguments = ConvertArgumentList(expressionConverter, node, argumentList.GetArguments());
            ExpressionSyntax target = node.Expression;
            SymbolInfo targetInfo = _model.GetSymbolInfo(target);
            switch (targetInfo.Symbol)
            {
                // TODO (std_string) : for some types of expression we receive null, but this is not error of recognition. Think about this
                case INamespaceSymbol:
                    Visit(node.Name);
                    break;
                default:
                    String targetDest = ConvertExpression(expressionConverter, target);
                    SimpleNameSyntax name = node.Name;
                    MemberData memberData = new MemberData(target, name, argumentList.GetArguments());
                    MemberRepresentation memberRepresentation = new MemberRepresentation(targetDest, arguments);
                    OperationResult<MemberResolveData> resolveResult = _externalEntityResolver.ResolveMember(memberData, memberRepresentation);
                    if (!resolveResult.Success)
                        throw new UnsupportedSyntaxException(resolveResult.Reason);
                    MemberResolveData memberResolveData = resolveResult.Data!;
                    Buffer.Append(memberResolveData.Member);
                    ImportData.AddImport(memberResolveData.ModuleName);
                    break;
            }
        }

        private IList<String> ConvertObjectInitializerExpressions(IReadOnlyList<ExpressionSyntax> initializerExpressions)
        {
            ExpressionConverter converter = new ExpressionConverter(_model, _appData, _settings);
            IList<String> destExpressions = new List<String>();
            // TODO (std_string) : this is simple approach. Think about smarter one
            foreach (ExpressionSyntax expression in initializerExpressions)
            {
                switch (expression)
                {
                    case AssignmentExpressionSyntax {Left: IdentifierNameSyntax identifier} expr when expr.Kind() == SyntaxKind.SimpleAssignmentExpression:
                        // TODO (std_string) : check identifier: is this field, property or something else
                        OperationResult<ITypeSymbol> expressionType = identifier.GetExpressionTypeSymbol(_model);
                        if (!expressionType.Success)
                            throw new UnsupportedSyntaxException($"Unsupported object initializer expression: {expressionType.Reason}");
                        String sourceTypeFullName = expressionType.Data!.GetTypeFullName();
                        String name = _appData.NameTransformer.TransformPropertyName(sourceTypeFullName, identifier.Identifier.Text);
                        ConvertResult expressionResult = converter.Convert(expr.Right);
                        ImportData.Append(expressionResult.ImportData);
                        destExpressions.Add($"{name} = {expressionResult.Result}");
                        foreach (String child in expressionResult.AfterResults)
                            destExpressions.Add($"{name}.{child}");
                        break;
                    default:
                        throw new UnsupportedSyntaxException($"Unsupported object initializer expression: {expression}");
                }
            }
            return destExpressions;
        }

        // TODO (std_string) : move into separate converter
        private ConvertedArguments ConvertArgumentList(ExpressionConverter expressionConverter, ExpressionSyntax source, IReadOnlyList<ArgumentSyntax> arguments)
        {
            Boolean IsOverloadedMember(IMethodSymbol methodSymbol)
            {
                IMethodSymbol[] methods = methodSymbol.ContainingType.GetMembers(methodSymbol.Name).OfType<IMethodSymbol>().ToArray();
                return methods switch
                {
                    {Length: 1} => false,
                    {Length: 2} when methods.Any(method => method.Parameters.Length == 0) => false,
                    _ => true
                };
            }
            String? GetArgumentName(Boolean useNamedArguments, ArgumentSyntax argument, IParameterSymbol parameter)
            {
                if (!useNamedArguments)
                    return null;
                return argument.NameColon switch
                {
                    null => _appData.NameTransformer.TransformLocalVariableName(parameter.Name),
                    var nameColon => _appData.NameTransformer.TransformLocalVariableName(nameColon.Name.ToString())
                };
            }
            (String value, String? namedValue) ProcessUsualArgument(Boolean useNamedArguments, ArgumentSyntax argument, IParameterSymbol parameter)
            {
                String argumentValue = ConvertExpression(expressionConverter, argument.Expression);
                return GetArgumentName(useNamedArguments, argument, parameter) switch
                {
                    null => (value: argumentValue, namedValue: null),
                    var name => (value: argumentValue, namedValue: $"{name} = {argumentValue}")
                };
            }
            String ProcessParamsArgumentValue(Int32 startIndex)
            {
                Int32 paramsSize = arguments.Count - startIndex;
                String[] paramsValues = new String[paramsSize];
                for (Int32 index = 0; index < paramsSize; ++index)
                    paramsValues[index] = ConvertExpression(expressionConverter, arguments[startIndex + index].Expression);
                switch (paramsSize)
                {
                    case 1:
                        TypeInfo lastArgumentInfo = _model.GetTypeInfo(arguments[^1].Expression);
                        switch (lastArgumentInfo.Type)
                        {
                            case null:
                                throw new UnsupportedSyntaxException("Unrecognizable params argument");
                            case IArrayTypeSymbol:
                                return paramsValues[0];
                            default:
                                return $"[{String.Join(", ", paramsValues)}]";
                        }
                    default:
                        return $"[{String.Join(", ", paramsValues)}]";
                }
            }
            (String value, String? namedValue) ProcessParamsArgument(Boolean useNamedArguments, Int32 startIndex, IParameterSymbol parameter)
            {
                String argumentValue = ProcessParamsArgumentValue(startIndex);
                return GetArgumentName(useNamedArguments, arguments[^1], parameter) switch
                {
                    null => (value: argumentValue, namedValue: null),
                    var name => (value: argumentValue, namedValue: $"{name} = {argumentValue}")
                };
            }
            if (arguments.Count == 0)
                return new ConvertedArguments(Array.Empty<String>(), null);
            OperationResult<IMethodSymbol> methodSymbol = source.GetMethodSymbol(_model);
            if (!methodSymbol.Success)
                throw new UnsupportedSyntaxException(methodSymbol.Reason);
            IReadOnlyList<IParameterSymbol> parameters = methodSymbol.Data!.Parameters;
            Boolean useNamedArguments = (arguments[^1].NameColon is not null) || IsOverloadedMember(methodSymbol.Data);
            Boolean hasParamsArguments = (parameters[^1].IsParams) && (arguments.Count >= parameters.Count);
            Int32 destCount = Math.Min(parameters.Count, arguments.Count);
            String[] destArguments = new String[destCount];
            String[]? destNamedArguments = useNamedArguments ? new String[destCount] : null;
            Int32 usualArgumentCount = arguments.Count < parameters.Count ? arguments.Count : parameters.Count;
            if (hasParamsArguments)
                --usualArgumentCount;
            for (Int32 index = 0; index < usualArgumentCount; ++index)
            {
                (String value, String? namedValue) argument = ProcessUsualArgument(useNamedArguments, arguments[index], parameters[index]);
                destArguments[index] = argument.value;
                if (destNamedArguments != null)
                    destNamedArguments[index] = argument.namedValue!;
            }
            if (hasParamsArguments)
            {
                (String value, String? namedValue) argument = ProcessParamsArgument(useNamedArguments, usualArgumentCount, parameters[^1]);
                destArguments[^1] = argument.value;
                if (destNamedArguments != null)
                    destNamedArguments[^1] = argument.namedValue!;
            }
            return new ConvertedArguments(destArguments, destNamedArguments);
        }

        private String ConvertExpression(ExpressionConverter expressionConverter, ExpressionSyntax expression)
        {
            ConvertResult result = expressionConverter.Convert(expression);
            ImportData.Append(result.ImportData);
            return result.Result;
        }

        private void ProcessTypeResolveData(TypeResolveData resolveData)
        {
            Buffer.Append($"{resolveData.ModuleName}.{resolveData.TypeName}");
            ImportData.AddImport(resolveData.ModuleName);
        }

        private void AppendResult(ConvertResult result)
        {
            Buffer.Append(result.Result);
            ImportData.Append(result.ImportData);
        }

        // TODO (std_string) : think about location
        private Boolean ProcessPredefinedExpressions(ExpressionSyntax expression)
        {
            String expressionRepresentation = expression.ToString();
            switch (expressionRepresentation)
            {
                case "double.NaN":
                    Buffer.Append("math.nan");
                    ImportData.AddImport("math");
                    return true;
                case "double.MaxValue":
                    Buffer.Append("1.7976931348623157E+308");
                    return true;
                case "double.MinValue":
                    Buffer.Append("-1.7976931348623157E+308");
                    return true;
                case "string.Empty":
                    Buffer.Append("\"\"");
                    return true;
                case "null":
                    Buffer.Append("None");
                    return true;
            }
            return false;
        }

        private ExpressionConverterSettings CreateChildSetting()
        {
            return new ExpressionConverterSettings(_settings)
            {
                AllowIncrementDecrement = false,
                AllowObjectInitializer = false
            };
        }

        private ExpressionConverter CreateChildConverter()
        {
            return new ExpressionConverter(_model, _appData, CreateChildSetting());
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExternalEntityResolver _externalEntityResolver;
        private readonly ExpressionConverterSettings _settings;
    }
}
