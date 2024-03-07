# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.settings
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExViewOptions(ApiExampleBase):
    def test_set_zoom_percentage(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.view_options.view_type = aspose.words.settings.ViewType.PAGE_LAYOUT
        doc.view_options.zoom_percent = 50
        self.assertEqual(aspose.words.settings.ZoomType.CUSTOM, doc.view_options.zoom_type)
        self.assertEqual(aspose.words.settings.ZoomType.NONE, doc.view_options.zoom_type)
        doc.save(file_name=ARTIFACTS_DIR + "ViewOptions.SetZoomPercentage.doc")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "ViewOptions.SetZoomPercentage.doc")
        self.assertEqual(aspose.words.settings.ViewType.PAGE_LAYOUT, doc.view_options.view_type)
        self.assertEqual(50, doc.view_options.zoom_percent)
        self.assertEqual(aspose.words.settings.ZoomType.NONE, doc.view_options.zoom_type)
