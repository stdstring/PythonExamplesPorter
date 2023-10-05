using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterApp.Converter
{
    internal record TypeResolveData(String TypeName, String ModuleName);

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
            String destModuleName = NameTransformer.TransformNamespaceName(sourceNamespaceName);
            String destTypeName = NameTransformer.TransformClassName(sourceTypeName);
            return new OperationResult<TypeResolveData>(true, "", new TypeResolveData(destTypeName, destModuleName));
        }

        public OperationResult<MethodCallResolveData> ResolveMethodCall(ExpressionSyntax target, String targetRepresentation, SimpleNameSyntax name, String[] arguments)
        {
            OperationResult<SourceType> targetTypeResult = ExtractMethodTargetType(target);
            if (!targetTypeResult.Success)
                return new OperationResult<MethodCallResolveData>(false, targetTypeResult.Reason);
            SourceType sourceType = targetTypeResult.Data!;
            String typeFullName = $"{sourceType.NamespaceName}.{sourceType.TypeName}";
            IList<ResolveMethodCallHandler> handlers = new List<ResolveMethodCallHandler>
            {
                ResolveMethodCallForKnownNamespace,
                ResolveMethodCallForNUnit,
                ResolveMethodCallForSystem
            };
            foreach (ResolveMethodCallHandler handler in handlers)
            {
                OperationResult<MethodCallResolveData> result = handler(targetRepresentation, sourceType, name, arguments);
                if (result.Success)
                    return result;
            }
            return new OperationResult<MethodCallResolveData>(false, $"Unsupported target type type \"{typeFullName}\"");
        }

        private record SourceType(String NamespaceName, String TypeName);

        private delegate OperationResult<MethodCallResolveData> ResolveMethodCallHandler(String targetRepresentation, SourceType sourceType, SimpleNameSyntax name, String[] arguments);

        private OperationResult<SourceType> ExtractMethodTargetType(ExpressionSyntax target)
        {
            return ExtractMethodTargetType(target, _model.GetSymbolInfo(target).Symbol);
        }

        private OperationResult<SourceType> ExtractMethodTargetType(ExpressionSyntax target, ISymbol? targetSymbol)
        {
            return targetSymbol switch
            {
                null =>
                    new OperationResult<SourceType>(false, $"Unrecognizable method target type for \"{target}\""),
                ILocalSymbol localSymbol => ExtractMethodTargetType(target, localSymbol.Type),
                INamedTypeSymbol typeSymbol =>
                    new OperationResult<SourceType>(true, "", new SourceType(typeSymbol.ContainingNamespace.ToDisplayString(), typeSymbol.Name)),
                _ =>
                    new OperationResult<SourceType>(false, $"Unsupported method target type for \"{target}\"")
            };
        }

        private OperationResult<MethodCallResolveData> ResolveMethodCallForKnownNamespace(String targetRepresentation, SourceType sourceType, SimpleNameSyntax name, String[] arguments)
        {
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            String typeFullName = $"{sourceType.NamespaceName}.{sourceType.TypeName}";
            Boolean isSupportedType = knownNamespaces.Any(sourceType.NamespaceName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<MethodCallResolveData>(false, $"Unsupported type: {typeFullName}");
            SymbolInfo nameInfo = _model.GetSymbolInfo(name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MethodCallResolveData>(false, $"Unrecognizable method \"{name.Identifier}\" for type \"{typeFullName}\"");
                case IMethodSymbol methodSymbol:
                    String methodName = NameTransformer.TransformMethodName(methodSymbol.Name);
                    String args = String.Join(", ", arguments);
                    String methodCall = String.Concat(targetRepresentation, ".", methodName, "(", args, ")");
                    MethodCallResolveData resolveData = new MethodCallResolveData(methodCall, "");
                    return new OperationResult<MethodCallResolveData>(true, "", resolveData);
                default:
                    return new OperationResult<MethodCallResolveData>(false, $"Unsupported method \"{name.Identifier}\" for type \"{typeFullName}\"");
            }
        }

        private OperationResult<MethodCallResolveData> ResolveMethodCallForNUnit(String targetRepresentation, SourceType sourceType, SimpleNameSyntax name, String[] arguments)
        {
            String typeFullName = $"{sourceType.NamespaceName}.{sourceType.TypeName}";
            if (!typeFullName.Equals("NUnit.Framework.Assert"))
                return new OperationResult<MethodCallResolveData>(false, $"Unsupported type \"{typeFullName}\"");
            SymbolInfo nameInfo = _model.GetSymbolInfo(name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MethodCallResolveData>(false, $"Unrecognizable method \"{name.Identifier}\" for type \"{typeFullName}\"");
                case IMethodSymbol{Name: "AreEqual"}:
                    String args = String.Join(", ", arguments);
                    String methodCall = String.Concat("self.assertEqual(", args, ")");
                    MethodCallResolveData resolveData = new MethodCallResolveData(methodCall, "unittest");
                    return new OperationResult<MethodCallResolveData>(true, "", resolveData);
                default:
                    return new OperationResult<MethodCallResolveData>(false, $"Unsupported method \"{name.Identifier}\" for type \"{typeFullName}\"");
            }
        }

        private OperationResult<MethodCallResolveData> ResolveMethodCallForSystem(String targetRepresentation, SourceType sourceType, SimpleNameSyntax name, String[] arguments)
        {
            return new OperationResult<MethodCallResolveData>(false, $"ResolveMethodCallForSystem: Not Implemented");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}