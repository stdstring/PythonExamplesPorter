# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.loading
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExDigitalSignatureUtil(ApiExampleBase):
    def test_load(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_remove_signatures(self):
        aw.digitalsignatures.DigitalSignatureUtil.remove_all_signatures(src_file_name=MY_DIR + "Digitally signed.odt", dst_file_name=ARTIFACTS_DIR + "DigitalSignatureUtil.RemoveSignatures.odt")
        self.assertEqual(0, aw.digitalsignatures.DigitalSignatureUtil.load_signatures(file_name=ARTIFACTS_DIR + "DigitalSignatureUtil.RemoveSignatures.odt").count)

    def test_decryption_password(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_sign_document_obfuscation_bug(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_incorrect_decryption_password(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_no_arguments_for_sing(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_no_certificate_for_sign(self):
        raise NotImplementedError("Unsupported target type System.DateTime")
