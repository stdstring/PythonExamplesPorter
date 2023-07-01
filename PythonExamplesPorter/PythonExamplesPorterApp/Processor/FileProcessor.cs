﻿using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Processor
{
    internal class FileProcessor
    {
        public FileProcessor(AppConfig appConfig, ILogger logger)
        {
            _appConfig = appConfig;
            _logger = logger;
        }

        public void Process(String filename)
        {
            throw new NotImplementedException();
        }

        public void Process(String relativeFilename, Document file, Compilation compilation)
        {
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
            FileConverter converter = new FileConverter(_appConfig, _logger);
            converter.Convert(relativeFilename, tree, model);
        }

        private readonly AppConfig _appConfig;
        private readonly ILogger _logger;
    }
}
