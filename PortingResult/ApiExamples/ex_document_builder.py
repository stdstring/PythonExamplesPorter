# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.drawing
import aspose.words.drawing.charts
import aspose.words.fields
import aspose.words.notes
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, IMAGE_URL, MY_DIR


class ExDocumentBuilder(ApiExampleBase):
    def test_write_and_font(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_headers_and_footers(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.page_setup.different_first_page_header_footer = True
        builder.page_setup.odd_and_even_pages_header_footer = True
        builder.move_to_header_footer(aspose.words.HeaderFooterType.HEADER_FIRST)
        builder.write("Header for the first page")
        builder.move_to_header_footer(aspose.words.HeaderFooterType.HEADER_EVEN)
        builder.write("Header for even pages")
        builder.move_to_header_footer(aspose.words.HeaderFooterType.HEADER_PRIMARY)
        builder.write("Header for all other pages")
        builder.move_to_section(0)
        builder.writeln("Page1")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.writeln("Page2")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.writeln("Page3")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.HeadersAndFooters.docx")
        headers_footers = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.HeadersAndFooters.docx").first_section.headers_footers
        self.assertEqual(3, headers_footers.count)
        self.assertEqual("Header for the first page", headers_footers.get_by_header_footer_type(aspose.words.HeaderFooterType.HEADER_FIRST).get_text().strip())
        self.assertEqual("Header for even pages", headers_footers.get_by_header_footer_type(aspose.words.HeaderFooterType.HEADER_EVEN).get_text().strip())
        self.assertEqual("Header for all other pages", headers_footers.get_by_header_footer_type(aspose.words.HeaderFooterType.HEADER_PRIMARY).get_text().strip())

    def test_merge_fields(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_horizontal_rule(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_horizontal_rule_format_exceptions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_insert_hyperlink_async(self):
        raise NotImplementedError("Unsupported expression: AwaitExpression")

    def test_push_pop_font(self):
        raise NotImplementedError("Unsupported expression: AwaitExpression")

    def test_insert_ole_object(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_html(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        html = "<p align='right'>Paragraph right</p>" + "<b>Implicit paragraph left</b>" + "<div align='center'>Div center</div>" + "<h1 align='left'>Heading 1 left.</h1>"
        builder.insert_html(html = html)
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual("Paragraph right", paragraphs[0].get_text().strip())
        self.assertEqual(aspose.words.ParagraphAlignment.RIGHT, paragraphs[0].paragraph_format.alignment)
        self.assertEqual("Implicit paragraph left", paragraphs[1].get_text().strip())
        self.assertEqual(aspose.words.ParagraphAlignment.LEFT, paragraphs[1].paragraph_format.alignment)
        self.assertTrue(paragraphs[1].runs[0].font.bold)
        self.assertEqual("Div center", paragraphs[2].get_text().strip())
        self.assertEqual(aspose.words.ParagraphAlignment.CENTER, paragraphs[2].paragraph_format.alignment)
        self.assertEqual("Heading 1 left.", paragraphs[3].get_text().strip())
        self.assertEqual("Heading 1", paragraphs[3].paragraph_format.style.name)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertHtml.docx")

    def test_math_ml(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_text_and_bookmark(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_bookmark("MyBookmark")
        builder.writeln("Hello world!")
        builder.end_bookmark("MyBookmark")
        self.assertEqual(1, doc.range.bookmarks.count)
        self.assertEqual("MyBookmark", doc.range.bookmarks[0].name)
        self.assertEqual("Hello world!", doc.range.bookmarks[0].text.strip())

    def test_create_column_bookmark(self):
        raise NotImplementedError("Unsupported expression: TypeOfExpression")

    def test_create_form(self):
        builder = aspose.words.DocumentBuilder()
        builder.insert_text_input("My text input", aspose.words.fields.TextFormFieldType.REGULAR, "", "Enter your name here", 30)
        items = ["-- Select your favorite footwear --", "Sneakers", "Oxfords", "Flip-flops", "Other"]
        builder.insert_paragraph()
        builder.insert_combo_box("My combo box", items, 0)
        builder.document.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.CreateForm.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.CreateForm.docx")
        form_field = doc.range.form_fields[0]
        self.assertEqual("My text input", form_field.name)
        self.assertEqual(aspose.words.fields.TextFormFieldType.REGULAR, form_field.text_input_type)
        self.assertEqual("Enter your name here", form_field.result)
        form_field = doc.range.form_fields[1]
        self.assertEqual("My combo box", form_field.name)
        self.assertEqual(aspose.words.fields.TextFormFieldType.REGULAR, form_field.text_input_type)
        self.assertEqual("-- Select your favorite footwear --", form_field.result)
        self.assertEqual(0, form_field.drop_down_selected_index)
        self.assertSequenceEqual(["-- Select your favorite footwear --", "Sneakers", "Oxfords", "Flip-flops", "Other"], form_field.drop_down_items.to_array())

    def test_insert_check_box(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Unchecked check box of a default size: ")
        builder.insert_check_box(name = "", default_value = False, checked_value = False, size = 0)
        builder.insert_paragraph()
        builder.write("Large checked check box: ")
        builder.insert_check_box(name = "CheckBox_Default", default_value = True, checked_value = True, size = 50)
        builder.insert_paragraph()
        builder.write("Very large checked check box: ")
        builder.insert_check_box(name = "CheckBox_OnlyCheckedValue", checked_value = True, size = 100)
        self.assertEqual("CheckBox_OnlyChecked", doc.range.form_fields[2].name)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertCheckBox.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertCheckBox.docx")
        form_fields = doc.range.form_fields
        self.assertEqual("", form_fields[0].name)
        self.assertEqual(False, form_fields[0].checked)
        self.assertEqual(False, form_fields[0].default)
        self.assertEqual(10, form_fields[0].check_box_size)
        self.assertEqual("CheckBox_Default", form_fields[1].name)
        self.assertEqual(True, form_fields[1].checked)
        self.assertEqual(True, form_fields[1].default)
        self.assertEqual(50, form_fields[1].check_box_size)
        self.assertEqual("CheckBox_OnlyChecked", form_fields[2].name)
        self.assertEqual(True, form_fields[2].checked)
        self.assertEqual(True, form_fields[2].default)
        self.assertEqual(100, form_fields[2].check_box_size)

    def test_insert_check_box_empty_name(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_check_box(name = "", default_value = True, checked_value = False, size = 1)
        builder.insert_check_box(name = "", checked_value = False, size = 1)

    def test_working_with_nodes(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_bookmark("MyBookmark")
        builder.write("Bookmark contents.")
        builder.end_bookmark("MyBookmark")
        first_paragraph_nodes = doc.first_section.body.first_paragraph.get_child_nodes(aspose.words.NodeType.ANY, False)
        self.assertEqual(aspose.words.NodeType.BOOKMARK_START, first_paragraph_nodes[0].node_type)
        self.assertEqual(aspose.words.NodeType.RUN, first_paragraph_nodes[1].node_type)
        self.assertEqual("Bookmark contents.", first_paragraph_nodes[1].get_text().strip())
        self.assertEqual(aspose.words.NodeType.BOOKMARK_END, first_paragraph_nodes[2].node_type)
        self.assertIsNone(builder.current_node)
        builder.move_to_bookmark(bookmark_name = "MyBookmark")
        self.assertEqual(first_paragraph_nodes[1], builder.current_node)
        builder.move_to(doc.first_section.body.first_paragraph.get_child_nodes(aspose.words.NodeType.ANY, False)[0])
        self.assertEqual(aspose.words.NodeType.BOOKMARK_START, builder.current_node.node_type)
        self.assertEqual(doc.first_section.body.first_paragraph, builder.current_paragraph)
        self.assertTrue(builder.is_at_start_of_paragraph)
        builder.move_to_document_end()
        self.assertTrue(builder.is_at_end_of_paragraph)
        builder.move_to_document_start()
        self.assertTrue(builder.is_at_start_of_paragraph)

    def test_fill_merge_fields(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_field(field_code = " MERGEFIELD Chairman ")
        builder.insert_field(field_code = " MERGEFIELD ChiefFinancialOfficer ")
        builder.insert_field(field_code = " MERGEFIELD ChiefTechnologyOfficer ")
        builder.move_to_merge_field(field_name = "Chairman")
        builder.bold = True
        builder.writeln("John Doe")
        builder.move_to_merge_field(field_name = "ChiefFinancialOfficer")
        builder.italic = True
        builder.writeln("Jane Doe")
        builder.move_to_merge_field(field_name = "ChiefTechnologyOfficer")
        builder.italic = True
        builder.writeln("John Bloggs")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.FillMergeFields.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.FillMergeFields.docx")
        paragraphs = doc.first_section.body.paragraphs
        self.assertTrue(paragraphs[0].runs[0].font.bold)
        self.assertEqual("John Doe", paragraphs[0].runs[0].get_text().strip())
        self.assertTrue(paragraphs[1].runs[0].font.italic)
        self.assertEqual("Jane Doe", paragraphs[1].runs[0].get_text().strip())
        self.assertTrue(paragraphs[2].runs[0].font.italic)
        self.assertEqual("John Bloggs", paragraphs[2].runs[0].get_text().strip())

    def test_insert_toc(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_table_of_contents("\\o \"1-3\" \\h \\z \\u")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING1
        builder.writeln("Heading 1")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING2
        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING1
        builder.writeln("Heading 2")
        builder.writeln("Heading 3")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING2
        builder.writeln("Heading 3.1")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING3
        builder.writeln("Heading 3.1.1")
        builder.writeln("Heading 3.1.2")
        builder.writeln("Heading 3.1.3")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING4
        builder.writeln("Heading 3.1.3.1")
        builder.writeln("Heading 3.1.3.2")
        builder.paragraph_format.style_identifier = aspose.words.StyleIdentifier.HEADING2
        builder.writeln("Heading 3.2")
        builder.writeln("Heading 3.3")
        doc.update_fields()
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertToc.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertToc.docx")
        table_of_contents = doc.range.fields[0].as_field_toc()
        self.assertEqual("1-3", table_of_contents.heading_level_range)
        self.assertTrue(table_of_contents.insert_hyperlinks)
        self.assertTrue(table_of_contents.hide_in_web_layout)
        self.assertTrue(table_of_contents.use_paragraph_outline_level)

    def test_insert_table(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_table()
        builder.paragraph_format.alignment = aspose.words.ParagraphAlignment.CENTER
        builder.cell_format.clear_formatting()
        builder.cell_format.width = 150
        builder.cell_format.vertical_alignment = aspose.words.tables.CellVerticalAlignment.CENTER
        builder.cell_format.shading.background_pattern_color = aspose.pydrawing.Color.green_yellow
        builder.cell_format.wrap_text = False
        builder.cell_format.fit_text = True
        builder.row_format.clear_formatting()
        builder.row_format.height_rule = aspose.words.HeightRule.EXACTLY
        builder.row_format.height = 50
        builder.row_format.borders.line_style = aspose.words.LineStyle.ENGRAVE_3D
        builder.row_format.borders.color = aspose.pydrawing.Color.orange
        builder.insert_cell()
        builder.write("Row 1, Col 1")
        builder.insert_cell()
        builder.write("Row 1, Col 2")
        builder.end_row()
        builder.cell_format.shading.clear_formatting()
        builder.insert_cell()
        builder.write("Row 2, Col 1")
        builder.insert_cell()
        builder.write("Row 2, Col 2")
        builder.end_row()
        builder.insert_cell()
        builder.row_format.height = 150
        builder.cell_format.orientation = aspose.words.TextOrientation.UPWARD
        builder.write("Row 3, Col 1")
        builder.insert_cell()
        builder.cell_format.orientation = aspose.words.TextOrientation.DOWNWARD
        builder.write("Row 3, Col 2")
        builder.end_row()
        builder.end_table()
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTable.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTable.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual("Row 1, Col 1\a", table.rows[0].cells[0].get_text().strip())
        self.assertEqual("Row 1, Col 2\a", table.rows[0].cells[1].get_text().strip())
        self.assertEqual(aspose.words.HeightRule.EXACTLY, table.rows[0].row_format.height_rule)
        self.assertEqual(50, table.rows[0].row_format.height)
        self.assertEqual(aspose.words.LineStyle.ENGRAVE_3D, table.rows[0].row_format.borders.line_style)
        self.assertEqual(aspose.pydrawing.Color.orange.to_argb(), table.rows[0].row_format.borders.color.to_argb())
        for c in table.rows[0].cells:
            c = c.as_cell()
            self.assertEqual(150, c.cell_format.width)
            self.assertEqual(aspose.words.tables.CellVerticalAlignment.CENTER, c.cell_format.vertical_alignment)
            self.assertEqual(aspose.pydrawing.Color.green_yellow.to_argb(), c.cell_format.shading.background_pattern_color.to_argb())
            self.assertFalse(c.cell_format.wrap_text)
            self.assertTrue(c.cell_format.fit_text)
            self.assertEqual(aspose.words.ParagraphAlignment.CENTER, c.first_paragraph.paragraph_format.alignment)
        self.assertEqual("Row 2, Col 1\a", table.rows[1].cells[0].get_text().strip())
        self.assertEqual("Row 2, Col 2\a", table.rows[1].cells[1].get_text().strip())
        for c in table.rows[1].cells:
            c = c.as_cell()
            self.assertEqual(150, c.cell_format.width)
            self.assertEqual(aspose.words.tables.CellVerticalAlignment.CENTER, c.cell_format.vertical_alignment)
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), c.cell_format.shading.background_pattern_color.to_argb())
            self.assertFalse(c.cell_format.wrap_text)
            self.assertTrue(c.cell_format.fit_text)
            self.assertEqual(aspose.words.ParagraphAlignment.CENTER, c.first_paragraph.paragraph_format.alignment)
        self.assertEqual(150, table.rows[2].row_format.height)
        self.assertEqual("Row 3, Col 1\a", table.rows[2].cells[0].get_text().strip())
        self.assertEqual(aspose.words.TextOrientation.UPWARD, table.rows[2].cells[0].cell_format.orientation)
        self.assertEqual(aspose.words.ParagraphAlignment.CENTER, table.rows[2].cells[0].first_paragraph.paragraph_format.alignment)
        self.assertEqual("Row 3, Col 2\a", table.rows[2].cells[1].get_text().strip())
        self.assertEqual(aspose.words.TextOrientation.DOWNWARD, table.rows[2].cells[1].cell_format.orientation)
        self.assertEqual(aspose.words.ParagraphAlignment.CENTER, table.rows[2].cells[1].first_paragraph.paragraph_format.alignment)

    def test_insert_table_with_style(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        table.style_identifier = aspose.words.StyleIdentifier.MEDIUM_SHADING1_ACCENT1
        table.style_options = aspose.words.tables.TableStyleOptions.FIRST_COLUMN | aspose.words.tables.TableStyleOptions.ROW_BANDS | aspose.words.tables.TableStyleOptions.FIRST_ROW
        table.auto_fit(aspose.words.tables.AutoFitBehavior.AUTO_FIT_TO_CONTENTS)
        builder.writeln("Item")
        builder.cell_format.right_padding = 40
        builder.insert_cell()
        builder.writeln("Quantity (kg)")
        builder.end_row()
        builder.insert_cell()
        builder.writeln("Apples")
        builder.insert_cell()
        builder.writeln("20")
        builder.end_row()
        builder.insert_cell()
        builder.writeln("Bananas")
        builder.insert_cell()
        builder.writeln("40")
        builder.end_row()
        builder.insert_cell()
        builder.writeln("Carrots")
        builder.insert_cell()
        builder.writeln("50")
        builder.end_row()
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTableWithStyle.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTableWithStyle.docx")
        doc.expand_table_styles_to_direct_formatting()
        self.assertEqual("Medium Shading 1 Accent 1", table.style.name)
        self.assertEqual(aspose.words.tables.TableStyleOptions.FIRST_COLUMN | aspose.words.tables.TableStyleOptions.ROW_BANDS | aspose.words.tables.TableStyleOptions.FIRST_ROW, table.style_options)
        self.assertEqual(189, table.first_row.first_cell.cell_format.shading.background_pattern_color.b)
        self.assertEqual(aspose.pydrawing.Color.white.to_argb(), table.first_row.first_cell.first_paragraph.runs[0].font.color.to_argb())
        self.assertNotEqual(aspose.pydrawing.Color.light_blue.to_argb(), table.last_row.first_cell.cell_format.shading.background_pattern_color.b)
        self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), table.last_row.first_cell.first_paragraph.runs[0].font.color.to_argb())

    def test_insert_table_set_heading_row(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_insert_table_with_preferred_width(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Cell #1")
        builder.insert_cell()
        builder.write("Cell #2")
        builder.insert_cell()
        builder.write("Cell #3")
        table.preferred_width = aspose.words.tables.PreferredWidth.from_percent(50)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTableWithPreferredWidth.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTableWithPreferredWidth.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(aspose.words.tables.PreferredWidthType.PERCENT, table.preferred_width.type)
        self.assertEqual(50, table.preferred_width.value)

    def test_insert_cells_with_preferred_widths(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_insert_table_from_html(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_html(html = "<table>" + "<tr>" + "<td>Row 1, Cell 1</td>" + "<td>Row 1, Cell 2</td>" + "</tr>" + "<tr>" + "<td>Row 2, Cell 2</td>" + "<td>Row 2, Cell 2</td>" + "</tr>" + "</table>")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTableFromHtml.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTableFromHtml.docx")
        self.assertEqual(1, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)
        self.assertEqual(2, doc.get_child_nodes(aspose.words.NodeType.ROW, True).count)
        self.assertEqual(4, doc.get_child_nodes(aspose.words.NodeType.CELL, True).count)

    def test_insert_nested_table(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        cell = builder.insert_cell()
        builder.writeln("Outer Table Cell 1")
        builder.insert_cell()
        builder.writeln("Outer Table Cell 2")
        builder.end_table()
        builder.move_to(cell.first_paragraph)
        builder.insert_cell()
        builder.writeln("Inner Table Cell 1")
        builder.insert_cell()
        builder.writeln("Inner Table Cell 2")
        builder.end_table()
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertNestedTable.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertNestedTable.docx")
        self.assertEqual(2, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)
        self.assertEqual(4, doc.get_child_nodes(aspose.words.NodeType.CELL, True).count)
        self.assertEqual(1, cell.tables[0].count)
        self.assertEqual(2, cell.tables[0].first_row.cells.count)

    def test_create_table(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_table()
        builder.insert_cell()
        builder.write("Row 1, Cell 1.")
        builder.insert_cell()
        builder.write("Row 1, Cell 2.")
        builder.end_row()
        builder.insert_cell()
        builder.write("Row 2, Cell 1.")
        builder.insert_cell()
        builder.write("Row 2, Cell 2.")
        builder.end_table()
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.CreateTable.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.CreateTable.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(4, table.get_child_nodes(aspose.words.NodeType.CELL, True).count)
        self.assertEqual("Row 1, Cell 1.\a", table.rows[0].cells[0].get_text().strip())
        self.assertEqual("Row 1, Cell 2.\a", table.rows[0].cells[1].get_text().strip())
        self.assertEqual("Row 2, Cell 1.\a", table.rows[1].cells[0].get_text().strip())
        self.assertEqual("Row 2, Cell 2.\a", table.rows[1].cells[1].get_text().strip())

    def test_build_formatted_table(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        table.left_indent = 20
        builder.row_format.height = 40
        builder.row_format.height_rule = aspose.words.HeightRule.AT_LEAST
        builder.cell_format.shading.background_pattern_color = aspose.pydrawing.Color.from_argb(198, 217, 241)
        builder.paragraph_format.alignment = aspose.words.ParagraphAlignment.CENTER
        builder.font.size = 16
        builder.font.name = "Arial"
        builder.font.bold = True
        builder.write("Header Row,\n Cell 1")
        builder.insert_cell()
        builder.write("Header Row,\n Cell 2")
        builder.insert_cell()
        builder.write("Header Row,\n Cell 3")
        builder.end_row()
        builder.cell_format.shading.background_pattern_color = aspose.pydrawing.Color.white
        builder.cell_format.vertical_alignment = aspose.words.tables.CellVerticalAlignment.CENTER
        builder.row_format.height = 30
        builder.row_format.height_rule = aspose.words.HeightRule.AUTO
        builder.insert_cell()
        builder.font.size = 12
        builder.font.bold = False
        builder.write("Row 1, Cell 1.")
        builder.insert_cell()
        builder.write("Row 1, Cell 2.")
        builder.insert_cell()
        builder.write("Row 1, Cell 3.")
        builder.end_row()
        builder.insert_cell()
        builder.write("Row 2, Cell 1.")
        builder.insert_cell()
        builder.write("Row 2, Cell 2.")
        builder.insert_cell()
        builder.write("Row 2, Cell 3.")
        builder.end_row()
        builder.end_table()
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.CreateFormattedTable.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.CreateFormattedTable.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(20, table.left_indent)
        self.assertEqual(aspose.words.HeightRule.AT_LEAST, table.rows[0].row_format.height_rule)
        self.assertEqual(40, table.rows[0].row_format.height)
        for c in doc.get_child_nodes(aspose.words.NodeType.CELL, True):
            c = c.as_cell()
            self.assertEqual(aspose.words.ParagraphAlignment.CENTER, c.first_paragraph.paragraph_format.alignment)
            for r in c.first_paragraph.runs:
                r = r.as_run()
                self.assertEqual("Arial", r.font.name)
                if c.parent_row == table.first_row:
                    self.assertEqual(16, r.font.size)
                    self.assertTrue(r.font.bold)
                else:
                    self.assertEqual(12, r.font.size)
                    self.assertFalse(r.font.bold)

    def test_table_borders_and_shading(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        table.set_borders(aspose.words.LineStyle.SINGLE, 2, aspose.pydrawing.Color.black)
        builder.insert_cell()
        builder.cell_format.shading.background_pattern_color = aspose.pydrawing.Color.light_sky_blue
        builder.writeln("Row 1, Cell 1.")
        builder.insert_cell()
        builder.cell_format.shading.background_pattern_color = aspose.pydrawing.Color.orange
        builder.writeln("Row 1, Cell 2.")
        builder.end_row()
        builder.cell_format.clear_formatting()
        builder.cell_format.borders.left.line_width = 4
        builder.cell_format.borders.right.line_width = 4
        builder.cell_format.borders.top.line_width = 4
        builder.cell_format.borders.bottom.line_width = 4
        builder.insert_cell()
        builder.writeln("Row 2, Cell 1.")
        builder.insert_cell()
        builder.writeln("Row 2, Cell 2.")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.TableBordersAndShading.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.TableBordersAndShading.docx")
        table = doc.first_section.body.tables[0]
        for c in table.first_row:
            c = c.as_cell()
            self.assertEqual(0.5, c.cell_format.borders.top.line_width)
            self.assertEqual(0.5, c.cell_format.borders.bottom.line_width)
            self.assertEqual(0.5, c.cell_format.borders.left.line_width)
            self.assertEqual(0.5, c.cell_format.borders.right.line_width)
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), c.cell_format.borders.left.color.to_argb())
            self.assertEqual(aspose.words.LineStyle.SINGLE, c.cell_format.borders.left.line_style)
        self.assertEqual(aspose.pydrawing.Color.light_sky_blue.to_argb(), table.first_row.first_cell.cell_format.shading.background_pattern_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.orange.to_argb(), table.first_row.cells[1].cell_format.shading.background_pattern_color.to_argb())
        for c in table.last_row:
            c = c.as_cell()
            self.assertEqual(4, c.cell_format.borders.top.line_width)
            self.assertEqual(4, c.cell_format.borders.bottom.line_width)
            self.assertEqual(4, c.cell_format.borders.left.line_width)
            self.assertEqual(4, c.cell_format.borders.right.line_width)
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), c.cell_format.borders.left.color.to_argb())
            self.assertEqual(aspose.words.LineStyle.SINGLE, c.cell_format.borders.left.line_style)
            self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), c.cell_format.shading.background_pattern_color.to_argb())

    def test_set_preferred_type_convert_util(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.cell_format.preferred_width = aspose.words.tables.PreferredWidth.from_points(aspose.words.ConvertUtil.inch_to_point(3))
        builder.insert_cell()
        self.assertEqual(216, table.first_row.first_cell.cell_format.preferred_width.value)

    def test_insert_hyperlink_to_local_bookmark(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_cursor_position(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Hello world!")
        self.assertIsNone(builder.current_node)
        self.assertEqual("Hello world!", builder.current_paragraph.get_text().strip())
        builder.move_to_document_start()
        self.assertEqual(aspose.words.NodeType.RUN, builder.current_node.node_type)

    def test_move_to(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Run 1. ")
        self.assertEqual(doc.first_section.body.last_paragraph, builder.current_paragraph)
        builder.move_to(doc.first_section.body.first_paragraph.runs[0])
        self.assertEqual(doc.first_section.body.first_paragraph, builder.current_paragraph)
        builder.writeln("Run 2. ")
        self.assertEqual("Run 2. \rRun 1.", doc.get_text().strip())
        builder.move_to(doc.last_section.body.last_paragraph)
        builder.writeln("Run 3. ")
        self.assertEqual("Run 2. \rRun 1. \rRun 3.", doc.get_text().strip())
        self.assertEqual(doc.first_section.body.last_paragraph, builder.current_paragraph)

    def test_move_to_paragraph(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_move_to_cell(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_table()
        builder.insert_cell()
        builder.insert_cell()
        builder.end_row()
        builder.insert_cell()
        builder.insert_cell()
        builder.end_table()
        builder.move_to_cell(0, 1, 1, 0)
        builder.write("Column 2, cell 2.")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MoveToCell.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MoveToCell.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual("Column 2, cell 2.\a", table.rows[1].cells[1].get_text().strip())

    def test_move_to_bookmark(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_bookmark("MyBookmark")
        builder.write("Hello world! ")
        builder.end_bookmark("MyBookmark")
        self.assertTrue(builder.move_to_bookmark(bookmark_name = "MyBookmark", is_start = True, is_after = False))
        builder.write("1. ")
        self.assertEqual("Hello world! ", doc.range.bookmarks.get_by_name("MyBookmark").text)
        self.assertEqual("1. Hello world!", doc.get_text().strip())
        self.assertTrue(builder.move_to_bookmark(bookmark_name = "MyBookmark", is_start = True, is_after = True))
        builder.write("2. ")
        self.assertEqual("2. Hello world! ", doc.range.bookmarks.get_by_name("MyBookmark").text)
        self.assertEqual("1. 2. Hello world!", doc.get_text().strip())
        self.assertTrue(builder.move_to_bookmark(bookmark_name = "MyBookmark", is_start = False, is_after = False))
        builder.write("3. ")
        self.assertEqual("2. Hello world! 3. ", doc.range.bookmarks.get_by_name("MyBookmark").text)
        self.assertEqual("1. 2. Hello world! 3.", doc.get_text().strip())
        self.assertTrue(builder.move_to_bookmark(bookmark_name = "MyBookmark", is_start = False, is_after = True))
        builder.write("4.")
        self.assertEqual("2. Hello world! 3. ", doc.range.bookmarks.get_by_name("MyBookmark").text)
        self.assertEqual("1. 2. Hello world! 3. 4.", doc.get_text().strip())

    def test_build_table(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.cell_format.vertical_alignment = aspose.words.tables.CellVerticalAlignment.CENTER
        builder.write("Row 1, cell 1.")
        builder.insert_cell()
        builder.write("Row 1, cell 2.")
        builder.end_row()
        self.assertEqual(aspose.words.tables.CellVerticalAlignment.CENTER, table.rows[0].cells[0].cell_format.vertical_alignment)
        self.assertEqual(aspose.words.tables.CellVerticalAlignment.CENTER, table.rows[0].cells[1].cell_format.vertical_alignment)
        builder.insert_cell()
        builder.row_format.height = 100
        builder.row_format.height_rule = aspose.words.HeightRule.EXACTLY
        builder.cell_format.orientation = aspose.words.TextOrientation.UPWARD
        builder.write("Row 2, cell 1.")
        builder.insert_cell()
        builder.cell_format.orientation = aspose.words.TextOrientation.DOWNWARD
        builder.write("Row 2, cell 2.")
        builder.end_row()
        builder.end_table()
        self.assertEqual(0, table.rows[0].row_format.height)
        self.assertEqual(aspose.words.HeightRule.AUTO, table.rows[0].row_format.height_rule)
        self.assertEqual(100, table.rows[1].row_format.height)
        self.assertEqual(aspose.words.HeightRule.EXACTLY, table.rows[1].row_format.height_rule)
        self.assertEqual(aspose.words.TextOrientation.UPWARD, table.rows[1].cells[0].cell_format.orientation)
        self.assertEqual(aspose.words.TextOrientation.DOWNWARD, table.rows[1].cells[1].cell_format.orientation)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.BuildTable.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.BuildTable.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(2, table.rows.count)
        self.assertEqual(2, table.rows[0].cells.count)
        self.assertEqual(2, table.rows[1].cells.count)
        self.assertEqual(0, table.rows[0].row_format.height)
        self.assertEqual(aspose.words.HeightRule.AUTO, table.rows[0].row_format.height_rule)
        self.assertEqual(100, table.rows[1].row_format.height)
        self.assertEqual(aspose.words.HeightRule.EXACTLY, table.rows[1].row_format.height_rule)
        self.assertEqual("Row 1, cell 1.\a", table.rows[0].cells[0].get_text().strip())
        self.assertEqual(aspose.words.tables.CellVerticalAlignment.CENTER, table.rows[0].cells[0].cell_format.vertical_alignment)
        self.assertEqual("Row 1, cell 2.\a", table.rows[0].cells[1].get_text().strip())
        self.assertEqual("Row 2, cell 1.\a", table.rows[1].cells[0].get_text().strip())
        self.assertEqual(aspose.words.TextOrientation.UPWARD, table.rows[1].cells[0].cell_format.orientation)
        self.assertEqual("Row 2, cell 2.\a", table.rows[1].cells[1].get_text().strip())
        self.assertEqual(aspose.words.TextOrientation.DOWNWARD, table.rows[1].cells[1].cell_format.orientation)

    def test_table_cell_vertical_rotated_far_east_text_orientation(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_floating_image(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_image_original_size(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_text_input(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_text_input("TextInput", aspose.words.fields.TextFormFieldType.REGULAR, "", "Enter your text here", 0)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTextInput.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertTextInput.docx")
        form_field = doc.range.form_fields[0]
        self.assertTrue(form_field.enabled)
        self.assertEqual("TextInput", form_field.name)
        self.assertEqual(0, form_field.max_length)
        self.assertEqual("Enter your text here", form_field.result)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_FORM_TEXT_INPUT, form_field.type)
        self.assertEqual("", form_field.text_input_format)
        self.assertEqual(aspose.words.fields.TextFormFieldType.REGULAR, form_field.text_input_type)

    def test_insert_combo_box(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Pick a fruit: ")
        items = ["Apple", "Banana", "Cherry"]
        builder.insert_combo_box("DropDown", items, 0)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertComboBox.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertComboBox.docx")
        form_field = doc.range.form_fields[0]
        self.assertTrue(form_field.enabled)
        self.assertEqual("DropDown", form_field.name)
        self.assertEqual(0, form_field.drop_down_selected_index)
        self.assertSequenceEqual(items, list(form_field.drop_down_items))
        self.assertEqual(aspose.words.fields.FieldType.FIELD_FORM_DROP_DOWN, form_field.type)

    def test_signature_line_provider_id(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_signature_line_inline(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        options = aspose.words.SignatureLineOptions()
        options.signer = "John Doe"
        options.signer_title = "Manager"
        options.email = "johndoe@aspose.com"
        options.show_date = True
        options.default_instructions = False
        options.instructions = "Please sign here."
        options.allow_comments = True
        builder.insert_signature_line(signature_line_options = options, horz_pos = aspose.words.drawing.RelativeHorizontalPosition.RIGHT_MARGIN, left = 2, vert_pos = aspose.words.drawing.RelativeVerticalPosition.PAGE, top = 3, wrap_type = aspose.words.drawing.WrapType.INLINE)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.SignatureLineInline.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.SignatureLineInline.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        signature_line = shape.signature_line
        self.assertEqual("John Doe", signature_line.signer)
        self.assertEqual("Manager", signature_line.signer_title)
        self.assertEqual("johndoe@aspose.com", signature_line.email)
        self.assertTrue(signature_line.show_date)
        self.assertFalse(signature_line.default_instructions)
        self.assertEqual("Please sign here.", signature_line.instructions)
        self.assertTrue(signature_line.allow_comments)
        self.assertFalse(signature_line.is_signed)
        self.assertFalse(signature_line.is_valid)

    def test_set_paragraph_formatting(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        paragraph_format = builder.paragraph_format
        paragraph_format.alignment = aspose.words.ParagraphAlignment.CENTER
        paragraph_format.left_indent = 100
        paragraph_format.right_indent = 50
        paragraph_format.space_after = 25
        builder.writeln("This paragraph demonstrates how left and right indentation affects word wrapping.")
        builder.writeln("The space between the above paragraph and this one depends on the DocumentBuilder's paragraph format.")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.SetParagraphFormatting.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.SetParagraphFormatting.docx")
        for paragraph in doc.first_section.body.paragraphs:
            paragraph = paragraph.as_paragraph()
            self.assertEqual(aspose.words.ParagraphAlignment.CENTER, paragraph.paragraph_format.alignment)
            self.assertEqual(100, paragraph.paragraph_format.left_indent)
            self.assertEqual(50, paragraph.paragraph_format.right_indent)
            self.assertEqual(25, paragraph.paragraph_format.space_after)

    def test_set_row_formatting(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Row 1, cell 1.")
        builder.end_row()
        row_format = builder.row_format
        row_format.height = 100
        row_format.height_rule = aspose.words.HeightRule.EXACTLY
        builder.insert_cell()
        builder.write("Row 2, cell 1.")
        builder.end_table()
        self.assertEqual(0, table.rows[0].row_format.height)
        self.assertEqual(aspose.words.HeightRule.AUTO, table.rows[0].row_format.height_rule)
        self.assertEqual(100, table.rows[1].row_format.height)
        self.assertEqual(aspose.words.HeightRule.EXACTLY, table.rows[1].row_format.height_rule)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.SetRowFormatting.docx")
        table = doc.first_section.body.tables[0]
        self.assertEqual(0, table.rows[0].row_format.height)
        self.assertEqual(aspose.words.HeightRule.AUTO, table.rows[0].row_format.height_rule)
        self.assertEqual(100, table.rows[1].row_format.height)
        self.assertEqual(aspose.words.HeightRule.EXACTLY, table.rows[1].row_format.height_rule)

    def test_insert_footnote(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_apply_borders_and_shading(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        borders = builder.paragraph_format.borders
        borders.distance_from_text = 20
        borders.get_by_border_type(aspose.words.BorderType.LEFT).line_style = aspose.words.LineStyle.DOUBLE
        borders.get_by_border_type(aspose.words.BorderType.RIGHT).line_style = aspose.words.LineStyle.DOUBLE
        borders.get_by_border_type(aspose.words.BorderType.TOP).line_style = aspose.words.LineStyle.DOUBLE
        borders.get_by_border_type(aspose.words.BorderType.BOTTOM).line_style = aspose.words.LineStyle.DOUBLE
        shading = builder.paragraph_format.shading
        shading.texture = aspose.words.TextureIndex.TEXTURE_DIAGONAL_CROSS
        shading.background_pattern_color = aspose.pydrawing.Color.light_coral
        shading.foreground_pattern_color = aspose.pydrawing.Color.light_salmon
        builder.write("This paragraph is formatted with a double border and shading.")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.ApplyBordersAndShading.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.ApplyBordersAndShading.docx")
        borders = doc.first_section.body.first_paragraph.paragraph_format.borders
        self.assertEqual(20, borders.distance_from_text)
        self.assertEqual(aspose.words.LineStyle.DOUBLE, borders.get_by_border_type(aspose.words.BorderType.LEFT).line_style)
        self.assertEqual(aspose.words.LineStyle.DOUBLE, borders.get_by_border_type(aspose.words.BorderType.RIGHT).line_style)
        self.assertEqual(aspose.words.LineStyle.DOUBLE, borders.get_by_border_type(aspose.words.BorderType.TOP).line_style)
        self.assertEqual(aspose.words.LineStyle.DOUBLE, borders.get_by_border_type(aspose.words.BorderType.BOTTOM).line_style)
        self.assertEqual(aspose.words.TextureIndex.TEXTURE_DIAGONAL_CROSS, shading.texture)
        self.assertEqual(aspose.pydrawing.Color.light_coral.to_argb(), shading.background_pattern_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.light_salmon.to_argb(), shading.foreground_pattern_color.to_argb())

    def test_delete_row(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Row 1, cell 1.")
        builder.insert_cell()
        builder.write("Row 1, cell 2.")
        builder.end_row()
        builder.insert_cell()
        builder.write("Row 2, cell 1.")
        builder.insert_cell()
        builder.write("Row 2, cell 2.")
        builder.end_table()
        self.assertEqual(2, table.rows.count)
        builder.delete_row(0, 0)
        self.assertEqual(1, table.rows.count)
        self.assertEqual("Row 2, cell 1.\aRow 2, cell 2.\a\a", table.get_text().strip())

    def test_insert_ole_object_exception(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_insert_chart_relative_position(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.PIE, horz_pos = aspose.words.drawing.RelativeHorizontalPosition.MARGIN, left = 100, vert_pos = aspose.words.drawing.RelativeVerticalPosition.MARGIN, top = 100, width = 200, height = 100, wrap_type = aspose.words.drawing.WrapType.SQUARE)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertedChartRelativePosition.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertedChartRelativePosition.docx")
        chart_shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(100, chart_shape.top)
        self.assertEqual(100, chart_shape.left)
        self.assertEqual(200, chart_shape.width)
        self.assertEqual(100, chart_shape.height)
        self.assertEqual(aspose.words.drawing.WrapType.SQUARE, chart_shape.wrap_type)
        self.assertEqual(aspose.words.drawing.RelativeHorizontalPosition.MARGIN, chart_shape.relative_horizontal_position)
        self.assertEqual(aspose.words.drawing.RelativeVerticalPosition.MARGIN, chart_shape.relative_vertical_position)

    def test_insert_underline(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.underline = aspose.words.Underline.DASH
        builder.font.color = aspose.pydrawing.Color.blue
        builder.font.size = 32
        builder.writeln("Large, blue, and underlined text.")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertUnderline.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.InsertUnderline.docx")
        first_run = doc.first_section.body.first_paragraph.runs[0]
        self.assertEqual("Large, blue, and underlined text.", first_run.get_text().strip())
        self.assertEqual(aspose.words.Underline.DASH, first_run.font.underline)
        self.assertEqual(aspose.pydrawing.Color.blue.to_argb(), first_run.font.color.to_argb())
        self.assertEqual(32, first_run.font.size)

    def test_current_story(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_ole_objects(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_style_separator(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_smart_style_behavior(self):
        dst_doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(dst_doc)
        my_style = builder.document.styles.add(aspose.words.StyleType.PARAGRAPH, "MyStyle")
        my_style.font.size = 14
        my_style.font.name = "Courier New"
        my_style.font.color = aspose.pydrawing.Color.blue
        builder.paragraph_format.style_name = my_style.name
        builder.writeln("Hello world!")
        src_doc = dst_doc.clone()
        src_doc.styles.get_by_name("MyStyle").font.color = aspose.pydrawing.Color.red
        options = aspose.words.ImportFormatOptions()
        options.smart_style_behavior = True
        builder.insert_document(src_doc = src_doc, import_format_mode = aspose.words.ImportFormatMode.KEEP_SOURCE_FORMATTING, import_format_options = options)
        dst_doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.SmartStyleBehavior.docx")
        dst_doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.SmartStyleBehavior.docx")
        self.assertEqual(aspose.pydrawing.Color.blue.to_argb(), dst_doc.styles.get_by_name("MyStyle").font.color.to_argb())
        self.assertEqual("MyStyle", dst_doc.first_section.body.paragraphs[0].paragraph_format.style.name)
        self.assertEqual("Normal", dst_doc.first_section.body.paragraphs[1].paragraph_format.style.name)
        self.assertEqual(14, dst_doc.first_section.body.paragraphs[1].runs[0].font.size)
        self.assertEqual("Courier New", dst_doc.first_section.body.paragraphs[1].runs[0].font.name)
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), dst_doc.first_section.body.paragraphs[1].runs[0].font.color.to_argb())

    def test_emphases_warning_source_markdown(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Emphases markdown warning.docx")
        warnings = aspose.words.WarningInfoCollection()
        doc.warning_callback = warnings
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.EmphasesWarningSourceMarkdown.md")
        for warning_info in warnings:
            if warning_info.source == aspose.words.WarningSource.MARKDOWN:
                self.assertEqual("The (*, 0:11) cannot be properly written into Markdown.", warning_info.description)

    def test_do_not_ignore_header_footer(self):
        dst_doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        src_doc = aspose.words.Document(file_name = MY_DIR + "Header and footer types.docx")
        import_format_options = aspose.words.ImportFormatOptions()
        import_format_options.ignore_header_footer = False
        dst_doc.append_document(src_doc = src_doc, import_format_mode = aspose.words.ImportFormatMode.KEEP_SOURCE_FORMATTING, import_format_options = import_format_options)
        dst_doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.DoNotIgnoreHeaderFooter.docx")

    def test_markdown_document_emphases(self):
        builder = aspose.words.DocumentBuilder()
        builder.font.italic = True
        builder.writeln("This text will be italic")
        builder.font.clear_formatting()
        builder.font.bold = True
        builder.writeln("This text will be bold")
        builder.font.clear_formatting()
        builder.font.italic = True
        builder.write("You ")
        builder.font.bold = True
        builder.write("can")
        builder.font.bold = False
        builder.writeln(" combine them")
        builder.font.clear_formatting()
        builder.font.strike_through = True
        builder.writeln("This text will be strikethrough")
        builder.document.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_inline_code(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        inline_code_1_back_ticks = doc.styles.add(aspose.words.StyleType.CHARACTER, "InlineCode")
        builder.font.style = inline_code_1_back_ticks
        builder.writeln("Text with InlineCode style with one backtick")
        inline_code_3_back_ticks = doc.styles.add(aspose.words.StyleType.CHARACTER, "InlineCode.3")
        builder.font.style = inline_code_3_back_ticks
        builder.writeln("Text with InlineCode style with 3 backticks")
        builder.document.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_headings(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        builder.font.bold = False
        builder.font.italic = False
        builder.paragraph_format.style_name = "Heading 1"
        builder.font.italic = True
        builder.writeln("This is an italic H1 tag")
        builder.font.bold = False
        builder.font.italic = False
        setext_heading1 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "SetextHeading1")
        builder.paragraph_format.style = setext_heading1
        doc.styles.get_by_name("SetextHeading1").base_style_name = "Heading 1"
        builder.writeln("SetextHeading 1")
        builder.paragraph_format.style_name = "Heading 2"
        builder.writeln("This is an H2 tag")
        builder.font.bold = False
        builder.font.italic = False
        setext_heading2 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "SetextHeading2")
        builder.paragraph_format.style = setext_heading2
        doc.styles.get_by_name("SetextHeading2").base_style_name = "Heading 2"
        builder.writeln("SetextHeading 2")
        builder.paragraph_format.style = doc.styles.get_by_name("Heading 3")
        builder.writeln("This is an H3 tag")
        builder.font.bold = False
        builder.font.italic = False
        builder.paragraph_format.style = doc.styles.get_by_name("Heading 4")
        builder.font.bold = True
        builder.writeln("This is an bold H4 tag")
        builder.font.bold = False
        builder.font.italic = False
        builder.paragraph_format.style = doc.styles.get_by_name("Heading 5")
        builder.font.italic = True
        builder.font.bold = True
        builder.writeln("This is an italic and bold H5 tag")
        builder.font.bold = False
        builder.font.italic = False
        builder.paragraph_format.style = doc.styles.get_by_name("Heading 6")
        builder.writeln("This is an H6 tag")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_blockquotes(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        builder.paragraph_format.style_name = "Quote"
        builder.writeln("Blockquote")
        quote_level2 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "Quote1")
        builder.paragraph_format.style = quote_level2
        doc.styles.get_by_name("Quote1").base_style_name = "Quote"
        builder.writeln("1. Nested blockquote")
        quote_level3 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "Quote2")
        builder.paragraph_format.style = quote_level3
        doc.styles.get_by_name("Quote2").base_style_name = "Quote1"
        builder.font.italic = True
        builder.writeln("2. Nested italic blockquote")
        quote_level4 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "Quote3")
        builder.paragraph_format.style = quote_level4
        doc.styles.get_by_name("Quote3").base_style_name = "Quote2"
        builder.font.italic = False
        builder.font.bold = True
        builder.writeln("3. Nested bold blockquote")
        quote_level5 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "Quote4")
        builder.paragraph_format.style = quote_level5
        doc.styles.get_by_name("Quote4").base_style_name = "Quote3"
        builder.font.bold = False
        builder.writeln("4. Nested blockquote")
        quote_level6 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "Quote5")
        builder.paragraph_format.style = quote_level6
        doc.styles.get_by_name("Quote5").base_style_name = "Quote4"
        builder.writeln("5. Nested blockquote")
        quote_level7 = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "Quote6")
        builder.paragraph_format.style = quote_level7
        doc.styles.get_by_name("Quote6").base_style_name = "Quote5"
        builder.font.italic = True
        builder.font.bold = True
        builder.writeln("6. Nested italic bold blockquote")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_indented_code(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.writeln("\n")
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        indented_code = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "IndentedCode")
        builder.paragraph_format.style = indented_code
        builder.writeln("This is an indented code")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_fenced_code(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.writeln("\n")
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        fenced_code = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "FencedCode")
        builder.paragraph_format.style = fenced_code
        builder.writeln("This is a fenced code")
        fenced_code_with_info = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "FencedCode.C#")
        builder.paragraph_format.style = fenced_code_with_info
        builder.writeln("This is a fenced code with info string")
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_horizontal_rule(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        builder.insert_horizontal_rule()
        builder.document.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_markdown_document_bulleted_list(self):
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.paragraph_format.clear_formatting()
        builder.writeln("\n")
        builder.list_format.apply_bullet_default()
        builder.list_format.list.list_levels[0].number_format = "-"
        builder.writeln("Item 1")
        builder.writeln("Item 2")
        builder.list_format.list_indent()
        builder.writeln("Item 2a")
        builder.writeln("Item 2b")
        builder.document.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.MarkdownDocument.md")

    def test_load_markdown_document_and_assert_content(self):
        raise NotImplementedError("Unsupported identifier with name = text and kind = IdentifierName")

    def test_insert_online_video(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_ole_object_as_icon(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_preserve_blocks(self):
        html = """
                <html>
                    <div style='border:dotted'>
                    <div style='border:solid'>
                        <p>paragraph 1</p>
                        <p>paragraph 2</p>
                    </div>
                    </div>
                </html>"""
        insert_options = aspose.words.HtmlInsertOptions.PRESERVE_BLOCKS
        builder = aspose.words.DocumentBuilder()
        builder.insert_html(html = html, options = insert_options)
        builder.document.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.PreserveBlocks.docx")

    def test_phonetic_guide(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Phonetic guide.docx")
        runs = doc.first_section.body.first_paragraph.runs
        self.assertEqual(True, runs[0].is_phonetic_guide)
        self.assertEqual("base", runs[0].phonetic_guide.base_text)
        self.assertEqual("ruby", runs[0].phonetic_guide.ruby_text)
