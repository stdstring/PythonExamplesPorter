# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.fonts
import aspose.words.loading
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, MY_DIR


class ExFontSettings(ApiExampleBase):
    def test_default_font_instance(self):
        #ExStart
        #ExFor:FontSettings.default_instance
        #ExSummary:Shows how to configure the default font settings instance.
        # Configure the default font settings instance to use the "Courier New" font
        # as a backup substitute when we attempt to use an unknown font.
        aw.fonts.FontSettings.default_instance.substitution_settings.default_font_substitution.default_font_name = "Courier New"
        self.assertTrue(aw.fonts.FontSettings.default_instance.substitution_settings.default_font_substitution.enabled)
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.font.name = "Non-existent font"
        builder.write("Hello world!")
        # This document does not have a FontSettings configuration. When we render the document,
        # the default FontSettings instance will resolve the missing font.
        # Aspose.Words will use "Courier New" to render text that uses the unknown font.
        self.assertIsNone(doc.font_settings)
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.DefaultFontInstance.pdf")
        #ExEnd

    def test_default_font_name(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: fontSources")

    def test_font_source_file(self):
        #ExStart
        #ExFor:FileFontSource
        #ExFor:FileFontSource.__init__(str)
        #ExFor:FileFontSource.__init__(str,int)
        #ExFor:FileFontSource.file_path
        #ExFor:FileFontSource.type
        #ExFor:FontSourceBase
        #ExFor:FontSourceBase.priority
        #ExFor:FontSourceBase.type
        #ExFor:FontSourceType
        #ExSummary:Shows how to use a font file in the local file system as a font source.
        file_font_source = aw.fonts.FileFontSource(file_path=MY_DIR + "Alte DIN 1451 Mittelschrift.ttf", priority=0)
        doc = aw.Document()
        doc.font_settings = aw.fonts.FontSettings()
        doc.font_settings.set_fonts_sources(sources=[file_font_source])
        self.assertEqual(MY_DIR + "Alte DIN 1451 Mittelschrift.ttf", file_font_source.file_path)
        self.assertEqual(aw.fonts.FontSourceType.FONT_FILE, file_font_source.type)
        self.assertEqual(0, file_font_source.priority)
        #ExEnd

    def test_font_source_folder(self):
        #ExStart
        #ExFor:FolderFontSource
        #ExFor:FolderFontSource.__init__(str,bool)
        #ExFor:FolderFontSource.__init__(str,bool,int)
        #ExFor:FolderFontSource.folder_path
        #ExFor:FolderFontSource.scan_subfolders
        #ExFor:FolderFontSource.type
        #ExSummary:Shows how to use a local system folder which contains fonts as a font source.
        # Create a font source from a folder that contains font files.
        folder_font_source = aw.fonts.FolderFontSource(folder_path=FONTS_DIR, scan_subfolders=False, priority=1)
        doc = aw.Document()
        doc.font_settings = aw.fonts.FontSettings()
        doc.font_settings.set_fonts_sources(sources=[folder_font_source])
        self.assertEqual(FONTS_DIR, folder_font_source.folder_path)
        self.assertEqual(False, folder_font_source.scan_subfolders)
        self.assertEqual(aw.fonts.FontSourceType.FONTS_FOLDER, folder_font_source.type)
        self.assertEqual(1, folder_font_source.priority)
        #ExEnd

    def test_set_fonts_folder(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: originalFontSources")

    def test_set_fonts_folders(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: originalFontSources")

    def test_add_font_source(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: originalFontSources")

    def test_set_specify_font_folder(self):
        font_settings = aw.fonts.FontSettings()
        font_settings.set_fonts_folder(FONTS_DIR, False)
        # Using load options
        load_options = aw.loading.LoadOptions()
        load_options.font_settings = font_settings
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx", load_options=load_options)
        folder_source = (doc.font_settings.get_fonts_sources()[0].as_folder_font_source())
        self.assertEqual(FONTS_DIR, folder_source.folder_path)
        self.assertFalse(folder_source.scan_subfolders)

    def test_table_substitution(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: fontSources")

    def test_set_specify_font_folders(self):
        font_settings = aw.fonts.FontSettings()
        font_settings.set_fonts_folders([FONTS_DIR, """C:\\Windows\\Fonts\\"""], True)
        # Using load options
        load_options = aw.loading.LoadOptions()
        load_options.font_settings = font_settings
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx", load_options=load_options)
        folder_source = (doc.font_settings.get_fonts_sources()[0].as_folder_font_source())
        self.assertEqual(FONTS_DIR, folder_source.folder_path)
        self.assertTrue(folder_source.scan_subfolders)
        folder_source = (doc.font_settings.get_fonts_sources()[1].as_folder_font_source())
        self.assertEqual("""C:\\Windows\\Fonts\\""", folder_source.folder_path)
        self.assertTrue(folder_source.scan_subfolders)

    def test_add_font_substitutes(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_font_source_memory(self):
        #ExStart
        #ExFor:MemoryFontSource
        #ExFor:MemoryFontSource.__init__(bytes)
        #ExFor:MemoryFontSource.__init__(bytes,int)
        #ExFor:MemoryFontSource.font_data
        #ExFor:MemoryFontSource.type
        #ExSummary:Shows how to use a byte array with data from a font file as a font source.
        font_bytes = system_helper.io.File.read_all_bytes(MY_DIR + "Alte DIN 1451 Mittelschrift.ttf")
        memory_font_source = aw.fonts.MemoryFontSource(font_data=font_bytes, priority=0)
        doc = aw.Document()
        doc.font_settings = aw.fonts.FontSettings()
        doc.font_settings.set_fonts_sources(sources=[memory_font_source])
        self.assertEqual(aw.fonts.FontSourceType.MEMORY_FONT, memory_font_source.type)
        self.assertEqual(0, memory_font_source.priority)
        #ExEnd

    def test_font_source_system(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: doc.FontSettings.GetFontsSources()")

    def test_load_font_fallback_settings_from_file(self):
        #ExStart
        #ExFor:FontFallbackSettings.load(str)
        #ExFor:FontFallbackSettings.save(str)
        #ExSummary:Shows how to load and save font fallback settings to/from an XML document in the local file system.
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        # Load an XML document that defines a set of font fallback settings.
        font_settings = aw.fonts.FontSettings()
        font_settings.fallback_settings.load(file_name=MY_DIR + "Font fallback rules.xml")
        doc.font_settings = font_settings
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.LoadFontFallbackSettingsFromFile.pdf")
        # Save our document's current font fallback settings as an XML document.
        doc.font_settings.fallback_settings.save(file_name=ARTIFACTS_DIR + "FallbackSettings.xml")
        #ExEnd

    def test_load_font_fallback_settings_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_load_noto_fonts_fallback_settings(self):
        #ExStart
        #ExFor:FontFallbackSettings.load_noto_fallback_settings
        #ExSummary:Shows how to add predefined font fallback settings for Google Noto fonts.
        font_settings = aw.fonts.FontSettings()
        # These are free fonts licensed under the SIL Open Font License.
        # We can download the fonts here:
        # https:#www.google.com/get/noto/#sans-lgc
        font_settings.set_fonts_folder(FONTS_DIR + "Noto", False)
        # Note that the predefined settings only use Sans-style Noto fonts with regular weight.
        # Some of the Noto fonts use advanced typography features.
        # Fonts featuring advanced typography may not be rendered correctly as Aspose.Words currently do not support them.
        font_settings.fallback_settings.load_noto_fallback_settings()
        font_settings.substitution_settings.font_info_substitution.enabled = False
        font_settings.substitution_settings.default_font_substitution.default_font_name = "Noto Sans"
        doc = aw.Document()
        doc.font_settings = font_settings
        #ExEnd

    def test_default_font_substitution_rule(self):
        #ExStart
        #ExFor:DefaultFontSubstitutionRule
        #ExFor:DefaultFontSubstitutionRule.default_font_name
        #ExFor:FontSubstitutionSettings.default_font_substitution
        #ExSummary:Shows how to set the default font substitution rule.
        doc = aw.Document()
        font_settings = aw.fonts.FontSettings()
        doc.font_settings = font_settings
        # Get the default substitution rule within FontSettings.
        # This rule will substitute all missing fonts with "Times New Roman".
        default_font_substitution_rule = font_settings.substitution_settings.default_font_substitution
        self.assertTrue(default_font_substitution_rule.enabled)
        self.assertEqual("Times New Roman", default_font_substitution_rule.default_font_name)
        # Set the default font substitute to "Courier New".
        default_font_substitution_rule.default_font_name = "Courier New"
        # Using a document builder, add some text in a font that we do not have to see the substitution take place,
        # and then render the result in a PDF.
        builder = aw.DocumentBuilder(doc=doc)
        builder.font.name = "Missing Font"
        builder.writeln("Line written in a missing font, which will be substituted with Courier New.")
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.DefaultFontSubstitutionRule.pdf")
        #ExEnd
        self.assertEqual("Courier New", default_font_substitution_rule.default_font_name)

    def test_font_config_substitution(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_fallback_settings(self):
        raise NotImplementedError("Unsupported ctor for type XmlDocument")

    def test_fallback_settings_custom(self):
        raise NotImplementedError("Unsupported target type System.Convert")

    def test_table_substitution_rule(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_table_substitution_rule_custom(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_resolve_fonts_before_loading_document(self):
        #ExStart
        #ExFor:LoadOptions.font_settings
        #ExSummary:Shows how to designate font substitutes during loading.
        load_options = aw.loading.LoadOptions()
        load_options.font_settings = aw.fonts.FontSettings()
        # Set a font substitution rule for a LoadOptions object.
        # If the document we are loading uses a font which we do not have,
        # this rule will substitute the unavailable font with one that does exist.
        # In this case, all uses of the "MissingFont" will convert to "Comic Sans MS".
        substitution_rule = load_options.font_settings.substitution_settings.table_substitution
        substitution_rule.add_substitutes("MissingFont", ["Comic Sans MS"])
        doc = aw.Document(file_name=MY_DIR + "Missing font.html", load_options=load_options)
        # At this point such text will still be in "MissingFont".
        # Font substitution will take place when we render the document.
        self.assertEqual("MissingFont", doc.first_section.body.first_paragraph.runs[0].font.name)
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.ResolveFontsBeforeLoadingDocument.pdf")
        #ExEnd
