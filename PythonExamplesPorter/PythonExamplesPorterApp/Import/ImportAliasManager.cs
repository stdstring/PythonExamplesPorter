using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Import
{
    internal class ImportAliasManager
    {
        public ImportAliasManager(ImportAliasEntries? data)
        {
            _importAliases = new Dictionary<String, String>();
            foreach (ImportAliasEntry entry in data?.ImportAliases ?? Array.Empty<ImportAliasEntry>())
                _importAliases.Add(entry.Import, entry.Alias);
        }

        public (String ModuleName, ImportData ImportData) PrepareImport(String moduleName)
        {
            ImportData importData = new ImportData();
            String destModuleName = PrepareImport(moduleName, importData);
            return (ModuleName: destModuleName, ImportData: importData);
        }

        public String PrepareImport(String moduleName, ImportData sourceData)
        {
            const char delimiter = '.';
            String leftPart = moduleName;
            String rightPart = "";
            while (leftPart.Length > 0)
            {
                if (_importAliases.ContainsKey(leftPart))
                    break;
                switch (leftPart.LastIndexOf(delimiter))
                {
                    case -1:
                        rightPart = $"{leftPart}{(rightPart.Length > 0 ? "." : "")}{rightPart}";
                        leftPart = "";
                        break;
                    case var lastDelimiterPos:
                        rightPart = $"{leftPart.Substring(lastDelimiterPos + 1)}{(rightPart.Length > 0 ? "." : "")}{rightPart}";
                        leftPart = leftPart.Substring(0, lastDelimiterPos);
                        break;
                }
            }
            String alias = "";
            if (leftPart.Length > 0)
            {
                alias = _importAliases[leftPart];
                sourceData.AddImport(leftPart, alias);
            }
            sourceData.AddImport(moduleName);
            return $"{alias}{((alias.Length > 0) && (rightPart.Length > 0) ? delimiter : "")}{rightPart}";
        }

        private readonly IDictionary<String, String> _importAliases;
    }
}
