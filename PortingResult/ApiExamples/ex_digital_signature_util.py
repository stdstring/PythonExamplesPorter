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
        raise NotImplementedError("Unsupported target type System.DateTime")

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
