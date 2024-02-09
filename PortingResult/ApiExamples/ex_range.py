# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.replacing
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExRange(ApiExampleBase):
    def test_replace(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Greetings, _FullName_!")
        replacement_count = doc.range.replace(pattern = "_FullName_", replacement = "John Doe")
        self.assertEqual(1, replacement_count)
        self.assertEqual("Greetings, John Doe!", doc.get_text().strip())

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
        raise NotImplementedError("Unsupported ctor for type Regex")

    def test_apply_paragraph_format(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Every paragraph that ends with a full stop like this one will be right aligned.")
        builder.writeln("This one will not!")
        builder.write("This one also will.")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(aspose.words.ParagraphAlignment.LEFT, paragraphs[0].paragraph_format.alignment)
        self.assertEqual(aspose.words.ParagraphAlignment.LEFT, paragraphs[1].paragraph_format.alignment)
        self.assertEqual(aspose.words.ParagraphAlignment.LEFT, paragraphs[2].paragraph_format.alignment)
        options = aspose.words.replacing.FindReplaceOptions()
        options.apply_paragraph_format.alignment = aspose.words.ParagraphAlignment.RIGHT
        count = doc.range.replace(pattern = ".&p", replacement = "!&p", options = options)
        self.assertEqual(2, count)
        self.assertEqual(aspose.words.ParagraphAlignment.RIGHT, paragraphs[0].paragraph_format.alignment)
        self.assertEqual(aspose.words.ParagraphAlignment.LEFT, paragraphs[1].paragraph_format.alignment)
        self.assertEqual(aspose.words.ParagraphAlignment.RIGHT, paragraphs[2].paragraph_format.alignment)
        self.assertEqual("Every paragraph that ends with a full stop like this one will be right aligned!\r" + "This one will not!\r" + "This one also will!", doc.get_text().strip())

    def test_delete_selection(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Section 1. ")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_CONTINUOUS)
        builder.write("Section 2.")
        self.assertEqual("Section 1. \fSection 2.", doc.get_text().strip())
        doc.sections[0].range.delete()
        self.assertEqual(1, doc.sections.count)
        self.assertEqual("Section 2.", doc.get_text().strip())

    def test_ranges_get_text(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Hello world!")
        self.assertEqual("Hello world!", doc.range.text.strip())
