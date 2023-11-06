using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Expressions
{
    internal record TypeResolveData(String TypeName, String ModuleName);

    internal record MemberData(ExpressionSyntax Target, SimpleNameSyntax Name, IReadOnlyList<ArgumentSyntax> Arguments);

    internal record MemberRepresentation(String Target, String[] Arguments);

    internal record MemberResolveData(String Member, String ModuleName);

    internal record CastResolveData(String Cast, String ModuleName);

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

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            OperationResult<ITypeSymbol> targetTypeResult = ExtractExpressionType(data.Target);
            if (!targetTypeResult.Success)
                return new OperationResult<MemberResolveData>(false, targetTypeResult.Reason);
            ITypeSymbol sourceType = targetTypeResult.Data!;
            IList<ResolveMemberHandler> handlers = new List<ResolveMemberHandler>
            {
                ResolveMemberForKnownNamespace,
                ResolveMemberForNUnit,
                ResolveMemberCallForSystem
            };
            foreach (ResolveMemberHandler handler in handlers)
            {
                OperationResult<MemberResolveData> result = handler(data, sourceType, representation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported target type {sourceType.GetTypeFullName()}");
        }

        public OperationResult<CastResolveData> ResolveCast(TypeSyntax castType, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            OperationResult<ITypeSymbol> targetTypeResult = ExtractExpressionType(castType);
            if (!targetTypeResult.Success)
                return new OperationResult<CastResolveData>(false, targetTypeResult.Reason);
            ITypeSymbol castTypeSymbol = targetTypeResult.Data!;
            IList<ResolveCastHandler> handlers = new List<ResolveCastHandler>
            {
                ResolveCastForKnownNamespace,
                ResolveCastForSystem
            };
            foreach (ResolveCastHandler handler in handlers)
            {
                OperationResult<CastResolveData> result = handler(castTypeSymbol, sourceExpression, sourceRepresentation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<CastResolveData>(false, $"Unsupported cast to type {castType}");
        }

        private delegate OperationResult<MemberResolveData> ResolveMemberHandler(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation);

        private delegate OperationResult<CastResolveData> ResolveCastHandler(ITypeSymbol castTypeSymbol, ExpressionSyntax sourceExpression, String sourceRepresentation);

        private OperationResult<MemberResolveData> ResolveMemberForKnownNamespace(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<MemberResolveData>(false, $"Unsupported type: {sourceTypeFullName}");
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = ModelExtensions.GetSymbolInfo(_model, name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unrecognizable member {name.Identifier} for type {sourceTypeFullName}");
                // TODO (std_string) : think about separation between methods, properties and fields
                case IMethodSymbol methodSymbol:
                {
                    String methodName = NameTransformer.TransformMethodName(methodSymbol.Name);
                    String args = String.Join(", ", representation.Arguments);
                    String methodCall = String.Concat(representation.Target, ".", methodName, "(", args, ")");
                    MemberResolveData resolveData = new MemberResolveData(methodCall, "");
                    return new OperationResult<MemberResolveData>(true, "", resolveData);
                }
                case IPropertySymbol propertySymbol:
                {
                    String propertyName = NameTransformer.TransformPropertyName(propertySymbol.Name);
                    String propertyCall = $"{representation.Target}.{propertyName}";
                    MemberResolveData resolveData = new MemberResolveData(propertyCall, "");
                    return new OperationResult<MemberResolveData>(true, "", resolveData);
                }
                case IFieldSymbol fieldSymbol:
                {
                    String fieldName = fieldSymbol.Type.TypeKind switch
                    {
                        TypeKind.Enum => NameTransformer.TransformEnumValueName(fieldSymbol.Name),
                        _ => NameTransformer.TransformFieldName(fieldSymbol.Name)
                    };
                    String fieldCall = $"{representation.Target}.{fieldName}";
                    MemberResolveData resolveData = new MemberResolveData(fieldCall, "");
                    return new OperationResult<MemberResolveData>(true, "", resolveData);
                }
                default:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member {name.Identifier} for type {sourceTypeFullName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveMemberForNUnit(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            OperationResult<MemberResolveData> GenerateAssertEqual(String arg0, String arg1, String? message = null)
            {
                String messagePart = message == null ? "" : $", msg={message}";
                String methodCall = $"self.assertEqual({arg0}, {arg1}{messagePart})";
                MemberResolveData resolveData = new MemberResolveData(methodCall, "unittest");
                return new OperationResult<MemberResolveData>(true, "", resolveData);
            }
            OperationResult<MemberResolveData> GenerateAssertAlmostEqual(String arg0, String arg1, String delta)
            {
                String methodCall = $"self.assertAlmostEqual({arg0}, {arg1}, delta={delta})";
                MemberResolveData resolveData = new MemberResolveData(methodCall, "unittest");
                return new OperationResult<MemberResolveData>(true, "", resolveData);
            }
            OperationResult<MemberResolveData> ResolveAssertEqual()
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
                                return GenerateAssertAlmostEqual(representation.Arguments[0], representation.Arguments[1], literalExpression.Token.ValueText);
                            case IdentifierNameSyntax identifier:
                                SymbolInfo identifierInfo = ModelExtensions.GetSymbolInfo(_model, identifier);
                                switch (identifierInfo.Symbol)
                                {
                                    case null:
                                        return new OperationResult<MemberResolveData>(false, $"Unrecognizable third argument in Assert.AreEqual: {identifier.Identifier}");
                                    case ILocalSymbol localSymbol when localSymbol.Type.GetTypeFullName() == "System.String":
                                        return GenerateAssertEqual(representation.Arguments[0], representation.Arguments[1], identifierInfo.Symbol.Name);
                                    case ILocalSymbol localSymbol when localSymbol.Type.GetTypeFullName() == "System.Single":
                                        return GenerateAssertAlmostEqual(representation.Arguments[0], representation.Arguments[1], identifierInfo.Symbol.Name);
                                    case ILocalSymbol localSymbol when localSymbol.Type.GetTypeFullName() == "System.Double":
                                        return GenerateAssertAlmostEqual(representation.Arguments[0], representation.Arguments[1], identifierInfo.Symbol.Name);
                                    }
                                return new OperationResult<MemberResolveData>(false, $"Unsupported third argument in Assert.AreEqual: {identifier.Identifier}");
                            }
                        return new OperationResult<MemberResolveData>(false, $"Unsupported third argument kind in Assert.AreEqual: {lastArgument.Kind()}");
                    }
                    default:
                        return new OperationResult<MemberResolveData>(false, $"Unsupported arguments count in Assert.AreEqual: {data.Arguments.Count}");
                }
            }
            String sourceTypeFullName = sourceType.GetTypeFullName();
            if (!sourceTypeFullName.Equals("NUnit.Framework.Assert"))
                return new OperationResult<MemberResolveData>(false, $"Unsupported type {sourceTypeFullName}");
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = ModelExtensions.GetSymbolInfo(_model, name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unrecognizable member {name.Identifier} for type {sourceTypeFullName}");
                case IMethodSymbol{Name: "AreEqual"}:
                    return ResolveAssertEqual();
                default:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member {name.Identifier} for type {sourceTypeFullName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveMemberCallForSystem(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            return new OperationResult<MemberResolveData>(false, "ResolveMemberCallForSystem: Not Implemented");
        }

        public OperationResult<CastResolveData> ResolveCastForKnownNamespace(ITypeSymbol castTypeSymbol, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            String sourceTypeFullName = castTypeSymbol.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<CastResolveData>(false, $"Unsupported type: {sourceTypeFullName}");
            // TODO (std_string) : think about check existing corresponding cast method in sourceExpression
            String castMethod = NameTransformer.TransformMethodName($"As{castTypeSymbol.Name}");
            CastResolveData castResolveData = new CastResolveData($"{sourceRepresentation}.{castMethod}()", "");
            return new OperationResult<CastResolveData>(true, String.Empty, castResolveData);
        }

        public OperationResult<CastResolveData> ResolveCastForSystem(ITypeSymbol castTypeSymbol, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            throw new NotImplementedException();
        }

        // TODO (std_string) : think about separation for members, cast etc
        private OperationResult<ITypeSymbol> ExtractExpressionType(ExpressionSyntax target)
        {
            return target.GetExpressionTypeSymbol(_model) switch
            {
                {Success: false, Reason: var reason} => new OperationResult<ITypeSymbol>(false, reason),
                {Success: true, Data: IArrayTypeSymbol type} => new OperationResult<ITypeSymbol>(false, $"Unsupported member target type - {type.ElementType.GetTypeFullName()}[] for expression: {target}"),
                {Success: true, Data: var type} => new OperationResult<ITypeSymbol>(true, "", type)
            };
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}