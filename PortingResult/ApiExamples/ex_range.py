# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.replacing
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExRange(ApiExampleBase):
    def test_replace(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_ignore_shapes(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_update_fields_in_range(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_field(field_code = " DOCPROPERTY Category")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_EVEN_PAGE)
        builder.insert_field(field_code = " DOCPROPERTY Category")
        doc.built_in_document_properties.category = "MyCategory"
        self.assertEqual("", doc.range.fields[0].result)
        self.assertEqual("", doc.range.fields[1].result)
        doc.first_section.range.update_fields()
        self.assertEqual("MyCategory", doc.range.fields[0].result)
        self.assertEqual("", doc.range.fields[1].result)

    def test_replace_with_string(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("This one is sad.")
        builder.writeln("That one is mad.")
        options = aspose.words.replacing.FindReplaceOptions()
        options.match_case = False
        options.find_whole_words_only = True
        doc.range.replace(pattern = "sad", replacement = "bad", options = options)
        doc.save(file_name = ARTIFACTS_DIR + "Range.ReplaceWithString.docx")

    def test_replace_with_regex(self):
        raise NotImplementedError("Unsupported type: Regex")

    def test_apply_paragraph_format(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_delete_selection(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_ranges_get_text(self):
        raise NotImplementedError("Unsupported target type System.String")
