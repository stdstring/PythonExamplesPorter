# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.fields
import aspose.words.properties
import datetime
import system_helper
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExDocumentProperties(ApiExampleBase):
    def test_built_in(self):
        raise NotImplementedError("Unsupported expression: GenericName")

    def test_custom(self):
        raise NotImplementedError("ignored method body")

    def test_description(self):
        #ExStart
        #ExFor:BuiltInDocumentProperties.author
        #ExFor:BuiltInDocumentProperties.category
        #ExFor:BuiltInDocumentProperties.comments
        #ExFor:BuiltInDocumentProperties.keywords
        #ExFor:BuiltInDocumentProperties.subject
        #ExFor:BuiltInDocumentProperties.title
        #ExSummary:Shows how to work with built-in document properties in the "Description" category.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        properties = doc.built_in_document_properties
        # Below are four built-in document properties that have fields that can display their values in the document body.
        # 1 -  "Author" property, which we can display using an AUTHOR field:
        properties.author = "John Doe"
        builder.write("Author:\t")
        builder.insert_field(field_type=aw.fields.FieldType.FIELD_AUTHOR, update_field=True)
        # 2 -  "Title" property, which we can display using a TITLE field:
        properties.title = "John's Document"
        builder.write("\nDoc title:\t")
        builder.insert_field(field_type=aw.fields.FieldType.FIELD_TITLE, update_field=True)
        # 3 -  "Subject" property, which we can display using a SUBJECT field:
        properties.subject = "My subject"
        builder.write("\nSubject:\t")
        builder.insert_field(field_type=aw.fields.FieldType.FIELD_SUBJECT, update_field=True)
        # 4 -  "Comments" property, which we can display using a COMMENTS field:
        properties.comments = f"This is {properties.author}'s document about {properties.subject}"
        builder.write("\nComments:\t\"")
        builder.insert_field(field_type=aw.fields.FieldType.FIELD_COMMENTS, update_field=True)
        builder.write("\"")
        # The "Category" built-in property does not have a field that can display its value.
        properties.category = "My category"
        # We can set multiple keywords for a document by separating the string value of the "Keywords" property with semicolons.
        properties.keywords = "Tag 1; Tag 2; Tag 3"
        # We can right-click this document in Windows Explorer and find these properties in "Properties" -> "Details".
        # The "Author" built-in property is in the "Origin" group, and the others are in the "Description" group.
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.Description.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.Description.docx")
        properties = doc.built_in_document_properties
        self.assertEqual("John Doe", properties.author)
        self.assertEqual("My category", properties.category)
        self.assertEqual(f"This is {properties.author}'s document about {properties.subject}", properties.comments)
        self.assertEqual("Tag 1; Tag 2; Tag 3", properties.keywords)
        self.assertEqual("My subject", properties.subject)
        self.assertEqual("John's Document", properties.title)
        self.assertEqual("Author:\t\u0013 AUTHOR \u0014John Doe\u0015\r" + "Doc title:\t\u0013 TITLE \u0014John's Document\u0015\r" + "Subject:\t\u0013 SUBJECT \u0014My subject\u0015\r" + "Comments:\t\"\u0013 COMMENTS \u0014This is John Doe's document about My subject\u0015\"", doc.get_text().strip())

    def test_origin(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_content(self):
        raise NotImplementedError("ignored method body")

    def test_thumbnail(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_hyperlink_base(self):
        #ExStart
        #ExFor:BuiltInDocumentProperties.hyperlink_base
        #ExSummary:Shows how to store the base part of a hyperlink in the document's properties.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Insert a relative hyperlink to a document in the local file system named "Document.docx".
        # Clicking on the link in Microsoft Word will open the designated document, if it is available.
        builder.insert_hyperlink("Relative hyperlink", "Document.docx", False)
        # This link is relative. If there is no "Document.docx" in the same folder
        # as the document that contains this link, the link will be broken.
        self.assertFalse(system_helper.io.File.exist(ARTIFACTS_DIR + "Document.docx"))
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.HyperlinkBase.BrokenLink.docx")
        # The document we are trying to link to is in a different directory to the one we are planning to save the document in.
        # We could fix links like this by putting an absolute filename in each one.
        # Alternatively, we could provide a base link that every hyperlink with a relative filename
        # will prepend to its link when we click on it.
        properties = doc.built_in_document_properties
        properties.hyperlink_base = MY_DIR
        self.assertTrue(system_helper.io.File.exist(properties.hyperlink_base + (doc.range.fields[0].as_field_hyperlink()).address))
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.HyperlinkBase.WorkingLink.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.HyperlinkBase.BrokenLink.docx")
        properties = doc.built_in_document_properties
        self.assertEqual("", properties.hyperlink_base)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.HyperlinkBase.WorkingLink.docx")
        properties = doc.built_in_document_properties
        self.assertEqual(MY_DIR, properties.hyperlink_base)
        self.assertTrue(system_helper.io.File.exist(properties.hyperlink_base + (doc.range.fields[0].as_field_hyperlink()).address))

    def test_heading_pairs(self):
        raise NotImplementedError("Unsupported member target type - System.Object[] for expression: headingPairs")

    def test_security(self):
        #ExStart
        #ExFor:BuiltInDocumentProperties.security
        #ExFor:DocumentSecurity
        #ExSummary:Shows how to use document properties to display the security level of a document.
        doc = aw.Document()
        self.assertEqual(aw.properties.DocumentSecurity.NONE, doc.built_in_document_properties.security)
        # If we configure a document to be read-only, it will display this status using the "Security" built-in property.
        doc.write_protection.read_only_recommended = True
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyRecommended.docx")
        self.assertEqual(aw.properties.DocumentSecurity.READ_ONLY_RECOMMENDED, aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyRecommended.docx").built_in_document_properties.security)
        # Write-protect a document, and then verify its security level.
        doc = aw.Document()
        self.assertFalse(doc.write_protection.is_write_protected)
        doc.write_protection.set_password("MyPassword")
        self.assertTrue(doc.write_protection.validate_password("MyPassword"))
        self.assertTrue(doc.write_protection.is_write_protected)
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyEnforced.docx")
        self.assertEqual(aw.properties.DocumentSecurity.READ_ONLY_ENFORCED, aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyEnforced.docx").built_in_document_properties.security)
        # "Security" is a descriptive property. We can edit its value manually.
        doc = aw.Document()
        doc.protect(type=aw.ProtectionType.ALLOW_ONLY_COMMENTS, password="MyPassword")
        doc.built_in_document_properties.security = aw.properties.DocumentSecurity.READ_ONLY_EXCEPT_ANNOTATIONS
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyExceptAnnotations.docx")
        self.assertEqual(aw.properties.DocumentSecurity.READ_ONLY_EXCEPT_ANNOTATIONS, aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyExceptAnnotations.docx").built_in_document_properties.security)
        #ExEnd

    def test_custom_named_access(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_link_custom_document_properties_to_bookmark(self):
        #ExStart
        #ExFor:CustomDocumentProperties.add_link_to_content(str,str)
        #ExFor:DocumentProperty.is_link_to_content
        #ExFor:DocumentProperty.link_source
        #ExSummary:Shows how to link a custom document property to a bookmark.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        builder.start_bookmark("MyBookmark")
        builder.write("Hello world!")
        builder.end_bookmark("MyBookmark")
        # Link a new custom property to a bookmark. The value of this property
        # will be the contents of the bookmark that it references in the "LinkSource" member.
        custom_properties = doc.custom_document_properties
        custom_property = custom_properties.add_link_to_content("Bookmark", "MyBookmark")
        self.assertEqual(True, custom_property.is_link_to_content)
        self.assertEqual("MyBookmark", custom_property.link_source)
        self.assertEqual("Hello world!", custom_property.value)
        doc.save(file_name=ARTIFACTS_DIR + "DocumentProperties.LinkCustomDocumentPropertiesToBookmark.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "DocumentProperties.LinkCustomDocumentPropertiesToBookmark.docx")
        custom_property = doc.custom_document_properties.get_by_name("Bookmark")
        self.assertEqual(True, custom_property.is_link_to_content)
        self.assertEqual("MyBookmark", custom_property.link_source)
        self.assertEqual("Hello world!", custom_property.value)

    def test_document_property_collection(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_property_types(self):
        #ExStart
        #ExFor:DocumentProperty.to_bool
        #ExFor:DocumentProperty.to_int
        #ExFor:DocumentProperty.to_double
        #ExFor:DocumentProperty.__str__
        #ExFor:DocumentProperty.to_date_time
        #ExSummary:Shows various type conversion methods of custom document properties.
        doc = aw.Document()
        properties = doc.custom_document_properties
        auth_date = datetime.date.today()
        properties.add(name="Authorized", value=True)
        properties.add(name="Authorized By", value="John Doe")
        properties.add(name="Authorized Date", value=auth_date)
        properties.add(name="Authorized Revision", value=doc.built_in_document_properties.revision_number)
        properties.add(name="Authorized Amount", value=123.45)
        self.assertEqual(True, properties.get_by_name("Authorized").to_bool())
        self.assertEqual("John Doe", properties.get_by_name("Authorized By").to_string())
        self.assertEqual(auth_date, properties.get_by_name("Authorized Date").to_date_time())
        self.assertEqual(1, properties.get_by_name("Authorized Revision").to_int())
        self.assertEqual(123.45, properties.get_by_name("Authorized Amount").to_double())
        #ExEnd
