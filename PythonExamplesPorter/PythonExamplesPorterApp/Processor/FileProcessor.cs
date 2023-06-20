using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Processor
{
    internal class FileProcessor
    {
        public FileProcessor(ILogger logger)
        {
            Logger = logger;
        }

        public void Process(String filename)
        {
            throw new NotImplementedException();
        }

        public void Process(Document file, Compilation compilation)
        {
            Logger.LogInfo($"Processing of the file {file.FilePath} is started");
            ProcessImpl(file, compilation);
            Logger.LogInfo($"Processing of the file {file.FilePath} is finished");
        }

        private void ProcessImpl(Document file, Compilation compilation)
        {
            SyntaxTree? tree = file.GetSyntaxTreeAsync().Result;
            if (tree == null)
                throw new InvalidOperationException();
            SemanticModel model = compilation.GetSemanticModel(tree);
            // ...
        }

        private ILogger Logger { get; }
    }
}
