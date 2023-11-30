using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Names
{
    [XmlRoot("member")]
    public class MemberAliasMapping
    {
        [XmlElement("name")]
        public String Name { get; set; } = "";

        [XmlElement("alias")]
        public String Alias { get; set; } = "";
    }

    [XmlRoot("conditions")]
    public class NameConditions
    {
        [XmlElement("equal")]
        public String? EqualCondition { get; set; }
    }

    [XmlRoot("type")]
    public class TypeNameEntry
    {
        [XmlElement("conditions")]
        public NameConditions? Condition { get; set; }

        [XmlArray("members")]
        [XmlArrayItem("member")]
        public MemberAliasMapping[]? Members { get; set; }
    }

    [XmlRoot("namespace")]
    public class NamespaceNameEntry
    {
        [XmlElement("conditions")]
        public NameConditions? Condition { get; set; }

        [XmlArray("types")]
        [XmlArrayItem("type")]
        public TypeNameEntry[]? Types { get; set; }
    }

    [XmlRoot("aliases")]
    public class HandmadeNameAliases
    {
        [XmlElement("namespace")]
        public NamespaceNameEntry[]? Namespaces { get; set; }
    }
}
