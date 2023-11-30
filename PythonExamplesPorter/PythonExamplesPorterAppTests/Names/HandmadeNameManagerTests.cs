using NUnit.Framework;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterAppTests.Names
{
    [TestFixture]
    internal class HandmadeNameManagerTests
    {
        [TestCase("SomeClass", "SomeMember", false, "")]
        [TestCase("SomeLibraryA.SomeClass", "SomeMember", false, "")]
        [TestCase("SomeLibraryB.SomeClass", "SomeMember", false, "")]
        [TestCase("SomeClass", "HRef", true, "href")]
        [TestCase("SomeLibraryA.SomeClass", "HRef", true, "href")]
        [TestCase("SomeLibraryB.SomeClass", "HRef", true, "href")]
        [TestCase("SomeClass", "IsForms2OleControl", false, "")]
        [TestCase("SomeLibraryA.SomeClass", "IsForms2OleControl", true, "is_forms2_ole_control")]
        [TestCase("SomeLibraryB.SomeClass", "IsForms2OleControl", false, "")]
        [TestCase("StyleIdentifier", "SomeMember", false, "SomeMember")]
        [TestCase("SomeLibraryA.StyleIdentifier", "SomeMember", false, "SomeMember")]
        [TestCase("SomeLibraryB.StyleIdentifier", "SomeMember", false, "SomeMember")]
        [TestCase("StyleIdentifier", "BodyText1I", true, "BODY_TEXT1_I")]
        [TestCase("SomeLibraryA.StyleIdentifier", "BodyText1I", true, "BODY_TEXT1_I")]
        [TestCase("SomeLibraryB.StyleIdentifier", "BodyText1I", true, "BODY_TEXT1_I")]
        [TestCase("StyleIdentifier", "MediumGrid1Accent1", false, "MediumGrid1Accent1")]
        [TestCase("SomeLibraryA.StyleIdentifier", "MediumGrid1Accent1", true, "MEDIUM_GRID1_ACCENT1")]
        [TestCase("SomeLibraryB.StyleIdentifier", "MediumGrid1Accent1", false, "MediumGrid1Accent1")]
        [TestCase("TextureIndex", "Texture12Pt5Percent", false, "Texture12Pt5Percent")]
        [TestCase("SomeLibraryA.TextureIndex", "Texture12Pt5Percent", true, "TEXTURE_12PT5_PERCENT")]
        [TestCase("SomeLibraryB.TextureIndex", "Texture12Pt5Percent", false, "Texture12Pt5Percent")]
        public void Search(String typeName, String memberName, Boolean success, String expectedData)
        {
            HandmadeNameManager manager = new HandmadeNameManager(_handmadeAliases);
            OperationResult<String> actualResult = manager.Search(typeName, memberName);
            OperationResult<String> expectedResult = new OperationResult<String>(success, Data: success ? expectedData : "");
            Assert.AreEqual(expectedResult, actualResult);
        }

        private readonly HandmadeNameAliases _handmadeAliases = new HandmadeNameAliases
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
                },
                new NamespaceNameEntry
                {
                    Condition = new NameConditions{EqualCondition = "SomeLibraryA"},
                    Types = new []
                    {
                        new TypeNameEntry
                        {
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "IsForms2OleControl", Alias="is_forms2_ole_control"},
                                new MemberAliasMapping{Name = "AsForms2OleControl", Alias="as_forms2_ole_control"}
                            }
                        },
                        new TypeNameEntry
                        {
                            Condition = new NameConditions{EqualCondition = "StyleIdentifier"},
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "MediumGrid1Accent1", Alias="MEDIUM_GRID1_ACCENT1"},
                                new MemberAliasMapping{Name = "MediumGrid1Accent2", Alias="MEDIUM_GRID1_ACCENT2"}
                            }
                        },
                        new TypeNameEntry
                        {
                            Condition = new NameConditions{EqualCondition = "TextureIndex"},
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "Texture12Pt5Percent", Alias="TEXTURE_12PT5_PERCENT"},
                                new MemberAliasMapping{Name = "Texture17Pt5Percent", Alias="TEXTURE_17PT5_PERCENT"}
                            }
                        }
                    }
                }
            }
        };
    }
}
