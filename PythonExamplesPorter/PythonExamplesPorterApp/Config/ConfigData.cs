using System.Xml.Serialization;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Names;

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

        [XmlElement("aliases")]
        public HandmadeNameAliases? HandmadeAliases { get; set; }
    }

    public enum RelativePathBase
    {
        [XmlEnum(Name = "app")]
        App = 0,
        [XmlEnum(Name = "config")]
        Config = 1
    }

    [XmlRoot("Source")]
    public class TargetPath
    {
        public TargetPath()
        {
        }

        public TargetPath(RelativePathBase relativePathBase, String path)
        {
            RelativePathBase = relativePathBase;
            Path = path;
        }

        [XmlAttribute("RelativePathBase")]
        public RelativePathBase RelativePathBase { get; set; }
        [XmlText]
        public String Path { get; set; } = "";
    }

    [XmlRoot("SourceDetails")]
    public class SourceDetails
    {
        // TODO (std_string) : think about name of property (and name of element in config)
        [XmlArray("KnownNamespaces")]
        [XmlArrayItem("KnownNamespace")]
        public String[]? KnownNamespaces { get; set; }
    }

    [XmlRoot("BaseConfig")]
    public class BaseConfig
    {
        [XmlElement("Source")]
        public TargetPath? Source { get; set; }

        [XmlElement("SourceDetails")]
        public SourceDetails? SourceDetails { get; set; }

        [XmlElement("Dest")]
        public TargetPath? DestDirectory { get; set; }
    }
}
