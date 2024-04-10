# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExTabStop(ApiExampleBase):
    def test_add_tab_stops(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_tab_stop_collection(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_remove_by_index(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_get_position_by_index(self):
        #ExStart
        #ExFor:TabStopCollection.get_position_by_index
        #ExSummary:Shows how to find a tab, stop by its index and verify its position.
        doc = aw.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops
        tab_stops.add(position=aw.ConvertUtil.millimeter_to_point(30), alignment=aw.TabAlignment.LEFT, leader=aw.TabLeader.DASHES)
        tab_stops.add(position=aw.ConvertUtil.millimeter_to_point(60), alignment=aw.TabAlignment.LEFT, leader=aw.TabLeader.DASHES)

        # Verify the position of the second tab stop in the collection.
        self.assertAlmostEqual(aw.ConvertUtil.millimeter_to_point(60), tab_stops.get_position_by_index(1), delta=0.1)
        #ExEnd

    def test_get_index_by_position(self):
        #ExStart
        #ExFor:TabStopCollection.get_index_by_position
        #ExSummary:Shows how to look up a position to see if a tab stop exists there and obtain its index.
        doc = aw.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops

        # Add a tab stop at a position of 30mm.
        tab_stops.add(position=aw.ConvertUtil.millimeter_to_point(30), alignment=aw.TabAlignment.LEFT, leader=aw.TabLeader.DASHES)

        # A result of "0" returned by "GetIndexByPosition" confirms that a tab stop
        # at 30mm exists in this collection, and it is at index 0.
        self.assertEqual(0, tab_stops.get_index_by_position(aw.ConvertUtil.millimeter_to_point(30)))

        # A "-1" returned by "GetIndexByPosition" confirms that
        # there is no tab stop in this collection with a position of 60mm.
        self.assertEqual(-1, tab_stops.get_index_by_position(aw.ConvertUtil.millimeter_to_point(60)))
        #ExEnd
