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
import aspose.words.lists
import aspose.words.saving
import aspose.words.settings
import datetime
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
        builder = aw.DocumentBuilder(doc=doc)
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
        for restart_list_at_each_section in [False, True]:
            #ExStart
            #ExFor:List.is_restart_at_each_section
            #ExFor:OoxmlCompliance
            #ExFor:OoxmlSaveOptions.compliance
            #ExSummary:Shows how to configure a list to restart numbering at each section.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            doc.lists.add(list_template=aw.lists.ListTemplate.NUMBER_DEFAULT)
            list = doc.lists[0]
            list.is_restart_at_each_section = restart_list_at_each_section
            # The "IsRestartAtEachSection" property will only be applicable when
            # the document's OOXML compliance level is to a standard that is newer than "OoxmlComplianceCore.Ecma376".
            options = aw.saving.OoxmlSaveOptions()
            options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_TRANSITIONAL
            builder.list_format.list = list
            builder.writeln("List item 1")
            builder.writeln("List item 2")
            builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
            builder.writeln("List item 3")
            builder.writeln("List item 4")
            doc.save(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.RestartingDocumentList.docx", save_options=options)
            doc = aw.Document(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.RestartingDocumentList.docx")
            self.assertEqual(restart_list_at_each_section, doc.lists[0].is_restart_at_each_section)
            #ExEnd

    def test_last_saved_time(self):
        raise NotImplementedError("Unsupported target type System.TimeSpan")

    def test_keep_legacy_control_chars(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_document_compression(self):
        raise NotImplementedError("Unsupported target type System.Diagnostics.Stopwatch")

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
