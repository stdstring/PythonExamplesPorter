# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.replacing
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExTable(ApiExampleBase):
    def test_create_table(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_padding(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Row 1, cell 1.")
        builder.insert_cell()
        builder.write("Row 1, cell 2.")
        builder.end_table()
        table.left_padding = 30
        table.right_padding = 60
        table.top_padding = 10
        table.bottom_padding = 90
        table.preferred_width = aspose.words.tables.PreferredWidth.from_points(250)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(30, table.left_padding)
        self.assertEqual(60, table.right_padding)
        self.assertEqual(10, table.top_padding)
        self.assertEqual(90, table.bottom_padding)

    def test_row_cell_format(self):
        raise NotImplementedError("Unsupported type of expression: BorderType.Bottom")

    def test_display_content_of_tables(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Tables.Table[] for expression: tables.ToArray()")

    def test_calculate_depth_of_nested_tables(self):
        raise NotImplementedError("Unsupported call of method named GetChildTableCount")

    def test_ensure_table_minimum(self):
        doc = aspose.words.Document()
        table = aspose.words.tables.Table(doc)
        doc.first_section.body.append_child(table)
        self.assertEqual(0, table.get_child_nodes(aspose.words.NodeType.ANY, True).count)
        table.ensure_minimum()
        table.first_row.first_cell.first_paragraph.append_child(aspose.words.Run(doc = doc, text = "Hello world!"))
        self.assertEqual(4, table.get_child_nodes(aspose.words.NodeType.ANY, True).count)

    def test_ensure_row_minimum(self):
        doc = aspose.words.Document()
        table = aspose.words.tables.Table(doc)
        doc.first_section.body.append_child(table)
        row = aspose.words.tables.Row(doc)
        table.append_child(row)
        self.assertEqual(0, row.get_child_nodes(aspose.words.NodeType.ANY, True).count)
        row.ensure_minimum()
        row.first_cell.first_paragraph.append_child(aspose.words.Run(doc = doc, text = "Hello world!"))
        self.assertEqual(3, row.get_child_nodes(aspose.words.NodeType.ANY, True).count)

    def test_ensure_cell_minimum(self):
        doc = aspose.words.Document()
        table = aspose.words.tables.Table(doc)
        doc.first_section.body.append_child(table)
        row = aspose.words.tables.Row(doc)
        table.append_child(row)
        cell = aspose.words.tables.Cell(doc)
        row.append_child(cell)
        self.assertEqual(0, cell.get_child_nodes(aspose.words.NodeType.ANY, True).count)
        cell.ensure_minimum()
        cell.first_paragraph.append_child(aspose.words.Run(doc = doc, text = "Hello world!"))
        self.assertEqual(2, cell.get_child_nodes(aspose.words.NodeType.ANY, True).count)

    def test_set_outline_borders(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_set_borders(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_row_format(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_cell_format(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_distance_between_table_and_text(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Table wrapped by text.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(25.9, table.distance_top)
        self.assertEqual(25.9, table.distance_bottom)
        self.assertEqual(17.3, table.distance_left)
        self.assertEqual(17.3, table.distance_right)
        table.distance_left = 24
        table.distance_right = 24
        table.distance_top = 3
        table.distance_bottom = 3
        doc.save(file_name = ARTIFACTS_DIR + "Table.DistanceBetweenTableAndText.docx")

    def test_borders(self):
        raise NotImplementedError("Unsupported type of expression: BorderType.Top")

    def test_replace_cell_text(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_print_table_range(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_clone_table(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_keep_table_together(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_get_index_of_table_elements(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        all_tables = doc.get_child_nodes(aspose.words.NodeType.TABLE, True)
        self.assertEqual(0, all_tables.index_of(table))
        row = table.rows[2]
        self.assertEqual(2, table.index_of(row))
        cell = row.last_cell
        self.assertEqual(4, row.index_of(cell))

    def test_get_preferred_width_type_and_value(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        first_cell = table.first_row.first_cell
        self.assertEqual(aspose.words.tables.PreferredWidthType.PERCENT, first_cell.cell_format.preferred_width.type)
        self.assertEqual(11.16, first_cell.cell_format.preferred_width.value)

    def test_create_nested_table(self):
        raise NotImplementedError("Unsupported call of method named CreateTable")

    def test_check_cells_merged(self):
        raise NotImplementedError("Unsupported call of method named PrintCellMergeType")

    def test_merge_cell_range(self):
        raise NotImplementedError("Unsupported call of method named MergeCells")

    def test_combine_tables(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Tables.docx")
        first_table = doc.first_section.body.tables[0]
        second_table = doc.get_child(aspose.words.NodeType.TABLE, 1, True).as_table()
        # while begin
        while second_table.has_child_nodes:
            first_table.rows.add(second_table.first_row)
        # while end
        second_table.remove()
        doc.save(file_name = ARTIFACTS_DIR + "Table.CombineTables.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Table.CombineTables.docx")
        self.assertEqual(1, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)
        self.assertEqual(9, doc.first_section.body.tables[0].rows.count)
        self.assertEqual(42, doc.first_section.body.tables[0].get_child_nodes(aspose.words.NodeType.CELL, True).count)

    def test_split_table(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_wrap_text(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Cell 1")
        builder.insert_cell()
        builder.write("Cell 2")
        builder.end_table()
        table.preferred_width = aspose.words.tables.PreferredWidth.from_points(300)
        builder.font.size = 16
        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        table.text_wrapping = aspose.words.tables.TextWrapping.AROUND
        table.absolute_horizontal_distance = 100
        table.absolute_vertical_distance = 20
        doc.save(file_name = ARTIFACTS_DIR + "Table.WrapText.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Table.WrapText.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aspose.words.tables.TextWrapping.AROUND, table.text_wrapping)
        self.assertEqual(100, table.absolute_horizontal_distance)
        self.assertEqual(20, table.absolute_vertical_distance)

    def test_get_floating_table_properties(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Table wrapped by text.docx")
        table = doc.first_section.body.tables[0]
        # if begin
        if table.text_wrapping == aspose.words.tables.TextWrapping.AROUND:
            self.assertEqual(aspose.words.drawing.RelativeHorizontalPosition.MARGIN, table.horizontal_anchor)
            self.assertEqual(aspose.words.drawing.RelativeVerticalPosition.PARAGRAPH, table.vertical_anchor)
            self.assertEqual(False, table.allow_overlap)
            table.horizontal_anchor = aspose.words.drawing.RelativeHorizontalPosition.COLUMN
            table.vertical_anchor = aspose.words.drawing.RelativeVerticalPosition.PAGE
        # if end

    def test_change_floating_table_properties(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Table 1, cell 1")
        builder.end_table()
        table.preferred_width = aspose.words.tables.PreferredWidth.from_points(300)
        table.relative_vertical_alignment = aspose.words.drawing.VerticalAlignment.BOTTOM
        table.relative_horizontal_alignment = aspose.words.drawing.HorizontalAlignment.RIGHT
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Table 2, cell 1")
        builder.end_table()
        table.preferred_width = aspose.words.tables.PreferredWidth.from_points(300)
        table.absolute_vertical_distance = 50
        table.absolute_horizontal_distance = 100
        doc.save(file_name = ARTIFACTS_DIR + "Table.ChangeFloatingTableProperties.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Table.ChangeFloatingTableProperties.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aspose.words.drawing.VerticalAlignment.BOTTOM, table.relative_vertical_alignment)
        self.assertEqual(aspose.words.drawing.HorizontalAlignment.RIGHT, table.relative_horizontal_alignment)
        table = doc.get_child(aspose.words.NodeType.TABLE, 1, True).as_table()
        self.assertEqual(50, table.absolute_vertical_distance)
        self.assertEqual(100, table.absolute_horizontal_distance)

    def test_table_style_creation(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_set_table_alignment(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_conditional_styles(self):
        raise NotImplementedError("Unsupported type of expression: ConditionalStyleType.FirstRow")

    def test_clear_table_style_formatting(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_alternating_row_styles(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_convert_to_horizontally_merged_cells(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_get_text_from_cells(self):
        raise NotImplementedError("Unsupported target type System.Console")
