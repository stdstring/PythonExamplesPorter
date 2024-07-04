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
import aspose.words.saving
import aspose.words.settings
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExOoxmlSaveOptions(ApiExampleBase):
    def test_password(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_iso_29500_strict(self):
        #ExStart
        #ExFor:CompatibilityOptions
        #ExFor:CompatibilityOptions.optimize_for(MsWordVersion)
        #ExFor:OoxmlSaveOptions
        #ExFor:OoxmlSaveOptions.__init__
        #ExFor:OoxmlSaveOptions.save_format
        #ExFor:OoxmlCompliance
        #ExFor:OoxmlSaveOptions.compliance
        #ExFor:ShapeMarkupLanguage
        #ExSummary:Shows how to set an OOXML compliance specification for a saved document to adhere to.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # If we configure compatibility options to comply with Microsoft Word 2003,
        # inserting an image will define its shape using VML.
        doc.compatibility_options.optimize_for(aw.settings.MsWordVersion.WORD2003)
        builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
        self.assertEqual(aw.drawing.ShapeMarkupLanguage.VML, (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).markup_language)
        # The "ISO/IEC 29500:2008" OOXML standard does not support VML shapes.
        # If we set the "Compliance" property of the SaveOptions object to "OoxmlCompliance.Iso29500_2008_Strict",
        # any document we save while passing this object will have to follow that standard.
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        save_options.save_format = aw.SaveFormat.DOCX
        doc.save(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.Iso29500Strict.docx", save_options=save_options)
        # Our saved document defines the shape using DML to adhere to the "ISO/IEC 29500:2008" OOXML standard.
        doc = aw.Document(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.Iso29500Strict.docx")
        self.assertEqual(aw.drawing.ShapeMarkupLanguage.DML, (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).markup_language)
        #ExEnd

    def test_restarting_document_list(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_last_saved_time(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_keep_legacy_control_chars(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_document_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_check_file_signatures(self):
        raise NotImplementedError("Unsupported member target type - System.String[] for expression: fileSignatures")

    def test_export_generator_name(self):
        #ExStart
        #ExFor:SaveOptions.export_generator_name
        #ExSummary:Shows how to disable adding name and version of Aspose.Words into produced files.
        doc = aw.Document()
        # Use https:#docs.aspose.com/words/net/generator-or-producer-name-included-in-output-documents/ to know how to check the result.
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.export_generator_name = False
        doc.save(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.ExportGeneratorName.docx", save_options=save_options)
        #ExEnd

    def test_zip_64_mode_option(self):
        raise NotImplementedError("Unsupported ctor for type Random")

    def test_digital_signature(self):
        raise NotImplementedError("Forbidden object initializer")
