using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Processor;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp
{
    internal class Program
    {
        public static Int32 Main(String[] args)
        {
            return MainImpl(args, Console.Out, Console.Error);
        }

        public static Int32 MainImpl(String[] args, TextWriter outputWriter, TextWriter errorWriter)
        {
            outputWriter.WriteLine(AppDescription);
            switch (ConfigParser.Parse(args))
            {
                case ConfigResult.VersionConfig config:
                    outputWriter.WriteLine($"Version: {config.Version}");
                    break;
                case ConfigResult.HelpConfig config:
                    outputWriter.WriteLine(config.Help);
                    break;
                case ConfigResult.WrongConfig config:
                    errorWriter.WriteLine(WrongConfig);
                    outputWriter.WriteLine(config.Help);
                    return 666;
                case ConfigResult.MainConfig config:
                    AppConfig appConfig = AppConfigFactory.Create(config);
                    switch (AppConfigChecker.Check(appConfig))
                    {
                        case (true, _):
                            RunPorter(appConfig, outputWriter, errorWriter);
                            break;
                        case (false, var problems):
                            errorWriter.WriteLine("There are the following problems with data:");
                            foreach (String problem in problems)
                                errorWriter.WriteLine(problem);
                            return 666;
                    }
                    break;
            }
            return 0;
        }

        private static void RunPorter(AppConfig appConfig, TextWriter outputWriter, TextWriter errorWriter)
        {
            PrerequisitesManager.Run();
            ILogger logger = new TextWriterLogger(outputWriter, errorWriter, LogLevel.Info);
            IgnoredEntitiesManager ignoredManager = new IgnoredEntitiesManager(appConfig.ConfigData.IgnoredEntities);
            HandmadeEntitiesManager handmadeManager = new HandmadeEntitiesManager(appConfig.ConfigData.HandmadeEntities);
            ProjectProcessor projectProcessor = new ProjectProcessor(appConfig, ignoredManager, handmadeManager, logger);
            projectProcessor.Process(appConfig.ConfigData.BaseConfig!.Source);
            HandmadePostProcessor handmadePostProcessor = new HandmadePostProcessor(appConfig);
            handmadePostProcessor.Process(handmadeManager.GetUsedHandmadeTypes());
            outputWriter.WriteLine("That's all folks !!!");
        }

        private const String AppDescription = "C# to Python example porter";
        private const String WrongConfig = "Wrong config data";
    }
}