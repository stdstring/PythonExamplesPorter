using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Converter
{
    internal class FileConverter
    {
        public FileConverter(AppConfig appConfig,
                             IgnoredEntitiesManager ignoredManager,
                             HandmadeEntitiesManager handmadeManager,
                             ILogger logger)
        {
            _appConfig = appConfig;
            _ignoredManager = ignoredManager;
            _handmadeManager = handmadeManager;
            _logger = logger;
        }

        public void Convert(String relativeFilePath, SyntaxTree tree, SemanticModel model)
        {
            String destRelativePath = PathTransformer.TransformPath(relativeFilePath);
            String destDirectory = _appConfig.ConfigData.BaseConfig!.DestDirectory.ResolveTargetPath(_appConfig);
            String destPath = Path.Combine(destDirectory, destRelativePath);
            FileStorage currentFile = new FileStorage(destPath);
            FileConverterSyntaxWalker converter = new FileConverterSyntaxWalker(model, currentFile, _ignoredManager, _handmadeManager, _logger);
            converter.Visit(tree.GetRoot());
            if (currentFile.IsEmpty())
                return;
            Directory.CreateDirectory(destDirectory);
            currentFile.Save();
        }

        private readonly AppConfig _appConfig;
        private readonly IgnoredEntitiesManager _ignoredManager;
        private readonly HandmadeEntitiesManager _handmadeManager;
        private readonly ILogger _logger;
    }
}
