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
            Assert.That(manager.IsIgnoredFile(filename), Is.EqualTo(expectedResult));
        }

        [TestCase("aa1.cs")]
        [TestCase("aa2.cs")]
        [TestCase("some_folder\\aa1.cs")]
        [TestCase("other_folder\\aa1.cs")]
        public void IsIgnoredFileForEmpty(String filename)
        {
            IgnoredEntitiesManager managerForNull = new IgnoredEntitiesManager(null);
            IgnoredEntitiesManager managerForEmpty = new IgnoredEntitiesManager(new IgnoredEntities());
            Assert.That(managerForNull.IsIgnoredFile(filename), Is.False);
            Assert.That(managerForEmpty.IsIgnoredFile(filename), Is.False);
        }

        [TestCase("ba1.cs", false)]
        [TestCase("SomeFolder1\\ba2.cs", true)]
        [TestCase("SomeFolder2\\ba3.cs", false)]
        [TestCase("SomeFolder2\\OtherFolder.cs", false)]
        [TestCase("SomeFolder2\\OtherFolder\\ba4.cs", true)]
        public void IsIgnoredFileViaDirectory(String filename, Boolean expectedResult)
        {
            IgnoredEntitiesManager manager = new IgnoredEntitiesManager(_ignoredEntities);
            Assert.That(manager.IsIgnoredFile(filename), Is.EqualTo(expectedResult));
        }

        [TestCase("ba1.cs")]
        [TestCase("SomeFolder1\\ba2.cs")]
        [TestCase("SomeFolder2\\ba3.cs")]
        [TestCase("SomeFolder2\\OtherFolder.cs")]
        [TestCase("SomeFolder2\\OtherFolder\\ba4.cs")]
        public void IsIgnoredFileViaDirectoryForEmpty(String filename)
        {
            IgnoredEntitiesManager managerForNull = new IgnoredEntitiesManager(null);
            IgnoredEntitiesManager managerForEmpty = new IgnoredEntitiesManager(new IgnoredEntities());
            Assert.That(managerForNull.IsIgnoredFile(filename), Is.False);
            Assert.That(managerForEmpty.IsIgnoredFile(filename), Is.False);
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
            Assert.That(manager.IsIgnoredType(fullName), Is.EqualTo(expectedResult));
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
            Assert.That(managerForNull.IsIgnoredType(fullName), Is.False);
            Assert.That(managerForEmpty.IsIgnoredType(fullName), Is.False);
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
            Assert.That(manager.IsIgnoredMethod(fullName), Is.EqualTo(expectedResult));
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
            Assert.That(managerForNull.IsIgnoredMethod(fullName), Is.False);
            Assert.That(managerForEmpty.IsIgnoredMethod(fullName), Is.False);
        }

        private readonly IgnoredEntities _ignoredEntities = new IgnoredEntities
        {
            Directories = new[] {"SomeFolder1", "SomeFolder2\\OtherFolder"},
            Files = new[] {"aa1.cs", "ab1.cs", "some_folder\\aa1.cs"},
            Types = new[] {"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
            Methods = new[] {"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
        };
    }
}
