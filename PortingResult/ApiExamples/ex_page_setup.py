# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.notes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExPageSetup(ApiExampleBase):
    def test_clear_formatting(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.page_setup.orientation = aspose.words.Orientation.LANDSCAPE
        builder.page_setup.vertical_alignment = aspose.words.PageVerticalAlignment.CENTER
        builder.writeln("This is the first section, which landscape oriented with vertically centered text.")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        self.assertEqual(aspose.words.Orientation.LANDSCAPE, doc.sections[1].page_setup.orientation)
        self.assertEqual(aspose.words.PageVerticalAlignment.CENTER, doc.sections[1].page_setup.vertical_alignment)
        builder.page_setup.clear_formatting()
        self.assertEqual(aspose.words.Orientation.PORTRAIT, doc.sections[1].page_setup.orientation)
        self.assertEqual(aspose.words.PageVerticalAlignment.TOP, doc.sections[1].page_setup.vertical_alignment)
        builder.writeln("This is the second section, which is in default Letter paper size, portrait orientation and top alignment.")
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.ClearFormatting.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.ClearFormatting.docx")
        self.assertEqual(aspose.words.Orientation.LANDSCAPE, doc.sections[0].page_setup.orientation)
        self.assertEqual(aspose.words.PageVerticalAlignment.CENTER, doc.sections[0].page_setup.vertical_alignment)
        self.assertEqual(aspose.words.Orientation.PORTRAIT, doc.sections[1].page_setup.orientation)
        self.assertEqual(aspose.words.PageVerticalAlignment.TOP, doc.sections[1].page_setup.vertical_alignment)

    def test_characters_per_line(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.page_setup.layout_mode = aspose.words.SectionLayoutMode.GRID
        builder.page_setup.characters_per_line = 10
        doc.styles.get_by_name("Normal").font.size = 20
        self.assertEqual(8, doc.first_section.page_setup.characters_per_line)
        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.CharactersPerLine.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.CharactersPerLine.docx")
        self.assertEqual(aspose.words.SectionLayoutMode.GRID, doc.first_section.page_setup.layout_mode)
        self.assertEqual(8, doc.first_section.page_setup.characters_per_line)

    def test_set_section_start(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("This text is in section 1.")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("This text is in section 2.")
        self.assertEqual(aspose.words.SectionStart.NEW_PAGE, doc.sections[1].page_setup.section_start)
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_CONTINUOUS)
        builder.writeln("This text is in section 3.")
        self.assertEqual(aspose.words.SectionStart.CONTINUOUS, doc.sections[2].page_setup.section_start)
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_EVEN_PAGE)
        builder.writeln("This text is in section 4.")
        self.assertEqual(aspose.words.SectionStart.EVEN_PAGE, doc.sections[3].page_setup.section_start)
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_ODD_PAGE)
        builder.writeln("This text is in section 5.")
        self.assertEqual(aspose.words.SectionStart.ODD_PAGE, doc.sections[4].page_setup.section_start)
        columns = builder.page_setup.text_columns
        columns.set_count(2)
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_COLUMN)
        builder.writeln("This text is in section 6.")
        self.assertEqual(aspose.words.SectionStart.NEW_COLUMN, doc.sections[5].page_setup.section_start)
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.SetSectionStart.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.SetSectionStart.docx")
        self.assertEqual(aspose.words.SectionStart.NEW_PAGE, doc.sections[0].page_setup.section_start)
        self.assertEqual(aspose.words.SectionStart.NEW_PAGE, doc.sections[1].page_setup.section_start)
        self.assertEqual(aspose.words.SectionStart.CONTINUOUS, doc.sections[2].page_setup.section_start)
        self.assertEqual(aspose.words.SectionStart.EVEN_PAGE, doc.sections[3].page_setup.section_start)
        self.assertEqual(aspose.words.SectionStart.ODD_PAGE, doc.sections[4].page_setup.section_start)
        self.assertEqual(aspose.words.SectionStart.NEW_COLUMN, doc.sections[5].page_setup.section_start)

    def test_page_margins(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.page_setup.paper_size = aspose.words.PaperSize.LEGAL
        builder.page_setup.orientation = aspose.words.Orientation.LANDSCAPE
        builder.page_setup.top_margin = aspose.words.ConvertUtil.inch_to_point(1)
        builder.page_setup.bottom_margin = aspose.words.ConvertUtil.inch_to_point(1)
        builder.page_setup.left_margin = aspose.words.ConvertUtil.inch_to_point(1.5)
        builder.page_setup.right_margin = aspose.words.ConvertUtil.inch_to_point(1.5)
        builder.page_setup.header_distance = aspose.words.ConvertUtil.inch_to_point(0.2)
        builder.page_setup.footer_distance = aspose.words.ConvertUtil.inch_to_point(0.2)
        builder.writeln("Hello world!")
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.PageMargins.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.PageMargins.docx")
        self.assertEqual(aspose.words.PaperSize.LEGAL, doc.first_section.page_setup.paper_size)
        self.assertEqual(1008, doc.first_section.page_setup.page_width)
        self.assertEqual(612, doc.first_section.page_setup.page_height)
        self.assertEqual(aspose.words.Orientation.LANDSCAPE, doc.first_section.page_setup.orientation)
        self.assertEqual(72, doc.first_section.page_setup.top_margin)
        self.assertEqual(72, doc.first_section.page_setup.bottom_margin)
        self.assertEqual(108, doc.first_section.page_setup.left_margin)
        self.assertEqual(108, doc.first_section.page_setup.right_margin)
        self.assertEqual(14.4, doc.first_section.page_setup.header_distance)
        self.assertEqual(14.4, doc.first_section.page_setup.footer_distance)

    def test_paper_sizes(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_columns_same_width(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        columns = builder.page_setup.text_columns
        columns.spacing = 100
        columns.set_count(2)
        builder.writeln("Column 1.")
        builder.insert_break(aspose.words.BreakType.COLUMN_BREAK)
        builder.writeln("Column 2.")
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.ColumnsSameWidth.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.ColumnsSameWidth.docx")
        self.assertEqual(100, doc.first_section.page_setup.text_columns.spacing)
        self.assertEqual(2, doc.first_section.page_setup.text_columns.count)

    def test_line_numbers(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_page_border_properties(self):
        doc = aspose.words.Document()
        page_setup = doc.sections[0].page_setup
        page_setup.border_always_in_front = False
        page_setup.border_distance_from = aspose.words.PageBorderDistanceFrom.PAGE_EDGE
        page_setup.border_applies_to = aspose.words.PageBorderAppliesTo.FIRST_PAGE
        border = page_setup.borders.get_by_border_type(aspose.words.BorderType.TOP)
        border.line_style = aspose.words.LineStyle.SINGLE
        border.line_width = 30
        border.color = aspose.pydrawing.Color.blue
        border.distance_from_text = 0
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.PageBorderProperties.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.PageBorderProperties.docx")
        page_setup = doc.first_section.page_setup
        self.assertFalse(page_setup.border_always_in_front)
        self.assertEqual(aspose.words.PageBorderDistanceFrom.PAGE_EDGE, page_setup.border_distance_from)
        self.assertEqual(aspose.words.PageBorderAppliesTo.FIRST_PAGE, page_setup.border_applies_to)
        border = page_setup.borders.get_by_border_type(aspose.words.BorderType.TOP)
        self.assertEqual(aspose.words.LineStyle.SINGLE, border.line_style)
        self.assertEqual(30, border.line_width)
        self.assertEqual(aspose.pydrawing.Color.blue.to_argb(), border.color.to_argb())
        self.assertEqual(0, border.distance_from_text)

    def test_page_borders(self):
        doc = aspose.words.Document()
        page_setup = doc.sections[0].page_setup
        page_setup.borders.line_style = aspose.words.LineStyle.DOUBLE_WAVE
        page_setup.borders.line_width = 2
        page_setup.borders.color = aspose.pydrawing.Color.green
        page_setup.borders.distance_from_text = 24
        page_setup.borders.shadow = True
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.PageBorders.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.PageBorders.docx")
        page_setup = doc.first_section.page_setup
        for border in page_setup.borders:
            self.assertEqual(aspose.words.LineStyle.DOUBLE_WAVE, border.line_style)
            self.assertEqual(2, border.line_width)
            self.assertEqual(aspose.pydrawing.Color.green.to_argb(), border.color.to_argb())
            self.assertEqual(24, border.distance_from_text)
            self.assertTrue(border.shadow)

    def test_page_numbering(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Section 1, page 1.")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.writeln("Section 1, page 2.")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.writeln("Section 1, page 3.")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("Section 2, page 1.")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.writeln("Section 2, page 2.")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.writeln("Section 2, page 3.")
        builder.move_to_section(0)
        builder.move_to_header_footer(aspose.words.HeaderFooterType.HEADER_PRIMARY)
        builder.write("Page ")
        builder.insert_field(field_code = "PAGE", field_value = "")
        page_setup = doc.sections[0].page_setup
        page_setup.restart_page_numbering = True
        page_setup.page_starting_number = 5
        page_setup.page_number_style = aspose.words.NumberStyle.UPPERCASE_ROMAN
        builder.move_to_section(1)
        builder.move_to_header_footer(aspose.words.HeaderFooterType.HEADER_PRIMARY)
        builder.paragraph_format.alignment = aspose.words.ParagraphAlignment.CENTER
        builder.write(" - ")
        builder.insert_field(field_code = "PAGE", field_value = "")
        builder.write(" - ")
        page_setup = doc.sections[1].page_setup
        page_setup.page_starting_number = 10
        page_setup.restart_page_numbering = True
        page_setup.page_number_style = aspose.words.NumberStyle.ARABIC
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.PageNumbering.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.PageNumbering.docx")
        page_setup = doc.sections[0].page_setup
        self.assertTrue(page_setup.restart_page_numbering)
        self.assertEqual(5, page_setup.page_starting_number)
        self.assertEqual(aspose.words.NumberStyle.UPPERCASE_ROMAN, page_setup.page_number_style)
        page_setup = doc.sections[1].page_setup
        self.assertTrue(page_setup.restart_page_numbering)
        self.assertEqual(10, page_setup.page_starting_number)
        self.assertEqual(aspose.words.NumberStyle.ARABIC, page_setup.page_number_style)

    def test_footnote_options(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Hello world!")
        builder.insert_footnote(footnote_type = aspose.words.notes.FootnoteType.FOOTNOTE, footnote_text = "Footnote reference text.")
        footnote_options = doc.sections[0].page_setup.footnote_options
        footnote_options.position = aspose.words.notes.FootnotePosition.BENEATH_TEXT
        footnote_options.restart_rule = aspose.words.notes.FootnoteNumberingRule.RESTART_PAGE
        footnote_options.start_number = 1
        builder.write(" Hello again.")
        builder.insert_footnote(footnote_type = aspose.words.notes.FootnoteType.FOOTNOTE, footnote_text = "Endnote reference text.")
        endnote_options = doc.sections[0].page_setup.endnote_options
        endnote_options.position = aspose.words.notes.EndnotePosition.END_OF_DOCUMENT
        endnote_options.restart_rule = aspose.words.notes.FootnoteNumberingRule.CONTINUOUS
        endnote_options.start_number = 1
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.FootnoteOptions.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.FootnoteOptions.docx")
        footnote_options = doc.first_section.page_setup.footnote_options
        self.assertEqual(aspose.words.notes.FootnotePosition.BENEATH_TEXT, footnote_options.position)
        self.assertEqual(aspose.words.notes.FootnoteNumberingRule.RESTART_PAGE, footnote_options.restart_rule)
        self.assertEqual(1, footnote_options.start_number)
        endnote_options = doc.first_section.page_setup.endnote_options
        self.assertEqual(aspose.words.notes.EndnotePosition.END_OF_DOCUMENT, endnote_options.position)
        self.assertEqual(aspose.words.notes.FootnoteNumberingRule.CONTINUOUS, endnote_options.restart_rule)
        self.assertEqual(1, endnote_options.start_number)

    def test_page_border(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world! This is the main body text.")
        builder.move_to_header_footer(aspose.words.HeaderFooterType.HEADER_PRIMARY)
        builder.write("This is the header.")
        builder.move_to_header_footer(aspose.words.HeaderFooterType.FOOTER_PRIMARY)
        builder.write("This is the footer.")
        builder.move_to_document_end()
        page_setup = doc.sections[0].page_setup
        page_setup.borders.line_style = aspose.words.LineStyle.DOUBLE
        page_setup.borders.color = aspose.pydrawing.Color.blue
        page_setup.border_surrounds_header = True
        page_setup.border_surrounds_footer = False
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.PageBorder.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.PageBorder.docx")
        page_setup = doc.first_section.page_setup
        self.assertTrue(page_setup.border_surrounds_header)
        self.assertFalse(page_setup.border_surrounds_footer)

    def test_booklet(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_set_text_orientation(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        page_setup = doc.sections[0].page_setup
        page_setup.text_orientation = aspose.words.TextOrientation.UPWARD
        doc.save(file_name = ARTIFACTS_DIR + "PageSetup.SetTextOrientation.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "PageSetup.SetTextOrientation.docx")
        page_setup = doc.first_section.page_setup
        self.assertEqual(aspose.words.TextOrientation.UPWARD, page_setup.text_orientation)

    def test_suppress_endnotes(self):
        raise NotImplementedError("Unsupported call of method named InsertSectionWithEndnote")

    def test_chapter_page_separator(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Big document.docx")
        page_setup = doc.first_section.page_setup
        page_setup.page_number_style = aspose.words.NumberStyle.UPPERCASE_ROMAN
        page_setup.chapter_page_separator = aspose.words.ChapterPageSeparator.COLON
        page_setup.heading_level_for_chapter = 1
