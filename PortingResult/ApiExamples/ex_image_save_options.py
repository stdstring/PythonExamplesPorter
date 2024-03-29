# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExImageSaveOptions(ApiExampleBase):
    def test_one_page(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_page_set(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_page_by_page(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_color_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_pixel_format(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_floyd_steinberg_dithering(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_jpeg_quality(self):
        raise NotImplementedError("Unsupported ctor for type FileInfo")

    def test_tiff_image_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_resolution(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_export_various_page_ranges(self):
        doc = aw.Document(file_name=MY_DIR + "Images.docx")
        image_options = aw.saving.ImageSaveOptions(aw.SaveFormat.TIFF)
        page_set = aw.saving.PageSet(ranges=[aw.saving.PageRange(1, 1), aw.saving.PageRange(2, 3), aw.saving.PageRange(1, 3), aw.saving.PageRange(2, 4), aw.saving.PageRange(1, 1)])
        image_options.page_set = page_set
        doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.ExportVariousPageRanges.tiff", save_options=image_options)

    def test_render_ink_object(self):
        doc = aw.Document(file_name=MY_DIR + "Ink object.docx")
        save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.JPEG)
        save_options.iml_rendering_mode = aw.saving.ImlRenderingMode.INK_ML
        doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.RenderInkObject.jpeg", save_options=save_options)
