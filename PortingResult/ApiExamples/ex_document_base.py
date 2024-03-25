# -*- coding: utf-8 -*-
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
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.page_color = aspose.pydrawing.Color.light_gray
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBase.SetPageColor.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentBase.SetPageColor.docx")
        self.assertEqual(aspose.pydrawing.Color.light_gray.to_argb(), doc.page_color.to_argb())

    def test_import_node(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_import_node_custom(self):
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
        imported_section = dst_doc.import_node(src_node=src_doc.first_section, is_import_children=True, import_format_mode=aw.ImportFormatMode.USE_DESTINATION_STYLES).as_section()
        self.assertEqual("Source document text.", imported_section.body.paragraphs[0].runs[0].get_text().strip())
        self.assertIsNone(dst_doc.styles.get_by_name("My style_0"))
        self.assertEqual(dst_style.font.name, imported_section.body.first_paragraph.runs[0].font.name)
        self.assertEqual(dst_style.name, imported_section.body.first_paragraph.runs[0].font.style_name)
        dst_doc.import_node(src_node=src_doc.first_section, is_import_children=True, import_format_mode=aw.ImportFormatMode.KEEP_DIFFERENT_STYLES)
        self.assertEqual(dst_style.font.name, dst_doc.styles.get_by_name("My style").font.name)
        self.assertEqual(src_style.font.name, dst_doc.styles.get_by_name("My style_0").font.name)

    def test_background_shape(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_use_pdf_document_for_background_shape(self):
        raise NotImplementedError("Unsupported call of method named BackgroundShape")
