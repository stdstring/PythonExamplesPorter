# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExXpsSaveOptions(ApiExampleBase):
    def test_outline_levels(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_export_exact_pages(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        # for loop begin
        i = 1
        while i < 6:
            builder.write("Page " + str(i))
            builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
            i += 1
        # for loop end
        xps_options = aspose.words.saving.XpsSaveOptions()
        xps_options.page_set = aspose.words.saving.PageSet(pages = [0, 1, 3])
        doc.save(file_name = ARTIFACTS_DIR + "XpsSaveOptions.ExportExactPages.xps", save_options = xps_options)
