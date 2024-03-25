# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExDocSaveOptions(ApiExampleBase):
    def test_save_as_doc(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_temp_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_picture_bullets(self):
        doc = aw.Document(file_name=MY_DIR + "Image bullet points.docx")
        self.assertIsNotNone(doc.lists[0].list_levels[0].image_data)
        save_options = aw.saving.DocSaveOptions(aw.SaveFormat.DOC)
        save_options.save_picture_bullet = False
        doc.save(file_name=ARTIFACTS_DIR + "DocSaveOptions.PictureBullets.doc", save_options=save_options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocSaveOptions.PictureBullets.doc")
        self.assertIsNone(doc.lists[0].list_levels[0].image_data)

    def test_update_last_printed_property(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_update_created_time_property(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_always_compress_metafiles(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")
