# -*- coding: utf-8 -*-
import aspose.words
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
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        save_options = aspose.words.saving.TxtSaveOptions()
        save_options.max_characters_per_line = 30
        doc.save(file_name=ARTIFACTS_DIR + "TxtSaveOptions.MaxCharactersPerLine.txt", save_options=save_options)
