using NUnit.Framework;
using PythonExamplesPorterApp.Handmade;

namespace PythonExamplesPorterAppTests.Handmade
{
    [TestFixture]
    internal class HandmadeEntitiesManagerTests
    {
        [TestCase("SomeNamespace.SomeTypeA", true)]
        [TestCase("SomeTypeA", false)]
        [TestCase("SomeNamespace.SomeTypeB", false)]
        [TestCase("OtherNamespace.SomeTypeB", true)]
        [TestCase("OtherNamespace.SomeTypeA", false)]
        [TestCase("XXXNamespace.YYYType", false)]
        public void IsHandmadeType(String fullName, Boolean expectedResult)
        {
            HandmadeEntitiesManager manager = new HandmadeEntitiesManager(_handmadeEntities);
            Assert.AreEqual(expectedResult, manager.IsHandmadeType(fullName));
        }

        [TestCase("SomeNamespace.SomeTypeA")]
        [TestCase("SomeTypeA")]
        [TestCase("SomeNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeA")]
        [TestCase("XXXNamespace.YYYType")]
        public void IsHandmadeTypeForEmpty(String fullName)
        {
            HandmadeEntitiesManager managerForNull = new HandmadeEntitiesManager(null);
            HandmadeEntitiesManager managerForEmpty = new HandmadeEntitiesManager(new HandmadeEntities());
            Assert.AreEqual(false, managerForNull.IsHandmadeType(fullName));
            Assert.AreEqual(false, managerForEmpty.IsHandmadeType(fullName));
        }

        [Test]
        public void UseHandmadeType()
        {
            HandmadeEntitiesManager manager = new HandmadeEntitiesManager(_handmadeEntities);
            foreach (String typename in new[] {"SomeNamespace.SomeTypeA", "SomeTypeA", "SomeNamespace.SomeTypeB", "XXXNamespace.YYYType"})
                Assert.DoesNotThrow(() => manager.UseHandmadeType(typename));
            HandmadeType[] expectedUsedHandmadeTypes = _handmadeEntities.HandmadeTypes!.Where(type => type.FullName == "SomeNamespace.SomeTypeA").ToArray();
            HandmadeType[] actualUsedHandmadeTypes = manager.GetUsedHandmadeTypes();
            Assert.AreEqual(expectedUsedHandmadeTypes.Length, actualUsedHandmadeTypes.Length);
            for (Int32 index = 0; index < expectedUsedHandmadeTypes.Length; ++index)
            {
                Assert.AreEqual(expectedUsedHandmadeTypes[index].FullName, actualUsedHandmadeTypes[index].FullName);
                Assert.AreEqual(expectedUsedHandmadeTypes[index].Source, actualUsedHandmadeTypes[index].Source);
                Assert.AreEqual(expectedUsedHandmadeTypes[index].Dest, actualUsedHandmadeTypes[index].Dest);
            }
        }

        [Test]
        public void UseHandmadeTypeForEmpty()
        {
            HandmadeEntitiesManager managerForNull = new HandmadeEntitiesManager(null);
            HandmadeEntitiesManager managerForEmpty = new HandmadeEntitiesManager(new HandmadeEntities());
            foreach (String typename in new[] {"SomeNamespace.SomeTypeA", "SomeTypeA", "SomeNamespace.SomeTypeB", "XXXNamespace.YYYType"})
            {
                Assert.DoesNotThrow(() => managerForNull.UseHandmadeType(typename));
                Assert.DoesNotThrow(() => managerForEmpty.UseHandmadeType(typename));
            }
            Assert.IsEmpty(managerForNull.GetUsedHandmadeTypes());
            Assert.IsEmpty(managerForEmpty.GetUsedHandmadeTypes());
        }

        [TestCase("SomeNamespace.SomeTypeA")]
        [TestCase("SomeTypeA")]
        [TestCase("SomeNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeB")]
        [TestCase("OtherNamespace.SomeTypeA")]
        [TestCase("XXXNamespace.YYYType")]
        public void GetHandmadeTypeMapping(String fullName)
        {
            HandmadeEntitiesManager manager = new HandmadeEntitiesManager(_handmadeEntities);
            HandmadeMemberMapping[] expected = _handmadeEntities
                .HandmadeTypes!
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
            HandmadeEntitiesManager managerForNull = new HandmadeEntitiesManager(null);
            HandmadeEntitiesManager managerForEmpty = new HandmadeEntitiesManager(new HandmadeEntities());
            Assert.IsEmpty(managerForNull.GetHandmadeTypeMapping(fullName));
            Assert.IsEmpty(managerForEmpty.GetHandmadeTypeMapping(fullName));
        }

        private void CheckMemberMappings(HandmadeMemberMapping[] expected, IDictionary<String, String> actual)
        {
            IDictionary<String, String> expectedMap = expected.ToDictionary(mapping => mapping.SourceName, mapping => mapping.DestName);
            Assert.AreEqual(expectedMap.Count, actual.Count);
            foreach (KeyValuePair<String, String> expectedMapping in expectedMap)
            {
                Assert.IsTrue(actual.ContainsKey(expectedMapping.Key));
                Assert.AreEqual(expectedMapping.Value, actual[expectedMapping.Key]);
            }
        }

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
                        new HandmadeMemberMapping{SourceName = "GetXXX", DestName = "get_super_xxx_value"},
                        new HandmadeMemberMapping{SourceName = "SomePath", DestName = "SOME_PATH"}
                    }
                }
            }
        };
    }
}
