using NUnit.Framework;
using PythonExamplesPorterApp.Ignored;

namespace PythonExamplesPorterAppTests.Ignored
{
    [TestFixture]
    public class IgnoredEntitiesManagerTests
    {
        [TestCase("aa1.cs", true)]
        [TestCase("aa2.cs", false)]
        [TestCase("some_folder\\aa1.cs", true)]
        [TestCase("other_folder\\aa1.cs", false)]
        public void IsIgnoredFile(String filename, Boolean expectedResult)
        {
            IgnoredEntitiesManager manager = new IgnoredEntitiesManager(_ignoredEntities);
            Assert.AreEqual(expectedResult, manager.IsIgnoredFile(filename));
        }

        [TestCase("aa1.cs")]
        [TestCase("aa2.cs")]
        [TestCase("some_folder\\aa1.cs")]
        [TestCase("other_folder\\aa1.cs")]
        public void IsIgnoredFileForEmpty(String filename)
        {
            IgnoredEntitiesManager managerForNull = new IgnoredEntitiesManager(null);
            IgnoredEntitiesManager managerForEmpty = new IgnoredEntitiesManager(new IgnoredEntities());
            Assert.AreEqual(false, managerForNull.IsIgnoredFile(filename));
            Assert.AreEqual(false, managerForEmpty.IsIgnoredFile(filename));
        }

        [TestCase("SomeNamespace.SomeType", true)]
        [TestCase("SomeNamespace.OtherType", false)]
        [TestCase("SomeType", false)]
        [TestCase("OtherNamespace.OtherType", true)]
        [TestCase("OtherNamespace.AnotherType", false)]
        [TestCase("XXXNamespace.YYYType", false)]
        public void IsIgnoredType(String fullName, Boolean expectedResult)
        {
            IgnoredEntitiesManager manager = new IgnoredEntitiesManager(_ignoredEntities);
            Assert.AreEqual(expectedResult, manager.IsIgnoredType(fullName));
        }

        [TestCase("SomeNamespace.SomeType")]
        [TestCase("SomeNamespace.OtherType")]
        [TestCase("SomeType")]
        [TestCase("OtherNamespace.OtherType")]
        [TestCase("OtherNamespace.AnotherType")]
        [TestCase("XXXNamespace.YYYType")]
        public void IsIgnoredTypeForEmpty(String fullName)
        {
            IgnoredEntitiesManager managerForNull = new IgnoredEntitiesManager(null);
            IgnoredEntitiesManager managerForEmpty = new IgnoredEntitiesManager(new IgnoredEntities());
            Assert.AreEqual(false, managerForNull.IsIgnoredType(fullName));
            Assert.AreEqual(false, managerForEmpty.IsIgnoredType(fullName));
        }

        [TestCase("SomeNamespace.SomeType.CheckAAA", true)]
        [TestCase("SomeType.CheckAAA", false)]
        [TestCase("CheckAAA", false)]
        [TestCase("SomeNamespace.SomeType.CheckAAB", false)]
        [TestCase("OtherNamespace.OtherType.CheckBBB", true)]
        [TestCase("AnotherNamespace.OtherType.CheckBBB", false)]
        [TestCase("XXXNamespace.YYYType.ZZZMethod", false)]
        public void IsIgnoredMethod(String fullName, Boolean expectedResult)
        {
            IgnoredEntitiesManager manager = new IgnoredEntitiesManager(_ignoredEntities);
            Assert.AreEqual(expectedResult, manager.IsIgnoredMethod(fullName));
        }

        [TestCase("SomeNamespace.SomeType.CheckAAA")]
        [TestCase("SomeType.CheckAAA")]
        [TestCase("CheckAAA")]
        [TestCase("SomeNamespace.SomeType.CheckAAB")]
        [TestCase("OtherNamespace.OtherType.CheckBBB")]
        [TestCase("AnotherNamespace.OtherType.CheckBBB")]
        [TestCase("XXXNamespace.YYYType.ZZZMethod")]
        public void IsIgnoredMethodForEmpty(String fullName)
        {
            IgnoredEntitiesManager managerForNull = new IgnoredEntitiesManager(null);
            IgnoredEntitiesManager managerForEmpty = new IgnoredEntitiesManager(new IgnoredEntities());
            Assert.AreEqual(false, managerForNull.IsIgnoredMethod(fullName));
            Assert.AreEqual(false, managerForEmpty.IsIgnoredMethod(fullName));
        }

        private readonly IgnoredEntities _ignoredEntities = new IgnoredEntities
        {
            Files = new[] {"aa1.cs", "ab1.cs", "some_folder\\aa1.cs"},
            Types = new[] {"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
            Methods = new[] {"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
        };
    }
}
