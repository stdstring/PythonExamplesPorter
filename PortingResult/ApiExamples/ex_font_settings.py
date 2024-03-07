# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.fonts
import aspose.words.loading
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, MY_DIR


class ExFontSettings(ApiExampleBase):
    def test_default_font_instance(self):
        aspose.words.fonts.FontSettings.default_instance.substitution_settings.default_font_substitution.default_font_name = "Courier New"
        self.assertTrue(aspose.words.fonts.FontSettings.default_instance.substitution_settings.default_font_substitution.enabled)
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.name = "Non-existent font"
        builder.write("Hello world!")
        self.assertIsNone(doc.font_settings)
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.DefaultFontInstance.pdf")

    def test_default_font_name(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: fontSources")

    def test_font_source_file(self):
        file_font_source = aspose.words.fonts.FileFontSource(file_path=MY_DIR + "Alte DIN 1451 Mittelschrift.ttf", priority=0)
        doc = aspose.words.Document()
        doc.font_settings = aspose.words.fonts.FontSettings()
        doc.font_settings.set_fonts_sources(sources=[file_font_source])
        self.assertEqual(MY_DIR + "Alte DIN 1451 Mittelschrift.ttf", file_font_source.file_path)
        self.assertEqual(aspose.words.fonts.FontSourceType.FONT_FILE, file_font_source.type)
        self.assertEqual(0, file_font_source.priority)

    def test_font_source_folder(self):
        folder_font_source = aspose.words.fonts.FolderFontSource(folder_path=FONTS_DIR, scan_subfolders=False, priority=1)
        doc = aspose.words.Document()
        doc.font_settings = aspose.words.fonts.FontSettings()
        doc.font_settings.set_fonts_sources(sources=[folder_font_source])
        self.assertEqual(FONTS_DIR, folder_font_source.folder_path)
        self.assertEqual(False, folder_font_source.scan_subfolders)
        self.assertEqual(aspose.words.fonts.FontSourceType.FONTS_FOLDER, folder_font_source.type)
        self.assertEqual(1, folder_font_source.priority)

    def test_add_font_source(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: originalFontSources")

    def test_set_specify_font_folder(self):
        font_settings = aspose.words.fonts.FontSettings()
        font_settings.set_fonts_folder(FONTS_DIR, False)
        load_options = aspose.words.loading.LoadOptions()
        load_options.font_settings = font_settings
        doc = aspose.words.Document(file_name=MY_DIR + "Rendering.docx", load_options=load_options)
        folder_source = (doc.font_settings.get_fonts_sources()[0].as_folder_font_source())
        self.assertEqual(FONTS_DIR, folder_source.folder_path)
        self.assertFalse(folder_source.scan_subfolders)

    def test_table_substitution(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: fontSources")

    def test_set_specify_font_folders(self):
        font_settings = aspose.words.fonts.FontSettings()
        font_settings.set_fonts_folders([FONTS_DIR, """C:\\Windows\\Fonts\\"""], True)
        load_options = aspose.words.loading.LoadOptions()
        load_options.font_settings = font_settings
        doc = aspose.words.Document(file_name=MY_DIR + "Rendering.docx", load_options=load_options)
        folder_source = (doc.font_settings.get_fonts_sources()[0].as_folder_font_source())
        self.assertEqual(FONTS_DIR, folder_source.folder_path)
        self.assertTrue(folder_source.scan_subfolders)
        folder_source = (doc.font_settings.get_fonts_sources()[1].as_folder_font_source())
        self.assertEqual("""C:\\Windows\\Fonts\\""", folder_source.folder_path)
        self.assertTrue(folder_source.scan_subfolders)

    def test_add_font_substitutes(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_font_source_memory(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_font_source_system(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Fonts.FontSourceBase[] for expression: doc.FontSettings.GetFontsSources()")

    def test_load_font_fallback_settings_from_file(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Rendering.docx")
        font_settings = aspose.words.fonts.FontSettings()
        font_settings.fallback_settings.load(file_name=MY_DIR + "Font fallback rules.xml")
        doc.font_settings = font_settings
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.LoadFontFallbackSettingsFromFile.pdf")
        doc.font_settings.fallback_settings.save(file_name=ARTIFACTS_DIR + "FallbackSettings.xml")

    def test_load_font_fallback_settings_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_load_noto_fonts_fallback_settings(self):
        font_settings = aspose.words.fonts.FontSettings()
        font_settings.set_fonts_folder(FONTS_DIR + "Noto", False)
        font_settings.fallback_settings.load_noto_fallback_settings()
        font_settings.substitution_settings.font_info_substitution.enabled = False
        font_settings.substitution_settings.default_font_substitution.default_font_name = "Noto Sans"
        doc = aspose.words.Document()
        doc.font_settings = font_settings

    def test_default_font_substitution_rule(self):
        doc = aspose.words.Document()
        font_settings = aspose.words.fonts.FontSettings()
        doc.font_settings = font_settings
        default_font_substitution_rule = font_settings.substitution_settings.default_font_substitution
        self.assertTrue(default_font_substitution_rule.enabled)
        self.assertEqual("Times New Roman", default_font_substitution_rule.default_font_name)
        default_font_substitution_rule.default_font_name = "Courier New"
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.name = "Missing Font"
        builder.writeln("Line written in a missing font, which will be substituted with Courier New.")
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.DefaultFontSubstitutionRule.pdf")
        self.assertEqual("Courier New", default_font_substitution_rule.default_font_name)

    def test_fallback_settings(self):
        raise NotImplementedError("Unsupported ctor for type XmlDocument")

    def test_fallback_settings_custom(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_table_substitution_rule(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_table_substitution_rule_custom(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_resolve_fonts_before_loading_document(self):
        load_options = aspose.words.loading.LoadOptions()
        load_options.font_settings = aspose.words.fonts.FontSettings()
        substitution_rule = load_options.font_settings.substitution_settings.table_substitution
        substitution_rule.add_substitutes("MissingFont", ["Comic Sans MS"])
        doc = aspose.words.Document(file_name=MY_DIR + "Missing font.html", load_options=load_options)
        self.assertEqual("MissingFont", doc.first_section.body.first_paragraph.runs[0].font.name)
        doc.save(file_name=ARTIFACTS_DIR + "FontSettings.ResolveFontsBeforeLoadingDocument.pdf")
