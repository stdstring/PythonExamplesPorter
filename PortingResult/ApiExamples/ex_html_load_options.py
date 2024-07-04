# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.loading
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExHtmlLoadOptions(ApiExampleBase):
    def test_support_vml(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_encrypted_html(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_base_uri(self):
        raise NotImplementedError("Unsupported member target type - System.Byte[] for expression: ((Shape)doc.GetChild(NodeType.Shape, 0, true)).ImageData.ImageBytes")

    def test_get_select_as_sdt(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_get_input_as_form_field(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_ignore_noscript_elements(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_block_import(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_font_face_rules(self):
        #ExStart:FontFaceRules
        #ExFor:HtmlLoadOptions.support_font_face_rules
        #ExSummary:Shows how to load declared "@font-face" rules.
        load_options = aw.loading.HtmlLoadOptions()
        load_options.support_font_face_rules = True
        doc = aw.Document(file_name=MY_DIR + "Html with FontFace.html", load_options=load_options)
        self.assertEqual("Squarish Sans CT Regular", doc.font_infos[0].name)
        #ExEnd:FontFaceRules
