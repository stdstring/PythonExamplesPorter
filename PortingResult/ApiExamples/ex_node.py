# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.saving
import unittest
from api_example_base import ApiExampleBase, MY_DIR


class ExNode(ApiExampleBase):
    def test_clone_composite_node(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

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
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_child_nodes_enumerate(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_recurse_children(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_remove_nodes(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Tables.docx")
        self.assertEqual(2, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)
        cur_node = doc.first_section.body.first_child
        # while begin
        while cur_node != None:
            next_node = cur_node.next_sibling
            # if begin
            if cur_node.node_type == aspose.words.NodeType.TABLE:
                cur_node.remove()
            # if end
            cur_node = next_node
        # while end
        self.assertEqual(0, doc.get_child_nodes(aspose.words.NodeType.TABLE, True).count)

    def test_enum_next_sibling(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_typed_access(self):
        raise NotImplementedError("Unsupported expression: ConditionalAccessExpression")

    def test_remove_child(self):
        raise NotImplementedError("Unsupported target type System.String")

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
        raise NotImplementedError("Unsupported target type System.String")

    def test_node_collection(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")
