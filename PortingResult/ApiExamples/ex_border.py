# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.themes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExBorder(ApiExampleBase):
    def test_font_border(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_paragraph_top_border(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        top_border = builder.paragraph_format.borders.top
        top_border.line_width = 4
        top_border.line_style = aspose.words.LineStyle.DASH_SMALL_GAP
        top_border.theme_color = aspose.words.themes.ThemeColor.ACCENT1
        top_border.tint_and_shade = 0.25
        builder.writeln("Text with a top border.")
        doc.save(file_name = ARTIFACTS_DIR + "Border.ParagraphTopBorder.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Border.ParagraphTopBorder.docx")
        border = doc.first_section.body.first_paragraph.paragraph_format.borders.top
        self.assertEqual(4, border.line_width)
        self.assertEqual(aspose.words.LineStyle.DASH_SMALL_GAP, border.line_style)
        self.assertEqual(aspose.words.themes.ThemeColor.ACCENT1, border.theme_color)
        self.assertAlmostEqual(0.25, border.tint_and_shade, delta=0.01)

    def test_clear_formatting(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_shared_elements(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_horizontal_borders(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_vertical_borders(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")
