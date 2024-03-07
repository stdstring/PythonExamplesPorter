# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.drawing
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExDrawing(ApiExampleBase):
    def test_fill_solid(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_stroke_pattern(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_text_box(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        textbox = aspose.words.drawing.Shape(doc, aspose.words.drawing.ShapeType.TEXT_BOX)
        textbox.width = 100
        textbox.height = 100
        textbox.text_box.layout_flow = aspose.words.drawing.LayoutFlow.BOTTOM_TO_TOP
        textbox.append_child(aspose.words.Paragraph(doc))
        builder.insert_node(textbox)
        builder.move_to(textbox.first_paragraph)
        builder.write("This text is flipped 90 degrees to the left.")
        doc.save(file_name=ARTIFACTS_DIR + "Drawing.TextBox.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Drawing.TextBox.docx")
        textbox = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aspose.words.drawing.ShapeType.TEXT_BOX, textbox.shape_type)
        self.assertEqual(100, textbox.width)
        self.assertEqual(100, textbox.height)
        self.assertEqual(aspose.words.drawing.LayoutFlow.BOTTOM_TO_TOP, textbox.text_box.layout_flow)
        self.assertEqual("This text is flipped 90 degrees to the left.", textbox.get_text().strip())

    def test_get_data_from_image(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_image_data(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_image_size(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")
