# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.fonts
import aspose.words.themes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, MY_DIR


class ExFont(ApiExampleBase):
    def test_create_formatted_run(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_caps(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_get_document_fonts(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_default_values_embedded_fonts_parameters(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_strike_through(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_position_subscript(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_scaling_spacing(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.scaling = 150
        builder.writeln("Wide characters")
        builder.font.spacing = 1
        builder.writeln("Expanded by 1pt")
        builder.font.spacing = -1
        builder.writeln("Condensed by 1pt")
        doc.save(file_name = ARTIFACTS_DIR + "Font.ScalingSpacing.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.ScalingSpacing.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Wide characters", run.get_text().strip())
        self.assertEqual(150, run.font.scaling)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("Expanded by 1pt", run.get_text().strip())
        self.assertEqual(1, run.font.spacing)
        run = doc.first_section.body.paragraphs[2].runs[0]
        self.assertEqual("Condensed by 1pt", run.get_text().strip())
        self.assertEqual(-1, run.font.spacing)

    def test_italic(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_engrave_emboss(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_shadow(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_outline(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_hidden(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_kerning(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.name = "Arial Black"
        builder.font.size = 18
        builder.font.kerning = 24
        builder.writeln("TALLY. (Kerning not applied)")
        builder.font.kerning = 12
        builder.writeln("TALLY. (Kerning applied)")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Kerning.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Kerning.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("TALLY. (Kerning not applied)", run.get_text().strip())
        self.assertEqual(24, run.font.kerning)
        self.assertEqual(18, run.font.size)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("TALLY. (Kerning applied)", run.get_text().strip())
        self.assertEqual(12, run.font.kerning)
        self.assertEqual(18, run.font.size)

    def test_no_proofing(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_locale_id(self):
        raise NotImplementedError("Unsupported type: CultureInfo")

    def test_underlines(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_complex_script(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_sparkling_text(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.size = 36
        builder.font.text_effect = aspose.words.TextEffect.SPARKLE_TEXT
        builder.writeln("Text with a sparkle effect.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.SparklingText.doc")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.SparklingText.doc")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Text with a sparkle effect.", run.get_text().strip())
        self.assertEqual(aspose.words.TextEffect.SPARKLE_TEXT, run.font.text_effect)

    def test_foreground_and_background(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_shading(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_bidi(self):
        raise NotImplementedError("Unsupported type: CultureInfo")

    def test_far_east(self):
        raise NotImplementedError("Unsupported type: CultureInfo")

    def test_name_ascii(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.name_ascii = "Calibri"
        self.assertEqual("Calibri", builder.font.name)
        builder.font.name_other = "Courier New"
        builder.writeln("Hello, Привет")
        doc.save(file_name = ARTIFACTS_DIR + "Font.NameAscii.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.NameAscii.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Hello, Привет", run.get_text().strip())
        self.assertEqual("Calibri", run.font.name)
        self.assertEqual("Calibri", run.font.name_ascii)
        self.assertEqual("Courier New", run.font.name_other)

    def test_change_style(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.style_name = "Emphasis"
        builder.writeln("Text originally in \"Emphasis\" style")
        builder.font.style_identifier = aspose.words.StyleIdentifier.INTENSE_EMPHASIS
        builder.writeln("Text originally in \"Intense Emphasis\" style")
        # for each loop begin
        for run in doc.get_child_nodes(aspose.words.NodeType.RUN, True).of_type():
            # if begin
            if run.font.style_name == "Emphasis":
                run.font.style_name = "Strong"
            # if end
            # if begin
            if run.font.style_identifier == aspose.words.StyleIdentifier.INTENSE_EMPHASIS:
                run.font.style_identifier = aspose.words.StyleIdentifier.STRONG
            # if end
        # for loop end
        doc.save(file_name = ARTIFACTS_DIR + "Font.ChangeStyle.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.ChangeStyle.docx")
        doc_run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Text originally in \"Emphasis\" style", doc_run.get_text().strip())
        self.assertEqual(aspose.words.StyleIdentifier.STRONG, doc_run.font.style_identifier)
        self.assertEqual("Strong", doc_run.font.style_name)
        doc_run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("Text originally in \"Intense Emphasis\" style", doc_run.get_text().strip())
        self.assertEqual(aspose.words.StyleIdentifier.STRONG, doc_run.font.style_identifier)
        self.assertEqual("Strong", doc_run.font.style_name)

    def test_built_in(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_style(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_get_available_fonts(self):
        raise NotImplementedError("Unrecognizable type of expression: folderFontSource[0]")

    def test_set_font_auto_color(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_default_fonts(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_extract_embedded_font(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_get_font_info_from_file(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerator")

    def test_has_dml_effect(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_theme_fonts_colors(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_create_themed_style(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")
