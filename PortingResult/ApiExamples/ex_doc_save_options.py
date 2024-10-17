# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.saving
import datetime
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExDocSaveOptions(ApiExampleBase):
    def test_save_as_doc(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_temp_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_picture_bullets(self):
        #ExStart
        #ExFor:DocSaveOptions.save_picture_bullet
        #ExSummary:Shows how to omit PictureBullet data from the document when saving.
        doc = aw.Document(file_name=MY_DIR + "Image bullet points.docx")
        self.assertIsNotNone(doc.lists[0].list_levels[0].image_data) #ExSkip
        # Some word processors, such as Microsoft Word 97, are incompatible with PictureBullet data.
        # By setting a flag in the SaveOptions object,
        # we can convert all image bullet points to ordinary bullet points while saving.
        save_options = aw.saving.DocSaveOptions(aw.SaveFormat.DOC)
        save_options.save_picture_bullet = False
        doc.save(file_name=ARTIFACTS_DIR + "DocSaveOptions.PictureBullets.doc", save_options=save_options)
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocSaveOptions.PictureBullets.doc")
        self.assertIsNone(doc.lists[0].list_levels[0].image_data)

    def test_update_last_printed_property(self):
        for is_update_last_printed_property in [True, False]:
            #ExStart
            #ExFor:SaveOptions.update_last_printed_property
            #ExSummary:Shows how to update a document's "Last printed" property when saving.
            doc = aw.Document()
            doc.built_in_document_properties.last_printed = datetime.datetime(2019,12,20)
            # This flag determines whether the last printed date, which is a built-in property, is updated.
            # If so, then the date of the document's most recent save operation
            # with this SaveOptions object passed as a parameter is used as the print date.
            save_options = aw.saving.DocSaveOptions()
            save_options.update_last_printed_property = is_update_last_printed_property
            # In Microsoft Word 2003, this property can be found via File -> Properties -> Statistics -> Printed.
            # It can also be displayed in the document's body by using a PRINTDATE field.
            doc.save(file_name=ARTIFACTS_DIR + "DocSaveOptions.UpdateLastPrintedProperty.doc", save_options=save_options)
            # Open the saved document, then verify the value of the property.
            doc = aw.Document(file_name=ARTIFACTS_DIR + "DocSaveOptions.UpdateLastPrintedProperty.doc")
            self.assertNotEqual(is_update_last_printed_property, datetime.datetime(2019,12,20) == doc.built_in_document_properties.last_printed)
            #ExEnd

    def test_update_created_time_property(self):
        for is_update_created_time_property in [True, False]:
            #ExStart
            #ExFor:SaveOptions.update_created_time_property
            #ExSummary:Shows how to update a document's "CreatedTime" property when saving.
            doc = aw.Document()
            doc.built_in_document_properties.created_time = datetime.datetime(2019,12,20)
            # This flag determines whether the created time, which is a built-in property, is updated.
            # If so, then the date of the document's most recent save operation
            # with this SaveOptions object passed as a parameter is used as the created time.
            save_options = aw.saving.DocSaveOptions()
            save_options.update_created_time_property = is_update_created_time_property
            doc.save(file_name=ARTIFACTS_DIR + "DocSaveOptions.UpdateCreatedTimeProperty.docx", save_options=save_options)
            # Open the saved document, then verify the value of the property.
            doc = aw.Document(file_name=ARTIFACTS_DIR + "DocSaveOptions.UpdateCreatedTimeProperty.docx")
            self.assertNotEqual(is_update_created_time_property, datetime.datetime(2019,12,20) == doc.built_in_document_properties.created_time)
            #ExEnd

    def test_always_compress_metafiles(self):
        for compress_all_metafiles in [False, True]:
            #ExStart
            #ExFor:DocSaveOptions.always_compress_metafiles
            #ExSummary:Shows how to change metafiles compression in a document while saving.
            # Open a document that contains a Microsoft Equation 3.0 formula.
            doc = aw.Document(file_name=MY_DIR + "Microsoft equation object.docx")
            # When we save a document, smaller metafiles are not compressed for performance reasons.
            # We can set a flag in a SaveOptions object to compress every metafile when saving.
            # Some editors such as LibreOffice cannot read uncompressed metafiles.
            save_options = aw.saving.DocSaveOptions()
            save_options.always_compress_metafiles = compress_all_metafiles
            doc.save(file_name=ARTIFACTS_DIR + "DocSaveOptions.AlwaysCompressMetafiles.docx", save_options=save_options)
            #ExEnd
            tested_file_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "DocSaveOptions.AlwaysCompressMetafiles.docx").length()
            if compress_all_metafiles:
                self.assertTrue(tested_file_length < 14000)
            else:
                self.assertTrue(tested_file_length < 22000)
