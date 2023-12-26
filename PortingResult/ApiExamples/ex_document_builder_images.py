# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.settings
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR


class ExDocumentBuilderImages(ApiExampleBase):
    def test_insert_image_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_image_from_filename(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_svg_image(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_image(file_name = IMAGE_DIR + "Scalable Vector Graphics.svg")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilderImages.InsertSvgImage.SvgWithSvgBlip.docx")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilderImages.InsertSvgImage.Svg.doc")
        doc.compatibility_options.optimize_for(aspose.words.settings.MsWordVersion.WORD2003)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilderImages.InsertSvgImage.Emf.docx")

    def test_insert_image_from_byte_array(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Image")

    def test_insert_gif(self):
        raise NotImplementedError("Unsupported target type System.IO.File")
