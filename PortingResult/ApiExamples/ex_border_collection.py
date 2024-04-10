# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.pydrawing
import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExBorderCollection(ApiExampleBase):
    def test_get_borders_enumerator(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_remove_all_borders(self):
        #ExStart
        #ExFor:BorderCollection.clear_formatting
        #ExSummary:Shows how to remove all borders from all paragraphs in a document.
        doc = aw.Document(file_name=MY_DIR + "Borders.docx")

        # The first paragraph of this document has visible borders with these settings.
        first_paragraph_borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), first_paragraph_borders.color.to_argb())
        self.assertEqual(aw.LineStyle.SINGLE, first_paragraph_borders.line_style)
        self.assertEqual(3, first_paragraph_borders.line_width)

        # Use the "ClearFormatting" method on each paragraph to remove all borders.
        for paragraph in doc.first_section.body.paragraphs:
            paragraph = paragraph.as_paragraph()
            paragraph.paragraph_format.borders.clear_formatting()
            for border in paragraph.paragraph_format.borders:
                self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), border.color.to_argb())
                self.assertEqual(aw.LineStyle.NONE, border.line_style)
                self.assertEqual(0, border.line_width)
        doc.save(file_name=ARTIFACTS_DIR + "BorderCollection.RemoveAllBorders.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "BorderCollection.RemoveAllBorders.docx")
        for border in doc.first_section.body.first_paragraph.paragraph_format.borders:
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), border.color.to_argb())
            self.assertEqual(aw.LineStyle.NONE, border.line_style)
            self.assertEqual(0, border.line_width)
