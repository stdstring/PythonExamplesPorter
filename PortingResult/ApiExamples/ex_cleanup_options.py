# -*- coding: utf-8 -*-
import aspose.pydrawing
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
        doc = aspose.words.Document()
        my_style = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "MyStyle1")
        my_style.font.size = 14
        my_style.font.name = "Courier New"
        my_style.font.color = aspose.pydrawing.Color.blue
        duplicate_style = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "MyStyle2")
        duplicate_style.font.size = 14
        duplicate_style.font.name = "Courier New"
        duplicate_style.font.color = aspose.pydrawing.Color.blue
        self.assertEqual(6, doc.styles.count)
        builder = aspose.words.DocumentBuilder(doc)
        builder.paragraph_format.style_name = my_style.name
        builder.writeln("Hello world!")
        builder.paragraph_format.style_name = duplicate_style.name
        builder.writeln("Hello again!")
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual(my_style, paragraphs[0].paragraph_format.style)
        self.assertEqual(duplicate_style, paragraphs[1].paragraph_format.style)
        cleanup_options = aspose.words.CleanupOptions()
        cleanup_options.duplicate_style = True
        doc.cleanup(cleanup_options)
        self.assertEqual(5, doc.styles.count)
        self.assertEqual(my_style, paragraphs[0].paragraph_format.style)
        self.assertEqual(my_style, paragraphs[1].paragraph_format.style)
