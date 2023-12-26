namespace PythonExamplesPorterApp.Converter
{
    internal class UnsupportedSyntaxException : Exception
    {
        public UnsupportedSyntaxException(String reason) : base(reason)
        {
        }

        public UnsupportedSyntaxException(String reason, Exception innerException) : base(reason, innerException)
        {
        }
    }
}
