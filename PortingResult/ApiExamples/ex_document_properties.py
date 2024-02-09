# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.fields
import aspose.words.properties
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExDocumentProperties(ApiExampleBase):
    def test_built_in(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_custom(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_description(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_origin(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_content(self):
        raise NotImplementedError("Unsupported ctor for type LineCounter")

    def test_thumbnail(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_hyperlink_base(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_heading_pairs(self):
        raise NotImplementedError("Unsupported member target type - System.Object[] for expression: headingPairs")

    def test_security(self):
        doc = aspose.words.Document()
        self.assertEqual(aspose.words.properties.DocumentSecurity.NONE, doc.built_in_document_properties.security)
        doc.write_protection.read_only_recommended = True
        doc.save(file_name = ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyRecommended.docx")
        self.assertEqual(aspose.words.properties.DocumentSecurity.READ_ONLY_RECOMMENDED, aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyRecommended.docx").built_in_document_properties.security)
        doc = aspose.words.Document()
        self.assertFalse(doc.write_protection.is_write_protected)
        doc.write_protection.set_password("MyPassword")
        self.assertTrue(doc.write_protection.validate_password("MyPassword"))
        self.assertTrue(doc.write_protection.is_write_protected)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyEnforced.docx")
        self.assertEqual(aspose.words.properties.DocumentSecurity.READ_ONLY_ENFORCED, aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyEnforced.docx").built_in_document_properties.security)
        doc = aspose.words.Document()
        doc.protect(type = aspose.words.ProtectionType.ALLOW_ONLY_COMMENTS, password = "MyPassword")
        doc.built_in_document_properties.security = aspose.words.properties.DocumentSecurity.READ_ONLY_EXCEPT_ANNOTATIONS
        doc.save(file_name = ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyExceptAnnotations.docx")
        self.assertEqual(aspose.words.properties.DocumentSecurity.READ_ONLY_EXCEPT_ANNOTATIONS, aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentProperties.Security.ReadOnlyExceptAnnotations.docx").built_in_document_properties.security)

    def test_custom_named_access(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_link_custom_document_properties_to_bookmark(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_bookmark("MyBookmark")
        builder.write("Hello world!")
        builder.end_bookmark("MyBookmark")
        custom_properties = doc.custom_document_properties
        custom_property = custom_properties.add_link_to_content("Bookmark", "MyBookmark")
        self.assertEqual(True, custom_property.is_link_to_content)
        self.assertEqual("MyBookmark", custom_property.link_source)
        self.assertEqual("Hello world!", custom_property.value)
        doc.save(file_name = ARTIFACTS_DIR + "DocumentProperties.LinkCustomDocumentPropertiesToBookmark.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "DocumentProperties.LinkCustomDocumentPropertiesToBookmark.docx")
        custom_property = doc.custom_document_properties.get_by_name("Bookmark")
        self.assertEqual(True, custom_property.is_link_to_content)
        self.assertEqual("MyBookmark", custom_property.link_source)
        self.assertEqual("Hello world!", custom_property.value)

    def test_document_property_collection(self):
        raise NotImplementedError("Unsupported target type System.DateTime")
