# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.pydrawing
import aspose.words as aw
import aspose.words.fields
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExParagraph(ApiExampleBase):
    def test_document_builder_insert_paragraph(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_append_field(self):
        raise NotImplementedError("Unsupported ctor for type TimeSpan")

    def test_insert_field(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_insert_field_before_text_in_paragraph(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_after_text_in_paragraph(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_insert_field_before_text_in_paragraph_without_update_field(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_after_text_in_paragraph_without_update_field(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_without_separator(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_before_paragraph_without_document_author(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_after_paragraph_without_changing_document_author(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_before_run_text(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_after_run_text(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_empty_paragraph_without_update_field(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_empty_paragraph_with_update_field(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_composite_node_children(self):
        #ExStart
        #ExFor:CompositeNode.count
        #ExFor:CompositeNode.get_child_nodes(NodeType,bool)
        #ExFor:CompositeNode.insert_after
        #ExFor:CompositeNode.insert_before
        #ExFor:CompositeNode.prepend_child
        #ExFor:Paragraph.get_text
        #ExFor:Run
        #ExSummary:Shows how to add, update and delete child nodes in a CompositeNode's collection of children.
        doc = aw.Document()
        # An empty document, by default, has one paragraph.
        self.assertEqual(1, doc.first_section.body.paragraphs.count)
        # Composite nodes such as our paragraph can contain other composite and inline nodes as children.
        paragraph = doc.first_section.body.first_paragraph
        paragraph_text = aw.Run(doc=doc, text="Initial text. ")
        paragraph.append_child(paragraph_text)
        # Create three more run nodes.
        run1 = aw.Run(doc=doc, text="Run 1. ")
        run2 = aw.Run(doc=doc, text="Run 2. ")
        run3 = aw.Run(doc=doc, text="Run 3. ")
        # The document body will not display these runs until we insert them into a composite node
        # that itself is a part of the document's node tree, as we did with the first run.
        # We can determine where the text contents of nodes that we insert
        # appears in the document by specifying an insertion location relative to another node in the paragraph.
        self.assertEqual("Initial text.", paragraph.get_text().strip())
        # Insert the second run into the paragraph in front of the initial run.
        paragraph.insert_before(run2, paragraph_text)
        self.assertEqual("Run 2. Initial text.", paragraph.get_text().strip())
        # Insert the third run after the initial run.
        paragraph.insert_after(run3, paragraph_text)
        self.assertEqual("Run 2. Initial text. Run 3.", paragraph.get_text().strip())
        # Insert the first run to the start of the paragraph's child nodes collection.
        paragraph.prepend_child(run1)
        self.assertEqual("Run 1. Run 2. Initial text. Run 3.", paragraph.get_text().strip())
        self.assertEqual(4, paragraph.get_child_nodes(aw.NodeType.ANY, True).count)
        # We can modify the contents of the run by editing and deleting existing child nodes.
        (paragraph.get_child_nodes(aw.NodeType.RUN, True)[1].as_run()).text = "Updated run 2. "
        paragraph.get_child_nodes(aw.NodeType.RUN, True).remove(paragraph_text)
        self.assertEqual("Run 1. Updated run 2. Run 3.", paragraph.get_text().strip())
        self.assertEqual(3, paragraph.get_child_nodes(aw.NodeType.ANY, True).count)
        #ExEnd

    def test_move_revisions(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_range_revisions(self):
        #ExStart
        #ExFor:Range.revisions
        #ExSummary:Shows how to work with revisions in range.
        doc = aw.Document(file_name=MY_DIR + "Revisions.docx")
        paragraph = doc.first_section.body.first_paragraph
        for revision in paragraph.range.revisions:
            if revision.revision_type == aw.RevisionType.DELETION:
                revision.accept()
        # Reject the first section revisions.
        doc.first_section.range.revisions.reject_all()
        #ExEnd

    def test_get_format_revision(self):
        #ExStart
        #ExFor:Paragraph.is_format_revision
        #ExSummary:Shows how to check whether a paragraph is a format revision.
        doc = aw.Document(file_name=MY_DIR + "Format revision.docx")
        # This paragraph is a "Format" revision, which occurs when we change the formatting of existing text
        # while tracking revisions in Microsoft Word via "Review" -> "Track changes".
        self.assertTrue(doc.first_section.body.first_paragraph.is_format_revision)
        #ExEnd

    def test_get_frame_properties(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_is_revision(self):
        #ExStart
        #ExFor:Paragraph.is_delete_revision
        #ExFor:Paragraph.is_insert_revision
        #ExSummary:Shows how to work with revision paragraphs.
        doc = aw.Document()
        body = doc.first_section.body
        para = body.first_paragraph
        para.append_child(aw.Run(doc=doc, text="Paragraph 1. "))
        body.append_paragraph("Paragraph 2. ")
        body.append_paragraph("Paragraph 3. ")
        # The above paragraphs are not revisions.
        # Paragraphs that we add after starting revision tracking will register as "Insert" revisions.
        doc.start_track_revisions(author="John Doe", date_time=datetime.datetime.now())
        para = body.append_paragraph("Paragraph 4. ")
        self.assertTrue(para.is_insert_revision)
        # Paragraphs that we remove after starting revision tracking will register as "Delete" revisions.
        paragraphs = body.paragraphs
        self.assertEqual(4, paragraphs.count)
        para = paragraphs[2]
        para.remove()
        # Such paragraphs will remain until we either accept or reject the delete revision.
        # Accepting the revision will remove the paragraph for good,
        # and rejecting the revision will leave it in the document as if we never deleted it.
        self.assertEqual(4, paragraphs.count)
        self.assertTrue(para.is_delete_revision)
        # Accept the revision, and then verify that the paragraph is gone.
        doc.accept_all_revisions()
        self.assertEqual(3, paragraphs.count)
        self.assertEqual(0, para.count)
        self.assertEqual("Paragraph 1. \r" + "Paragraph 2. \r" + "Paragraph 4.", doc.get_text().strip())
        #ExEnd

    def test_break_is_style_separator(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_tab_stops(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.TabStop[] for expression: doc.FirstSection.Body.FirstParagraph.GetEffectiveTabStops()")

    def test_join_runs(self):
        #ExStart
        #ExFor:Paragraph.join_runs_with_same_formatting
        #ExSummary:Shows how to simplify paragraphs by merging superfluous runs.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert four runs of text into the paragraph.
        builder.write("Run 1. ")
        builder.write("Run 2. ")
        builder.write("Run 3. ")
        builder.write("Run 4. ")
        # If we open this document in Microsoft Word, the paragraph will look like one seamless text body.
        # However, it will consist of four separate runs with the same formatting. Fragmented paragraphs like this
        # may occur when we manually edit parts of one paragraph many times in Microsoft Word.
        para = builder.current_paragraph
        self.assertEqual(4, para.runs.count)
        # Change the style of the last run to set it apart from the first three.
        para.runs[3].font.style_identifier = aw.StyleIdentifier.EMPHASIS
        # We can run the "JoinRunsWithSameFormatting" method to optimize the document's contents
        # by merging similar runs into one, reducing their overall count.
        # This method also returns the number of runs that this method merged.
        # These two merges occurred to combine Runs #1, #2, and #3,
        # while leaving out Run #4 because it has an incompatible style.
        self.assertEqual(2, para.join_runs_with_same_formatting())
        # The number of runs left will equal the original count
        # minus the number of run merges that the "JoinRunsWithSameFormatting" method carried out.
        self.assertEqual(2, para.runs.count)
        self.assertEqual("Run 1. Run 2. Run 3. ", para.runs[0].text)
        self.assertEqual("Run 4. ", para.runs[1].text)
        #ExEnd
