# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
import aspose.words.buildingblocks
import aspose.words.markup
import aspose.words.replacing
import aspose.words.tables
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExStructuredDocumentTag(ApiExampleBase):
    def test_repeating_section(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_flat_opc_content(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_apply_style(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_check_box(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_date(self):
        raise NotImplementedError("Unsupported target type System.Globalization.CultureInfo")

    def test_plain_text(self):
        doc = aw.Document()
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        tag.title = "My plain text"
        tag.color = aspose.pydrawing.Color.magenta
        tag.tag = "MyPlainTextSDT"
        self.assertTrue(tag.id > 0)
        tag.contents_font.name = "Arial"
        tag.end_character_font.name = "Arial Black"
        tag.multiline = True
        tag.appearance = aw.markup.SdtAppearance.TAGS
        builder = aw.DocumentBuilder(doc)
        builder.insert_node(tag)
        tag_clone = tag.clone(True).as_structured_document_tag()
        builder.insert_paragraph()
        builder.insert_node(tag_clone)
        tag_clone.remove_self_only()
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.PlainText.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.PlainText.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual("My plain text", tag.title)
        self.assertEqual(aspose.pydrawing.Color.magenta.to_argb(), tag.color.to_argb())
        self.assertEqual("MyPlainTextSDT", tag.tag)
        self.assertTrue(tag.id > 0)
        self.assertEqual("Arial", tag.contents_font.name)
        self.assertEqual("Arial Black", tag.end_character_font.name)
        self.assertTrue(tag.multiline)
        self.assertEqual(aw.markup.SdtAppearance.TAGS, tag.appearance)

    def test_is_temporary(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_placeholder_building_block(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_lock(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        tag.lock_contents = True
        builder.write("The contents of this structured document tag cannot be edited: ")
        builder.insert_node(tag)
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        tag.lock_content_control = True
        builder.insert_paragraph()
        builder.write("This structured document tag cannot be deleted but its contents can be edited: ")
        builder.insert_node(tag)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.Lock.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.Lock.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertTrue(tag.lock_contents)
        self.assertFalse(tag.lock_content_control)
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 1, True).as_structured_document_tag()
        self.assertFalse(tag.lock_contents)
        self.assertTrue(tag.lock_content_control)

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
        doc = aw.Document(file_name=MY_DIR + "Custom XML part in structured document tag.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual("{F3029283-4FF8-4DD2-9F31-395F19ACEE85}", tag.xml_mapping.store_item_id)

    def test_custom_xml_part_store_item_id_read_only_null(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_clear_text_from_structured_document_tags(self):
        doc = aw.Document()
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)
        doc.first_section.body.append_child(tag)
        self.assertEqual("Click here to enter text.", tag.get_text().strip())
        self.assertTrue(tag.is_showing_placeholder_text)
        glossary_doc = doc.glossary_document
        substitute_block = aw.buildingblocks.BuildingBlock(glossary_doc)
        substitute_block.name = "My placeholder"
        substitute_block.append_child(aw.Section(glossary_doc))
        substitute_block.first_section.ensure_minimum()
        substitute_block.first_section.body.first_paragraph.append_child(aw.Run(doc=glossary_doc, text="Custom placeholder text."))
        glossary_doc.append_child(substitute_block)
        tag.placeholder_name = "My placeholder"
        self.assertEqual("Custom placeholder text.", tag.get_text().strip())
        self.assertTrue(tag.is_showing_placeholder_text)
        run = tag.get_child(aw.NodeType.RUN, 0, True).as_run()
        run.text = "New text."
        tag.is_showing_placeholder_text = False
        self.assertEqual("New text.", tag.get_text().strip())
        tag.clear()
        self.assertTrue(tag.is_showing_placeholder_text)
        self.assertEqual("Custom placeholder text.", tag.get_text().strip())

    def test_access_to_building_block_properties_from_doc_part_obj_sdt(self):
        doc = aw.Document(file_name=MY_DIR + "Structured document tags with building blocks.docx")
        doc_part_obj_sdt = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual(aw.markup.SdtType.DOC_PART_OBJ, doc_part_obj_sdt.sdt_type)
        self.assertEqual("Table of Contents", doc_part_obj_sdt.building_block_gallery)

    def test_access_to_building_block_properties_from_plain_text_sdt(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_building_block_categories(self):
        doc = aw.Document()
        building_block_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.BUILDING_BLOCK_GALLERY, aw.markup.MarkupLevel.BLOCK)
        building_block_sdt.building_block_category = "Built-in"
        building_block_sdt.building_block_gallery = "Table of Contents"
        doc.first_section.body.append_child(building_block_sdt)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.BuildingBlockCategories.docx")
        building_block_sdt = doc.first_section.body.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual(aw.markup.SdtType.BUILDING_BLOCK_GALLERY, building_block_sdt.sdt_type)
        self.assertEqual("Table of Contents", building_block_sdt.building_block_gallery)
        self.assertEqual("Built-in", building_block_sdt.building_block_category)

    def test_update_sdt_content(self):
        doc = aw.Document()
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.DROP_DOWN_LIST, aw.markup.MarkupLevel.BLOCK)
        tag.list_items.add(aw.markup.SdtListItem(value="Value 1"))
        tag.list_items.add(aw.markup.SdtListItem(value="Value 2"))
        tag.list_items.add(aw.markup.SdtListItem(value="Value 3"))
        tag.list_items.selected_value = tag.list_items[1]
        doc.first_section.body.append_child(tag)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.UpdateSdtContent.pdf")

    def test_use_pdf_document_for_update_sdt_content(self):
        raise NotImplementedError("Unsupported call of method named UpdateSdtContent")

    def test_fill_table_using_repeating_section_item(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_custom_xml_part(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_multi_section_tags(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_sdt_child_nodes(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_sdt_range_extended_methods(self):
        raise NotImplementedError("Unsupported call of method named InsertStructuredDocumentTagRanges")

    def test_get_sdt(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_range_sdt(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_sdt_at_row_level(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        group_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.GROUP, aw.markup.MarkupLevel.ROW)
        table.append_child(group_sdt)
        group_sdt.is_showing_placeholder_text = False
        group_sdt.remove_all_children()
        row = aw.tables.Row(doc)
        group_sdt.append_child(row)
        cell = aw.tables.Cell(doc)
        row.append_child(cell)
        builder.end_table()
        cell.ensure_minimum()
        builder.move_to(cell.last_paragraph)
        builder.write("Lorem ipsum dolor.")
        builder.move_to(table.next_sibling)
        builder.write("Nulla blandit nisi.")
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.SdtAtRowLevel.docx")

    def test_ignore_structured_document_tags(self):
        doc = aw.Document(file_name=MY_DIR + "Structured document tags.docx")
        p = doc.first_section.body.get_child(aw.NodeType.PARAGRAPH, 2, True).as_paragraph()
        text_to_search = p.to_string(save_format=aw.SaveFormat.TEXT).strip()
        options = aw.replacing.FindReplaceOptions()
        options.ignore_structured_document_tags = True
        doc.range.replace(pattern=text_to_search, replacement="replacement", options=options)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.IgnoreStructuredDocumentTags.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.IgnoreStructuredDocumentTags.docx")
        self.assertEqual("This document contains Structured Document Tags with text inside them\r\rRepeatingSection\rRichText\rreplacement", doc.get_text().strip())

    def test_citation(self):
        doc = aw.Document()
        sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.CITATION, aw.markup.MarkupLevel.INLINE)
        paragraph = doc.first_section.body.first_paragraph
        paragraph.append_child(sdt)
        builder = aw.DocumentBuilder(doc)
        builder.move_to_paragraph(0, -1)
        builder.insert_field(field_code="""CITATION Ath22 \\l 1033 """, field_value="(John Lennon, 2022)")
        while sdt.next_sibling != None:
            sdt.append_child(sdt.next_sibling)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.Citation.docx")

    def test_range_start_word_open_xml_minimal(self):
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()
        self.assertTrue(("<pkg:part pkg:name=\"/docProps/app.xml\" pkg:contentType=\"application/vnd.openxmlformats-officedocument.extended-properties+xml\">" in tag.word_open_xml_minimal))
        self.assertFalse(("xmlns:w16cid=\"http://schemas.microsoft.com/office/word/2016/wordml/cid\"" in tag.word_open_xml_minimal))

    def test_remove_self_only(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_appearance(self):
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()
        if tag.appearance == aw.markup.SdtAppearance.HIDDEN:
            tag.appearance = aw.markup.SdtAppearance.TAGS
