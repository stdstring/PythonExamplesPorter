# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.words as aw
import aspose.words.saving
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
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_simplify_list_labels(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paragraph_break(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

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
