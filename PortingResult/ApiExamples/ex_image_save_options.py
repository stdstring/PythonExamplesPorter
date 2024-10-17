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
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExImageSaveOptions(ApiExampleBase):
    def test_one_page(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_renderer(self):
        for use_gdi_emf_renderer in [False, True]:
            #ExStart
            #ExFor:ImageSaveOptions.use_gdi_emf_renderer
            #ExSummary:Shows how to choose a renderer when converting a document to .emf.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.paragraph_format.style = doc.styles.get_by_name("Heading 1")
            builder.writeln("Hello world!")
            builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            # When we save the document as an EMF image, we can pass a SaveOptions object to select a renderer for the image.
            # If we set the "UseGdiEmfRenderer" flag to "true", Aspose.Words will use the GDI+ renderer.
            # If we set the "UseGdiEmfRenderer" flag to "false", Aspose.Words will use its own metafile renderer.
            save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.EMF)
            save_options.use_gdi_emf_renderer = use_gdi_emf_renderer
            doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.Renderer.emf", save_options=save_options)
            #ExEnd

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
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_page_by_page(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_color_mode(self):
        for image_color_mode in [aw.saving.ImageColorMode.BLACK_AND_WHITE,
                                 aw.saving.ImageColorMode.GRAYSCALE,
                                 aw.saving.ImageColorMode.NONE]:
            #ExStart
            #ExFor:ImageColorMode
            #ExFor:ImageSaveOptions.image_color_mode
            #ExSummary:Shows how to set a color mode when rendering documents.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.paragraph_format.style = doc.styles.get_by_name("Heading 1")
            builder.writeln("Hello world!")
            builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            # When we save the document as an image, we can pass a SaveOptions object to
            # select a color mode for the image that the saving operation will generate.
            # If we set the "ImageColorMode" property to "ImageColorMode.BlackAndWhite",
            # the saving operation will apply grayscale color reduction while rendering the document.
            # If we set the "ImageColorMode" property to "ImageColorMode.Grayscale",
            # the saving operation will render the document into a monochrome image.
            # If we set the "ImageColorMode" property to "None", the saving operation will apply the default method
            # and preserve all the document's colors in the output image.
            image_save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)
            image_save_options.image_color_mode = image_color_mode
            doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.ColorMode.png", save_options=image_save_options)
            #ExEnd
            tested_image_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "ImageSaveOptions.ColorMode.png").length()
            switch_condition = image_color_mode
            if switch_condition == aw.saving.ImageColorMode.NONE:
                self.assertTrue(tested_image_length < 175000)
            elif switch_condition == aw.saving.ImageColorMode.GRAYSCALE:
                self.assertTrue(tested_image_length < 90000)
            elif switch_condition == aw.saving.ImageColorMode.BLACK_AND_WHITE:
                self.assertTrue(tested_image_length < 15000)

    def test_paper_color(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_pixel_format(self):
        for image_pixel_format in [aw.saving.ImagePixelFormat.FORMAT_1BPP_INDEXED,
                                   aw.saving.ImagePixelFormat.FORMAT_16BPP_RGB_555,
                                   aw.saving.ImagePixelFormat.FORMAT_16BPP_RGB_565,
                                   aw.saving.ImagePixelFormat.FORMAT_24BPP_RGB,
                                   aw.saving.ImagePixelFormat.FORMAT_32BPP_RGB,
                                   aw.saving.ImagePixelFormat.FORMAT_32BPP_ARGB,
                                   aw.saving.ImagePixelFormat.FORMAT_32BPP_P_ARGB,
                                   aw.saving.ImagePixelFormat.FORMAT_48BPP_RGB,
                                   aw.saving.ImagePixelFormat.FORMAT_64BPP_ARGB,
                                   aw.saving.ImagePixelFormat.FORMAT_64BPP_P_ARGB]:
            #ExStart
            #ExFor:ImagePixelFormat
            #ExFor:ImageSaveOptions.clone
            #ExFor:ImageSaveOptions.pixel_format
            #ExSummary:Shows how to select a bit-per-pixel rate with which to render a document to an image.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.paragraph_format.style = doc.styles.get_by_name("Heading 1")
            builder.writeln("Hello world!")
            builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            # When we save the document as an image, we can pass a SaveOptions object to
            # select a pixel format for the image that the saving operation will generate.
            # Various bit per pixel rates will affect the quality and file size of the generated image.
            image_save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)
            image_save_options.pixel_format = image_pixel_format
            # We can clone ImageSaveOptions instances.
            self.assertNotEqual(image_save_options, image_save_options.clone())
            doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.PixelFormat.png", save_options=image_save_options)
            #ExEnd
            tested_image_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "ImageSaveOptions.PixelFormat.png").length()
            switch_condition = image_pixel_format
            if switch_condition == aw.saving.ImagePixelFormat.FORMAT_1BPP_INDEXED:
                self.assertTrue(tested_image_length < 2500)
            elif switch_condition == aw.saving.ImagePixelFormat.FORMAT_16BPP_RGB_565:
                self.assertTrue(tested_image_length < 104000)
            elif switch_condition == aw.saving.ImagePixelFormat.FORMAT_16BPP_RGB_555:
                self.assertTrue(tested_image_length < 88000)
            elif switch_condition == aw.saving.ImagePixelFormat.FORMAT_24BPP_RGB:
                self.assertTrue(tested_image_length < 160000)
            elif (switch_condition == aw.saving.ImagePixelFormat.FORMAT_32BPP_RGB) and (switch_condition == aw.saving.ImagePixelFormat.FORMAT_32BPP_ARGB):
                self.assertTrue(tested_image_length < 175000)
            elif switch_condition == aw.saving.ImagePixelFormat.FORMAT_48BPP_RGB:
                self.assertTrue(tested_image_length < 212000)
            elif (switch_condition == aw.saving.ImagePixelFormat.FORMAT_64BPP_ARGB) and (switch_condition == aw.saving.ImagePixelFormat.FORMAT_64BPP_P_ARGB):
                self.assertTrue(tested_image_length < 239000)

    def test_floyd_steinberg_dithering(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_edit_image(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_jpeg_quality(self):
        #ExStart
        #ExFor:Document.save(str,SaveOptions)
        #ExFor:FixedPageSaveOptions.jpeg_quality
        #ExFor:ImageSaveOptions
        #ExFor:ImageSaveOptions.__init__
        #ExFor:ImageSaveOptions.jpeg_quality
        #ExSummary:Shows how to configure compression while saving a document as a JPEG.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
        # Create an "ImageSaveOptions" object which we can pass to the document's "Save" method
        # to modify the way in which that method renders the document into an image.
        image_options = aw.saving.ImageSaveOptions(aw.SaveFormat.JPEG)
        # Set the "JpegQuality" property to "10" to use stronger compression when rendering the document.
        # This will reduce the file size of the document, but the image will display more prominent compression artifacts.
        image_options.jpeg_quality = 10
        doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.JpegQuality.HighCompression.jpg", save_options=image_options)
        # Set the "JpegQuality" property to "100" to use weaker compression when rending the document.
        # This will improve the quality of the image at the cost of an increased file size.
        image_options.jpeg_quality = 100
        doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.JpegQuality.HighQuality.jpg", save_options=image_options)
        #ExEnd
        self.assertTrue(system_helper.io.FileInfo(ARTIFACTS_DIR + "ImageSaveOptions.JpegQuality.HighCompression.jpg").length() < 18000)
        self.assertTrue(system_helper.io.FileInfo(ARTIFACTS_DIR + "ImageSaveOptions.JpegQuality.HighQuality.jpg").length() < 75000)

    def test_tiff_image_compression(self):
        for tiff_compression in [aw.saving.TiffCompression.NONE,
                                 aw.saving.TiffCompression.RLE,
                                 aw.saving.TiffCompression.LZW,
                                 aw.saving.TiffCompression.CCITT3,
                                 aw.saving.TiffCompression.CCITT4]:
            #ExStart
            #ExFor:TiffCompression
            #ExFor:ImageSaveOptions.tiff_compression
            #ExSummary:Shows how to select the compression scheme to apply to a document that we convert into a TIFF image.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            # Create an "ImageSaveOptions" object which we can pass to the document's "Save" method
            # to modify the way in which that method renders the document into an image.
            options = aw.saving.ImageSaveOptions(aw.SaveFormat.TIFF)
            # Set the "TiffCompression" property to "TiffCompression.None" to apply no compression while saving,
            # which may result in a very large output file.
            # Set the "TiffCompression" property to "TiffCompression.Rle" to apply RLE compression
            # Set the "TiffCompression" property to "TiffCompression.Lzw" to apply LZW compression.
            # Set the "TiffCompression" property to "TiffCompression.Ccitt3" to apply CCITT3 compression.
            # Set the "TiffCompression" property to "TiffCompression.Ccitt4" to apply CCITT4 compression.
            options.tiff_compression = tiff_compression
            doc.save(file_name=ARTIFACTS_DIR + "ImageSaveOptions.TiffImageCompression.tiff", save_options=options)
            #ExEnd
            tested_image_length = system_helper.io.FileInfo(ARTIFACTS_DIR + "ImageSaveOptions.TiffImageCompression.tiff").length()
            switch_condition = tiff_compression
            if switch_condition == aw.saving.TiffCompression.NONE:
                self.assertTrue(tested_image_length < 3450000)
            elif switch_condition == aw.saving.TiffCompression.RLE:
                self.assertTrue(tested_image_length < 687000)
            elif switch_condition == aw.saving.TiffCompression.LZW:
                self.assertTrue(tested_image_length < 250000)
            elif switch_condition == aw.saving.TiffCompression.CCITT3:
                self.assertTrue(tested_image_length < 8300)
            elif switch_condition == aw.saving.TiffCompression.CCITT4:
                self.assertTrue(tested_image_length < 1700)

    def test_resolution(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_export_various_page_ranges(self):
        #ExStart
        #ExFor:PageSet.__init__(List[PageRange])
        #ExFor:PageRange
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
