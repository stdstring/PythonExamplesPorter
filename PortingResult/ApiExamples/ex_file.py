# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.saving
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExFile(ApiExampleBase):
    def test_catch_file_corrupted_exception(self):
        raise NotImplementedError("Unsupported statement type: TryStatement")

    def test_detect_encoding(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_file_format_to_string(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_detect_document_encryption(self):
        #ExStart
        #ExFor:FileFormatUtil.detect_file_format(str)
        #ExFor:FileFormatInfo
        #ExFor:FileFormatInfo.load_format
        #ExFor:FileFormatInfo.is_encrypted
        #ExSummary:Shows how to use the FileFormatUtil class to detect the document format and encryption.
        doc = aw.Document()
        # Configure a SaveOptions object to encrypt the document
        # with a password when we save it, and then save the document.
        save_options = aw.saving.OdtSaveOptions(save_format=aw.SaveFormat.ODT)
        save_options.password = "MyPassword"
        doc.save(file_name=ARTIFACTS_DIR + "File.DetectDocumentEncryption.odt", save_options=save_options)
        # Verify the file type of our document, and its encryption status.
        info = aw.FileFormatUtil.detect_file_format(file_name=ARTIFACTS_DIR + "File.DetectDocumentEncryption.odt")
        self.assertEqual(".odt", aw.FileFormatUtil.load_format_to_extension(info.load_format))
        self.assertTrue(info.is_encrypted)
        #ExEnd

    def test_detect_digital_signatures(self):
        #ExStart
        #ExFor:FileFormatUtil.detect_file_format(str)
        #ExFor:FileFormatInfo
        #ExFor:FileFormatInfo.load_format
        #ExFor:FileFormatInfo.has_digital_signature
        #ExSummary:Shows how to use the FileFormatUtil class to detect the document format and presence of digital signatures.
        # Use a FileFormatInfo instance to verify that a document is not digitally signed.
        info = aw.FileFormatUtil.detect_file_format(file_name=MY_DIR + "Document.docx")
        self.assertEqual(".docx", aw.FileFormatUtil.load_format_to_extension(info.load_format))
        self.assertFalse(info.has_digital_signature)
        certificate_holder = aw.digitalsignatures.CertificateHolder.create(file_name=MY_DIR + "morzal.pfx", password="aw", alias=None)
        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.sign_time = datetime.datetime.now()
        aw.digitalsignatures.DigitalSignatureUtil.sign(src_file_name=MY_DIR + "Document.docx", dst_file_name=ARTIFACTS_DIR + "File.DetectDigitalSignatures.docx", cert_holder=certificate_holder, sign_options=sign_options)
        # Use a new FileFormatInstance to confirm that it is signed.
        info = aw.FileFormatUtil.detect_file_format(file_name=ARTIFACTS_DIR + "File.DetectDigitalSignatures.docx")
        self.assertTrue(info.has_digital_signature)
        # We can load and access the signatures of a signed document in a collection like this.
        self.assertEqual(1, aw.digitalsignatures.DigitalSignatureUtil.load_signatures(file_name=ARTIFACTS_DIR + "File.DetectDigitalSignatures.docx").count)
        #ExEnd

    def test_save_to_detected_file_format(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_detect_file_format_save_format_to_load_format(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_extract_images(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")
