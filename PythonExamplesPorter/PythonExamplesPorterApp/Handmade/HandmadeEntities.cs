using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Handmade
{
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
