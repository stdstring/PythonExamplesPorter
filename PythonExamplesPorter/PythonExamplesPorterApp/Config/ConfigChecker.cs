namespace PythonExamplesPorterApp.Config
{
    internal static class ConfigDataChecker
    {
        public static Tuple<Boolean, String[]> Check(ConfigData data)
        {
            Boolean result = true;
            String[] supportedSourcesByExtension = {".csproj"};
            IList<String> problems = new List<String>();
            switch (File.Exists(data.Source))
            {
                case false:
                    problems.Add($"\"{data.Source}\" must be existing file");
                    result = false;
                    break;
                case true:
                    switch (Path.GetExtension(data.Source))
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
            if (Directory.Exists(data.DestDirectory) && !IsEmpty(data.DestDirectory))
            {
                problems.Add($"\"{data.DestDirectory}\" must be non existing or empty directory");
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
