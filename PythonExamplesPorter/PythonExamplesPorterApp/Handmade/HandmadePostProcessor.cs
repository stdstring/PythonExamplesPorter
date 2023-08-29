using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Handmade
{
    internal class HandmadePostProcessor
    {
        public HandmadePostProcessor(AppConfig appConfig)
        {
            _appConfig = appConfig;
        }

        public void Process(HandmadeType[] usedTypes)
        {
            String destDirectory = _appConfig.ConfigData.BaseConfig!.DestDirectory.ResolveTargetPath(_appConfig);
            foreach (HandmadeType usedType in usedTypes)
            {
                String sourcePath = Path.Combine(_appConfig.ConfigBaseDirectory, usedType.Source);
                String destPath = Path.Combine(destDirectory, usedType.Dest);
                File.Copy(sourcePath, destPath, true);
            }
        }

        private readonly AppConfig _appConfig;
    }
}
