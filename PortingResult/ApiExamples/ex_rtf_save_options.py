# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.drawing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExRtfSaveOptions(ApiExampleBase):
    def test_export_images(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_save_images_as_wmf(self):
        for save_images_as_wmf in [False, True]:
            #ExStart
            #ExFor:RtfSaveOptions.save_images_as_wmf
            #ExSummary:Shows how to convert all images in a document to the Windows Metafile format as we save the document as an RTF.
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc=doc)
            builder.writeln("Jpeg image:")
            image_shape = builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
            self.assertEqual(aw.drawing.ImageType.JPEG, image_shape.image_data.image_type)
            builder.insert_paragraph()
            builder.writeln("Png image:")
            image_shape = builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
            self.assertEqual(aw.drawing.ImageType.PNG, image_shape.image_data.image_type)
            # Create an "RtfSaveOptions" object to pass to the document's "Save" method to modify how we save it to an RTF.
            rtf_save_options = aw.saving.RtfSaveOptions()
            # Set the "SaveImagesAsWmf" property to "true" to convert all images in the document to WMF as we save it to RTF.
            # Doing so will help readers such as WordPad to read our document.
            # Set the "SaveImagesAsWmf" property to "false" to preserve the original format of all images in the document
            # as we save it to RTF. This will preserve the quality of the images at the cost of compatibility with older RTF readers.
            rtf_save_options.save_images_as_wmf = save_images_as_wmf
            doc.save(file_name=ARTIFACTS_DIR + "RtfSaveOptions.SaveImagesAsWmf.rtf", save_options=rtf_save_options)
            doc = aw.Document(file_name=ARTIFACTS_DIR + "RtfSaveOptions.SaveImagesAsWmf.rtf")
            shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
            if save_images_as_wmf:
                self.assertEqual(aw.drawing.ImageType.WMF, (shapes[0].as_shape()).image_data.image_type)
                self.assertEqual(aw.drawing.ImageType.WMF, (shapes[1].as_shape()).image_data.image_type)
            else:
                self.assertEqual(aw.drawing.ImageType.JPEG, (shapes[0].as_shape()).image_data.image_type)
                self.assertEqual(aw.drawing.ImageType.PNG, (shapes[1].as_shape()).image_data.image_type)
            #ExEnd
