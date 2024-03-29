# -*- coding: utf-8 -*-
import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExParagraphFormat(ApiExampleBase):
    def test_asian_typography_properties(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        format = doc.first_section.body.first_paragraph.paragraph_format
        format.far_east_line_break_control = True
        format.word_wrap = False
        format.hanging_punctuation = True
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.AsianTypographyProperties.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.AsianTypographyProperties.docx")
        format = doc.first_section.body.first_paragraph.paragraph_format
        self.assertTrue(format.far_east_line_break_control)
        self.assertFalse(format.word_wrap)
        self.assertTrue(format.hanging_punctuation)

    def test_drop_cap(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_line_spacing(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.line_spacing_rule = aw.LineSpacingRule.AT_LEAST
        builder.paragraph_format.line_spacing = 20
        builder.writeln("Minimum line spacing of 20.")
        builder.writeln("Minimum line spacing of 20.")
        builder.paragraph_format.line_spacing_rule = aw.LineSpacingRule.EXACTLY
        builder.paragraph_format.line_spacing = 5
        builder.writeln("Line spacing of exactly 5.")
        builder.writeln("Line spacing of exactly 5.")
        builder.paragraph_format.line_spacing_rule = aw.LineSpacingRule.MULTIPLE
        builder.paragraph_format.line_spacing = 18
        builder.writeln("Line spacing of 1.5 default lines.")
        builder.writeln("Line spacing of 1.5 default lines.")
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.LineSpacing.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.LineSpacing.docx")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(aw.LineSpacingRule.AT_LEAST, paragraphs[0].paragraph_format.line_spacing_rule)
        self.assertEqual(20, paragraphs[0].paragraph_format.line_spacing)
        self.assertEqual(aw.LineSpacingRule.AT_LEAST, paragraphs[1].paragraph_format.line_spacing_rule)
        self.assertEqual(20, paragraphs[1].paragraph_format.line_spacing)
        self.assertEqual(aw.LineSpacingRule.EXACTLY, paragraphs[2].paragraph_format.line_spacing_rule)
        self.assertEqual(5, paragraphs[2].paragraph_format.line_spacing)
        self.assertEqual(aw.LineSpacingRule.EXACTLY, paragraphs[3].paragraph_format.line_spacing_rule)
        self.assertEqual(5, paragraphs[3].paragraph_format.line_spacing)
        self.assertEqual(aw.LineSpacingRule.MULTIPLE, paragraphs[4].paragraph_format.line_spacing_rule)
        self.assertEqual(18, paragraphs[4].paragraph_format.line_spacing)
        self.assertEqual(aw.LineSpacingRule.MULTIPLE, paragraphs[5].paragraph_format.line_spacing_rule)
        self.assertEqual(18, paragraphs[5].paragraph_format.line_spacing)

    def test_paragraph_spacing_auto(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paragraph_spacing_same_style(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paragraph_outline_level(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.outline_level = aw.OutlineLevel.LEVEL1
        builder.writeln("Paragraph outline level 1.")
        builder.paragraph_format.outline_level = aw.OutlineLevel.LEVEL2
        builder.writeln("Paragraph outline level 2.")
        builder.paragraph_format.outline_level = aw.OutlineLevel.LEVEL3
        builder.writeln("Paragraph outline level 3.")
        builder.writeln("Paragraph outline level 3.")
        builder.paragraph_format.outline_level = aw.OutlineLevel.BODY_TEXT
        builder.writeln("Paragraph at main text level.")
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphOutlineLevel.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphOutlineLevel.docx")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(aw.OutlineLevel.LEVEL1, paragraphs[0].paragraph_format.outline_level)
        self.assertEqual(aw.OutlineLevel.LEVEL2, paragraphs[1].paragraph_format.outline_level)
        self.assertEqual(aw.OutlineLevel.LEVEL3, paragraphs[2].paragraph_format.outline_level)
        self.assertEqual(aw.OutlineLevel.LEVEL3, paragraphs[3].paragraph_format.outline_level)
        self.assertEqual(aw.OutlineLevel.BODY_TEXT, paragraphs[4].paragraph_format.outline_level)

    def test_page_break_before(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_widow_control(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_lines_to_drop(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.lines_to_drop = 4
        builder.writeln("H")
        builder.paragraph_format.lines_to_drop = 0
        builder.writeln("ello world!")
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.LinesToDrop.odt")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.LinesToDrop.odt")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(4, paragraphs[0].paragraph_format.lines_to_drop)
        self.assertEqual(0, paragraphs[1].paragraph_format.lines_to_drop)

    def test_suppress_hyphens(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_suppress_hyphens(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paragraph_spacing_and_indents(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_paragraph_baseline_alignment(self):
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        format = doc.first_section.body.paragraphs[0].paragraph_format
        if format.baseline_alignment == aw.BaselineAlignment.AUTO:
            format.baseline_alignment = aw.BaselineAlignment.TOP
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphBaselineAlignment.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphBaselineAlignment.docx")
        format = doc.first_section.body.paragraphs[0].paragraph_format
        self.assertEqual(aw.BaselineAlignment.TOP, format.baseline_alignment)
