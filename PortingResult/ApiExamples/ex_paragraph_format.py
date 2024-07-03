# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExParagraphFormat(ApiExampleBase):
    def test_asian_typography_properties(self):
        #ExStart
        #ExFor:ParagraphFormat.far_east_line_break_control
        #ExFor:ParagraphFormat.word_wrap
        #ExFor:ParagraphFormat.hanging_punctuation
        #ExSummary:Shows how to set special properties for Asian typography.
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        format = doc.first_section.body.first_paragraph.paragraph_format
        format.far_east_line_break_control = True
        format.word_wrap = False
        format.hanging_punctuation = True
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.AsianTypographyProperties.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.AsianTypographyProperties.docx")
        format = doc.first_section.body.first_paragraph.paragraph_format
        self.assertTrue(format.far_east_line_break_control)
        self.assertFalse(format.word_wrap)
        self.assertTrue(format.hanging_punctuation)

    def test_drop_cap(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_line_spacing(self):
        #ExStart
        #ExFor:ParagraphFormat.line_spacing
        #ExFor:ParagraphFormat.line_spacing_rule
        #ExSummary:Shows how to work with line spacing.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Below are three line spacing rules that we can define using the
        # paragraph's "LineSpacingRule" property to configure spacing between paragraphs.
        # 1 -  Set a minimum amount of spacing.
        # This will give vertical padding to lines of text of any size
        # that is too small to maintain the minimum line-height.
        builder.paragraph_format.line_spacing_rule = aw.LineSpacingRule.AT_LEAST
        builder.paragraph_format.line_spacing = 20
        builder.writeln("Minimum line spacing of 20.")
        builder.writeln("Minimum line spacing of 20.")
        # 2 -  Set exact spacing.
        # Using font sizes that are too large for the spacing will truncate the text.
        builder.paragraph_format.line_spacing_rule = aw.LineSpacingRule.EXACTLY
        builder.paragraph_format.line_spacing = 5
        builder.writeln("Line spacing of exactly 5.")
        builder.writeln("Line spacing of exactly 5.")
        # 3 -  Set spacing as a multiple of default line spacing, which is 12 points by default.
        # This kind of spacing will scale to different font sizes.
        builder.paragraph_format.line_spacing_rule = aw.LineSpacingRule.MULTIPLE
        builder.paragraph_format.line_spacing = 18
        builder.writeln("Line spacing of 1.5 default lines.")
        builder.writeln("Line spacing of 1.5 default lines.")
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.LineSpacing.docx")
        #ExEnd
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
        #ExStart
        #ExFor:ParagraphFormat.outline_level
        #ExSummary:Shows how to configure paragraph outline levels to create collapsible text.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Each paragraph has an OutlineLevel, which could be any number from 1 to 9, or at the default "BodyText" value.
        # Setting the property to one of the numbered values will show an arrow to the left
        # of the beginning of the paragraph.
        builder.paragraph_format.outline_level = aw.OutlineLevel.LEVEL1
        builder.writeln("Paragraph outline level 1.")
        # Level 1 is the topmost level. If there is a paragraph with a lower level below a paragraph with a higher level,
        # collapsing the higher-level paragraph will collapse the lower level paragraph.
        builder.paragraph_format.outline_level = aw.OutlineLevel.LEVEL2
        builder.writeln("Paragraph outline level 2.")
        # Two paragraphs of the same level will not collapse each other,
        # and the arrows do not collapse the paragraphs they point to.
        builder.paragraph_format.outline_level = aw.OutlineLevel.LEVEL3
        builder.writeln("Paragraph outline level 3.")
        builder.writeln("Paragraph outline level 3.")
        # The default "BodyText" value is the lowest, which a paragraph of any level can collapse.
        builder.paragraph_format.outline_level = aw.OutlineLevel.BODY_TEXT
        builder.writeln("Paragraph at main text level.")
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphOutlineLevel.docx")
        #ExEnd
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
        #ExStart
        #ExFor:ParagraphFormat.lines_to_drop
        #ExSummary:Shows how to set the size of a drop cap.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Modify the "LinesToDrop" property to designate a paragraph as a drop cap,
        # which will turn it into a large capital letter that will decorate the next paragraph.
        # Give this property a value of 4 to give the drop cap the height of four text lines.
        builder.paragraph_format.lines_to_drop = 4
        builder.writeln("H")
        # Reset the "LinesToDrop" property to 0 to turn the next paragraph into an ordinary paragraph.
        # The text in this paragraph will wrap around the drop cap.
        builder.paragraph_format.lines_to_drop = 0
        builder.writeln("ello world!")
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.LinesToDrop.odt")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.LinesToDrop.odt")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(4, paragraphs[0].paragraph_format.lines_to_drop)
        self.assertEqual(0, paragraphs[1].paragraph_format.lines_to_drop)

    def test_suppress_hyphens(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paragraph_spacing_and_indents(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_paragraph_baseline_alignment(self):
        #ExStart
        #ExFor:BaselineAlignment
        #ExFor:ParagraphFormat.baseline_alignment
        #ExSummary:Shows how to set fonts vertical position on a line.
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        format = doc.first_section.body.paragraphs[0].paragraph_format
        if format.baseline_alignment == aw.BaselineAlignment.AUTO:
            format.baseline_alignment = aw.BaselineAlignment.TOP
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphBaselineAlignment.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.ParagraphBaselineAlignment.docx")
        format = doc.first_section.body.paragraphs[0].paragraph_format
        self.assertEqual(aw.BaselineAlignment.TOP, format.baseline_alignment)

    def test_mirror_indents(self):
        #ExStart:MirrorIndents
        #ExFor:ParagraphFormat.mirror_indents
        #ExSummary:Show how to make left and right indents the same.
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        format = doc.first_section.body.paragraphs[0].paragraph_format
        format.mirror_indents = True
        doc.save(file_name=ARTIFACTS_DIR + "ParagraphFormat.MirrorIndents.docx")
        #ExEnd:MirrorIndents
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ParagraphFormat.MirrorIndents.docx")
        format = doc.first_section.body.paragraphs[0].paragraph_format
        self.assertEqual(True, format.mirror_indents)
