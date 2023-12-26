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
        raise NotImplementedError("Unsupported type: ApiExamples.LineCounter")

    def test_thumbnail(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_hyperlink_base(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_heading_pairs(self):
        raise NotImplementedError("Unsupported member target type - System.Object[] for expression: headingPairs")

    def test_security(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

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
