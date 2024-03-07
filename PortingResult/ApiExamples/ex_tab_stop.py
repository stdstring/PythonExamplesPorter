# -*- coding: utf-8 -*-
import aspose.words
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
        doc = aspose.words.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops
        tab_stops.add(position=aspose.words.ConvertUtil.millimeter_to_point(30), alignment=aspose.words.TabAlignment.LEFT, leader=aspose.words.TabLeader.DASHES)
        tab_stops.add(position=aspose.words.ConvertUtil.millimeter_to_point(60), alignment=aspose.words.TabAlignment.LEFT, leader=aspose.words.TabLeader.DASHES)
        self.assertAlmostEqual(aspose.words.ConvertUtil.millimeter_to_point(60), tab_stops.get_position_by_index(1), delta=0.1)

    def test_get_index_by_position(self):
        doc = aspose.words.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops
        tab_stops.add(position=aspose.words.ConvertUtil.millimeter_to_point(30), alignment=aspose.words.TabAlignment.LEFT, leader=aspose.words.TabLeader.DASHES)
        self.assertEqual(0, tab_stops.get_index_by_position(aspose.words.ConvertUtil.millimeter_to_point(30)))
        self.assertEqual(-1, tab_stops.get_index_by_position(aspose.words.ConvertUtil.millimeter_to_point(60)))
