using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class ExternalEntityResolver
    {
        public ExternalEntityResolver(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _resolvers = new IExternalEntityResolver[]
            {
                new KnownNamespacesEntityResolver(model, appData),
                new SystemEntityResolver(model, _appData, settings),
                new NUnitEntityResolver(model)
            };
        }

        public OperationResult<TypeResolveData> ResolveType(TypeSyntax type)
        {
            SymbolInfo symbolInfo = _model.GetSymbolInfo(type);
            ISymbol? typeInfo = symbolInfo.Symbol;
            if (typeInfo == null)
                return new OperationResult<TypeResolveData>.Error($"Unrecognizable type: {type}");
            return typeInfo switch
            {
                INamedTypeSymbol typeSymbol => ResolveType(typeSymbol),
                _ => new OperationResult<TypeResolveData>.Error($"Unsupported {typeInfo.Kind} kind of symbol info for {type}")
            };
        }

        // TODO (std_string) : move into resolvers
        public OperationResult<TypeResolveData> ResolveType(ITypeSymbol typeSymbol)
        {
            String sourceNamespaceName = typeSymbol.ContainingNamespace.ToDisplayString();
            String sourceTypeName = typeSymbol.Name;
            String[] systemNamespaces = {"System", "NUnit.Framework"};
            Boolean isSystemType = systemNamespaces.Any(sourceNamespaceName.StartsWith);
            // TODO (std_string) : I return empty type for system type because we need in additional analysis - think about approach
            if (isSystemType)
                return new OperationResult<TypeResolveData>.Ok(new TypeResolveData("", "", new ImportData()));
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceNamespaceName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<TypeResolveData>.Error($"Unsupported type: {sourceNamespaceName}.{sourceTypeName}");
            String destModuleName = _appData.NameTransformer.TransformNamespaceName(sourceNamespaceName);
            String destTypeName = _appData.NameTransformer.TransformTypeName(sourceTypeName);
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport(destModuleName);
            return new OperationResult<TypeResolveData>.Ok(new TypeResolveData(destTypeName, prepareResult.moduleName, prepareResult.importData));
        }

        public OperationResult<MemberResolveData> ResolveCtor(TypeSyntax type, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            switch (ExtractExpressionType(type))
            {
                case OperationResult<ITypeSymbol>.Error(Reason: var reason):
                    return new OperationResult<MemberResolveData>.Error(reason);
                case OperationResult<ITypeSymbol>.Ok(Data: var typeSymbol):
                    foreach (IExternalEntityResolver resolver in _resolvers)
                    {
                        switch (resolver.ResolveCtor(typeSymbol, argumentsData, argumentsRepresentation))
                        {
                            case OperationResult<MemberResolveData>.Ok result:
                                return result;
                        }
                    }
                    return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for type {type}");
                default:
                    throw new InvalidOperationException("Unexpected control flow branch");
            }
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            switch (ExtractExpressionType(data.Target))
            {
                case OperationResult<ITypeSymbol>.Error(Reason: var reason):
                    return new OperationResult<MemberResolveData>.Error(reason);
                case OperationResult<ITypeSymbol>.Ok(Data: var sourceType):
                    foreach (IExternalEntityResolver resolver in _resolvers)
                    {
                        switch (resolver.ResolveMember(data, sourceType, representation))
                        {
                            case OperationResult<MemberResolveData>.Ok result:
                                return result;
                        }
                    }
                    return new OperationResult<MemberResolveData>.Error($"Unsupported target type {sourceType.GetTypeFullName()}");
                default:
                    throw new InvalidOperationException("Unexpected control flow branch");
            }
        }

        public OperationResult<CastResolveData> ResolveCast(TypeSyntax castType, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            switch (ExtractExpressionType(castType))
            {
                case OperationResult<ITypeSymbol>.Error(Reason: var reason):
                    return new OperationResult<CastResolveData>.Error(reason);
                case OperationResult<ITypeSymbol>.Ok(Data: var castTypeSymbol):
                    foreach (IExternalEntityResolver resolver in _resolvers)
                    {
                        switch (resolver.ResolveCast(sourceExpression, castTypeSymbol, sourceRepresentation))
                        {
                            case OperationResult<CastResolveData>.Ok result:
                                return result;
                        }
                    }
                    return new OperationResult<CastResolveData>.Error($"Unsupported cast to type {castType}");
                default:
                    throw new InvalidOperationException("Unexpected control flow branch");
            }
        }

        public OperationResult<CastResolveData> ResolveCast(ITypeSymbol castType, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            foreach (IExternalEntityResolver resolver in _resolvers)
            {
                switch (resolver.ResolveCast(sourceExpression, castType, sourceRepresentation))
                {
                    case OperationResult<CastResolveData>.Ok result:
                        return result;
                }
            }
            return new OperationResult<CastResolveData>.Error($"Unsupported cast to type {castType.GetTypeFullName()}");
        }

        // TODO (std_string) : think about separation for members, cast etc
        private OperationResult<ITypeSymbol> ExtractExpressionType(ExpressionSyntax target)
        {
            return target.GetExpressionTypeSymbol(_model) switch
            {
                OperationResult<ITypeSymbol>.Error error => error,
                OperationResult<ITypeSymbol>.Ok(Data: IArrayTypeSymbol type) =>
                    new OperationResult<ITypeSymbol>.Error($"Unsupported member target type - {type.ElementType.GetTypeFullName()}[] for expression: {target}"),
                OperationResult<ITypeSymbol>.Ok result => result,
                _ => throw new InvalidOperationException("Unexpected control flow branch")
            };
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly IExternalEntityResolver[] _resolvers;
    }
}