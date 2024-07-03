# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

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
        #ExStart
        #ExFor:StructuredDocumentTag.color
        #ExFor:StructuredDocumentTag.contents_font
        #ExFor:StructuredDocumentTag.end_character_font
        #ExFor:StructuredDocumentTag.id
        #ExFor:StructuredDocumentTag.level
        #ExFor:StructuredDocumentTag.multiline
        #ExFor:StructuredDocumentTag.tag
        #ExFor:StructuredDocumentTag.title
        #ExFor:StructuredDocumentTag.remove_self_only
        #ExFor:StructuredDocumentTag.appearance
        #ExSummary:Shows how to create a structured document tag in a plain text box and modify its appearance.
        doc = aw.Document()
        # Create a structured document tag that will contain plain text.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        # Set the title and color of the frame that appears when you mouse over the structured document tag in Microsoft Word.
        tag.title = "My plain text"
        tag.color = aspose.pydrawing.Color.magenta
        # Set a tag for this structured document tag, which is obtainable
        # as an XML element named "tag", with the string below in its "@val" attribute.
        tag.tag = "MyPlainTextSDT"
        # Every structured document tag has a random unique ID.
        self.assertTrue(tag.id > 0)
        # Set the font for the text inside the structured document tag.
        tag.contents_font.name = "Arial"
        # Set the font for the text at the end of the structured document tag.
        # Any text that we type in the document body after moving out of the tag with arrow keys will use this font.
        tag.end_character_font.name = "Arial Black"
        # By default, this is false and pressing enter while inside a structured document tag does nothing.
        # When set to true, our structured document tag can have multiple lines.
        # Set the "Multiline" property to "false" to only allow the contents
        # of this structured document tag to span a single line.
        # Set the "Multiline" property to "true" to allow the tag to contain multiple lines of content.
        tag.multiline = True
        # Set the "Appearance" property to "SdtAppearance.Tags" to show tags around content.
        # By default structured document tag shows as BoundingBox.
        tag.appearance = aw.markup.SdtAppearance.TAGS
        builder = aw.DocumentBuilder(doc)
        builder.insert_node(tag)
        # Insert a clone of our structured document tag in a new paragraph.
        tag_clone = tag.clone(True).as_structured_document_tag()
        builder.insert_paragraph()
        builder.insert_node(tag_clone)
        # Use the "RemoveSelfOnly" method to remove a structured document tag, while keeping its contents in the document.
        tag_clone.remove_self_only()
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.PlainText.docx")
        #ExEnd
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
        #ExStart
        #ExFor:StructuredDocumentTag.lock_content_control
        #ExFor:StructuredDocumentTag.lock_contents
        #ExSummary:Shows how to apply editing restrictions to structured document tags.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert a plain text structured document tag, which acts as a text box that prompts the user to fill it in.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        # Set the "LockContents" property to "true" to prohibit the user from editing this text box's contents.
        tag.lock_contents = True
        builder.write("The contents of this structured document tag cannot be edited: ")
        builder.insert_node(tag)
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        # Set the "LockContentControl" property to "true" to prohibit the user from
        # deleting this structured document tag manually in Microsoft Word.
        tag.lock_content_control = True
        builder.insert_paragraph()
        builder.write("This structured document tag cannot be deleted but its contents can be edited: ")
        builder.insert_node(tag)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.Lock.docx")
        #ExEnd
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
        #ExStart
        #ExFor:XmlMapping.store_item_id
        #ExSummary:Shows how to get the custom XML data identifier of an XML part.
        doc = aw.Document(file_name=MY_DIR + "Custom XML part in structured document tag.docx")
        # Structured document tags have IDs in the form of GUIDs.
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual("{F3029283-4FF8-4DD2-9F31-395F19ACEE85}", tag.xml_mapping.store_item_id)
        #ExEnd

    def test_custom_xml_part_store_item_id_read_only_null(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_clear_text_from_structured_document_tags(self):
        #ExStart
        #ExFor:StructuredDocumentTag.clear
        #ExSummary:Shows how to delete contents of structured document tag elements.
        doc = aw.Document()
        # Create a plain text structured document tag, and then append it to the document.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)
        doc.first_section.body.append_child(tag)
        # This structured document tag, which is in the form of a text box, already displays placeholder text.
        self.assertEqual("Click here to enter text.", tag.get_text().strip())
        self.assertTrue(tag.is_showing_placeholder_text)
        # Create a building block with text contents.
        glossary_doc = doc.glossary_document
        substitute_block = aw.buildingblocks.BuildingBlock(glossary_doc)
        substitute_block.name = "My placeholder"
        substitute_block.append_child(aw.Section(glossary_doc))
        substitute_block.first_section.ensure_minimum()
        substitute_block.first_section.body.first_paragraph.append_child(aw.Run(doc=glossary_doc, text="Custom placeholder text."))
        glossary_doc.append_child(substitute_block)
        # Set the structured document tag's "PlaceholderName" property to our building block's name to get
        # the structured document tag to display the contents of the building block in place of the original default text.
        tag.placeholder_name = "My placeholder"
        self.assertEqual("Custom placeholder text.", tag.get_text().strip())
        self.assertTrue(tag.is_showing_placeholder_text)
        # Edit the text of the structured document tag and hide the placeholder text.
        run = tag.get_child(aw.NodeType.RUN, 0, True).as_run()
        run.text = "New text."
        tag.is_showing_placeholder_text = False
        self.assertEqual("New text.", tag.get_text().strip())
        # Use the "Clear" method to clear this structured document tag's contents and display the placeholder again.
        tag.clear()
        self.assertTrue(tag.is_showing_placeholder_text)
        self.assertEqual("Custom placeholder text.", tag.get_text().strip())
        #ExEnd

    def test_access_to_building_block_properties_from_doc_part_obj_sdt(self):
        doc = aw.Document(file_name=MY_DIR + "Structured document tags with building blocks.docx")
        doc_part_obj_sdt = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual(aw.markup.SdtType.DOC_PART_OBJ, doc_part_obj_sdt.sdt_type)
        self.assertEqual("Table of Contents", doc_part_obj_sdt.building_block_gallery)

    def test_access_to_building_block_properties_from_plain_text_sdt(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_building_block_categories(self):
        #ExStart
        #ExFor:StructuredDocumentTag.building_block_category
        #ExFor:StructuredDocumentTag.building_block_gallery
        #ExSummary:Shows how to insert a structured document tag as a building block, and set its category and gallery.
        doc = aw.Document()
        building_block_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.BUILDING_BLOCK_GALLERY, aw.markup.MarkupLevel.BLOCK)
        building_block_sdt.building_block_category = "Built-in"
        building_block_sdt.building_block_gallery = "Table of Contents"
        doc.first_section.body.append_child(building_block_sdt)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.BuildingBlockCategories.docx")
        #ExEnd
        building_block_sdt = doc.first_section.body.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual(aw.markup.SdtType.BUILDING_BLOCK_GALLERY, building_block_sdt.sdt_type)
        self.assertEqual("Table of Contents", building_block_sdt.building_block_gallery)
        self.assertEqual("Built-in", building_block_sdt.building_block_category)

    def test_update_sdt_content(self):
        doc = aw.Document()
        # Insert a drop-down list structured document tag.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.DROP_DOWN_LIST, aw.markup.MarkupLevel.BLOCK)
        tag.list_items.add(aw.markup.SdtListItem(value="Value 1"))
        tag.list_items.add(aw.markup.SdtListItem(value="Value 2"))
        tag.list_items.add(aw.markup.SdtListItem(value="Value 3"))
        # The drop-down list currently displays "Choose an item" as the default text.
        # Set the "SelectedValue" property to one of the list items to get the tag to
        # display that list item's value instead of the default text.
        tag.list_items.selected_value = tag.list_items[1]
        doc.first_section.body.append_child(tag)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.UpdateSdtContent.pdf")

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
        #ExStart
        #ExFor:SdtType
        #ExSummary:Shows how to create group structured document tag at the Row level.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        table = builder.start_table()
        # Create a Group structured document tag at the Row level.
        group_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.GROUP, aw.markup.MarkupLevel.ROW)
        table.append_child(group_sdt)
        group_sdt.is_showing_placeholder_text = False
        group_sdt.remove_all_children()
        # Create a child row of the structured document tag.
        row = aw.tables.Row(doc)
        group_sdt.append_child(row)
        cell = aw.tables.Cell(doc)
        row.append_child(cell)
        builder.end_table()
        # Insert cell contents.
        cell.ensure_minimum()
        builder.move_to(cell.last_paragraph)
        builder.write("Lorem ipsum dolor.")
        # Insert text after the table.
        builder.move_to(table.next_sibling)
        builder.write("Nulla blandit nisi.")
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.SdtAtRowLevel.docx")
        #ExEnd

    def test_ignore_structured_document_tags(self):
        #ExStart
        #ExFor:FindReplaceOptions.ignore_structured_document_tags
        #ExSummary:Shows how to ignore content of tags from replacement.
        doc = aw.Document(file_name=MY_DIR + "Structured document tags.docx")
        # This paragraph contains SDT.
        p = doc.first_section.body.get_child(aw.NodeType.PARAGRAPH, 2, True).as_paragraph()
        text_to_search = p.to_string(save_format=aw.SaveFormat.TEXT).strip()
        options = aw.replacing.FindReplaceOptions()
        options.ignore_structured_document_tags = True
        doc.range.replace(pattern=text_to_search, replacement="replacement", options=options)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.IgnoreStructuredDocumentTags.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.IgnoreStructuredDocumentTags.docx")
        self.assertEqual("This document contains Structured Document Tags with text inside them\r\rRepeatingSection\rRichText\rreplacement", doc.get_text().strip())

    def test_citation(self):
        #ExStart
        #ExFor:SdtType
        #ExSummary:Shows how to create a structured document tag of the Citation type.
        doc = aw.Document()
        sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.CITATION, aw.markup.MarkupLevel.INLINE)
        paragraph = doc.first_section.body.first_paragraph
        paragraph.append_child(sdt)
        # Create a Citation field.
        builder = aw.DocumentBuilder(doc)
        builder.move_to_paragraph(0, -1)
        builder.insert_field(field_code="""CITATION Ath22 \\l 1033 """, field_value="(John Lennon, 2022)")
        # Move the field to the structured document tag.
        while sdt.next_sibling != None:
            sdt.append_child(sdt.next_sibling)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.Citation.docx")
        #ExEnd

    def test_range_start_word_open_xml_minimal(self):
        #ExStart:RangeStartWordOpenXmlMinimal
        #ExFor:StructuredDocumentTagRangeStart.word_open_xml_minimal
        #ExSummary:Shows how to get minimal XML contained within the node in the FlatOpc format.
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()
        self.assertTrue(("<pkg:part pkg:name=\"/docProps/app.xml\" pkg:contentType=\"application/vnd.openxmlformats-officedocument.extended-properties+xml\">" in tag.word_open_xml_minimal))
        self.assertFalse(("xmlns:w16cid=\"http://schemas.microsoft.com/office/word/2016/wordml/cid\"" in tag.word_open_xml_minimal))
        #ExEnd:RangeStartWordOpenXmlMinimal

    def test_remove_self_only(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_appearance(self):
        #ExStart:Appearance
        #ExFor:SdtAppearance
        #ExFor:StructuredDocumentTagRangeStart.appearance
        #ExSummary:Shows how to show tag around content.
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()
        if tag.appearance == aw.markup.SdtAppearance.HIDDEN:
            tag.appearance = aw.markup.SdtAppearance.TAGS
        #ExEnd:Appearance
        #ExEnd:Appearance
