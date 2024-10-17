# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.drawing
import aspose.words.fields
import aspose.words.lists
import aspose.words.loading
import aspose.words.saving
import aspose.words.tables
import os
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExHtmlSaveOptions(ApiExampleBase):
    def test_export_page_margins_epub(self):
        for save_format in [aw.SaveFormat.HTML,
                            aw.SaveFormat.MHTML,
                            aw.SaveFormat.EPUB,
                            aw.SaveFormat.AZW3,
                            aw.SaveFormat.MOBI]:
            doc = aw.Document(file_name=MY_DIR + "TextBoxes.docx")
            save_options = aw.saving.HtmlSaveOptions()
            save_options.save_format = save_format
            save_options.export_page_margins = True
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportPageMarginsEpub" + aw.FileFormatUtil.save_format_to_extension(save_format), save_options=save_options)

    def test_export_office_math_epub(self):
        for save_format, output_mode in [(aw.SaveFormat.HTML, aw.saving.HtmlOfficeMathOutputMode.IMAGE),
                                         (aw.SaveFormat.MHTML, aw.saving.HtmlOfficeMathOutputMode.MATH_ML),
                                         (aw.SaveFormat.EPUB, aw.saving.HtmlOfficeMathOutputMode.TEXT),
                                         (aw.SaveFormat.AZW3, aw.saving.HtmlOfficeMathOutputMode.TEXT),
                                         (aw.SaveFormat.MOBI, aw.saving.HtmlOfficeMathOutputMode.TEXT)]:
            doc = aw.Document(file_name=MY_DIR + "Office math.docx")
            save_options = aw.saving.HtmlSaveOptions()
            save_options.office_math_output_mode = output_mode
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportOfficeMathEpub" + aw.FileFormatUtil.save_format_to_extension(save_format), save_options=save_options)

    def test_export_text_box_as_svg_epub(self):
        raise NotImplementedError("Unsupported statement type: ReturnStatement")

    def test_create_azw_3_toc(self):
        #ExStart
        #ExFor:HtmlSaveOptions.navigation_map_level
        #ExSummary:Shows how to generate table of contents for Azw3 documents.
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        options = aw.saving.HtmlSaveOptions(aw.SaveFormat.AZW3)
        options.navigation_map_level = 2
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.CreateAZW3Toc.azw3", save_options=options)
        #ExEnd

    def test_create_mobi_toc(self):
        #ExStart
        #ExFor:HtmlSaveOptions.navigation_map_level
        #ExSummary:Shows how to generate table of contents for Mobi documents.
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        options = aw.saving.HtmlSaveOptions(aw.SaveFormat.MOBI)
        options.navigation_map_level = 5
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.CreateMobiToc.mobi", save_options=options)
        #ExEnd

    def test_control_list_labels_export(self):
        for how_export_list_labels in [aw.saving.ExportListLabels.AUTO,
                                       aw.saving.ExportListLabels.AS_INLINE_TEXT,
                                       aw.saving.ExportListLabels.BY_HTML_TAGS]:
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            bulleted_list = doc.lists.add(list_template=aw.lists.ListTemplate.BULLET_DEFAULT)
            builder.list_format.list = bulleted_list
            builder.paragraph_format.left_indent = 72
            builder.writeln("Bulleted list item 1.")
            builder.writeln("Bulleted list item 2.")
            builder.paragraph_format.clear_formatting()
            save_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
            save_options.export_list_labels = how_export_list_labels
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ControlListLabelsExport.html", save_options=save_options)

    def test_export_url_for_linked_image(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

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

    def test_external_resource_saving_config(self):
        raise NotImplementedError("Unsupported member target type - System.String[] for expression: imageFiles")

    def test_convert_fonts_as_base64(self):
        doc = aw.Document(file_name=MY_DIR + "TextBoxes.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
        save_options.resource_folder = "Resources"
        save_options.export_font_resources = True
        save_options.export_fonts_as_base64 = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ConvertFontsAsBase64.html", save_options=save_options)

    def test_html_5_support(self):
        for html_version in [aw.saving.HtmlVersion.HTML5, aw.saving.HtmlVersion.XHTML]:
            doc = aw.Document(file_name=MY_DIR + "Document.docx")
            save_options = aw.saving.HtmlSaveOptions()
            save_options.html_version = html_version
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.Html5Support.html", save_options=save_options)

    def test_export_fonts(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_resource_folder_priority(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
        save_options.export_font_resources = True
        save_options.resource_folder = ARTIFACTS_DIR + "Resources"
        save_options.resource_folder_alias = "http://example.com/resources"
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ResourceFolderPriority.html", save_options=save_options)
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Resources", "HtmlSaveOptions.ResourceFolderPriority.001.png", system_helper.io.SearchOption.All_DIRECTORIES))
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Resources", "HtmlSaveOptions.ResourceFolderPriority.002.png", system_helper.io.SearchOption.All_DIRECTORIES))
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Resources", "HtmlSaveOptions.ResourceFolderPriority.arial.ttf", system_helper.io.SearchOption.All_DIRECTORIES))
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Resources", "HtmlSaveOptions.ResourceFolderPriority.css", system_helper.io.SearchOption.All_DIRECTORIES))

    def test_resource_folder_low_priority(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
        save_options.export_font_resources = True
        save_options.fonts_folder = ARTIFACTS_DIR + "Fonts"
        save_options.images_folder = ARTIFACTS_DIR + "Images"
        save_options.resource_folder = ARTIFACTS_DIR + "Resources"
        save_options.resource_folder_alias = "http://example.com/resources"
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ResourceFolderLowPriority.html", save_options=save_options)
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Images", "HtmlSaveOptions.ResourceFolderLowPriority.001.png", system_helper.io.SearchOption.All_DIRECTORIES))
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Images", "HtmlSaveOptions.ResourceFolderLowPriority.002.png", system_helper.io.SearchOption.All_DIRECTORIES))
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Fonts", "HtmlSaveOptions.ResourceFolderLowPriority.arial.ttf", system_helper.io.SearchOption.All_DIRECTORIES))
        self.assertTrue(system_helper.io.Directory.get_files(ARTIFACTS_DIR + "Resources", "HtmlSaveOptions.ResourceFolderLowPriority.css", system_helper.io.SearchOption.All_DIRECTORIES))

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
        #ExStart
        #ExFor:HtmlSaveOptions.css_class_name_prefix
        #ExSummary:Shows how to save a document to HTML, and add a prefix to all of its CSS class names.
        doc = aw.Document(file_name=MY_DIR + "Paragraphs.docx")
        save_options = aw.saving.HtmlSaveOptions()
        save_options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
        save_options.css_class_name_prefix = "myprefix-"
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.CssClassNamePrefix.html", save_options=save_options)
        out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.CssClassNamePrefix.html")
        self.assertTrue(("<p class=\"myprefix-Header\">" in out_doc_contents))
        self.assertTrue(("<p class=\"myprefix-Footer\">" in out_doc_contents))
        out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.CssClassNamePrefix.css")
        self.assertTrue((".myprefix-Footer { margin-bottom:0pt; line-height:normal; font-family:Arial; font-size:11pt; -aw-style-name:footer }" in out_doc_contents))
        self.assertTrue((".myprefix-Header { margin-bottom:0pt; line-height:normal; font-family:Arial; font-size:11pt; -aw-style-name:header }" in out_doc_contents))
        #ExEnd

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

    def test_resolve_font_names(self):
        raise NotImplementedError("Unsupported initializer expression: ObjectInitializerExpression")

    def test_heading_levels(self):
        #ExStart
        #ExFor:HtmlSaveOptions.document_split_heading_level
        #ExSummary:Shows how to split an output HTML document by headings into several parts.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Every paragraph that we format using a "Heading" style can serve as a heading.
        # Each heading may also have a heading level, determined by the number of its heading style.
        # The headings below are of levels 1-3.
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
        # Create a HtmlSaveOptions object and set the split criteria to "HeadingParagraph".
        # These criteria will split the document at paragraphs with "Heading" styles into several smaller documents,
        # and save each document in a separate HTML file in the local file system.
        # We will also set the maximum heading level, which splits the document to 2.
        # Saving the document will split it at headings of levels 1 and 2, but not at 3 to 9.
        options = aw.saving.HtmlSaveOptions()
        options.document_split_criteria = aw.saving.DocumentSplitCriteria.HEADING_PARAGRAPH
        options.document_split_heading_level = 2
        # Our document has four headings of levels 1 - 2. One of those headings will not be
        # a split point since it is at the beginning of the document.
        # The saving operation will split our document at three places, into four smaller documents.
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels.html", save_options=options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels.html")
        self.assertEqual("Heading #1", doc.get_text().strip())
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels-01.html")
        self.assertEqual("Heading #2\r" + "Heading #3", doc.get_text().strip())
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels-02.html")
        self.assertEqual("Heading #4", doc.get_text().strip())
        doc = aw.Document(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HeadingLevels-03.html")
        self.assertEqual("Heading #5\r" + "Heading #6", doc.get_text().strip())
        #ExEnd

    def test_negative_indent(self):
        for allow_negative_indent in [False, True]:
            #ExStart
            #ExFor:HtmlElementSizeOutputMode
            #ExFor:HtmlSaveOptions.allow_negative_indent
            #ExFor:HtmlSaveOptions.table_width_output_mode
            #ExSummary:Shows how to preserve negative indents in the output .html.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Insert a table with a negative indent, which will push it to the left past the left page boundary.
            table = builder.start_table()
            builder.insert_cell()
            builder.write("Row 1, Cell 1")
            builder.insert_cell()
            builder.write("Row 1, Cell 2")
            builder.end_table()
            table.left_indent = -36
            table.preferred_width = aw.tables.PreferredWidth.from_points(144)
            builder.insert_break(aw.BreakType.PARAGRAPH_BREAK)
            # Insert a table with a positive indent, which will push the table to the right.
            table = builder.start_table()
            builder.insert_cell()
            builder.write("Row 1, Cell 1")
            builder.insert_cell()
            builder.write("Row 1, Cell 2")
            builder.end_table()
            table.left_indent = 36
            table.preferred_width = aw.tables.PreferredWidth.from_points(144)
            # When we save a document to HTML, Aspose.Words will only preserve negative indents
            # such as the one we have applied to the first table if we set the "AllowNegativeIndent" flag
            # in a SaveOptions object that we will pass to "true".
            options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
            options.allow_negative_indent = allow_negative_indent
            options.table_width_output_mode = aw.saving.HtmlElementSizeOutputMode.RELATIVE_ONLY
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.NegativeIndent.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.NegativeIndent.html")
            if allow_negative_indent:
                self.assertTrue(("<table cellspacing=\"0\" cellpadding=\"0\" style=\"margin-left:-41.65pt; border:0.75pt solid #000000; -aw-border:0.5pt single; -aw-border-insideh:0.5pt single #000000; -aw-border-insidev:0.5pt single #000000; border-collapse:collapse\">" in out_doc_contents))
                self.assertTrue(("<table cellspacing=\"0\" cellpadding=\"0\" style=\"margin-left:30.35pt; border:0.75pt solid #000000; -aw-border:0.5pt single; -aw-border-insideh:0.5pt single #000000; -aw-border-insidev:0.5pt single #000000; border-collapse:collapse\">" in out_doc_contents))
            else:
                self.assertTrue(("<table cellspacing=\"0\" cellpadding=\"0\" style=\"border:0.75pt solid #000000; -aw-border:0.5pt single; -aw-border-insideh:0.5pt single #000000; -aw-border-insidev:0.5pt single #000000; border-collapse:collapse\">" in out_doc_contents))
                self.assertTrue(("<table cellspacing=\"0\" cellpadding=\"0\" style=\"margin-left:30.35pt; border:0.75pt solid #000000; -aw-border:0.5pt single; -aw-border-insideh:0.5pt single #000000; -aw-border-insidev:0.5pt single #000000; border-collapse:collapse\">" in out_doc_contents))
            #ExEnd

    def test_folder_alias(self):
        #ExStart
        #ExFor:HtmlSaveOptions.export_original_url_for_linked_images
        #ExFor:HtmlSaveOptions.fonts_folder
        #ExFor:HtmlSaveOptions.fonts_folder_alias
        #ExFor:HtmlSaveOptions.image_resolution
        #ExFor:HtmlSaveOptions.images_folder_alias
        #ExFor:HtmlSaveOptions.resource_folder
        #ExFor:HtmlSaveOptions.resource_folder_alias
        #ExSummary:Shows how to set folders and folder aliases for externally saved resources that Aspose.Words will create when saving a document to HTML.
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
        #ExEnd

    def test_html_versions(self):
        for html_version in [aw.saving.HtmlVersion.HTML5, aw.saving.HtmlVersion.XHTML]:
            #ExStart
            #ExFor:HtmlSaveOptions.__init__(SaveFormat)
            #ExFor:HtmlSaveOptions.html_version
            #ExFor:HtmlVersion
            #ExSummary:Shows how to save a document to a specific version of HTML.
            doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
            options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
            options.html_version = html_version
            options.pretty_format = True
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.HtmlVersions.html", save_options=options)
            # Our HTML documents will have minor differences to be compatible with different HTML versions.
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.HtmlVersions.html")
            switch_condition = html_version
            if switch_condition == aw.saving.HtmlVersion.HTML5:
                self.assertTrue(("<a id=\"_Toc76372689\"></a>" in out_doc_contents))
                self.assertTrue(("<a id=\"_Toc76372689\"></a>" in out_doc_contents))
                self.assertTrue(("<table style=\"padding:0pt; -aw-border-insideh:0.5pt single #000000; -aw-border-insidev:0.5pt single #000000; border-collapse:collapse\">" in out_doc_contents))
            elif switch_condition == aw.saving.HtmlVersion.XHTML:
                self.assertTrue(("<a name=\"_Toc76372689\"></a>" in out_doc_contents))
                self.assertTrue(("<ul type=\"disc\" style=\"margin:0pt; padding-left:0pt\">" in out_doc_contents))
                self.assertTrue(("<table cellspacing=\"0\" cellpadding=\"0\" style=\"-aw-border-insideh:0.5pt single #000000; -aw-border-insidev:0.5pt single #000000; border-collapse:collapse\"" in out_doc_contents))
            #ExEnd

    def test_export_xhtml_transitional(self):
        for show_doctype_declaration in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_xhtml_transitional
            #ExFor:HtmlSaveOptions.html_version
            #ExFor:HtmlVersion
            #ExSummary:Shows how to display a DOCTYPE heading when converting documents to the Xhtml 1.0 transitional standard.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Hello world!")
            options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
            options.html_version = aw.saving.HtmlVersion.XHTML
            options.export_xhtml_transitional = show_doctype_declaration
            options.pretty_format = True
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportXhtmlTransitional.html", save_options=options)
            # Our document will only contain a DOCTYPE declaration heading if we have set the "ExportXhtmlTransitional" flag to "true".
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.ExportXhtmlTransitional.html")
            if show_doctype_declaration:
                self.assertTrue(("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n" + "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\r\n" + "<html xmlns=\"http://www.w3.org/1999/xhtml\">" in out_doc_contents))
            else:
                self.assertTrue(("<html>" in out_doc_contents))
            #ExEnd

    def test_epub_headings(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_doc_2_epub_save_options(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_content_id_urls(self):
        for export_cid_urls_for_mhtml_resources in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_cid_urls_for_mhtml_resources
            #ExSummary:Shows how to enable content IDs for output MHTML documents.
            doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
            # Setting this flag will replace "Content-Location" tags
            # with "Content-ID" tags for each resource from the input document.
            options = aw.saving.HtmlSaveOptions(aw.SaveFormat.MHTML)
            options.export_cid_urls_for_mhtml_resources = export_cid_urls_for_mhtml_resources
            options.css_style_sheet_type = aw.saving.CssStyleSheetType.EXTERNAL
            options.export_font_resources = True
            options.pretty_format = True
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ContentIdUrls.mht", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.ContentIdUrls.mht")
            if export_cid_urls_for_mhtml_resources:
                self.assertTrue(("Content-ID: <document.html>" in out_doc_contents))
                self.assertTrue(("<link href=3D\"cid:styles.css\" type=3D\"text/css\" rel=3D\"stylesheet\" />" in out_doc_contents))
                self.assertTrue(("@font-face { font-family:'Arial Black'; font-weight:bold; src:url('cid:arib=\r\nlk.ttf') }" in out_doc_contents))
                self.assertTrue(("<img src=3D\"cid:image.003.jpeg\" width=3D\"350\" height=3D\"180\" alt=3D\"\" />" in out_doc_contents))
            else:
                self.assertTrue(("Content-Location: document.html" in out_doc_contents))
                self.assertTrue(("<link href=3D\"styles.css\" type=3D\"text/css\" rel=3D\"stylesheet\" />" in out_doc_contents))
                self.assertTrue(("@font-face { font-family:'Arial Black'; font-weight:bold; src:url('ariblk.t=\r\ntf') }" in out_doc_contents))
                self.assertTrue(("<img src=3D\"image.003.jpeg\" width=3D\"350\" height=3D\"180\" alt=3D\"\" />" in out_doc_contents))
            #ExEnd

    def test_drop_down_form_field(self):
        for export_drop_down_form_field_as_text in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_drop_down_form_field_as_text
            #ExSummary:Shows how to get drop-down combo box form fields to blend in with paragraph text when saving to html.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Use a document builder to insert a combo box with the value "Two" selected.
            builder.insert_combo_box("MyComboBox", ["One", "Two", "Three"], 1)
            # The "ExportDropDownFormFieldAsText" flag of this SaveOptions object allows us to
            # control how saving the document to HTML treats drop-down combo boxes.
            # Setting it to "true" will convert each combo box into simple text
            # that displays the combo box's currently selected value, effectively freezing it.
            # Setting it to "false" will preserve the functionality of the combo box using <select> and <option> tags.
            options = aw.saving.HtmlSaveOptions()
            options.export_drop_down_form_field_as_text = export_drop_down_form_field_as_text
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.DropDownFormField.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.DropDownFormField.html")
            if export_drop_down_form_field_as_text:
                self.assertTrue(("<span>Two</span>" in out_doc_contents))
            else:
                self.assertTrue(("<select name=\"MyComboBox\">" + "<option>One</option>" + "<option selected=\"selected\">Two</option>" + "<option>Three</option>" + "</select>" in out_doc_contents))
            #ExEnd

    def test_export_images_as_base64(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_export_fonts_as_base64(self):
        #ExStart
        #ExFor:HtmlSaveOptions.export_fonts_as_base64
        #ExFor:HtmlSaveOptions.export_images_as_base64
        #ExSummary:Shows how to embed fonts inside a saved HTML document.
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        options = aw.saving.HtmlSaveOptions()
        options.export_fonts_as_base64 = True
        options.css_style_sheet_type = aw.saving.CssStyleSheetType.EMBEDDED
        options.pretty_format = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportFontsAsBase64.html", save_options=options)
        #ExEnd

    def test_export_language_information(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_list(self):
        for export_list_labels in [aw.saving.ExportListLabels.AS_INLINE_TEXT,
                                   aw.saving.ExportListLabels.AUTO,
                                   aw.saving.ExportListLabels.BY_HTML_TAGS]:
            #ExStart
            #ExFor:ExportListLabels
            #ExFor:HtmlSaveOptions.export_list_labels
            #ExSummary:Shows how to configure list exporting to HTML.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            list = doc.lists.add(list_template=aw.lists.ListTemplate.NUMBER_DEFAULT)
            builder.list_format.list = list
            builder.writeln("Default numbered list item 1.")
            builder.writeln("Default numbered list item 2.")
            builder.list_format.list_indent()
            builder.writeln("Default numbered list item 3.")
            builder.list_format.remove_numbers()
            list = doc.lists.add(list_template=aw.lists.ListTemplate.OUTLINE_HEADINGS_LEGAL)
            builder.list_format.list = list
            builder.writeln("Outline legal heading list item 1.")
            builder.writeln("Outline legal heading list item 2.")
            builder.list_format.list_indent()
            builder.writeln("Outline legal heading list item 3.")
            builder.list_format.list_indent()
            builder.writeln("Outline legal heading list item 4.")
            builder.list_format.list_indent()
            builder.writeln("Outline legal heading list item 5.")
            builder.list_format.remove_numbers()
            # When saving the document to HTML, we can pass a SaveOptions object
            # to decide which HTML elements the document will use to represent lists.
            # Setting the "ExportListLabels" property to "ExportListLabels.AsInlineText"
            # will create lists by formatting spans.
            # Setting the "ExportListLabels" property to "ExportListLabels.Auto" will use the <p> tag
            # to build lists in cases when using the <ol> and <li> tags may cause loss of formatting.
            # Setting the "ExportListLabels" property to "ExportListLabels.ByHtmlTags"
            # will use <ol> and <li> tags to build all lists.
            options = aw.saving.HtmlSaveOptions()
            options.export_list_labels = export_list_labels
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.List.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.List.html")
            switch_condition = export_list_labels
            if switch_condition == aw.saving.ExportListLabels.AS_INLINE_TEXT:
                self.assertTrue(("<p style=\"margin-top:0pt; margin-left:72pt; margin-bottom:0pt; text-indent:-18pt; -aw-import:list-item; -aw-list-level-number:1; -aw-list-number-format:'%1.'; -aw-list-number-styles:'lowerLetter'; -aw-list-number-values:'1'; -aw-list-padding-sml:9.67pt\">" + "<span style=\"-aw-import:ignore\">" + "<span>a.</span>" + "<span style=\"width:9.67pt; font:7pt 'Times New Roman'; display:inline-block; -aw-import:spaces\">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0; </span>" + "</span>" + "<span>Default numbered list item 3.</span>" + "</p>" in out_doc_contents))
                self.assertTrue(("<p style=\"margin-top:0pt; margin-left:43.2pt; margin-bottom:0pt; text-indent:-43.2pt; -aw-import:list-item; -aw-list-level-number:3; -aw-list-number-format:'%0.%1.%2.%3'; -aw-list-number-styles:'decimal decimal decimal decimal'; -aw-list-number-values:'2 1 1 1'; -aw-list-padding-sml:10.2pt\">" + "<span style=\"-aw-import:ignore\">" + "<span>2.1.1.1</span>" + "<span style=\"width:10.2pt; font:7pt 'Times New Roman'; display:inline-block; -aw-import:spaces\">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0; </span>" + "</span>" + "<span>Outline legal heading list item 5.</span>" + "</p>" in out_doc_contents))
            elif switch_condition == aw.saving.ExportListLabels.AUTO:
                self.assertTrue(("<ol type=\"a\" style=\"margin-right:0pt; margin-left:0pt; padding-left:0pt\">" + "<li style=\"margin-left:31.33pt; padding-left:4.67pt\">" + "<span>Default numbered list item 3.</span>" + "</li>" + "</ol>" in out_doc_contents))
            elif switch_condition == aw.saving.ExportListLabels.BY_HTML_TAGS:
                self.assertTrue(("<ol type=\"a\" style=\"margin-right:0pt; margin-left:0pt; padding-left:0pt\">" + "<li style=\"margin-left:31.33pt; padding-left:4.67pt\">" + "<span>Default numbered list item 3.</span>" + "</li>" + "</ol>" in out_doc_contents))
            #ExEnd

    def test_export_page_margins(self):
        for export_page_margins in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_page_margins
            #ExSummary:Shows how to show out-of-bounds objects in output HTML documents.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Use a builder to insert a shape with no wrapping.
            shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.CUBE, width=200, height=200)
            shape.relative_horizontal_position = aw.drawing.RelativeHorizontalPosition.PAGE
            shape.relative_vertical_position = aw.drawing.RelativeVerticalPosition.PAGE
            shape.wrap_type = aw.drawing.WrapType.NONE
            # Negative shape position values may place the shape outside of page boundaries.
            # If we export this to HTML, the shape will appear truncated.
            shape.left = -150
            # When saving the document to HTML, we can pass a SaveOptions object
            # to decide whether to adjust the page to display out-of-bounds objects fully.
            # If we set the "ExportPageMargins" flag to "true", the shape will be fully visible in the output HTML.
            # If we set the "ExportPageMargins" flag to "false",
            # our document will display the shape truncated as we would see it in Microsoft Word.
            options = aw.saving.HtmlSaveOptions()
            options.export_page_margins = export_page_margins
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportPageMargins.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.ExportPageMargins.html")
            if export_page_margins:
                self.assertTrue(("<style type=\"text/css\">div.Section_1 { margin:70.85pt }</style>" in out_doc_contents))
                self.assertTrue(("<div class=\"Section_1\"><p style=\"margin-top:0pt; margin-left:150pt; margin-bottom:0pt\">" in out_doc_contents))
            else:
                self.assertFalse(("style type=\"text/css\">" in out_doc_contents))
                self.assertTrue(("<div><p style=\"margin-top:0pt; margin-left:220.85pt; margin-bottom:0pt\">" in out_doc_contents))
            #ExEnd

    def test_export_page_setup(self):
        for export_page_setup in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_page_setup
            #ExSummary:Shows how decide whether to preserve section structure/page setup information when saving to HTML.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.write("Section 1")
            builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
            builder.write("Section 2")
            page_setup = doc.sections[0].page_setup
            page_setup.top_margin = 36
            page_setup.bottom_margin = 36
            page_setup.paper_size = aw.PaperSize.A5
            # When saving the document to HTML, we can pass a SaveOptions object
            # to decide whether to preserve or discard page setup settings.
            # If we set the "ExportPageSetup" flag to "true", the output HTML document will contain our page setup configuration.
            # If we set the "ExportPageSetup" flag to "false", the save operation will discard our page setup settings
            # for the first section, and both sections will look identical.
            options = aw.saving.HtmlSaveOptions()
            options.export_page_setup = export_page_setup
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportPageSetup.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.ExportPageSetup.html")
            if export_page_setup:
                self.assertTrue(("<style type=\"text/css\">" + "@page Section_1 { size:419.55pt 595.3pt; margin:36pt 70.85pt; -aw-footer-distance:35.4pt; -aw-header-distance:35.4pt }" + "@page Section_2 { size:612pt 792pt; margin:70.85pt; -aw-footer-distance:35.4pt; -aw-header-distance:35.4pt }" + "div.Section_1 { page:Section_1 }div.Section_2 { page:Section_2 }" + "</style>" in out_doc_contents))
                self.assertTrue(("<div class=\"Section_1\">" + "<p style=\"margin-top:0pt; margin-bottom:0pt\">" + "<span>Section 1</span>" + "</p>" + "</div>" in out_doc_contents))
            else:
                self.assertFalse(("style type=\"text/css\">" in out_doc_contents))
                self.assertTrue(("<div>" + "<p style=\"margin-top:0pt; margin-bottom:0pt\">" + "<span>Section 1</span>" + "</p>" + "</div>" in out_doc_contents))
            #ExEnd

    def test_relative_font_size(self):
        for export_relative_font_size in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_relative_font_size
            #ExSummary:Shows how to use relative font sizes when saving to .html.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Default font size, ")
            builder.font.size = 24
            builder.writeln("2x default font size,")
            builder.font.size = 96
            builder.write("8x default font size")
            # When we save the document to HTML, we can pass a SaveOptions object
            # to determine whether to use relative or absolute font sizes.
            # Set the "ExportRelativeFontSize" flag to "true" to declare font sizes
            # using the "em" measurement unit, which is a factor that multiplies the current font size.
            # Set the "ExportRelativeFontSize" flag to "false" to declare font sizes
            # using the "pt" measurement unit, which is the font's absolute size in points.
            options = aw.saving.HtmlSaveOptions()
            options.export_relative_font_size = export_relative_font_size
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.RelativeFontSize.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.RelativeFontSize.html")
            if export_relative_font_size:
                self.assertTrue(("<body style=\"font-family:'Times New Roman'\">" + "<div>" + "<p style=\"margin-top:0pt; margin-bottom:0pt\">" + "<span>Default font size, </span>" + "</p>" + "<p style=\"margin-top:0pt; margin-bottom:0pt; font-size:2em\">" + "<span>2x default font size,</span>" + "</p>" + "<p style=\"margin-top:0pt; margin-bottom:0pt; font-size:8em\">" + "<span>8x default font size</span>" + "</p>" + "</div>" + "</body>" in out_doc_contents))
            else:
                self.assertTrue(("<body style=\"font-family:'Times New Roman'; font-size:12pt\">" + "<div>" + "<p style=\"margin-top:0pt; margin-bottom:0pt\">" + "<span>Default font size, </span>" + "</p>" + "<p style=\"margin-top:0pt; margin-bottom:0pt; font-size:24pt\">" + "<span>2x default font size,</span>" + "</p>" + "<p style=\"margin-top:0pt; margin-bottom:0pt; font-size:96pt\">" + "<span>8x default font size</span>" + "</p>" + "</div>" + "</body>" in out_doc_contents))
            #ExEnd

    def test_export_shape(self):
        for export_shapes_as_svg in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_shapes_as_svg
            #ExSummary:Shows how to export shape as scalable vector graphics.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            text_box = builder.insert_shape(shape_type=aw.drawing.ShapeType.TEXT_BOX, width=100, height=60)
            builder.move_to(text_box.first_paragraph)
            builder.write("My text box")
            # When we save the document to HTML, we can pass a SaveOptions object
            # to determine how the saving operation will export text box shapes.
            # If we set the "ExportTextBoxAsSvg" flag to "true",
            # the save operation will convert shapes with text into SVG objects.
            # If we set the "ExportTextBoxAsSvg" flag to "false",
            # the save operation will convert shapes with text into images.
            options = aw.saving.HtmlSaveOptions()
            options.export_shapes_as_svg = export_shapes_as_svg
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportTextBox.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.ExportTextBox.html")
            if export_shapes_as_svg:
                self.assertTrue(("<span style=\"-aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline\">" + "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" width=\"133\" height=\"80\">" in out_doc_contents))
            else:
                self.assertTrue(("<p style=\"margin-top:0pt; margin-bottom:0pt\">" + "<img src=\"HtmlSaveOptions.ExportTextBox.001.png\" width=\"136\" height=\"83\" alt=\"\" " + "style=\"-aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline\" />" + "</p>" in out_doc_contents))
            #ExEnd

    def test_round_trip_information(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_export_toc_page_numbers(self):
        for export_toc_page_numbers in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.export_toc_page_numbers
            #ExSummary:Shows how to display page numbers when saving a document with a table of contents to .html.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Insert a table of contents, and then populate the document with paragraphs formatted using a "Heading"
            # style that the table of contents will pick up as entries. Each entry will display the heading paragraph on the left,
            # and the page number that contains the heading on the right.
            field_toc = builder.insert_field(field_type=aw.fields.FieldType.FIELD_TOC, update_field=True).as_field_toc()
            builder.paragraph_format.style = builder.document.styles.get_by_name("Heading 1")
            builder.insert_break(aw.BreakType.PAGE_BREAK)
            builder.writeln("Entry 1")
            builder.writeln("Entry 2")
            builder.insert_break(aw.BreakType.PAGE_BREAK)
            builder.writeln("Entry 3")
            builder.insert_break(aw.BreakType.PAGE_BREAK)
            builder.writeln("Entry 4")
            field_toc.update_page_numbers()
            doc.update_fields()
            # HTML documents do not have pages. If we save this document to HTML,
            # the page numbers that our TOC displays will have no meaning.
            # When we save the document to HTML, we can pass a SaveOptions object to omit these page numbers from the TOC.
            # If we set the "ExportTocPageNumbers" flag to "true",
            # each TOC entry will display the heading, separator, and page number, preserving its appearance in Microsoft Word.
            # If we set the "ExportTocPageNumbers" flag to "false",
            # the save operation will omit both the separator and page number and leave the heading for each entry intact.
            options = aw.saving.HtmlSaveOptions()
            options.export_toc_page_numbers = export_toc_page_numbers
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ExportTocPageNumbers.html", save_options=options)
            out_doc_contents = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.ExportTocPageNumbers.html")
            if export_toc_page_numbers:
                self.assertTrue(("<span>Entry 1</span>" + "<span style=\"width:428.14pt; font-family:'Lucida Console'; font-size:10pt; display:inline-block; -aw-font-family:'Times New Roman'; " + "-aw-tabstop-align:right; -aw-tabstop-leader:dots; -aw-tabstop-pos:469.8pt\">.......................................................................</span>" + "<span>2</span>" + "</p>" in out_doc_contents))
            else:
                self.assertTrue(("<p style=\"margin-top:0pt; margin-bottom:0pt\">" + "<span>Entry 2</span>" + "</p>" in out_doc_contents))
            #ExEnd

    def test_font_subsetting(self):
        raise NotImplementedError("Unsupported target type System.Int32")

    def test_metafile_format(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_office_math_output_mode(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_scale_image_to_shape_size(self):
        for scale_image_to_shape_size in [False, True]:
            #ExStart
            #ExFor:HtmlSaveOptions.scale_image_to_shape_size
            #ExSummary:Shows how to disable the scaling of images to their parent shape dimensions when saving to .html.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Insert a shape which contains an image, and then make that shape considerably smaller than the image.
            image_shape = builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
            image_shape.width = 50
            image_shape.height = 50
            # Saving a document that contains shapes with images to HTML will create an image file in the local file system
            # for each such shape. The output HTML document will use <image> tags to link to and display these images.
            # When we save the document to HTML, we can pass a SaveOptions object to determine
            # whether to scale all images that are inside shapes to the sizes of their shapes.
            # Setting the "ScaleImageToShapeSize" flag to "true" will shrink every image
            # to the size of the shape that contains it, so that no saved images will be larger than the document requires them to be.
            # Setting the "ScaleImageToShapeSize" flag to "false" will preserve these images' original sizes,
            # which will take up more space in exchange for preserving image quality.
            options = aw.saving.HtmlSaveOptions()
            options.scale_image_to_shape_size = scale_image_to_shape_size
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ScaleImageToShapeSize.html", save_options=options)
            #ExEnd
            tested_image_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "HtmlSaveOptions.ScaleImageToShapeSize.001.png").length()
            if scale_image_to_shape_size:
                self.assertTrue(tested_image_length < 3000)
            else:
                self.assertTrue(tested_image_length < 16000)

    def test_image_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_pretty_format(self):
        for use_pretty_format in [True, False]:
            #ExStart
            #ExFor:SaveOptions.pretty_format
            #ExSummary:Shows how to enhance the readability of the raw code of a saved .html document.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Hello world!")
            html_options = aw.saving.HtmlSaveOptions(aw.SaveFormat.HTML)
            html_options.pretty_format = use_pretty_format
            doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.PrettyFormat.html", save_options=html_options)
            # Enabling pretty format makes the raw html code more readable by adding tab stop and new line characters.
            html = system_helper.io.File.read_all_text(ARTIFACTS_DIR + "HtmlSaveOptions.PrettyFormat.html")
            if use_pretty_format:
                self.assertEqual("<html>\r\n" + "\t<head>\r\n" + "\t\t<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\r\n" + "\t\t<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />\r\n" + f"\t\t<meta name=\"generator\" content=\"{aw.BuildVersionInfo.product} {aw.BuildVersionInfo.version}\" />\r\n" + "\t\t<title>\r\n" + "\t\t</title>\r\n" + "\t</head>\r\n" + "\t<body style=\"font-family:'Times New Roman'; font-size:12pt\">\r\n" + "\t\t<div>\r\n" + "\t\t\t<p style=\"margin-top:0pt; margin-bottom:0pt\">\r\n" + "\t\t\t\t<span>Hello world!</span>\r\n" + "\t\t\t</p>\r\n" + "\t\t\t<p style=\"margin-top:0pt; margin-bottom:0pt\">\r\n" + "\t\t\t\t<span style=\"-aw-import:ignore\">&#xa0;</span>\r\n" + "\t\t\t</p>\r\n" + "\t\t</div>\r\n" + "\t</body>\r\n</html>", html)
            else:
                self.assertEqual("<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />" + "<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />" + f"<meta name=\"generator\" content=\"{aw.BuildVersionInfo.product} {aw.BuildVersionInfo.version}\" /><title></title></head>" + "<body style=\"font-family:'Times New Roman'; font-size:12pt\">" + "<div><p style=\"margin-top:0pt; margin-bottom:0pt\"><span>Hello world!</span></p>" + "<p style=\"margin-top:0pt; margin-bottom:0pt\"><span style=\"-aw-import:ignore\">&#xa0;</span></p></div></body></html>", html)
            #ExEnd

    def test_html_replace_backslash_with_yen_sign(self):
        #ExStart:HtmlReplaceBackslashWithYenSign
        #ExFor:HtmlSaveOptions.replace_backslash_with_yen_sign
        #ExSummary:Shows how to replace backslash characters with yen signs (Html).
        doc = aw.Document(file_name=MY_DIR + "Korean backslash symbol.docx")
        # By default, Aspose.Words mimics MS Word's behavior and doesn't replace backslash characters with yen signs in
        # generated HTML documents. However, previous versions of Aspose.Words performed such replacements in certain
        # scenarios. This flag enables backward compatibility with previous versions of Aspose.Words.
        save_options = aw.saving.HtmlSaveOptions()
        save_options.replace_backslash_with_yen_sign = True
        doc.save(file_name=ARTIFACTS_DIR + "HtmlSaveOptions.ReplaceBackslashWithYenSign.html", save_options=save_options)
        #ExEnd:HtmlReplaceBackslashWithYenSign
