# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExPclSaveOptions(ApiExampleBase):
    def test_rasterize_elements(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        save_options = aw.saving.PclSaveOptions()
        save_options.save_format = aw.SaveFormat.PCL
        save_options.rasterize_transformed_elements = True
        doc.save(file_name=ARTIFACTS_DIR + "PclSaveOptions.RasterizeElements.pcl", save_options=save_options)

    def test_fallback_font_name(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.font.name = "Non-existent font"
        builder.write("Hello world!")
        save_options = aw.saving.PclSaveOptions()
        save_options.fallback_font_name = "Times New Roman"
        doc.save(file_name=ARTIFACTS_DIR + "PclSaveOptions.SetPrinterFont.pcl", save_options=save_options)

    def test_add_printer_font(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.font.name = "Courier"
        builder.write("Hello world!")
        save_options = aw.saving.PclSaveOptions()
        save_options.add_printer_font("Courier New", "Courier")
        doc.save(file_name=ARTIFACTS_DIR + "PclSaveOptions.AddPrinterFont.pcl", save_options=save_options)

    def test_get_preserved_paper_tray_information(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        for section in doc.sections.of_type():
            section.page_setup.first_page_tray = 15
            section.page_setup.other_pages_tray = 12
        doc.save(file_name=ARTIFACTS_DIR + "PclSaveOptions.GetPreservedPaperTrayInformation.pcl")
