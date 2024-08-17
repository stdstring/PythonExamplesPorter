using PythonExamplesPorterApp.Utils;
using System.Xml.Serialization;

namespace PythonExamplesPorterApp.Config
{
    internal record AppConfig(ConfigData ConfigData, String AppBaseDirectory, String ConfigBaseDirectory);

    internal static class AppConfigExtensions
    {
        public static SourceDetails GetSourceDetails(this AppConfig appConfig)
        {
            return appConfig.ConfigData.BaseConfig.Must("Bad config").SourceDetails ?? new SourceDetails();
        }

        public static String ResolveSource(this AppConfig appConfig)
        {
            return appConfig.ConfigData.BaseConfig.Must("Bad config").Source.ResolveTargetPath(appConfig);
        }

        public static String ResolveDestDirectory(this AppConfig appConfig)
        {
            return appConfig.ConfigData.BaseConfig.Must("Bad config").DestDirectory.ResolveTargetPath(appConfig);
        }
    }

    internal static class AppConfigFactory
    {
        public static AppConfig Create(ConfigResult.MainConfig config)
        {
            using (StreamReader reader = new StreamReader(config.ConfigPath))
            {
                XmlSerializer serializer = new XmlSerializer(typeof(ConfigData));
                ConfigData configData = serializer.Deserialize(reader).MustCast<Object, ConfigData>("Bad config data");
                configData.BaseConfig.Must("Bad config data");
                String appBaseDirectory = Path.GetFullPath(AppDomain.CurrentDomain.BaseDirectory);
                String configBaseDirectory = Path.GetFullPath(Path.GetDirectoryName(config.ConfigPath)!);
                return new AppConfig(configData, appBaseDirectory, configBaseDirectory);
            }
        }
    }
}