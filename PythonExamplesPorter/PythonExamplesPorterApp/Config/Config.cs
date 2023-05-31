namespace PythonExamplesPorterApp.Config
{
    internal record ConfigData(String Source, String DestDirectory);

    internal abstract record ConfigResult
    {
        internal record VersionConfig(String Version) : ConfigResult;

        internal record HelpConfig(String Help) : ConfigResult;

        internal record MainConfig(ConfigData Data) : ConfigResult;

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
                _ => ProcessMainConfig(args)
            };
        }

        private static ConfigResult ProcessMainConfig(String[] args)
        {
            const Char keyValueDelimiter = '=';
            IDictionary<String, String> configData = new Dictionary<String, String>();
            foreach (String arg in args)
            {
                switch (arg.Split(keyValueDelimiter))
                {
                    case {Length: 2} parts:
                        configData[parts[0]] = parts[1];
                        break;
                    default:
                        return new ConfigResult.WrongConfig(Help);
                }
            }
            if (!CheckConfigKeys(configData))
                return new ConfigResult.WrongConfig(Help);
            ConfigData data = new ConfigData(configData[SourceKey], configData[DestKey]);
            return new ConfigResult.MainConfig(data);
        }

        private static bool CheckConfigKeys(IDictionary<String, String> configData)
        {
            // check mandatory keys
            String[] mandatoryKeys = {SourceKey, DestKey};
            if (mandatoryKeys.Any(key => !configData.ContainsKey(key) || String.IsNullOrEmpty(configData[key])))
                return false;
            // check actual keys
            ISet<String> allKeys = new HashSet<String> {SourceKey, DestKey};
            return configData.Keys.All(allKeys.Contains);
        }

        public const String SourceKey = "--source";

        public const String DestKey = "--dest";

        public const String HelpKey = "--help";

        public const String VersionKey = "--version";

        public const String Version = "0.0.1";

        public const String Help = "Usage: <app> " +
                                   "--source=<source project file(.csproj)> " +
                                   "--dest=<dest directory>";
    }
}
