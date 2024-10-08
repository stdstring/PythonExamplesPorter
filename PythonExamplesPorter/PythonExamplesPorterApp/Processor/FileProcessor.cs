﻿using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Processor
{
    internal class FileProcessor
    {
        public FileProcessor(AppData appData)
        {
            _appData = appData;
        }

        public void Process(String filename)
        {
            throw new NotImplementedException();
        }

        public void Process(String relativeFilename, Document file, Compilation compilation)
        {
            if (_appData.IgnoredManager.IsIgnoredFile(relativeFilename))
            {
                _appData.Logger.LogInfo($"Processing of the file {relativeFilename} is skipped");
                return;
            }
            _appData.Logger.LogInfo($"Processing of the file {relativeFilename} is started");
            ProcessImpl(relativeFilename, file, compilation);
            _appData.Logger.LogInfo($"Processing of the file {relativeFilename} is finished");
        }

        private void ProcessImpl(String relativeFilename, Document file, Compilation compilation)
        {
            SyntaxTree tree = file.GetSyntaxTreeAsync().Result.Must("Bad file: without syntax tree");
            SemanticModel model = compilation.GetSemanticModel(tree);
            FileConverter converter = new FileConverter(_appData);
            converter.Convert(relativeFilename, tree, model);
        }

        private readonly AppData _appData;
    }
}
