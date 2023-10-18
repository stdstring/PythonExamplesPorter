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

        public static void Foreach<TElement>(this IEnumerable<TElement> source, Action<TElement> action)
        {
            foreach (TElement element in source)
                action(element);
        }
    }
}
