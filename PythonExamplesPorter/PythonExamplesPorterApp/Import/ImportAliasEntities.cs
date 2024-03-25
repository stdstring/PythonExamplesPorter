using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Import
{
    [XmlRoot("ImportAliase")]
    public class ImportAliasEntry
    {
        [XmlElement("Import")]
        public String Import { get; set; } = "";

        [XmlElement("Alias")]
        public String Alias { get; set; } = "";
    }

    [XmlRoot("ImportAliases")]
    public class ImportAliasEntries
    {
        [XmlElement("ImportAlias")]
        public ImportAliasEntry[]? ImportAliases { get; set; }
    }
}
