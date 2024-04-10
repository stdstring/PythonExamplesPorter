# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################


import aspose.words as aw
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExBookmarks(ApiExampleBase):
    def test_insert(self):
        #ExStart
        #ExFor:Bookmark.name
        #ExSummary:Shows how to insert a bookmark.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # A valid bookmark has a name, a BookmarkStart, and a BookmarkEnd node.
        # Any whitespace in the names of bookmarks will be converted to underscores if we open the saved document with Microsoft Word.
        # If we highlight the bookmark's name in Microsoft Word via Insert -> Links -> Bookmark, and press "Go To",
        # the cursor will jump to the text enclosed between the BookmarkStart and BookmarkEnd nodes.
        builder.start_bookmark("My Bookmark")
        builder.write("Contents of MyBookmark.")
        builder.end_bookmark("My Bookmark")

        # Bookmarks are stored in this collection.
        self.assertEqual("My Bookmark", doc.range.bookmarks[0].name)
        doc.save(file_name=ARTIFACTS_DIR + "Bookmarks.Insert.docx")
        #ExEnd

        doc = aw.Document(file_name=ARTIFACTS_DIR + "Bookmarks.Insert.docx")
        self.assertEqual("My Bookmark", doc.range.bookmarks[0].name)

    def test_table_column_bookmarks(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_remove(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")
