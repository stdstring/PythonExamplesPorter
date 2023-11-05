using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Handmade
{
    internal record MappingData(String Name, Boolean NeedImport);

    internal class HandmadeEntitiesManager
    {
        public HandmadeEntitiesManager(HandmadeEntities? handmadeEntities)
        {
            _handmadeTypes = handmadeEntities?
                .HandmadeTypes?
                .ToDictionary(type => type.FullName) ?? new Dictionary<string, HandmadeType>();
        }

        public Boolean IsHandmadeType(String fullName) => _handmadeTypes.ContainsKey(fullName);

        public Boolean UseHandmadeType(String fullName)
        {
            if (!_handmadeTypes.ContainsKey(fullName))
                return false;
            _usedHandmadeTypes.Add(fullName);
            return true;
        }

        public HandmadeType[] GetUsedHandmadeTypes() => _usedHandmadeTypes.Select(type => _handmadeTypes[type]).ToArray();

        public IDictionary<String, MappingData> GetHandmadeTypeMapping(String fullName)
        {
            if (!_handmadeTypes.ContainsKey(fullName))
                return new Dictionary<String, MappingData>();
            return _handmadeTypes[fullName]
                .MemberMappings?
                .ToDictionary(mapping => mapping.SourceName, mapping => new MappingData(mapping.DestName, mapping.NeedImport)) ?? new Dictionary<String, MappingData>();
        }

        public String CalcHandmadeTypeModuleName(String fullName)
        {
            if (!_handmadeTypes.ContainsKey(fullName))
                return "";
            HandmadeType handmadeType = _handmadeTypes[fullName];
            String[] destParts = handmadeType.Dest.Split('\\', '/');
            destParts[^1] = Path.GetFileNameWithoutExtension(destParts[^1]);
            return String.Join(".", destParts.Select(NameTransformer.TransformFileObjectName));
        }

        private readonly IDictionary<String, HandmadeType> _handmadeTypes;
        private readonly ISet<String> _usedHandmadeTypes = new HashSet<String>();
    }
}
