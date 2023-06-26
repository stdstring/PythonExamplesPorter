namespace PythonExamplesPorterApp.Utils
{
    internal static class EnumerableUtils
    {
        public static Boolean IsEmpty<TElement>(this IEnumerable<TElement> source)
        {
            return !source.Any();
        }

        public static Boolean IsEmpty<TElement>(this IList<TElement> source)
        {
            return source.Count == 0;
        }
    }
}
