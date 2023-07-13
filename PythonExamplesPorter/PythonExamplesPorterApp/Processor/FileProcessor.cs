using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Processor
{
    internal class FileProcessor
    {
        public FileProcessor(AppConfig appConfig,
                             IgnoredEntitiesManager ignoredManager,
                             HandmadeEntitiesManager handmadeManager,
                             ILogger logger)
        {
            _appConfig = appConfig;
            _ignoredManager = ignoredManager;
            _handmadeManager = handmadeManager;
            _logger = logger;
        }

        public void Process(String filename)
        {
            throw new NotImplementedException();
        }

        public void Process(String relativeFilename, Document file, Compilation compilation)
        {
            if (_ignoredManager.IsIgnoredFile(relativeFilename))
            {
                _logger.LogInfo($"Processing of the file {relativeFilename} is skipped");
                return;
            }
            _logger.LogInfo($"Processing of the file {relativeFilename} is started");
            ProcessImpl(relativeFilename, file, compilation);
            _logger.LogInfo($"Processing of the file {relativeFilename} is finished");
        }

        private void ProcessImpl(String relativeFilename, Document file, Compilation compilation)
        {
            SyntaxTree? tree = file.GetSyntaxTreeAsync().Result;
            if (tree == null)
                throw new InvalidOperationException();
            SemanticModel model = compilation.GetSemanticModel(tree);
            FileConverter converter = new FileConverter(_appConfig, _ignoredManager, _handmadeManager, _logger);
            converter.Convert(relativeFilename, tree, model);
        }

        private readonly AppConfig _appConfig;
        private readonly IgnoredEntitiesManager _ignoredManager;
        private readonly HandmadeEntitiesManager _handmadeManager;
        private readonly ILogger _logger;
    }
}
