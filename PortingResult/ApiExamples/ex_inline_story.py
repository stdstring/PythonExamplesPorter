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
        #ExStart
        #ExFor:Story
        #ExFor:Story.delete_shapes
        #ExFor:Story.story_type
        #ExFor:StoryType
        #ExSummary:Shows how to remove all shapes from a node.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Use a DocumentBuilder to insert a shape. This is an inline shape,
        # which has a parent Paragraph, which is a child node of the first section's Body.
        builder.insert_shape(shape_type=aw.drawing.ShapeType.CUBE, width=100, height=100)
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)

        # We can delete all shapes from the child paragraphs of this Body.
        self.assertEqual(aw.StoryType.MAIN_TEXT, doc.first_section.body.story_type)
        doc.first_section.body.delete_shapes()
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
        #ExEnd

    def test_update_actual_reference_marks(self):
        #ExStart:UpdateActualReferenceMarks
        #GistId:a775441ecb396eea917a2717cb9e8f8f
        #ExFor:Document.update_actual_reference_marks
        #ExFor:Footnote.actual_reference_mark
        #ExSummary:Shows how to get actual footnote reference mark.
        doc = aw.Document(file_name=MY_DIR + "Footnotes and endnotes.docx")
        footnote = doc.get_child(aw.NodeType.FOOTNOTE, 1, True).as_footnote()
        doc.update_fields()
        doc.update_actual_reference_marks()
        self.assertEqual("1", footnote.actual_reference_mark)
        #ExEnd:UpdateActualReferenceMarks
