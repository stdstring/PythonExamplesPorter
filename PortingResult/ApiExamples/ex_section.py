# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.drawing
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExSection(ApiExampleBase):
    def test_protect(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Section 1. Hello world!")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("Section 2. Hello again!")
        builder.write("Please enter text here: ")
        builder.insert_text_input("TextInput1", aw.fields.TextFormFieldType.REGULAR, "", "Placeholder text", 0)
        doc.protect(type=aw.ProtectionType.ALLOW_ONLY_FORM_FIELDS)
        doc.sections[0].protected_for_forms = False
        doc.save(file_name=ARTIFACTS_DIR + "Section.Protect.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Section.Protect.docx")
        self.assertFalse(doc.sections[0].protected_for_forms)
        self.assertTrue(doc.sections[1].protected_for_forms)

    def test_add_remove(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Section 1")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 2")
        self.assertEqual("Section 1\u000cSection 2", doc.get_text().strip())
        doc.sections.remove_at(0)
        self.assertEqual("Section 2", doc.get_text().strip())
        last_section_idx = doc.sections.count - 1
        new_section = doc.sections[last_section_idx].clone()
        doc.sections.add(new_section)
        self.assertEqual("Section 2\u000cSection 2", doc.get_text().strip())

    def test_first_and_last(self):
        doc = aw.Document()
        self.assertEqual(1, doc.sections.count)
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        self.assertEqual(2, doc.sections.count)
        doc.last_section.page_setup.text_columns.set_count(2)
        builder.writeln("Column 1.")
        builder.insert_break(aw.BreakType.COLUMN_BREAK)
        builder.writeln("Column 2.")
        self.assertEqual(1, doc.first_section.page_setup.text_columns.count)
        self.assertEqual(2, doc.last_section.page_setup.text_columns.count)
        doc.save(file_name=ARTIFACTS_DIR + "Section.Create.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Section.Create.docx")
        self.assertEqual(1, doc.first_section.page_setup.text_columns.count)
        self.assertEqual(2, doc.last_section.page_setup.text_columns.count)

    def test_create_manually(self):
        doc = aw.Document()
        doc.remove_all_children()
        section = aw.Section(doc)
        doc.append_child(section)
        section.page_setup.section_start = aw.SectionStart.NEW_PAGE
        section.page_setup.paper_size = aw.PaperSize.LETTER
        body = aw.Body(doc)
        section.append_child(body)
        para = aw.Paragraph(doc)
        para.paragraph_format.style_name = "Heading 1"
        para.paragraph_format.alignment = aw.ParagraphAlignment.CENTER
        body.append_child(para)
        run = aw.Run(doc=doc)
        run.text = "Hello World!"
        run.font.color = aspose.pydrawing.Color.red
        para.append_child(run)
        self.assertEqual("Hello World!", doc.get_text().strip())
        doc.save(file_name=ARTIFACTS_DIR + "Section.CreateManually.docx")

    def test_ensure_minimum(self):
        doc = aw.Document()
        self.assertEqual(aw.NodeType.SECTION, doc.get_child(aw.NodeType.ANY, 0, True).node_type)
        self.assertEqual(aw.NodeType.BODY, doc.sections[0].get_child(aw.NodeType.ANY, 0, True).node_type)
        self.assertEqual(aw.NodeType.PARAGRAPH, doc.sections[0].body.get_child(aw.NodeType.ANY, 0, True).node_type)
        doc.sections.add(aw.Section(doc))
        self.assertEqual(0, doc.sections[1].get_child_nodes(aw.NodeType.ANY, True).count)
        doc.last_section.ensure_minimum()
        self.assertEqual(aw.NodeType.BODY, doc.sections[1].get_child(aw.NodeType.ANY, 0, True).node_type)
        self.assertEqual(aw.NodeType.PARAGRAPH, doc.sections[1].body.get_child(aw.NodeType.ANY, 0, True).node_type)
        doc.sections[0].body.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        self.assertEqual("Hello world!", doc.get_text().strip())

    def test_body_ensure_minimum(self):
        doc = aw.Document()
        doc.remove_all_children()
        section = aw.Section(doc)
        doc.append_child(section)
        body = aw.Body(doc)
        section.append_child(body)
        self.assertEqual(0, doc.first_section.body.get_child_nodes(aw.NodeType.ANY, True).count)
        body.ensure_minimum()
        body.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        self.assertEqual("Hello world!", doc.get_text().strip())

    def test_body_child_nodes(self):
        raise NotImplementedError("Unsupported break statement usage")

    def test_clear(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        self.assertEqual(1, doc.sections.count)
        self.assertEqual(17, doc.sections[0].get_child_nodes(aw.NodeType.ANY, True).count)
        self.assertEqual("Hello World!\r\rHello Word!\r\r\rHello World!", doc.get_text().strip())
        doc.sections.clear()
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.ANY, True).count)
        self.assertEqual("", doc.get_text().strip())

    def test_prepend_append_content(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Section 1")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 2")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 3")
        section = doc.sections[2]
        self.assertEqual("Section 3" + aw.ControlChar.SECTION_BREAK, section.get_text())
        section_to_prepend = doc.sections[0]
        section.prepend_content(section_to_prepend)
        section_to_append = doc.sections[1]
        section.append_content(section_to_append)
        self.assertEqual(3, doc.sections.count)
        self.assertEqual("Section 1" + aw.ControlChar.PARAGRAPH_BREAK + "Section 3" + aw.ControlChar.PARAGRAPH_BREAK + "Section 2" + aw.ControlChar.SECTION_BREAK, section.get_text())

    def test_clear_content(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Hello world!")
        self.assertEqual("Hello world!", doc.get_text().strip())
        self.assertEqual(1, doc.first_section.body.paragraphs.count)
        doc.first_section.clear_content()
        self.assertEqual("", doc.get_text().strip())
        self.assertEqual(1, doc.first_section.body.paragraphs.count)

    def test_clear_headers_footers(self):
        doc = aw.Document()
        self.assertEqual(0, doc.first_section.headers_footers.count)
        builder = aw.DocumentBuilder(doc)
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.writeln("This is the primary header.")
        builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_PRIMARY)
        builder.writeln("This is the primary footer.")
        self.assertEqual(2, doc.first_section.headers_footers.count)
        self.assertEqual("This is the primary header.", doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY).get_text().strip())
        self.assertEqual("This is the primary footer.", doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY).get_text().strip())
        doc.first_section.clear_headers_footers()
        self.assertEqual(2, doc.first_section.headers_footers.count)
        self.assertEqual("", doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY).get_text().strip())
        self.assertEqual("", doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY).get_text().strip())

    def test_delete_header_footer_shapes(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=100, height=100)
        builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_PRIMARY)
        builder.insert_image(file_name=IMAGE_DIR + "Logo Icon.ico")
        self.assertEqual(1, doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY).get_child_nodes(aw.NodeType.SHAPE, True).count)
        self.assertEqual(1, doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY).get_child_nodes(aw.NodeType.SHAPE, True).count)
        doc.first_section.delete_header_footer_shapes()
        self.assertEqual(0, doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY).get_child_nodes(aw.NodeType.SHAPE, True).count)
        self.assertEqual(0, doc.first_section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY).get_child_nodes(aw.NodeType.SHAPE, True).count)

    def test_sections_clone_section(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        clone_section = doc.sections[0].clone()

    def test_sections_import_section(self):
        src_doc = aw.Document(file_name=MY_DIR + "Document.docx")
        dst_doc = aw.Document()
        source_section = src_doc.sections[0]
        new_section = dst_doc.import_node(src_node=source_section, is_import_children=True).as_section()
        dst_doc.sections.add(new_section)

    def test_migrate_from_2x_import_section(self):
        src_doc = aw.Document()
        dst_doc = aw.Document()
        source_section = src_doc.sections[0]
        new_section = dst_doc.import_node(src_node=source_section, is_import_children=True).as_section()
        dst_doc.sections.add(new_section)

    def test_modify_page_setup_in_all_sections(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Section 1")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 2")
        for section in doc.of_type():
            section.page_setup.paper_size = aw.PaperSize.LETTER
        doc.save(file_name=ARTIFACTS_DIR + "Section.ModifyPageSetupInAllSections.doc")
