namespace PythonExamplesPorterApp.Logger
{
    internal enum LogLevel
    {
        Info,
        Warning,
        Error
    }

    internal interface ILogger
    {
        LogLevel Level { get; }

        void LogInfo(String message);

        void LogWarning(String message);

        void LogError(String message);

        void LogFatal(String message);
    }
}
