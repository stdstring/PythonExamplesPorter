# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExHtmlSaveOptions(ApiExampleBase):
    def test_create_azw_3_toc(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Big document.docx")
        options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.AZW3)
        options.navigation_map_level = 2
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.CreateAZW3Toc.azw3", save_options = options)

    def test_create_mobi_toc(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Big document.docx")
        options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.MOBI)
        options.navigation_map_level = 5
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.CreateMobiToc.mobi", save_options = options)

    def test_export_roundtrip_information(self):
        doc = aspose.words.Document(file_name = MY_DIR + "TextBoxes.docx")
        save_options = aspose.words.saving.HtmlSaveOptions()
        save_options.export_roundtrip_information = True
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.RoundtripInformation.html", save_options = save_options)

    def test_roundtrip_information_defaul_value(self):
        save_options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.HTML)
        self.assertEqual(True, save_options.export_roundtrip_information)
        save_options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.MHTML)
        self.assertEqual(False, save_options.export_roundtrip_information)
        save_options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.EPUB)
        self.assertEqual(False, save_options.export_roundtrip_information)

    def test_convert_fonts_as_base64(self):
        doc = aspose.words.Document(file_name = MY_DIR + "TextBoxes.docx")
        save_options = aspose.words.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aspose.words.saving.CssStyleSheetType.EXTERNAL
        save_options.resource_folder = "Resources"
        save_options.export_font_resources = True
        save_options.export_fonts_as_base64 = True
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.ConvertFontsAsBase64.html", save_options = save_options)

    def test_resource_folder_priority(self):
        raise NotImplementedError("Unsupported target type System.IO.SearchOption")

    def test_resource_folder_low_priority(self):
        raise NotImplementedError("Unsupported target type System.IO.SearchOption")

    def test_svg_metafile_format(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_png_metafile_format(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_emf_or_wmf_metafile_format(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_css_class_names_prefix(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_css_class_names_not_valid_prefix(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_css_class_names_null_prefix(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Paragraphs.docx")
        save_options = aspose.words.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aspose.words.saving.CssStyleSheetType.EMBEDDED
        save_options.css_class_name_prefix = None
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.CssClassNamePrefix.html", save_options = save_options)

    def test_content_id_scheme(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        save_options = aspose.words.saving.HtmlSaveOptions(aspose.words.SaveFormat.MHTML)
        save_options.pretty_format = True
        save_options.export_cid_urls_for_mhtml_resources = True
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.ContentIdScheme.mhtml", save_options = save_options)

    def test_heading_levels(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_folder_alias(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        options = aspose.words.saving.HtmlSaveOptions()
        options.css_style_sheet_type = aspose.words.saving.CssStyleSheetType.EXTERNAL
        options.export_font_resources = True
        options.image_resolution = 72
        options.font_resources_subsetting_size_threshold = 0
        options.fonts_folder = ARTIFACTS_DIR + "Fonts"
        options.images_folder = ARTIFACTS_DIR + "Images"
        options.resource_folder = ARTIFACTS_DIR + "Resources"
        options.fonts_folder_alias = "http://example.com/fonts"
        options.images_folder_alias = "http://example.com/images"
        options.resource_folder_alias = "http://example.com/resources"
        options.export_original_url_for_linked_images = True
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.FolderAlias.html", save_options = options)

    def test_epub_headings(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_doc_2_epub_save_options(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_export_fonts_as_base64(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        options = aspose.words.saving.HtmlSaveOptions()
        options.export_fonts_as_base64 = True
        options.css_style_sheet_type = aspose.words.saving.CssStyleSheetType.EMBEDDED
        options.pretty_format = True
        doc.save(file_name = ARTIFACTS_DIR + "HtmlSaveOptions.ExportFontsAsBase64.html", save_options = options)

    def test_image_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Path")
