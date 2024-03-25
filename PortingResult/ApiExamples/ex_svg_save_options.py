# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExSvgSaveOptions(ApiExampleBase):
    def test_save_like_image(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        options = aw.saving.SvgSaveOptions()
        options.fit_to_view_port = True
        options.show_page_border = False
        options.text_output_mode = aw.saving.SvgTextOutputMode.USE_PLACED_GLYPHS
        doc.save(file_name=ARTIFACTS_DIR + "SvgSaveOptions.SaveLikeImage.svg", save_options=options)

    def test_save_office_math(self):
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        math = doc.get_child(aw.NodeType.OFFICE_MATH, 0, True).as_office_math()
        options = aw.saving.SvgSaveOptions()
        options.text_output_mode = aw.saving.SvgTextOutputMode.USE_PLACED_GLYPHS
        math.get_math_renderer().save(file_name=ARTIFACTS_DIR + "SvgSaveOptions.Output.svg", save_options=options)
