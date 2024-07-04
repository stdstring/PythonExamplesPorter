# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.settings
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExViewOptions(ApiExampleBase):
    def test_set_zoom_percentage(self):
        #ExStart
        #ExFor:Document.view_options
        #ExFor:ViewOptions
        #ExFor:ViewOptions.view_type
        #ExFor:ViewOptions.zoom_percent
        #ExFor:ViewOptions.zoom_type
        #ExFor:ViewType
        #ExSummary:Shows how to set a custom zoom factor, which older versions of Microsoft Word will apply to a document upon loading.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.view_options.view_type = aw.settings.ViewType.PAGE_LAYOUT
        doc.view_options.zoom_percent = 50
        self.assertEqual(aw.settings.ZoomType.CUSTOM, doc.view_options.zoom_type)
        self.assertEqual(aw.settings.ZoomType.NONE, doc.view_options.zoom_type)
        doc.save(file_name=ARTIFACTS_DIR + "ViewOptions.SetZoomPercentage.doc")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "ViewOptions.SetZoomPercentage.doc")
        self.assertEqual(aw.settings.ViewType.PAGE_LAYOUT, doc.view_options.view_type)
        self.assertEqual(50, doc.view_options.zoom_percent)
        self.assertEqual(aw.settings.ZoomType.NONE, doc.view_options.zoom_type)

    def test_set_zoom_type(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_display_background_shape(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_display_page_boundaries(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_forms_design(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")
