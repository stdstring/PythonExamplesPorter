# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.lowcode
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExLowCode(ApiExampleBase):
    def test_merge_documents(self):
        aw.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SimpleMerge.docx", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"])
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.password = "Aspose.Words"
        aw.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SaveOptions.docx", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], save_options=save_options, merge_format_mode=aw.lowcode.MergeFormatMode.KEEP_SOURCE_FORMATTING)
        aw.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SaveFormat.pdf", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], save_format=aw.SaveFormat.PDF, merge_format_mode=aw.lowcode.MergeFormatMode.KEEP_SOURCE_LAYOUT)
        doc = aw.lowcode.Merger.merge(input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], merge_format_mode=aw.lowcode.MergeFormatMode.MERGE_FORMATTING)
        doc.save(file_name=ARTIFACTS_DIR + "LowCode.MergeDocument.DocumentInstance.docx")

    def test_merge_stream_document(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_merge_document_instances(self):
        first_doc = aw.DocumentBuilder()
        first_doc.font.size = 16
        first_doc.font.color = aspose.pydrawing.Color.blue
        first_doc.write("Hello first word!")
        second_doc = aw.DocumentBuilder()
        second_doc.write("Hello second word!")
        merged_doc = aw.lowcode.Merger.merge(input_documents=[first_doc.document, second_doc.document], merge_format_mode=aw.lowcode.MergeFormatMode.KEEP_SOURCE_LAYOUT)
        self.assertEqual("Hello first word!\fHello second word!\f", merged_doc.get_text())
