# -*- coding: utf-8 -*-
import aspose.words
import unittest
from api_example_base import ApiExampleBase


class ExCleanupOptions(ApiExampleBase):
    def test_remove_unused_resources(self):
        doc = aspose.words.Document()
        doc.styles.add(aspose.words.StyleType.LIST, "MyListStyle1")
        doc.styles.add(aspose.words.StyleType.LIST, "MyListStyle2")
        doc.styles.add(aspose.words.StyleType.CHARACTER, "MyParagraphStyle1")
        doc.styles.add(aspose.words.StyleType.CHARACTER, "MyParagraphStyle2")
        self.assertEqual(8, doc.styles.count)
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.style = doc.styles.get_by_name("MyParagraphStyle1")
        builder.writeln("Hello world!")
        list = doc.lists.add(list_style = doc.styles.get_by_name("MyListStyle1"))
        builder.list_format.list = list
        builder.writeln("Item 1")
        builder.writeln("Item 2")
        cleanup_options = aspose.words.CleanupOptions()
        cleanup_options.unused_lists = True
        cleanup_options.unused_styles = True
        cleanup_options.unused_builtin_styles = True
        doc.cleanup(cleanup_options)
        self.assertEqual(4, doc.styles.count)
        doc.first_section.body.remove_all_children()
        doc.cleanup(cleanup_options)
        self.assertEqual(2, doc.styles.count)

    def test_remove_duplicate_styles(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")
