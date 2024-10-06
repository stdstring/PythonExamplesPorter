# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.

import aspose.words as aw
import aspose.words.drawing
import aspose.words.saving
import os
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR


class ExMarkdownSaveOptions(ApiExampleBase):
    def test_markdown_document_table_content_alignment(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_images_as_base64(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_list_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_images_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

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
        #ExStart:LinkExportMode
        #ExFor:MarkdownSaveOptions.link_export_mode
        #ExFor:MarkdownLinkExportMode
        #ExSummary:Shows how to links will be written to the .md file.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_shape(shape_type=aw.drawing.ShapeType.BALLOON, width=100, height=100)
        # Image will be written as reference:
        # ![ref1]
        #
        # [ref1]: aw_ref.001.png
        save_options = aw.saving.MarkdownSaveOptions()
        save_options.link_export_mode = aw.saving.MarkdownLinkExportMode.REFERENCE
        doc.save(file_name=ARTIFACTS_DIR + "MarkdownSaveOptions.LinkExportMode.Reference.md", save_options=save_options)
        # Image will be written as inline:
        # ![](aw_inline.001.png)
        save_options.link_export_mode = aw.saving.MarkdownLinkExportMode.INLINE
        doc.save(file_name=ARTIFACTS_DIR + "MarkdownSaveOptions.LinkExportMode.Inline.md", save_options=save_options)
        #ExEnd:LinkExportMode
        out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "MarkdownSaveOptions.LinkExportMode.Inline.md")
        self.assertEqual("![](MarkdownSaveOptions.LinkExportMode.Inline.001.png)", out_doc_contents.strip())
