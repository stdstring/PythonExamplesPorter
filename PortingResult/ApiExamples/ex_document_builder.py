# -*- coding: utf-8 -*-
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
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_headers_and_footers(self):
        raise NotImplementedError("Unsupported type of expression: HeaderFooterType.HeaderFirst")

    def test_merge_fields(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_insert_horizontal_rule(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_horizontal_rule_format_exceptions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_insert_hyperlink_async(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_push_pop_font(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_insert_ole_object(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_html(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_math_ml(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_text_and_bookmark(self):
        raise NotImplementedError("Unsupported target type System.String")

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
        raise NotImplementedError("Unsupported target type System.String")

    def test_fill_merge_fields(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_insert_toc(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_insert_table(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_insert_table_with_style(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

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
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

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
        raise NotImplementedError("Unsupported target type System.String")

    def test_build_formatted_table(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_table_borders_and_shading(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_set_preferred_type_convert_util(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        builder.cell_format.preferred_width = aspose.words.tables.PreferredWidth.from_points(aspose.words.ConvertUtil.inch_to_point(3))
        builder.insert_cell()
        self.assertEqual(216, table.first_row.first_cell.cell_format.preferred_width.value)

    def test_insert_hyperlink_to_local_bookmark(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_cursor_position(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_move_to(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_move_to_paragraph(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_move_to_cell(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_move_to_bookmark(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_build_table(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_table_cell_vertical_rotated_far_east_text_orientation(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_floating_image(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_image_original_size(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_insert_text_input(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_insert_combo_box(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_signature_line_provider_id(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_signature_line_inline(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

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
        # for each loop begin
        for paragraph in doc.first_section.body.paragraphs:
            paragraph = paragraph.as_paragraph()
            self.assertEqual(aspose.words.ParagraphAlignment.CENTER, paragraph.paragraph_format.alignment)
            self.assertEqual(100, paragraph.paragraph_format.left_indent)
            self.assertEqual(50, paragraph.paragraph_format.right_indent)
            self.assertEqual(25, paragraph.paragraph_format.space_after)
        # for loop end

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
        raise NotImplementedError("Unsupported type of expression: BorderType.Left")

    def test_delete_row(self):
        raise NotImplementedError("Unsupported target type System.String")

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
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_current_story(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_insert_ole_objects(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_style_separator(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_smart_style_behavior(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_emphases_warning_source_markdown(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Emphases markdown warning.docx")
        warnings = aspose.words.WarningInfoCollection()
        doc.warning_callback = warnings
        doc.save(file_name = ARTIFACTS_DIR + "DocumentBuilder.EmphasesWarningSourceMarkdown.md")
        # for each loop begin
        for warning_info in warnings:
            # if begin
            if warning_info.source == aspose.words.WarningSource.MARKDOWN:
                self.assertEqual("The (*, 0:11) cannot be properly written into Markdown.", warning_info.description)
            # if end
        # for loop end

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
