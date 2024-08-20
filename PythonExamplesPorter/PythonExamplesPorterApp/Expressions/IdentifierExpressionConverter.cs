using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.ExternalEntities;
using PythonExamplesPorterApp.Handmade;

namespace PythonExamplesPorterApp.Expressions
{
    internal class IdentifierExpressionConverter
    {
        public IdentifierExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _externalEntityResolver = new ExternalEntityResolver(model, appData, settings);
        }

        public ConvertResult Convert(IdentifierNameSyntax identifier)
        {
            ImportData importData = new ImportData();
            SymbolInfo symbolInfo = _model.GetSymbolInfo(identifier);
            switch (symbolInfo.Symbol)
            {
                case null:
                    throw new UnsupportedSyntaxException($"Unrecognizable identifier: {identifier.Identifier}");
                case ILocalSymbol localSymbol:
                    return new ConvertResult(_appData.NameTransformer.TransformLocalVariableName(localSymbol.Name), importData);
                case INamedTypeSymbol typeSymbol:
                    TypeResolveData resolveData = _externalEntityResolver.ResolveType(typeSymbol).MustSuccess();
                    return ProcessTypeResolveData(resolveData, importData);
                case IPropertySymbol propertySymbol:
                    // TODO (std_string) : think about smart (not straightforward) solution
                    // TODO (std_string) : think about cases when property/method/etc in source type is absent in dest handmade type
                    String name = propertySymbol.Name;
                    String typeFullName = propertySymbol.ContainingType.GetTypeFullName();
                    if (!_appData.HandmadeManager.IsHandmadeType(typeFullName))
                        throw new UnsupportedSyntaxException($"Unsupported identifier with name = {identifier.Identifier} and kind = {identifier.Kind()}");
                    IDictionary<String, MappingData> mapping = _appData.HandmadeManager.GetHandmadeTypeMapping(typeFullName);
                    if (mapping.ContainsKey(name))
                    {
                        MappingData mappingData = mapping[name];
                        name = mappingData.Name;
                        if (mappingData.NeedImport)
                        {
                            String moduleName = _appData.HandmadeManager.CalcHandmadeTypeModuleName(typeFullName);
                            importData.AddEntity(moduleName, name);
                        }
                    }
                    return new ConvertResult(name, importData);
                default:
                    throw new UnsupportedSyntaxException($"Unsupported identifier with name = {identifier.Identifier} and kind = {identifier.Kind()}");
            }
        }

        private ConvertResult ProcessTypeResolveData(TypeResolveData resolveData, ImportData importData)
        {
            importData.Append(resolveData.ImportData);
            return new ConvertResult($"{resolveData.ModuleName}.{resolveData.TypeName}", importData);
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExternalEntityResolver _externalEntityResolver;
    }
}
