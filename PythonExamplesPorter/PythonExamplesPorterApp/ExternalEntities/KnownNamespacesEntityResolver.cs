﻿using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class KnownNamespacesEntityResolver : IExternalEntityResolver
    {
        public KnownNamespacesEntityResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<MemberResolveData>(false, $"Unsupported type: {sourceTypeFullName}");
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = _model.GetSymbolInfo(name);
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
                        MemberResolveData resolveData = new MemberResolveData(methodCall);
                        return new OperationResult<MemberResolveData>(true, "", resolveData);
                    }
                case IPropertySymbol propertySymbol:
                    {
                        String propertyName = _appData.NameTransformer.TransformPropertyName(sourceTypeFullName, propertySymbol.Name);
                        String propertyCall = $"{representation.Target}.{propertyName}";
                        MemberResolveData resolveData = new MemberResolveData(propertyCall);
                        return new OperationResult<MemberResolveData>(true, "", resolveData);
                    }
                case IFieldSymbol { IsStatic: var isStatic, IsReadOnly: var isReadOnly, Type.TypeKind: var typeKind } fieldSymbol:
                    {
                        String fieldName = typeKind switch
                        {
                            TypeKind.Enum => _appData.NameTransformer.TransformEnumValueName(sourceTypeFullName, fieldSymbol.Name),
                            _ when isStatic && isReadOnly => _appData.NameTransformer.TransformStaticReadonlyFieldName(sourceTypeFullName, fieldSymbol.Name),
                            _ => _appData.NameTransformer.TransformFieldName(sourceTypeFullName, fieldSymbol.Name)
                        };
                        String fieldCall = $"{representation.Target}.{fieldName}";
                        MemberResolveData resolveData = new MemberResolveData(fieldCall);
                        return new OperationResult<MemberResolveData>(true, "", resolveData);
                    }
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported member {name.Identifier} for type {sourceTypeFullName}");
        }

        public OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation)
        {
            String sourceTypeFullName = castTypeSymbol.GetTypeFullName();
            // TODO (std_string) : think about check containing assemblies
            String[] knownNamespaces = _appData.AppConfig.GetSourceDetails().KnownNamespaces ?? Array.Empty<String>();
            Boolean isSupportedType = knownNamespaces.Any(sourceTypeFullName.StartsWith);
            if (!isSupportedType)
                return new OperationResult<CastResolveData>(false, $"Unsupported type: {sourceTypeFullName}");
            // TODO (std_string) : think about check existing corresponding cast method in sourceExpression
            String castMethod = _appData.NameTransformer.TransformMethodName(sourceTypeFullName, $"As{castTypeSymbol.Name}");
            CastResolveData castResolveData = new CastResolveData($"{sourceRepresentation}.{castMethod}()");
            return new OperationResult<CastResolveData>(true, String.Empty, castResolveData);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
    }
}
