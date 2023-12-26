# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, MY_DIR


class ExParagraph(ApiExampleBase):
    def test_document_builder_insert_paragraph(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

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
        raise NotImplementedError("Unsupported target type System.String")

    def test_move_revisions(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_range_revisions(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Revisions.docx")
        paragraph = doc.first_section.body.first_paragraph
        # for each loop begin
        for revision in paragraph.range.revisions:
            # if begin
            if revision.revision_type == aspose.words.RevisionType.DELETION:
                revision.accept()
            # if end
        # for loop end
        doc.first_section.range.revisions.reject_all()

    def test_get_format_revision(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_get_frame_properties(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_is_revision(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_break_is_style_separator(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_tab_stops(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.TabStop[] for expression: doc.FirstSection.Body.FirstParagraph.GetEffectiveTabStops()")

    def test_join_runs(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Run 1. ")
        builder.write("Run 2. ")
        builder.write("Run 3. ")
        builder.write("Run 4. ")
        para = builder.current_paragraph
        self.assertEqual(4, para.runs.count)
        para.runs[3].font.style_identifier = aspose.words.StyleIdentifier.EMPHASIS
        self.assertEqual(2, para.join_runs_with_same_formatting())
        self.assertEqual(2, para.runs.count)
        self.assertEqual("Run 1. Run 2. Run 3. ", para.runs[0].text)
        self.assertEqual("Run 4. ", para.runs[1].text)
