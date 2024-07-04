# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExXpsSaveOptions(ApiExampleBase):
    def test_outline_levels(self):
        #ExStart
        #ExFor:XpsSaveOptions
        #ExFor:XpsSaveOptions.__init__
        #ExFor:XpsSaveOptions.outline_options
        #ExFor:XpsSaveOptions.save_format
        #ExSummary:Shows how to limit the headings' level that will appear in the outline of a saved XPS document.
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
        # Create an "XpsSaveOptions" object that we can pass to the document's "Save" method
        # to modify how that method converts the document to .XPS.
        save_options = aw.saving.XpsSaveOptions()
        self.assertEqual(aw.SaveFormat.XPS, save_options.save_format)
        # The output XPS document will contain an outline, a table of contents that lists headings in the document body.
        # Clicking on an entry in this outline will take us to the location of its respective heading.
        # Set the "HeadingsOutlineLevels" property to "2" to exclude all headings whose levels are above 2 from the outline.
        # The last two headings we have inserted above will not appear.
        save_options.outline_options.headings_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "XpsSaveOptions.OutlineLevels.xps", save_options=save_options)
        #ExEnd

    def test_book_fold(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_optimize_output(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_exact_pages(self):
        #ExStart
        #ExFor:FixedPageSaveOptions.page_set
        #ExFor:PageSet.__init__(List[int])
        #ExSummary:Shows how to extract pages based on exact page indices.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Add five pages to the document.
        i = 1
        while i < 6:
            builder.write("Page " + str(i))
            builder.insert_break(aw.BreakType.PAGE_BREAK)
            i += 1
        # Create an "XpsSaveOptions" object, which we can pass to the document's "Save" method
        # to modify how that method converts the document to .XPS.
        xps_options = aw.saving.XpsSaveOptions()
        # Use the "PageSet" property to select a set of the document's pages to save to output XPS.
        # In this case, we will choose, via a zero-based index, only three pages: page 1, page 2, and page 4.
        xps_options.page_set = aw.saving.PageSet(pages=[0, 1, 3])
        doc.save(file_name=ARTIFACTS_DIR + "XpsSaveOptions.ExportExactPages.xps", save_options=xps_options)
        #ExEnd
