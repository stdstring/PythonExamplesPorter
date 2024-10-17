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
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExDigitalSignatureUtil(ApiExampleBase):
    def test_load(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_remove(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_remove_signatures(self):
        aw.digitalsignatures.DigitalSignatureUtil.remove_all_signatures(src_file_name=MY_DIR + "Digitally signed.odt", dst_file_name=ARTIFACTS_DIR + "DigitalSignatureUtil.RemoveSignatures.odt")
        self.assertEqual(0, aw.digitalsignatures.DigitalSignatureUtil.load_signatures(file_name=ARTIFACTS_DIR + "DigitalSignatureUtil.RemoveSignatures.odt").count)

    def test_sign_document(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_decryption_password(self):
        #ExStart
        #ExFor:CertificateHolder
        #ExFor:SignOptions.decryption_password
        #ExFor:LoadOptions.password
        #ExSummary:Shows how to sign encrypted document file.
        # Create an X.509 certificate from a PKCS#12 store, which should contain a private key.
        certificate_holder = aw.digitalsignatures.CertificateHolder.create(file_name=MY_DIR + "morzal.pfx", password="aw")
        # Create a comment, date, and decryption password which will be applied with our new digital signature.
        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.comments = "Comment"
        sign_options.sign_time = datetime.datetime.now()
        sign_options.decryption_password = "docPassword"
        # Set a local system filename for the unsigned input document, and an output filename for its new digitally signed copy.
        input_file_name = MY_DIR + "Encrypted.docx"
        output_file_name = ARTIFACTS_DIR + "DigitalSignatureUtil.DecryptionPassword.docx"
        aw.digitalsignatures.DigitalSignatureUtil.sign(src_file_name=input_file_name, dst_file_name=output_file_name, cert_holder=certificate_holder, sign_options=sign_options)
        #ExEnd
        # Open encrypted document from a file.
        load_options = aw.loading.LoadOptions(password="docPassword")
        self.assertEqual(sign_options.decryption_password, load_options.password)
        # Check that encrypted document was successfully signed.
        signed_doc = aw.Document(file_name=output_file_name, load_options=load_options)
        signatures = signed_doc.digital_signatures
        self.assertEqual(1, signatures.count)
        self.assertTrue(signatures.is_valid)

    def test_sign_document_obfuscation_bug(self):
        ch = aw.digitalsignatures.CertificateHolder.create(file_name=MY_DIR + "morzal.pfx", password="aw")
        doc = aw.Document(file_name=MY_DIR + "Structured document tags.docx")
        output_file_name = ARTIFACTS_DIR + "DigitalSignatureUtil.SignDocumentObfuscationBug.doc"
        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.comments = "Comment"
        sign_options.sign_time = datetime.datetime.now()
        aw.digitalsignatures.DigitalSignatureUtil.sign(src_file_name=doc.original_file_name, dst_file_name=output_file_name, cert_holder=ch, sign_options=sign_options)

    def test_incorrect_decryption_password(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_no_arguments_for_sing(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_no_certificate_for_sign(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_xml_dsig(self):
        #ExStart:XmlDsig
        #ExFor:SignOptions.xml_dsig_level
        #ExFor:XmlDsigLevel
        #ExSummary:Shows how to sign document based on XML-DSig standard.
        certificate_holder = aw.digitalsignatures.CertificateHolder.create(file_name=MY_DIR + "morzal.pfx", password="aw")
        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.xml_dsig_level = aw.digitalsignatures.XmlDsigLevel.X_AD_ES_EPES
        input_file_name = MY_DIR + "Document.docx"
        output_file_name = ARTIFACTS_DIR + "DigitalSignatureUtil.XmlDsig.docx"
        aw.digitalsignatures.DigitalSignatureUtil.sign(src_file_name=input_file_name, dst_file_name=output_file_name, cert_holder=certificate_holder, sign_options=sign_options)
        #ExEnd:XmlDsig
