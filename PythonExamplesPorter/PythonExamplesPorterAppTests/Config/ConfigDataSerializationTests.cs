using System.Xml.Serialization;
using NUnit.Framework;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;

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
        public void DeserializeWithBaseConfigOnlyWithBaseDirectory()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>.\\result</Dest>\r\n" +
                                  "    <BaseDirectory>C:\\dest\\examples</BaseDirectory>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = ".\\result", BaseDirectory = "C:\\dest\\examples"}
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
                    Files = new[] {"aa1.cs", "ab1.cs", "some_folder\\aa1.cs"},
                    Types = new []{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
                    Methods = new []{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithEmptyHandmadeEntities()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <HandmadeEntities/>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                HandmadeEntities = new HandmadeEntities{HandmadeTypes = Array.Empty<HandmadeType>()}
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithHandmadeTypes()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source>C:\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest>C:\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <HandmadeEntities>\r\n" +
                                  "    <Types>\r\n" +
                                  "      <Type FullName=\"SomeNamespace.SomeTypeA\">\r\n" +
                                  "        <Source>SomeStorage\\some_typea.py</Source>\r\n" +
                                  "        <Dest>helpers\\some_typea.py</Dest>\r\n" +
                                  "      </Type>\r\n" +
                                  "      <Type FullName=\"OtherNamespace.SomeTypeB\">\r\n" +
                                  "        <Source>SomeStorage\\some_typeb.py</Source>\r\n" +
                                  "        <Dest>utils\\some_typeb.py</Dest>\r\n" +
                                  "        <MemberMapping>\r\n" +
                                  "          <Member SourceName=\"GetXXX\" DestName=\"get_super_xxx_value\"/>\r\n" +
                                  "          <Member SourceName=\"SomePath\" DestName=\"SOME_PATH\"/>\r\n" +
                                  "        </MemberMapping>\r\n" +
                                  "      </Type>\r\n" +
                                  "    </Types>\r\n" +
                                  "  </HandmadeEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                HandmadeEntities = new HandmadeEntities
                {
                    HandmadeTypes = new []
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
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeFull()
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
                                  "  <HandmadeEntities>\r\n" +
                                  "    <Types>\r\n" +
                                  "      <Type FullName=\"SomeNamespace.SomeTypeA\">\r\n" +
                                  "        <Source>SomeStorage\\some_typea.py</Source>\r\n" +
                                  "        <Dest>helpers\\some_typea.py</Dest>\r\n" +
                                  "      </Type>\r\n" +
                                  "      <Type FullName=\"OtherNamespace.SomeTypeB\">\r\n" +
                                  "        <Source>SomeStorage\\some_typeb.py</Source>\r\n" +
                                  "        <Dest>utils\\some_typeb.py</Dest>\r\n" +
                                  "        <MemberMapping>\r\n" +
                                  "          <Member SourceName=\"GetXXX\" DestName=\"get_super_xxx_value\"/>\r\n" +
                                  "          <Member SourceName=\"SomePath\" DestName=\"SOME_PATH\"/>\r\n" +
                                  "        </MemberMapping>\r\n" +
                                  "      </Type>\r\n" +
                                  "    </Types>\r\n" +
                                  "  </HandmadeEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig {Source = "C:\\source\\someproj.csproj", DestDirectory = "C:\\dest\\examples"},
                IgnoredEntities = new IgnoredEntities
                {
                    Files = new[] { "aa1.cs", "ab1.cs", "some_folder\\aa1.cs" },
                    Types = new []{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
                    Methods = new []{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
                },
                HandmadeEntities = new HandmadeEntities
                {
                    HandmadeTypes = new []
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
            CheckHandmadeEntities(expected.HandmadeEntities, actual.HandmadeEntities);
        }

        private void CheckBaseConfig(BaseConfig expected, BaseConfig actual)
        {
            Assert.AreEqual(expected.Source, actual.Source);
            Assert.AreEqual(expected.DestDirectory, actual.DestDirectory);
            Assert.AreEqual(expected.BaseDirectory, actual.BaseDirectory);
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
                for (Int32 index = 0; index < expected.Length; ++index)
                    Assert.AreEqual(expected[index], actual[index]);
            }
        }

        private void CheckHandmadeEntities(HandmadeEntities? expected, HandmadeEntities? actual)
        {
            if (expected == null)
                Assert.IsNull(actual);
            else
                CheckHandmadeTypes(expected.HandmadeTypes, actual!.HandmadeTypes);
        }

        private void CheckHandmadeTypes(HandmadeType[]? expected, HandmadeType[]? actual)
        {
            if (expected == null || expected.Length == 0)
                Assert.That(actual == null || actual.Length == 0);
            else
            {
                Assert.IsNotNull(actual);
                Assert.AreEqual(expected.Length, actual!.Length);
                for (Int32 index = 0; index < expected.Length; ++index)
                    CheckHandmadeType(expected[index], actual[index]);
            }
        }

        private void CheckHandmadeType(HandmadeType expected, HandmadeType actual)
        {
            Assert.AreEqual(expected.FullName, actual.FullName);
            Assert.AreEqual(expected.Source, actual.Source);
            Assert.AreEqual(expected.Dest, actual.Dest);
            CheckHandmadeMemberMapping(expected.MemberMappings, actual.MemberMappings);
        }

        private void CheckHandmadeMemberMapping(HandmadeMemberMapping[]? expected, HandmadeMemberMapping[]? actual)
        {
            if (expected == null)
                Assert.That(actual == null || actual.Length == 0);
            else
            {
                Assert.IsNotNull(actual);
                Assert.AreEqual(expected.Length, actual!.Length);
                for (Int32 index = 0; index < expected.Length; ++index)
                {
                    Assert.AreEqual(expected[index].SourceName, actual[index].SourceName);
                    Assert.AreEqual(expected[index].DestName, actual[index].DestName);
                }
            }
        }
    }
}
