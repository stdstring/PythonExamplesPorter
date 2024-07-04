# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExControlChar(ApiExampleBase):
    def test_carriage_return(self):
        #ExStart
        #ExFor:ControlChar
        #ExFor:ControlChar.cr
        #ExFor:Node.get_text
        #ExSummary:Shows how to use control characters.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert paragraphs with text with DocumentBuilder.
        builder.writeln("Hello world!")
        builder.writeln("Hello again!")
        # Converting the document to text form reveals that control characters
        # represent some of the document's structural elements, such as page breaks.
        self.assertEqual(f"Hello world!{aw.ControlChar.CR}" + f"Hello again!{aw.ControlChar.CR}" + aw.ControlChar.PAGE_BREAK, doc.get_text())
        # When converting a document to string form,
        # we can omit some of the control characters with the Trim method.
        self.assertEqual(f"Hello world!{aw.ControlChar.CR}" + "Hello again!", doc.get_text().strip())
        #ExEnd

    def test_insert_control_chars(self):
        raise NotImplementedError("Unsupported target type System.Convert")
