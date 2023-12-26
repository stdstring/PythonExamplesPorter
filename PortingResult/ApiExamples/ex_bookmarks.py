# -*- coding: utf-8 -*-
import aspose.words
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExBookmarks(ApiExampleBase):
    def test_insert(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_bookmark("My Bookmark")
        builder.write("Contents of MyBookmark.")
        builder.end_bookmark("My Bookmark")
        self.assertEqual("My Bookmark", doc.range.bookmarks[0].name)
        doc.save(file_name = ARTIFACTS_DIR + "Bookmarks.Insert.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Bookmarks.Insert.docx")
        self.assertEqual("My Bookmark", doc.range.bookmarks[0].name)

    def test_table_column_bookmarks(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_remove(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")
