# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.drawing
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, IMAGE_URL, MY_DIR


class ExImage(ApiExampleBase):
    def test_from_file(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_from_url(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_create_floating_page_center(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_create_floating_position_size(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_image_with_hyperlink(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_create_linked_image(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_delete_all_images(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_delete_all_images_pre_order(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_scale_image(self):
        raise NotImplementedError("Unsupported assignment expression: MultiplyAssignmentExpression")

    def test_insert_webp_image(self):
        #ExStart:InsertWebpImage
        #ExFor:DocumentBuilder.insert_image(str)
        #ExSummary:Shows how to insert WebP image.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.insert_image(file_name=IMAGE_DIR + "WebP image.webp")
        doc.save(file_name=ARTIFACTS_DIR + "Image.InsertWebpImage.docx")
        #ExEnd:InsertWebpImage

    def test_read_webp_image(self):
        #ExStart:ReadWebpImage
        #ExFor:ImageType
        #ExSummary:Shows how to read WebP image.
        doc = aw.Document(file_name=MY_DIR + "Document with WebP image.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.drawing.ImageType.WEB_P, shape.image_data.image_type)
        #ExEnd:ReadWebpImage
