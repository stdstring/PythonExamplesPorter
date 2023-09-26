using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.MSBuild;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Processor
{
    internal class ProjectProcessor
    {
        public ProjectProcessor(AppData appData)
        {
            _appData = appData;
            _fileProcessor = new FileProcessor(appData);
        }

        public void Process(String projectFilename)
        {
            _appData.Logger.LogInfo($"Processing of the project {projectFilename} is started");
            MSBuildWorkspace workspace = MSBuildWorkspace.Create();
            Project project = workspace.OpenProjectAsync(projectFilename).Result;
            ProcessImpl(project);
            _appData.Logger.LogInfo($"Processing of the project {projectFilename} is finished");
        }

        private void ProcessImpl(Project project)
        {
            if (project.FilePath == null)
                throw new InvalidOperationException();
            Compilation? compilation = project.GetCompilationAsync().Result;
            if (compilation == null)
                throw new InvalidOperationException();
            if (!CompilationChecker.CheckCompilationErrors(project.FilePath, compilation, _appData.Logger))
                throw new InvalidOperationException();
            String projectDir = Path.GetDirectoryName(project.FilePath)!;
            foreach (Document document in project.Documents.Where(doc => doc.SourceCodeKind == SourceCodeKind.Regular))
            {
                String documentRelativePath = Path.GetRelativePath(projectDir, document.FilePath!);
                _fileProcessor.Process(documentRelativePath, document, compilation);
            }
        }

        private readonly AppData _appData;
        private readonly FileProcessor _fileProcessor;
    }
}
