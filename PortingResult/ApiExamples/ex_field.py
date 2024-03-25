# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.buildingblocks
import aspose.words.drawing
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExField(ApiExampleBase):
    def test_get_field_data(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_get_field_code(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_display_result(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("This document was written by ")
        field_author = builder.insert_field(field_type=aw.fields.FieldType.FIELD_AUTHOR, update_field=True).as_field_author()
        field_author.author_name = "John Doe"
        self.assertEqual("", field_author.display_result)
        field_author.update()
        self.assertEqual("John Doe", field_author.display_result)
        doc.save(file_name=ARTIFACTS_DIR + "Field.DisplayResult.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Field.DisplayResult.docx")
        self.assertEqual("John Doe", doc.range.fields[0].display_result)

    def test_create_with_field_builder(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_rev_num(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_field_none(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_insert_tc_field(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_field(field_code="TC \"Entry Text\" \\f t")

    def test_insert_field_with_field_builder_exception(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_preserve_include_picture(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_unlink(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_unlink_all_fields_in_range(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_unlink_single_field(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_update_toc_page_numbers(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_field_advance(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_address_block(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_remove_fields(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_field(field_code=" DATE \\@ \"dddd, d MMMM yyyy\" ")
        builder.insert_field(field_code=" TIME ")
        builder.insert_field(field_code=" REVNUM ")
        builder.insert_field(field_code=" AUTHOR  \"John Doe\" ")
        builder.insert_field(field_code=" SUBJECT \"My Subject\" ")
        builder.insert_field(field_code=" QUOTE \"Hello world!\" ")
        doc.update_fields()
        fields = doc.range.fields
        self.assertEqual(6, fields.count)
        fields[0].remove()
        self.assertEqual(5, fields.count)
        last_field = fields[3]
        fields.remove(last_field)
        self.assertEqual(4, fields.count)
        fields.remove_at(2)
        self.assertEqual(3, fields.count)
        fields.clear()
        self.assertEqual(0, fields.count)

    def test_field_compare(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_if(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_auto_num(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_auto_num_lgl(self):
        raise NotImplementedError("Unsupported call of method named InsertNumberedClause")

    def test_field_auto_num_out(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_field_auto_text(self):
        raise NotImplementedError("Unsupported member target type - System.String[] for expression: doc.FieldOptions.BuiltInTemplatesPaths")

    def test_field_auto_text_list(self):
        raise NotImplementedError("Unsupported call of method named AppendAutoTextEntry")

    def test_field_list_num(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_toc(self):
        raise NotImplementedError("Unsupported call of method named InsertNewPageWithHeading")

    def test_field_toc_entry_identifier(self):
        raise NotImplementedError("Unsupported call of method named InsertTocEntry")

    def test_toc_seq_prefix(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_toc_seq_numbering(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_citation(self):
        raise NotImplementedError("Unsupported target type System.Threading.Thread")

    def test_change_bibliography_styles(self):
        raise NotImplementedError("Unsupported target type System.Threading.Thread")

    def test_field_data(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_field_include(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_field_include_picture(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_field_barcode(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_display_barcode(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_user_address(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_user_initials(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_user_name(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_author(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_doc_variable(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_subject(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_comments(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_file_size(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_go_to_button(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_info(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_macro_button(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_keywords(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_num(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_print(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_print_date(self):
        doc = aw.Document(file_name=MY_DIR + "Field sample - PRINTDATE.docx")
        field = doc.range.fields[0].as_field_print_date()
        self.assertEqual("3/25/2020 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE ", field.get_field_code())
        field = doc.range.fields[1].as_field_print_date()
        self.assertTrue(field.use_lunar_calendar)
        self.assertEqual("8/1/1441 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE  \\h", field.get_field_code())
        field = doc.range.fields[2].as_field_print_date()
        self.assertTrue(field.use_um_al_qura_calendar)
        self.assertEqual("8/1/1441 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE  \\u", field.get_field_code())
        field = doc.range.fields[3].as_field_print_date()
        self.assertTrue(field.use_saka_era_calendar)
        self.assertEqual("1/5/1942 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE  \\s", field.get_field_code())

    def test_field_set_ref(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_template(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        doc.field_options.template_name = ""
        field = builder.insert_field(field_type=aw.fields.FieldType.FIELD_TEMPLATE, update_field=False).as_field_template()
        self.assertEqual(" TEMPLATE ", field.get_field_code())
        builder.writeln()
        field = builder.insert_field(field_type=aw.fields.FieldType.FIELD_TEMPLATE, update_field=False).as_field_template()
        field.include_full_path = True
        self.assertEqual(" TEMPLATE  \\p", field.get_field_code())
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "Field.TEMPLATE.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Field.TEMPLATE.docx")
        field = doc.range.fields[0].as_field_template()
        self.assertEqual(" TEMPLATE ", field.get_field_code())
        self.assertEqual("Normal.dotm", field.result)
        field = doc.range.fields[1].as_field_template()
        self.assertEqual(" TEMPLATE  \\p", field.get_field_code())
        self.assertEqual("Normal.dotm", field.result)

    def test_field_symbol(self):
        raise NotImplementedError("Unrecognizable type of expression: 0x00a9")

    def test_field_title(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_toa(self):
        raise NotImplementedError("Unsupported call of method named InsertToaEntry")

    def test_field_add_in(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_field_edit_time(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_eq(self):
        raise NotImplementedError("Unsupported call of method named InsertFieldEQ")

    def test_field_forms(self):
        doc = aw.Document(file_name=MY_DIR + "Form fields.docx")
        field_form_check_box = doc.range.fields[1].as_field_form_check_box()
        self.assertEqual(" FORMCHECKBOX \u0001", field_form_check_box.get_field_code())
        field_form_drop_down = doc.range.fields[2].as_field_form_drop_down()
        self.assertEqual(" FORMDROPDOWN \u0001", field_form_drop_down.get_field_code())
        field_form_text = doc.range.fields[0].as_field_form_text()
        self.assertEqual(" FORMTEXT \u0001", field_form_text.get_field_code())

    def test_field_formula(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_last_saved_by(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_ocx(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_section(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_bidi_outline(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_legacy(self):
        doc = aw.Document(file_name=MY_DIR + "Legacy fields.doc")
        self.assertEqual(0, doc.range.fields.count)
        shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
        self.assertEqual(3, shapes.count)
        shape = shapes[0].as_shape()
        self.assertEqual(aw.drawing.ShapeType.IMAGE, shape.shape_type)
        shape = shapes[1].as_shape()
        self.assertEqual(aw.drawing.ShapeType.CAN, shape.shape_type)
        shape = shapes[2].as_shape()
        self.assertEqual(aw.drawing.ShapeType.OLE_OBJECT, shape.shape_type)

    def test_set_field_index_format(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("A")
        builder.insert_break(aw.BreakType.LINE_BREAK)
        builder.insert_field(field_code="XE \"A\"")
        builder.write("B")
        builder.insert_field(field_code=" INDEX \\e \" · \" \\h \"A\" \\c \"2\" \\z \"1033\"", field_value=None)
        doc.field_options.field_index_format = aw.fields.FieldIndexFormat.FANCY
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "Field.SetFieldIndexFormat.docx")

    def test_bibliography_sources(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.ICollection")
