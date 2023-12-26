# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.fonts
import aspose.words.loading
import aspose.words.settings
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, IMAGE_DIR, MY_DIR


class ExLoadOptions(ApiExampleBase):
    def test_set_encoding(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_font_settings(self):
        font_settings = aspose.words.fonts.FontSettings()
        font_settings.set_fonts_folder(FONTS_DIR, False)
        font_settings.substitution_settings.table_substitution.add_substitutes("Times New Roman", ["Arvo"])
        load_options = aspose.words.loading.LoadOptions()
        load_options.font_settings = font_settings
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx", load_options = load_options)
        doc.save(file_name = ARTIFACTS_DIR + "LoadOptions.FontSettings.pdf")

    def test_load_options_msw_version(self):
        load_options = aspose.words.loading.LoadOptions()
        self.assertEqual(aspose.words.settings.MsWordVersion.WORD2019, load_options.msw_version)
        load_options.msw_version = aspose.words.settings.MsWordVersion.WORD2007
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx", load_options = load_options)
        self.assertAlmostEqual(12.95, doc.styles.default_paragraph_format.line_spacing, delta=0.01)

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
        load_options = aspose.words.loading.LoadOptions()
        load_options.ignore_ole_data = True
        doc = aspose.words.Document(file_name = MY_DIR + "OLE objects.docx", load_options = load_options)
        doc.save(file_name = ARTIFACTS_DIR + "LoadOptions.IgnoreOleData.docx")
