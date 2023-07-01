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
}
