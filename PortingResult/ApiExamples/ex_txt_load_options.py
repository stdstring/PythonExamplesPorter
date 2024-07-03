# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.loading
import unittest
from api_example_base import ApiExampleBase, MY_DIR


class ExTxtLoadOptions(ApiExampleBase):
    def test_detect_numbering_with_whitespaces(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_trail_spaces(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_detect_document_direction(self):
        #ExStart
        #ExFor:TxtLoadOptions.document_direction
        #ExFor:ParagraphFormat.bidi
        #ExSummary:Shows how to detect plaintext document text direction.
        # Create a "TxtLoadOptions" object, which we can pass to a document's constructor
        # to modify how we load a plaintext document.
        load_options = aw.loading.TxtLoadOptions()
        # Set the "DocumentDirection" property to "DocumentDirection.Auto" automatically detects
        # the direction of every paragraph of text that Aspose.Words loads from plaintext.
        # Each paragraph's "Bidi" property will store its direction.
        load_options.document_direction = aw.loading.DocumentDirection.AUTO
        # Detect Hebrew text as right-to-left.
        doc = aw.Document(file_name=MY_DIR + "Hebrew text.txt", load_options=load_options)
        self.assertTrue(doc.first_section.body.first_paragraph.paragraph_format.bidi)
        # Detect English text as right-to-left.
        doc = aw.Document(file_name=MY_DIR + "English text.txt", load_options=load_options)
        self.assertFalse(doc.first_section.body.first_paragraph.paragraph_format.bidi)
        #ExEnd

    def test_auto_numbering_detection(self):
        #ExStart
        #ExFor:TxtLoadOptions.auto_numbering_detection
        #ExSummary:Shows how to disable automatic numbering detection.
        options = aw.loading.TxtLoadOptions()
        options.auto_numbering_detection = False
        doc = aw.Document(file_name=MY_DIR + "Number detection.txt", load_options=options)
        #ExEnd
        list_items_count = 0
        for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            paragraph = paragraph.as_paragraph()
            if paragraph.is_list_item:
                list_items_count += 1
        self.assertEqual(0, list_items_count)

    def test_detect_hyperlinks(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")
