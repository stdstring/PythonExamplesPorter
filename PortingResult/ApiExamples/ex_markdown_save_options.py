# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.

import aspose.words as aw
import aspose.words.drawing
import aspose.words.saving
import os
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExMarkdownSaveOptions(ApiExampleBase):
    def test_markdown_document_table_content_alignment(self):
        for table_content_alignment in [aw.saving.TableContentAlignment.LEFT,
                                        aw.saving.TableContentAlignment.RIGHT,
                                        aw.saving.TableContentAlignment.CENTER,
                                        aw.saving.TableContentAlignment.AUTO]:
            #ExStart
            #ExFor:TableContentAlignment
            #ExFor:MarkdownSaveOptions.table_content_alignment
            #ExSummary:Shows how to align contents in tables.
            builder = aw.DocumentBuilder()
            builder.insert_cell()
            builder.paragraph_format.alignment = aw.ParagraphAlignment.RIGHT
            builder.write("Cell1")
            builder.insert_cell()
            builder.paragraph_format.alignment = aw.ParagraphAlignment.CENTER
            builder.write("Cell2")
            save_options = aw.saving.MarkdownSaveOptions()
            save_options.table_content_alignment = table_content_alignment
            builder.document.save(file_name=ARTIFACTS_DIR + "MarkdownSaveOptions.MarkdownDocumentTableContentAlignment.md", save_options=save_options)
            doc = aw.Document(file_name=ARTIFACTS_DIR + "MarkdownSaveOptions.MarkdownDocumentTableContentAlignment.md")
            table = doc.first_section.body.tables[0]
            switch_condition = table_content_alignment
            if switch_condition == aw.saving.TableContentAlignment.AUTO:
                self.assertEqual(aw.ParagraphAlignment.RIGHT, table.first_row.cells[0].first_paragraph.paragraph_format.alignment)
                self.assertEqual(aw.ParagraphAlignment.CENTER, table.first_row.cells[1].first_paragraph.paragraph_format.alignment)
            elif switch_condition == aw.saving.TableContentAlignment.LEFT:
                self.assertEqual(aw.ParagraphAlignment.LEFT, table.first_row.cells[0].first_paragraph.paragraph_format.alignment)
                self.assertEqual(aw.ParagraphAlignment.LEFT, table.first_row.cells[1].first_paragraph.paragraph_format.alignment)
            elif switch_condition == aw.saving.TableContentAlignment.CENTER:
                self.assertEqual(aw.ParagraphAlignment.CENTER, table.first_row.cells[0].first_paragraph.paragraph_format.alignment)
                self.assertEqual(aw.ParagraphAlignment.CENTER, table.first_row.cells[1].first_paragraph.paragraph_format.alignment)
            elif switch_condition == aw.saving.TableContentAlignment.RIGHT:
                self.assertEqual(aw.ParagraphAlignment.RIGHT, table.first_row.cells[0].first_paragraph.paragraph_format.alignment)
                self.assertEqual(aw.ParagraphAlignment.RIGHT, table.first_row.cells[1].first_paragraph.paragraph_format.alignment)
            #ExEnd

    def test_export_images_as_base64(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_list_export_mode(self):
        for markdown_list_export_mode in [aw.saving.MarkdownListExportMode.PLAIN_TEXT,
                                          aw.saving.MarkdownListExportMode.MARKDOWN_SYNTAX]:
            #ExStart
            #ExFor:MarkdownSaveOptions.list_export_mode
            #ExFor:MarkdownListExportMode
            #ExSummary:Shows how to list items will be written to the markdown document.
            doc = aw.Document(file_name=MY_DIR + "List item.docx")
            # Use MarkdownListExportMode.PlainText or MarkdownListExportMode.MarkdownSyntax to export list.
            options = aw.saving.MarkdownSaveOptions()
            options.list_export_mode = markdown_list_export_mode
            doc.save(file_name=ARTIFACTS_DIR + "MarkdownSaveOptions.ListExportMode.md", save_options=options)
            #ExEnd

    def test_images_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_export_underline_formatting(self):
        #ExStart:ExportUnderlineFormatting
        #ExFor:MarkdownSaveOptions.export_underline_formatting
        #ExSummary:Shows how to export underline formatting as ++.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
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
        builder = aw.DocumentBuilder(doc=doc)
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
