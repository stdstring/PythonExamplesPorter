# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.pydrawing
import aspose.words as aw
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExFormFields(ApiExampleBase):
    def test_create(self):
        #ExStart
        #ExFor:FormField
        #ExFor:FormField.result
        #ExFor:FormField.type
        #ExFor:FormField.name
        #ExSummary:Shows how to insert a combo box.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Please select a fruit: ")

        # Insert a combo box which will allow a user to choose an option from a collection of strings.
        combo_box = builder.insert_combo_box("MyComboBox", ["Apple", "Banana", "Cherry"], 0)
        self.assertEqual("MyComboBox", combo_box.name)
        self.assertEqual(aw.fields.FieldType.FIELD_FORM_DROP_DOWN, combo_box.type)
        self.assertEqual("Apple", combo_box.result)

        # The form field will appear in the form of a "select" html tag.
        doc.save(file_name=ARTIFACTS_DIR + "FormFields.Create.html")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "FormFields.Create.html")
        combo_box = doc.range.form_fields[0]
        self.assertEqual("MyComboBox", combo_box.name)
        self.assertEqual(aw.fields.FieldType.FIELD_FORM_DROP_DOWN, combo_box.type)
        self.assertEqual("Apple", combo_box.result)

    def test_text_input(self):
        #ExStart
        #ExFor:DocumentBuilder.insert_text_input
        #ExSummary:Shows how to insert a text input form field.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Please enter text here: ")

        # Insert a text input field, which will allow the user to click it and enter text.
        # Assign some placeholder text that the user may overwrite and pass
        # a maximum text length of 0 to apply no limit on the form field's contents.
        builder.insert_text_input("TextInput1", aw.fields.TextFormFieldType.REGULAR, "", "Placeholder text", 0)

        # The form field will appear in the form of an "input" html tag, with a type of "text".
        doc.save(file_name=ARTIFACTS_DIR + "FormFields.TextInput.html")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "FormFields.TextInput.html")
        text_input = doc.range.form_fields[0]
        self.assertEqual("TextInput1", text_input.name)
        self.assertEqual(aw.fields.TextFormFieldType.REGULAR, text_input.text_input_type)
        self.assertEqual("", text_input.text_input_format)
        self.assertEqual("Placeholder text", text_input.result)
        self.assertEqual(0, text_input.max_length)

    def test_delete_form_field(self):
        #ExStart
        #ExFor:FormField.remove_field
        #ExSummary:Shows how to delete a form field.
        doc = aw.Document(file_name=MY_DIR + "Form fields.docx")
        form_field = doc.range.form_fields[3]
        form_field.remove_field()
        #ExEnd

        form_field_after = doc.range.form_fields[3]
        self.assertIsNone(form_field_after)

    def test_delete_form_field_associated_with_bookmark(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_form_field_font_formatting(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_drop_down_item_collection(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")
