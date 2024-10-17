# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.drawing
import aspose.words.loading
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExHtmlLoadOptions(ApiExampleBase):
    def test_support_vml(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_encrypted_html(self):
        #ExStart
        #ExFor:HtmlLoadOptions.__init__(str)
        #ExSummary:Shows how to encrypt an Html document, and then open it using a password.
        # Create and sign an encrypted HTML document from an encrypted .docx.
        certificate_holder = aw.digitalsignatures.CertificateHolder.create(file_name=MY_DIR + "morzal.pfx", password="aw")
        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.comments = "Comment"
        sign_options.sign_time = datetime.datetime.now()
        sign_options.decryption_password = "docPassword"
        input_file_name = MY_DIR + "Encrypted.docx"
        output_file_name = ARTIFACTS_DIR + "HtmlLoadOptions.EncryptedHtml.html"
        aw.digitalsignatures.DigitalSignatureUtil.sign(src_file_name=input_file_name, dst_file_name=output_file_name, cert_holder=certificate_holder, sign_options=sign_options)
        # To load and read this document, we will need to pass its decryption
        # password using a HtmlLoadOptions object.
        load_options = aw.loading.HtmlLoadOptions(password="docPassword")
        self.assertEqual(sign_options.decryption_password, load_options.password)
        doc = aw.Document(file_name=output_file_name, load_options=load_options)
        self.assertEqual("Test encrypted document.", doc.get_text().strip())
        #ExEnd

    def test_base_uri(self):
        raise NotImplementedError("Unsupported member target type - System.Byte[] for expression: ((Shape)doc.GetChild(NodeType.Shape, 0, true)).ImageData.ImageBytes")

    def test_get_select_as_sdt(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_get_input_as_form_field(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_ignore_noscript_elements(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_block_import(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_font_face_rules(self):
        #ExStart:FontFaceRules
        #ExFor:HtmlLoadOptions.support_font_face_rules
        #ExSummary:Shows how to load declared "@font-face" rules.
        load_options = aw.loading.HtmlLoadOptions()
        load_options.support_font_face_rules = True
        doc = aw.Document(file_name=MY_DIR + "Html with FontFace.html", load_options=load_options)
        self.assertEqual("Squarish Sans CT Regular", doc.font_infos[0].name)
        #ExEnd:FontFaceRules
