using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Ignored
{
    [XmlRoot("IgnoredEntities")]
    public class IgnoredEntities
    {
        [XmlArray("Directories")]
        [XmlArrayItem("Directory")]
        public String[]? Directories { get; set; }

        [XmlArray("Files")]
        [XmlArrayItem("File")]
        public String[]? Files { get; set; }

        [XmlArray("Types")]
        [XmlArrayItem("Type")]
        public String[]? Types { get; set; }

        [XmlArray("Methods")]
        [XmlArrayItem("Method")]
        public String[]? Methods { get; set; }

        [XmlArray("MethodsBody")]
        [XmlArrayItem("MethodBody")]
        public String[]? MethodsBody { get; set; }
    }
}
