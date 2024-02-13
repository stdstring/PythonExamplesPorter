# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, MY_DIR


class ExNode(ApiExampleBase):
    def test_clone_composite_node(self):
        doc = aspose.words.Document()
        para = doc.first_section.body.first_paragraph
        para.append_child(aspose.words.Run(doc = doc, text = "Hello world!"))
        clone_with_children = para.clone(True)
        self.assertTrue((clone_with_children.as_composite_node()).has_child_nodes)
        self.assertEqual("Hello world!", clone_with_children.get_text().strip())
        clone_without_children = para.clone(False)
        self.assertFalse((clone_without_children.as_composite_node()).has_child_nodes)
        self.assertEqual("", clone_without_children.get_text().strip())

    def test_get_parent_node(self):
        doc = aspose.words.Document()
        para = doc.first_section.body.first_paragraph
        run = aspose.words.Run(doc = doc, text = "Hello world!")
        para.append_child(run)
        self.assertEqual(para, run.parent_node)
        self.assertEqual(doc.first_section.body, para.parent_node)
        self.assertEqual(doc.first_section, doc.first_section.body.parent_node)
        self.assertEqual(doc, doc.first_section.parent_node)

    def test_owner_document(self):
        doc = aspose.words.Document()
        para = aspose.words.Paragraph(doc)
        para.append_child(aspose.words.Run(doc = doc, text = "Hello world!"))
        self.assertIsNone(para.parent_node)
        self.assertEqual(para.document, doc)
        self.assertEqual("", doc.get_text().strip())
        para.paragraph_format.style = doc.styles.get_by_name("Heading 1")
        doc.first_section.body.append_child(para)
        self.assertEqual(doc.first_section.body, para.parent_node)
        self.assertEqual("Hello world!", doc.get_text().strip())
        self.assertEqual(doc, para.document)
        self.assertIsNotNone(para.parent_node)

    def test_child_nodes_enumerate(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_recurse_children(self):
        raise NotImplementedError("Unsupported call of method named TraverseAllNodes")

    def test_remove_nodes(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Tables.docx")
        self.assertEqual(2, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)
        cur_node = doc.first_section.body.first_child
        while cur_node != None:
            next_node = cur_node.next_sibling
            if cur_node.node_type == aspose.words.NodeType.TABLE:
                cur_node.remove()
            cur_node = next_node
        self.assertEqual(0, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)

    def test_enum_next_sibling(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_typed_access(self):
        raise NotImplementedError("Unsupported expression: ConditionalAccessExpression")

    def test_remove_child(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Section 1 text.")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_CONTINUOUS)
        builder.writeln("Section 2 text.")
        last_section = doc.last_child.as_section()
        first_section = last_section.previous_sibling.as_section()
        if last_section.previous_sibling != None:
            doc.remove_child(first_section)
        self.assertEqual("Section 2 text.", doc.get_text().strip())

    def test_select_composite_nodes(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_node_is_inside_field(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_create_and_add_paragraph_node(self):
        doc = aspose.words.Document()
        para = aspose.words.Paragraph(doc)
        section = doc.last_section
        section.body.append_child(para)

    def test_remove_smart_tags_from_composite_node(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Smart tags.doc")
        self.assertEqual(8, doc.get_child_nodes(aspose.words.NodeType.SMART_TAG, True).count)
        doc.remove_smart_tags()
        self.assertEqual(0, doc.get_child_nodes(aspose.words.NodeType.SMART_TAG, True).count)

    def test_get_index_of_node(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        body = doc.first_section.body
        self.assertEqual(24, body.get_child_nodes(aspose.words.NodeType.ANY, False).index_of(body.last_paragraph))

    def test_convert_node_to_html_with_default_options(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        node = doc.last_section.body.last_paragraph
        self.assertEqual("<p style=\"margin-top:0pt; margin-bottom:8pt; line-height:108%; font-size:12pt\">" + "<span style=\"font-family:'Times New Roman'\">Hello World!</span>" + "</p>", node.to_string(save_format = aspose.words.SaveFormat.HTML))
        save_options = aspose.words.saving.HtmlSaveOptions()
        save_options.export_relative_font_size = True
        self.assertEqual("<p style=\"margin-top:0pt; margin-bottom:8pt; line-height:108%\">" + "<span style=\"font-family:'Times New Roman'\">Hello World!</span>" + "</p>", node.to_string(save_options = save_options))

    def test_typed_node_collection_to_array(self):
        raise NotImplementedError("Unsupported member target type - Aspose.Words.Paragraph[] for expression: paras")

    def test_node_enumeration_hot_remove(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("The first paragraph")
        builder.writeln("The second paragraph")
        builder.writeln("The third paragraph")
        builder.writeln("The fourth paragraph")
        for para in doc.first_section.body.paragraphs.to_array():
            if ("third" in para.range.text):
                para.remove()
        self.assertFalse(("The third paragraph" in doc.get_text()))

    def test_node_collection(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Run 1. ")
        builder.write("Run 2. ")
        runs = doc.first_section.body.first_paragraph.runs
        self.assertEqual(2, runs.count)
        new_run = aspose.words.Run(doc = doc, text = "Run 3. ")
        runs.insert(3, new_run)
        self.assertTrue(runs.contains(new_run))
        self.assertEqual("Run 1. Run 2. Run 3.", doc.get_text().strip())
        run = runs[1]
        runs.remove(run)
        self.assertEqual("Run 1. Run 3.", doc.get_text().strip())
        self.assertIsNotNone(run)
        self.assertFalse(runs.contains(run))
