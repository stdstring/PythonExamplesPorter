# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExThemes(ApiExampleBase):
    def test_custom_colors_and_fonts(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Theme colors.docx")
        theme = doc.theme
        theme.major_fonts.latin = "Courier New"
        theme.minor_fonts.latin = "Agency FB"
        self.assertEqual("", theme.major_fonts.complex_script)
        self.assertEqual("", theme.major_fonts.east_asian)
        self.assertEqual("", theme.minor_fonts.complex_script)
        self.assertEqual("", theme.minor_fonts.east_asian)
        colors = theme.colors
        colors.dark1 = aspose.pydrawing.Color.midnight_blue
        colors.light1 = aspose.pydrawing.Color.pale_green
        colors.dark2 = aspose.pydrawing.Color.indigo
        colors.light2 = aspose.pydrawing.Color.khaki
        colors.accent1 = aspose.pydrawing.Color.orange_red
        colors.accent2 = aspose.pydrawing.Color.light_salmon
        colors.accent3 = aspose.pydrawing.Color.yellow
        colors.accent4 = aspose.pydrawing.Color.gold
        colors.accent5 = aspose.pydrawing.Color.blue_violet
        colors.accent6 = aspose.pydrawing.Color.dark_violet
        colors.hyperlink = aspose.pydrawing.Color.black
        colors.followed_hyperlink = aspose.pydrawing.Color.gray
        doc.save(file_name=ARTIFACTS_DIR + "Themes.CustomColorsAndFonts.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Themes.CustomColorsAndFonts.docx")
        self.assertEqual(aspose.pydrawing.Color.orange_red.to_argb(), doc.theme.colors.accent1.to_argb())
        self.assertEqual(aspose.pydrawing.Color.midnight_blue.to_argb(), doc.theme.colors.dark1.to_argb())
        self.assertEqual(aspose.pydrawing.Color.gray.to_argb(), doc.theme.colors.followed_hyperlink.to_argb())
        self.assertEqual(aspose.pydrawing.Color.black.to_argb(), doc.theme.colors.hyperlink.to_argb())
        self.assertEqual(aspose.pydrawing.Color.pale_green.to_argb(), doc.theme.colors.light1.to_argb())
        self.assertEqual("", doc.theme.major_fonts.complex_script)
        self.assertEqual("", doc.theme.major_fonts.east_asian)
        self.assertEqual("Courier New", doc.theme.major_fonts.latin)
        self.assertEqual("", doc.theme.minor_fonts.complex_script)
        self.assertEqual("", doc.theme.minor_fonts.east_asian)
        self.assertEqual("Agency FB", doc.theme.minor_fonts.latin)
