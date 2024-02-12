using Microsoft.Build.Locator;
using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterApp.Utils
{
    internal static class PrerequisitesManager
    {
        public static void Run(AppConfig appConfig)
        {
            // usage of MSBuild
            MSBuildLocator.RegisterDefaults();
            // recreate dest directory
            String destDirectory = appConfig.ResolveDestDirectory();
            if (Directory.Exists(destDirectory))
                Directory.Delete(destDirectory, true);
            Directory.CreateDirectory(destDirectory);
        }
    }
}
