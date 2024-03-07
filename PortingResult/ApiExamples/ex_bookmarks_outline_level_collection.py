# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR


class ExBookmarksOutlineLevelCollection(ApiExampleBase):
    def test_bookmark_levels(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.start_bookmark("Bookmark 1")
        builder.writeln("Text inside Bookmark 1.")
        builder.start_bookmark("Bookmark 2")
        builder.writeln("Text inside Bookmark 1 and 2.")
        builder.end_bookmark("Bookmark 2")
        builder.writeln("Text inside Bookmark 1.")
        builder.end_bookmark("Bookmark 1")
        builder.start_bookmark("Bookmark 3")
        builder.writeln("Text inside Bookmark 3.")
        builder.end_bookmark("Bookmark 3")
        pdf_save_options = aspose.words.saving.PdfSaveOptions()
        outline_levels = pdf_save_options.outline_options.bookmarks_outline_levels
        outline_levels.add("Bookmark 1", 1)
        outline_levels.add("Bookmark 2", 2)
        outline_levels.add("Bookmark 3", 3)
        self.assertEqual(3, outline_levels.count)
        self.assertTrue(outline_levels.contains("Bookmark 1"))
        self.assertEqual(1, outline_levels[0])
        self.assertEqual(2, outline_levels.get_by_name("Bookmark 2"))
        self.assertEqual(2, outline_levels.index_of_key("Bookmark 3"))
        outline_levels.remove_at(2)
        outline_levels.remove("Bookmark 2")
        outline_levels.add("Bookmark 2", 5)
        outline_levels.add("Bookmark 3", 9)
        doc.save(file_name=ARTIFACTS_DIR + "BookmarksOutlineLevelCollection.BookmarkLevels.pdf", save_options=pdf_save_options)
        outline_levels.clear()

    def test_use_pdf_bookmark_editor_for_bookmark_levels(self):
        raise NotImplementedError("Unsupported call of method named BookmarkLevels")
