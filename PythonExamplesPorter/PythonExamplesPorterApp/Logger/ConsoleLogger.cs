namespace PythonExamplesPorterApp.Logger
{
    internal class ConsoleLogger : ILogger
    {
        public ConsoleLogger(LogLevel level)
        {
            Level = level;
        }

        public LogLevel Level { get; init; }

        public void LogInfo(String message)
        {
            if (Level > LogLevel.Info)
                return;
            Console.Out.WriteLine($"[INFO]: {message}");
        }

        public void LogWarning(String message)
        {
            if (Level > LogLevel.Warning)
                return;
            Console.Out.WriteLine($"[WARNING]: {message}");
        }

        public void LogError(String message)
        {
            if (Level > LogLevel.Error)
                return;
            Console.Error.WriteLine($"[ERROR]: {message}");
        }

        public void LogFatal(String message)
        {
            Console.Error.WriteLine($"[FATAL]: {message}");
        }
    }
}
