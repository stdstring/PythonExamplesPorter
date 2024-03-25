using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Import;
using PythonExamplesPorterApp.Logger;
using PythonExamplesPorterApp.Names;
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
            try
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
            catch (Exception err)
            {
                errorWriter.WriteLine("Unhandled exception:");
                errorWriter.WriteLine(err.ToString());
                return 999;
            }
        }

        private static AppData CreateAppData(AppConfig appConfig, TextWriter outputWriter, TextWriter errorWriter)
        {
            ILogger logger = new TextWriterLogger(outputWriter, errorWriter, LogLevel.Info);
            INameTransformStrategy nameTransformStrategy = new SeparatedDigitsExceptSinglesNameConverter();
            IHandmadeNameManager handmadeNameManager = HandmadeNameManagerFactory.Create(appConfig.ConfigData.HandmadeAliases);
            NameTransformer nameTransformer = new NameTransformer(nameTransformStrategy, handmadeNameManager);
            IgnoredEntitiesManager ignoredManager = new IgnoredEntitiesManager(appConfig.ConfigData.IgnoredEntities);
            HandmadeEntitiesManager handmadeManager = new HandmadeEntitiesManager(appConfig.ConfigData.HandmadeEntities, nameTransformer);
            ImportAliasManager importAliasManager = new ImportAliasManager(appConfig.ConfigData.ImportAliases);
            return new AppData(appConfig, ignoredManager, handmadeManager, importAliasManager, nameTransformer, logger);
        }

        private static void RunPorter(AppConfig appConfig, TextWriter outputWriter, TextWriter errorWriter)
        {
            PrerequisitesManager.Run(appConfig);
            AppData appData = CreateAppData(appConfig, outputWriter, errorWriter);
            ProjectProcessor projectProcessor = new ProjectProcessor(appData);
            projectProcessor.Process(appData.AppConfig.ResolveSource());
            HandmadePostProcessor handmadePostProcessor = new HandmadePostProcessor(appData);
            handmadePostProcessor.Process();
            outputWriter.WriteLine("That's all folks !!!");
        }

        private const String AppDescription = "C# to Python example porter";
        private const String WrongConfig = "Wrong config data";
    }
}