# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExPdfSaveOptions(ApiExampleBase):
    def test_one_page(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_use_pdf_document_for_one_page(self):
        raise NotImplementedError("Unsupported call of method named OnePage")

    def test_headings_outline_levels(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        save_options = aw.saving.PdfSaveOptions()
        save_options.save_format = aw.SaveFormat.PDF
        save_options.outline_options.headings_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.HeadingsOutlineLevels.pdf", save_options=save_options)

    def test_use_pdf_bookmark_editor_for_headings_outline_levels(self):
        raise NotImplementedError("Unsupported call of method named HeadingsOutlineLevels")

    def test_create_missing_outline_levels(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_bookmark_editor_for_create_missing_outline_levels(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_table_heading_outlines(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_table_heading_outlines(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_expanded_outline_levels(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING4
        builder.writeln("Heading 1.2.2.1")
        builder.writeln("Heading 1.2.2.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING5
        builder.writeln("Heading 1.2.2.2.1")
        builder.writeln("Heading 1.2.2.2.2")
        options = aw.saving.PdfSaveOptions()
        options.outline_options.headings_outline_levels = 4
        options.outline_options.expanded_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExpandedOutlineLevels.pdf", save_options=options)

    def test_use_pdf_document_for_expanded_outline_levels(self):
        raise NotImplementedError("Unsupported call of method named ExpandedOutlineLevels")

    def test_update_fields(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_update_fields(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_preserve_form_fields(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_preserve_form_fields(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_compliance(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_compliance(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_image_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_image_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_image_color_space_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_image_color_space_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_downsample_options(self):
        doc = aw.Document(file_name=MY_DIR + "Images.docx")
        options = aw.saving.PdfSaveOptions()
        self.assertTrue(options.downsample_options.downsample_images)
        self.assertEqual(220, options.downsample_options.resolution)
        self.assertEqual(0, options.downsample_options.resolution_threshold)
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DownsampleOptions.Default.pdf", save_options=options)
        options.downsample_options.resolution = 36
        options.downsample_options.resolution_threshold = 128
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DownsampleOptions.LowerResolution.pdf", save_options=options)

    def test_use_pdf_document_for_downsample_options(self):
        raise NotImplementedError("Unsupported call of method named DownsampleOptions")

    def test_color_rendering(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_color_rendering(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_doc_title(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_doc_title(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_memory_optimization(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_escape_uri(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_escape_uri(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_open_hyperlinks_in_new_window(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_header_footer_bookmarks_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_header_footer_bookmarks_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_emulate_rendering_to_size_on_page(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_emulate_rendering_to_size_on_page(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_embed_full_fonts(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_embed_windows_fonts(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_embed_core_fonts(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_additional_text_positioning(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_additional_text_positioning(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_save_as_pdf_book_fold(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_save_as_pdf_book_fold(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_zoom_behaviour(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        options = aw.saving.PdfSaveOptions()
        options.zoom_behavior = aw.saving.PdfZoomBehavior.ZOOM_FACTOR
        options.zoom_factor = 25
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ZoomBehaviour.pdf", save_options=options)

    def test_use_pdf_document_for_zoom_behaviour(self):
        raise NotImplementedError("Unsupported call of method named ZoomBehaviour")

    def test_use_pdf_document_for_page_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_note_hyperlinks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_note_hyperlinks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_custom_properties_export(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_custom_properties_export(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_drawing_ml_effects(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_drawing_ml_effects(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_drawing_ml_fallback(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_drawing_ml_fallback(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_document_structure(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported ctor for type DateTime")

    def test_use_pdf_document_for_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported call of method named PdfDigitalSignature")

    def test_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_use_pdf_document_for_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported call of method named PdfDigitalSignatureTimestamp")

    def test_render_metafile(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_render_metafile(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_encryption_permissions(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        encryption_details = aw.saving.PdfEncryptionDetails(user_password="password", owner_password="", permissions=aw.saving.PdfPermissions.MODIFY_ANNOTATIONS | aw.saving.PdfPermissions.DOCUMENT_ASSEMBLY)
        save_options = aw.saving.PdfSaveOptions()
        save_options.encryption_details = encryption_details
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EncryptionPermissions.pdf", save_options=save_options)

    def test_use_pdf_document_for_encryption_permissions(self):
        raise NotImplementedError("Unsupported call of method named EncryptionPermissions")

    def test_set_numeral_format(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_set_numeral_format(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_page_set(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_use_pdf_document_for_export_page_set(self):
        raise NotImplementedError("Unsupported call of method named ExportPageSet")

    def test_export_language_to_span_tag(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        builder.writeln("Hola mundo!")
        save_options = aw.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_language_to_span_tag = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExportLanguageToSpanTag.pdf", save_options=save_options)

    def test_pdf_embed_attachments(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_ole_object(file_name=MY_DIR + "Spreadsheet.xlsx", prog_id="Excel.Sheet", is_linked=False, as_icon=True, presentation=None)
        options = aw.saving.PdfSaveOptions()
        options.embed_attachments = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PdfEmbedAttachments.pdf", save_options=options)

    def test_cache_background_graphics(self):
        raise NotImplementedError("Unsupported ctor for type FileInfo")

    def test_export_paragraph_graphics_to_artifact(self):
        doc = aw.Document(file_name=MY_DIR + "PDF artifacts.docx")
        save_options = aw.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_paragraph_graphics_to_artifact = True
        save_options.text_compression = aw.saving.PdfTextCompression.NONE
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExportParagraphGraphicsToArtifact.pdf", save_options=save_options)

    def test_use_pdf_document_for_export_paragraph_graphics_to_artifact(self):
        raise NotImplementedError("Unsupported call of method named ExportParagraphGraphicsToArtifact")

    def test_page_layout(self):
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        save_options = aw.saving.PdfSaveOptions()
        save_options.page_layout = aw.saving.PdfPageLayout.TWO_PAGE_LEFT
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PageLayout.pdf", save_options=save_options)
