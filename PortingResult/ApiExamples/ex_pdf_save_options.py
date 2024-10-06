# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.digitalsignatures
import aspose.words.saving
import datetime
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


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
        builder = aw.DocumentBuilder(doc)
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
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_table_heading_outlines(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_expanded_outline_levels(self):
        #ExStart
        #ExFor:Document.save(str,SaveOptions)
        #ExFor:PdfSaveOptions
        #ExFor:OutlineOptions.headings_outline_levels
        #ExFor:OutlineOptions.expanded_outline_levels
        #ExSummary:Shows how to convert a whole document to PDF with three levels in the document outline.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
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
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_preserve_form_fields(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_compliance(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_text_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_image_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_image_color_space_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

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
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_doc_title(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_memory_optimization(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_escape_uri(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_open_hyperlinks_in_new_window(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_header_footer_bookmarks_export_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_emulate_rendering_to_size_on_page(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_embed_full_fonts(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_embed_windows_fonts(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_embed_core_fonts(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_additional_text_positioning(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_save_as_pdf_book_fold(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_zoom_behaviour(self):
        #ExStart
        #ExFor:PdfSaveOptions.zoom_behavior
        #ExFor:PdfSaveOptions.zoom_factor
        #ExFor:PdfZoomBehavior
        #ExSummary:Shows how to set the default zooming that a reader applies when opening a rendered PDF document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
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
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_note_hyperlinks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_custom_properties_export(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_drawing_ml_effects(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_drawing_ml_fallback(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_document_structure(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_preblend_images(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_interpolate_images(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_pdf_digital_signature(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_pdf_digital_signature_timestamp(self):
        raise NotImplementedError("Unsupported target type System.TimeSpan")

    def test_render_metafile(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

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
        builder = aw.DocumentBuilder(doc)
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
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_page_set(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_export_language_to_span_tag(self):
        #ExStart
        #ExFor:PdfSaveOptions.export_language_to_span_tag
        #ExSummary:Shows how to create a "Span" tag in the document structure to export the text language.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
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
        builder = aw.DocumentBuilder(doc)
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
