# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.lowcode
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExLowCode(ApiExampleBase):
    def test_merge_documents(self):
        aspose.words.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SimpleMerge.docx", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"])
        save_options = aspose.words.saving.OoxmlSaveOptions()
        save_options.password = "Aspose.Words"
        aspose.words.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SaveOptions.docx", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], save_options=save_options, merge_format_mode=aspose.words.lowcode.MergeFormatMode.KEEP_SOURCE_FORMATTING)
        aspose.words.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SaveFormat.pdf", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], save_format=aspose.words.SaveFormat.PDF, merge_format_mode=aspose.words.lowcode.MergeFormatMode.KEEP_SOURCE_LAYOUT)
        doc = aspose.words.lowcode.Merger.merge(input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], merge_format_mode=aspose.words.lowcode.MergeFormatMode.MERGE_FORMATTING)
        doc.save(file_name=ARTIFACTS_DIR + "LowCode.MergeDocument.DocumentInstance.docx")

    def test_merge_stream_document(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_merge_document_instances(self):
        first_doc = aspose.words.DocumentBuilder()
        first_doc.font.size = 16
        first_doc.font.color = aspose.pydrawing.Color.blue
        first_doc.write("Hello first word!")
        second_doc = aspose.words.DocumentBuilder()
        second_doc.write("Hello second word!")
        merged_doc = aspose.words.lowcode.Merger.merge(input_documents=[first_doc.document, second_doc.document], merge_format_mode=aspose.words.lowcode.MergeFormatMode.KEEP_SOURCE_LAYOUT)
        self.assertEqual("Hello first word!\fHello second word!\f", merged_doc.get_text())
