# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExFile(ApiExampleBase):
    def test_catch_file_corrupted_exception(self):
        raise NotImplementedError("Unsupported statement type: TryStatement")

    def test_file_format_to_string(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_detect_document_encryption(self):
        doc = aw.Document()
        save_options = aw.saving.OdtSaveOptions(save_format=aw.SaveFormat.ODT)
        save_options.password = "MyPassword"
        doc.save(file_name=ARTIFACTS_DIR + "File.DetectDocumentEncryption.odt", save_options=save_options)
        info = aw.FileFormatUtil.detect_file_format(file_name=ARTIFACTS_DIR + "File.DetectDocumentEncryption.odt")
        self.assertEqual(".odt", aw.FileFormatUtil.load_format_to_extension(info.load_format))
        self.assertTrue(info.is_encrypted)

    def test_detect_digital_signatures(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_save_to_detected_file_format(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_detect_file_format_save_format_to_load_format(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_extract_images(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")
