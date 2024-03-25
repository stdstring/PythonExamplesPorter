# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExFieldOptions(ApiExampleBase):
    def test_current_user(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        user_information = aw.fields.UserInformation()
        user_information.name = "John Doe"
        user_information.initials = "J. D."
        user_information.address = "123 Main Street"
        doc.field_options.current_user = user_information
        self.assertEqual(user_information.name, builder.insert_field(field_code=" USERNAME ").result)
        self.assertEqual(user_information.initials, builder.insert_field(field_code=" USERINITIALS ").result)
        self.assertEqual(user_information.address, builder.insert_field(field_code=" USERADDRESS ").result)
        aw.fields.UserInformation.default_user.name = "Default User"
        aw.fields.UserInformation.default_user.initials = "D. U."
        aw.fields.UserInformation.default_user.address = "One Microsoft Way"
        doc.field_options.current_user = aw.fields.UserInformation.default_user
        self.assertEqual("Default User", builder.insert_field(field_code=" USERNAME ").result)
        self.assertEqual("D. U.", builder.insert_field(field_code=" USERINITIALS ").result)
        self.assertEqual("One Microsoft Way", builder.insert_field(field_code=" USERADDRESS ").result)
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "FieldOptions.CurrentUser.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "FieldOptions.CurrentUser.docx")
        self.assertIsNone(doc.field_options.current_user)
        field_user_name = doc.range.fields[0].as_field_user_name()
        self.assertIsNone(field_user_name.user_name)
        self.assertEqual("Default User", field_user_name.result)
        field_user_initials = doc.range.fields[1].as_field_user_initials()
        self.assertIsNone(field_user_initials.user_initials)
        self.assertEqual("D. U.", field_user_initials.result)
        field_user_address = doc.range.fields[2].as_field_user_address()
        self.assertIsNone(field_user_address.user_address)
        self.assertEqual("One Microsoft Way", field_user_address.result)

    def test_file_name(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_bidi(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        doc.field_options.is_bidi_text_supported_on_update = True
        combo_box = builder.insert_combo_box("MyComboBox", ["עֶשְׂרִים", "שְׁלוֹשִׁים", "אַרְבָּעִים", "חֲמִשִּׁים", "שִׁשִּׁים"], 0)
        combo_box.calculate_on_exit = True
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "FieldOptions.Bidi.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "FieldOptions.Bidi.docx")
        self.assertFalse(doc.field_options.is_bidi_text_supported_on_update)
        combo_box = doc.range.form_fields[0]
        self.assertEqual("עֶשְׂרִים", combo_box.result)

    def test_legacy_number_format(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_table_of_authority_categories(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")
