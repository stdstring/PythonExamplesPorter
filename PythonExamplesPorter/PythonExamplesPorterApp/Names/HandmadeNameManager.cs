using PythonExamplesPorterApp.Common;

namespace PythonExamplesPorterApp.Names
{
    internal interface IHandmadeNameManager
    {
        OperationResult<String> Search(String typeName, String memberName);
    }

    internal class EmptyHandmadeNameManager : IHandmadeNameManager
    {
        public OperationResult<String> Search(String typeName, String memberName)
        {
            return new OperationResult<String>.Error("Not found");
        }
    }

    internal class HandmadeNameManager : IHandmadeNameManager
    {
        public HandmadeNameManager(HandmadeNameAliases aliases)
        {
            IList<NamespaceData> namespacesData = new List<NamespaceData>();
            foreach (NamespaceNameEntry namespaceEntry in aliases.Namespaces ?? Array.Empty<NamespaceNameEntry>())
            {
                TypeData? commonTypeData = null;
                IList<TypeData> typesData = new List<TypeData>();
                foreach (TypeNameEntry typeEntry in namespaceEntry.Types ?? Array.Empty<TypeNameEntry>())
                {
                    IDictionary<String, String> mappingData = new Dictionary<String, String>();
                    foreach (MemberAliasMapping memberAliasMapping in typeEntry.Members ?? Array.Empty<MemberAliasMapping>())
                        mappingData.Add(memberAliasMapping.Name, memberAliasMapping.Alias);
                    if (typeEntry.Condition == null)
                        commonTypeData = new TypeData(null, mappingData);
                    else
                    {
                        NameConditionsData conditionsData = new NameConditionsData(typeEntry.Condition.EqualCondition);
                        typesData.Add(new TypeData(conditionsData, mappingData));
                    }
                }
                if (namespaceEntry.Condition == null)
                    _commonNamespaceData = new NamespaceData(null, commonTypeData, typesData.ToArray());
                else
                {
                    NameConditionsData conditionsData = new NameConditionsData(namespaceEntry.Condition.EqualCondition);
                    namespacesData.Add(new NamespaceData(conditionsData, commonTypeData, typesData.ToArray()));
                }
            }
            _namespacesData = namespacesData.ToArray();
        }

        public OperationResult<String> Search(String typeName, String memberName)
        {
            Int32 lastDotIndex = typeName.LastIndexOf('.');
            String namespaceName = lastDotIndex == -1 ? "" : typeName.Substring(0, lastDotIndex);
            String simpleTypeName = lastDotIndex == -1 ? typeName : typeName.Substring(lastDotIndex + 1);
            if (_commonNamespaceData is not null)
            {
                switch (Search(_commonNamespaceData, namespaceName, simpleTypeName, memberName))
                {
                    case OperationResult<String>.Ok result:
                        return result;
                }
            }
            foreach (NamespaceData namespaceData in _namespacesData)
            {
                switch (Search(namespaceData, namespaceName, simpleTypeName, memberName))
                {
                    case OperationResult<String>.Ok result:
                        return result;
                }
            }
            return new OperationResult<String>.Error("Not found");
        }

        private OperationResult<String> Search(NamespaceData data, String namespaceName, String typeName, String memberName)
        {
            switch (data.NameConditions)
            {
                case null:
                case {EqualCondition: var expectedNamespaceName} when String.Equals(expectedNamespaceName, namespaceName):
                    if (data.CommonData is not null)
                    {
                        switch (Search(data.CommonData, typeName, memberName))
                        {
                            case OperationResult<String>.Ok result:
                                return result;
                        }
                    }
                    foreach (TypeData typeData in data.TypesData)
                    {
                        switch (Search(typeData, typeName, memberName))
                        {
                            case OperationResult<String>.Ok result:
                                return result;
                        }
                    }
                    return new OperationResult<String>.Error("Not found");
                default:
                    return new OperationResult<String>.Error("Not found");
            }
        }

        private OperationResult<String> Search(TypeData data, String typeName, String memberName)
        {
            switch (data.NameConditions)
            {
                case null when data.MemberAliasMapping.ContainsKey(memberName):
                case {EqualCondition: var expectedTypeName} when String.Equals(expectedTypeName, typeName) && data.MemberAliasMapping.ContainsKey(memberName):
                    return new OperationResult<String>.Ok(data.MemberAliasMapping[memberName]);
                default:
                    return new OperationResult<String>.Error("Not found");
            }
        }

        private record NameConditionsData(String? EqualCondition);

        private record TypeData(NameConditionsData? NameConditions, IDictionary<String, String> MemberAliasMapping);

        private record NamespaceData(NameConditionsData? NameConditions, TypeData? CommonData, TypeData[] TypesData);

        private readonly NamespaceData? _commonNamespaceData;
        private readonly NamespaceData[] _namespacesData;
    }

    internal static class HandmadeNameManagerFactory
    {
        public static IHandmadeNameManager Create(HandmadeNameAliases? aliases)
        {
            return aliases == null ? new EmptyHandmadeNameManager() : new HandmadeNameManager(aliases);
        }
    }
}
