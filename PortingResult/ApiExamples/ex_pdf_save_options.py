# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.digitalsignatures
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExPdfSaveOptions(ApiExampleBase):
    def test_one_page(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_headings_outline_levels(self):
        raise NotImplementedError("Unsupported ctor for type PdfBookmarkEditor")

    def test_expanded_outline_levels(self):
        raise NotImplementedError("Unsupported ctor for type Aspose.Pdf.Document")

    def test_downsample_options(self):
        raise NotImplementedError("Unsupported ctor for type Aspose.Pdf.Document")

    def test_zoom_behaviour(self):
        raise NotImplementedError("Unsupported ctor for type Aspose.Pdf.Document")

    def test_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_encryption_permissions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_export_page_set(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_export_language_to_span_tag(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        builder.writeln("Hola mundo!")
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_language_to_span_tag = True
        doc.save(file_name = ARTIFACTS_DIR + "PdfSaveOptions.ExportLanguageToSpanTag.pdf", save_options = save_options)

    def test_pdf_embed_attachments(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_ole_object(file_name = MY_DIR + "Spreadsheet.xlsx", prog_id = "Excel.Sheet", is_linked = False, as_icon = True, presentation = None)
        options = aspose.words.saving.PdfSaveOptions()
        options.embed_attachments = True
        doc.save(file_name = ARTIFACTS_DIR + "PdfSaveOptions.PdfEmbedAttachments.pdf", save_options = options)

    def test_cache_background_graphics(self):
        raise NotImplementedError("Unsupported ctor for type FileInfo")

    def test_export_paragraph_graphics_to_artifact(self):
        raise NotImplementedError("Unsupported ctor for type Aspose.Pdf.Document")
