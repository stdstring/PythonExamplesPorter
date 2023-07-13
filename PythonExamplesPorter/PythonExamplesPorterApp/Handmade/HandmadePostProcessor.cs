using PythonExamplesPorterApp.Config;

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
            String baseDirectory = _appConfig.BaseDirectory;
            String destDirectory = Path.Combine(baseDirectory, _appConfig.ConfigData.BaseConfig!.DestDirectory);
            foreach (HandmadeType usedType in usedTypes)
            {
                String sourcePath = Path.Combine(baseDirectory, usedType.Source);
                String destPath = Path.Combine(destDirectory, usedType.Dest);
                File.Copy(sourcePath, destPath, true);
            }
        }

        private readonly AppConfig _appConfig;
    }
}
