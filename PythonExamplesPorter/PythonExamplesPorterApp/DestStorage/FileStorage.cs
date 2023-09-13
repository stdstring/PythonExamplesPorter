using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.DestStorage
{
    internal class FileStorage
    {
        public FileStorage(String filePath)
        {
            _filePath = filePath;
            _indentation = 0;
            ImportStorage = new ImportStorage();
        }

        public void Save()
        {
            using (StreamWriter writer = new StreamWriter(_filePath, false))
            {
                writer.WriteLine("# -*- coding: utf-8 -*-");
                ImportStorage.Save(writer);
                for (Int32 index = 0; index < _classes.Count; ++index)
                {
                    if (index > 0)
                        writer.WriteLine();
                    _classes[index].Save(writer);
                }
            }
        }

        public ClassStorage CreateClassStorage(String className)
        {
            Int32 indentation = _indentation + (_indentation > 0 ? StorageDef.IndentationDelta : 0);
            ClassStorage classStorage = new ClassStorage(className, indentation, ImportStorage);
            _classes.Add(classStorage);
            return classStorage;
        }

        public Boolean IsEmpty() => _classes.IsEmpty();

        public ImportStorage ImportStorage { get; }

        private readonly String _filePath;
        private readonly Int32 _indentation;
        private readonly IList<ClassStorage> _classes = new List<ClassStorage>();
    }
}
