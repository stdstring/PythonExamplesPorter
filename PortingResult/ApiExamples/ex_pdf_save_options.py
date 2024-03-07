# -*- coding: utf-8 -*-
import aspose.words
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
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.save_format = aspose.words.SaveFormat.PDF
        save_options.outline_options.headings_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.HeadingsOutlineLevels.pdf", save_options=save_options)

    def test_use_pdf_bookmark_editor_for_headings_outline_levels(self):
        raise NotImplementedError("Unsupported call of method named HeadingsOutlineLevels")

    def test_expanded_outline_levels(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING4
        builder.writeln("Heading 1.2.2.1")
        builder.writeln("Heading 1.2.2.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING5
        builder.writeln("Heading 1.2.2.2.1")
        builder.writeln("Heading 1.2.2.2.2")
        options = aspose.words.saving.PdfSaveOptions()
        options.outline_options.headings_outline_levels = 4
        options.outline_options.expanded_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExpandedOutlineLevels.pdf", save_options=options)

    def test_use_pdf_document_for_expanded_outline_levels(self):
        raise NotImplementedError("Unsupported call of method named ExpandedOutlineLevels")

    def test_downsample_options(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Images.docx")
        options = aspose.words.saving.PdfSaveOptions()
        self.assertTrue(options.downsample_options.downsample_images)
        self.assertEqual(220, options.downsample_options.resolution)
        self.assertEqual(0, options.downsample_options.resolution_threshold)
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DownsampleOptions.Default.pdf", save_options=options)
        options.downsample_options.resolution = 36
        options.downsample_options.resolution_threshold = 128
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DownsampleOptions.LowerResolution.pdf", save_options=options)

    def test_use_pdf_document_for_downsample_options(self):
        raise NotImplementedError("Unsupported call of method named DownsampleOptions")

    def test_zoom_behaviour(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        options = aspose.words.saving.PdfSaveOptions()
        options.zoom_behavior = aspose.words.saving.PdfZoomBehavior.ZOOM_FACTOR
        options.zoom_factor = 25
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ZoomBehaviour.pdf", save_options=options)

    def test_use_pdf_document_for_zoom_behaviour(self):
        raise NotImplementedError("Unsupported call of method named ZoomBehaviour")

    def test_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported ctor for type DateTime")

    def test_use_pdf_document_for_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported call of method named PdfDigitalSignature")

    def test_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_use_pdf_document_for_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported call of method named PdfDigitalSignatureTimestamp")

    def test_encryption_permissions(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        encryption_details = aspose.words.saving.PdfEncryptionDetails(user_password="password", owner_password="", permissions=aspose.words.saving.PdfPermissions.MODIFY_ANNOTATIONS | aspose.words.saving.PdfPermissions.DOCUMENT_ASSEMBLY)
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.encryption_details = encryption_details
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EncryptionPermissions.pdf", save_options=save_options)

    def test_use_pdf_document_for_encryption_permissions(self):
        raise NotImplementedError("Unsupported call of method named EncryptionPermissions")

    def test_export_page_set(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_use_pdf_document_for_export_page_set(self):
        raise NotImplementedError("Unsupported call of method named ExportPageSet")

    def test_export_language_to_span_tag(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        builder.writeln("Hola mundo!")
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_language_to_span_tag = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExportLanguageToSpanTag.pdf", save_options=save_options)

    def test_pdf_embed_attachments(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_ole_object(file_name=MY_DIR + "Spreadsheet.xlsx", prog_id="Excel.Sheet", is_linked=False, as_icon=True, presentation=None)
        options = aspose.words.saving.PdfSaveOptions()
        options.embed_attachments = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PdfEmbedAttachments.pdf", save_options=options)

    def test_cache_background_graphics(self):
        raise NotImplementedError("Unsupported ctor for type FileInfo")

    def test_export_paragraph_graphics_to_artifact(self):
        doc = aspose.words.Document(file_name=MY_DIR + "PDF artifacts.docx")
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_paragraph_graphics_to_artifact = True
        save_options.text_compression = aspose.words.saving.PdfTextCompression.NONE
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExportParagraphGraphicsToArtifact.pdf", save_options=save_options)

    def test_use_pdf_document_for_export_paragraph_graphics_to_artifact(self):
        raise NotImplementedError("Unsupported call of method named ExportParagraphGraphicsToArtifact")

    def test_page_layout(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Big document.docx")
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.page_layout = aspose.words.saving.PdfPageLayout.TWO_PAGE_LEFT
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PageLayout.pdf", save_options=save_options)
