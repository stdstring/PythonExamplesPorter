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
            foreach (HandmadeType usedType in usedTypes)
            {
                String sourcePath = Path.Combine(_appConfig.BaseDirectory, usedType.Source);
                String destPath = Path.Combine(_appConfig.BaseDirectory, usedType.Dest);
                File.Copy(sourcePath, destPath, true);
            }
        }

        private readonly AppConfig _appConfig;
    }
}
