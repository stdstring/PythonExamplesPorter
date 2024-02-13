using System.Xml.Serialization;
using NUnit.Framework;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterAppTests.Config
{
    [TestFixture]
    public class ConfigDataSerializationTests
    {
        [Test]
        public void DeserializeWithAppRelativeBaseConfigOnly()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithConfigRelativeBaseConfigOnly()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"config\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"config\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.Config, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.Config, "..\\dest\\examples"),
                    ForceDestDelete = false
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithBaseConfigWithSourceDetailsOnly()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <SourceDetails>\r\n" +
                                  "        <KnownNamespaces>\r\n" +
                                  "            <KnownNamespace>RootNamespace.OtherNamespace</KnownNamespace>\r\n" +
                                  "            <KnownNamespace>RootNamespace.AnotherNamespace</KnownNamespace>\r\n" +
                                  "        </KnownNamespaces>\r\n" +
                                  "    </SourceDetails>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    SourceDetails = new SourceDetails
                    {
                        KnownNamespaces = new[]{"RootNamespace.OtherNamespace", "RootNamespace.AnotherNamespace"}
                    },
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithForceDestDeleteBaseConfigOnly()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "    <ForceDestDelete>true</ForceDestDelete>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = true
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithEmptyIgnoredEntities()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities/>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = Array.Empty<String>(),
                    Files = Array.Empty<String>(),
                    Types = Array.Empty<String>(),
                    Methods = Array.Empty<String>()
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithIgnoredDirectories()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Directories>" +
                                  "      <Directory>SomeFolder1</Directory>" +
                                  "      <Directory>SomeFolder2\\OtherFolder</Directory>" +
                                  "    </Directories>" +
                                  "  </IgnoredEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = new[]{"SomeFolder1", "SomeFolder2\\OtherFolder"},
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
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
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = Array.Empty<String>(),
                    Files = new[]{"aa1.cs", "ab1.cs", "some_folder\\aa1.cs"},
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
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
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = Array.Empty<String>(),
                    Files = Array.Empty<String>(),
                    Types = new[]{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
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
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = Array.Empty<String>(),
                    Files = Array.Empty<String>(),
                    Types = Array.Empty<String>(),
                    Methods = new[]{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Directories>" +
                                  "      <Directory>SomeFolder1</Directory>" +
                                  "      <Directory>SomeFolder2\\OtherFolder</Directory>" +
                                  "    </Directories>" +
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
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = new[]{"SomeFolder1", "SomeFolder2\\OtherFolder"},
                    Files = new[]{"aa1.cs", "ab1.cs", "some_folder\\aa1.cs"},
                    Types = new[]{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
                    Methods = new[]{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <HandmadeEntities/>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
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
                                  "          <Member SourceName=\"GetXXX\" DestName=\"get_super_xxx_value\" NeedImport=\"true\"/>\r\n" +
                                  "          <Member SourceName=\"SomePath\" DestName=\"SOME_PATH\" NeedImport=\"false\"/>\r\n" +
                                  "        </MemberMapping>\r\n" +
                                  "      </Type>\r\n" +
                                  "    </Types>\r\n" +
                                  "  </HandmadeEntities>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                HandmadeEntities = new HandmadeEntities
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
                            MemberMappings = new[]
                            {
                                new HandmadeMemberMapping{SourceName = "GetXXX", DestName = "get_super_xxx_value", NeedImport = true},
                                new HandmadeMemberMapping{SourceName = "SomePath", DestName = "SOME_PATH", NeedImport = false}
                            }
                        }
                    }
                }
            };
            CheckDeserialization(expected, source);
        }

        [Test]
        public void DeserializeWithHandmadeNameAliases()
        {
            const String source = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n" +
                                  "<ConfigData>\r\n" +
                                  "  <BaseConfig>\r\n" +
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <aliases>\r\n" +
                                  "    <namespace>\r\n" +
                                  "      <types>\r\n" +
                                  "        <type>\r\n" +
                                  "          <members>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>HRef</name>\r\n" +
                                  "              <alias>href</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>XPath</name>\r\n" +
                                  "              <alias>xpath</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "          </members>\r\n" +
                                  "        </type>\r\n" +
                                  "        <type>\r\n" +
                                  "          <conditions>\r\n" +
                                  "            <equal>StyleIdentifier</equal>\r\n" +
                                  "          </conditions>" +
                                  "          <members>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>BodyText1I</name>\r\n" +
                                  "              <alias>BODY_TEXT1_I</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>BodyText1I2</name>\r\n" +
                                  "              <alias>BODY_TEXT1_I2</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "          </members>\r\n" +
                                  "        </type>\r\n" +
                                  "      </types>\r\n" +
                                  "    </namespace>\r\n" +
                                  "  </aliases>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = false
                },
                HandmadeAliases = new HandmadeNameAliases
                {
                    Namespaces = new []
                    {
                        new NamespaceNameEntry
                        {
                            Types = new []
                            {
                                new TypeNameEntry
                                {
                                    Members = new []
                                    {
                                        new MemberAliasMapping{Name = "HRef", Alias="href"},
                                        new MemberAliasMapping{Name = "XPath", Alias="xpath"}
                                    }
                                },
                                new TypeNameEntry
                                {
                                    Condition = new NameConditions{EqualCondition = "StyleIdentifier"},
                                    Members = new []
                                    {
                                        new MemberAliasMapping{Name = "BodyText1I", Alias="BODY_TEXT1_I"},
                                        new MemberAliasMapping{Name = "BodyText1I2", Alias="BODY_TEXT1_I2"}
                                    }
                                }
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
                                  "    <Source RelativePathBase=\"app\">..\\source\\someproj.csproj</Source>\r\n" +
                                  "    <SourceDetails>\r\n" +
                                  "        <KnownNamespaces>\r\n" +
                                  "            <KnownNamespace>RootNamespace.OtherNamespace</KnownNamespace>\r\n" +
                                  "            <KnownNamespace>RootNamespace.AnotherNamespace</KnownNamespace>\r\n" +
                                  "        </KnownNamespaces>\r\n" +
                                  "    </SourceDetails>\r\n" +
                                  "    <Dest RelativePathBase=\"app\">..\\dest\\examples</Dest>\r\n" +
                                  "    <ForceDestDelete>true</ForceDestDelete>\r\n" +
                                  "  </BaseConfig>\r\n" +
                                  "  <IgnoredEntities>\r\n" +
                                  "    <Directories>" +
                                  "      <Directory>SomeFolder1</Directory>" +
                                  "      <Directory>SomeFolder2\\OtherFolder</Directory>" +
                                  "    </Directories>" +
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
                                  "          <Member SourceName=\"GetXXX\" DestName=\"get_super_xxx_value\" NeedImport=\"true\"/>\r\n" +
                                  "          <Member SourceName=\"SomePath\" DestName=\"SOME_PATH\" NeedImport=\"false\"/>\r\n" +
                                  "        </MemberMapping>\r\n" +
                                  "      </Type>\r\n" +
                                  "    </Types>\r\n" +
                                  "  </HandmadeEntities>\r\n" +
                                  "  <aliases>\r\n" +
                                  "    <namespace>\r\n" +
                                  "      <types>\r\n" +
                                  "        <type>\r\n" +
                                  "          <members>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>HRef</name>\r\n" +
                                  "              <alias>href</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>XPath</name>\r\n" +
                                  "              <alias>xpath</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "          </members>\r\n" +
                                  "        </type>\r\n" +
                                  "        <type>\r\n" +
                                  "          <conditions>\r\n" +
                                  "            <equal>StyleIdentifier</equal>\r\n" +
                                  "          </conditions>" +
                                  "          <members>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>BodyText1I</name>\r\n" +
                                  "              <alias>BODY_TEXT1_I</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "            <member>\r\n" +
                                  "              <name>BodyText1I2</name>\r\n" +
                                  "              <alias>BODY_TEXT1_I2</alias>\r\n" +
                                  "            </member>\r\n" +
                                  "          </members>\r\n" +
                                  "        </type>\r\n" +
                                  "      </types>\r\n" +
                                  "    </namespace>\r\n" +
                                  "  </aliases>\r\n" +
                                  "</ConfigData>";
            ConfigData expected = new ConfigData
            {
                BaseConfig = new BaseConfig
                {
                    Source = new TargetPath(RelativePathBase.App, "..\\source\\someproj.csproj"),
                    SourceDetails = new SourceDetails
                    {
                        KnownNamespaces = new[]{"RootNamespace.OtherNamespace", "RootNamespace.AnotherNamespace"}
                    },
                    DestDirectory = new TargetPath(RelativePathBase.App, "..\\dest\\examples"),
                    ForceDestDelete = true
                },
                IgnoredEntities = new IgnoredEntities
                {
                    Directories = new[]{"SomeFolder1", "SomeFolder2\\OtherFolder"},
                    Files = new[]{"aa1.cs", "ab1.cs", "some_folder\\aa1.cs"},
                    Types = new[]{"SomeNamespace.SomeType", "OtherNamespace.OtherType"},
                    Methods = new[]{"SomeNamespace.SomeType.CheckAAA", "OtherNamespace.OtherType.CheckBBB"}
                },
                HandmadeEntities = new HandmadeEntities
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
                            MemberMappings = new[]
                            {
                                new HandmadeMemberMapping{SourceName = "GetXXX", DestName = "get_super_xxx_value", NeedImport = true},
                                new HandmadeMemberMapping{SourceName = "SomePath", DestName = "SOME_PATH", NeedImport = false}
                            }
                        }
                    }
                },
                HandmadeAliases = new HandmadeNameAliases
                {
                    Namespaces = new[]
                    {
                        new NamespaceNameEntry
                        {
                            Types = new []
                            {
                                new TypeNameEntry
                                {
                                    Members = new []
                                    {
                                        new MemberAliasMapping{Name = "HRef", Alias="href"},
                                        new MemberAliasMapping{Name = "XPath", Alias="xpath"}
                                    }
                                },
                                new TypeNameEntry
                                {
                                    Condition = new NameConditions{EqualCondition = "StyleIdentifier"},
                                    Members = new []
                                    {
                                        new MemberAliasMapping{Name = "BodyText1I", Alias="BODY_TEXT1_I"},
                                        new MemberAliasMapping{Name = "BodyText1I2", Alias="BODY_TEXT1_I2"}
                                    }
                                }
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
            CheckHandmadeNameAliases(expected.HandmadeAliases, actual.HandmadeAliases);
        }

        private void CheckTargetPath(TargetPath expected, TargetPath actual)
        {
            Assert.AreEqual(expected.RelativePathBase, actual.RelativePathBase);
            Assert.AreEqual(expected.Path, actual.Path);
        }

        private void CheckSourceDetails(SourceDetails? expected, SourceDetails? actual)
        {
            if (expected == null)
                Assert.IsNull(actual);
            else
                CheckCollections(expected.KnownNamespaces!, actual!.KnownNamespaces);
        }

        private void CheckBaseConfig(BaseConfig expected, BaseConfig actual)
        {
            Assert.IsNotNull(actual.Source);
            CheckTargetPath(expected.Source!, actual.Source!);
            Assert.IsNotNull(actual.DestDirectory);
            CheckTargetPath(expected.DestDirectory!, actual.DestDirectory!);
            CheckSourceDetails(expected.SourceDetails, actual.SourceDetails);
            Assert.AreEqual(expected.ForceDestDelete, actual.ForceDestDelete);
        }

        private void CheckIgnoredEntities(IgnoredEntities? expected, IgnoredEntities? actual)
        {
            if (expected ==  null)
                Assert.IsNull(actual);
            else
            {
                CheckCollections(expected.Directories!, actual!.Directories);
                CheckCollections(expected.Files!, actual.Files);
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
                    Assert.AreEqual(expected[index].NeedImport, actual[index].NeedImport);
                }
            }
        }

        private void CheckHandmadeNameAliases(HandmadeNameAliases? expected, HandmadeNameAliases? actual)
        {
            if (expected == null)
                Assert.IsNull(actual);
            else
            {
                Assert.IsNotNull(actual);
                CheckNamespaceNameEntries(expected.Namespaces, actual!.Namespaces);
            }
        }

        private void CheckNameConditions(NameConditions? expected, NameConditions? actual)
        {
            if (expected == null)
                Assert.IsNull(actual);
            else
            {
                Assert.IsNotNull(actual);
                if (expected.EqualCondition == null)
                    Assert.IsNull(actual);
                else
                    Assert.AreEqual(expected.EqualCondition, actual!.EqualCondition);
            }
        }

        private void CheckNamespaceNameEntries(NamespaceNameEntry[]? expected, NamespaceNameEntry[]? actual)
        {
            if (expected == null || expected.Length == 0)
                Assert.That(actual == null || actual.Length == 0);
            else
            {
                Assert.IsNotNull(actual);
                Assert.AreEqual(expected.Length, actual!.Length);
                for (Int32 index = 0; index < expected.Length; ++index)
                    CheckNamespaceNameEntry(expected[index], actual[index]);
            }
        }

        private void CheckNamespaceNameEntry(NamespaceNameEntry expected, NamespaceNameEntry actual)
        {
            CheckNameConditions(expected.Condition, actual.Condition);
            CheckTypeNameEntries(expected.Types, actual.Types);
        }

        private void CheckTypeNameEntries(TypeNameEntry[]? expected, TypeNameEntry[]? actual)
        {
            if (expected == null || expected.Length == 0)
                Assert.That(actual == null || actual.Length == 0);
            else
            {
                Assert.IsNotNull(actual);
                Assert.AreEqual(expected.Length, actual!.Length);
                for (Int32 index = 0; index < expected.Length; ++index)
                    CheckTypeNameEntry(expected[index], actual[index]);
            }
        }

        private void CheckTypeNameEntry(TypeNameEntry expected, TypeNameEntry actual)
        {
            CheckNameConditions(expected.Condition, actual.Condition);
            CheckMemberAliasMappings(expected.Members, actual.Members);
        }

        private void CheckMemberAliasMappings(MemberAliasMapping[]? expected, MemberAliasMapping[]? actual)
        {
            if (expected == null || expected.Length == 0)
                Assert.That(actual == null || actual.Length == 0);
            else
            {
                Assert.IsNotNull(actual);
                Assert.AreEqual(expected.Length, actual!.Length);
                for (Int32 index = 0; index < expected.Length; ++index)
                {
                    Assert.AreEqual(expected[index].Name, actual[index].Name);
                    Assert.AreEqual(expected[index].Alias, actual[index].Alias);
                }
            }
        }
    }
}
