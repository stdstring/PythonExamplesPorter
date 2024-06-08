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
            Assert.That(StringUtils.Escape(source), Is.EqualTo(expected));
        }

        [TestCase("", "")]
        [TestCase("abcd", "abcd")]
        [TestCase("abcd efgh", "abcd efgh")]
        [TestCase("a\\t\\r\\nbc", "a\\t\\r\\nbc")]
        [TestCase("a\\u00A7bcd", "a\\u00A7bcd")]
        [TestCase("a\\U000000A7bcd", "a\\U000000A7bcd")]
        [TestCase("z\\x7zz", "z\\u0007zz")]
        [TestCase("z\\x7Azz", "z\\u007azz")]
        [TestCase("z\\x7Abzz", "z\\u07abzz")]
        [TestCase("z\\x7AbCzz", "z\\u7abczz")]
        [TestCase("z\\x7AbCcc", "z\\u7abccc")]
        public void ConvertEscapeSequences(String source, String expected)
        {
            Assert.That(StringUtils.ConvertEscapeSequences(source), Is.EqualTo(expected));
        }

        [TestCase("", "")]
        [TestCase("abcd", "abcd")]
        [TestCase("abcd efgh", "abcd efgh")]
        [TestCase(@"\a\b\c\d\", "\\\\a\\\\b\\\\c\\\\d\\\\")]
        public void PrepareVerbatimString(String source, String expected)
        {
            Assert.That(StringUtils.PrepareVerbatimString(source), Is.EqualTo(expected));
        }
    }
}
