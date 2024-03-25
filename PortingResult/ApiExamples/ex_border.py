# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.themes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExBorder(ApiExampleBase):
    def test_font_border(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.font.border.color = aspose.pydrawing.Color.green
        builder.font.border.line_width = 2.5
        builder.font.border.line_style = aw.LineStyle.DASH_DOT_STROKER
        builder.write("Text surrounded by green border.")
        doc.save(file_name=ARTIFACTS_DIR + "Border.FontBorder.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Border.FontBorder.docx")
        border = doc.first_section.body.first_paragraph.runs[0].font.border
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), border.color.to_argb())
        self.assertEqual(2.5, border.line_width)
        self.assertEqual(aw.LineStyle.DASH_DOT_STROKER, border.line_style)

    def test_paragraph_top_border(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        top_border = builder.paragraph_format.borders.top
        top_border.line_width = 4
        top_border.line_style = aw.LineStyle.DASH_SMALL_GAP
        top_border.theme_color = aw.themes.ThemeColor.ACCENT1
        top_border.tint_and_shade = 0.25
        builder.writeln("Text with a top border.")
        doc.save(file_name=ARTIFACTS_DIR + "Border.ParagraphTopBorder.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Border.ParagraphTopBorder.docx")
        border = doc.first_section.body.first_paragraph.paragraph_format.borders.top
        self.assertEqual(4, border.line_width)
        self.assertEqual(aw.LineStyle.DASH_SMALL_GAP, border.line_style)
        self.assertEqual(aw.themes.ThemeColor.ACCENT1, border.theme_color)
        self.assertAlmostEqual(0.25, border.tint_and_shade, delta=0.01)

    def test_clear_formatting(self):
        doc = aw.Document(file_name=MY_DIR + "Borders.docx")
        borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), borders[0].color.to_argb())
        self.assertEqual(3, borders[0].line_width)
        self.assertEqual(aw.LineStyle.SINGLE, borders[0].line_style)
        self.assertTrue(borders[0].is_visible)
        for border in borders:
            border.clear_formatting()
        self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), borders[0].color.to_argb())
        self.assertEqual(0, borders[0].line_width)
        self.assertEqual(aw.LineStyle.NONE, borders[0].line_style)
        self.assertFalse(borders[0].is_visible)
        doc.save(file_name=ARTIFACTS_DIR + "Border.ClearFormatting.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Border.ClearFormatting.docx")
        for test_border in doc.first_section.body.first_paragraph.paragraph_format.borders:
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), test_border.color.to_argb())
            self.assertEqual(0, test_border.line_width)
            self.assertEqual(aw.LineStyle.NONE, test_border.line_style)

    def test_shared_elements(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Paragraph 1.")
        builder.write("Paragraph 2.")
        first_paragraph_borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        second_paragraph_borders = builder.current_paragraph.paragraph_format.borders
        self.assertEqual(6, first_paragraph_borders.count)
        i = 0
        while i < first_paragraph_borders.count:
            self.assertTrue(first_paragraph_borders[i].equals(rhs=second_paragraph_borders[i]))
            self.assertEqual(first_paragraph_borders[i].get_hash_code(), second_paragraph_borders[i].get_hash_code())
            self.assertFalse(first_paragraph_borders[i].is_visible)
            i += 1
        for border in second_paragraph_borders:
            border.line_style = aw.LineStyle.DOT_DASH
        i = 0
        while i < first_paragraph_borders.count:
            self.assertFalse(first_paragraph_borders[i].equals(rhs=second_paragraph_borders[i]))
            self.assertNotEqual(first_paragraph_borders[i].get_hash_code(), second_paragraph_borders[i].get_hash_code())
            self.assertTrue(second_paragraph_borders[i].is_visible)
            i += 1
        doc.save(file_name=ARTIFACTS_DIR + "Border.SharedElements.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Border.SharedElements.docx")
        paragraphs = doc.first_section.body.paragraphs
        for test_border in paragraphs[0].paragraph_format.borders:
            self.assertEqual(aw.LineStyle.NONE, test_border.line_style)
        for test_border in paragraphs[1].paragraph_format.borders:
            self.assertEqual(aw.LineStyle.DOT_DASH, test_border.line_style)

    def test_horizontal_borders(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        borders.horizontal.color = aspose.pydrawing.Color.red
        borders.horizontal.line_style = aw.LineStyle.DASH_SMALL_GAP
        borders.horizontal.line_width = 3
        builder.write("Paragraph above horizontal border.")
        builder.insert_paragraph()
        builder.write("Paragraph below horizontal border.")
        doc.save(file_name=ARTIFACTS_DIR + "Border.HorizontalBorders.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Border.HorizontalBorders.docx")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(aw.LineStyle.DASH_SMALL_GAP, paragraphs[0].paragraph_format.borders.get_by_border_type(aw.BorderType.HORIZONTAL).line_style)
        self.assertEqual(aw.LineStyle.DASH_SMALL_GAP, paragraphs[1].paragraph_format.borders.get_by_border_type(aw.BorderType.HORIZONTAL).line_style)

    def test_vertical_borders(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")
