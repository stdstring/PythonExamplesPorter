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

    internal record MemberRepresentation(String Target, ConvertedArguments Arguments);

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
            SymbolInfo symbolInfo = _model.GetSymbolInfo(type);
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
            String destModuleName = _appData.NameTransformer.TransformNamespaceName(sourceNamespaceName);
            String destTypeName = _appData.NameTransformer.TransformTypeName(sourceTypeName);
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

        public OperationResult<CastResolveData> ResolveCast(ITypeSymbol castType, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            IList<ResolveCastHandler> handlers = new List<ResolveCastHandler>
            {
                ResolveCastForKnownNamespace,
                ResolveCastForSystem
            };
            foreach (ResolveCastHandler handler in handlers)
            {
                OperationResult<CastResolveData> result = handler(castType, sourceExpression, sourceRepresentation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<CastResolveData>(false, $"Unsupported cast to type {castType.GetTypeFullName()}");
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
                    String methodName = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, methodSymbol.Name);
                    String args = String.Join(", ", representation.Arguments.GetArguments(true));
                    String methodCall = String.Concat(representation.Target, ".", methodName, "(", args, ")");
                    MemberResolveData resolveData = new MemberResolveData(methodCall, "");
                    return new OperationResult<MemberResolveData>(true, "", resolveData);
                }
                case IPropertySymbol propertySymbol:
                {
                    String propertyName = _appData.NameTransformer.TransformPropertyName(sourceTypeFullName, propertySymbol.Name);
                    String propertyCall = $"{representation.Target}.{propertyName}";
                    MemberResolveData resolveData = new MemberResolveData(propertyCall, "");
                    return new OperationResult<MemberResolveData>(true, "", resolveData);
                }
                case IFieldSymbol{IsStatic: var isStatic, IsReadOnly: var isReadOnly, Type.TypeKind: var typeKind} fieldSymbol:
                {
                    String fieldName = typeKind switch
                    {
                        TypeKind.Enum => _appData.NameTransformer.TransformEnumValueName(sourceTypeFullName, fieldSymbol.Name),
                        _ when isStatic && isReadOnly => _appData.NameTransformer.TransformStaticReadonlyFieldName(sourceTypeFullName, fieldSymbol.Name),
                        _ => _appData.NameTransformer.TransformFieldName(sourceTypeFullName, fieldSymbol.Name)
                    };
                    String fieldCall = $"{representation.Target}.{fieldName}";
                    MemberResolveData resolveData = new MemberResolveData(fieldCall, "");
                    return new OperationResult<MemberResolveData>(true, "", resolveData);
                }
                default:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member {name.Identifier} for type {sourceTypeFullName}");
            }
        }

        // TODO (std_string) : think about processing of named arguments in C# code
        // TODO (std_string) : think about processing more smart expression
        private OperationResult<MemberResolveData> ResolveMemberForNUnit(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            OperationResult<MemberResolveData> GenerateAssertEqual(String methodName, String arg0, String arg1, (String name, String value)[] namedArguments)
            {
                String namedArgumentsPart = String.Join("", namedArguments.Select(arg => $", {arg.name}={arg.value}"));
                String methodCall = $"self.{methodName}({arg0}, {arg1}{namedArgumentsPart})";
                MemberResolveData resolveData = new MemberResolveData(methodCall, "unittest");
                return new OperationResult<MemberResolveData>(true, "", resolveData);
            }
            OperationResult<MemberResolveData> ResolveAssertEqual()
            {
                if (data.Arguments.Count < 2)
                    return new OperationResult<MemberResolveData>(false, $"Bad arguments count in Assert.AreEqual: {data.Arguments.Count}");
                String firstArg = representation.Arguments.Values[0];
                String secondArg = representation.Arguments.Values[1];
                TypeInfo firstArgInfo = _model.GetTypeInfo(data.Arguments[0].Expression);
                TypeInfo secondArgInfo = _model.GetTypeInfo(data.Arguments[1].Expression);
                Boolean useEqualForCollections = firstArgInfo.Type is IArrayTypeSymbol || secondArgInfo.Type is IArrayTypeSymbol;
                switch (data.Arguments.Count)
                {
                    case 2:
                        (String name, String value)[] emptyNamedArguments = Array.Empty<(String name, String value)>();
                        return useEqualForCollections switch
                        {
                            true => GenerateAssertEqual("assertSequenceEqual", firstArg, secondArg, emptyNamedArguments),
                            false => GenerateAssertEqual("assertEqual", firstArg, secondArg, emptyNamedArguments)
                        };
                    case 3:
                        String thirdArg = representation.Arguments.Values[2];
                        ExpressionSyntax lastArgument = data.Arguments.Last().Expression;
                        String? lastArgumentType = _model.GetTypeInfo(lastArgument).Type?.GetTypeFullName();
                        if (lastArgumentType == null)
                            return new OperationResult<MemberResolveData>(false, "Unrecognizable third argument of Assert.AreEqual");
                        String? methodName = lastArgumentType switch
                        {
                            "System.Single" => "assertAlmostEqual",
                            "System.Double" => "assertAlmostEqual",
                            "System.String" when useEqualForCollections => "assertSequenceEqual",
                            "System.String" => "assertEqual",
                            _ => null
                        };
                        if (methodName is null)
                            return new OperationResult<MemberResolveData>(false, "Unsupported third argument of Assert.AreEqual");
                        (String name, String value)[] namedArguments = lastArgumentType! switch
                        {
                            "System.Single" => new []{(name: "delta", value: thirdArg)},
                            "System.Double" => new []{(name: "delta", value: thirdArg)},
                            "System.String" => new []{(name: "msg", value: thirdArg)},
                            _ => Array.Empty<(String name, String value)>()
                        };
                        return GenerateAssertEqual(methodName, firstArg, secondArg, namedArguments);
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
            String castMethod = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, $"As{castTypeSymbol.Name}");
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