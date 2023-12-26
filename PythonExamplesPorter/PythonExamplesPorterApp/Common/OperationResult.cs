namespace PythonExamplesPorterApp.Common
{
    internal record OperationResult<TData>(Boolean Success, String Reason = "", TData? Data = null) where TData : class;
}
