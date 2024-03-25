# -*- coding: utf-8 -*-
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
        load_options = aw.loading.TxtLoadOptions()
        load_options.document_direction = aw.loading.DocumentDirection.AUTO
        doc = aw.Document(file_name=MY_DIR + "Hebrew text.txt", load_options=load_options)
        self.assertTrue(doc.first_section.body.first_paragraph.paragraph_format.bidi)
        doc = aw.Document(file_name=MY_DIR + "English text.txt", load_options=load_options)
        self.assertFalse(doc.first_section.body.first_paragraph.paragraph_format.bidi)

    def test_auto_numbering_detection(self):
        options = aw.loading.TxtLoadOptions()
        options.auto_numbering_detection = False
        doc = aw.Document(file_name=MY_DIR + "Number detection.txt", load_options=options)
        list_items_count = 0
        for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            paragraph = paragraph.as_paragraph()
            if paragraph.is_list_item:
                list_items_count += 1
        self.assertEqual(0, list_items_count)

    def test_detect_hyperlinks(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")
