using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Config
{
    internal static class AppConfigChecker
    {
        public static Tuple<Boolean, String[]> Check(AppConfig appConfig)
        {
            Boolean result = true;
            String[] supportedSourcesByExtension = {".csproj"};
            IList<String> problems = new List<String>();
            String source = appConfig.ConfigData.BaseConfig!.Source.ResolveTargetPath(appConfig);
            switch (File.Exists(source))
            {
                case false:
                    problems.Add($"\"{source}\" must be existing file");
                    result = false;
                    break;
                case true:
                    switch (Path.GetExtension(source))
                    {
                        case "":
                            problems.Add($"We don't support sources (files) without extension");
                            result = false;
                            break;
                        case var extension when !supportedSourcesByExtension.Contains(extension):
                            problems.Add($"We don't support sources with extension \"{extension}\"");
                            result = false;
                            break;
                    }
                    break;
            }
            String destDirectory = appConfig.ConfigData.BaseConfig.DestDirectory.ResolveTargetPath(appConfig);
            if (Directory.Exists(destDirectory) && !IsEmpty(destDirectory))
            {
                problems.Add($"\"{destDirectory}\" must be non existing or empty directory");
                result = false;
            }
            return new Tuple<Boolean, String[]>(result, problems.ToArray());
        }

        private static Boolean IsEmpty(String directory)
        {
            return (Directory.GetDirectories(directory).Length == 0) && (Directory.GetFiles(directory).Length == 0);
        }
    }
}
