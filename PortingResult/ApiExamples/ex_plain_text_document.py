# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.loading
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExPlainTextDocument(ApiExampleBase):
    def test_load(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.save(file_name=ARTIFACTS_DIR + "PlainTextDocument.Load.docx")
        plaintext = aw.PlainTextDocument(file_name=ARTIFACTS_DIR + "PlainTextDocument.Load.docx")
        self.assertEqual("Hello world!", plaintext.text.strip())

    def test_load_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_load_encrypted(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.password = "MyPassword"
        doc.save(file_name=ARTIFACTS_DIR + "PlainTextDocument.LoadEncrypted.docx", save_options=save_options)
        load_options = aw.loading.LoadOptions()
        load_options.password = "MyPassword"
        plaintext = aw.PlainTextDocument(file_name=ARTIFACTS_DIR + "PlainTextDocument.LoadEncrypted.docx", load_options=load_options)
        self.assertEqual("Hello world!", plaintext.text.strip())

    def test_load_encrypted_using_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_built_in_properties(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.built_in_document_properties.author = "John Doe"
        doc.save(file_name=ARTIFACTS_DIR + "PlainTextDocument.BuiltInProperties.docx")
        plaintext = aw.PlainTextDocument(file_name=ARTIFACTS_DIR + "PlainTextDocument.BuiltInProperties.docx")
        self.assertEqual("Hello world!", plaintext.text.strip())
        self.assertEqual("John Doe", plaintext.built_in_document_properties.author)

    def test_custom_document_properties(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        doc.custom_document_properties.add(name="Location of writing", value="123 Main St, London, UK")
        doc.save(file_name=ARTIFACTS_DIR + "PlainTextDocument.CustomDocumentProperties.docx")
        plaintext = aw.PlainTextDocument(file_name=ARTIFACTS_DIR + "PlainTextDocument.CustomDocumentProperties.docx")
        self.assertEqual("Hello world!", plaintext.text.strip())
        self.assertEqual("123 Main St, London, UK", plaintext.custom_document_properties.get_by_name("Location of writing").value)
