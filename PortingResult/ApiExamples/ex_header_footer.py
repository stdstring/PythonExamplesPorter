# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.replacing
import aspose.words.saving
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExHeaderFooter(ApiExampleBase):
    def test_create(self):
        doc = aspose.words.Document()
        header = aspose.words.HeaderFooter(doc, aspose.words.HeaderFooterType.HEADER_PRIMARY)
        doc.first_section.headers_footers.add(header)
        para = header.append_paragraph("My header.")
        self.assertTrue(header.is_header)
        self.assertTrue(para.is_end_of_header_footer)
        footer = aspose.words.HeaderFooter(doc, aspose.words.HeaderFooterType.FOOTER_PRIMARY)
        doc.first_section.headers_footers.add(footer)
        para = footer.append_paragraph("My footer.")
        self.assertFalse(footer.is_header)
        self.assertTrue(para.is_end_of_header_footer)
        self.assertEqual(footer, para.parent_story)
        self.assertEqual(footer.parent_section, para.parent_section)
        self.assertEqual(footer.parent_section, header.parent_section)
        doc.save(file_name = ARTIFACTS_DIR + "HeaderFooter.Create.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "HeaderFooter.Create.docx")
        self.assertTrue(("My header." in doc.first_section.headers_footers.get_by_header_footer_type(aspose.words.HeaderFooterType.HEADER_PRIMARY).range.text))
        self.assertTrue(("My footer." in doc.first_section.headers_footers.get_by_header_footer_type(aspose.words.HeaderFooterType.FOOTER_PRIMARY).range.text))

    def test_link(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_remove_footers(self):
        raise NotImplementedError("Unsupported expression: ConditionalAccessExpression")

    def test_export_mode(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Header and footer types.docx")
        self.assertEqual("First header", doc.first_section.headers_footers.get_by_header_footer_type(aspose.words.HeaderFooterType.HEADER_FIRST).get_text().strip())
        save_options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.HTML)
        save_options.export_headers_footers_mode = aspose.words.saving.ExportHeadersFootersMode.NONE
        doc.save(file_name = ARTIFACTS_DIR + "HeaderFooter.ExportMode.html", save_options = save_options)
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "HeaderFooter.ExportMode.html")
        self.assertFalse(("First header" in doc.range.text))

    def test_replace_text(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_primer(self):
        raise NotImplementedError("Unsupported call of method named CopyHeadersFootersFromPreviousSection")
