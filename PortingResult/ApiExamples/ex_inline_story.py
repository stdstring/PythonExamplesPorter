# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.drawing
import aspose.words.notes
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExInlineStory(ApiExampleBase):
    def test_position_footnote(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_position_endnote(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_ref_mark_number_style(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_numbering_rule(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_start_number(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_add_footnote(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_footnote_endnote(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_add_comment(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_inline_story_revisions(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_insert_inline_story_nodes(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_delete_shapes(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_shape(shape_type=aw.drawing.ShapeType.CUBE, width=100, height=100)
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
        self.assertEqual(aw.StoryType.MAIN_TEXT, doc.first_section.body.story_type)
        doc.first_section.body.delete_shapes()
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)

    def test_update_actual_reference_marks(self):
        doc = aw.Document(file_name=MY_DIR + "Footnotes and endnotes.docx")
        footnote = doc.get_child(aw.NodeType.FOOTNOTE, 1, True).as_footnote()
        doc.update_fields()
        doc.update_actual_reference_marks()
        self.assertEqual("1", footnote.actual_reference_mark)
