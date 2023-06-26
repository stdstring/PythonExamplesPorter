using NUnit.Framework;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterAppTests.Converter
{
    [TestFixture]
    public class PathTransformerTests
    {
        [TestCase("Border.cs", "border.py")]
        [TestCase("ExBorder.cs", "ex_border.py")]
        [TestCase("Tests\\Border.cs", "tests\\border.py")]
        [TestCase("Tests\\ExBorder.cs", "tests\\ex_border.py")]
        [TestCase("SomeTests\\ExBorder.cs", "some_tests\\ex_border.py")]
        [TestCase("Outer\\Tests\\Border.cs", "outer\\tests\\border.py")]
        [TestCase("Outer\\Tests\\ExBorder.cs", "outer\\tests\\ex_border.py")]
        [TestCase("Outer\\SomeTests\\ExBorder.cs", "outer\\some_tests\\ex_border.py")]
        [TestCase("CurrentOuter\\SomeTests\\ExBorder.cs", "current_outer\\some_tests\\ex_border.py")]
        public void TransformPath(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, PathTransformer.TransformPath(source));
        }
    }
}
