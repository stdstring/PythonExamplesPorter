using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Converter
{
    internal class FileConverter
    {
        public FileConverter(AppData appData)
        {
            _appData = appData;
        }

        public void Convert(String relativeFilePath, SyntaxTree tree, SemanticModel model)
        {
            String destRelativePath = PathTransformer.TransformPath(relativeFilePath);
            String destDirectory = _appData.AppConfig.ResolveDestDirectory();
            String destPath = Path.Combine(destDirectory, destRelativePath);
            FileStorage currentFile = new FileStorage(destPath);
            FileConverterVisitor converter = new FileConverterVisitor(model, currentFile, _appData);
            converter.Visit(tree.GetRoot());
            if (currentFile.IsEmpty())
                return;
            Directory.CreateDirectory(destDirectory);
            currentFile.Save();
        }

        private readonly AppData _appData;
    }
}
