using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Common
{
    internal abstract record OperationResult<TData>
    {
        internal record Ok(TData Data) : OperationResult<TData>;

        internal record Error(String Reason) : OperationResult<TData>;
    }

    internal static class OperationResultExtensions
    {
        public static TData MustSuccess<TData>(this OperationResult<TData> result, String errorTemplate = "")
        {
            return result switch
            {
                OperationResult<TData>.Ok(Data: var data) => data,
                OperationResult<TData>.Error(Reason: var reason) =>
                    throw new UnsupportedSyntaxException(String.IsNullOrEmpty(errorTemplate) ? reason : String.Format(errorTemplate, reason)),
                _ => throw new InvalidOperationException("Unexpected control flow branch")
            };
        }
    }
}
