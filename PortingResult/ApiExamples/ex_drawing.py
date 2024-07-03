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
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExDrawing(ApiExampleBase):
    def test_various_shapes(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_import_image(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_type_of_image(self):
        #ExStart
        #ExFor:ImageType
        #ExSummary:Shows how to add an image to a shape and check its type.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        img_shape = builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
        self.assertEqual(aw.drawing.ImageType.JPEG, img_shape.image_data.image_type)
        #ExEnd

    def test_fill_solid(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_save_all_images(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_stroke_pattern(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_text_box(self):
        #ExStart
        #ExFor:LayoutFlow
        #ExSummary:Shows how to add text to a text box, and change its orientation
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        textbox = aw.drawing.Shape(doc, aw.drawing.ShapeType.TEXT_BOX)
        textbox.width = 100
        textbox.height = 100
        textbox.text_box.layout_flow = aw.drawing.LayoutFlow.BOTTOM_TO_TOP
        textbox.append_child(aw.Paragraph(doc))
        builder.insert_node(textbox)
        builder.move_to(textbox.first_paragraph)
        builder.write("This text is flipped 90 degrees to the left.")
        doc.save(file_name=ARTIFACTS_DIR + "Drawing.TextBox.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Drawing.TextBox.docx")
        textbox = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.drawing.ShapeType.TEXT_BOX, textbox.shape_type)
        self.assertEqual(100, textbox.width)
        self.assertEqual(100, textbox.height)
        self.assertEqual(aw.drawing.LayoutFlow.BOTTOM_TO_TOP, textbox.text_box.layout_flow)
        self.assertEqual("This text is flipped 90 degrees to the left.", textbox.get_text().strip())

    def test_get_data_from_image(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_image_data(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_image_size(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")
