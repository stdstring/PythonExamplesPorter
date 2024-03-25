# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExParagraph(ApiExampleBase):
    def test_document_builder_insert_paragraph(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_insert_field_before_text_in_paragraph(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

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
        doc = aw.Document()
        self.assertEqual(1, doc.first_section.body.paragraphs.count)
        paragraph = doc.first_section.body.first_paragraph
        paragraph_text = aw.Run(doc=doc, text="Initial text. ")
        paragraph.append_child(paragraph_text)
        run1 = aw.Run(doc=doc, text="Run 1. ")
        run2 = aw.Run(doc=doc, text="Run 2. ")
        run3 = aw.Run(doc=doc, text="Run 3. ")
        self.assertEqual("Initial text.", paragraph.get_text().strip())
        paragraph.insert_before(run2, paragraph_text)
        self.assertEqual("Run 2. Initial text.", paragraph.get_text().strip())
        paragraph.insert_after(run3, paragraph_text)
        self.assertEqual("Run 2. Initial text. Run 3.", paragraph.get_text().strip())
        paragraph.prepend_child(run1)
        self.assertEqual("Run 1. Run 2. Initial text. Run 3.", paragraph.get_text().strip())
        self.assertEqual(4, paragraph.get_child_nodes(aw.NodeType.ANY, True).count)
        (paragraph.get_child_nodes(aw.NodeType.RUN, True)[1].as_run()).text = "Updated run 2. "
        paragraph.get_child_nodes(aw.NodeType.RUN, True).remove(paragraph_text)
        self.assertEqual("Run 1. Updated run 2. Run 3.", paragraph.get_text().strip())
        self.assertEqual(3, paragraph.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_move_revisions(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_range_revisions(self):
        doc = aw.Document(file_name=MY_DIR + "Revisions.docx")
        paragraph = doc.first_section.body.first_paragraph
        for revision in paragraph.range.revisions:
            if revision.revision_type == aw.RevisionType.DELETION:
                revision.accept()
        doc.first_section.range.revisions.reject_all()

    def test_get_format_revision(self):
        doc = aw.Document(file_name=MY_DIR + "Format revision.docx")
        self.assertTrue(doc.first_section.body.first_paragraph.is_format_revision)

    def test_get_frame_properties(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_is_revision(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_break_is_style_separator(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_tab_stops(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.TabStop[] for expression: doc.FirstSection.Body.FirstParagraph.GetEffectiveTabStops()")

    def test_join_runs(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Run 1. ")
        builder.write("Run 2. ")
        builder.write("Run 3. ")
        builder.write("Run 4. ")
        para = builder.current_paragraph
        self.assertEqual(4, para.runs.count)
        para.runs[3].font.style_identifier = aw.StyleIdentifier.EMPHASIS
        self.assertEqual(2, para.join_runs_with_same_formatting())
        self.assertEqual(2, para.runs.count)
        self.assertEqual("Run 1. Run 2. Run 3. ", para.runs[0].text)
        self.assertEqual("Run 4. ", para.runs[1].text)
