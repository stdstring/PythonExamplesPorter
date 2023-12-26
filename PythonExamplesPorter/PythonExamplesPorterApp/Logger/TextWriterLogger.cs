namespace PythonExamplesPorterApp.Logger
{
    internal class TextWriterLogger : ILogger
    {
        public TextWriterLogger(TextWriter outputWriter, TextWriter errorWriter, LogLevel level)
        {
            _outputWriter = outputWriter;
            _errorWriter = errorWriter;
            Level = level;
        }

        public LogLevel Level { get; init; }

        public void LogInfo(String message)
        {
            if (Level > LogLevel.Info)
                return;
            _outputWriter.WriteLine($"[INFO]: {message}");
        }

        public void LogWarning(String message)
        {
            if (Level > LogLevel.Warning)
                return;
            _outputWriter.WriteLine($"[WARNING]: {message}");
        }

        public void LogError(String message)
        {
            if (Level > LogLevel.Error)
                return;
            _errorWriter.WriteLine($"[ERROR]: {message}");
        }

        public void LogFatal(String message)
        {
            _errorWriter.WriteLine($"[FATAL]: {message}");
        }

        private readonly TextWriter _outputWriter;
        private readonly TextWriter _errorWriter;
    }
}
