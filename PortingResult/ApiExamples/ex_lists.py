# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.pydrawing
import aspose.words as aw
import aspose.words.lists
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExLists(ApiExampleBase):
    def test_apply_default_bullets_and_numbers(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_specify_list_level(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_nested_lists(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_create_custom_list(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_restart_numbering_using_list_copy(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_create_and_use_list_style(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_detect_bulleted_paragraphs(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_remove_bullets_from_paragraphs(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_apply_existing_list_to_paragraphs(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_apply_new_list_to_paragraphs(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_outline_heading_templates(self):
        raise NotImplementedError("Unsupported call of method named AddOutlineHeadingParagraphs")

    def test_print_out_all_lists(self):
        raise NotImplementedError("Unsupported call of method named AddListSample")

    def test_list_document(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_create_list_restart_after_higher(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_get_list_labels(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_create_picture_bullet(self):
        #ExStart
        #ExFor:ListLevel.create_picture_bullet
        #ExFor:ListLevel.delete_picture_bullet
        #ExSummary:Shows how to set a custom image icon for list item labels.
        doc = aw.Document()
        list = doc.lists.add(list_template=aw.lists.ListTemplate.BULLET_CIRCLE)

        # Create a picture bullet for the current list level, and set an image from a local file system
        # as the icon that the bullets for this list level will display.
        list.list_levels[0].create_picture_bullet()
        list.list_levels[0].image_data.set_image(file_name=IMAGE_DIR + "Logo icon.ico")
        self.assertTrue(list.list_levels[0].image_data.has_image)
        builder = aw.DocumentBuilder(doc)
        builder.list_format.list = list
        builder.writeln("Hello world!")
        builder.write("Hello again!")
        doc.save(file_name=ARTIFACTS_DIR + "Lists.CreatePictureBullet.docx")
        list.list_levels[0].delete_picture_bullet()
        self.assertIsNone(list.list_levels[0].image_data)
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Lists.CreatePictureBullet.docx")
        self.assertTrue(doc.lists[0].list_levels[0].image_data.has_image)

    def test_custom_number_style_format(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_has_same_template(self):
        #ExStart
        #ExFor:List.has_same_template(List)
        #ExSummary:Shows how to define lists with the same ListDefId.
        doc = aw.Document(file_name=MY_DIR + "Different lists.docx")
        self.assertTrue(doc.lists[0].has_same_template(doc.lists[1]))
        self.assertFalse(doc.lists[1].has_same_template(doc.lists[2]))
        #ExEnd
