# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExSvgSaveOptions(ApiExampleBase):
    def test_save_like_image(self):
        #ExStart
        #ExFor:SvgSaveOptions.fit_to_view_port
        #ExFor:SvgSaveOptions.show_page_border
        #ExFor:SvgSaveOptions.text_output_mode
        #ExFor:SvgTextOutputMode
        #ExSummary:Shows how to mimic the properties of images when converting a .docx document to .svg.
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        # Configure the SvgSaveOptions object to save with no page borders or selectable text.
        options = aw.saving.SvgSaveOptions()
        options.fit_to_view_port = True
        options.show_page_border = False
        options.text_output_mode = aw.saving.SvgTextOutputMode.USE_PLACED_GLYPHS
        doc.save(file_name=ARTIFACTS_DIR + "SvgSaveOptions.SaveLikeImage.svg", save_options=options)
        #ExEnd

    def test_save_office_math(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_max_image_resolution(self):
        #ExStart:MaxImageResolution
        #ExFor:ShapeBase.soft_edge
        #ExFor:SoftEdgeFormat.radius
        #ExFor:SoftEdgeFormat.remove
        #ExFor:SvgSaveOptions.max_image_resolution
        #ExSummary:Shows how to set limit for image resolution.
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        save_options = aw.saving.SvgSaveOptions()
        save_options.max_image_resolution = 72
        doc.save(file_name=ARTIFACTS_DIR + "SvgSaveOptions.MaxImageResolution.svg", save_options=save_options)
        #ExEnd:MaxImageResolution
