# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.drawing
import aspose.words.fonts
import aspose.words.loading
import aspose.words.settings
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, IMAGE_DIR, MY_DIR


class ExLoadOptions(ApiExampleBase):
    def test_convert_shape_to_office_math(self):
        for is_convert_shape_to_office_math in [True, False]:
            #ExStart
            #ExFor:LoadOptions.convert_shape_to_office_math
            #ExSummary:Shows how to convert EquationXML shapes to Office Math objects.
            load_options = aw.loading.LoadOptions()
            # Use this flag to specify whether to convert the shapes with EquationXML attributes
            # to Office Math objects and then load the document.
            load_options.convert_shape_to_office_math = is_convert_shape_to_office_math
            doc = aw.Document(file_name=MY_DIR + "Math shapes.docx", load_options=load_options)
            if is_convert_shape_to_office_math:
                self.assertEqual(16, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
                self.assertEqual(34, doc.get_child_nodes(aw.NodeType.OFFICE_MATH, True).count)
            else:
                self.assertEqual(24, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
                self.assertEqual(0, doc.get_child_nodes(aw.NodeType.OFFICE_MATH, True).count)
            #ExEnd

    def test_set_encoding(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_font_settings(self):
        #ExStart
        #ExFor:LoadOptions.font_settings
        #ExSummary:Shows how to apply font substitution settings while loading a document.
        # Create a FontSettings object that will substitute the "Times New Roman" font
        # with the font "Arvo" from our "MyFonts" folder.
        font_settings = aw.fonts.FontSettings()
        font_settings.set_fonts_folder(FONTS_DIR, False)
        font_settings.substitution_settings.table_substitution.add_substitutes("Times New Roman", ["Arvo"])
        # Set that FontSettings object as a property of a newly created LoadOptions object.
        load_options = aw.loading.LoadOptions()
        load_options.font_settings = font_settings
        # Load the document, then render it as a PDF with the font substitution.
        doc = aw.Document(file_name=MY_DIR + "Document.docx", load_options=load_options)
        doc.save(file_name=ARTIFACTS_DIR + "LoadOptions.FontSettings.pdf")
        #ExEnd

    def test_load_options_msw_version(self):
        #ExStart
        #ExFor:LoadOptions.msw_version
        #ExSummary:Shows how to emulate the loading procedure of a specific Microsoft Word version during document loading.
        # By default, Aspose.Words load documents according to Microsoft Word 2019 specification.
        load_options = aw.loading.LoadOptions()
        self.assertEqual(aw.settings.MsWordVersion.WORD2019, load_options.msw_version)
        # This document is missing the default paragraph formatting style.
        # This default style will be regenerated when we load the document either with Microsoft Word or Aspose.Words.
        load_options.msw_version = aw.settings.MsWordVersion.WORD2007
        doc = aw.Document(file_name=MY_DIR + "Document.docx", load_options=load_options)
        # The style's line spacing will have this value when loaded by Microsoft Word 2007 specification.
        self.assertAlmostEqual(12.95, doc.styles.default_paragraph_format.line_spacing, delta=0.01)
        #ExEnd

    def test_temp_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_add_editing_language(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_set_editing_language_as_default(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_convert_metafiles_to_png(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_open_chm_file(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_ignore_ole_data(self):
        #ExStart
        #ExFor:LoadOptions.ignore_ole_data
        #ExSummary:Shows how to ingore OLE data while loading.
        # Ignoring OLE data may reduce memory consumption and increase performance
        # without data lost in a case when destination format does not support OLE objects.
        load_options = aw.loading.LoadOptions()
        load_options.ignore_ole_data = True
        doc = aw.Document(file_name=MY_DIR + "OLE objects.docx", load_options=load_options)
        doc.save(file_name=ARTIFACTS_DIR + "LoadOptions.IgnoreOleData.docx")
        #ExEnd
