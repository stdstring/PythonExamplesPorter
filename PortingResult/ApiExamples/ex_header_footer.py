# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.replacing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExHeaderFooter(ApiExampleBase):
    def test_create(self):
        doc = aw.Document()
        header = aw.HeaderFooter(doc, aw.HeaderFooterType.HEADER_PRIMARY)
        doc.first_section.headers_footers.add(header)
        para = header.append_paragraph("My header.")
        self.assertTrue(header.is_header)
        self.assertTrue(para.is_end_of_header_footer)
        footer = aw.HeaderFooter(doc, aw.HeaderFooterType.FOOTER_PRIMARY)
        doc.first_section.headers_footers.add(footer)
        para = footer.append_paragraph("My footer.")
        self.assertFalse(footer.is_header)
        self.assertTrue(para.is_end_of_header_footer)
        self.assertEqual(footer, para.parent_story)
        self.assertEqual(footer.parent_section, para.parent_section)
        self.assertEqual(footer.parent_section, header.parent_section)
        doc.save(file_name=ARTIFACTS_DIR + "HeaderFooter.Create.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HeaderFooter.Create.docx")
        self.assertTrue(("My header." in doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY).range.text))
        self.assertTrue(("My footer." in doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY).range.text))

    def test_link(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_remove_footers(self):
        raise NotImplementedError("Unsupported expression: ConditionalAccessExpression")

    def test_export_mode(self):
        doc = aw.Document(file_name=MY_DIR + "Header and footer types.docx")
        self.assertEqual("First header", doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_FIRST).get_text().strip())
        save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
        save_options.export_headers_footers_mode = aw.saving.ExportHeadersFootersMode.NONE
        doc.save(file_name=ARTIFACTS_DIR + "HeaderFooter.ExportMode.html", save_options=save_options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HeaderFooter.ExportMode.html")
        self.assertFalse(("First header" in doc.range.text))

    def test_replace_text(self):
        raise NotImplementedError("Unsupported target type System.DateTime")
