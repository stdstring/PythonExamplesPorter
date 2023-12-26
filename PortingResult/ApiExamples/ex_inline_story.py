# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.notes
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExInlineStory(ApiExampleBase):
    def test_ref_mark_number_style(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_numbering_rule(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_start_number(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_add_footnote(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_footnote_endnote(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_add_comment(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_inline_story_revisions(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_insert_inline_story_nodes(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Is")

    def test_delete_shapes(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.CUBE, width = 100, height = 100)
        self.assertEqual(1, doc.get_child_nodes(aspose.words.NodeType.SHAPE, True).count)
        self.assertEqual(aspose.words.StoryType.MAIN_TEXT, doc.first_section.body.story_type)
        doc.first_section.body.delete_shapes()
        self.assertEqual(0, doc.get_child_nodes(aspose.words.NodeType.SHAPE, True).count)
