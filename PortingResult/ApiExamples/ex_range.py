# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.drawing
import aspose.words.notes
import aspose.words.replacing
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExRange(ApiExampleBase):
    def test_replace(self):
        #ExStart
        #ExFor:Range.replace(str,str)
        #ExSummary:Shows how to perform a find-and-replace text operation on the contents of a document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.writeln("Greetings, _FullName_!")
        # Perform a find-and-replace operation on our document's contents and verify the number of replacements that took place.
        replacement_count = doc.range.replace(pattern="_FullName_", replacement="John Doe")
        self.assertEqual(1, replacement_count)
        self.assertEqual("Greetings, John Doe!", doc.get_text().strip())
        #ExEnd

    def test_replace_match_case(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_replace_find_whole_words_only(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_ignore_deleted(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_ignore_inserted(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_ignore_fields(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_ignore_field_codes(self):
        raise NotImplementedError("Unsupported ctor for type Regex")

    def test_ignore_footnote(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_ignore_shapes(self):
        #ExStart
        #ExFor:FindReplaceOptions.ignore_shapes
        #ExSummary:Shows how to ignore shapes while replacing text.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        builder.insert_shape(shape_type=aw.drawing.ShapeType.BALLOON, width=200, height=200)
        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        find_replace_options = aw.replacing.FindReplaceOptions()
        find_replace_options.ignore_shapes = True
        builder.document.range.replace(pattern="Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.", replacement="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", options=find_replace_options)
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", builder.document.get_text().strip())
        #ExEnd

    def test_update_fields_in_range(self):
        #ExStart
        #ExFor:Range.update_fields
        #ExSummary:Shows how to update all the fields in a range.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.insert_field(field_code=" DOCPROPERTY Category")
        builder.insert_break(aw.BreakType.SECTION_BREAK_EVEN_PAGE)
        builder.insert_field(field_code=" DOCPROPERTY Category")
        # The above DOCPROPERTY fields will display the value of this built-in document property.
        doc.built_in_document_properties.category = "MyCategory"
        # If we update the value of a document property, we will need to update all the DOCPROPERTY fields to display it.
        self.assertEqual("", doc.range.fields[0].result)
        self.assertEqual("", doc.range.fields[1].result)
        # Update all the fields that are in the range of the first section.
        doc.first_section.range.update_fields()
        self.assertEqual("MyCategory", doc.range.fields[0].result)
        self.assertEqual("", doc.range.fields[1].result)
        #ExEnd

    def test_replace_with_string(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.writeln("This one is sad.")
        builder.writeln("That one is mad.")
        options = aw.replacing.FindReplaceOptions()
        options.match_case = False
        options.find_whole_words_only = True
        doc.range.replace(pattern="sad", replacement="bad", options=options)
        doc.save(file_name=ARTIFACTS_DIR + "Range.ReplaceWithString.docx")

    def test_replace_with_regex(self):
        raise NotImplementedError("Unsupported ctor for type Regex")

    def test_apply_paragraph_format(self):
        #ExStart
        #ExFor:FindReplaceOptions.apply_paragraph_format
        #ExFor:Range.replace(str,str)
        #ExSummary:Shows how to add formatting to paragraphs in which a find-and-replace operation has found matches.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.writeln("Every paragraph that ends with a full stop like this one will be right aligned.")
        builder.writeln("This one will not!")
        builder.write("This one also will.")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(aw.ParagraphAlignment.LEFT, paragraphs[0].paragraph_format.alignment)
        self.assertEqual(aw.ParagraphAlignment.LEFT, paragraphs[1].paragraph_format.alignment)
        self.assertEqual(aw.ParagraphAlignment.LEFT, paragraphs[2].paragraph_format.alignment)
        # We can use a "FindReplaceOptions" object to modify the find-and-replace process.
        options = aw.replacing.FindReplaceOptions()
        # Set the "Alignment" property to "ParagraphAlignment.Right" to right-align every paragraph
        # that contains a match that the find-and-replace operation finds.
        options.apply_paragraph_format.alignment = aw.ParagraphAlignment.RIGHT
        # Replace every full stop that is right before a paragraph break with an exclamation point.
        count = doc.range.replace(pattern=".&p", replacement="!&p", options=options)
        self.assertEqual(2, count)
        self.assertEqual(aw.ParagraphAlignment.RIGHT, paragraphs[0].paragraph_format.alignment)
        self.assertEqual(aw.ParagraphAlignment.LEFT, paragraphs[1].paragraph_format.alignment)
        self.assertEqual(aw.ParagraphAlignment.RIGHT, paragraphs[2].paragraph_format.alignment)
        self.assertEqual("Every paragraph that ends with a full stop like this one will be right aligned!\r" + "This one will not!\r" + "This one also will!", doc.get_text().strip())
        #ExEnd

    def test_delete_selection(self):
        #ExStart
        #ExFor:Node.range
        #ExFor:Range.delete
        #ExSummary:Shows how to delete all the nodes from a range.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Add text to the first section in the document, and then add another section.
        builder.write("Section 1. ")
        builder.insert_break(aw.BreakType.SECTION_BREAK_CONTINUOUS)
        builder.write("Section 2.")
        self.assertEqual("Section 1. \fSection 2.", doc.get_text().strip())
        # Remove the first section entirely by removing all the nodes
        # within its range, including the section itself.
        doc.sections[0].range.delete()
        self.assertEqual(1, doc.sections.count)
        self.assertEqual("Section 2.", doc.get_text().strip())
        #ExEnd

    def test_ranges_get_text(self):
        #ExStart
        #ExFor:Range
        #ExFor:Range.text
        #ExSummary:Shows how to get the text contents of all the nodes that a range covers.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.write("Hello world!")
        self.assertEqual("Hello world!", doc.range.text.strip())
        #ExEnd

    def test_use_substitutions(self):
        raise NotImplementedError("Unsupported ctor for type Regex")
