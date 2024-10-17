# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.fonts
import aspose.words.saving
import aspose.words.settings
import datetime
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, IMAGE_DIR, MY_DIR


class ExPdfSaveOptions(ApiExampleBase):
    def test_one_page(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_headings_outline_levels(self):
        #ExStart
        #ExFor:ParagraphFormat.is_heading
        #ExFor:PdfSaveOptions.outline_options
        #ExFor:PdfSaveOptions.save_format
        #ExSummary:Shows how to limit the headings' level that will appear in the outline of a saved PDF document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Insert headings that can serve as TOC entries of levels 1, 2, and then 3.
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
        # to modify how that method converts the document to .PDF.
        save_options = aw.saving.PdfSaveOptions()
        save_options.save_format = aw.SaveFormat.PDF
        # The output PDF document will contain an outline, which is a table of contents that lists headings in the document body.
        # Clicking on an entry in this outline will take us to the location of its respective heading.
        # Set the "HeadingsOutlineLevels" property to "2" to exclude all headings whose levels are above 2 from the outline.
        # The last two headings we have inserted above will not appear.
        save_options.outline_options.headings_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.HeadingsOutlineLevels.pdf", save_options=save_options)
        #ExEnd

    def test_create_missing_outline_levels(self):
        for create_missing_outline_levels in [False, True]:
            #ExStart
            #ExFor:OutlineOptions.create_missing_outline_levels
            #ExFor:PdfSaveOptions.outline_options
            #ExSummary:Shows how to work with outline levels that do not contain any corresponding headings when saving a PDF document.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Insert headings that can serve as TOC entries of levels 1 and 5.
            builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
            self.assertTrue(builder.paragraph_format.is_heading)
            builder.writeln("Heading 1")
            builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING5
            builder.writeln("Heading 1.1.1.1.1")
            builder.writeln("Heading 1.1.1.1.2")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            save_options = aw.saving.PdfSaveOptions()
            # The output PDF document will contain an outline, which is a table of contents that lists headings in the document body.
            # Clicking on an entry in this outline will take us to the location of its respective heading.
            # Set the "HeadingsOutlineLevels" property to "5" to include all headings of levels 5 and below in the outline.
            save_options.outline_options.headings_outline_levels = 5
            # This document contains headings of levels 1 and 5, and no headings with levels of 2, 3, and 4.
            # The output PDF document will treat outline levels 2, 3, and 4 as "missing".
            # Set the "CreateMissingOutlineLevels" property to "true" to include all missing levels in the outline,
            # leaving blank outline entries since there are no usable headings.
            # Set the "CreateMissingOutlineLevels" property to "false" to ignore missing outline levels,
            # and treat the outline level 5 headings as level 2.
            save_options.outline_options.create_missing_outline_levels = create_missing_outline_levels
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.CreateMissingOutlineLevels.pdf", save_options=save_options)
            #ExEnd

    def test_table_heading_outlines(self):
        for create_outlines_for_headings_in_tables in [False, True]:
            #ExStart
            #ExFor:OutlineOptions.create_outlines_for_headings_in_tables
            #ExSummary:Shows how to create PDF document outline entries for headings inside tables.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Create a table with three rows. The first row,
            # whose text we will format in a heading-type style, will serve as the column header.
            builder.start_table()
            builder.insert_cell()
            builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
            builder.write("Customers")
            builder.end_row()
            builder.insert_cell()
            builder.paragraph_format.style_identifier = aw.StyleIdentifier.NORMAL
            builder.write("John Doe")
            builder.end_row()
            builder.insert_cell()
            builder.write("Jane Doe")
            builder.end_table()
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            pdf_save_options = aw.saving.PdfSaveOptions()
            # The output PDF document will contain an outline, which is a table of contents that lists headings in the document body.
            # Clicking on an entry in this outline will take us to the location of its respective heading.
            # Set the "HeadingsOutlineLevels" property to "1" to get the outline
            # to only register headings with heading levels that are no larger than 1.
            pdf_save_options.outline_options.headings_outline_levels = 1
            # Set the "CreateOutlinesForHeadingsInTables" property to "false" to exclude all headings within tables,
            # such as the one we have created above from the outline.
            # Set the "CreateOutlinesForHeadingsInTables" property to "true" to include all headings within tables
            # in the outline, provided that they have a heading level that is no larger than the value of the "HeadingsOutlineLevels" property.
            pdf_save_options.outline_options.create_outlines_for_headings_in_tables = create_outlines_for_headings_in_tables
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.TableHeadingOutlines.pdf", save_options=pdf_save_options)
            #ExEnd

    def test_expanded_outline_levels(self):
        #ExStart
        #ExFor:Document.save(str,SaveOptions)
        #ExFor:PdfSaveOptions
        #ExFor:OutlineOptions.headings_outline_levels
        #ExFor:OutlineOptions.expanded_outline_levels
        #ExSummary:Shows how to convert a whole document to PDF with three levels in the document outline.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Insert headings of levels 1 to 5.
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING4
        builder.writeln("Heading 1.2.2.1")
        builder.writeln("Heading 1.2.2.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING5
        builder.writeln("Heading 1.2.2.2.1")
        builder.writeln("Heading 1.2.2.2.2")
        # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
        # to modify how that method converts the document to .PDF.
        options = aw.saving.PdfSaveOptions()
        # The output PDF document will contain an outline, which is a table of contents that lists headings in the document body.
        # Clicking on an entry in this outline will take us to the location of its respective heading.
        # Set the "HeadingsOutlineLevels" property to "4" to exclude all headings whose levels are above 4 from the outline.
        options.outline_options.headings_outline_levels = 4
        # If an outline entry has subsequent entries of a higher level inbetween itself and the next entry of the same or lower level,
        # an arrow will appear to the left of the entry. This entry is the "owner" of several such "sub-entries".
        # In our document, the outline entries from the 5th heading level are sub-entries of the second 4th level outline entry,
        # the 4th and 5th heading level entries are sub-entries of the second 3rd level entry, and so on.
        # In the outline, we can click on the arrow of the "owner" entry to collapse/expand all its sub-entries.
        # Set the "ExpandedOutlineLevels" property to "2" to automatically expand all heading level 2 and lower outline entries
        # and collapse all level and 3 and higher entries when we open the document.
        options.outline_options.expanded_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExpandedOutlineLevels.pdf", save_options=options)
        #ExEnd

    def test_update_fields(self):
        for update_fields in [False, True]:
            #ExStart
            #ExFor:PdfSaveOptions.clone
            #ExFor:SaveOptions.update_fields
            #ExSummary:Shows how to update all the fields in a document immediately before saving it to PDF.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # Insert text with PAGE and NUMPAGES fields. These fields do not display the correct value in real time.
            # We will need to manually update them using updating methods such as "Field.Update()", and "Document.UpdateFields()"
            # each time we need them to display accurate values.
            builder.write("Page ")
            builder.insert_field(field_code="PAGE", field_value="")
            builder.write(" of ")
            builder.insert_field(field_code="NUMPAGES", field_value="")
            builder.insert_break(aw.BreakType.PAGE_BREAK)
            builder.writeln("Hello World!")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            options = aw.saving.PdfSaveOptions()
            # Set the "UpdateFields" property to "false" to not update all the fields in a document right before a save operation.
            # This is the preferable option if we know that all our fields will be up to date before saving.
            # Set the "UpdateFields" property to "true" to iterate through all the document
            # fields and update them before we save it as a PDF. This will make sure that all the fields will display
            # the most accurate values in the PDF.
            options.update_fields = update_fields
            # We can clone PdfSaveOptions objects.
            self.assertNotEqual(options, options.clone())
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.UpdateFields.pdf", save_options=options)
            #ExEnd

    def test_preserve_form_fields(self):
        for preserve_form_fields in [False, True]:
            #ExStart
            #ExFor:PdfSaveOptions.preserve_form_fields
            #ExSummary:Shows how to save a document to the PDF format using the Save method and the PdfSaveOptions class.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.write("Please select a fruit: ")
            # Insert a combo box which will allow a user to choose an option from a collection of strings.
            builder.insert_combo_box("MyComboBox", ["Apple", "Banana", "Cherry"], 0)
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            pdf_options = aw.saving.PdfSaveOptions()
            # Set the "PreserveFormFields" property to "true" to save form fields as interactive objects in the output PDF.
            # Set the "PreserveFormFields" property to "false" to freeze all form fields in the document at
            # their current values and display them as plain text in the output PDF.
            pdf_options.preserve_form_fields = preserve_form_fields
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PreserveFormFields.pdf", save_options=pdf_options)
            #ExEnd

    def test_compliance(self):
        for pdf_compliance in [aw.saving.PdfCompliance.PDF_A_2U,
                               aw.saving.PdfCompliance.PDF17,
                               aw.saving.PdfCompliance.PDF_A_2A,
                               aw.saving.PdfCompliance.PDF_UA1,
                               aw.saving.PdfCompliance.PDF20,
                               aw.saving.PdfCompliance.PDF_A4,
                               aw.saving.PdfCompliance.PDF_A_4_UA_2,
                               aw.saving.PdfCompliance.PDF_UA2]:
            #ExStart
            #ExFor:PdfSaveOptions.compliance
            #ExFor:PdfCompliance
            #ExSummary:Shows how to set the PDF standards compliance level of saved PDF documents.
            doc = aw.Document(file_name=MY_DIR + "Images.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            # Note that some PdfSaveOptions are prohibited when saving to one of the standards and automatically fixed.
            # Use IWarningCallback to know which options are automatically fixed.
            save_options = aw.saving.PdfSaveOptions()
            # Set the "Compliance" property to "PdfCompliance.PdfA1b" to comply with the "PDF/A-1b" standard,
            # which aims to preserve the visual appearance of the document as Aspose.Words convert it to PDF.
            # Set the "Compliance" property to "PdfCompliance.Pdf17" to comply with the "1.7" standard.
            # Set the "Compliance" property to "PdfCompliance.PdfA1a" to comply with the "PDF/A-1a" standard,
            # which complies with "PDF/A-1b" as well as preserving the document structure of the original document.
            # Set the "Compliance" property to "PdfCompliance.PdfUa1" to comply with the "PDF/UA-1" (ISO 14289-1) standard,
            # which aims to define represent electronic documents in PDF that allow the file to be accessible.
            # Set the "Compliance" property to "PdfCompliance.Pdf20" to comply with the "PDF 2.0" (ISO 32000-2) standard.
            # Set the "Compliance" property to "PdfCompliance.PdfA4" to comply with the "PDF/A-4" (ISO 19004:2020) standard,
            # which preserving document static visual appearance over time.
            # Set the "Compliance" property to "PdfCompliance.PdfA4Ua2" to comply with both PDF/A-4 (ISO 19005-4:2020)
            # and PDF/UA-2 (ISO 14289-2:2024) standards.
            # Set the "Compliance" property to "PdfCompliance.PdfUa2" to comply with the PDF/UA-2 (ISO 14289-2:2024) standard.
            # This helps with making documents searchable but may significantly increase the size of already large documents.
            save_options.compliance = pdf_compliance
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.Compliance.pdf", save_options=save_options)
            #ExEnd

    def test_text_compression(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_image_compression(self):
        for pdf_image_compression in [aw.saving.PdfImageCompression.AUTO,
                                      aw.saving.PdfImageCompression.JPEG]:
            #ExStart
            #ExFor:PdfSaveOptions.image_compression
            #ExFor:PdfSaveOptions.jpeg_quality
            #ExFor:PdfImageCompression
            #ExSummary:Shows how to specify a compression type for all images in a document that we are converting to PDF.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Jpeg image:")
            builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            builder.insert_paragraph()
            builder.writeln("Png image:")
            builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            pdf_save_options = aw.saving.PdfSaveOptions()
            # Set the "ImageCompression" property to "PdfImageCompression.Auto" to use the
            # "ImageCompression" property to control the quality of the Jpeg images that end up in the output PDF.
            # Set the "ImageCompression" property to "PdfImageCompression.Jpeg" to use the
            # "ImageCompression" property to control the quality of all images that end up in the output PDF.
            pdf_save_options.image_compression = pdf_image_compression
            # Set the "JpegQuality" property to "10" to strengthen compression at the cost of image quality.
            pdf_save_options.jpeg_quality = 10
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ImageCompression.pdf", save_options=pdf_save_options)
            #ExEnd

    def test_image_color_space_export_mode(self):
        for pdf_image_color_space_export_mode in [aw.saving.PdfImageColorSpaceExportMode.AUTO,
                                                  aw.saving.PdfImageColorSpaceExportMode.SIMPLE_CMYK]:
            #ExStart
            #ExFor:PdfImageColorSpaceExportMode
            #ExFor:PdfSaveOptions.image_color_space_export_mode
            #ExSummary:Shows how to set a different color space for images in a document as we export it to PDF.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Jpeg image:")
            builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            builder.insert_paragraph()
            builder.writeln("Png image:")
            builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            pdf_save_options = aw.saving.PdfSaveOptions()
            # Set the "ImageColorSpaceExportMode" property to "PdfImageColorSpaceExportMode.Auto" to get Aspose.Words to
            # automatically select the color space for images in the document that it converts to PDF.
            # In most cases, the color space will be RGB.
            # Set the "ImageColorSpaceExportMode" property to "PdfImageColorSpaceExportMode.SimpleCmyk"
            # to use the CMYK color space for all images in the saved PDF.
            # Aspose.Words will also apply Flate compression to all images and ignore the "ImageCompression" property's value.
            pdf_save_options.image_color_space_export_mode = pdf_image_color_space_export_mode
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ImageColorSpaceExportMode.pdf", save_options=pdf_save_options)
            #ExEnd

    def test_downsample_options(self):
        #ExStart
        #ExFor:DownsampleOptions
        #ExFor:DownsampleOptions.downsample_images
        #ExFor:DownsampleOptions.resolution
        #ExFor:DownsampleOptions.resolution_threshold
        #ExFor:PdfSaveOptions.downsample_options
        #ExSummary:Shows how to change the resolution of images in the PDF document.
        doc = aw.Document(file_name=MY_DIR + "Images.docx")
        # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
        # to modify how that method converts the document to .PDF.
        options = aw.saving.PdfSaveOptions()
        # By default, Aspose.Words downsample all images in a document that we save to PDF to 220 ppi.
        self.assertTrue(options.downsample_options.downsample_images)
        self.assertEqual(220, options.downsample_options.resolution)
        self.assertEqual(0, options.downsample_options.resolution_threshold)
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DownsampleOptions.Default.pdf", save_options=options)
        # Set the "Resolution" property to "36" to downsample all images to 36 ppi.
        options.downsample_options.resolution = 36
        # Set the "ResolutionThreshold" property to only apply the downsampling to
        # images with a resolution that is above 128 ppi.
        options.downsample_options.resolution_threshold = 128
        # Only the first two images from the document will be downsampled at this stage.
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DownsampleOptions.LowerResolution.pdf", save_options=options)
        #ExEnd

    def test_color_rendering(self):
        for color_mode in [aw.saving.ColorMode.GRAYSCALE, aw.saving.ColorMode.NORMAL]:
            #ExStart
            #ExFor:PdfSaveOptions
            #ExFor:ColorMode
            #ExFor:FixedPageSaveOptions.color_mode
            #ExSummary:Shows how to change image color with saving options property.
            doc = aw.Document(file_name=MY_DIR + "Images.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            # Set the "ColorMode" property to "Grayscale" to render all images from the document in black and white.
            # The size of the output document may be larger with this setting.
            # Set the "ColorMode" property to "Normal" to render all images in color.
            pdf_save_options = aw.saving.PdfSaveOptions()
            pdf_save_options.color_mode = color_mode
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ColorRendering.pdf", save_options=pdf_save_options)
            #ExEnd

    def test_doc_title(self):
        for display_doc_title in [False, True]:
            #ExStart
            #ExFor:PdfSaveOptions.display_doc_title
            #ExSummary:Shows how to display the title of the document as the title bar.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Hello world!")
            doc.built_in_document_properties.title = "Windows bar pdf title"
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            # Set the "DisplayDocTitle" to "true" to get some PDF readers, such as Adobe Acrobat Pro,
            # to display the value of the document's "Title" built-in property in the tab that belongs to this document.
            # Set the "DisplayDocTitle" to "false" to get such readers to display the document's filename.
            pdf_save_options = aw.saving.PdfSaveOptions()
            pdf_save_options.display_doc_title = display_doc_title
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DocTitle.pdf", save_options=pdf_save_options)
            #ExEnd

    def test_memory_optimization(self):
        for memory_optimization in [False, True]:
            #ExStart
            #ExFor:SaveOptions.create_save_options(SaveFormat)
            #ExFor:SaveOptions.memory_optimization
            #ExSummary:Shows an option to optimize memory consumption when rendering large documents to PDF.
            doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            save_options = aw.saving.SaveOptions.create_save_options(save_format=aw.SaveFormat.PDF)
            # Set the "MemoryOptimization" property to "true" to lower the memory footprint of large documents' saving operations
            # at the cost of increasing the duration of the operation.
            # Set the "MemoryOptimization" property to "false" to save the document as a PDF normally.
            save_options.memory_optimization = memory_optimization
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.MemoryOptimization.pdf", save_options=save_options)
            #ExEnd

    def test_escape_uri(self):
        for uri, result in [("""https://www.google.com/search?q= aspose""", "https://www.google.com/search?q=%20aspose"),
                            ("""https://www.google.com/search?q=%20aspose""", "https://www.google.com/search?q=%20aspose")]:
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.insert_hyperlink("Testlink", uri, False)
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EscapedUri.pdf")

    def test_open_hyperlinks_in_new_window(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_header_footer_bookmarks_export_mode(self):
        for header_footer_bookmarks_export_mode in [aw.saving.HeaderFooterBookmarksExportMode.NONE,
                                                    aw.saving.HeaderFooterBookmarksExportMode.FIRST,
                                                    aw.saving.HeaderFooterBookmarksExportMode.ALL]:
            #ExStart
            #ExFor:HeaderFooterBookmarksExportMode
            #ExFor:OutlineOptions
            #ExFor:OutlineOptions.default_bookmarks_outline_level
            #ExFor:PdfSaveOptions.header_footer_bookmarks_export_mode
            #ExFor:PdfSaveOptions.page_mode
            #ExFor:PdfPageMode
            #ExSummary:Shows to process bookmarks in headers/footers in a document that we are rendering to PDF.
            doc = aw.Document(file_name=MY_DIR + "Bookmarks in headers and footers.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            save_options = aw.saving.PdfSaveOptions()
            # Set the "PageMode" property to "PdfPageMode.UseOutlines" to display the outline navigation pane in the output PDF.
            save_options.page_mode = aw.saving.PdfPageMode.USE_OUTLINES
            # Set the "DefaultBookmarksOutlineLevel" property to "1" to display all
            # bookmarks at the first level of the outline in the output PDF.
            save_options.outline_options.default_bookmarks_outline_level = 1
            # Set the "HeaderFooterBookmarksExportMode" property to "HeaderFooterBookmarksExportMode.None" to
            # not export any bookmarks that are inside headers/footers.
            # Set the "HeaderFooterBookmarksExportMode" property to "HeaderFooterBookmarksExportMode.First" to
            # only export bookmarks in the first section's header/footers.
            # Set the "HeaderFooterBookmarksExportMode" property to "HeaderFooterBookmarksExportMode.All" to
            # export bookmarks that are in all headers/footers.
            save_options.header_footer_bookmarks_export_mode = header_footer_bookmarks_export_mode
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.HeaderFooterBookmarksExportMode.pdf", save_options=save_options)
            #ExEnd

    def test_emulate_rendering_to_size_on_page(self):
        for render_to_size in [False, True]:
            #ExStart
            #ExFor:MetafileRenderingOptions.emulate_rendering_to_size_on_page
            #ExFor:MetafileRenderingOptions.emulate_rendering_to_size_on_page_resolution
            #ExSummary:Shows how to display of the metafile according to the size on page.
            doc = aw.Document(file_name=MY_DIR + "WMF with text.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            save_options = aw.saving.PdfSaveOptions()
            # Set the "EmulateRenderingToSizeOnPage" property to "true"
            # to emulate rendering according to the metafile size on page.
            # Set the "EmulateRenderingToSizeOnPage" property to "false"
            # to emulate metafile rendering to its default size in pixels.
            save_options.metafile_rendering_options.emulate_rendering_to_size_on_page = render_to_size
            save_options.metafile_rendering_options.emulate_rendering_to_size_on_page_resolution = 50
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EmulateRenderingToSizeOnPage.pdf", save_options=save_options)
            #ExEnd

    def test_embed_full_fonts(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_embed_windows_fonts(self):
        for pdf_font_embedding_mode in [aw.saving.PdfFontEmbeddingMode.EMBED_ALL,
                                        aw.saving.PdfFontEmbeddingMode.EMBED_NONE,
                                        aw.saving.PdfFontEmbeddingMode.EMBED_NONSTANDARD]:
            #ExStart
            #ExFor:PdfSaveOptions.font_embedding_mode
            #ExFor:PdfFontEmbeddingMode
            #ExSummary:Shows how to set Aspose.Words to skip embedding Arial and Times New Roman fonts into a PDF document.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            # "Arial" is a standard font, and "Courier New" is a nonstandard font.
            builder.font.name = "Arial"
            builder.writeln("Hello world!")
            builder.font.name = "Courier New"
            builder.writeln("The quick brown fox jumps over the lazy dog.")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            options = aw.saving.PdfSaveOptions()
            # Set the "EmbedFullFonts" property to "true" to embed every glyph of every embedded font in the output PDF.
            options.embed_full_fonts = True
            # Set the "FontEmbeddingMode" property to "EmbedAll" to embed all fonts in the output PDF.
            # Set the "FontEmbeddingMode" property to "EmbedNonstandard" to only allow nonstandard fonts' embedding in the output PDF.
            # Set the "FontEmbeddingMode" property to "EmbedNone" to not embed any fonts in the output PDF.
            options.font_embedding_mode = pdf_font_embedding_mode
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EmbedWindowsFonts.pdf", save_options=options)
            #ExEnd
            tested_file_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "PdfSaveOptions.EmbedWindowsFonts.pdf").length()
            switch_condition = pdf_font_embedding_mode
            if switch_condition == aw.saving.PdfFontEmbeddingMode.EMBED_ALL:
                self.assertTrue(tested_file_length < 1040000)
            elif switch_condition == aw.saving.PdfFontEmbeddingMode.EMBED_NONSTANDARD:
                self.assertTrue(tested_file_length < 492000)
            elif switch_condition == aw.saving.PdfFontEmbeddingMode.EMBED_NONE:
                self.assertTrue(tested_file_length < 4300)

    def test_embed_core_fonts(self):
        for use_core_fonts in [False, True]:
            #ExStart
            #ExFor:PdfSaveOptions.use_core_fonts
            #ExSummary:Shows how enable/disable PDF Type 1 font substitution.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.font.name = "Arial"
            builder.writeln("Hello world!")
            builder.font.name = "Courier New"
            builder.writeln("The quick brown fox jumps over the lazy dog.")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            options = aw.saving.PdfSaveOptions()
            # Set the "UseCoreFonts" property to "true" to replace some fonts,
            # including the two fonts in our document, with their PDF Type 1 equivalents.
            # Set the "UseCoreFonts" property to "false" to not apply PDF Type 1 fonts.
            options.use_core_fonts = use_core_fonts
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EmbedCoreFonts.pdf", save_options=options)
            #ExEnd
            tested_file_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "PdfSaveOptions.EmbedCoreFonts.pdf").length()
            if use_core_fonts:
                self.assertTrue(tested_file_length < 2000)
            else:
                self.assertTrue(tested_file_length < 33500)

    def test_additional_text_positioning(self):
        for apply_additional_text_positioning in [False, True]:
            #ExStart
            #ExFor:PdfSaveOptions.additional_text_positioning
            #ExSummary:Show how to write additional text positioning operators.
            doc = aw.Document(file_name=MY_DIR + "Text positioning operators.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            save_options = aw.saving.PdfSaveOptions()
            save_options.text_compression = aw.saving.PdfTextCompression.NONE
            save_options.additional_text_positioning = apply_additional_text_positioning
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.AdditionalTextPositioning.pdf", save_options=save_options)
            #ExEnd

    def test_save_as_pdf_book_fold(self):
        for render_text_as_bookfold in [False, True]:
            #ExStart
            #ExFor:PdfSaveOptions.use_book_fold_printing_settings
            #ExSummary:Shows how to save a document to the PDF format in the form of a book fold.
            doc = aw.Document(file_name=MY_DIR + "Paragraphs.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            options = aw.saving.PdfSaveOptions()
            # Set the "UseBookFoldPrintingSettings" property to "true" to arrange the contents
            # in the output PDF in a way that helps us use it to make a booklet.
            # Set the "UseBookFoldPrintingSettings" property to "false" to render the PDF normally.
            options.use_book_fold_printing_settings = render_text_as_bookfold
            # If we are rendering the document as a booklet, we must set the "MultiplePages"
            # properties of the page setup objects of all sections to "MultiplePagesType.BookFoldPrinting".
            if render_text_as_bookfold:
                for s in doc.sections:
                    s = s.as_section()
                    s.page_setup.multiple_pages = aw.settings.MultiplePagesType.BOOK_FOLD_PRINTING
            # Once we print this document on both sides of the pages, we can fold all the pages down the middle at once,
            # and the contents will line up in a way that creates a booklet.
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.SaveAsPdfBookFold.pdf", save_options=options)
            #ExEnd

    def test_zoom_behaviour(self):
        #ExStart
        #ExFor:PdfSaveOptions.zoom_behavior
        #ExFor:PdfSaveOptions.zoom_factor
        #ExFor:PdfZoomBehavior
        #ExSummary:Shows how to set the default zooming that a reader applies when opening a rendered PDF document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.writeln("Hello world!")
        # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
        # to modify how that method converts the document to .PDF.
        # Set the "ZoomBehavior" property to "PdfZoomBehavior.ZoomFactor" to get a PDF reader to
        # apply a percentage-based zoom factor when we open the document with it.
        # Set the "ZoomFactor" property to "25" to give the zoom factor a value of 25%.
        options = aw.saving.PdfSaveOptions()
        options.zoom_behavior = aw.saving.PdfZoomBehavior.ZOOM_FACTOR
        options.zoom_factor = 25
        # When we open this document using a reader such as Adobe Acrobat, we will see the document scaled at 1/4 of its actual size.
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ZoomBehaviour.pdf", save_options=options)
        #ExEnd

    def test_page_mode(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_note_hyperlinks(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_custom_properties_export(self):
        raise NotImplementedError("Unsupported call of method named IsRunningOnMono")

    def test_drawing_ml_effects(self):
        for effects_rendering_mode in [aw.saving.DmlEffectsRenderingMode.NONE,
                                       aw.saving.DmlEffectsRenderingMode.SIMPLIFIED,
                                       aw.saving.DmlEffectsRenderingMode.FINE]:
            #ExStart
            #ExFor:DmlRenderingMode
            #ExFor:DmlEffectsRenderingMode
            #ExFor:PdfSaveOptions.dml_effects_rendering_mode
            #ExFor:SaveOptions.dml_effects_rendering_mode
            #ExFor:SaveOptions.dml_rendering_mode
            #ExSummary:Shows how to configure the rendering quality of DrawingML effects in a document as we save it to PDF.
            doc = aw.Document(file_name=MY_DIR + "DrawingML shape effects.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            options = aw.saving.PdfSaveOptions()
            # Set the "DmlEffectsRenderingMode" property to "DmlEffectsRenderingMode.None" to discard all DrawingML effects.
            # Set the "DmlEffectsRenderingMode" property to "DmlEffectsRenderingMode.Simplified"
            # to render a simplified version of DrawingML effects.
            # Set the "DmlEffectsRenderingMode" property to "DmlEffectsRenderingMode.Fine" to
            # render DrawingML effects with more accuracy and also with more processing cost.
            options.dml_effects_rendering_mode = effects_rendering_mode
            self.assertEqual(aw.saving.DmlRenderingMode.DRAWING_ML, options.dml_rendering_mode)
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.DrawingMLEffects.pdf", save_options=options)
            #ExEnd

    def test_drawing_ml_fallback(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_export_document_structure(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_preblend_images(self):
        raise NotImplementedError("Unsupported ctor for type Aspose.Pdf.Document")

    def test_interpolate_images(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported target type System.TimeSpan")

    def test_render_metafile(self):
        for rendering_mode in [aw.saving.EmfPlusDualRenderingMode.EMF,
                               aw.saving.EmfPlusDualRenderingMode.EMF_PLUS,
                               aw.saving.EmfPlusDualRenderingMode.EMF_PLUS_WITH_FALLBACK]:
            #ExStart
            #ExFor:EmfPlusDualRenderingMode
            #ExFor:MetafileRenderingOptions.emf_plus_dual_rendering_mode
            #ExFor:MetafileRenderingOptions.use_emf_embedded_to_wmf
            #ExSummary:Shows how to configure Enhanced Windows Metafile-related rendering options when saving to PDF.
            doc = aw.Document(file_name=MY_DIR + "EMF.docx")
            # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
            # to modify how that method converts the document to .PDF.
            save_options = aw.saving.PdfSaveOptions()
            # Set the "EmfPlusDualRenderingMode" property to "EmfPlusDualRenderingMode.Emf"
            # to only render the EMF part of an EMF+ dual metafile.
            # Set the "EmfPlusDualRenderingMode" property to "EmfPlusDualRenderingMode.EmfPlus" to
            # to render the EMF+ part of an EMF+ dual metafile.
            # Set the "EmfPlusDualRenderingMode" property to "EmfPlusDualRenderingMode.EmfPlusWithFallback"
            # to render the EMF+ part of an EMF+ dual metafile if all of the EMF+ records are supported.
            # Otherwise, Aspose.Words will render the EMF part.
            save_options.metafile_rendering_options.emf_plus_dual_rendering_mode = rendering_mode
            # Set the "UseEmfEmbeddedToWmf" property to "true" to render embedded EMF data
            # for metafiles that we can render as vector graphics.
            save_options.metafile_rendering_options.use_emf_embedded_to_wmf = True
            doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.RenderMetafile.pdf", save_options=save_options)
            #ExEnd

    def test_encryption_permissions(self):
        #ExStart
        #ExFor:PdfEncryptionDetails.__init__(str,str,PdfPermissions)
        #ExFor:PdfSaveOptions.encryption_details
        #ExFor:PdfEncryptionDetails.permissions
        #ExFor:PdfEncryptionDetails.owner_password
        #ExFor:PdfEncryptionDetails.user_password
        #ExFor:PdfPermissions
        #ExFor:PdfEncryptionDetails
        #ExSummary:Shows how to set permissions on a saved PDF document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.writeln("Hello world!")
        # Extend permissions to allow the editing of annotations.
        encryption_details = aw.saving.PdfEncryptionDetails(user_password="password", owner_password="", permissions=aw.saving.PdfPermissions.MODIFY_ANNOTATIONS | aw.saving.PdfPermissions.DOCUMENT_ASSEMBLY)
        # Create a "PdfSaveOptions" object that we can pass to the document's "Save" method
        # to modify how that method converts the document to .PDF.
        save_options = aw.saving.PdfSaveOptions()
        # Enable encryption via the "EncryptionDetails" property.
        save_options.encryption_details = encryption_details
        # When we open this document, we will need to provide the password before accessing its contents.
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.EncryptionPermissions.pdf", save_options=save_options)
        #ExEnd

    def test_set_numeral_format(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_export_page_set(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_export_language_to_span_tag(self):
        #ExStart
        #ExFor:PdfSaveOptions.export_language_to_span_tag
        #ExSummary:Shows how to create a "Span" tag in the document structure to export the text language.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.writeln("Hello world!")
        builder.writeln("Hola mundo!")
        save_options = aw.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_language_to_span_tag = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExportLanguageToSpanTag.pdf", save_options=save_options)
        #ExEnd

    def test_pdf_embed_attachments(self):
        #ExStart
        #ExFor:PdfSaveOptions.embed_attachments
        #ExSummary:Shows how to add embed attachments to the PDF document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.insert_ole_object(file_name=MY_DIR + "Spreadsheet.xlsx", prog_id="Excel.Sheet", is_linked=False, as_icon=True, presentation=None)
        options = aw.saving.PdfSaveOptions()
        options.embed_attachments = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PdfEmbedAttachments.pdf", save_options=options)
        #ExEnd

    def test_cache_background_graphics(self):
        #ExStart
        #ExFor:PdfSaveOptions.cache_background_graphics
        #ExSummary:Shows how to cache graphics placed in document's background.
        doc = aw.Document(file_name=MY_DIR + "Background images.docx")
        save_options = aw.saving.PdfSaveOptions()
        save_options.cache_background_graphics = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.CacheBackgroundGraphics.pdf", save_options=save_options)
        aspose_to_pdf_size = system_helper.io.FileInfo(ARTIFACTS_DIR + "PdfSaveOptions.CacheBackgroundGraphics.pdf").length()
        word_to_pdf_size = system_helper.io.FileInfo(MY_DIR + "Background images (word to pdf).pdf").length()
        self.assertLess(aspose_to_pdf_size, word_to_pdf_size)
        #ExEnd

    def test_export_paragraph_graphics_to_artifact(self):
        #ExStart
        #ExFor:PdfSaveOptions.export_paragraph_graphics_to_artifact
        #ExSummary:Shows how to export paragraph graphics as artifact (underlines, text emphasis, etc.).
        doc = aw.Document(file_name=MY_DIR + "PDF artifacts.docx")
        save_options = aw.saving.PdfSaveOptions()
        save_options.export_document_structure = True
        save_options.export_paragraph_graphics_to_artifact = True
        save_options.text_compression = aw.saving.PdfTextCompression.NONE
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.ExportParagraphGraphicsToArtifact.pdf", save_options=save_options)
        #ExEnd

    def test_page_layout(self):
        #ExStart:PageLayout
        #ExFor:PdfSaveOptions.page_layout
        #ExFor:PdfPageLayout
        #ExSummary:Shows how to display pages when opened in a PDF reader.
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        # Display the pages two at a time, with odd-numbered pages on the left.
        save_options = aw.saving.PdfSaveOptions()
        save_options.page_layout = aw.saving.PdfPageLayout.TWO_PAGE_LEFT
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.PageLayout.pdf", save_options=save_options)
        #ExEnd:PageLayout

    def test_sdt_tag_as_form_field_name(self):
        #ExStart:SdtTagAsFormFieldName
        #ExFor:PdfSaveOptions.use_sdt_tag_as_form_field_name
        #ExSummary:Shows how to use SDT control Tag or Id property as a name of form field in PDF.
        doc = aw.Document(file_name=MY_DIR + "Form fields.docx")
        save_options = aw.saving.PdfSaveOptions()
        save_options.preserve_form_fields = True
        # When set to 'false', SDT control Id property is used as a name of form field in PDF.
        # When set to 'true', SDT control Tag property is used as a name of form field in PDF.
        save_options.use_sdt_tag_as_form_field_name = True
        doc.save(file_name=ARTIFACTS_DIR + "PdfSaveOptions.SdtTagAsFormFieldName.pdf", save_options=save_options)
        #ExEnd:SdtTagAsFormFieldName
