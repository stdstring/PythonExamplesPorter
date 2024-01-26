# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExFormFields(ApiExampleBase):
    def test_create(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Please select a fruit: ")
        combo_box = builder.insert_combo_box("MyComboBox", ["Apple", "Banana", "Cherry"], 0)
        self.assertEqual("MyComboBox", combo_box.name)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_FORM_DROP_DOWN, combo_box.type)
        self.assertEqual("Apple", combo_box.result)
        doc.save(file_name = ARTIFACTS_DIR + "FormFields.Create.html")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "FormFields.Create.html")
        combo_box = doc.range.form_fields[0]
        self.assertEqual("MyComboBox", combo_box.name)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_FORM_DROP_DOWN, combo_box.type)
        self.assertEqual("Apple", combo_box.result)

    def test_text_input(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Please enter text here: ")
        builder.insert_text_input("TextInput1", aspose.words.fields.TextFormFieldType.REGULAR, "", "Placeholder text", 0)
        doc.save(file_name = ARTIFACTS_DIR + "FormFields.TextInput.html")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "FormFields.TextInput.html")
        text_input = doc.range.form_fields[0]
        self.assertEqual("TextInput1", text_input.name)
        self.assertEqual(aspose.words.fields.TextFormFieldType.REGULAR, text_input.text_input_type)
        self.assertEqual("", text_input.text_input_format)
        self.assertEqual("Placeholder text", text_input.result)
        self.assertEqual(0, text_input.max_length)

    def test_delete_form_field(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Form fields.docx")
        form_field = doc.range.form_fields[3]
        form_field.remove_field()
        form_field_after = doc.range.form_fields[3]
        self.assertIsNone(form_field_after)

    def test_delete_form_field_associated_with_bookmark(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_form_field_font_formatting(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_drop_down_item_collection(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")
