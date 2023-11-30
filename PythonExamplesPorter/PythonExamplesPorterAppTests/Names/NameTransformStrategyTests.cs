using NUnit.Framework;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterAppTests.Names
{
    [TestFixture]
    internal class SeparatedDigitsExceptSinglesNameConverterTests
    {
        [TestCase("UICompat97To2003", "ui_compat_97_to_2003")]
        [TestCase("Rotate90FlipNone", "rotate_90_flip_none")]
        [TestCase("PlainTable5", "plain_table5")]
        [TestCase("IsoB4", "iso_b4")]
        [TestCase("Standard10x14", "standard_10x14")]
        [TestCase("AccentColors2to3", "accent_colors_2_to_3")]
        [TestCase("Effect3D", "effect_3d")]
        [TestCase("Border", "border")]
        [TestCase("BorderStart", "border_start")]
        [TestCase("SuperBorderStart", "super_border_start")]
        [TestCase("AbsoluteSuperBorderStart", "absolute_super_border_start")]
        [TestCase("ABC23Border", "abc_23_border")]
        [TestCase("ExABC23Border", "ex_abc_23_border")]
        [TestCase("MWSmallCaps", "mw_small_caps")]
        [TestCase("UseFELayout", "use_fe_layout")]
        [TestCase("DoNotUseHTMLParagraphAutoSpacing", "do_not_use_html_paragraph_auto_spacing")]
        [TestCase("WPJustification", "wp_justification")]
        [TestCase("UseWord97LineBreakRules", "use_word_97_line_break_rules")]
        [TestCase("UseWord2002TableStyleRules", "use_word_2002_table_style_rules")]
        [TestCase("IsForms2OleControl", "is_forms_2_ole_control")]
        public void ConvertPascalCaseIntoSnakeCase(String source, String expectedResult)
        {
            INameTransformStrategy transformStrategy = new SeparatedDigitsExceptSinglesNameConverter();
            Assert.AreEqual(expectedResult, transformStrategy.ConvertPascalCaseIntoSnakeCase(source));
        }
    }
}
