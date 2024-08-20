using NUnit.Framework;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterAppTests.TestUtils
{
    internal static class RefTypeTestExtensions
    {
        public static T MustCheck<T>(this T? source) where T : class
        {
            Assert.That(source, Is.Not.Null);
            return source!;
        }

        public static TDest MustCheckCast<TSource, TDest>(this TSource? source)
            where TSource : class
            where TDest : class
        {
            TDest? dest = source.Must() as TDest;
            return dest.MustCheck();
        }
    }
}