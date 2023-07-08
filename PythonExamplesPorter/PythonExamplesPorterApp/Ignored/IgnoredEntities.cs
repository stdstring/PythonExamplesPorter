using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Ignored
{
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
