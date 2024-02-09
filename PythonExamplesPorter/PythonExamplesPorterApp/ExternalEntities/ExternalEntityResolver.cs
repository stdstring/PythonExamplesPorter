using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class ExternalEntityResolver
    {
        public ExternalEntityResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
            _resolvers = new IExternalEntityResolver[]
            {
                new KnownNamespacesEntityResolver(model, appData),
                new SystemEntityResolver(model, _appData),
                new NUnitEntityResolver(model)
            };
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

        // TODO (std_string) : move into resolvers
        public OperationResult<TypeResolveData> ResolveType(ITypeSymbol typeSymbol)
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

        public OperationResult<MemberResolveData> ResolveCtor(TypeSyntax type, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            OperationResult<ITypeSymbol> typeResult = ExtractExpressionType(type);
            if (!typeResult.Success)
                return new OperationResult<MemberResolveData>(false, typeResult.Reason);
            ITypeSymbol typeSymbol = typeResult.Data!;
            foreach (IExternalEntityResolver resolver in _resolvers)
            {
                OperationResult<MemberResolveData> result = resolver.ResolveCtor(typeSymbol, argumentsData, argumentsRepresentation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported ctor for type {type}");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            OperationResult<ITypeSymbol> targetTypeResult = ExtractExpressionType(data.Target);
            if (!targetTypeResult.Success)
                return new OperationResult<MemberResolveData>(false, targetTypeResult.Reason);
            ITypeSymbol sourceType = targetTypeResult.Data!;
            foreach (IExternalEntityResolver resolver in _resolvers)
            {
                OperationResult<MemberResolveData> result = resolver.ResolveMember(data, sourceType, representation);
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
            foreach (IExternalEntityResolver resolver in _resolvers)
            {
                OperationResult<CastResolveData> result = resolver.ResolveCast(sourceExpression, castTypeSymbol, sourceRepresentation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<CastResolveData>(false, $"Unsupported cast to type {castType}");
        }

        public OperationResult<CastResolveData> ResolveCast(ITypeSymbol castType, ExpressionSyntax sourceExpression, String sourceRepresentation)
        {
            foreach (IExternalEntityResolver resolver in _resolvers)
            {
                OperationResult<CastResolveData> result = resolver.ResolveCast(sourceExpression, castType, sourceRepresentation);
                if (result.Success)
                    return result;
            }
            return new OperationResult<CastResolveData>(false, $"Unsupported cast to type {castType.GetTypeFullName()}");
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
        private readonly IExternalEntityResolver[] _resolvers;
    }
}