# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.layout
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExLayout(ApiExampleBase):
    def test_layout_collector(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_layout_enumerator(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_restart_page_numbering_in_continuous_section(self):
        doc = aw.Document(file_name=MY_DIR + "Continuous section page numbering.docx")
        doc.layout_options.continuous_section_page_numbering_restart = aw.layout.ContinuousSectionRestart.FROM_NEW_PAGE_ONLY
        doc.update_page_layout()
        doc.save(file_name=ARTIFACTS_DIR + "Layout.RestartPageNumberingInContinuousSection.pdf")
