using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Common
{
    internal record AppData(AppConfig AppConfig, IgnoredEntitiesManager IgnoredManager, HandmadeEntitiesManager HandmadeManager, ILogger Logger);
}
