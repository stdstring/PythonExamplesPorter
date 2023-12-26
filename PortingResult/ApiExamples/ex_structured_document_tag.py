# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.markup
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExStructuredDocumentTag(ApiExampleBase):
    def test_repeating_section(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_flat_opc_content(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_apply_style(self):
        raise NotImplementedError("Unsupported type of expression: StyleIdentifier.Quote")

    def test_check_box(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_date(self):
        raise NotImplementedError("Unsupported target type System.Globalization.CultureInfo")

    def test_plain_text(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_lock(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_list_item_collection(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_creating_custom_xml(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_data_checksum(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_xml_mapping(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_structured_document_tag_range_start_xml_mapping(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_custom_xml_schema_collection(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_custom_xml_part_store_item_id_read_only(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Custom XML part in structured document tag.docx")
        tag = doc.get_child(aspose.words.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual("{F3029283-4FF8-4DD2-9F31-395F19ACEE85}", tag.xml_mapping.store_item_id)

    def test_custom_xml_part_store_item_id_read_only_null(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_clear_text_from_structured_document_tags(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_access_to_building_block_properties_from_doc_part_obj_sdt(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Structured document tags with building blocks.docx")
        doc_part_obj_sdt = doc.get_child(aspose.words.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual(aspose.words.markup.SdtType.DOC_PART_OBJ, doc_part_obj_sdt.sdt_type)
        self.assertEqual("Table of Contents", doc_part_obj_sdt.building_block_gallery)

    def test_access_to_building_block_properties_from_plain_text_sdt(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_building_block_categories(self):
        doc = aspose.words.Document()
        building_block_sdt = aspose.words.markup.StructuredDocumentTag(doc, aspose.words.markup.SdtType.BUILDING_BLOCK_GALLERY, aspose.words.markup.MarkupLevel.BLOCK)
        building_block_sdt.building_block_category = "Built-in"
        building_block_sdt.building_block_gallery = "Table of Contents"
        doc.first_section.body.append_child(building_block_sdt)
        doc.save(file_name = ARTIFACTS_DIR + "StructuredDocumentTag.BuildingBlockCategories.docx")
        building_block_sdt = doc.first_section.body.get_child(aspose.words.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual(aspose.words.markup.SdtType.BUILDING_BLOCK_GALLERY, building_block_sdt.sdt_type)
        self.assertEqual("Table of Contents", building_block_sdt.building_block_gallery)
        self.assertEqual("Built-in", building_block_sdt.building_block_category)

    def test_update_sdt_content(self):
        raise NotImplementedError("Unsupported type: Aspose.Pdf.Document")

    def test_fill_table_using_repeating_section_item(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_custom_xml_part(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_multi_section_tags(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_sdt_child_nodes(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_sdt_range_extended_methods(self):
        raise NotImplementedError("Unsupported argument kind: ref")

    def test_get_sdt(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_range_sdt(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_sdt_at_row_level(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        table = builder.start_table()
        group_sdt = aspose.words.markup.StructuredDocumentTag(doc, aspose.words.markup.SdtType.GROUP, aspose.words.markup.MarkupLevel.ROW)
        table.append_child(group_sdt)
        group_sdt.is_showing_placeholder_text = False
        group_sdt.remove_all_children()
        row = aspose.words.tables.Row(doc)
        group_sdt.append_child(row)
        cell = aspose.words.tables.Cell(doc)
        row.append_child(cell)
        builder.end_table()
        cell.ensure_minimum()
        builder.move_to(cell.last_paragraph)
        builder.write("Lorem ipsum dolor.")
        builder.move_to(table.next_sibling)
        builder.write("Nulla blandit nisi.")
        doc.save(file_name = ARTIFACTS_DIR + "StructuredDocumentTag.SdtAtRowLevel.docx")

    def test_ignore_structured_document_tags(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_citation(self):
        doc = aspose.words.Document()
        sdt = aspose.words.markup.StructuredDocumentTag(doc, aspose.words.markup.SdtType.CITATION, aspose.words.markup.MarkupLevel.INLINE)
        paragraph = doc.first_section.body.first_paragraph
        paragraph.append_child(sdt)
        builder = aspose.words.DocumentBuilder(doc)
        builder.move_to_paragraph(0, -1)
        builder.insert_field(field_code = """CITATION Ath22 \l 1033 """, field_value = "(John Lennon, 2022)")
        # while begin
        while sdt.next_sibling != None:
            sdt.append_child(sdt.next_sibling)
        # while end
        doc.save(file_name = ARTIFACTS_DIR + "StructuredDocumentTag.Citation.docx")
