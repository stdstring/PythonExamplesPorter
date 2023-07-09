namespace PythonExamplesPorterApp.Handmade
{
    internal class HandmadeEntitiesManager
    {
        public HandmadeEntitiesManager(HandmadeEntities? handmadeEntities)
        {
            _handmadeTypes = handmadeEntities?
                .HandmadeTypes?
                .ToDictionary(type => type.FullName) ?? new Dictionary<string, HandmadeType>();
        }

        public Boolean IsHandmadeType(String fullName) => _handmadeTypes.ContainsKey(fullName);

        public void UseHandmadeType(String fullName)
        {
            if (_handmadeTypes.ContainsKey(fullName))
                _usedHandmadeTypes.Add(fullName);
        }

        public HandmadeType[] GetUsedHandmadeTypes() => _usedHandmadeTypes.Select(type => _handmadeTypes[type]).ToArray();

        public IDictionary<String, String> GetHandmadeTypeMapping(String fullName)
        {
            if (!_handmadeTypes.ContainsKey(fullName))
                return new Dictionary<String, String>();
            return _handmadeTypes[fullName]
                .MemberMappings?
                .ToDictionary(mapping => mapping.SourceName, mapping => mapping.DestName) ?? new Dictionary<String, String>();
        }

        private readonly IDictionary<String, HandmadeType> _handmadeTypes;
        private readonly ISet<String> _usedHandmadeTypes = new HashSet<String>();
    }
}
