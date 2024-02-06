# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.drawing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR


class ExDocumentBase(ApiExampleBase):
    def test_constructor(self):
        raise NotImplementedError("Unsupported expression: TypeOfExpression")

    def test_set_page_color(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.page_color = aspose.pydrawing.Color.light_gray
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBase.SetPageColor.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBase.SetPageColor.docx")
        self.assertEqual(aspose.pydrawing.Color.light_gray.to_argb(), doc.page_color.to_argb())

    def test_import_node(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_import_node_custom(self):
        src_doc = aspose.words.Document()
        src_style = src_doc.styles.add(aspose.words.StyleType.CHARACTER, "My style")
        src_style.font.name = "Courier New"
        src_builder = aspose.words.DocumentBuilder(src_doc)
        src_builder.font.style = src_style
        src_builder.writeln("Source document text.")
        dst_doc = aspose.words.Document()
        dst_style = dst_doc.styles.add(aspose.words.StyleType.CHARACTER, "My style")
        dst_style.font.name = "Calibri"
        dst_builder = aspose.words.DocumentBuilder(dst_doc)
        dst_builder.font.style = dst_style
        dst_builder.writeln("Destination document text.")
        imported_section = dst_doc.import_node(src_node = src_doc.first_section, is_import_children = True, import_format_mode = aspose.words.ImportFormatMode.USE_DESTINATION_STYLES).as_section()
        self.assertEqual("Source document text.", imported_section.body.paragraphs[0].runs[0].get_text().strip())
        self.assertIsNone(dst_doc.styles.get_by_name("My style_0"))
        self.assertEqual(dst_style.font.name, imported_section.body.first_paragraph.runs[0].font.name)
        self.assertEqual(dst_style.name, imported_section.body.first_paragraph.runs[0].font.style_name)
        dst_doc.import_node(src_node = src_doc.first_section, is_import_children = True, import_format_mode = aspose.words.ImportFormatMode.KEEP_DIFFERENT_STYLES)
        self.assertEqual(dst_style.font.name, dst_doc.styles.get_by_name("My style").font.name)
        self.assertEqual(src_style.font.name, dst_doc.styles.get_by_name("My style_0").font.name)

    def test_background_shape(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")
