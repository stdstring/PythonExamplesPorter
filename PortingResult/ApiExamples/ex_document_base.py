# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.pydrawing
import aspose.words as aw
import aspose.words.drawing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR


class ExDocumentBase(ApiExampleBase):
    def test_constructor(self):
        raise NotImplementedError("Unsupported expression: TypeOfExpression")

    def test_set_page_color(self):
        #ExStart
        #ExFor:DocumentBase.page_color
        #ExSummary:Shows how to set the background color for all pages of a document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.page_color = aspose.pydrawing.Color.light_gray
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBase.SetPageColor.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentBase.SetPageColor.docx")
        self.assertEqual(aspose.pydrawing.Color.light_gray.to_argb(), doc.page_color.to_argb())

    def test_import_node(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_import_node_custom(self):
        #ExStart
        #ExFor:DocumentBase.import_node(Node,bool,ImportFormatMode)
        #ExSummary:Shows how to import node from source document to destination document with specific options.
        # Create two documents and add a character style to each document.
        # Configure the styles to have the same name, but different text formatting.
        src_doc = aw.Document()
        src_style = src_doc.styles.add(aw.StyleType.CHARACTER, "My style")
        src_style.font.name = "Courier New"
        src_builder = aw.DocumentBuilder(src_doc)
        src_builder.font.style = src_style
        src_builder.writeln("Source document text.")
        dst_doc = aw.Document()
        dst_style = dst_doc.styles.add(aw.StyleType.CHARACTER, "My style")
        dst_style.font.name = "Calibri"
        dst_builder = aw.DocumentBuilder(dst_doc)
        dst_builder.font.style = dst_style
        dst_builder.writeln("Destination document text.")

        # Import the Section from the destination document into the source document, causing a style name collision.
        # If we use destination styles, then the imported source text with the same style name
        # as destination text will adopt the destination style.
        imported_section = dst_doc.import_node(src_node=src_doc.first_section, is_import_children=True, import_format_mode=aw.ImportFormatMode.USE_DESTINATION_STYLES).as_section()
        self.assertEqual("Source document text.", imported_section.body.paragraphs[0].runs[0].get_text().strip()) #ExSkip
        self.assertIsNone(dst_doc.styles.get_by_name("My style_0")) #ExSkip
        self.assertEqual(dst_style.font.name, imported_section.body.first_paragraph.runs[0].font.name)
        self.assertEqual(dst_style.name, imported_section.body.first_paragraph.runs[0].font.style_name)

        # If we use ImportFormatMode.KeepDifferentStyles, the source style is preserved,
        # and the naming clash resolves by adding a suffix.
        dst_doc.import_node(src_node=src_doc.first_section, is_import_children=True, import_format_mode=aw.ImportFormatMode.KEEP_DIFFERENT_STYLES)
        self.assertEqual(dst_style.font.name, dst_doc.styles.get_by_name("My style").font.name)
        self.assertEqual(src_style.font.name, dst_doc.styles.get_by_name("My style_0").font.name)
        #ExEnd

    def test_background_shape(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_use_pdf_document_for_background_shape(self):
        raise NotImplementedError("Unsupported call of method named BackgroundShape")
