using Microsoft.Build.Locator;

namespace PythonExamplesPorterApp.Utils
{
    internal static class PrerequisitesManager
    {
        public static void Run()
        {
            MSBuildLocator.RegisterDefaults();
        }
    }
}
