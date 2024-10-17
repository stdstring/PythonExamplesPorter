# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, MY_DIR


class ExNodeImporter(ApiExampleBase):
    def test_keep_source_numbering(self):
        for keep_source_numbering in [False, True]:
            #ExStart
            #ExFor:ImportFormatOptions.keep_source_numbering
            #ExFor:NodeImporter.__init__(DocumentBase,DocumentBase,ImportFormatMode,ImportFormatOptions)
            #ExSummary:Shows how to resolve list numbering clashes in source and destination documents.
            # Open a document with a custom list numbering scheme, and then clone it.
            # Since both have the same numbering format, the formats will clash if we import one document into the other.
            src_doc = aw.Document(file_name=MY_DIR + "Custom list numbering.docx")
            dst_doc = src_doc.clone()
            # When we import the document's clone into the original and then append it,
            # then the two lists with the same list format will join.
            # If we set the "KeepSourceNumbering" flag to "false", then the list from the document clone
            # that we append to the original will carry on the numbering of the list we append it to.
            # This will effectively merge the two lists into one.
            # If we set the "KeepSourceNumbering" flag to "true", then the document clone
            # list will preserve its original numbering, making the two lists appear as separate lists.
            import_format_options = aw.ImportFormatOptions()
            import_format_options.keep_source_numbering = keep_source_numbering
            importer = aw.NodeImporter(src_doc=src_doc, dst_doc=dst_doc, import_format_mode=aw.ImportFormatMode.KEEP_DIFFERENT_STYLES, import_format_options=import_format_options)
            for paragraph in src_doc.first_section.body.paragraphs:
                paragraph = paragraph.as_paragraph()
                imported_node = importer.import_node(paragraph, True)
                dst_doc.first_section.body.append_child(imported_node)
            dst_doc.update_list_labels()
            if keep_source_numbering:
                self.assertEqual("6. Item 1\r\n" + "7. Item 2 \r\n" + "8. Item 3\r\n" + "9. Item 4\r\n" + "6. Item 1\r\n" + "7. Item 2 \r\n" + "8. Item 3\r\n" + "9. Item 4", dst_doc.first_section.body.to_string(save_format=aw.SaveFormat.TEXT).strip())
            else:
                self.assertEqual("6. Item 1\r\n" + "7. Item 2 \r\n" + "8. Item 3\r\n" + "9. Item 4\r\n" + "10. Item 1\r\n" + "11. Item 2 \r\n" + "12. Item 3\r\n" + "13. Item 4", dst_doc.first_section.body.to_string(save_format=aw.SaveFormat.TEXT).strip())
            #ExEnd

    def test_insert_at_bookmark(self):
        raise NotImplementedError("ignored method body")
