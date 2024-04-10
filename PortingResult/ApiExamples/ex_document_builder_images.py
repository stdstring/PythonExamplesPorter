# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.words as aw
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
        #ExStart
        #ExFor:DocumentBuilder.insert_image(string)
        #ExSummary:Shows how to determine which image will be inserted.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(file_name=IMAGE_DIR + "Scalable Vector Graphics.svg")

        # Aspose.Words insert SVG image to the document as PNG with svgBlip extension
        # that contains the original vector SVG image representation.
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBuilderImages.InsertSvgImage.SvgWithSvgBlip.docx")

        # Aspose.Words insert SVG image to the document as PNG, just like Microsoft Word does for old format.
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBuilderImages.InsertSvgImage.Svg.doc")
        doc.compatibility_options.optimize_for(aw.settings.MsWordVersion.WORD2003)

        # Aspose.Words insert SVG image to the document as EMF metafile to keep the image in vector representation.
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBuilderImages.InsertSvgImage.Emf.docx")
        #ExEnd

    def test_insert_image_from_byte_array(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_insert_gif(self):
        raise NotImplementedError("Unsupported target type System.IO.File")
