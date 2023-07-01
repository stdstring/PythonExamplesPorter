using System.Xml.Serialization;
using NUnit.Framework;
using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterAppTests.Config
{
    [TestFixture]
    public class ConfigDataSerializationTests
    {
        [Test]
        public void DeserializeWithBaseConfigOnly()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"}
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithEmptyIgnoredEntities()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities/>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                IgnoredEntities = new IgnoredEntities
                {
                    Files = Array.Empty<String>(),
                    Types = Array.Empty<String>(),
                    Methods = Array.Empty<String>()
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithIgnoredFiles()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Files>\r\n" +
                                  "      <File>aa1.cs</File>\r\n" +
                                  "      <File>ab1.cs</File>\r\n" +
                                  "      <File>some_folder\\aa1.cs</File>\r\n" +
                                  "    </Files>\r\n" +
                                  "  </IgnoredEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                IgnoredEntities = new IgnoredEntities
                {
                    Files = new[] { "aa1.cs", "ab1.cs", "some_folder\\aa1.cs" },
                    Types = Array.Empty<String>(),
                    Methods = Array.Empty<String>()
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithIgnoredTypes()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Types>\r\n" +
                                  "      <Type>SomeNamespace.SomeType</Type>\r\n" +
                                  "      <Type>OtherNamespace.OtherType</Type>\r\n" +
                                  "    </Types>\r\n" +
                                  "  </IgnoredEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                IgnoredEntities = new IgnoredEntities
                {
                    Files = Array.Empty<String>(),
                    Types = new []{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
                    Methods = Array.Empty<String>()
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithIgnoredMethods()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Methods>\r\n" +
                                  "      <Method>SomeNamespace.SomeType.CheckAAA</Method>\r\n" +
                                  "      <Method>OtherNamespace.OtherType.CheckBBB</Method>\r\n" +
                                  "    </Methods>\r\n" +
                                  "  </IgnoredEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                IgnoredEntities = new IgnoredEntities
                {
                    Files = Array.Empty<String>(),
                    Types = Array.Empty<String>(),
                    Methods = new []{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithIgnoredEntities()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Files>\r\n" +
                                  "      <File>aa1.cs</File>\r\n" +
                                  "      <File>ab1.cs</File>\r\n" +
                                  "      <File>some_folder\\aa1.cs</File>\r\n" +
                                  "    </Files>\r\n" +
                                  "    <Types>\r\n" +
                                  "      <Type>SomeNamespace.SomeType</Type>\r\n" +
                                  "      <Type>OtherNamespace.OtherType</Type>\r\n" +
                                  "    </Types>\r\n" +
                                  "    <Methods>\r\n" +
                                  "      <Method>SomeNamespace.SomeType.CheckAAA</Method>\r\n" +
                                  "      <Method>OtherNamespace.OtherType.CheckBBB</Method>\r\n" +
                                  "    </Methods>\r\n" +
                                  "  </IgnoredEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                IgnoredEntities = new IgnoredEntities
                {
                    Files = new[] { "aa1.cs", "ab1.cs", "some_folder\\aa1.cs" },
                    Types = new []{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
                    Methods = new []{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
                }
            };
            CheckDeserialization(expected, source);
        }

        private void CheckDeserialization(ConfigData expected, String actualSource)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(ConfigData));
            using (StringReader reader = new StringReader(actualSource))
            {
                ConfigData? actual = serializer.Deserialize(reader) as ConfigData;
                Assert.IsNotNull(actual);
                CheckConfigData(expected, actual!);
            }
        }

        private void CheckConfigData(ConfigData expected, ConfigData actual)
        {
            Assert.IsNotNull(actual.BaseConfig);
            CheckBaseConfig(expected.BaseConfig!, actual.BaseConfig!);
            CheckIgnoredEntities(expected.IgnoredEntities, actual.IgnoredEntities);
        }

        private void CheckBaseConfig(BaseConfig expected, BaseConfig actual)
        {
            Assert.AreEqual(expected.Source, actual.Source);
            Assert.AreEqual(expected.DestDirectory, actual.DestDirectory);
        }

        private void CheckIgnoredEntities(IgnoredEntities? expected, IgnoredEntities? actual)
        {
            if (expected ==  null)
                Assert.IsNull(actual);
            else
            {
                CheckCollections(expected.Files!, actual!.Files);
                CheckCollections(expected.Types!, actual.Types);
                CheckCollections(expected.Methods!, actual.Methods);
            }
        }

        private void CheckCollections(String[] expected, String[]? actual)
        {
            if (expected.Length == 0)
                Assert.That(actual == null || actual.Length == 0);
            else
            {
                Assert.IsNotNull(actual);
                Assert.AreEqual(expected.Length, actual!.Length);
                String[] expectedCollection = expected.Order().ToArray();
                String[] actualCollection = actual.Order().ToArray();
                for (Int32 index = 0; index < expectedCollection.Length; ++index)
                    Assert.AreEqual(expectedCollection[index], actualCollection[index]);
            }
        }
    }
}
