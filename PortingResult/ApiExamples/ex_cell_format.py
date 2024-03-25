# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExCellFormat(ApiExampleBase):
    def test_vertical_merge(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_cell()
        builder.cell_format.vertical_merge = aw.tables.CellMerge.FIRST
        builder.write("Text in merged cells.")
        builder.insert_cell()
        builder.cell_format.vertical_merge = aw.tables.CellMerge.NONE
        builder.write("Text in unmerged cell.")
        builder.end_row()
        builder.insert_cell()
        builder.cell_format.vertical_merge = aw.tables.CellMerge.PREVIOUS
        builder.insert_cell()
        builder.cell_format.vertical_merge = aw.tables.CellMerge.NONE
        builder.write("Text in unmerged cell.")
        builder.end_row()
        builder.end_table()
        doc.save(file_name=ARTIFACTS_DIR + "CellFormat.VerticalMerge.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "CellFormat.VerticalMerge.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.tables.CellMerge.FIRST, table.rows[0].cells[0].cell_format.vertical_merge)
        self.assertEqual(aw.tables.CellMerge.PREVIOUS, table.rows[1].cells[0].cell_format.vertical_merge)
        self.assertEqual("Text in merged cells.", table.rows[0].cells[0].get_text().strip("\a"))
        self.assertNotEqual(table.rows[0].cells[0].get_text(), table.rows[1].cells[0].get_text())

    def test_horizontal_merge(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_cell()
        builder.cell_format.horizontal_merge = aw.tables.CellMerge.FIRST
        builder.write("Text in merged cells.")
        builder.insert_cell()
        builder.cell_format.horizontal_merge = aw.tables.CellMerge.PREVIOUS
        builder.end_row()
        builder.cell_format.horizontal_merge = aw.tables.CellMerge.NONE
        builder.insert_cell()
        builder.write("Text in unmerged cell.")
        builder.insert_cell()
        builder.write("Text in unmerged cell.")
        builder.end_row()
        builder.end_table()
        doc.save(file_name=ARTIFACTS_DIR + "CellFormat.HorizontalMerge.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "CellFormat.HorizontalMerge.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(1, table.rows[0].cells.count)
        self.assertEqual(aw.tables.CellMerge.NONE, table.rows[0].cells[0].cell_format.horizontal_merge)
        self.assertEqual("Text in merged cells.", table.rows[0].cells[0].get_text().strip("\a"))

    def test_padding(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.cell_format.set_paddings(5, 10, 40, 50)
        builder.start_table()
        builder.insert_cell()
        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        doc.save(file_name=ARTIFACTS_DIR + "CellFormat.Padding.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "CellFormat.Padding.docx")
        table = doc.first_section.body.tables[0]
        cell = table.rows[0].cells[0]
        self.assertEqual(5, cell.cell_format.left_padding)
        self.assertEqual(10, cell.cell_format.top_padding)
        self.assertEqual(40, cell.cell_format.right_padding)
        self.assertEqual(50, cell.cell_format.bottom_padding)
