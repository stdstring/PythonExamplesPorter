namespace PythonExamplesPorterApp.DestStorage
{
    internal class ImportStorage
    {
        public void Save(TextWriter writer)
        {
            foreach (String import in _imports)
                writer.WriteLine(import);
            writer.WriteLine();
            writer.WriteLine();
        }

        public void AddImport(String import)
        {
            if (_importKeys.Contains(import))
                return;
            _importKeys.Add(import);
            _imports.Add($"import {import}");
        }

        public void AddImportWithAlias(String import, String alias)
        {
            if (_importKeys.Contains(import))
                return;
            _importKeys.Add(import);
            _imports.Add($"import {import} as {alias}");
        }

        private readonly IList<String> _imports = new List<String>();
        private readonly ISet<String> _importKeys = new HashSet<String>();
    }
}