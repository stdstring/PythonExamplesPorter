# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExBorderCollection(ApiExampleBase):
    def test_get_borders_enumerator(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_remove_all_borders(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Borders.docx")
        first_paragraph_borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), first_paragraph_borders.color.to_argb())
        self.assertEqual(aspose.words.LineStyle.SINGLE, first_paragraph_borders.line_style)
        self.assertEqual(3, first_paragraph_borders.line_width)
        for paragraph in doc.first_section.body.paragraphs:
            paragraph = paragraph.as_paragraph()
            paragraph.paragraph_format.borders.clear_formatting()
            for border in paragraph.paragraph_format.borders:
                self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), border.color.to_argb())
                self.assertEqual(aspose.words.LineStyle.NONE, border.line_style)
                self.assertEqual(0, border.line_width)
        doc.save(file_name=ARTIFACTS_DIR + "BorderCollection.RemoveAllBorders.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "BorderCollection.RemoveAllBorders.docx")
        for border in doc.first_section.body.first_paragraph.paragraph_format.borders:
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), border.color.to_argb())
            self.assertEqual(aspose.words.LineStyle.NONE, border.line_style)
            self.assertEqual(0, border.line_width)
