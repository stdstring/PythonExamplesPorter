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
        #ExStart
        #ExFor:LayoutCollector
        #ExFor:LayoutCollector.__init__(Document)
        #ExFor:LayoutCollector.clear
        #ExFor:LayoutCollector.document
        #ExFor:LayoutCollector.get_end_page_index(Node)
        #ExFor:LayoutCollector.get_entity(Node)
        #ExFor:LayoutCollector.get_num_pages_spanned(Node)
        #ExFor:LayoutCollector.get_start_page_index(Node)
        #ExFor:LayoutEnumerator.current
        #ExSummary:Shows how to see the the ranges of pages that a node spans.
        doc = aw.Document()
        layout_collector = aw.layout.LayoutCollector(doc)
        # Call the "GetNumPagesSpanned" method to count how many pages the content of our document spans.
        # Since the document is empty, that number of pages is currently zero.
        self.assertEqual(doc, layout_collector.document)
        self.assertEqual(0, layout_collector.get_num_pages_spanned(doc))
        # Populate the document with 5 pages of content.
        builder = aw.DocumentBuilder(doc)
        builder.write("Section 1")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.insert_break(aw.BreakType.SECTION_BREAK_EVEN_PAGE)
        builder.write("Section 2")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        # Before the layout collector, we need to call the "UpdatePageLayout" method to give us
        # an accurate figure for any layout-related metric, such as the page count.
        self.assertEqual(0, layout_collector.get_num_pages_spanned(doc))
        layout_collector.clear()
        doc.update_page_layout()
        self.assertEqual(5, layout_collector.get_num_pages_spanned(doc))
        # We can see the numbers of the start and end pages of any node and their overall page spans.
        nodes = doc.get_child_nodes(aw.NodeType.ANY, True)
        for node in nodes:
            print(f"->  NodeType.{node.node_type}: ")
            print(f"\tStarts on page {layout_collector.get_start_page_index(node)}, ends on page {layout_collector.get_end_page_index(node)}," + f" spanning {layout_collector.get_num_pages_spanned(node)} pages.")
        # We can iterate over the layout entities using a LayoutEnumerator.
        layout_enumerator = aw.layout.LayoutEnumerator(doc)
        self.assertEqual(aw.layout.LayoutEntityType.PAGE, layout_enumerator.type)
        # The LayoutEnumerator can traverse the collection of layout entities like a tree.
        # We can also apply it to any node's corresponding layout entity.
        layout_enumerator.current = layout_collector.get_entity(doc.get_child(aw.NodeType.PARAGRAPH, 1, True))
        self.assertEqual(aw.layout.LayoutEntityType.SPAN, layout_enumerator.type)
        self.assertEqual("¶", layout_enumerator.text)
        #ExEnd

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
