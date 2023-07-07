using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Config
{
    [XmlRoot("ConfigData")]
    public class ConfigData
    {
        [XmlElement("BaseConfig")]
        public BaseConfig? BaseConfig { get; set; }

        [XmlElement("IgnoredEntities")]
        public IgnoredEntities? IgnoredEntities { get; set; }

        [XmlElement("HandmadeEntities")]
        public HandmadeEntities? HandmadeEntities { get; set; }
    }

    [XmlRoot("BaseConfig")]
    public class BaseConfig
    {
        [XmlElement("Source")]
        public String Source { get; set; } = "";

        [XmlElement("Dest")]
        public String DestDirectory { get; set; } = "";
    }

    [XmlRoot("IgnoredEntities")]
    public class IgnoredEntities
    {
        [XmlArray("Files")]
        [XmlArrayItem("File")]
        public String[]? Files { get; set; }

        [XmlArray("Types")]
        [XmlArrayItem("Type")]
        public String[]? Types { get; set; }

        [XmlArray("Methods")]
        [XmlArrayItem("Method")]
        public String[]? Methods { get; set; }
    }

    [XmlRoot("HandmadeEntities")]
    public class HandmadeEntities
    {
        [XmlArray("Types")]
        [XmlArrayItem("Type")]
        public HandmadeType[]? HandmadeTypes { get; set; }
    }

    [XmlRoot("HandmadeType")]
    public class HandmadeType
    {
        [XmlAttribute("FullName")]
        public String FullName { get; set; } = "";

        [XmlElement("Source")]
        public String Source { get; set; } = "";

        [XmlElement("Dest")]
        public String Dest { get; set; } = "";

        [XmlArray("MemberMapping")]
        [XmlArrayItem("Member")]
        public HandmadeMemberMapping[]? MemberMappings { get; set; }
    }

    [XmlRoot("HandmadeMemberMapping")]
    public class HandmadeMemberMapping
    {
        [XmlAttribute("SourceName")]
        public String SourceName { get; set; } = "";

        [XmlAttribute("DestName")]
        public String DestName { get; set; } = "";
    }
}
