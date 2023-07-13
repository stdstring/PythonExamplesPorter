using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Config
{
    internal abstract record ConfigResult
    {
        internal record VersionConfig(String Version) : ConfigResult;

        internal record HelpConfig(String Help) : ConfigResult;

        internal record MainConfig(String ConfigPath) : ConfigResult;

        internal record WrongConfig(String Help) : ConfigResult;
    }

    internal static class ConfigParser
    {
        public static ConfigResult Parse(String[] args)
        {
            return args switch
            {
                [] => new ConfigResult.HelpConfig(Help),
                [HelpKey] => new ConfigResult.HelpConfig(Help),
                [VersionKey] => new ConfigResult.HelpConfig(Version),
                [var arg] when arg.StartsWith(ConfigKey) => ProcessMainConfig(arg),
                _ => new ConfigResult.WrongConfig(Help)
            };
        }

        private static ConfigResult ProcessMainConfig(String arg)
        {
            String configPath = arg.Substring(ConfigKey.Length);
            return new ConfigResult.MainConfig(configPath);
        }

        public const String ConfigKey = "--config=";

        public const String HelpKey = "--help";

        public const String VersionKey = "--version";

        public const String Version = "0.0.1";

        public const String Help = "Usage: <app> --config=<path to config file>";
    }

    // TODO (std_string) : think about duplication of BaseDirectory
    internal record AppConfig(String BaseDirectory, ConfigData ConfigData);

    internal static class AppConfigFactory
    {
        public static AppConfig Create(ConfigResult.MainConfig config)
        {
            using (StreamReader reader = new StreamReader(config.ConfigPath))
            {
                XmlSerializer serializer = new XmlSerializer(typeof(ConfigData));
                ConfigData? configData = serializer.Deserialize(reader) as ConfigData;
                if (configData == null ||
                    configData.BaseConfig == null)
                    throw new InvalidOperationException("Bad config data");
                String baseDirectory = configData.BaseConfig.BaseDirectory ?? AppDomain.CurrentDomain.BaseDirectory;
                return new AppConfig(baseDirectory, configData);
            }
        }
    }
}
