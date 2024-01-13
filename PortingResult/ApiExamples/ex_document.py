# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.fields
import aspose.words.loading
import aspose.words.notes
import aspose.words.rendering
import aspose.words.saving
import aspose.words.settings
import aspose.words.webextensions
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExDocument(ApiExampleBase):
    def test_constructor(self):
        doc = aspose.words.Document()
        doc.first_section.body.first_paragraph.append_child(aspose.words.Run(doc = doc, text = "Hello world!"))
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        self.assertEqual("Hello World!", doc.first_section.body.first_paragraph.get_text().strip())
        doc = aspose.words.Document(file_name = MY_DIR + "Encrypted.docx", load_options = aspose.words.loading.LoadOptions(password = "docPassword"))
        self.assertEqual("Test encrypted document.", doc.first_section.body.first_paragraph.get_text().strip())

    def test_load_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_convert_to_pdf(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Document.ConvertToPdf.pdf")

    def test_save_to_image_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_detect_mobi_document_format(self):
        info = aspose.words.FileFormatUtil.detect_file_format(file_name = MY_DIR + "Document.mobi")
        self.assertEqual(info.load_format, aspose.words.LoadFormat.MOBI)

    def test_detect_pdf_document_format(self):
        info = aspose.words.FileFormatUtil.detect_file_format(file_name = MY_DIR + "Pdf Document.pdf")
        self.assertEqual(info.load_format, aspose.words.LoadFormat.PDF)

    def test_open_pdf_document(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Pdf Document.pdf")
        self.assertEqual("Heading 1\rHeading 1.1.1.1 Heading 1.1.1.2\rHeading 1.1.1.1.1.1.1.1.1 Heading 1.1.1.1.1.1.1.1.2\u000c", doc.range.text)

    def test_open_protected_pdf_document(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Pdf Document.pdf")
        save_options = aspose.words.saving.PdfSaveOptions()
        save_options.encryption_details = aspose.words.saving.PdfEncryptionDetails(user_password = "Aspose", owner_password = None)
        doc.save(file_name = ARTIFACTS_DIR + "Document.PdfDocumentEncrypted.pdf", save_options = save_options)
        load_options = aspose.words.loading.PdfLoadOptions()
        load_options.password = "Aspose"
        load_options.load_format = aspose.words.LoadFormat.PDF
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Document.PdfDocumentEncrypted.pdf", load_options = load_options)

    def test_open_from_stream_with_base_uri(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_html_from_web_page(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_load_encrypted(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_temp_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_convert_to_html(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Document.ConvertToHtml.html", save_format = aspose.words.SaveFormat.HTML)

    def test_convert_to_mhtml(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Document.ConvertToMhtml.mht")

    def test_convert_to_txt(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Document.ConvertToTxt.txt")

    def test_convert_to_epub(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Document.ConvertToEpub.epub")

    def test_save_to_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_append_document(self):
        raise NotImplementedError("Unsupported target type System.StringComparison")

    def test_append_document_from_automation(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_keep_source_numbering_same_list_ids(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_merge_pasted_lists(self):
        src_doc = aspose.words.Document(file_name = MY_DIR + "List item.docx")
        dst_doc = aspose.words.Document(file_name = MY_DIR + "List destination.docx")
        options = aspose.words.ImportFormatOptions()
        options.merge_pasted_lists = True
        dst_doc.append_document(src_doc = src_doc, import_format_mode = aspose.words.ImportFormatMode.USE_DESTINATION_STYLES, import_format_options = options)
        dst_doc.save(file_name = ARTIFACTS_DIR + "Document.MergePastedLists.docx")

    def test_force_copy_styles(self):
        src_doc = aspose.words.Document(file_name = MY_DIR + "Styles source.docx")
        dst_doc = aspose.words.Document(file_name = MY_DIR + "Styles destination.docx")
        options = aspose.words.ImportFormatOptions()
        options.force_copy_styles = True
        dst_doc.append_document(src_doc = src_doc, import_format_mode = aspose.words.ImportFormatMode.KEEP_SOURCE_FORMATTING, import_format_options = options)
        paras = dst_doc.sections[1].body.paragraphs
        self.assertEqual(paras[0].paragraph_format.style.name, "MyStyle1_0")
        self.assertEqual(paras[1].paragraph_format.style.name, "MyStyle2_0")
        self.assertEqual(paras[2].paragraph_format.style.name, "MyStyle3")

    def test_adjust_sentence_and_word_spacing(self):
        src_doc = aspose.words.Document()
        dst_doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(src_doc)
        builder.write("Dolor sit amet.")
        builder = aspose.words.DocumentBuilder(dst_doc)
        builder.write("Lorem ipsum.")
        options = aspose.words.ImportFormatOptions()
        options.adjust_sentence_and_word_spacing = True
        builder.insert_document(src_doc = src_doc, import_format_mode = aspose.words.ImportFormatMode.USE_DESTINATION_STYLES, import_format_options = options)
        self.assertEqual("Lorem ipsum. Dolor sit amet.", dst_doc.first_section.body.first_paragraph.get_text().strip())

    def test_validate_individual_document_signatures(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_signature_value(self):
        raise NotImplementedError("Unsupported target type System.Convert")

    def test_append_all_documents_in_folder(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_join_runs_with_same_formatting(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        self.assertEqual(317, doc.get_child_nodes(aspose.words.NodeType.RUN, True).count)
        self.assertEqual(121, doc.join_runs_with_same_formatting())
        self.assertEqual(196, doc.get_child_nodes(aspose.words.NodeType.RUN, True).count)

    def test_default_tab_stop(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_clone_document(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_document_get_text_to_string(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_field(field_code = "MERGEFIELD Field")
        self.assertEqual("\u0013MERGEFIELD Field\u0014«Field»\u0015\u000c", doc.get_text())
        self.assertEqual("«Field»\r\n", doc.to_string(save_format = aspose.words.SaveFormat.TEXT))

    def test_document_byte_array(self):
        raise NotImplementedError("Unsupported type: MemoryStream")

    def test_protect_unprotect(self):
        doc = aspose.words.Document()
        doc.protect(type = aspose.words.ProtectionType.READ_ONLY, password = "password")
        self.assertEqual(aspose.words.ProtectionType.READ_ONLY, doc.protection_type)
        doc.save(file_name = ARTIFACTS_DIR + "Document.Protect.docx")
        protected_doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Document.Protect.docx")
        self.assertEqual(aspose.words.ProtectionType.READ_ONLY, protected_doc.protection_type)
        builder = aspose.words.DocumentBuilder(protected_doc)
        builder.writeln("Text added to a protected document.")
        self.assertEqual("Text added to a protected document.", protected_doc.range.text.strip())
        doc.unprotect()
        self.assertEqual(aspose.words.ProtectionType.NO_PROTECTION, doc.protection_type)
        doc.protect(type = aspose.words.ProtectionType.READ_ONLY, password = "NewPassword")
        self.assertEqual(aspose.words.ProtectionType.READ_ONLY, doc.protection_type)
        doc.unprotect("WrongPassword")
        self.assertEqual(aspose.words.ProtectionType.READ_ONLY, doc.protection_type)
        doc.unprotect("NewPassword")
        self.assertEqual(aspose.words.ProtectionType.NO_PROTECTION, doc.protection_type)

    def test_document_ensure_minimum(self):
        doc = aspose.words.Document()
        nodes = doc.get_child_nodes(aspose.words.NodeType.ANY, True)
        self.assertEqual(aspose.words.NodeType.SECTION, nodes[0].node_type)
        self.assertEqual(doc, nodes[0].parent_node)
        self.assertEqual(aspose.words.NodeType.BODY, nodes[1].node_type)
        self.assertEqual(nodes[0], nodes[1].parent_node)
        self.assertEqual(aspose.words.NodeType.PARAGRAPH, nodes[2].node_type)
        self.assertEqual(nodes[1], nodes[2].parent_node)
        doc.remove_all_children()
        self.assertEqual(0, doc.get_child_nodes(aspose.words.NodeType.ANY, True).count)
        doc.ensure_minimum()
        self.assertEqual(aspose.words.NodeType.SECTION, nodes[0].node_type)
        self.assertEqual(aspose.words.NodeType.BODY, nodes[1].node_type)
        self.assertEqual(aspose.words.NodeType.PARAGRAPH, nodes[2].node_type)
        (nodes[2].as_paragraph()).runs.add(aspose.words.Run(doc = doc, text = "Hello world!"))
        self.assertEqual("Hello world!", doc.get_text().strip())

    def test_remove_macros_from_document(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_get_page_count(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.write("Page 1")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.write("Page 2")
        builder.insert_break(aspose.words.BreakType.PAGE_BREAK)
        builder.write("Page 3")
        self.assertEqual(3, doc.page_count)
        doc.save(file_name = ARTIFACTS_DIR + "Document.GetPageCount.pdf")

    def test_get_updated_page_properties(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, " + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        builder.write("Ut enim ad minim veniam, " + "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        self.assertEqual(0, doc.built_in_document_properties.characters)
        self.assertEqual(0, doc.built_in_document_properties.words)
        self.assertEqual(1, doc.built_in_document_properties.paragraphs)
        self.assertEqual(1, doc.built_in_document_properties.lines)
        doc.update_word_count()
        self.assertEqual(196, doc.built_in_document_properties.characters)
        self.assertEqual(36, doc.built_in_document_properties.words)
        self.assertEqual(2, doc.built_in_document_properties.paragraphs)
        self.assertEqual(1, doc.built_in_document_properties.lines)
        doc.update_word_count(True)
        self.assertEqual(4, doc.built_in_document_properties.lines)

    def test_table_style_to_direct_formatting(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_get_original_file_info(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        self.assertEqual(MY_DIR + "Document.docx", doc.original_file_name)
        self.assertEqual(aspose.words.LoadFormat.DOCX, doc.original_load_format)

    def test_footnote_columns(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Footnotes and endnotes.docx")
        self.assertEqual(0, doc.footnote_options.columns)
        doc.footnote_options.columns = 2
        doc.save(file_name = ARTIFACTS_DIR + "Document.FootnoteColumns.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Document.FootnoteColumns.docx")
        self.assertEqual(2, doc.first_section.page_setup.footnote_options.columns)

    def test_compare(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_compare_document_with_revisions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_compare_options(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_remove_external_schema_references(self):
        doc = aspose.words.Document(file_name = MY_DIR + "External XML schema.docx")
        doc.remove_external_schema_references()

    def test_track_revisions(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_accept_all_revisions(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        doc.start_track_revisions(author = "John Doe")
        builder.write("Hello world! ")
        builder.write("Hello again! ")
        builder.write("This is another revision.")
        doc.stop_track_revisions()
        self.assertEqual(3, doc.revisions.count)
        doc.accept_all_revisions()
        self.assertEqual(0, doc.revisions.count)
        self.assertEqual("Hello world! Hello again! This is another revision.", doc.get_text().strip())

    def test_get_revised_properties_of_list(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Revisions at list levels.docx")
        doc.update_list_labels()
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual("1.", paragraphs[0].list_label.label_string)
        self.assertEqual("a.", paragraphs[1].list_label.label_string)
        self.assertEqual("", paragraphs[2].list_label.label_string)
        doc.revisions_view = aspose.words.RevisionsView.FINAL
        self.assertEqual("", paragraphs[0].list_label.label_string)
        self.assertEqual("1.", paragraphs[1].list_label.label_string)
        self.assertEqual("a.", paragraphs[2].list_label.label_string)
        doc.revisions_view = aspose.words.RevisionsView.ORIGINAL
        doc.accept_all_revisions()
        self.assertEqual("a.", paragraphs[0].list_label.label_string)
        self.assertEqual("", paragraphs[1].list_label.label_string)
        self.assertEqual("b.", paragraphs[2].list_label.label_string)

    def test_update_thumbnail(self):
        raise NotImplementedError("Unsupported type: Size")

    def test_hyphenation_options(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_hyphenation_options_default_values(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_hyphenation_options_exceptions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_ooxml_compliance_version(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.doc")
        self.assertEqual(doc.compliance, aspose.words.saving.OoxmlCompliance.ECMA376_2006)
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        self.assertEqual(doc.compliance, aspose.words.saving.OoxmlCompliance.ISO29500_2008_TRANSITIONAL)

    def test_cleanup(self):
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
        doc.cleanup()
        self.assertEqual(6, doc.styles.count)
        doc.first_section.body.remove_all_children()
        doc.cleanup()
        self.assertEqual(4, doc.styles.count)

    def test_automatically_update_styles(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_default_template(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_use_substitutions(self):
        raise NotImplementedError("Unsupported type: Regex")

    def test_set_invalidate_field_types(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        field = builder.insert_field(field_code = "DATE", field_value = None)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_DATE, field.type)
        field_text = doc.first_section.body.first_paragraph.get_child_nodes(aspose.words.NodeType.RUN, True)[0].as_run()
        self.assertEqual("DATE", field_text.text)
        field_text.text = "PAGE"
        self.assertEqual("PAGE", field.get_field_code())
        self.assertEqual(aspose.words.fields.FieldType.FIELD_DATE, field.type)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_DATE, field.start.field_type)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_DATE, field.separator.field_type)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_DATE, field.end.field_type)
        doc.normalize_field_types()
        self.assertEqual(aspose.words.fields.FieldType.FIELD_PAGE, field.type)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_PAGE, field.start.field_type)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_PAGE, field.separator.field_type)
        self.assertEqual(aspose.words.fields.FieldType.FIELD_PAGE, field.end.field_type)

    def test_layout_options_revisions(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_update_page_layout(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Document.UpdatePageLayout.1.pdf")
        doc.styles.get_by_name("Normal").font.size = 6
        doc.sections[0].page_setup.orientation = aspose.words.Orientation.LANDSCAPE
        doc.sections[0].page_setup.margins = aspose.words.Margins.MIRRORED
        doc.update_page_layout()
        doc.save(file_name = ARTIFACTS_DIR + "Document.UpdatePageLayout.2.pdf")

    def test_doc_package_custom_parts(self):
        raise NotImplementedError("Unsupported call of method named TestDocPackageCustomParts")

    def test_versions_count(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Versions.doc")
        self.assertEqual(4, doc.versions_count)
        doc.save(file_name = ARTIFACTS_DIR + "Document.VersionsCount.doc")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Document.VersionsCount.doc")
        self.assertEqual(0, doc.versions_count)

    def test_write_protection(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_show_comments(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_copy_template_styles_via_document(self):
        template = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        target = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        self.assertEqual(18, template.styles.count)
        self.assertEqual(12, target.styles.count)
        target.copy_styles_from_template(template = template)
        self.assertEqual(22, target.styles.count)

    def test_copy_template_styles_via_document_new(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_read_macros_from_existing_document(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_save_output_parameters(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        parameters = doc.save(file_name = ARTIFACTS_DIR + "Document.SaveOutputParameters.doc")
        self.assertEqual("application/msword", parameters.content_type)
        parameters = doc.save(file_name = ARTIFACTS_DIR + "Document.SaveOutputParameters.pdf")
        self.assertEqual("application/pdf", parameters.content_type)

    def test_sub_document(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_create_web_extension(self):
        raise NotImplementedError("Unsupported target type System.Globalization.CultureInfo")

    def test_get_web_extension_info(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_epub_cover(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_text_watermark(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_ignore_printer_metrics(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Rendering.docx")
        doc.layout_options.ignore_printer_metrics = False
        doc.save(file_name = ARTIFACTS_DIR + "Document.IgnorePrinterMetrics.docx")

    def test_extract_pages(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Layout entities.docx")
        doc = doc.extract_pages(0, 2)
        doc.save(file_name = ARTIFACTS_DIR + "Document.ExtractPages.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Document.ExtractPages.docx")
        self.assertEqual(doc.page_count, 2)

    def test_allow_embedding_post_script_fonts(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_frameset(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_open_azw(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_open_epub(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_open_xml(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_move_to_structured_document_tag(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_include_textboxes_footnotes_endnotes_in_stat(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln("Lorem ipsum")
        builder.insert_footnote(footnote_type = aspose.words.notes.FootnoteType.FOOTNOTE, footnote_text = "sit amet")
        doc.update_word_count()
        self.assertEqual(2, doc.built_in_document_properties.words)
        doc.include_textboxes_footnotes_endnotes_in_stat = True
        doc.update_word_count()
        self.assertEqual(4, doc.built_in_document_properties.words)

    def test_set_justification_mode(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Document.docx")
        justification_mode = doc.justification_mode
        # if begin
        if justification_mode == aspose.words.settings.JustificationMode.EXPAND:
            doc.justification_mode = aspose.words.settings.JustificationMode.COMPRESS
        # if end
        doc.save(file_name = ARTIFACTS_DIR + "Document.SetJustificationMode.docx")

    def test_page_is_in_color(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")
