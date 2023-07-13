using System.Xml.Serialization;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;

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

        [XmlElement("BaseDirectory")]
        public String? BaseDirectory { get; set; }
    }
}
