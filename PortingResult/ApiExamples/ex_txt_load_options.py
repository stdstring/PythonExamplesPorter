# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.loading
import unittest
from api_example_base import ApiExampleBase, MY_DIR


class ExTxtLoadOptions(ApiExampleBase):
    def test_detect_document_direction(self):
        load_options = aspose.words.loading.TxtLoadOptions()
        load_options.document_direction = aspose.words.loading.DocumentDirection.AUTO
        doc = aspose.words.Document(file_name = MY_DIR + "Hebrew text.txt", load_options = load_options)
        self.assertTrue(doc.first_section.body.first_paragraph.paragraph_format.bidi)
        doc = aspose.words.Document(file_name = MY_DIR + "English text.txt", load_options = load_options)
        self.assertFalse(doc.first_section.body.first_paragraph.paragraph_format.bidi)

    def test_auto_numbering_detection(self):
        options = aspose.words.loading.TxtLoadOptions()
        options.auto_numbering_detection = False
        doc = aspose.words.Document(file_name = MY_DIR + "Number detection.txt", load_options = options)
        list_items_count = 0
        # for each loop begin
        for paragraph in doc.get_child_nodes(aspose.words.NodeType.PARAGRAPH, True):
            paragraph = paragraph.as_paragraph()
            # if begin
            if paragraph.is_list_item:
                list_items_count += 1
            # if end
        # for loop end
        self.assertEqual(0, list_items_count)
