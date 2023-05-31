using PythonExamplesPorterApp.Config;

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
                    RunPorter(config.Data);
                    break;
            }
        }

        private static void RunPorter(ConfigData configData)
        {
            Console.WriteLine("That's all folks !!!");
        }

        private const String AppDescription = "C# to Python example porter";
        private const String WrongConfig = "Wrong config data";
    }
}