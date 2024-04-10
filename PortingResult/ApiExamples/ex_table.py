# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.pydrawing
import aspose.words as aw
import aspose.words.drawing
import aspose.words.replacing
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExTable(ApiExampleBase):
    def test_create_table(self):
        #ExStart
        #ExFor:Table
        #ExFor:Row
        #ExFor:Cell
        #ExFor:Table.__init__(DocumentBase)
        #ExSummary:Shows how to create a table.
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)

        # Tables contain rows, which contain cells, which may have paragraphs
        # with typical elements such as runs, shapes, and even other tables.
        # Calling the "EnsureMinimum" method on a table will ensure that
        # the table has at least one row, cell, and paragraph.
        first_row = aw.tables.Row(doc)
        table.append_child(first_row)
        first_cell = aw.tables.Cell(doc)
        first_row.append_child(first_cell)
        paragraph = aw.Paragraph(doc)
        first_cell.append_child(paragraph)

        # Add text to the first cell in the first row of the table.
        run = aw.Run(doc=doc, text="Hello world!")
        paragraph.append_child(run)
        doc.save(file_name=ARTIFACTS_DIR + "Table.CreateTable.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.CreateTable.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(1, table.rows.count)
        self.assertEqual(1, table.first_row.cells.count)
        self.assertEqual("Hello world!\a\a", table.get_text().strip())

    def test_padding(self):
        #ExStart
        #ExFor:Table.left_padding
        #ExFor:Table.right_padding
        #ExFor:Table.top_padding
        #ExFor:Table.bottom_padding
        #ExSummary:Shows how to configure content padding in a table.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Row 1, cell 1.")
        builder.insert_cell()
        builder.write("Row 1, cell 2.")
        builder.end_table()

        # For every cell in the table, set the distance between its contents and each of its borders.
        # This table will maintain the minimum padding distance by wrapping text.
        table.left_padding = 30
        table.right_padding = 60
        table.top_padding = 10
        table.bottom_padding = 90
        table.preferred_width = aw.tables.PreferredWidth.from_points(250)
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(30, table.left_padding)
        self.assertEqual(60, table.right_padding)
        self.assertEqual(10, table.top_padding)
        self.assertEqual(90, table.bottom_padding)

    def test_row_cell_format(self):
        #ExStart
        #ExFor:Row.row_format
        #ExFor:RowFormat
        #ExFor:Cell.cell_format
        #ExFor:CellFormat
        #ExFor:CellFormat.shading
        #ExSummary:Shows how to modify the format of rows and cells in a table.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("City")
        builder.insert_cell()
        builder.write("Country")
        builder.end_row()
        builder.insert_cell()
        builder.write("London")
        builder.insert_cell()
        builder.write("U.K.")
        builder.end_table()

        # Use the first row's "RowFormat" property to modify the formatting
        # of the contents of all cells in this row.
        row_format = table.first_row.row_format
        row_format.height = 25
        row_format.borders.get_by_border_type(aw.BorderType.BOTTOM).color = aspose.pydrawing.Color.red

        # Use the "CellFormat" property of the first cell in the last row to modify the formatting of that cell's contents.
        cell_format = table.last_row.first_cell.cell_format
        cell_format.width = 100
        cell_format.shading.background_pattern_color = aspose.pydrawing.Color.orange
        doc.save(file_name=ARTIFACTS_DIR + "Table.RowCellFormat.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.RowCellFormat.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual("City\aCountry\a\aLondon\aU.K.\a\a", table.get_text().strip())
        row_format = table.first_row.row_format
        self.assertEqual(25, row_format.height)
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), row_format.borders.get_by_border_type(aw.BorderType.BOTTOM).color.to_argb())
        cell_format = table.last_row.first_cell.cell_format
        self.assertEqual(110.8, cell_format.width)
        self.assertEqual(aspose.pydrawing.Color.orange.to_argb(), cell_format.shading.background_pattern_color.to_argb())

    def test_display_content_of_tables(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Tables.Table[] for expression: tables.ToArray()")

    def test_calculate_depth_of_nested_tables(self):
        raise NotImplementedError("Unsupported call of method named GetChildTableCount")

    def test_ensure_table_minimum(self):
        #ExStart
        #ExFor:Table.ensure_minimum
        #ExSummary:Shows how to ensure that a table node contains the nodes we need to add content.
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)

        # Tables contain rows, which contain cells, which may contain paragraphs
        # with typical elements such as runs, shapes, and even other tables.
        # Our new table has none of these nodes, and we cannot add contents to it until it does.
        self.assertEqual(0, table.get_child_nodes(aw.NodeType.ANY, True).count)

        # Calling the "EnsureMinimum" method on a table will ensure that
        # the table has at least one row and one cell with an empty paragraph.
        table.ensure_minimum()
        table.first_row.first_cell.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        #ExEnd

        self.assertEqual(4, table.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_ensure_row_minimum(self):
        #ExStart
        #ExFor:Row.ensure_minimum
        #ExSummary:Shows how to ensure a row node contains the nodes we need to begin adding content to it.
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)
        row = aw.tables.Row(doc)
        table.append_child(row)

        # Rows contain cells, containing paragraphs with typical elements such as runs, shapes, and even other tables.
        # Our new row has none of these nodes, and we cannot add contents to it until it does.
        self.assertEqual(0, row.get_child_nodes(aw.NodeType.ANY, True).count)

        # Calling the "EnsureMinimum" method on a table will ensure that
        # the table has at least one cell with an empty paragraph.
        row.ensure_minimum()
        row.first_cell.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        #ExEnd

        self.assertEqual(3, row.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_ensure_cell_minimum(self):
        #ExStart
        #ExFor:Cell.ensure_minimum
        #ExSummary:Shows how to ensure a cell node contains the nodes we need to begin adding content to it.
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)
        row = aw.tables.Row(doc)
        table.append_child(row)
        cell = aw.tables.Cell(doc)
        row.append_child(cell)

        # Cells may contain paragraphs with typical elements such as runs, shapes, and even other tables.
        # Our new cell does not have any paragraphs, and we cannot add contents such as run and shape nodes to it until it does.
        self.assertEqual(0, cell.get_child_nodes(aw.NodeType.ANY, True).count)

        # Calling the "EnsureMinimum" method on a cell will ensure that
        # the cell has at least one empty paragraph, which we can then add contents to.
        cell.ensure_minimum()
        cell.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        #ExEnd

        self.assertEqual(2, cell.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_set_outline_borders(self):
        #ExStart
        #ExFor:Table.alignment
        #ExFor:TableAlignment
        #ExFor:Table.clear_borders
        #ExFor:Table.clear_shading
        #ExFor:Table.set_border
        #ExFor:TextureIndex
        #ExFor:Table.set_shading
        #ExSummary:Shows how to apply an outline border to a table.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]

        # Align the table to the center of the page.
        table.alignment = aw.tables.TableAlignment.CENTER

        # Clear any existing borders and shading from the table.
        table.clear_borders()
        table.clear_shading()

        # Add green borders to the outline of the table.
        table.set_border(aw.BorderType.LEFT, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_border(aw.BorderType.RIGHT, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_border(aw.BorderType.TOP, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_border(aw.BorderType.BOTTOM, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)

        # Fill the cells with a light green solid color.
        table.set_shading(aw.TextureIndex.TEXTURE_SOLID, aspose.pydrawing.Color.light_green, aspose.pydrawing.Color.empty())
        doc.save(file_name=ARTIFACTS_DIR + "Table.SetOutlineBorders.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.SetOutlineBorders.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.tables.TableAlignment.CENTER, table.alignment)
        borders = table.first_row.row_format.borders
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), borders.top.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), borders.left.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), borders.right.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), borders.bottom.color.to_argb())
        self.assertNotEqual(aspose.pydrawing.Color.green.to_argb(), borders.horizontal.color.to_argb())
        self.assertNotEqual(aspose.pydrawing.Color.green.to_argb(), borders.vertical.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.light_green.to_argb(), table.first_row.first_cell.cell_format.shading.foreground_pattern_color.to_argb())

    def test_set_borders(self):
        #ExStart
        #ExFor:Table.set_borders
        #ExSummary:Shows how to format of all of a table's borders at once.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]

        # Clear all existing borders from the table.
        table.clear_borders()

        # Set a single green line to serve as every outer and inner border of this table.
        table.set_borders(aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green)
        doc.save(file_name=ARTIFACTS_DIR + "Table.SetBorders.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.SetBorders.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.top.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.left.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.right.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.bottom.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.horizontal.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.vertical.color.to_argb())

    def test_row_format(self):
        #ExStart
        #ExFor:RowFormat
        #ExFor:Row.row_format
        #ExSummary:Shows how to modify formatting of a table row.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]

        # Use the first row's "RowFormat" property to set formatting that modifies that entire row's appearance.
        first_row = table.first_row
        first_row.row_format.borders.line_style = aw.LineStyle.NONE
        first_row.row_format.height_rule = aw.HeightRule.AUTO
        first_row.row_format.allow_break_across_pages = True
        doc.save(file_name=ARTIFACTS_DIR + "Table.RowFormat.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.RowFormat.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.LineStyle.NONE, table.first_row.row_format.borders.line_style)
        self.assertEqual(aw.HeightRule.AUTO, table.first_row.row_format.height_rule)
        self.assertTrue(table.first_row.row_format.allow_break_across_pages)

    def test_cell_format(self):
        #ExStart
        #ExFor:CellFormat
        #ExFor:Cell.cell_format
        #ExSummary:Shows how to modify formatting of a table cell.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        first_cell = table.first_row.first_cell

        # Use a cell's "CellFormat" property to set formatting that modifies the appearance of that cell.
        first_cell.cell_format.width = 30
        first_cell.cell_format.orientation = aw.TextOrientation.DOWNWARD
        first_cell.cell_format.shading.foreground_pattern_color = aspose.pydrawing.Color.light_green
        doc.save(file_name=ARTIFACTS_DIR + "Table.CellFormat.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.CellFormat.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(30, table.first_row.first_cell.cell_format.width)
        self.assertEqual(aw.TextOrientation.DOWNWARD, table.first_row.first_cell.cell_format.orientation)
        self.assertEqual(aspose.pydrawing.Color.light_green.to_argb(), table.first_row.first_cell.cell_format.shading.foreground_pattern_color.to_argb())

    def test_distance_between_table_and_text(self):
        #ExStart
        #ExFor:Table.distance_bottom
        #ExFor:Table.distance_left
        #ExFor:Table.distance_right
        #ExFor:Table.distance_top
        #ExSummary:Shows how to set distance between table boundaries and text.
        doc = aw.Document(file_name=MY_DIR + "Table wrapped by text.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(25.9, table.distance_top)
        self.assertEqual(25.9, table.distance_bottom)
        self.assertEqual(17.3, table.distance_left)
        self.assertEqual(17.3, table.distance_right)

        # Set distance between table and surrounding text.
        table.distance_left = 24
        table.distance_right = 24
        table.distance_top = 3
        table.distance_bottom = 3
        doc.save(file_name=ARTIFACTS_DIR + "Table.DistanceBetweenTableAndText.docx")
        #ExEnd

    def test_borders(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_replace_cell_text(self):
        #ExStart
        #ExFor:Range.replace(string,string,FindReplaceOptions)
        #ExSummary:Shows how to replace all instances of String of text in a table and cell.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Carrots")
        builder.insert_cell()
        builder.write("50")
        builder.end_row()
        builder.insert_cell()
        builder.write("Potatoes")
        builder.insert_cell()
        builder.write("50")
        builder.end_table()
        options = aw.replacing.FindReplaceOptions()
        options.match_case = True
        options.find_whole_words_only = True

        # Perform a find-and-replace operation on an entire table.
        table.range.replace(pattern="Carrots", replacement="Eggs", options=options)

        # Perform a find-and-replace operation on the last cell of the last row of the table.
        table.last_row.last_cell.range.replace(pattern="50", replacement="20", options=options)
        self.assertEqual("Eggs\a50\a\a" + "Potatoes\a20\a\a", table.get_text().strip())
        #ExEnd

    def test_remove_paragraph_text_and_mark(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_print_table_range(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_clone_table(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        table_clone = table.clone(True).as_table()

        # Insert the cloned table into the document after the original.
        table.parent_node.insert_after(table_clone, table)

        # Insert an empty paragraph between the two tables.
        table.parent_node.insert_after(aw.Paragraph(doc), table)
        doc.save(file_name=ARTIFACTS_DIR + "Table.CloneTable.doc")
        self.assertEqual(3, doc.get_child_nodes(aw.NodeType.TABLE, True).count)
        self.assertEqual(table.range.text, table_clone.range.text)
        for cell in table_clone.get_child_nodes(aw.NodeType.CELL, True).of_type():
            cell.remove_all_children()
        self.assertEqual("", table_clone.to_string(save_format=aw.SaveFormat.TEXT).strip())

    def test_allow_break_across_pages(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_allow_auto_fit_on_table(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_keep_table_together(self):
        #ExStart
        #ExFor:ParagraphFormat.keep_with_next
        #ExFor:Row.is_last_row
        #ExFor:Paragraph.is_end_of_cell
        #ExFor:Paragraph.is_in_cell
        #ExFor:Cell.parent_row
        #ExFor:Cell.paragraphs
        #ExSummary:Shows how to set a table to stay together on the same page.
        doc = aw.Document(file_name=MY_DIR + "Table spanning two pages.docx")
        table = doc.first_section.body.tables[0]

        # Enabling KeepWithNext for every paragraph in the table except for the
        # last ones in the last row will prevent the table from splitting across multiple pages.
        for cell in table.get_child_nodes(aw.NodeType.CELL, True).of_type():
            for para in cell.paragraphs.of_type():
                self.assertTrue(para.is_in_cell)
                if not (cell.parent_row.is_last_row and para.is_end_of_cell):
                    para.paragraph_format.keep_with_next = True
        doc.save(file_name=ARTIFACTS_DIR + "Table.KeepTableTogether.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.KeepTableTogether.docx")
        table = doc.first_section.body.tables[0]
        for para in table.get_child_nodes(aw.NodeType.PARAGRAPH, True).of_type():
            if para.is_end_of_cell and (para.parent_node.as_cell()).parent_row.is_last_row:
                self.assertFalse(para.paragraph_format.keep_with_next)
            else:
                self.assertTrue(para.paragraph_format.keep_with_next)

    def test_get_index_of_table_elements(self):
        #ExStart
        #ExFor:NodeCollection.index_of(Node)
        #ExSummary:Shows how to get the index of a node in a collection.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        all_tables = doc.get_child_nodes(aw.NodeType.TABLE, True)
        self.assertEqual(0, all_tables.index_of(table))
        row = table.rows[2]
        self.assertEqual(2, table.index_of(row))
        cell = row.last_cell
        self.assertEqual(4, row.index_of(cell))
        #ExEnd

    def test_get_preferred_width_type_and_value(self):
        #ExStart
        #ExFor:PreferredWidthType
        #ExFor:PreferredWidth.type
        #ExFor:PreferredWidth.value
        #ExSummary:Shows how to verify the preferred width type and value of a table cell.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        first_cell = table.first_row.first_cell
        self.assertEqual(aw.tables.PreferredWidthType.PERCENT, first_cell.cell_format.preferred_width.type)
        self.assertEqual(11.16, first_cell.cell_format.preferred_width.value)
        #ExEnd

    def test_allow_cell_spacing(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_create_nested_table(self):
        raise NotImplementedError("Unsupported call of method named CreateTable")

    def test_check_cells_merged(self):
        raise NotImplementedError("Unsupported call of method named PrintCellMergeType")

    def test_merge_cell_range(self):
        raise NotImplementedError("Unsupported call of method named MergeCells")

    def test_combine_tables(self):
        #ExStart
        #ExFor:Cell.cell_format
        #ExFor:CellFormat.borders
        #ExFor:Table.rows
        #ExFor:Table.first_row
        #ExFor:CellFormat.clear_formatting
        #ExFor:CompositeNode.has_child_nodes
        #ExSummary:Shows how to combine the rows from two tables into one.
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")

        # Below are two ways of getting a table from a document.
        # 1 -  From the "Tables" collection of a Body node:
        first_table = doc.first_section.body.tables[0]

        # 2 -  Using the "GetChild" method:
        second_table = doc.get_child(aw.NodeType.TABLE, 1, True).as_table()

        # Append all rows from the current table to the next.
        while second_table.has_child_nodes:
            first_table.rows.add(second_table.first_row)

        # Remove the empty table container.
        second_table.remove()
        doc.save(file_name=ARTIFACTS_DIR + "Table.CombineTables.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.CombineTables.docx")
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.TABLE, True).count)
        self.assertEqual(9, doc.first_section.body.tables[0].rows.count)
        self.assertEqual(42, doc.first_section.body.tables[0].get_child_nodes(aw.NodeType.CELL, True).count)

    def test_split_table(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_wrap_text(self):
        #ExStart
        #ExFor:Table.text_wrapping
        #ExFor:TextWrapping
        #ExSummary:Shows how to work with table text wrapping.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Cell 1")
        builder.insert_cell()
        builder.write("Cell 2")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)
        builder.font.size = 16
        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

        # Set the "TextWrapping" property to "TextWrapping.Around" to get the table to wrap text around it,
        # and push it down into the paragraph below by setting the position.
        table.text_wrapping = aw.tables.TextWrapping.AROUND
        table.absolute_horizontal_distance = 100
        table.absolute_vertical_distance = 20
        doc.save(file_name=ARTIFACTS_DIR + "Table.WrapText.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.WrapText.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.tables.TextWrapping.AROUND, table.text_wrapping)
        self.assertEqual(100, table.absolute_horizontal_distance)
        self.assertEqual(20, table.absolute_vertical_distance)

    def test_get_floating_table_properties(self):
        #ExStart
        #ExFor:Table.horizontal_anchor
        #ExFor:Table.vertical_anchor
        #ExFor:Table.allow_overlap
        #ExFor:ShapeBase.allow_overlap
        #ExSummary:Shows how to work with floating tables properties.
        doc = aw.Document(file_name=MY_DIR + "Table wrapped by text.docx")
        table = doc.first_section.body.tables[0]
        if table.text_wrapping == aw.tables.TextWrapping.AROUND:
            self.assertEqual(aw.drawing.RelativeHorizontalPosition.MARGIN, table.horizontal_anchor)
            self.assertEqual(aw.drawing.RelativeVerticalPosition.PARAGRAPH, table.vertical_anchor)
            self.assertEqual(False, table.allow_overlap)

        # Only Margin, Page, Column available in RelativeHorizontalPosition for HorizontalAnchor setter.
        # The ArgumentException will be thrown for any other values.
            table.horizontal_anchor = aw.drawing.RelativeHorizontalPosition.COLUMN

        # Only Margin, Page, Paragraph available in RelativeVerticalPosition for VerticalAnchor setter.
        # The ArgumentException will be thrown for any other values.
            table.vertical_anchor = aw.drawing.RelativeVerticalPosition.PAGE
        #ExEnd
        #ExEnd

    def test_change_floating_table_properties(self):
        #ExStart
        #ExFor:Table.relative_horizontal_alignment
        #ExFor:Table.relative_vertical_alignment
        #ExFor:Table.absolute_horizontal_distance
        #ExFor:Table.absolute_vertical_distance
        #ExSummary:Shows how set the location of floating tables.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Table 1, cell 1")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)

        # Set the table's location to a place on the page, such as, in this case, the bottom right corner.
        table.relative_vertical_alignment = aw.drawing.VerticalAlignment.BOTTOM
        table.relative_horizontal_alignment = aw.drawing.HorizontalAlignment.RIGHT
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Table 2, cell 1")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)

        # We can also set a horizontal and vertical offset in points from the paragraph's location where we inserted the table.
        table.absolute_vertical_distance = 50
        table.absolute_horizontal_distance = 100
        doc.save(file_name=ARTIFACTS_DIR + "Table.ChangeFloatingTableProperties.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.ChangeFloatingTableProperties.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.drawing.VerticalAlignment.BOTTOM, table.relative_vertical_alignment)
        self.assertEqual(aw.drawing.HorizontalAlignment.RIGHT, table.relative_horizontal_alignment)
        table = doc.get_child(aw.NodeType.TABLE, 1, True).as_table()
        self.assertEqual(50, table.absolute_vertical_distance)
        self.assertEqual(100, table.absolute_horizontal_distance)

    def test_table_style_creation(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_set_table_alignment(self):
        #ExStart
        #ExFor:TableStyle.alignment
        #ExFor:TableStyle.left_indent
        #ExSummary:Shows how to set the position of a table.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Below are two ways of aligning a table horizontally.
        # 1 -  Use the "Alignment" property to align it to a location on the page, such as the center:
        table_style = doc.styles.add(aw.StyleType.TABLE, "MyTableStyle1").as_table_style()
        table_style.alignment = aw.tables.TableAlignment.CENTER
        table_style.borders.color = aspose.pydrawing.Color.blue
        table_style.borders.line_style = aw.LineStyle.SINGLE

        # Insert a table and apply the style we created to it.
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Aligned to the center of the page")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)
        table.style = table_style

        # 2 -  Use the "LeftIndent" to specify an indent from the left margin of the page:
        table_style = doc.styles.add(aw.StyleType.TABLE, "MyTableStyle2").as_table_style()
        table_style.left_indent = 55
        table_style.borders.color = aspose.pydrawing.Color.green
        table_style.borders.line_style = aw.LineStyle.SINGLE
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Aligned according to left indent")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)
        table.style = table_style
        doc.save(file_name=ARTIFACTS_DIR + "Table.SetTableAlignment.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.SetTableAlignment.docx")
        table_style = doc.styles.get_by_name("MyTableStyle1").as_table_style()
        self.assertEqual(aw.tables.TableAlignment.CENTER, table_style.alignment)
        self.assertEqual(table_style, doc.first_section.body.tables[0].style)
        table_style = doc.styles.get_by_name("MyTableStyle2").as_table_style()
        self.assertEqual(55, table_style.left_indent)
        self.assertEqual(table_style, (doc.get_child(aw.NodeType.TABLE, 1, True).as_table()).style)

    def test_conditional_styles(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_clear_table_style_formatting(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_alternating_row_styles(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_convert_to_horizontally_merged_cells(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_get_text_from_cells(self):
        raise NotImplementedError("Unsupported target type System.Console")
