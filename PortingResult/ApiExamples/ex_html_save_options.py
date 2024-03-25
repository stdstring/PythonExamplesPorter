# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExHtmlSaveOptions(ApiExampleBase):
    def test_export_page_margins_epub(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_text_box_as_svg_epub(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_create_azw_3_toc(self):
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        options = aw.saving.HtmlSaveOptions(aw.SaveFormat.AZW3)
        options.navigation_map_level = 2
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.CreateAZW3Toc.azw3", save_options=options)

    def test_create_mobi_toc(self):
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        options = aw.saving.HtmlSaveOptions(aw.SaveFormat.MOBI)
        options.navigation_map_level = 5
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.CreateMobiToc.mobi", save_options=options)

    def test_control_list_labels_export(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_url_for_linked_image(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_roundtrip_information(self):
        doc = aw.Document(file_name=MY_DIR + "TextBoxes.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.export_roundtrip_information = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.RoundtripInformation.html", save_options=save_options)

    def test_roundtrip_information_defaul_value(self):
        save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
        self.assertEqual(True, save_options.export_roundtrip_information)
        save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.MHTML)
        self.assertEqual(False, save_options.export_roundtrip_information)
        save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.EPUB)
        self.assertEqual(False, save_options.export_roundtrip_information)

    def test_convert_fonts_as_base64(self):
        doc = aw.Document(file_name=MY_DIR + "TextBoxes.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
        save_options.resource_folder = "Resources"
        save_options.export_font_resources = True
        save_options.export_fonts_as_base64 = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ConvertFontsAsBase64.html", save_options=save_options)

    def test_html_5_support(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_resource_folder_priority(self):
        raise NotImplementedError("Unsupported target type System.IO.SearchOption")

    def test_resource_folder_low_priority(self):
        raise NotImplementedError("Unsupported target type System.IO.SearchOption")

    def test_svg_metafile_format(self):
        builder = aw.DocumentBuilder()
        builder.write("Here is an SVG image: ")
        builder.insert_html(html="""<svg height='210' width='500'>
                    <polygon points='100,10 40,198 190,78 10,78 160,198' 
                        style='fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;' />
                  </svg> """)
        save_options = aw.saving.HtmlSaveOptions()
        save_options.metafile_format = aw.saving.HtmlMetafileFormat.PNG
        builder.document.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.SvgMetafileFormat.html", save_options=save_options)

    def test_png_metafile_format(self):
        builder = aw.DocumentBuilder()
        builder.write("Here is an Png image: ")
        builder.insert_html(html="""<svg height='210' width='500'>
                    <polygon points='100,10 40,198 190,78 10,78 160,198' 
                        style='fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;' />
                  </svg> """)
        save_options = aw.saving.HtmlSaveOptions()
        save_options.metafile_format = aw.saving.HtmlMetafileFormat.PNG
        builder.document.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.PngMetafileFormat.html", save_options=save_options)

    def test_emf_or_wmf_metafile_format(self):
        builder = aw.DocumentBuilder()
        builder.write("Here is an image as is: ")
        builder.insert_html(html="""<img src=""data:image/png;base64,
                    iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABGdBTUEAALGP
                    C/xhBQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9YGARc5KB0XV+IA
                    AAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAF1J
                    REFUGNO9zL0NglAAxPEfdLTs4BZM4DIO4C7OwQg2JoQ9LE1exdlYvBBeZ7jq
                    ch9//q1uH4TLzw4d6+ErXMMcXuHWxId3KOETnnXXV6MJpcq2MLaI97CER3N0
                    vr4MkhoXe0rZigAAAABJRU5ErkJggg=="" alt=""Red dot"" />""")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.metafile_format = aw.saving.HtmlMetafileFormat.EMF_OR_WMF
        builder.document.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.EmfOrWmfMetafileFormat.html", save_options=save_options)

    def test_css_class_names_prefix(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_css_class_names_not_valid_prefix(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_css_class_names_null_prefix(self):
        doc = aw.Document(file_name=MY_DIR + "Paragraphs.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aw.saving.CssStyleSheetType.EMBEDDED
        save_options.css_class_name_prefix = None
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.CssClassNamePrefix.html", save_options=save_options)

    def test_content_id_scheme(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.MHTML)
        save_options.pretty_format = True
        save_options.export_cid_urls_for_mhtml_resources = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ContentIdScheme.mhtml", save_options=save_options)

    def test_heading_levels(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 1")
        builder.writeln("Heading #1")
        builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 2")
        builder.writeln("Heading #2")
        builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 3")
        builder.writeln("Heading #3")
        builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 1")
        builder.writeln("Heading #4")
        builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 2")
        builder.writeln("Heading #5")
        builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 3")
        builder.writeln("Heading #6")
        options = aw.saving.HtmlSaveOptions()
        options.document_split_criteria = aw.saving.DocumentSplitCriteria.HEADING_PARAGRAPH
        options.document_split_heading_level = 2
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels.html", save_options=options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels.html")
        self.assertEqual("Heading #1", doc.get_text().strip())
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels-01.html")
        self.assertEqual("Heading #2\r" + "Heading #3", doc.get_text().strip())
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels-02.html")
        self.assertEqual("Heading #4", doc.get_text().strip())
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels-03.html")
        self.assertEqual("Heading #5\r" + "Heading #6", doc.get_text().strip())

    def test_negative_indent(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_folder_alias(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        options = aw.saving.HtmlSaveOptions()
        options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
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
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.FolderAlias.html", save_options=options)

    def test_html_versions(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_xhtml_transitional(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_epub_headings(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_doc_2_epub_save_options(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_drop_down_form_field(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_images_as_base64(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_fonts_as_base64(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        options = aw.saving.HtmlSaveOptions()
        options.export_fonts_as_base64 = True
        options.css_style_sheet_type = aw.saving.CssStyleSheetType.EMBEDDED
        options.pretty_format = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportFontsAsBase64.html", save_options=options)

    def test_export_language_information(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_list(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_relative_font_size(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_shape(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_round_trip_information(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_metafile_format(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_image_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Path")

    def test_pretty_format(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")
