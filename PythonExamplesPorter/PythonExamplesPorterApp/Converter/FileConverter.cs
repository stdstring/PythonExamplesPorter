using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Comments;
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
            String destRelativePath = PathTransformer.TransformPath(relativeFilePath, _appData.NameTransformer);
            String destDirectory = _appData.AppConfig.ResolveDestDirectory();
            String destPath = Path.Combine(destDirectory, destRelativePath);
            FileStorage currentFile = new FileStorage(destPath);
            FileConverterVisitor converter = new FileConverterVisitor(model, currentFile, _appData);
            SyntaxNode root = tree.GetRoot();
            CommentsProcessor commentsProcessor = new CommentsProcessor(_appData.NameTransformer);
            currentFile.AppendHeaderData(commentsProcessor.Process(CommentsExtractor.ExtractComments(root)));
            converter.Visit(root);
            if (currentFile.IsEmpty())
                return;
            currentFile.Save();
        }

        private readonly AppData _appData;
    }
}
