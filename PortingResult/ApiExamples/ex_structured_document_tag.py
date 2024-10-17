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
import uuid
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExStructuredDocumentTag(ApiExampleBase):
    def test_repeating_section(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_flat_opc_content(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_apply_style(self):
        #ExStart
        #ExFor:StructuredDocumentTag
        #ExFor:StructuredDocumentTag.node_type
        #ExFor:StructuredDocumentTag.style
        #ExFor:StructuredDocumentTag.style_name
        #ExFor:StructuredDocumentTag.word_open_xml_minimal
        #ExFor:MarkupLevel
        #ExFor:SdtType
        #ExSummary:Shows how to work with styles for content control elements.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
        # Below are two ways to apply a style from the document to a structured document tag.
        # 1 -  Apply a style object from the document's style collection:
        quote_style = doc.styles.get_by_style_identifier(aw.StyleIdentifier.QUOTE)
        sdt_plain_text = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        sdt_plain_text.style = quote_style
        # 2 -  Reference a style in the document by name:
        sdt_rich_text = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.RICH_TEXT, aw.markup.MarkupLevel.INLINE)
        sdt_rich_text.style_name = "Quote"
        builder.insert_node(sdt_plain_text)
        builder.insert_node(sdt_rich_text)
        self.assertEqual(aw.NodeType.STRUCTURED_DOCUMENT_TAG, sdt_plain_text.node_type)
        tags = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG, True)
        for node in tags:
            sdt = node.as_structured_document_tag()
            print(sdt.word_open_xml_minimal)
            self.assertEqual(aw.StyleIdentifier.QUOTE, sdt.style.style_identifier)
            self.assertEqual("Quote", sdt.style_name)
        #ExEnd

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
        #ExFor:IStructuredDocumentTag.tag
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
        builder = aw.DocumentBuilder(doc=doc)
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
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_placeholder_building_block(self):
        for is_showing_placeholder_text in [False, True]:
            #ExStart
            #ExFor:StructuredDocumentTag.is_showing_placeholder_text
            #ExFor:IStructuredDocumentTag.is_showing_placeholder_text
            #ExFor:StructuredDocumentTag.placeholder
            #ExFor:StructuredDocumentTag.placeholder_name
            #ExFor:IStructuredDocumentTag.placeholder
            #ExFor:IStructuredDocumentTag.placeholder_name
            #ExSummary:Shows how to use a building block's contents as a custom placeholder text for a structured document tag.
            doc = aw.Document()
            # Insert a plain text structured document tag of the "PlainText" type, which will function as a text box.
            # The contents that it will display by default are a "Click here to enter text." prompt.
            tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
            # We can get the tag to display the contents of a building block instead of the default text.
            # First, add a building block with contents to the glossary document.
            glossary_doc = doc.glossary_document
            substitute_block = aw.buildingblocks.BuildingBlock(glossary_doc)
            substitute_block.name = "Custom Placeholder"
            substitute_block.append_child(aw.Section(glossary_doc))
            substitute_block.first_section.append_child(aw.Body(glossary_doc))
            substitute_block.first_section.body.append_paragraph("Custom placeholder text.")
            glossary_doc.append_child(substitute_block)
            # Then, use the structured document tag's "PlaceholderName" property to reference that building block by name.
            tag.placeholder_name = "Custom Placeholder"
            # If "PlaceholderName" refers to an existing block in the parent document's glossary document,
            # we will be able to verify the building block via the "Placeholder" property.
            self.assertEqual(substitute_block, tag.placeholder)
            # Set the "IsShowingPlaceholderText" property to "true" to treat the
            # structured document tag's current contents as placeholder text.
            # This means that clicking on the text box in Microsoft Word will immediately highlight all the tag's contents.
            # Set the "IsShowingPlaceholderText" property to "false" to get the
            # structured document tag to treat its contents as text that a user has already entered.
            # Clicking on this text in Microsoft Word will place the blinking cursor at the clicked location.
            tag.is_showing_placeholder_text = is_showing_placeholder_text
            builder = aw.DocumentBuilder(doc=doc)
            builder.insert_node(tag)
            doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.PlaceholderBuildingBlock.docx")
            #ExEnd
            doc = aw.Document(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.PlaceholderBuildingBlock.docx")
            tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
            substitute_block = doc.glossary_document.get_child(aw.NodeType.BUILDING_BLOCK, 0, True).as_building_block()
            self.assertEqual("Custom Placeholder", substitute_block.name)
            self.assertEqual(is_showing_placeholder_text, tag.is_showing_placeholder_text)
            self.assertEqual(substitute_block, tag.placeholder)
            self.assertEqual(substitute_block.name, tag.placeholder_name)

    def test_lock(self):
        #ExStart
        #ExFor:StructuredDocumentTag.lock_content_control
        #ExFor:StructuredDocumentTag.lock_contents
        #ExFor:IStructuredDocumentTag.lock_content_control
        #ExFor:IStructuredDocumentTag.lock_contents
        #ExSummary:Shows how to apply editing restrictions to structured document tags.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
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
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_data_checksum(self):
        #ExStart
        #ExFor:CustomXmlPart.data_checksum
        #ExSummary:Shows how the checksum is calculated in a runtime.
        doc = aw.Document()
        rich_text = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.RICH_TEXT, aw.markup.MarkupLevel.BLOCK)
        doc.first_section.body.append_child(rich_text)
        # The checksum is read-only and computed using the data of the corresponding custom XML data part.
        rich_text.xml_mapping.set_mapping(doc.custom_xml_parts.add(id=str(uuid.uuid4()), xml="<root><text>ContentControl</text></root>"), "/root/text", "")
        checksum = rich_text.xml_mapping.custom_xml_part.data_checksum
        print(checksum)
        rich_text.xml_mapping.set_mapping(doc.custom_xml_parts.add(id=str(uuid.uuid4()), xml="<root><text>Updated ContentControl</text></root>"), "/root/text", "")
        updated_checksum = rich_text.xml_mapping.custom_xml_part.data_checksum
        print(updated_checksum)
        # We changed the XmlPart of the tag, and the checksum was updated at runtime.
        self.assertNotEqual(checksum, updated_checksum)
        #ExEnd

    def test_xml_mapping(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_structured_document_tag_range_start_xml_mapping(self):
        raise NotImplementedError("Unsupported target type System.Text.Encoding")

    def test_custom_xml_schema_collection(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

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
        xml_string = "<?xml version=\"1.0\"?>" + "<Company>" + "<Employee id=\"1\">" + "<FirstName>John</FirstName>" + "<LastName>Doe</LastName>" + "</Employee>" + "<Employee id=\"2\">" + "<FirstName>Jane</FirstName>" + "<LastName>Doe</LastName>" + "</Employee>" + "</Company>"
        doc = aw.Document()
        # Insert the full XML document as a custom document part.
        # We can find the mapping for this part in Microsoft Word via "Developer" -> "XML Mapping Pane", if it is enabled.
        xml_part = doc.custom_xml_parts.add(id='{' + str(uuid.uuid4()) + '}', xml=xml_string)
        # Create a structured document tag, which will use an XPath to refer to a single element from the XML.
        sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)
        sdt.xml_mapping.set_mapping(xml_part, "Company//Employee[@id='2']/FirstName", "")
        # Add the StructuredDocumentTag to the document to display the element in the text.
        doc.first_section.body.append_child(sdt)

    def test_multi_section_tags(self):
        #ExStart
        #ExFor:StructuredDocumentTagRangeStart
        #ExFor:IStructuredDocumentTag.id
        #ExFor:StructuredDocumentTagRangeStart.id
        #ExFor:StructuredDocumentTagRangeStart.title
        #ExFor:StructuredDocumentTagRangeStart.placeholder_name
        #ExFor:StructuredDocumentTagRangeStart.is_showing_placeholder_text
        #ExFor:StructuredDocumentTagRangeStart.lock_content_control
        #ExFor:StructuredDocumentTagRangeStart.lock_contents
        #ExFor:IStructuredDocumentTag.level
        #ExFor:StructuredDocumentTagRangeStart.level
        #ExFor:StructuredDocumentTagRangeStart.range_end
        #ExFor:IStructuredDocumentTag.color
        #ExFor:StructuredDocumentTagRangeStart.color
        #ExFor:StructuredDocumentTagRangeStart.sdt_type
        #ExFor:StructuredDocumentTagRangeStart.word_open_xml
        #ExFor:StructuredDocumentTagRangeStart.tag
        #ExFor:StructuredDocumentTagRangeEnd
        #ExFor:StructuredDocumentTagRangeEnd.id
        #ExSummary:Shows how to get the properties of multi-section structured document tags.
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        range_start_tag = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, True)[0].as_structured_document_tag_range_start()
        range_end_tag = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_END, True)[0].as_structured_document_tag_range_end()
        self.assertEqual(range_start_tag.id, range_end_tag.id) #ExSkip
        self.assertEqual(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, range_start_tag.node_type) #ExSkip
        self.assertEqual(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_END, range_end_tag.node_type) #ExSkip
        print("StructuredDocumentTagRangeStart values:")
        print(f"\t|Id: {range_start_tag.id}")
        print(f"\t|Title: {range_start_tag.title}")
        print(f"\t|PlaceholderName: {range_start_tag.placeholder_name}")
        print(f"\t|IsShowingPlaceholderText: {range_start_tag.is_showing_placeholder_text}")
        print(f"\t|LockContentControl: {range_start_tag.lock_content_control}")
        print(f"\t|LockContents: {range_start_tag.lock_contents}")
        print(f"\t|Level: {range_start_tag.level}")
        print(f"\t|NodeType: {range_start_tag.node_type}")
        print(f"\t|RangeEnd: {range_start_tag.range_end}")
        print(f"\t|Color: {range_start_tag.color.to_argb()}")
        print(f"\t|SdtType: {range_start_tag.sdt_type}")
        print(f"\t|FlatOpcContent: {range_start_tag.word_open_xml}")
        print(f"\t|Tag: {range_start_tag.tag}\n")
        print("StructuredDocumentTagRangeEnd values:")
        print(f"\t|Id: {range_end_tag.id}")
        print(f"\t|NodeType: {range_end_tag.node_type}")
        #ExEnd

    def test_sdt_child_nodes(self):
        #ExStart
        #ExFor:StructuredDocumentTagRangeStart.get_child_nodes(NodeType,bool)
        #ExSummary:Shows how to get child nodes of StructuredDocumentTagRangeStart.
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, True)[0].as_structured_document_tag_range_start()
        print("StructuredDocumentTagRangeStart values:")
        print(f"\t|Child nodes count: {tag.get_child_nodes(aw.NodeType.ANY, False).count}\n")
        for node in tag.get_child_nodes(aw.NodeType.ANY, False):
            print(f"\t|Child node type: {node.node_type}")
        for node in tag.get_child_nodes(aw.NodeType.RUN, True):
            print(f"\t|Child node text: {node.get_text()}")
        #ExEnd

    def test_sdt_range_extended_methods(self):
        raise NotImplementedError("Unsupported call of method named InsertStructuredDocumentTagRanges")

    def test_get_sdt(self):
        #ExStart
        #ExFor:Range.structured_document_tags
        #ExFor:StructuredDocumentTagCollection.remove(int)
        #ExFor:StructuredDocumentTagCollection.remove_at(int)
        #ExSummary:Shows how to remove structured document tag.
        doc = aw.Document(file_name=MY_DIR + "Structured document tags.docx")
        structured_document_tags = doc.range.structured_document_tags
        sdt = None
        i = 0
        while i < structured_document_tags.count:
            sdt = structured_document_tags[i]
            print(sdt.title)
            i += 1
        sdt = structured_document_tags.get_by_id(1691867797)
        self.assertEqual(1691867797, sdt.id)
        self.assertEqual(5, structured_document_tags.count)
        # Remove the structured document tag by Id.
        structured_document_tags.remove(1691867797)
        # Remove the structured document tag at position 0.
        structured_document_tags.remove_at(0)
        self.assertEqual(3, structured_document_tags.count)
        #ExEnd

    def test_range_sdt(self):
        #ExStart
        #ExFor:StructuredDocumentTagCollection
        #ExFor:StructuredDocumentTagCollection.get_by_id(int)
        #ExFor:StructuredDocumentTagCollection.get_by_title(str)
        #ExFor:IStructuredDocumentTag.is_multi_section
        #ExFor:IStructuredDocumentTag.title
        #ExSummary:Shows how to get structured document tag.
        doc = aw.Document(file_name=MY_DIR + "Structured document tags by id.docx")
        # Get the structured document tag by Id.
        sdt = doc.range.structured_document_tags.get_by_id(1160505028)
        print(sdt.is_multi_section)
        print(sdt.title)
        # Get the structured document tag or ranged tag by Title.
        sdt = doc.range.structured_document_tags.get_by_title("Alias4")
        print(sdt.id)
        #ExEnd

    def test_sdt_at_row_level(self):
        #ExStart
        #ExFor:SdtType
        #ExSummary:Shows how to create group structured document tag at the Row level.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc=doc)
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
        builder = aw.DocumentBuilder(doc=doc)
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
        #ExFor:IStructuredDocumentTag.appearance
        #ExSummary:Shows how to show tag around content.
        doc = aw.Document(file_name=MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()
        if tag.appearance == aw.markup.SdtAppearance.HIDDEN:
            tag.appearance = aw.markup.SdtAppearance.TAGS
        #ExEnd:Appearance

    def test_insert_structured_document_tag(self):
        #ExStart:InsertStructuredDocumentTag
        #ExFor:DocumentBuilder.insert_structured_document_tag(SdtType)
        #ExSummary:Shows how to simply insert structured document tag.
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        builder = aw.DocumentBuilder(doc=doc)
        builder.move_to(doc.first_section.body.paragraphs[3])
        # Note, that only following StructuredDocumentTag types are allowed for insertion:
        # SdtType.PlainText, SdtType.RichText, SdtType.Checkbox, SdtType.DropDownList,
        # SdtType.ComboBox, SdtType.Picture, SdtType.Date.
        # Markup level of inserted StructuredDocumentTag will be detected automatically and depends on position being inserted at.
        # Added StructuredDocumentTag will inherit paragraph and font formatting from cursor position.
        sdt_plain = builder.insert_structured_document_tag(aw.markup.SdtType.PLAIN_TEXT)
        doc.save(file_name=ARTIFACTS_DIR + "StructuredDocumentTag.InsertStructuredDocumentTag.docx")
        #ExEnd:InsertStructuredDocumentTag
