# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.layout
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExLayout(ApiExampleBase):
    def test_layout_collector(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_layout_enumerator(self):
        raise NotImplementedError("ignored method body")

    def test_restart_page_numbering_in_continuous_section(self):
        #ExStart
        #ExFor:LayoutOptions.continuous_section_page_numbering_restart
        #ExFor:ContinuousSectionRestart
        #ExSummary:Shows how to control page numbering in a continuous section.
        doc = aw.Document(file_name=MY_DIR + "Continuous section page numbering.docx")
        # By default Aspose.Words behavior matches the Microsoft Word 2019.
        # If you need old Aspose.Words behavior, repetitive Microsoft Word 2016, use 'ContinuousSectionRestart.FromNewPageOnly'.
        # Page numbering restarts only if there is no other content before the section on the page where the section starts,
        # because of that the numbering will reset to 2 from the second page.
        doc.layout_options.continuous_section_page_numbering_restart = aw.layout.ContinuousSectionRestart.FROM_NEW_PAGE_ONLY
        doc.update_page_layout()
        doc.save(file_name=ARTIFACTS_DIR + "Layout.RestartPageNumberingInContinuousSection.pdf")
        #ExEnd
