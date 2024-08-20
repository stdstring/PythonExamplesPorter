# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.buildingblocks
import aspose.words.drawing
import aspose.words.fields
import aspose.words.lists
import aspose.words.notes
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExField(ApiExampleBase):
    def test_get_field_from_document(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_get_field_data(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_get_field_code(self):
        #ExStart
        #ExFor:Field.get_field_code
        #ExFor:Field.get_field_code(bool)
        #ExSummary:Shows how to get a field's field code.
        # Open a document which contains a MERGEFIELD inside an IF field.
        doc = aw.Document(file_name=MY_DIR + "Nested fields.docx")
        field_if = doc.range.fields[0].as_field_if()
        # There are two ways of getting a field's field code:
        # 1 -  Omit its inner fields:
        self.assertEqual(" IF  > 0 \" (surplus of ) \" \"\" ", field_if.get_field_code(False))
        # 2 -  Include its inner fields:
        self.assertEqual(f" IF \u0013 MERGEFIELD NetIncome \u0014\u0015 > 0 \" (surplus of \u0013 MERGEFIELD  NetIncome \\f $ \u0014\u0015) \" \"\" ", field_if.get_field_code(True))
        # By default, the GetFieldCode method displays inner fields.
        self.assertEqual(field_if.get_field_code(), field_if.get_field_code(True))
        #ExEnd

    def test_display_result(self):
        #ExStart
        #ExFor:Field.display_result
        #ExSummary:Shows how to get the real text that a field displays in the document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("This document was written by ")
        field_author = builder.insert_field(field_type=aw.fields.FieldType.FIELD_AUTHOR, update_field=True).as_field_author()
        field_author.author_name = "John Doe"
        # We can use the DisplayResult property to verify what exact text
        # a field would display in its place in the document.
        self.assertEqual("", field_author.display_result)
        # Fields do not maintain accurate result values in real-time.
        # To make sure our fields display accurate results at any given time,
        # such as right before a save operation, we need to update them manually.
        field_author.update()
        self.assertEqual("John Doe", field_author.display_result)
        doc.save(file_name=ARTIFACTS_DIR + "Field.DisplayResult.docx")
        #ExEnd
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
        # Insert a TC field at the current document builder position.
        builder.insert_field(field_code="TC \"Entry Text\" \\f t")

    def test_field_locale(self):
        raise NotImplementedError("Unsupported target type System.Globalization.CultureInfo")

    def test_update_dirty_fields(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_insert_field_with_field_builder_exception(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_preserve_include_picture(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_field_format(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

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
        #ExStart
        #ExFor:FieldCollection
        #ExFor:FieldCollection.count
        #ExFor:FieldCollection.clear
        #ExFor:FieldCollection.__getitem__(int)
        #ExFor:FieldCollection.remove(Field)
        #ExFor:FieldCollection.remove_at(int)
        #ExFor:Field.remove
        #ExSummary:Shows how to remove fields from a field collection.
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
        # Below are four ways of removing fields from a field collection.
        # 1 -  Get a field to remove itself:
        fields[0].remove()
        self.assertEqual(5, fields.count)
        # 2 -  Get the collection to remove a field that we pass to its removal method:
        last_field = fields[3]
        fields.remove(last_field)
        self.assertEqual(4, fields.count)
        # 3 -  Remove a field from a collection at an index:
        fields.remove_at(2)
        self.assertEqual(3, fields.count)
        # 4 -  Remove all the fields from the collection at once:
        fields.clear()
        self.assertEqual(0, fields.count)
        #ExEnd

    def test_field_compare(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_if(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_auto_num(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_auto_num_lgl(self):
        raise NotImplementedError("ignored method body")

    def test_field_auto_num_out(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_field_auto_text(self):
        raise NotImplementedError("Unsupported member target type - System.String[] for expression: doc.FieldOptions.BuiltInTemplatesPaths")

    def test_field_auto_text_list(self):
        raise NotImplementedError("ignored method body")

    def test_field_list_num(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_toc(self):
        raise NotImplementedError("ignored method body")

    def test_field_toc_entry_identifier(self):
        raise NotImplementedError("ignored method body")

    def test_toc_seq_prefix(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_toc_seq_numbering(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_toc_seq_bookmark(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_field_citation(self):
        raise NotImplementedError("Unsupported target type System.Threading.Thread")

    def test_field_data(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_field_include(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_field_include_picture(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_field_include_text(self):
        raise NotImplementedError("ignored method body")

    def test_field_hyperlink(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_index_filter(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_index_formatting(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_index_sequence(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_field_index_page_number_separator(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_index_page_range_bookmark(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_index_cross_reference_separator(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_index_subheading(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_field_index_yomi(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_field_barcode(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_display_barcode(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_linked_objects_as_text(self):
        raise NotImplementedError("ignored method body")

    def test_field_user_address(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_user_initials(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_user_name(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_style_ref_paragraph_numbers(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_date(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_field_create_date(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_field_save_date(self):
        raise NotImplementedError("Unsupported target type System.Text.RegularExpressions.Regex")

    def test_field_builder(self):
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
        #ExStart
        #ExFor:FieldPrintDate
        #ExFor:FieldPrintDate.use_lunar_calendar
        #ExFor:FieldPrintDate.use_saka_era_calendar
        #ExFor:FieldPrintDate.use_um_al_qura_calendar
        #ExSummary:Shows read PRINTDATE fields.
        doc = aw.Document(file_name=MY_DIR + "Field sample - PRINTDATE.docx")
        # When a document is printed by a printer or printed as a PDF (but not exported to PDF),
        # PRINTDATE fields will display the print operation's date/time.
        # If no printing has taken place, these fields will display "0/0/0000".
        field = doc.range.fields[0].as_field_print_date()
        self.assertEqual("3/25/2020 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE ", field.get_field_code())
        # Below are three different calendar types according to which the PRINTDATE field
        # can display the date and time of the last printing operation.
        # 1 -  Islamic Lunar Calendar:
        field = doc.range.fields[1].as_field_print_date()
        self.assertTrue(field.use_lunar_calendar)
        self.assertEqual("8/1/1441 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE  \\h", field.get_field_code())
        field = doc.range.fields[2].as_field_print_date()
        # 2 -  Umm al-Qura calendar:
        self.assertTrue(field.use_um_al_qura_calendar)
        self.assertEqual("8/1/1441 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE  \\u", field.get_field_code())
        field = doc.range.fields[3].as_field_print_date()
        # 3 -  Indian National Calendar:
        self.assertTrue(field.use_saka_era_calendar)
        self.assertEqual("1/5/1942 12:00:00 AM", field.result)
        self.assertEqual(" PRINTDATE  \\s", field.get_field_code())
        #ExEnd

    def test_field_quote(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_field_note_ref(self):
        raise NotImplementedError("ignored method body")

    def test_note_ref(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_page_ref(self):
        raise NotImplementedError("ignored method body")

    def test_field_ref(self):
        raise NotImplementedError("ignored method body")

    def test_field_rd(self):
        raise NotImplementedError("Unsupported usage of backslash symbol in literal expression: @\"\\\"")

    def test_field_set_ref(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_template(self):
        #ExStart
        #ExFor:FieldTemplate
        #ExFor:FieldTemplate.include_full_path
        #ExFor:FieldOptions.template_name
        #ExSummary:Shows how to use a TEMPLATE field to display the local file system location of a document's template.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # We can set a template name using by the fields. This property is used when the "doc.AttachedTemplate" is empty.
        # If this property is empty the default template file name "Normal.dotm" is used.
        doc.field_options.template_name = ""
        field = builder.insert_field(field_type=aw.fields.FieldType.FIELD_TEMPLATE, update_field=False).as_field_template()
        self.assertEqual(" TEMPLATE ", field.get_field_code())
        builder.writeln()
        field = builder.insert_field(field_type=aw.fields.FieldType.FIELD_TEMPLATE, update_field=False).as_field_template()
        field.include_full_path = True
        self.assertEqual(" TEMPLATE  \\p", field.get_field_code())
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "Field.TEMPLATE.docx")
        #ExEnd
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
        raise NotImplementedError("ignored method body")

    def test_field_add_in(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_field_edit_time(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_eq(self):
        raise NotImplementedError("ignored method body")

    def test_field_eq_as_office_math(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_field_forms(self):
        #ExStart
        #ExFor:FieldFormCheckBox
        #ExFor:FieldFormDropDown
        #ExFor:FieldFormText
        #ExSummary:Shows how to process FORMCHECKBOX, FORMDROPDOWN and FORMTEXT fields.
        # These fields are legacy equivalents of the FormField. We can read, but not create these fields using Aspose.Words.
        # In Microsoft Word, we can insert these fields via the Legacy Tools menu in the Developer tab.
        doc = aw.Document(file_name=MY_DIR + "Form fields.docx")
        field_form_check_box = doc.range.fields[1].as_field_form_check_box()
        self.assertEqual(" FORMCHECKBOX \u0001", field_form_check_box.get_field_code())
        field_form_drop_down = doc.range.fields[2].as_field_form_drop_down()
        self.assertEqual(" FORMDROPDOWN \u0001", field_form_drop_down.get_field_code())
        field_form_text = doc.range.fields[0].as_field_form_text()
        self.assertEqual(" FORMTEXT \u0001", field_form_text.get_field_code())
        #ExEnd

    def test_field_formula(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_last_saved_by(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_ocx(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_section(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_field_time(self):
        raise NotImplementedError("ignored method body")

    def test_bidi_outline(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_legacy(self):
        #ExStart
        #ExFor:FieldEmbed
        #ExFor:FieldShape
        #ExFor:FieldShape.text
        #ExSummary:Shows how some older Microsoft Word fields such as SHAPE and EMBED are handled during loading.
        # Open a document that was created in Microsoft Word 2003.
        doc = aw.Document(file_name=MY_DIR + "Legacy fields.doc")
        # If we open the Word document and press Alt+F9, we will see a SHAPE and an EMBED field.
        # A SHAPE field is the anchor/canvas for an AutoShape object with the "In line with text" wrapping style enabled.
        # An EMBED field has the same function, but for an embedded object,
        # such as a spreadsheet from an external Excel document.
        # However, these fields will not appear in the document's Fields collection.
        self.assertEqual(0, doc.range.fields.count)
        # These fields are supported only by old versions of Microsoft Word.
        # The document loading process will convert these fields into Shape objects,
        # which we can access in the document's node collection.
        shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
        self.assertEqual(3, shapes.count)
        # The first Shape node corresponds to the SHAPE field in the input document,
        # which is the inline canvas for the AutoShape.
        shape = shapes[0].as_shape()
        self.assertEqual(aw.drawing.ShapeType.IMAGE, shape.shape_type)
        # The second Shape node is the AutoShape itself.
        shape = shapes[1].as_shape()
        self.assertEqual(aw.drawing.ShapeType.CAN, shape.shape_type)
        # The third Shape is what was the EMBED field that contained the external spreadsheet.
        shape = shapes[2].as_shape()
        self.assertEqual(aw.drawing.ShapeType.OLE_OBJECT, shape.shape_type)
        #ExEnd

    def test_set_field_index_format(self):
        #ExStart
        #ExFor:FieldIndexFormat
        #ExFor:FieldOptions.field_index_format
        #ExSummary:Shows how to formatting FieldIndex fields.
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
        #ExEnd

    def test_bibliography_sources(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IList")
