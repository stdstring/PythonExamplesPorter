# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExFieldOptions(ApiExampleBase):
    def test_current_user(self):
        #ExStart
        #ExFor:Document.update_fields
        #ExFor:FieldOptions.current_user
        #ExFor:UserInformation
        #ExFor:UserInformation.name
        #ExFor:UserInformation.initials
        #ExFor:UserInformation.address
        #ExFor:UserInformation.default_user
        #ExSummary:Shows how to set user details, and display them using fields.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Create a UserInformation object and set it as the data source for fields that display user information.
        user_information = aw.fields.UserInformation()
        user_information.name = "John Doe"
        user_information.initials = "J. D."
        user_information.address = "123 Main Street"
        doc.field_options.current_user = user_information
        # Insert USERNAME, USERINITIALS, and USERADDRESS fields, which display values of
        # the respective properties of the UserInformation object that we have created above.
        self.assertEqual(user_information.name, builder.insert_field(field_code=" USERNAME ").result)
        self.assertEqual(user_information.initials, builder.insert_field(field_code=" USERINITIALS ").result)
        self.assertEqual(user_information.address, builder.insert_field(field_code=" USERADDRESS ").result)
        # The field options object also has a static default user that fields from all documents can refer to.
        aw.fields.UserInformation.default_user.name = "Default User"
        aw.fields.UserInformation.default_user.initials = "D. U."
        aw.fields.UserInformation.default_user.address = "One Microsoft Way"
        doc.field_options.current_user = aw.fields.UserInformation.default_user
        self.assertEqual("Default User", builder.insert_field(field_code=" USERNAME ").result)
        self.assertEqual("D. U.", builder.insert_field(field_code=" USERINITIALS ").result)
        self.assertEqual("One Microsoft Way", builder.insert_field(field_code=" USERADDRESS ").result)
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "FieldOptions.CurrentUser.docx")
        #ExEnd
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
        #ExStart
        #ExFor:FieldOptions.is_bidi_text_supported_on_update
        #ExSummary:Shows how to use FieldOptions to ensure that field updating fully supports bi-directional text.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Ensure that any field operation involving right-to-left text is performs as expected.
        doc.field_options.is_bidi_text_supported_on_update = True
        # Use a document builder to insert a field that contains the right-to-left text.
        combo_box = builder.insert_combo_box("MyComboBox", ["עֶשְׂרִים", "שְׁלוֹשִׁים", "אַרְבָּעִים", "חֲמִשִּׁים", "שִׁשִּׁים"], 0)
        combo_box.calculate_on_exit = True
        doc.update_fields()
        doc.save(file_name=ARTIFACTS_DIR + "FieldOptions.Bidi.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "FieldOptions.Bidi.docx")
        self.assertFalse(doc.field_options.is_bidi_text_supported_on_update)
        combo_box = doc.range.form_fields[0]
        self.assertEqual("עֶשְׂרִים", combo_box.result)

    def test_legacy_number_format(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_pre_process_culture(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_table_of_authority_categories(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_use_invariant_culture_number_format(self):
        raise NotImplementedError("Unsupported target type System.Threading.Thread")
