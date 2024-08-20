using NUnit.Framework;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Names;
using PythonExamplesPorterAppTests.TestUtils;

namespace PythonExamplesPorterAppTests.Handmade
{
    [TestFixture]
    public class HandmadeEntitiesManagerTests
    {
        public HandmadeEntitiesManagerTests()
        {
            INameTransformStrategy transformStrategy = new SeparatedDigitsExceptSinglesNameConverter();
            IHandmadeNameManager manager = HandmadeNameManagerFactory.Create(null);
            _nameTransformer = new NameTransformer(transformStrategy, manager);
        }

        [TestCase("SomeNamespace.SomeTypeA", true)]
        [TestCase("SomeTypeA", false)]
        [TestCase("SomeNamespace.SomeTypeB", false)]
        [TestCase("OtherNamespace.SomeTypeB", true)]
        [TestCase("OtherNamespace.SomeTypeA", false)]
        [TestCase("XXXNamespace.YYYType", false)]
        public void IsHandmadeType(String fullName, Boolean expectedResult)
        {
            HandmadeEntitiesManager manager = new HandmadeEntitiesManager(_handmadeEntities, _nameTransformer);
            Assert.That(manager.IsHandmadeType(fullName), Is.EqualTo(expectedResult));
        }

        [TestCase("SomeNamespace.SomeTypeA")]
        [TestCase("SomeTypeA")]
        [TestCase("SomeNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeA")]
        [TestCase("XXXNamespace.YYYType")]
        public void IsHandmadeTypeForEmpty(String fullName)
        {
            HandmadeEntitiesManager managerForNull = new HandmadeEntitiesManager(null, _nameTransformer);
            HandmadeEntitiesManager managerForEmpty = new HandmadeEntitiesManager(new HandmadeEntities(), _nameTransformer);
            Assert.That(managerForNull.IsHandmadeType(fullName), Is.False);
            Assert.That(managerForEmpty.IsHandmadeType(fullName), Is.False);
        }

        [Test]
        public void UseHandmadeType()
        {
            HandmadeEntitiesManager manager = new HandmadeEntitiesManager(_handmadeEntities, _nameTransformer);
            foreach (String typename in new[] {"SomeNamespace.SomeTypeA", "SomeTypeA", "SomeNamespace.SomeTypeB", "XXXNamespace.YYYType"})
                Assert.DoesNotThrow(() => manager.UseHandmadeType(typename));
            HandmadeType[] expectedUsedHandmadeTypes = _handmadeEntities.HandmadeTypes!.Where(type => type.FullName == "SomeNamespace.SomeTypeA").ToArray();
            HandmadeType[] actualUsedHandmadeTypes = manager.GetUsedHandmadeTypes();
            Assert.That(actualUsedHandmadeTypes.Length, Is.EqualTo(expectedUsedHandmadeTypes.Length));
            for (Int32 index = 0; index < expectedUsedHandmadeTypes.Length; ++index)
            {
                Assert.That(actualUsedHandmadeTypes[index].FullName, Is.EqualTo(expectedUsedHandmadeTypes[index].FullName));
                Assert.That(actualUsedHandmadeTypes[index].Source, Is.EqualTo(expectedUsedHandmadeTypes[index].Source));
                Assert.That(actualUsedHandmadeTypes[index].Dest, Is.EqualTo(expectedUsedHandmadeTypes[index].Dest));
            }
        }

        [Test]
        public void UseHandmadeTypeForEmpty()
        {
            HandmadeEntitiesManager managerForNull = new HandmadeEntitiesManager(null, _nameTransformer);
            HandmadeEntitiesManager managerForEmpty = new HandmadeEntitiesManager(new HandmadeEntities(), _nameTransformer);
            foreach (String typename in new[] {"SomeNamespace.SomeTypeA", "SomeTypeA", "SomeNamespace.SomeTypeB", "XXXNamespace.YYYType"})
            {
                Assert.DoesNotThrow(() => managerForNull.UseHandmadeType(typename));
                Assert.DoesNotThrow(() => managerForEmpty.UseHandmadeType(typename));
            }
            Assert.That(managerForNull.GetUsedHandmadeTypes(), Is.Empty);
            Assert.That(managerForEmpty.GetUsedHandmadeTypes(), Is.Empty);
        }

        [TestCase("SomeNamespace.SomeTypeA")]
        [TestCase("SomeTypeA")]
        [TestCase("SomeNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeA")]
        [TestCase("XXXNamespace.YYYType")]
        public void GetHandmadeTypeMapping(String fullName)
        {
            HandmadeEntitiesManager manager = new HandmadeEntitiesManager(_handmadeEntities, _nameTransformer);
            HandmadeMemberMapping[] expected = _handmadeEntities
                .HandmadeTypes
                .MustCheck()
                .SingleOrDefault(type => type.FullName == fullName)?
                .MemberMappings ?? Array.Empty<HandmadeMemberMapping>();
            CheckMemberMappings(expected, manager.GetHandmadeTypeMapping(fullName));
        }

        [TestCase("SomeNamespace.SomeTypeA")]
        [TestCase("SomeTypeA")]
        [TestCase("SomeNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeA")]
        [TestCase("XXXNamespace.YYYType")]
        public void GetHandmadeTypeMappingForEmpty(String fullName)
        {
            HandmadeEntitiesManager managerForNull = new HandmadeEntitiesManager(null, _nameTransformer);
            HandmadeEntitiesManager managerForEmpty = new HandmadeEntitiesManager(new HandmadeEntities(), _nameTransformer);
            Assert.That(managerForNull.GetHandmadeTypeMapping(fullName), Is.Empty);
            Assert.That(managerForEmpty.GetHandmadeTypeMapping(fullName), Is.Empty);
        }

        private void CheckMemberMappings(HandmadeMemberMapping[] expected, IDictionary<String, MappingData> actual)
        {
            IDictionary<String, MappingData> expectedMap = expected.ToDictionary(mapping => mapping.SourceName, mapping => new MappingData(mapping.DestName, mapping.NeedImport));
            Assert.That(actual.Count, Is.EqualTo(expectedMap.Count));
            foreach (KeyValuePair<String, MappingData> expectedMapping in expectedMap)
            {
                Assert.That(actual.ContainsKey(expectedMapping.Key), Is.True);
                Assert.That(actual[expectedMapping.Key], Is.EqualTo(expectedMapping.Value));
            }
        }

        private readonly NameTransformer _nameTransformer;

        private readonly HandmadeEntities _handmadeEntities = new HandmadeEntities
        {
            HandmadeTypes = new[]
            {
                new HandmadeType
                {
                    FullName = "SomeNamespace.SomeTypeA",
                    Source = "SomeStorage\\some_typea.py",
                    Dest = "helpers\\some_typea.py"
                },
                new HandmadeType
                {
                    FullName = "OtherNamespace.SomeTypeB",
                    Source = "SomeStorage\\some_typeb.py",
                    Dest = "utils\\some_typeb.py",
                    MemberMappings = new []
                    {
                        new HandmadeMemberMapping{SourceName = "GetXXX", DestName = "get_super_xxx_value", NeedImport = true},
                        new HandmadeMemberMapping{SourceName = "SomePath", DestName = "SOME_PATH", NeedImport = false}
                    }
                }
            }
        };
    }
}
