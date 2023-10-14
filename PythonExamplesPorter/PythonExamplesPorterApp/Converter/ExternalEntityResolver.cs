using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterApp.Converter
{
    internal record TypeResolveData(String TypeName, String ModuleName);

    internal record MethodData(ExpressionSyntax Target, SimpleNameSyntax Name, IReadOnlyList<ArgumentSyntax> Arguments);

    internal record MethodRepresentation(String Target, String[] Arguments);

    internal record MethodCallResolveData(String Call, String ModuleName);

    // TODO (std_string) : we must implement this functionality via Strategy pattern
    internal class ExternalEntityResolver
    {
        public ExternalEntityResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public OperationResult<TypeResolveData> ResolveType(TypeSyntax type)
        {
            SymbolInfo symbolInfo = ModelExtensions.GetSymbolInfo(_model, type);
            ISymbol? typeInfo = symbolInfo.Symbol;
            if (typeInfo == null)
                return new OperationResult<TypeResolveData>(false, $"Unrecognizable type: {type}");
            return typeInfo switch
            {
                INamedTypeSymbol typeSymbol => ResolveType(typeSymbol),
                _ => new OperationResult<TypeResolveData>(false, $"Unsupported {typeInfo.Kind} kind of symbol info for {type}")
            };
        }

        public OperationResult<TypeResolveData> ResolveType(INamedTypeSymbol typeSymbol)
        {
            String sourceNamespaceName = typeSymbol.ContainingNamespace.ToDisplayString();
            String sourceTypeName = typeSymbol.Name;
            String[] systemNamespaces = {"System", "NUnit.Framework"};
            Boolean isSystemType = systemNamespaces.Any(sourceNamespaceName.StartsWith);
            if (isSystemType)
                // TODO (std_string) : i return empty type for system type because we need in additional analysis - think about approach
                return new OperationResult<TypeResolveData>(true, "", new TypeResolveData("", ""));
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceNamespaceName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<TypeResolveData>(false, $"Unsupported type: {sourceNamespaceName}.{sourceTypeName}");
            String destModuleName = NameTransformer.TransformNamespaceName(sourceNamespaceName);
            String destTypeName = NameTransformer.TransformClassName(sourceTypeName);
            return new OperationResult<TypeResolveData>(true, "", new TypeResolveData(destTypeName, destModuleName));
        }

        public OperationResult<MethodCallResolveData> ResolveMethodCall(MethodData data, MethodRepresentation representation)
        {
            OperationResult<SourceType> targetTypeResult = ExtractMethodTargetType(data.Target);
            if (!targetTypeResult.Success)
                return new OperationResult<MethodCallResolveData>(false, targetTypeResult.Reason);
            SourceType sourceType = targetTypeResult.Data!;
            IList<ResolveMethodCallHandler> handlers = new List<ResolveMethodCallHandler>
            {
                ResolveMethodCallForKnownNamespace,
                ResolveMethodCallForNUnit,
                ResolveMethodCallForSystem
            };
            foreach (ResolveMethodCallHandler handler in handlers)
            {
                OperationResult<MethodCallResolveData> result = handler(data, sourceType, representation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<MethodCallResolveData>(false, $"Unsupported target type \"{sourceType.FullName}\"");
        }

        private delegate OperationResult<MethodCallResolveData> ResolveMethodCallHandler(MethodData data, SourceType sourceType, MethodRepresentation representation);

        private OperationResult<SourceType> ExtractMethodTargetType(ExpressionSyntax target)
        {
            return ExtractMethodTargetType(target, ModelExtensions.GetSymbolInfo(_model, target).Symbol);
        }

        private OperationResult<SourceType> ExtractMethodTargetType(ExpressionSyntax target, ISymbol? targetSymbol)
        {
            return targetSymbol switch
            {
                null => new OperationResult<SourceType>(false, $"Unrecognizable method target type for \"{target}\""),
                ILocalSymbol localSymbol => ExtractMethodTargetType(target, localSymbol.Type),
                INamedTypeSymbol typeSymbol => new OperationResult<SourceType>(true, "", new SourceType(typeSymbol)),
                IPropertySymbol propertySymbol => new OperationResult<SourceType>(true, "", new SourceType(propertySymbol.ContainingType)),
                _ => new OperationResult<SourceType>(false, $"Unsupported method target type for \"{target}\"")
            };
        }

        private OperationResult<MethodCallResolveData> ResolveMethodCallForKnownNamespace(MethodData data, SourceType sourceType, MethodRepresentation representation)
        {
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceType.NamespaceName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<MethodCallResolveData>(false, $"Unsupported type: {sourceType.FullName}");
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = ModelExtensions.GetSymbolInfo(_model, name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MethodCallResolveData>(false, $"Unrecognizable method \"{name.Identifier}\" for type \"{sourceType.FullName}\"");
                // TODO (std_string) : think about separation between methods, properties and fields
                case IMethodSymbol methodSymbol:
                {
                    String methodName = NameTransformer.TransformMethodName(methodSymbol.Name);
                    String args = String.Join(", ", representation.Arguments);
                    String methodCall = String.Concat(representation.Target, ".", methodName, "(", args, ")");
                    MethodCallResolveData resolveData = new MethodCallResolveData(methodCall, "");
                    return new OperationResult<MethodCallResolveData>(true, "", resolveData);
                }
                case IPropertySymbol propertySymbol:
                {
                    String propertyName = NameTransformer.TransformMethodName(propertySymbol.Name);
                    String propertyCall = $"{representation.Target}.{propertyName}";
                    MethodCallResolveData resolveData = new MethodCallResolveData(propertyCall, "");
                    return new OperationResult<MethodCallResolveData>(true, "", resolveData);
                }
                case IFieldSymbol fieldSymbol:
                {
                    String fieldName = fieldSymbol.Type.TypeKind switch
                    {
                        TypeKind.Enum => NameTransformer.TransformEnumValueName(fieldSymbol.Name),
                        _ => NameTransformer.TransformFieldName(fieldSymbol.Name)
                    };
                    String fieldCall = $"{representation.Target}.{fieldName}";
                    MethodCallResolveData resolveData = new MethodCallResolveData(fieldCall, "");
                    return new OperationResult<MethodCallResolveData>(true, "", resolveData);
                }
                default:
                    return new OperationResult<MethodCallResolveData>(false, $"Unsupported method \"{name.Identifier}\" for type \"{sourceType.FullName}\"");
            }
        }

        private OperationResult<MethodCallResolveData> ResolveMethodCallForNUnit(MethodData data, SourceType sourceType, MethodRepresentation representation)
        {
            OperationResult<MethodCallResolveData> GenerateAssertEqual(String arg0, String arg1, String? message = null)
            {
                String messagePart = message == null ? "" : $", msg={message}";
                String methodCall = $"self.assertEqual({arg0}, {arg1}{messagePart})";
                MethodCallResolveData resolveData = new MethodCallResolveData(methodCall, "unittest");
                return new OperationResult<MethodCallResolveData>(true, "", resolveData);
            }
            OperationResult<MethodCallResolveData> GenerateAssertAlmostEqual(String arg0, String arg1, String delta)
            {
                String methodCall = $"self.assertAlmostEqual({arg0}, {arg1}, delta={delta})";
                MethodCallResolveData resolveData = new MethodCallResolveData(methodCall, "unittest");
                return new OperationResult<MethodCallResolveData>(true, "", resolveData);
            }
            OperationResult<MethodCallResolveData> ResolveAssertEqual()
            {
                switch (data.Arguments.Count)
                {
                    case 2:
                        return GenerateAssertEqual(representation.Arguments[0], representation.Arguments[1]);
                    case 3:
                    {
                        ExpressionSyntax lastArgument = data.Arguments.Last().Expression;
                        switch (lastArgument)
                        {
                            case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.StringLiteralExpression:
                                return GenerateAssertEqual(representation.Arguments[0], representation.Arguments[1], literalExpression.Token.Text);
                            case LiteralExpressionSyntax literalExpression when literalExpression.Kind() == SyntaxKind.NumericLiteralExpression:
                                return GenerateAssertAlmostEqual(representation.Arguments[0], representation.Arguments[1], literalExpression.Token.Text);
                            case IdentifierNameSyntax identifier:
                                SymbolInfo identifierInfo = ModelExtensions.GetSymbolInfo(_model, identifier);
                                switch (identifierInfo.Symbol)
                                {
                                    case null:
                                        return new OperationResult<MethodCallResolveData>(false, $"Unrecognizable third argument in Assert.AreEqual: {identifier.Identifier}");
                                    case ILocalSymbol localSymbol when localSymbol.Type.GetTypeFullName() == "System.String":
                                        return GenerateAssertEqual(representation.Arguments[0], representation.Arguments[1], identifierInfo.Symbol.Name);
                                    case ILocalSymbol localSymbol when localSymbol.Type.GetTypeFullName() == "System.Single":
                                        return GenerateAssertAlmostEqual(representation.Arguments[0], representation.Arguments[1], identifierInfo.Symbol.Name);
                                    case ILocalSymbol localSymbol when localSymbol.Type.GetTypeFullName() == "System.Double":
                                        return GenerateAssertAlmostEqual(representation.Arguments[0], representation.Arguments[1], identifierInfo.Symbol.Name);
                                    }
                                return new OperationResult<MethodCallResolveData>(false, $"Unsupported third argument in Assert.AreEqual: {identifier.Identifier}");
                            }
                        return new OperationResult<MethodCallResolveData>(false, $"Unsupported third argument kind in Assert.AreEqual: {lastArgument.Kind()}");
                    }
                    default:
                        return new OperationResult<MethodCallResolveData>(false, $"Unsupported arguments count in Assert.AreEqual: {data.Arguments.Count}");
                }
            }
            if (!sourceType.FullName.Equals("NUnit.Framework.Assert"))
                return new OperationResult<MethodCallResolveData>(false, $"Unsupported type \"{sourceType.FullName}\"");
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = ModelExtensions.GetSymbolInfo(_model, name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MethodCallResolveData>(false, $"Unrecognizable method \"{name.Identifier}\" for type \"{sourceType.FullName}\"");
                case IMethodSymbol{Name: "AreEqual"}:
                    return ResolveAssertEqual();
                default:
                    return new OperationResult<MethodCallResolveData>(false, $"Unsupported method \"{name.Identifier}\" for type \"{sourceType.FullName}\"");
            }
        }

        private OperationResult<MethodCallResolveData> ResolveMethodCallForSystem(MethodData data, SourceType sourceType, MethodRepresentation representation)
        {
            return new OperationResult<MethodCallResolveData>(false, $"ResolveMethodCallForSystem: Not Implemented");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}