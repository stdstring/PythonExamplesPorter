# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.fields
import aspose.words.loading
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExOdtSaveOptions(ApiExampleBase):
    def test_odt_11_schema(self):
        for export_to_odt_11_specs in [False, True]:
            #ExStart
            #ExFor:OdtSaveOptions
            #ExFor:OdtSaveOptions.__init__
            #ExFor:OdtSaveOptions.is_strict_schema11
            #ExFor:RevisionOptions.measurement_unit
            #ExFor:MeasurementUnits
            #ExSummary:Shows how to make a saved document conform to an older ODT schema.
            doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
            save_options = aw.saving.OdtSaveOptions()
            save_options.measure_unit = aw.saving.OdtSaveMeasureUnit.CENTIMETERS
            save_options.is_strict_schema11 = export_to_odt_11_specs
            doc.save(file_name=ARTIFACTS_DIR + "OdtSaveOptions.Odt11Schema.odt", save_options=save_options)
            #ExEnd
            doc = aw.Document(file_name=ARTIFACTS_DIR + "OdtSaveOptions.Odt11Schema.odt")
            self.assertEqual(aw.MeasurementUnits.CENTIMETERS, doc.layout_options.revision_options.measurement_unit)
            if export_to_odt_11_specs:
                self.assertEqual(2, doc.range.form_fields.count)
                self.assertEqual(aw.fields.FieldType.FIELD_FORM_TEXT_INPUT, doc.range.form_fields[0].type)
                self.assertEqual(aw.fields.FieldType.FIELD_FORM_CHECK_BOX, doc.range.form_fields[1].type)
            else:
                self.assertEqual(3, doc.range.form_fields.count)
                self.assertEqual(aw.fields.FieldType.FIELD_FORM_TEXT_INPUT, doc.range.form_fields[0].type)
                self.assertEqual(aw.fields.FieldType.FIELD_FORM_CHECK_BOX, doc.range.form_fields[1].type)
                self.assertEqual(aw.fields.FieldType.FIELD_FORM_DROP_DOWN, doc.range.form_fields[2].type)

    def test_measurement_units(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_encrypt(self):
        for save_format in [aw.SaveFormat.ODT, aw.SaveFormat.OTT]:
            #ExStart
            #ExFor:OdtSaveOptions.__init__(SaveFormat)
            #ExFor:OdtSaveOptions.password
            #ExFor:OdtSaveOptions.save_format
            #ExSummary:Shows how to encrypt a saved ODT/OTT document with a password, and then load it using Aspose.Words.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Hello world!")
            # Create a new OdtSaveOptions, and pass either "SaveFormat.Odt",
            # or "SaveFormat.Ott" as the format to save the document in.
            save_options = aw.saving.OdtSaveOptions(save_format=save_format)
            save_options.password = "@sposeEncrypted_1145"
            extension_string = aw.FileFormatUtil.save_format_to_extension(save_format)
            # If we open this document with an appropriate editor,
            # it will prompt us for the password we specified in the SaveOptions object.
            doc.save(file_name=ARTIFACTS_DIR + "OdtSaveOptions.Encrypt" + extension_string, save_options=save_options)
            doc_info = aw.FileFormatUtil.detect_file_format(file_name=ARTIFACTS_DIR + "OdtSaveOptions.Encrypt" + extension_string)
            self.assertTrue(doc_info.is_encrypted)
            # If we wish to open or edit this document again using Aspose.Words,
            # we will have to provide a LoadOptions object with the correct password to the loading constructor.
            doc = aw.Document(file_name=ARTIFACTS_DIR + "OdtSaveOptions.Encrypt" + extension_string, load_options=aw.loading.LoadOptions(password="@sposeEncrypted_1145"))
            self.assertEqual("Hello world!", doc.get_text().strip())
            #ExEnd
