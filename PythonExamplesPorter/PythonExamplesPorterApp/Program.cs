using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Processor;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine(AppDescription);
            switch (ConfigParser.Parse(args))
            {
                case ConfigResult.VersionConfig config:
                    Console.WriteLine($"Version: {config.Version}");
                    break;
                case ConfigResult.HelpConfig config:
                    Console.WriteLine(config.Help);
                    break;
                case ConfigResult.WrongConfig config:
                    Console.WriteLine(WrongConfig);
                    Console.WriteLine(config.Help);
                    break;
                case ConfigResult.MainConfig config:
                    AppConfig appConfig = AppConfigFactory.Create(config);
                    switch (AppConfigChecker.Check(appConfig))
                    {
                        case (true, _):
                            RunPorter(appConfig);
                            break;
                        case (false, var problems):
                            Console.WriteLine("There are the following problems with data:");
                            foreach (String problem in problems)
                                Console.WriteLine(problem);
                            break;
                    }
                    break;
            }
        }

        private static void RunPorter(AppConfig appConfig)
        {
            PrerequisitesManager.Run();
            ILogger logger = new ConsoleLogger(LogLevel.Info);
            IgnoredEntitiesManager ignoredManager = new IgnoredEntitiesManager(appConfig.ConfigData.IgnoredEntities);
            ProjectProcessor projectProcessor = new ProjectProcessor(appConfig, ignoredManager, logger);
            projectProcessor.Process(appConfig.ConfigData.BaseConfig!.Source);
            Console.WriteLine("That's all folks !!!");
        }

        private const String AppDescription = "C# to Python example porter";
        private const String WrongConfig = "Wrong config data";
    }
}