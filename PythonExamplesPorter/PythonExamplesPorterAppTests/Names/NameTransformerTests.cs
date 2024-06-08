using NUnit.Framework;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterAppTests.Names
{
    [TestFixture]
    public class NameTransformerTests
    {
        public NameTransformerTests()
        {
            INameTransformStrategy transformStrategy = new SeparatedDigitsExceptSinglesNameConverter();
            IHandmadeNameManager manager = HandmadeNameManagerFactory.Create(_handmadeAliases);
            _nameTransformer = new NameTransformer(transformStrategy, manager);
        }

        [TestCase("border", "border")]
        [TestCase("Border", "border")]
        [TestCase("ExBorder", "ex_border")]
        [TestCase("ExSuperBorder", "ex_super_border")]
        [TestCase("ExAbsoluteSuperBorder", "ex_absolute_super_border")]
        [TestCase("ABC23Border", "abc23_border")]
        [TestCase("ExABC23Border", "ex_abc23_border")]
        [TestCase("ExMossRtf2Docx", "ex_moss_rtf2docx")]
        [TestCase("ExPdf2Word", "ex_pdf2word")]
        [TestCase("ExWordML2003SaveOptions", "ex_word_ml2003_save_options")]
        public void TransformFileObjectName(String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformFileObjectName(source), Is.EqualTo(expectedResult));
        }

        [TestCase("SomeNamespace", "somenamespace")]
        [TestCase("SomeNamespace.OtherNamespace", "somenamespace.othernamespace")]
        [TestCase("SomeNamespace.OtherNamespace.AnotherNamespace", "somenamespace.othernamespace.anothernamespace")]
        [TestCase("Namespace1", "namespace1")]
        [TestCase("Namespace1.Namespace2", "namespace1.namespace2")]
        public void TransformNamespaceName(String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformNamespaceName(source), Is.EqualTo(expectedResult));
        }

        [TestCase("Border", "Border")]
        [TestCase("ExBorder", "ExBorder")]
        [TestCase("ExSuperBorder", "ExSuperBorder")]
        [TestCase("ExAbsoluteSuperBorder", "ExAbsoluteSuperBorder")]
        [TestCase("ABC23Border", "ABC23Border")]
        [TestCase("ExABC23Border", "ExABC23Border")]
        public void TransformTypeName(String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformTypeName(source), Is.EqualTo(expectedResult));
        }

        [TestCase("SomeType", "Calculate", "calculate")]
        [TestCase("SomeLibrary.SomeType", "Calculate", "calculate")]
        [TestCase("SomeType", "CalculateBorder", "calculate_border")]
        [TestCase("SomeLibrary.SomeType", "CalculateBorder", "calculate_border")]
        [TestCase("SomeType", "CalculateSuperBorder", "calculate_super_border")]
        [TestCase("SomeLibrary.SomeType", "CalculateSuperBorder", "calculate_super_border")]
        [TestCase("SomeType", "CalculateAbsoluteSuperBorder", "calculate_absolute_super_border")]
        [TestCase("SomeLibrary.SomeType", "CalculateAbsoluteSuperBorder", "calculate_absolute_super_border")]
        [TestCase("SomeType", "ABC23CalculateBorder", "abc_23_calculate_border")]
        [TestCase("SomeLibrary.SomeType", "ABC23CalculateBorder", "abc_23_calculate_border")]
        [TestCase("SomeType", "CalculateABC23Border", "calculate_abc_23_border")]
        [TestCase("SomeLibrary.SomeType", "CalculateABC23Border", "calculate_abc_23_border")]
        public void TransformMethodName(String typeName, String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformMethodName(typeName, source), Is.EqualTo(expectedResult));
        }

        [TestCase("SomeType", "Border", "border")]
        [TestCase("SomeLibrary.SomeType", "Border", "border")]
        [TestCase("SomeType", "BorderStart", "border_start")]
        [TestCase("SomeLibrary.SomeType", "BorderStart", "border_start")]
        [TestCase("SomeType", "SuperBorderStart", "super_border_start")]
        [TestCase("SomeLibrary.SomeType", "SuperBorderStart", "super_border_start")]
        [TestCase("SomeType", "AbsoluteSuperBorderStart", "absolute_super_border_start")]
        [TestCase("SomeLibrary.SomeType", "AbsoluteSuperBorderStart", "absolute_super_border_start")]
        [TestCase("SomeType", "ABC23Border", "abc_23_border")]
        [TestCase("SomeLibrary.SomeType", "ABC23Border", "abc_23_border")]
        [TestCase("SomeType", "ExABC23Border", "ex_abc_23_border")]
        [TestCase("SomeLibrary.SomeType", "ExABC23Border", "ex_abc_23_border")]
        [TestCase("SomeType", "MWSmallCaps", "mw_small_caps")]
        [TestCase("SomeLibrary.SomeType", "MWSmallCaps", "mw_small_caps")]
        [TestCase("SomeType", "UseFELayout", "use_fe_layout")]
        [TestCase("SomeLibrary.SomeType", "UseFELayout", "use_fe_layout")]
        [TestCase("SomeType", "DoNotUseHTMLParagraphAutoSpacing", "do_not_use_html_paragraph_auto_spacing")]
        [TestCase("SomeLibrary.SomeType", "DoNotUseHTMLParagraphAutoSpacing", "do_not_use_html_paragraph_auto_spacing")]
        [TestCase("SomeType", "WPJustification", "wp_justification")]
        [TestCase("SomeLibrary.SomeType", "WPJustification", "wp_justification")]
        [TestCase("CompatibilityOptions", "UseWord97LineBreakRules", "use_word97_line_break_rules")]
        [TestCase("SomeLibrary.CompatibilityOptions", "UseWord97LineBreakRules", "use_word97_line_break_rules")]
        [TestCase("CompatibilityOptions", "UICompat97To2003", "ui_compat_97_to_2003")]
        [TestCase("SomeLibrary.CompatibilityOptions", "UICompat97To2003", "ui_compat_97_to_2003")]
        [TestCase("CompatibilityOptions", "UseWord2002TableStyleRules", "use_word2002_table_style_rules")]
        [TestCase("SomeLibrary.CompatibilityOptions", "UseWord2002TableStyleRules", "use_word2002_table_style_rules")]
        [TestCase("SomeType", "IsForms2OleControl", "is_forms2_ole_control")]
        [TestCase("SomeLibrary.SomeType", "IsForms2OleControl", "is_forms2_ole_control")]
        public void TransformPropertyName(String typeName, String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformPropertyName(typeName, source), Is.EqualTo(expectedResult));
        }

        [TestCase("SomeType", "Field", "field")]
        [TestCase("SomeLibrary.SomeType", "Field", "field")]
        [TestCase("SomeType", "BorderField", "border_field")]
        [TestCase("SomeLibrary.SomeType", "BorderField", "border_field")]
        [TestCase("SomeType", "SuperBorderField", "super_border_field")]
        [TestCase("SomeLibrary.SomeType", "SuperBorderField", "super_border_field")]
        [TestCase("SomeType", "AbsoluteSuperBorderField", "absolute_super_border_field")]
        [TestCase("SomeLibrary.SomeType", "AbsoluteSuperBorderField", "absolute_super_border_field")]
        [TestCase("SomeType", "ABC23Border", "abc_23_border")]
        [TestCase("SomeLibrary.SomeType", "ABC23Border", "abc_23_border")]
        [TestCase("SomeType", "ExABC23Border", "ex_abc_23_border")]
        [TestCase("SomeLibrary.SomeType", "ExABC23Border", "ex_abc_23_border")]
        public void TransformFieldName(String typeName, String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformFieldName(typeName, source), Is.EqualTo(expectedResult));
        }

        [TestCase("ControlChar", "SectionBreak", "SECTION_BREAK")]
        [TestCase("ControlChar", "PageBreak", "PAGE_BREAK")]
        [TestCase("ControlChar", "Lf", "LF")]
        [TestCase("ControlChar", "LineFeed", "LINE_FEED")]
        [TestCase("ControlChar", "Cr", "CR")]
        public void TransformStaticReadonlyFieldName(String typeName, String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformStaticReadonlyFieldName(typeName, source), Is.EqualTo(expectedResult));
        }

        [TestCase("SomeEnum", "Item", "ITEM")]
        [TestCase("SomeLibrary.SomeEnum", "Item", "ITEM")]
        [TestCase("SomeEnum", "BorderItem", "BORDER_ITEM")]
        [TestCase("SomeLibrary.SomeEnum", "BorderItem", "BORDER_ITEM")]
        [TestCase("SomeEnum", "SuperBorderItem", "SUPER_BORDER_ITEM")]
        [TestCase("SomeLibrary.SomeEnum", "SuperBorderItem", "SUPER_BORDER_ITEM")]
        [TestCase("SomeEnum", "AbsoluteSuperBorderItem", "ABSOLUTE_SUPER_BORDER_ITEM")]
        [TestCase("SomeLibrary.SomeEnum", "AbsoluteSuperBorderItem", "ABSOLUTE_SUPER_BORDER_ITEM")]
        [TestCase("SomeEnum", "ABC23BorderItem", "ABC_23_BORDER_ITEM")]
        [TestCase("SomeLibrary.SomeEnum", "ABC23BorderItem", "ABC_23_BORDER_ITEM")]
        [TestCase("SomeEnum", "SuperABC23BorderItem", "SUPER_ABC_23_BORDER_ITEM")]
        [TestCase("SomeLibrary.SomeEnum", "SuperABC23BorderItem", "SUPER_ABC_23_BORDER_ITEM")]
        [TestCase("SomeEnum", "Area3D", "AREA_3D")]
        [TestCase("SomeLibrary.SomeEnum", "Area3D", "AREA_3D")]
        [TestCase("SomeEnum", "Area3DStacked", "AREA_3D_STACKED")]
        [TestCase("SomeLibrary.SomeEnum", "Area3DStacked", "AREA_3D_STACKED")]
        [TestCase("SomeEnum", "Area3DPercentStacked", "AREA_3D_PERCENT_STACKED")]
        [TestCase("SomeLibrary.SomeEnum", "Area3DPercentStacked", "AREA_3D_PERCENT_STACKED")]
        [TestCase("OoxmlCompliance", "Iso29500_2008_Transitional", "ISO29500_2008_TRANSITIONAL")]
        [TestCase("SomeLibrary.OoxmlCompliance", "Iso29500_2008_Transitional", "ISO29500_2008_TRANSITIONAL")]
        public void TransformEnumValueName(String typeName, String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformEnumValueName(typeName, source), Is.EqualTo(expectedResult));
        }

        [TestCase("data", "data")]
        [TestCase("someData", "some_data")]
        [TestCase("someDataValue", "some_data_value")]
        [TestCase("abc23Data", "abc_23_data")]
        [TestCase("someABC23Data", "some_abc_23_data")]
        public void TransformLocalVariableName(String source, String expectedResult)
        {
            Assert.That(_nameTransformer.TransformLocalVariableName(source), Is.EqualTo(expectedResult));
        }

        private readonly NameTransformer _nameTransformer;

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
                                new MemberAliasMapping{Name = "XPath", Alias="xpath"},
                                new MemberAliasMapping{Name = "IsForms2OleControl", Alias="is_forms2_ole_control"},
                            }
                        },
                        new TypeNameEntry
                        {
                            Condition = new NameConditions{EqualCondition = "CompatibilityOptions"},
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "UseWord97LineBreakRules", Alias="use_word97_line_break_rules"},
                                new MemberAliasMapping{Name = "UseWord2002TableStyleRules", Alias="use_word2002_table_style_rules"}
                            }
                        },
                        new TypeNameEntry
                        {
                            Condition = new NameConditions{EqualCondition = "OoxmlCompliance"},
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "Iso29500_2008_Transitional", Alias="ISO29500_2008_TRANSITIONAL"},
                                new MemberAliasMapping{Name = "Ecma376_2006", Alias="ECMA376_2006"}
                            }
                        }
                    }
                }
            }
        };
    }
}
