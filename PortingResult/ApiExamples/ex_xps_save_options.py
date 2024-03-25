# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExXpsSaveOptions(ApiExampleBase):
    def test_outline_levels(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1
        self.assertTrue(builder.paragraph_format.is_heading)
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING3
        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")
        save_options = aw.saving.XpsSaveOptions()
        self.assertEqual(aw.SaveFormat.XPS, save_options.save_format)
        save_options.outline_options.headings_outline_levels = 2
        doc.save(file_name=ARTIFACTS_DIR + "XpsSaveOptions.OutlineLevels.xps", save_options=save_options)

    def test_book_fold(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_export_exact_pages(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        i = 1
        while i < 6:
            builder.write("Page " + str(i))
            builder.insert_break(aw.BreakType.PAGE_BREAK)
            i += 1
        xps_options = aw.saving.XpsSaveOptions()
        xps_options.page_set = aw.saving.PageSet(pages=[0, 1, 3])
        doc.save(file_name=ARTIFACTS_DIR + "XpsSaveOptions.ExportExactPages.xps", save_options=xps_options)
