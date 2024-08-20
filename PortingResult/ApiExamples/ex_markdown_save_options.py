# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.

import aspose.words as aw
import aspose.words.drawing
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR


class ExMarkdownSaveOptions(ApiExampleBase):
    def test_markdown_document_table_content_alignment(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_images_as_base64(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_list_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_images_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Path")

    def test_export_underline_formatting(self):
        #ExStart:ExportUnderlineFormatting
        #ExFor:MarkdownSaveOptions.export_underline_formatting
        #ExSummary:Shows how to export underline formatting as ++.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.underline = aw.Underline.SINGLE
        builder.write("Lorem ipsum. Dolor sit amet.")
        save_options = aw.saving.MarkdownSaveOptions()
        save_options.export_underline_formatting = True
        doc.save(file_name=ARTIFACTS_DIR + "MarkdownSaveOptions.ExportUnderlineFormatting.md", save_options=save_options)
        #ExEnd:ExportUnderlineFormatting

    def test_link_export_mode(self):
        raise NotImplementedError("Unsupported target type System.IO.File")
