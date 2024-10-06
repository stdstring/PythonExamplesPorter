# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.saving
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExTxtSaveOptions(ApiExampleBase):
    def test_page_breaks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_add_bidi_marks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_headers_footers(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_txt_list_indentation(self):
        #ExStart
        #ExFor:TxtListIndentation
        #ExFor:TxtListIndentation.count
        #ExFor:TxtListIndentation.character
        #ExFor:TxtSaveOptions.list_indentation
        #ExSummary:Shows how to configure list indenting when saving a document to plaintext.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Create a list with three levels of indentation.
        builder.list_format.apply_number_default()
        builder.writeln("Item 1")
        builder.list_format.list_indent()
        builder.writeln("Item 2")
        builder.list_format.list_indent()
        builder.write("Item 3")
        # Create a "TxtSaveOptions" object, which we can pass to the document's "Save" method
        # to modify how we save the document to plaintext.
        txt_save_options = aw.saving.TxtSaveOptions()
        # Set the "Character" property to assign a character to use
        # for padding that simulates list indentation in plaintext.
        txt_save_options.list_indentation.character = " "
        # Set the "Count" property to specify the number of times
        # to place the padding character for each list indent level.
        txt_save_options.list_indentation.count = 3
        doc.save(file_name=ARTIFACTS_DIR + "TxtSaveOptions.TxtListIndentation.txt", save_options=txt_save_options)
        doc_text = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "TxtSaveOptions.TxtListIndentation.txt")
        self.assertEqual("1. Item 1\r\n" + "   a. Item 2\r\n" + "      i. Item 3\r\n", doc_text)
        #ExEnd

    def test_simplify_list_labels(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paragraph_break(self):
        #ExStart
        #ExFor:TxtSaveOptions
        #ExFor:TxtSaveOptions.save_format
        #ExFor:TxtSaveOptionsBase
        #ExFor:TxtSaveOptionsBase.paragraph_break
        #ExSummary:Shows how to save a .txt document with a custom paragraph break.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Paragraph 1.")
        builder.writeln("Paragraph 2.")
        builder.write("Paragraph 3.")
        # Create a "TxtSaveOptions" object, which we can pass to the document's "Save" method
        # to modify how we save the document to plaintext.
        txt_save_options = aw.saving.TxtSaveOptions()
        self.assertEqual(aw.SaveFormat.TEXT, txt_save_options.save_format)
        # Set the "ParagraphBreak" to a custom value that we wish to put at the end of every paragraph.
        txt_save_options.paragraph_break = " End of paragraph.\n\n\t"
        doc.save(file_name=ARTIFACTS_DIR + "TxtSaveOptions.ParagraphBreak.txt", save_options=txt_save_options)
        doc_text = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "TxtSaveOptions.ParagraphBreak.txt")
        self.assertEqual("Paragraph 1. End of paragraph.\n\n\t" + "Paragraph 2. End of paragraph.\n\n\t" + "Paragraph 3. End of paragraph.\n\n\t", doc_text)
        #ExEnd

    def test_encoding(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_preserve_table_layout(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_max_characters_per_line(self):
        #ExStart
        #ExFor:TxtSaveOptions.max_characters_per_line
        #ExSummary:Shows how to set maximum number of characters per line.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        # Set 30 characters as maximum allowed per one line.
        save_options = aw.saving.TxtSaveOptions()
        save_options.max_characters_per_line = 30
        doc.save(file_name=ARTIFACTS_DIR + "TxtSaveOptions.MaxCharactersPerLine.txt", save_options=save_options)
        #ExEnd
