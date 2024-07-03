# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.lowcode
import aspose.words.saving
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExLowCode(ApiExampleBase):
    def test_merge_documents(self):
        #ExStart
        #ExFor:Merger.merge(str,List[str])
        #ExFor:Merger.merge(List[str],MergeFormatMode)
        #ExFor:Merger.merge(str,List[str],SaveOptions,MergeFormatMode)
        #ExFor:Merger.merge(str,List[str],SaveFormat,MergeFormatMode)
        #ExSummary:Shows how to merge documents into a single output document.
        #There is a several ways to merge documents:
        aw.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SimpleMerge.docx", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"])
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.password = "Aspose.Words"
        aw.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SaveOptions.docx", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], save_options=save_options, merge_format_mode=aw.lowcode.MergeFormatMode.KEEP_SOURCE_FORMATTING)
        aw.lowcode.Merger.merge(output_file=ARTIFACTS_DIR + "LowCode.MergeDocument.SaveFormat.pdf", input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], save_format=aw.SaveFormat.PDF, merge_format_mode=aw.lowcode.MergeFormatMode.KEEP_SOURCE_LAYOUT)
        doc = aw.lowcode.Merger.merge(input_files=[MY_DIR + "Big document.docx", MY_DIR + "Tables.docx"], merge_format_mode=aw.lowcode.MergeFormatMode.MERGE_FORMATTING)
        doc.save(file_name=ARTIFACTS_DIR + "LowCode.MergeDocument.DocumentInstance.docx")
        #ExEnd

    def test_merge_stream_document(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_merge_document_instances(self):
        raise NotImplementedError("ignored method body")
