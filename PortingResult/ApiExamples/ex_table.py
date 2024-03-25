# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.drawing
import aspose.words.replacing
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExTable(ApiExampleBase):
    def test_create_table(self):
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)
        first_row = aw.tables.Row(doc)
        table.append_child(first_row)
        first_cell = aw.tables.Cell(doc)
        first_row.append_child(first_cell)
        paragraph = aw.Paragraph(doc)
        first_cell.append_child(paragraph)
        run = aw.Run(doc=doc, text="Hello world!")
        paragraph.append_child(run)
        doc.save(file_name=ARTIFACTS_DIR + "Table.CreateTable.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.CreateTable.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(1, table.rows.count)
        self.assertEqual(1, table.first_row.cells.count)
        self.assertEqual("Hello world!\a\a", table.get_text().strip())

    def test_padding(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
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
        table.preferred_width = aw.tables.PreferredWidth.from_points(250)
        doc.save(file_name=ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(30, table.left_padding)
        self.assertEqual(60, table.right_padding)
        self.assertEqual(10, table.top_padding)
        self.assertEqual(90, table.bottom_padding)

    def test_row_cell_format(self):
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
        row_format = table.first_row.row_format
        row_format.height = 25
        row_format.borders.get_by_border_type(aw.BorderType.BOTTOM).color = aspose.pydrawing.Color.red
        cell_format = table.last_row.first_cell.cell_format
        cell_format.width = 100
        cell_format.shading.background_pattern_color = aspose.pydrawing.Color.orange
        doc.save(file_name=ARTIFACTS_DIR + "Table.RowCellFormat.docx")
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
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)
        self.assertEqual(0, table.get_child_nodes(aw.NodeType.ANY, True).count)
        table.ensure_minimum()
        table.first_row.first_cell.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        self.assertEqual(4, table.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_ensure_row_minimum(self):
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)
        row = aw.tables.Row(doc)
        table.append_child(row)
        self.assertEqual(0, row.get_child_nodes(aw.NodeType.ANY, True).count)
        row.ensure_minimum()
        row.first_cell.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        self.assertEqual(3, row.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_ensure_cell_minimum(self):
        doc = aw.Document()
        table = aw.tables.Table(doc)
        doc.first_section.body.append_child(table)
        row = aw.tables.Row(doc)
        table.append_child(row)
        cell = aw.tables.Cell(doc)
        row.append_child(cell)
        self.assertEqual(0, cell.get_child_nodes(aw.NodeType.ANY, True).count)
        cell.ensure_minimum()
        cell.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        self.assertEqual(2, cell.get_child_nodes(aw.NodeType.ANY, True).count)

    def test_set_outline_borders(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        table.alignment = aw.tables.TableAlignment.CENTER
        table.clear_borders()
        table.clear_shading()
        table.set_border(aw.BorderType.LEFT, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_border(aw.BorderType.RIGHT, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_border(aw.BorderType.TOP, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_border(aw.BorderType.BOTTOM, aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green, True)
        table.set_shading(aw.TextureIndex.TEXTURE_SOLID, aspose.pydrawing.Color.light_green, aspose.pydrawing.Color.empty())
        doc.save(file_name=ARTIFACTS_DIR + "Table.SetOutlineBorders.docx")
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
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        table.clear_borders()
        table.set_borders(aw.LineStyle.SINGLE, 1.5, aspose.pydrawing.Color.green)
        doc.save(file_name=ARTIFACTS_DIR + "Table.SetBorders.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.SetBorders.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.top.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.left.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.right.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.bottom.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.horizontal.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), table.first_row.row_format.borders.vertical.color.to_argb())

    def test_row_format(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        first_row = table.first_row
        first_row.row_format.borders.line_style = aw.LineStyle.NONE
        first_row.row_format.height_rule = aw.HeightRule.AUTO
        first_row.row_format.allow_break_across_pages = True
        doc.save(file_name=ARTIFACTS_DIR + "Table.RowFormat.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.RowFormat.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.LineStyle.NONE, table.first_row.row_format.borders.line_style)
        self.assertEqual(aw.HeightRule.AUTO, table.first_row.row_format.height_rule)
        self.assertTrue(table.first_row.row_format.allow_break_across_pages)

    def test_cell_format(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        first_cell = table.first_row.first_cell
        first_cell.cell_format.width = 30
        first_cell.cell_format.orientation = aw.TextOrientation.DOWNWARD
        first_cell.cell_format.shading.foreground_pattern_color = aspose.pydrawing.Color.light_green
        doc.save(file_name=ARTIFACTS_DIR + "Table.CellFormat.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.CellFormat.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(30, table.first_row.first_cell.cell_format.width)
        self.assertEqual(aw.TextOrientation.DOWNWARD, table.first_row.first_cell.cell_format.orientation)
        self.assertEqual(aspose.pydrawing.Color.light_green.to_argb(), table.first_row.first_cell.cell_format.shading.foreground_pattern_color.to_argb())

    def test_distance_between_table_and_text(self):
        doc = aw.Document(file_name=MY_DIR + "Table wrapped by text.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(25.9, table.distance_top)
        self.assertEqual(25.9, table.distance_bottom)
        self.assertEqual(17.3, table.distance_left)
        self.assertEqual(17.3, table.distance_right)
        table.distance_left = 24
        table.distance_right = 24
        table.distance_top = 3
        table.distance_bottom = 3
        doc.save(file_name=ARTIFACTS_DIR + "Table.DistanceBetweenTableAndText.docx")

    def test_borders(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_replace_cell_text(self):
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
        table.range.replace(pattern="Carrots", replacement="Eggs", options=options)
        table.last_row.last_cell.range.replace(pattern="50", replacement="20", options=options)
        self.assertEqual("Eggs\a50\a\a" + "Potatoes\a20\a\a", table.get_text().strip())

    def test_remove_paragraph_text_and_mark(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_print_table_range(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_clone_table(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        table_clone = table.clone(True).as_table()
        table.parent_node.insert_after(table_clone, table)
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
        doc = aw.Document(file_name=MY_DIR + "Table spanning two pages.docx")
        table = doc.first_section.body.tables[0]
        for cell in table.get_child_nodes(aw.NodeType.CELL, True).of_type():
            for para in cell.paragraphs.of_type():
                self.assertTrue(para.is_in_cell)
                if not (cell.parent_row.is_last_row and para.is_end_of_cell):
                    para.paragraph_format.keep_with_next = True
        doc.save(file_name=ARTIFACTS_DIR + "Table.KeepTableTogether.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.KeepTableTogether.docx")
        table = doc.first_section.body.tables[0]
        for para in table.get_child_nodes(aw.NodeType.PARAGRAPH, True).of_type():
            if para.is_end_of_cell and (para.parent_node.as_cell()).parent_row.is_last_row:
                self.assertFalse(para.paragraph_format.keep_with_next)
            else:
                self.assertTrue(para.paragraph_format.keep_with_next)

    def test_get_index_of_table_elements(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        all_tables = doc.get_child_nodes(aw.NodeType.TABLE, True)
        self.assertEqual(0, all_tables.index_of(table))
        row = table.rows[2]
        self.assertEqual(2, table.index_of(row))
        cell = row.last_cell
        self.assertEqual(4, row.index_of(cell))

    def test_get_preferred_width_type_and_value(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        table = doc.first_section.body.tables[0]
        first_cell = table.first_row.first_cell
        self.assertEqual(aw.tables.PreferredWidthType.PERCENT, first_cell.cell_format.preferred_width.type)
        self.assertEqual(11.16, first_cell.cell_format.preferred_width.value)

    def test_allow_cell_spacing(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_create_nested_table(self):
        raise NotImplementedError("Unsupported call of method named CreateTable")

    def test_check_cells_merged(self):
        raise NotImplementedError("Unsupported call of method named PrintCellMergeType")

    def test_merge_cell_range(self):
        raise NotImplementedError("Unsupported call of method named MergeCells")

    def test_combine_tables(self):
        doc = aw.Document(file_name=MY_DIR + "Tables.docx")
        first_table = doc.first_section.body.tables[0]
        second_table = doc.get_child(aw.NodeType.TABLE, 1, True).as_table()
        while second_table.has_child_nodes:
            first_table.rows.add(second_table.first_row)
        second_table.remove()
        doc.save(file_name=ARTIFACTS_DIR + "Table.CombineTables.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.CombineTables.docx")
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.TABLE, True).count)
        self.assertEqual(9, doc.first_section.body.tables[0].rows.count)
        self.assertEqual(42, doc.first_section.body.tables[0].get_child_nodes(aw.NodeType.CELL, True).count)

    def test_split_table(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_wrap_text(self):
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
        table.text_wrapping = aw.tables.TextWrapping.AROUND
        table.absolute_horizontal_distance = 100
        table.absolute_vertical_distance = 20
        doc.save(file_name=ARTIFACTS_DIR + "Table.WrapText.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Table.WrapText.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aw.tables.TextWrapping.AROUND, table.text_wrapping)
        self.assertEqual(100, table.absolute_horizontal_distance)
        self.assertEqual(20, table.absolute_vertical_distance)

    def test_get_floating_table_properties(self):
        doc = aw.Document(file_name=MY_DIR + "Table wrapped by text.docx")
        table = doc.first_section.body.tables[0]
        if table.text_wrapping == aw.tables.TextWrapping.AROUND:
            self.assertEqual(aw.drawing.RelativeHorizontalPosition.MARGIN, table.horizontal_anchor)
            self.assertEqual(aw.drawing.RelativeVerticalPosition.PARAGRAPH, table.vertical_anchor)
            self.assertEqual(False, table.allow_overlap)
            table.horizontal_anchor = aw.drawing.RelativeHorizontalPosition.COLUMN
            table.vertical_anchor = aw.drawing.RelativeVerticalPosition.PAGE

    def test_change_floating_table_properties(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Table 1, cell 1")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)
        table.relative_vertical_alignment = aw.drawing.VerticalAlignment.BOTTOM
        table.relative_horizontal_alignment = aw.drawing.HorizontalAlignment.RIGHT
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Table 2, cell 1")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)
        table.absolute_vertical_distance = 50
        table.absolute_horizontal_distance = 100
        doc.save(file_name=ARTIFACTS_DIR + "Table.ChangeFloatingTableProperties.docx")
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
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table_style = doc.styles.add(aw.StyleType.TABLE, "MyTableStyle1").as_table_style()
        table_style.alignment = aw.tables.TableAlignment.CENTER
        table_style.borders.color = aspose.pydrawing.Color.blue
        table_style.borders.line_style = aw.LineStyle.SINGLE
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Aligned to the center of the page")
        builder.end_table()
        table.preferred_width = aw.tables.PreferredWidth.from_points(300)
        table.style = table_style
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
