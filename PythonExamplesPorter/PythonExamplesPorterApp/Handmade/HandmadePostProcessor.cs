using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterApp.Handmade
{
    internal class HandmadePostProcessor
    {
        public HandmadePostProcessor(AppData appData)
        {
            _appData = appData;
        }

        public void Process(HandmadeType[] usedTypes)
        {
            String destDirectory = _appData.AppConfig.ResolveDestDirectory();
            foreach (HandmadeType usedType in usedTypes)
            {
                String sourcePath = Path.Combine(_appData.AppConfig.ConfigBaseDirectory, usedType.Source);
                String destPath = Path.Combine(destDirectory, usedType.Dest);
                File.Copy(sourcePath, destPath, true);
            }
        }

        private readonly AppData _appData;
    }
}
