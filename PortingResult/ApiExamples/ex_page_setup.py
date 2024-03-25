# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.notes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExPageSetup(ApiExampleBase):
    def test_clear_formatting(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.page_setup.orientation = aw.Orientation.LANDSCAPE
        builder.page_setup.vertical_alignment = aw.PageVerticalAlignment.CENTER
        builder.writeln("This is the first section, which landscape oriented with vertically centered text.")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        self.assertEqual(aw.Orientation.LANDSCAPE, doc.sections[1].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.CENTER, doc.sections[1].page_setup.vertical_alignment)
        builder.page_setup.clear_formatting()
        self.assertEqual(aw.Orientation.PORTRAIT, doc.sections[1].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.TOP, doc.sections[1].page_setup.vertical_alignment)
        builder.writeln("This is the second section, which is in default Letter paper size, portrait orientation and top alignment.")
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.ClearFormatting.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.ClearFormatting.docx")
        self.assertEqual(aw.Orientation.LANDSCAPE, doc.sections[0].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.CENTER, doc.sections[0].page_setup.vertical_alignment)
        self.assertEqual(aw.Orientation.PORTRAIT, doc.sections[1].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.TOP, doc.sections[1].page_setup.vertical_alignment)

    def test_different_first_page_header_footer(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_odd_and_even_pages_header_footer(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_characters_per_line(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.page_setup.layout_mode = aw.SectionLayoutMode.GRID
        builder.page_setup.characters_per_line = 10
        doc.styles.get_by_name("Normal").font.size = 20
        self.assertEqual(8, doc.first_section.page_setup.characters_per_line)
        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.CharactersPerLine.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.CharactersPerLine.docx")
        self.assertEqual(aw.SectionLayoutMode.GRID, doc.first_section.page_setup.layout_mode)
        self.assertEqual(8, doc.first_section.page_setup.characters_per_line)

    def test_set_section_start(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("This text is in section 1.")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("This text is in section 2.")
        self.assertEqual(aw.SectionStart.NEW_PAGE, doc.sections[1].page_setup.section_start)
        builder.insert_break(aw.BreakType.SECTION_BREAK_CONTINUOUS)
        builder.writeln("This text is in section 3.")
        self.assertEqual(aw.SectionStart.CONTINUOUS, doc.sections[2].page_setup.section_start)
        builder.insert_break(aw.BreakType.SECTION_BREAK_EVEN_PAGE)
        builder.writeln("This text is in section 4.")
        self.assertEqual(aw.SectionStart.EVEN_PAGE, doc.sections[3].page_setup.section_start)
        builder.insert_break(aw.BreakType.SECTION_BREAK_ODD_PAGE)
        builder.writeln("This text is in section 5.")
        self.assertEqual(aw.SectionStart.ODD_PAGE, doc.sections[4].page_setup.section_start)
        columns = builder.page_setup.text_columns
        columns.set_count(2)
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_COLUMN)
        builder.writeln("This text is in section 6.")
        self.assertEqual(aw.SectionStart.NEW_COLUMN, doc.sections[5].page_setup.section_start)
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.SetSectionStart.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.SetSectionStart.docx")
        self.assertEqual(aw.SectionStart.NEW_PAGE, doc.sections[0].page_setup.section_start)
        self.assertEqual(aw.SectionStart.NEW_PAGE, doc.sections[1].page_setup.section_start)
        self.assertEqual(aw.SectionStart.CONTINUOUS, doc.sections[2].page_setup.section_start)
        self.assertEqual(aw.SectionStart.EVEN_PAGE, doc.sections[3].page_setup.section_start)
        self.assertEqual(aw.SectionStart.ODD_PAGE, doc.sections[4].page_setup.section_start)
        self.assertEqual(aw.SectionStart.NEW_COLUMN, doc.sections[5].page_setup.section_start)

    def test_page_margins(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.page_setup.paper_size = aw.PaperSize.LEGAL
        builder.page_setup.orientation = aw.Orientation.LANDSCAPE
        builder.page_setup.top_margin = aw.ConvertUtil.inch_to_point(1)
        builder.page_setup.bottom_margin = aw.ConvertUtil.inch_to_point(1)
        builder.page_setup.left_margin = aw.ConvertUtil.inch_to_point(1.5)
        builder.page_setup.right_margin = aw.ConvertUtil.inch_to_point(1.5)
        builder.page_setup.header_distance = aw.ConvertUtil.inch_to_point(0.2)
        builder.page_setup.footer_distance = aw.ConvertUtil.inch_to_point(0.2)
        builder.writeln("Hello world!")
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.PageMargins.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.PageMargins.docx")
        self.assertEqual(aw.PaperSize.LEGAL, doc.first_section.page_setup.paper_size)
        self.assertEqual(1008, doc.first_section.page_setup.page_width)
        self.assertEqual(612, doc.first_section.page_setup.page_height)
        self.assertEqual(aw.Orientation.LANDSCAPE, doc.first_section.page_setup.orientation)
        self.assertEqual(72, doc.first_section.page_setup.top_margin)
        self.assertEqual(72, doc.first_section.page_setup.bottom_margin)
        self.assertEqual(108, doc.first_section.page_setup.left_margin)
        self.assertEqual(108, doc.first_section.page_setup.right_margin)
        self.assertEqual(14.4, doc.first_section.page_setup.header_distance)
        self.assertEqual(14.4, doc.first_section.page_setup.footer_distance)

    def test_paper_sizes(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_columns_same_width(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        columns = builder.page_setup.text_columns
        columns.spacing = 100
        columns.set_count(2)
        builder.writeln("Column 1.")
        builder.insert_break(aw.BreakType.COLUMN_BREAK)
        builder.writeln("Column 2.")
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.ColumnsSameWidth.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.ColumnsSameWidth.docx")
        self.assertEqual(100, doc.first_section.page_setup.text_columns.spacing)
        self.assertEqual(2, doc.first_section.page_setup.text_columns.count)

    def test_vertical_line_between_columns(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_line_numbers(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_page_border_properties(self):
        doc = aw.Document()
        page_setup = doc.sections[0].page_setup
        page_setup.border_always_in_front = False
        page_setup.border_distance_from = aw.PageBorderDistanceFrom.PAGE_EDGE
        page_setup.border_applies_to = aw.PageBorderAppliesTo.FIRST_PAGE
        border = page_setup.borders.get_by_border_type(aw.BorderType.TOP)
        border.line_style = aw.LineStyle.SINGLE
        border.line_width = 30
        border.color = aspose.pydrawing.Color.blue
        border.distance_from_text = 0
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.PageBorderProperties.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.PageBorderProperties.docx")
        page_setup = doc.first_section.page_setup
        self.assertFalse(page_setup.border_always_in_front)
        self.assertEqual(aw.PageBorderDistanceFrom.PAGE_EDGE, page_setup.border_distance_from)
        self.assertEqual(aw.PageBorderAppliesTo.FIRST_PAGE, page_setup.border_applies_to)
        border = page_setup.borders.get_by_border_type(aw.BorderType.TOP)
        self.assertEqual(aw.LineStyle.SINGLE, border.line_style)
        self.assertEqual(30, border.line_width)
        self.assertEqual(aspose.pydrawing.Color.blue.to_argb(), border.color.to_argb())
        self.assertEqual(0, border.distance_from_text)

    def test_page_borders(self):
        doc = aw.Document()
        page_setup = doc.sections[0].page_setup
        page_setup.borders.line_style = aw.LineStyle.DOUBLE_WAVE
        page_setup.borders.line_width = 2
        page_setup.borders.color = aspose.pydrawing.Color.green
        page_setup.borders.distance_from_text = 24
        page_setup.borders.shadow = True
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.PageBorders.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.PageBorders.docx")
        page_setup = doc.first_section.page_setup
        for border in page_setup.borders:
            self.assertEqual(aw.LineStyle.DOUBLE_WAVE, border.line_style)
            self.assertEqual(2, border.line_width)
            self.assertEqual(aspose.pydrawing.Color.green.to_argb(), border.color.to_argb())
            self.assertEqual(24, border.distance_from_text)
            self.assertTrue(border.shadow)

    def test_page_numbering(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Section 1, page 1.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 1, page 2.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 1, page 3.")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("Section 2, page 1.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 2, page 2.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 2, page 3.")
        builder.move_to_section(0)
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.write("Page ")
        builder.insert_field(field_code="PAGE", field_value="")
        page_setup = doc.sections[0].page_setup
        page_setup.restart_page_numbering = True
        page_setup.page_starting_number = 5
        page_setup.page_number_style = aw.NumberStyle.UPPERCASE_ROMAN
        builder.move_to_section(1)
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.paragraph_format.alignment = aw.ParagraphAlignment.CENTER
        builder.write(" - ")
        builder.insert_field(field_code="PAGE", field_value="")
        builder.write(" - ")
        page_setup = doc.sections[1].page_setup
        page_setup.page_starting_number = 10
        page_setup.restart_page_numbering = True
        page_setup.page_number_style = aw.NumberStyle.ARABIC
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.PageNumbering.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.PageNumbering.docx")
        page_setup = doc.sections[0].page_setup
        self.assertTrue(page_setup.restart_page_numbering)
        self.assertEqual(5, page_setup.page_starting_number)
        self.assertEqual(aw.NumberStyle.UPPERCASE_ROMAN, page_setup.page_number_style)
        page_setup = doc.sections[1].page_setup
        self.assertTrue(page_setup.restart_page_numbering)
        self.assertEqual(10, page_setup.page_starting_number)
        self.assertEqual(aw.NumberStyle.ARABIC, page_setup.page_number_style)

    def test_footnote_options(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Hello world!")
        builder.insert_footnote(footnote_type=aw.notes.FootnoteType.FOOTNOTE, footnote_text="Footnote reference text.")
        footnote_options = doc.sections[0].page_setup.footnote_options
        footnote_options.position = aw.notes.FootnotePosition.BENEATH_TEXT
        footnote_options.restart_rule = aw.notes.FootnoteNumberingRule.RESTART_PAGE
        footnote_options.start_number = 1
        builder.write(" Hello again.")
        builder.insert_footnote(footnote_type=aw.notes.FootnoteType.FOOTNOTE, footnote_text="Endnote reference text.")
        endnote_options = doc.sections[0].page_setup.endnote_options
        endnote_options.position = aw.notes.EndnotePosition.END_OF_DOCUMENT
        endnote_options.restart_rule = aw.notes.FootnoteNumberingRule.CONTINUOUS
        endnote_options.start_number = 1
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.FootnoteOptions.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.FootnoteOptions.docx")
        footnote_options = doc.first_section.page_setup.footnote_options
        self.assertEqual(aw.notes.FootnotePosition.BENEATH_TEXT, footnote_options.position)
        self.assertEqual(aw.notes.FootnoteNumberingRule.RESTART_PAGE, footnote_options.restart_rule)
        self.assertEqual(1, footnote_options.start_number)
        endnote_options = doc.first_section.page_setup.endnote_options
        self.assertEqual(aw.notes.EndnotePosition.END_OF_DOCUMENT, endnote_options.position)
        self.assertEqual(aw.notes.FootnoteNumberingRule.CONTINUOUS, endnote_options.restart_rule)
        self.assertEqual(1, endnote_options.start_number)

    def test_bidi(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_page_border(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world! This is the main body text.")
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.write("This is the header.")
        builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_PRIMARY)
        builder.write("This is the footer.")
        builder.move_to_document_end()
        page_setup = doc.sections[0].page_setup
        page_setup.borders.line_style = aw.LineStyle.DOUBLE
        page_setup.borders.color = aspose.pydrawing.Color.blue
        page_setup.border_surrounds_header = True
        page_setup.border_surrounds_footer = False
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.PageBorder.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.PageBorder.docx")
        page_setup = doc.first_section.page_setup
        self.assertTrue(page_setup.border_surrounds_header)
        self.assertFalse(page_setup.border_surrounds_footer)

    def test_booklet(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_set_text_orientation(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        page_setup = doc.sections[0].page_setup
        page_setup.text_orientation = aw.TextOrientation.UPWARD
        doc.save(file_name=ARTIFACTS_DIR + "PageSetup.SetTextOrientation.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "PageSetup.SetTextOrientation.docx")
        page_setup = doc.first_section.page_setup
        self.assertEqual(aw.TextOrientation.UPWARD, page_setup.text_orientation)

    def test_suppress_endnotes(self):
        raise NotImplementedError("Unsupported call of method named InsertSectionWithEndnote")

    def test_chapter_page_separator(self):
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        page_setup = doc.first_section.page_setup
        page_setup.page_number_style = aw.NumberStyle.UPPERCASE_ROMAN
        page_setup.chapter_page_separator = aw.ChapterPageSeparator.COLON
        page_setup.heading_level_for_chapter = 1
