# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.replacing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExHeaderFooter(ApiExampleBase):
    def test_create(self):
        #ExStart
        #ExFor:HeaderFooter
        #ExFor:HeaderFooter.__init__(DocumentBase,HeaderFooterType)
        #ExFor:HeaderFooter.header_footer_type
        #ExFor:HeaderFooter.is_header
        #ExFor:HeaderFooterCollection
        #ExFor:Paragraph.is_end_of_header_footer
        #ExFor:Paragraph.parent_section
        #ExFor:Paragraph.parent_story
        #ExFor:Story.append_paragraph
        #ExSummary:Shows how to create a header and a footer.
        doc = aw.Document()
        # Create a header and append a paragraph to it. The text in that paragraph
        # will appear at the top of every page of this section, above the main body text.
        header = aw.HeaderFooter(doc, aw.HeaderFooterType.HEADER_PRIMARY)
        doc.first_section.headers_footers.add(header)
        para = header.append_paragraph("My header.")
        self.assertTrue(header.is_header)
        self.assertTrue(para.is_end_of_header_footer)
        # Create a footer and append a paragraph to it. The text in that paragraph
        # will appear at the bottom of every page of this section, below the main body text.
        footer = aw.HeaderFooter(doc, aw.HeaderFooterType.FOOTER_PRIMARY)
        doc.first_section.headers_footers.add(footer)
        para = footer.append_paragraph("My footer.")
        self.assertFalse(footer.is_header)
        self.assertTrue(para.is_end_of_header_footer)
        self.assertEqual(footer, para.parent_story)
        self.assertEqual(footer.parent_section, para.parent_section)
        self.assertEqual(footer.parent_section, header.parent_section)
        doc.save(file_name=ARTIFACTS_DIR + "HeaderFooter.Create.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HeaderFooter.Create.docx")
        self.assertTrue(("My header." in doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY).range.text))
        self.assertTrue(("My footer." in doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY).range.text))

    def test_link(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_remove_footers(self):
        raise NotImplementedError("Unsupported expression: ConditionalAccessExpression")

    def test_export_mode(self):
        #ExStart
        #ExFor:HtmlSaveOptions.export_headers_footers_mode
        #ExFor:ExportHeadersFootersMode
        #ExSummary:Shows how to omit headers/footers when saving a document to HTML.
        doc = aw.Document(file_name=MY_DIR + "Header and footer types.docx")
        # This document contains headers and footers. We can access them via the "HeadersFooters" collection.
        self.assertEqual("First header", doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_FIRST).get_text().strip())
        # Formats such as .html do not split the document into pages, so headers/footers will not function the same way
        # they would when we open the document as a .docx using Microsoft Word.
        # If we convert a document with headers/footers to html, the conversion will assimilate the headers/footers into body text.
        # We can use a SaveOptions object to omit headers/footers while converting to html.
        save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
        save_options.export_headers_footers_mode = aw.saving.ExportHeadersFootersMode.NONE
        doc.save(file_name=ARTIFACTS_DIR + "HeaderFooter.ExportMode.html", save_options=save_options)
        # Open our saved document and verify that it does not contain the header's text
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HeaderFooter.ExportMode.html")
        self.assertFalse(("First header" in doc.range.text))
        #ExEnd

    def test_replace_text(self):
        raise NotImplementedError("Unsupported target type System.DateTime")
