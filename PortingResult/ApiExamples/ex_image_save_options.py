# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.pydrawing
import aspose.words as aw
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExImageSaveOptions(ApiExampleBase):
    def test_one_page(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_renderer(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_page_set(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_graphics_quality(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Drawing2D.SmoothingMode")

    def test_use_tile_flip_mode(self):
        #ExStart
        #ExFor:GraphicsQualityOptions.use_tile_flip_mode
        #ExSummary:Shows how to prevent the white line appears when rendering with a high resolution.
        doc = aw.Document(file_name=MY_DIR + "Shape high dpi.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        renderer = shape.get_shape_renderer()
        save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)
        save_options.resolution = 500
        save_options.graphics_quality_options = aw.saving.GraphicsQualityOptions()
        save_options.graphics_quality_options.use_tile_flip_mode = True
        renderer.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.UseTileFlipMode.png", save_options=save_options)
        #ExEnd

    def test_windows_meta_file(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_page_by_page(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_color_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_paper_color(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_pixel_format(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_floyd_steinberg_dithering(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_edit_image(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_jpeg_quality(self):
        raise NotImplementedError("Unsupported ctor for type FileInfo")

    def test_tiff_image_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_resolution(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_export_various_page_ranges(self):
        #ExStart
        #ExFor:PageSet.__init__(List[PageRange])
        #ExFor:PageRange.__init__(int,int)
        #ExFor:ImageSaveOptions.page_set
        #ExSummary:Shows how to extract pages based on exact page ranges.
        doc = aw.Document(file_name=MY_DIR + "Images.docx")
        image_options = aw.saving.ImageSaveOptions(aw.SaveFormat.TIFF)
        page_set = aw.saving.PageSet(ranges=[aw.saving.PageRange(1, 1), aw.saving.PageRange(2, 3), aw.saving.PageRange(1, 3), aw.saving.PageRange(2, 4), aw.saving.PageRange(1, 1)])
        image_options.page_set = page_set
        doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.ExportVariousPageRanges.tiff", save_options=image_options)
        #ExEnd

    def test_render_ink_object(self):
        #ExStart
        #ExFor:SaveOptions.iml_rendering_mode
        #ExFor:ImlRenderingMode
        #ExSummary:Shows how to render Ink object.
        doc = aw.Document(file_name=MY_DIR + "Ink object.docx")
        # Set 'ImlRenderingMode.InkML' ignores fall-back shape of ink (InkML) object and renders InkML itself.
        # If the rendering result is unsatisfactory,
        # please use 'ImlRenderingMode.Fallback' to get a result similar to previous versions.
        save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.JPEG)
        save_options.iml_rendering_mode = aw.saving.ImlRenderingMode.INK_ML
        doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.RenderInkObject.jpeg", save_options=save_options)
        #ExEnd
