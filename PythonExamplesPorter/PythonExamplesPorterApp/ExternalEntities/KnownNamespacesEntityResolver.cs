using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class KnownNamespacesEntityResolver : IExternalEntityResolver
    {
        public KnownNamespacesEntityResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public OperationResult<MemberResolveData> ResolveCtor(ITypeSymbol sourceType, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<MemberResolveData>.Error($"Unsupported type: {sourceTypeFullName}");
            String moduleName = _appData.NameTransformer.TransformNamespaceName(sourceType.ContainingNamespace.ToDisplayString());
            String typeName = _appData.NameTransformer.TransformTypeName(sourceType.Name);
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport(moduleName);
            String ctorCall = $"{prepareResult.moduleName}.{typeName}({String.Join(", ", argumentsRepresentation.GetArguments(true))})";
            MemberResolveData resolveData = new MemberResolveData(ctorCall, prepareResult.importData);
            return new OperationResult<MemberResolveData>.Ok(resolveData);
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<MemberResolveData>.Error($"Unsupported type: {sourceTypeFullName}");
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = _model.GetSymbolInfo(name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>.Error($"Unrecognizable member {name.Identifier} for type {sourceTypeFullName}");
                case IMethodSymbol methodSymbol:
                {
                    String methodCall = this.GetMethodCall(sourceTypeFullName, representation, methodSymbol);
                    MemberResolveData resolveData = new MemberResolveData(methodCall);
                    return new OperationResult<MemberResolveData>.Ok(resolveData);
                }
                case IPropertySymbol propertySymbol:
                {
                    String propertyName = _appData.NameTransformer.TransformPropertyName(sourceTypeFullName, propertySymbol.Name);
                    String propertyCall = $"{representation.Target}.{propertyName}";
                    MemberResolveData resolveData = new MemberResolveData(propertyCall);
                    return new OperationResult<MemberResolveData>.Ok(resolveData);
                }
                case IFieldSymbol {IsStatic: var isStatic, IsReadOnly: var isReadOnly, Type.TypeKind: var typeKind} fieldSymbol:
                {
                    String fieldName = typeKind switch
                    {
                        TypeKind.Enum => _appData.NameTransformer.TransformEnumValueName(sourceTypeFullName, fieldSymbol.Name),
                        _ when isStatic && isReadOnly => _appData.NameTransformer.TransformStaticReadonlyFieldName(sourceTypeFullName, fieldSymbol.Name),
                        _ => _appData.NameTransformer.TransformFieldName(sourceTypeFullName, fieldSymbol.Name)
                    };
                    String fieldCall = $"{representation.Target}.{fieldName}";
                    MemberResolveData resolveData = new MemberResolveData(fieldCall);
                    return new OperationResult<MemberResolveData>.Ok(resolveData);
                }
            }
            return new OperationResult<MemberResolveData>.Error($"Unsupported member {name.Identifier} for type {sourceTypeFullName}");
        }

        public OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation)
        {
            String sourceTypeFullName = castTypeSymbol.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<CastResolveData>.Error($"Unsupported type: {sourceTypeFullName}");
            // TODO (std_string) : think about check existing corresponding cast method in sourceExpression
            String castMethod = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, $"As{castTypeSymbol.Name}");
            CastResolveData castResolveData = new CastResolveData($"{sourceRepresentation}.{castMethod}()");
            return new OperationResult<CastResolveData>.Ok(castResolveData);
        }

        private String GetMethodCall(String sourceTypeFullName, MemberRepresentation representation, IMethodSymbol methodSymbol)
        {
            switch (methodSymbol)
            {
                case {Name: "GetHashCode"}:
                    return String.Concat("hash(", representation.Target, ")");
                case {Name: "ToArray"}:
                    return String.Concat("list(", representation.Target, ")");
                default:
                    String methodName = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, methodSymbol.Name);
                    String args = String.Join(", ", representation.Arguments.GetArguments(true));
                    return String.Concat(representation.Target, ".", methodName, "(", args, ")");
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}
