# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.lists
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExStyles(ApiExampleBase):
    def test_styles(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_create_style(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_style_collection(self):
        doc = aspose.words.Document()
        styles = doc.styles
        styles.default_font.name = "Courier New"
        styles.default_paragraph_format.first_line_indent = 15
        styles.add(aspose.words.StyleType.PARAGRAPH, "MyStyle")
        self.assertEqual("Courier New", styles[4].font.name)
        self.assertEqual(15, styles.get_by_name("MyStyle").paragraph_format.first_line_indent)

    def test_remove_styles_from_style_gallery(self):
        doc = aspose.words.Document()
        doc.styles.clear_quick_style_gallery()
        doc.save(file_name = ARTIFACTS_DIR + "Styles.RemoveStylesFromStyleGallery.docx")

    def test_change_tocs_tab_stops(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Table of contents.docx")
        # for each loop begin
        for para in doc.get_child_nodes(aspose.words.NodeType.PARAGRAPH, True).of_type():
            # if begin
            if para.paragraph_format.style.style_identifier >= aspose.words.StyleIdentifier.TOC1 and para.paragraph_format.style.style_identifier <= aspose.words.StyleIdentifier.TOC9:
                tab = para.paragraph_format.tab_stops[0]
                para.paragraph_format.tab_stops.remove_by_position(tab.position)
                para.paragraph_format.tab_stops.add(position = tab.position - 50, alignment = tab.alignment, leader = tab.leader)
            # if end
        # for loop end
        doc.save(file_name = ARTIFACTS_DIR + "Styles.ChangeTocsTabStops.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Styles.ChangeTocsTabStops.docx")
        # for each loop begin
        for para in doc.get_child_nodes(aspose.words.NodeType.PARAGRAPH, True).of_type():
            # if begin
            if para.paragraph_format.style.style_identifier >= aspose.words.StyleIdentifier.TOC1 and para.paragraph_format.style.style_identifier <= aspose.words.StyleIdentifier.TOC9:
                tab_stop = para.get_effective_tab_stops()[0]
                self.assertEqual(400.8, tab_stop.position)
                self.assertEqual(aspose.words.TabAlignment.RIGHT, tab_stop.alignment)
                self.assertEqual(aspose.words.TabLeader.DOTS, tab_stop.leader)
            # if end
        # for loop end

    def test_copy_style_same_document(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_copy_style_different_document(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_default_styles(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_paragraph_style_bulleted_list(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        style = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "MyStyle1")
        style.font.size = 24
        style.font.name = "Verdana"
        style.paragraph_format.space_after = 12
        style.list_format.list = doc.lists.add(list_template = aspose.words.lists.ListTemplate.BULLET_DEFAULT)
        style.list_format.list_level_number = 0
        builder.paragraph_format.style = style
        builder.writeln("Hello World: MyStyle1, bulleted list.")
        builder.paragraph_format.style = doc.styles.get_by_name("Normal")
        builder.writeln("Hello World: Normal.")
        builder.document.save(file_name = ARTIFACTS_DIR + "Styles.ParagraphStyleBulletedList.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Styles.ParagraphStyleBulletedList.docx")
        style = doc.styles.get_by_name("MyStyle1")
        self.assertEqual("MyStyle1", style.name)
        self.assertEqual(24, style.font.size)
        self.assertEqual("Verdana", style.font.name)
        self.assertEqual(12, style.paragraph_format.space_after)

    def test_style_aliases(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Style with alias.docx")
        style = doc.styles.get_by_name("MyStyle")
        self.assertSequenceEqual(["MyStyle Alias 1", "MyStyle Alias 2"], style.aliases)
        self.assertEqual("Title", style.base_style_name)
        self.assertEqual("MyStyle Char", style.linked_style_name)
        self.assertEqual(doc.styles.get_by_name("MyStyle Alias 1"), doc.styles.get_by_name("MyStyle Alias 2"))
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.paragraph_format.style = doc.styles.get_by_name("MyStyle Alias 1")
        builder.writeln("Hello world!")
        builder.paragraph_format.style = doc.styles.get_by_name("MyStyle Alias 2")
        builder.write("Hello again!")
        self.assertEqual(doc.first_section.body.paragraphs[0].paragraph_format.style, doc.first_section.body.paragraphs[1].paragraph_format.style)

    def test_latent_styles(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")
