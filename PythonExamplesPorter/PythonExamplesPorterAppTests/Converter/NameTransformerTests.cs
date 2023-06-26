using NUnit.Framework;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterAppTests.Converter
{
    [TestFixture]
    public class NameTransformerTests
    {
        [TestCase("border", "border")]
        [TestCase("Border", "border")]
        [TestCase("ExBorder", "ex_border")]
        [TestCase("ExSuperBorder", "ex_super_border")]
        [TestCase("ExAbsoluteSuperBorder", "ex_absolute_super_border")]
        public void TransformFileObjectName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformFileObjectName(source));
        }

        [TestCase("Border", "Border")]
        [TestCase("ExBorder", "ExBorder")]
        [TestCase("ExSuperBorder", "ExSuperBorder")]
        [TestCase("ExAbsoluteSuperBorder", "ExAbsoluteSuperBorder")]
        public void TransformClassName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformClassName(source));
        }

        [TestCase("Calculate", "calculate")]
        [TestCase("CalculateBorder", "calculate_border")]
        [TestCase("CalculateSuperBorder", "calculate_super_border")]
        [TestCase("CalculateAbsoluteSuperBorder", "calculate_absolute_super_border")]
        public void TransformMethodName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformMethodName(source));
        }
    }
}
