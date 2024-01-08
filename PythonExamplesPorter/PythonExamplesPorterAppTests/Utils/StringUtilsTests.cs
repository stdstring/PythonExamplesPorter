using NUnit.Framework;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterAppTests.Utils
{
    [TestFixture]
    public class StringUtilsTests
    {
        [TestCase("", "")]
        [TestCase("abcd", "abcd")]
        [TestCase("abcd efgh", "abcd efgh")]
        [TestCase("\"abcd\" \"efgh\"", "\\\"abcd\\\" \\\"efgh\\\"")]
        [TestCase("\"abcd\"\t\r\n \"efgh\" - \\", "\\\"abcd\\\"\\\\t\\\\r\\\\n \\\"efgh\\\" - \\\\")]
        public void Escape(String source, String expected)
        {
            Assert.AreEqual(expected, StringUtils.Escape(source));
        }
    }
}
