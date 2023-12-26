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
}
