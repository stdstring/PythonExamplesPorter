# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExXpsSaveOptions(ApiExampleBase):
    def test_outline_levels(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        save_options = aspose.words.saving.XpsSaveOptions()
        self.assertEqual(aspose.words.SaveFormat.XPS, save_options.save_format)
        save_options.outline_options.headings_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "XpsSaveOptions.OutlineLevels.xps", save_options=save_options)

    def test_export_exact_pages(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        i = 1
        while i < 6:
            builder.write("Page " + str(i))
            builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
            i += 1
        xps_options = aspose.words.saving.XpsSaveOptions()
        xps_options.page_set = aspose.words.saving.PageSet(pages=[0, 1, 3])
        doc.save(file_name=ARTIFACTS_DIR + "XpsSaveOptions.ExportExactPages.xps", save_options=xps_options)
