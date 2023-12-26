using Microsoft.Build.Locator;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.MSBuild;
using NUnit.Framework;
using System.Reflection;

namespace SolutionStructureTests
{
    [TestFixture]
    public class SolutionStructureExplorerTests
    {
        public SolutionStructureExplorerTests()
        {
            MSBuildLocator.RegisterDefaults();
        }

        [Test]
        public void ShowThisSolutionStructure()
        {
            String currentDir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ?? ".";
            MSBuildWorkspace workspace = MSBuildWorkspace.Create();
            Solution solution = workspace.OpenSolutionAsync(Path.Combine(currentDir, "..//..//..//..//PythonExamplesPorter.sln")).Result;
            foreach (ProjectId projectId in solution.GetProjectDependencyGraph().GetTopologicallySortedProjects())
            {
                Project? project = solution.GetProject(projectId);
                Assert.NotNull(project);
                String projectRoot = Path.GetDirectoryName(project!.FilePath) + "\\";
                Console.WriteLine("project : {0}, path : {1}", project.Name, project.FilePath);
                foreach (Document document in project.Documents)
                {
                    Assert.NotNull(document.FilePath);
                    Console.WriteLine("    file : {0}", document.FilePath!.Substring(projectRoot.Length));
                }
                Console.WriteLine();
            }
        }
    }
}