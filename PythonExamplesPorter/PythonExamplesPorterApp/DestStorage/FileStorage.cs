namespace PythonExamplesPorterApp.DestStorage
{
    internal class FileStorage
    {
        public FileStorage(String filePath)
        {
            _filePath = filePath;
            _indentation = 0;
        }

        public void Save()
        {
            using (StreamWriter writer = new StreamWriter(_filePath, false))
            {
                writer.WriteLine("# -*- coding: utf-8 -*-");
                foreach (String import in _imports)
                    writer.WriteLine(import);
                writer.WriteLine();
                for (Int32 index = 0; index < _classes.Count; ++index)
                {
                    if (index > 0)
                        writer.WriteLine();
                    _classes[index].Save(writer);
                }
            }
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

        public ClassStorage CreateClassStorage(String className)
        {
            ClassStorage classStorage = new ClassStorage(className, _indentation + StorageDef.IndentationDelta);
            _classes.Add(classStorage);
            return classStorage;
        }

        private readonly String _filePath;
        private readonly Int32 _indentation;
        private readonly IList<String> _imports = new List<String>();
        private readonly ISet<String> _importKeys = new HashSet<String>();
        private readonly IList<ClassStorage> _classes = new List<ClassStorage>();
    }
}
