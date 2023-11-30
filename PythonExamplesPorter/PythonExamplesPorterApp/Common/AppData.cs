using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterApp.Common
{
    internal record AppData(AppConfig AppConfig,
                            IgnoredEntitiesManager IgnoredManager,
                            HandmadeEntitiesManager HandmadeManager,
                            NameTransformer NameTransformer,
                            ILogger Logger);
}
