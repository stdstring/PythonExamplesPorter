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

        [TestCase("SomeNamespace", "somenamespace")]
        [TestCase("SomeNamespace.OtherNamespace", "somenamespace.othernamespace")]
        [TestCase("SomeNamespace.OtherNamespace.AnotherNamespace", "somenamespace.othernamespace.anothernamespace")]
        [TestCase("Namespace1", "namespace1")]
        [TestCase("Namespace1.Namespace2", "namespace1.namespace2")]
        public void TransformNamespaceName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformNamespaceName(source));
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

        [TestCase("Border", "border")]
        [TestCase("BorderStart", "border_start")]
        [TestCase("SuperBorderStart", "super_border_start")]
        [TestCase("AbsoluteSuperBorderStart", "absolute_super_border_start")]
        public void TransformPropertyName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformPropertyName(source));
        }

        [TestCase("Field", "field")]
        [TestCase("BorderField", "border_field")]
        [TestCase("SuperBorderField", "super_border_field")]
        [TestCase("AbsoluteSuperBorderField", "absolute_super_border_field")]
        public void TransformFieldName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformFieldName(source));
        }

        [TestCase("Item", "ITEM")]
        [TestCase("BorderItem", "BORDER_ITEM")]
        [TestCase("SuperBorderItem", "SUPER_BORDER_ITEM")]
        [TestCase("AbsoluteSuperBorderItem", "ABSOLUTE_SUPER_BORDER_ITEM")]
        public void TransformEnumValueName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformEnumValueName(source));
        }

        [TestCase("data", "data")]
        [TestCase("someData", "some_data")]
        [TestCase("someDataValue", "some_data_value")]
        public void TransformLocalVariableName(String source, String expectedResult)
        {
            Assert.AreEqual(expectedResult, NameTransformer.TransformLocalVariableName(source));
        }
    }
}
