# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExXlsxSaveOptions(ApiExampleBase):
    def test_compress_xlsx(self):
        doc = aw.Document(file_name=MY_DIR + "Shape with linked chart.docx")
        xlsx_save_options = aw.saving.XlsxSaveOptions()
        xlsx_save_options.compression_level = aw.saving.CompressionLevel.MAXIMUM
        doc.save(file_name=ARTIFACTS_DIR + "XlsxSaveOptions.CompressXlsx.xlsx", save_options=xlsx_save_options)

    def test_selection_mode(self):
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        xlsx_save_options = aw.saving.XlsxSaveOptions()
        xlsx_save_options.section_mode = aw.saving.XlsxSectionMode.MULTIPLE_WORKSHEETS
        doc.save(file_name=ARTIFACTS_DIR + "XlsxSaveOptions.SelectionMode.xlsx", save_options=xlsx_save_options)
