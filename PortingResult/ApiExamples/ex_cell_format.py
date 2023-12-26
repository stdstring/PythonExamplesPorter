# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExCellFormat(ApiExampleBase):
    def test_vertical_merge(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_horizontal_merge(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_padding(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.cell_format.set_paddings(5, 10, 40, 50)
        builder.start_table()
        builder.insert_cell()
        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        doc.save(file_name = ARTIFACTS_DIR + "CellFormat.Padding.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "CellFormat.Padding.docx")
        table = doc.first_section.body.tables[0]
        cell = table.rows[0].cells[0]
        self.assertEqual(5, cell.cell_format.left_padding)
        self.assertEqual(10, cell.cell_format.top_padding)
        self.assertEqual(40, cell.cell_format.right_padding)
        self.assertEqual(50, cell.cell_format.bottom_padding)
