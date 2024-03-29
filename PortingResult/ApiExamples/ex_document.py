# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
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
    def test_create_simple_document(self):
        doc = aw.Document()
        doc.append_child(aw.Section(doc)).append_child(aw.Body(doc)).append_child(aw.Paragraph(doc)).append_child(aw.Run(doc=doc, text="Hello world!"))

    def test_constructor(self):
        doc = aw.Document()
        doc.first_section.body.first_paragraph.append_child(aw.Run(doc=doc, text="Hello world!"))
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        self.assertEqual("Hello World!", doc.first_section.body.first_paragraph.get_text().strip())
        doc = aw.Document(file_name=MY_DIR + "Encrypted.docx", load_options=aw.loading.LoadOptions(password="docPassword"))
        self.assertEqual("Test encrypted document.", doc.first_section.body.first_paragraph.get_text().strip())

    def test_load_from_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_load_from_web_async(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_convert_to_pdf(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Document.ConvertToPdf.pdf")

    def test_save_to_image_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_detect_mobi_document_format(self):
        info = aw.FileFormatUtil.detect_file_format(file_name=MY_DIR + "Document.mobi")
        self.assertEqual(info.load_format, aw.LoadFormat.MOBI)

    def test_detect_pdf_document_format(self):
        info = aw.FileFormatUtil.detect_file_format(file_name=MY_DIR + "Pdf Document.pdf")
        self.assertEqual(info.load_format, aw.LoadFormat.PDF)

    def test_open_pdf_document(self):
        doc = aw.Document(file_name=MY_DIR + "Pdf Document.pdf")
        self.assertEqual("Heading 1\rHeading 1.1.1.1 Heading 1.1.1.2\rHeading 1.1.1.1.1.1.1.1.1 Heading 1.1.1.1.1.1.1.1.2\u000c", doc.range.text)

    def test_open_protected_pdf_document(self):
        doc = aw.Document(file_name=MY_DIR + "Pdf Document.pdf")
        save_options = aw.saving.PdfSaveOptions()
        save_options.encryption_details = aw.saving.PdfEncryptionDetails(user_password="Aspose", owner_password=None)
        doc.save(file_name=ARTIFACTS_DIR + "Document.PdfDocumentEncrypted.pdf", save_options=save_options)
        load_options = aw.loading.PdfLoadOptions()
        load_options.password = "Aspose"
        load_options.load_format = aw.LoadFormat.PDF
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.PdfDocumentEncrypted.pdf", load_options=load_options)

    def test_pdf_renderer(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_open_from_stream_with_base_uri(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_html_from_web_page_async(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_insert_html_from_web_page(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_load_encrypted(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_temp_folder(self):
        raise NotImplementedError("Unsupported target type System.IO.Directory")

    def test_convert_to_html(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Document.ConvertToHtml.html", save_format=aw.SaveFormat.HTML)

    def test_convert_to_mhtml(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Document.ConvertToMhtml.mht")

    def test_convert_to_txt(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Document.ConvertToTxt.txt")

    def test_convert_to_epub(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Document.ConvertToEpub.epub")

    def test_save_to_stream(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_append_document(self):
        raise NotImplementedError("Unsupported target type System.StringComparison")

    def test_append_document_from_automation(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_import_list(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_keep_source_numbering_same_list_ids(self):
        src_doc = aw.Document(file_name=MY_DIR + "List with the same definition identifier - source.docx")
        dst_doc = aw.Document(file_name=MY_DIR + "List with the same definition identifier - destination.docx")
        import_format_options = aw.ImportFormatOptions()
        import_format_options.keep_source_numbering = True
        dst_doc.append_document(src_doc=src_doc, import_format_mode=aw.ImportFormatMode.USE_DESTINATION_STYLES, import_format_options=import_format_options)
        dst_doc.update_list_labels()
        para_text = dst_doc.sections[1].body.last_paragraph.get_text()
        self.assertTrue(para_text.startswith("13->13"), msg=para_text)
        self.assertEqual("1.", dst_doc.sections[1].body.last_paragraph.list_label.label_string)

    def test_merge_pasted_lists(self):
        src_doc = aw.Document(file_name=MY_DIR + "List item.docx")
        dst_doc = aw.Document(file_name=MY_DIR + "List destination.docx")
        options = aw.ImportFormatOptions()
        options.merge_pasted_lists = True
        dst_doc.append_document(src_doc=src_doc, import_format_mode=aw.ImportFormatMode.USE_DESTINATION_STYLES, import_format_options=options)
        dst_doc.save(file_name=ARTIFACTS_DIR + "Document.MergePastedLists.docx")

    def test_force_copy_styles(self):
        src_doc = aw.Document(file_name=MY_DIR + "Styles source.docx")
        dst_doc = aw.Document(file_name=MY_DIR + "Styles destination.docx")
        options = aw.ImportFormatOptions()
        options.force_copy_styles = True
        dst_doc.append_document(src_doc=src_doc, import_format_mode=aw.ImportFormatMode.KEEP_SOURCE_FORMATTING, import_format_options=options)
        paras = dst_doc.sections[1].body.paragraphs
        self.assertEqual(paras[0].paragraph_format.style.name, "MyStyle1_0")
        self.assertEqual(paras[1].paragraph_format.style.name, "MyStyle2_0")
        self.assertEqual(paras[2].paragraph_format.style.name, "MyStyle3")

    def test_adjust_sentence_and_word_spacing(self):
        src_doc = aw.Document()
        dst_doc = aw.Document()
        builder = aw.DocumentBuilder(src_doc)
        builder.write("Dolor sit amet.")
        builder = aw.DocumentBuilder(dst_doc)
        builder.write("Lorem ipsum.")
        options = aw.ImportFormatOptions()
        options.adjust_sentence_and_word_spacing = True
        builder.insert_document(src_doc=src_doc, import_format_mode=aw.ImportFormatMode.USE_DESTINATION_STYLES, import_format_options=options)
        self.assertEqual("Lorem ipsum. Dolor sit amet.", dst_doc.first_section.body.first_paragraph.get_text().strip())

    def test_validate_individual_document_signatures(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_signature_value(self):
        raise NotImplementedError("Unsupported target type System.Convert")

    def test_append_all_documents_in_folder(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_join_runs_with_same_formatting(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        self.assertEqual(317, doc.get_child_nodes(aw.NodeType.RUN, True).count)
        self.assertEqual(121, doc.join_runs_with_same_formatting())
        self.assertEqual(196, doc.get_child_nodes(aw.NodeType.RUN, True).count)

    def test_default_tab_stop(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_clone_document(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Hello world!")
        clone = doc.clone()
        self.assertEqual(doc.first_section.body.first_paragraph.runs[0].get_text(), clone.first_section.body.first_paragraph.runs[0].text)
        self.assertNotEqual(doc.first_section.body.first_paragraph.runs[0].get_hash_code(), clone.first_section.body.first_paragraph.runs[0].get_hash_code())

    def test_document_get_text_to_string(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_field(field_code="MERGEFIELD Field")
        self.assertEqual("\u0013MERGEFIELD Field\u0014«Field»\u0015", doc.get_text().strip())
        self.assertEqual("«Field»", doc.to_string(save_format=aw.SaveFormat.TEXT).strip())

    def test_protect_unprotect(self):
        doc = aw.Document()
        doc.protect(type=aw.ProtectionType.READ_ONLY, password="password")
        self.assertEqual(aw.ProtectionType.READ_ONLY, doc.protection_type)
        doc.save(file_name=ARTIFACTS_DIR + "Document.Protect.docx")
        protected_doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.Protect.docx")
        self.assertEqual(aw.ProtectionType.READ_ONLY, protected_doc.protection_type)
        builder = aw.DocumentBuilder(protected_doc)
        builder.writeln("Text added to a protected document.")
        self.assertEqual("Text added to a protected document.", protected_doc.range.text.strip())
        doc.unprotect()
        self.assertEqual(aw.ProtectionType.NO_PROTECTION, doc.protection_type)
        doc.protect(type=aw.ProtectionType.READ_ONLY, password="NewPassword")
        self.assertEqual(aw.ProtectionType.READ_ONLY, doc.protection_type)
        doc.unprotect("WrongPassword")
        self.assertEqual(aw.ProtectionType.READ_ONLY, doc.protection_type)
        doc.unprotect("NewPassword")
        self.assertEqual(aw.ProtectionType.NO_PROTECTION, doc.protection_type)

    def test_document_ensure_minimum(self):
        doc = aw.Document()
        nodes = doc.get_child_nodes(aw.NodeType.ANY, True)
        self.assertEqual(aw.NodeType.SECTION, nodes[0].node_type)
        self.assertEqual(doc, nodes[0].parent_node)
        self.assertEqual(aw.NodeType.BODY, nodes[1].node_type)
        self.assertEqual(nodes[0], nodes[1].parent_node)
        self.assertEqual(aw.NodeType.PARAGRAPH, nodes[2].node_type)
        self.assertEqual(nodes[1], nodes[2].parent_node)
        doc.remove_all_children()
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.ANY, True).count)
        doc.ensure_minimum()
        self.assertEqual(aw.NodeType.SECTION, nodes[0].node_type)
        self.assertEqual(aw.NodeType.BODY, nodes[1].node_type)
        self.assertEqual(aw.NodeType.PARAGRAPH, nodes[2].node_type)
        (nodes[2].as_paragraph()).runs.add(aw.Run(doc=doc, text="Hello world!"))
        self.assertEqual("Hello world!", doc.get_text().strip())

    def test_remove_macros_from_document(self):
        doc = aw.Document(file_name=MY_DIR + "Macro.docm")
        self.assertTrue(doc.has_macros)
        self.assertEqual("Project", doc.vba_project.name)
        doc.remove_macros()
        self.assertFalse(doc.has_macros)
        self.assertIsNone(doc.vba_project)

    def test_get_page_count(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write("Page 1")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.write("Page 2")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.write("Page 3")
        self.assertEqual(3, doc.page_count)
        doc.save(file_name=ARTIFACTS_DIR + "Document.GetPageCount.pdf")

    def test_get_updated_page_properties(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
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
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_get_original_file_info(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        self.assertEqual(MY_DIR + "Document.docx", doc.original_file_name)
        self.assertEqual(aw.LoadFormat.DOCX, doc.original_load_format)

    def test_footnote_columns(self):
        doc = aw.Document(file_name=MY_DIR + "Footnotes and endnotes.docx")
        self.assertEqual(0, doc.footnote_options.columns)
        doc.footnote_options.columns = 2
        doc.save(file_name=ARTIFACTS_DIR + "Document.FootnoteColumns.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.FootnoteColumns.docx")
        self.assertEqual(2, doc.first_section.page_setup.footnote_options.columns)

    def test_compare(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_compare_document_with_revisions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_compare_options(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_ignore_dml_unique_id(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_remove_external_schema_references(self):
        doc = aw.Document(file_name=MY_DIR + "External XML schema.docx")
        doc.remove_external_schema_references()

    def test_track_revisions(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_accept_all_revisions(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        doc.start_track_revisions(author="John Doe")
        builder.write("Hello world! ")
        builder.write("Hello again! ")
        builder.write("This is another revision.")
        doc.stop_track_revisions()
        self.assertEqual(3, doc.revisions.count)
        doc.accept_all_revisions()
        self.assertEqual(0, doc.revisions.count)
        self.assertEqual("Hello world! Hello again! This is another revision.", doc.get_text().strip())

    def test_get_revised_properties_of_list(self):
        doc = aw.Document(file_name=MY_DIR + "Revisions at list levels.docx")
        doc.update_list_labels()
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual("1.", paragraphs[0].list_label.label_string)
        self.assertEqual("a.", paragraphs[1].list_label.label_string)
        self.assertEqual("", paragraphs[2].list_label.label_string)
        doc.revisions_view = aw.RevisionsView.FINAL
        self.assertEqual("", paragraphs[0].list_label.label_string)
        self.assertEqual("1.", paragraphs[1].list_label.label_string)
        self.assertEqual("a.", paragraphs[2].list_label.label_string)
        doc.revisions_view = aw.RevisionsView.ORIGINAL
        doc.accept_all_revisions()
        self.assertEqual("a.", paragraphs[0].list_label.label_string)
        self.assertEqual("", paragraphs[1].list_label.label_string)
        self.assertEqual("b.", paragraphs[2].list_label.label_string)

    def test_update_thumbnail(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        builder.insert_image(file_name=IMAGE_DIR + "Logo.jpg")
        doc.update_thumbnail()
        doc.save(file_name=ARTIFACTS_DIR + "Document.UpdateThumbnail.FirstPage.epub")
        options = aw.rendering.ThumbnailGeneratingOptions()
        self.assertEqual(aspose.pydrawing.Size(600, 900), options.thumbnail_size)
        self.assertTrue(options.generate_from_first_page)
        options.thumbnail_size = aspose.pydrawing.Size(400, 400)
        options.generate_from_first_page = False
        doc.update_thumbnail(options)
        doc.save(file_name=ARTIFACTS_DIR + "Document.UpdateThumbnail.FirstImage.epub")

    def test_hyphenation_options(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_hyphenation_options_default_values(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_hyphenation_zone_exception(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_ooxml_compliance_version(self):
        doc = aw.Document(file_name=MY_DIR + "Document.doc")
        self.assertEqual(doc.compliance, aw.saving.OoxmlCompliance.ECMA376_2006)
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        self.assertEqual(doc.compliance, aw.saving.OoxmlCompliance.ISO29500_2008_TRANSITIONAL)

    def test_cleanup(self):
        doc = aw.Document()
        doc.styles.add(aw.StyleType.LIST, "MyListStyle1")
        doc.styles.add(aw.StyleType.LIST, "MyListStyle2")
        doc.styles.add(aw.StyleType.CHARACTER, "MyParagraphStyle1")
        doc.styles.add(aw.StyleType.CHARACTER, "MyParagraphStyle2")
        self.assertEqual(8, doc.styles.count)
        builder = aw.DocumentBuilder(doc)
        builder.font.style = doc.styles.get_by_name("MyParagraphStyle1")
        builder.writeln("Hello world!")
        list = doc.lists.add(list_style=doc.styles.get_by_name("MyListStyle1"))
        builder.list_format.list = list
        builder.writeln("Item 1")
        builder.writeln("Item 2")
        doc.cleanup()
        self.assertEqual(6, doc.styles.count)
        doc.first_section.body.remove_all_children()
        doc.cleanup()
        self.assertEqual(4, doc.styles.count)

    def test_automatically_update_styles(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_default_template(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_use_substitutions(self):
        raise NotImplementedError("Unsupported ctor for type Regex")

    def test_set_invalidate_field_types(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        field = builder.insert_field(field_code="DATE", field_value=None)
        self.assertEqual(aw.fields.FieldType.FIELD_DATE, field.type)
        field_text = doc.first_section.body.first_paragraph.get_child_nodes(aw.NodeType.RUN, True)[0].as_run()
        self.assertEqual("DATE", field_text.text)
        field_text.text = "PAGE"
        self.assertEqual("PAGE", field.get_field_code())
        self.assertEqual(aw.fields.FieldType.FIELD_DATE, field.type)
        self.assertEqual(aw.fields.FieldType.FIELD_DATE, field.start.field_type)
        self.assertEqual(aw.fields.FieldType.FIELD_DATE, field.separator.field_type)
        self.assertEqual(aw.fields.FieldType.FIELD_DATE, field.end.field_type)
        doc.normalize_field_types()
        self.assertEqual(aw.fields.FieldType.FIELD_PAGE, field.type)
        self.assertEqual(aw.fields.FieldType.FIELD_PAGE, field.start.field_type)
        self.assertEqual(aw.fields.FieldType.FIELD_PAGE, field.separator.field_type)
        self.assertEqual(aw.fields.FieldType.FIELD_PAGE, field.end.field_type)

    def test_layout_options_revisions(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_layout_options_hidden_text(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_layout_options_hidden_text(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_layout_options_paragraph_marks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_use_pdf_document_for_layout_options_paragraph_marks(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_update_page_layout(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Document.UpdatePageLayout.1.pdf")
        doc.styles.get_by_name("Normal").font.size = 6
        doc.sections[0].page_setup.orientation = aw.Orientation.LANDSCAPE
        doc.sections[0].page_setup.margins = aw.Margins.MIRRORED
        doc.update_page_layout()
        doc.save(file_name=ARTIFACTS_DIR + "Document.UpdatePageLayout.2.pdf")

    def test_doc_package_custom_parts(self):
        raise NotImplementedError("Unsupported call of method named TestDocPackageCustomParts")

    def test_shade_form_data(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_versions_count(self):
        doc = aw.Document(file_name=MY_DIR + "Versions.doc")
        self.assertEqual(4, doc.versions_count)
        doc.save(file_name=ARTIFACTS_DIR + "Document.VersionsCount.doc")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.VersionsCount.doc")
        self.assertEqual(0, doc.versions_count)

    def test_write_protection(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world! This document is protected.")
        self.assertFalse(doc.write_protection.is_write_protected)
        self.assertFalse(doc.write_protection.read_only_recommended)
        doc.write_protection.set_password("MyPassword")
        doc.write_protection.read_only_recommended = True
        self.assertTrue(doc.write_protection.is_write_protected)
        self.assertTrue(doc.write_protection.validate_password("MyPassword"))
        doc.save(file_name=ARTIFACTS_DIR + "Document.WriteProtection.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.WriteProtection.docx")
        self.assertTrue(doc.write_protection.is_write_protected)
        builder = aw.DocumentBuilder(doc)
        builder.move_to_document_end()
        builder.writeln("Writing text in a protected document.")
        self.assertEqual("Hello world! This document is protected." + "\rWriting text in a protected document.", doc.get_text().strip())
        self.assertTrue(doc.write_protection.read_only_recommended)
        self.assertTrue(doc.write_protection.validate_password("MyPassword"))
        self.assertFalse(doc.write_protection.validate_password("wrongpassword"))

    def test_remove_personal_information(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_show_comments(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_use_pdf_document_for_show_comments(self):
        raise NotImplementedError("Unsupported call of method named ShowComments")

    def test_copy_template_styles_via_document(self):
        template = aw.Document(file_name=MY_DIR + "Rendering.docx")
        target = aw.Document(file_name=MY_DIR + "Document.docx")
        self.assertEqual(18, template.styles.count)
        self.assertEqual(12, target.styles.count)
        target.copy_styles_from_template(template=template)
        self.assertEqual(22, target.styles.count)

    def test_copy_template_styles_via_document_new(self):
        template = aw.Document()
        style = template.styles.add(aw.StyleType.PARAGRAPH, "TemplateStyle1")
        style.font.name = "Times New Roman"
        style.font.color = aspose.pydrawing.Color.navy
        style = template.styles.add(aw.StyleType.PARAGRAPH, "TemplateStyle2")
        style.font.name = "Arial"
        style.font.color = aspose.pydrawing.Color.deep_sky_blue
        style = template.styles.add(aw.StyleType.PARAGRAPH, "TemplateStyle3")
        style.font.name = "Courier New"
        style.font.color = aspose.pydrawing.Color.royal_blue
        self.assertEqual(7, template.styles.count)
        target = aw.Document()
        style = target.styles.add(aw.StyleType.PARAGRAPH, "TemplateStyle3")
        style.font.name = "Calibri"
        style.font.color = aspose.pydrawing.Color.orange
        self.assertEqual(5, target.styles.count)
        target.copy_styles_from_template(template=template)
        self.assertEqual(7, target.styles.count)
        self.assertEqual("Courier New", target.styles.get_by_name("TemplateStyle3").font.name)
        self.assertEqual(aspose.pydrawing.Color.royal_blue.to_argb(), target.styles.get_by_name("TemplateStyle3").font.color.to_argb())
        target.copy_styles_from_template(template=MY_DIR + "Rendering.docx")
        self.assertEqual(21, target.styles.count)

    def test_read_macros_from_existing_document(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

    def test_save_output_parameters(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")
        parameters = doc.save(file_name=ARTIFACTS_DIR + "Document.SaveOutputParameters.doc")
        self.assertEqual("application/msword", parameters.content_type)
        parameters = doc.save(file_name=ARTIFACTS_DIR + "Document.SaveOutputParameters.pdf")
        self.assertEqual("application/pdf", parameters.content_type)

    def test_sub_document(self):
        doc = aw.Document(file_name=MY_DIR + "Master document.docx")
        sub_documents = doc.get_child_nodes(aw.NodeType.SUB_DOCUMENT, True)
        self.assertEqual(1, sub_documents.count)
        sub_document = sub_documents[0].as_sub_document()
        self.assertFalse(sub_document.is_composite)

    def test_create_web_extension(self):
        raise NotImplementedError("Unsupported target type System.Globalization.CultureInfo")

    def test_get_web_extension_info(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_epub_cover(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_text_watermark(self):
        doc = aw.Document()
        doc.watermark.set_text(text="Aspose Watermark")
        text_watermark_options = aw.TextWatermarkOptions()
        text_watermark_options.font_family = "Arial"
        text_watermark_options.font_size = 36
        text_watermark_options.color = aspose.pydrawing.Color.black
        text_watermark_options.layout = aw.WatermarkLayout.DIAGONAL
        text_watermark_options.is_semitrasparent = False
        doc.watermark.set_text(text="Aspose Watermark", options=text_watermark_options)
        doc.save(file_name=ARTIFACTS_DIR + "Document.TextWatermark.docx")
        if doc.watermark.type == aw.WatermarkType.TEXT:
            doc.watermark.remove()
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.TextWatermark.docx")
        self.assertEqual(aw.WatermarkType.TEXT, doc.watermark.type)

    def test_spelling_and_grammar_errors(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_granularity_compare_option(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_ignore_printer_metrics(self):
        doc = aw.Document(file_name=MY_DIR + "Rendering.docx")
        doc.layout_options.ignore_printer_metrics = False
        doc.save(file_name=ARTIFACTS_DIR + "Document.IgnorePrinterMetrics.docx")

    def test_extract_pages(self):
        doc = aw.Document(file_name=MY_DIR + "Layout entities.docx")
        doc = doc.extract_pages(0, 2)
        doc.save(file_name=ARTIFACTS_DIR + "Document.ExtractPages.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Document.ExtractPages.docx")
        self.assertEqual(doc.page_count, 2)

    def test_spelling_or_grammar(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_allow_embedding_post_script_fonts(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_frameset(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_open_azw(self):
        info = aw.FileFormatUtil.detect_file_format(file_name=MY_DIR + "Azw3 document.azw3")
        self.assertEqual(info.load_format, aw.LoadFormat.AZW3)
        doc = aw.Document(file_name=MY_DIR + "Azw3 document.azw3")
        self.assertTrue(("Hachette Book Group USA" in doc.get_text()))

    def test_open_epub(self):
        info = aw.FileFormatUtil.detect_file_format(file_name=MY_DIR + "Epub document.epub")
        self.assertEqual(info.load_format, aw.LoadFormat.EPUB)
        doc = aw.Document(file_name=MY_DIR + "Epub document.epub")
        self.assertTrue(("Down the Rabbit-Hole" in doc.get_text()))

    def test_open_xml(self):
        info = aw.FileFormatUtil.detect_file_format(file_name=MY_DIR + "Mail merge data - Customers.xml")
        self.assertEqual(info.load_format, aw.LoadFormat.XML)
        doc = aw.Document(file_name=MY_DIR + "Mail merge data - Purchase order.xml")
        self.assertTrue(("Ellen Adams\r123 Maple Street" in doc.get_text()))

    def test_move_to_structured_document_tag(self):
        doc = aw.Document(file_name=MY_DIR + "Structured document tags.docx")
        builder = aw.DocumentBuilder(doc)
        builder.move_to_structured_document_tag(structured_document_tag_index=1, character_index=1)
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 2, True).as_structured_document_tag()
        builder.move_to_structured_document_tag(structured_document_tag=tag, character_index=1)
        builder.write(" New text.")
        self.assertEqual("R New text.ichText", tag.get_text().strip())
        builder.move_to_structured_document_tag(structured_document_tag_index=1, character_index=-1)
        self.assertTrue(builder.is_at_end_of_structured_document_tag)
        builder.current_structured_document_tag.color = aspose.pydrawing.Color.green
        doc.save(file_name=ARTIFACTS_DIR + "Document.MoveToStructuredDocumentTag.docx")

    def test_include_textboxes_footnotes_endnotes_in_stat(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Lorem ipsum")
        builder.insert_footnote(footnote_type=aw.notes.FootnoteType.FOOTNOTE, footnote_text="sit amet")
        doc.update_word_count()
        self.assertEqual(2, doc.built_in_document_properties.words)
        doc.include_textboxes_footnotes_endnotes_in_stat = True
        doc.update_word_count()
        self.assertEqual(4, doc.built_in_document_properties.words)

    def test_set_justification_mode(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        justification_mode = doc.justification_mode
        if justification_mode == aw.settings.JustificationMode.EXPAND:
            doc.justification_mode = aw.settings.JustificationMode.COMPRESS
        doc.save(file_name=ARTIFACTS_DIR + "Document.SetJustificationMode.docx")

    def test_page_is_in_color(self):
        doc = aw.Document(file_name=MY_DIR + "Document.docx")
        self.assertFalse(doc.get_page_info(0).colored)

    def test_insert_document_inline(self):
        raise NotImplementedError("Unsupported target type System.String")
