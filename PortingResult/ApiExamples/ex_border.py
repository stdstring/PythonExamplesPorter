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
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Paragraph 1.")
        builder.write("Paragraph 2.")
        first_paragraph_borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        second_paragraph_borders = builder.current_paragraph.paragraph_format.borders
        self.assertEqual(6, first_paragraph_borders.count)
        # for loop begin
        i = 0
        while i < first_paragraph_borders.count:
            self.assertTrue(first_paragraph_borders[i].equals(rhs = second_paragraph_borders[i]))
            self.assertEqual(first_paragraph_borders[i].get_hash_code(), second_paragraph_borders[i].get_hash_code())
            self.assertFalse(first_paragraph_borders[i].is_visible)
            i += 1
        # for loop end
        # for each loop begin
        for border in second_paragraph_borders:
            border.line_style = aspose.words.LineStyle.DOT_DASH
        # for loop end
        # for loop begin
        i = 0
        while i < first_paragraph_borders.count:
            self.assertFalse(first_paragraph_borders[i].equals(rhs = second_paragraph_borders[i]))
            self.assertNotEqual(first_paragraph_borders[i].get_hash_code(), second_paragraph_borders[i].get_hash_code())
            self.assertTrue(second_paragraph_borders[i].is_visible)
            i += 1
        # for loop end
        doc.save(file_name = ARTIFACTS_DIR + "Border.SharedElements.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Border.SharedElements.docx")
        paragraphs = doc.first_section.body.paragraphs
        # for each loop begin
        for test_border in paragraphs[0].paragraph_format.borders:
            self.assertEqual(aspose.words.LineStyle.NONE, test_border.line_style)
        # for loop end
        # for each loop begin
        for test_border in paragraphs[1].paragraph_format.borders:
            self.assertEqual(aspose.words.LineStyle.DOT_DASH, test_border.line_style)
        # for loop end

    def test_horizontal_borders(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_vertical_borders(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")
