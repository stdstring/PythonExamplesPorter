using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.MSBuild;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Processor
{
    internal class ProjectProcessor
    {
        public ProjectProcessor(ILogger logger)
        {
            Logger = logger;
            _fileProcessor = new FileProcessor(logger);
        }

        public void Process(String projectFilename)
        {
            Logger.LogInfo($"Processing of the project {projectFilename} is started");
            MSBuildWorkspace workspace = MSBuildWorkspace.Create();
            Project project = workspace.OpenProjectAsync(projectFilename).Result;
            ProcessImpl(project);
            Logger.LogInfo($"Processing of the project {projectFilename} is finished");
        }

        private void ProcessImpl(Project project)
        {
            if (project.FilePath == null)
                throw new InvalidOperationException();
            Compilation? compilation = project.GetCompilationAsync().Result;
            if (compilation == null)
                throw new InvalidOperationException();
            if (!CompilationChecker.CheckCompilationErrors(project.FilePath, compilation, Logger))
                throw new InvalidOperationException();
            String projectDir = Path.GetDirectoryName(project.FilePath)!;
            foreach (Document file in project.Documents.Where(doc => doc.SourceCodeKind == SourceCodeKind.Regular))
            {
                // TODO (std_string) : check if file must be ignored
                String documentRelativeFilename = GetRelativeFilename(projectDir, file.FilePath!);
                _fileProcessor.Process(file, compilation);
            }
        }

        private ILogger Logger { get; }

        private readonly FileProcessor _fileProcessor;

        // TODO (std_string) : think about place
        private static String GetRelativeFilename(String projectDir, String filename)
        {
            return filename.Substring(projectDir.Length + 1);
        }
    }
}
