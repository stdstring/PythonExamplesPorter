# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.fields
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExSection(ApiExampleBase):
    def test_protect(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_add_remove(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_first_and_last(self):
        doc = aspose.words.Document()
        self.assertEqual(1, doc.sections.count)
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        self.assertEqual(2, doc.sections.count)
        doc.last_section.page_setup.text_columns.set_count(2)
        builder.writeln("Column 1.")
        builder.insert_break(aspose.words.BreakType.COLUMN_BREAK)
        builder.writeln("Column 2.")
        self.assertEqual(1, doc.first_section.page_setup.text_columns.count)
        self.assertEqual(2, doc.last_section.page_setup.text_columns.count)
        doc.save(file_name = ARTIFACTS_DIR + "Section.Create.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Section.Create.docx")
        self.assertEqual(1, doc.first_section.page_setup.text_columns.count)
        self.assertEqual(2, doc.last_section.page_setup.text_columns.count)

    def test_create_manually(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_ensure_minimum(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_body_ensure_minimum(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_body_child_nodes(self):
        raise NotImplementedError("Unsupported break statement usage")

    def test_clear(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_prepend_append_content(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Section 1")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 2")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 3")
        section = doc.sections[2]
        self.assertEqual("Section 3" + aspose.words.ControlChar.SECTION_BREAK, section.get_text())
        section_to_prepend = doc.sections[0]
        section.prepend_content(section_to_prepend)
        section_to_append = doc.sections[1]
        section.append_content(section_to_append)
        self.assertEqual(3, doc.sections.count)
        self.assertEqual("Section 1" + aspose.words.ControlChar.PARAGRAPH_BREAK + "Section 3" + aspose.words.ControlChar.PARAGRAPH_BREAK + "Section 2" + aspose.words.ControlChar.SECTION_BREAK, section.get_text())

    def test_clear_content(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_clear_headers_footers(self):
        raise NotImplementedError("Unsupported type of expression: HeaderFooterType.HeaderPrimary")

    def test_delete_header_footer_shapes(self):
        raise NotImplementedError("Unsupported type of expression: HeaderFooterType.HeaderPrimary")

    def test_sections_clone_section(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        clone_section = doc.sections[0].clone()

    def test_sections_import_section(self):
        src_doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        dst_doc = aspose.words.Document()
        source_section = src_doc.sections[0]
        new_section = dst_doc.import_node(src_node = source_section, is_import_children = True).as_section()
        dst_doc.sections.add(new_section)

    def test_migrate_from_2x_import_section(self):
        src_doc = aspose.words.Document()
        dst_doc = aspose.words.Document()
        source_section = src_doc.sections[0]
        new_section = dst_doc.import_node(src_node = source_section, is_import_children = True).as_section()
        dst_doc.sections.add(new_section)

    def test_modify_page_setup_in_all_sections(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Section 1")
        builder.insert_break(aspose.words.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.write("Section 2")
        # for each loop begin
        for section in doc.of_type():
            section.page_setup.paper_size = aspose.words.PaperSize.LETTER
        # for loop end
        doc.save(file_name = ARTIFACTS_DIR + "Section.ModifyPageSetupInAllSections.doc")
