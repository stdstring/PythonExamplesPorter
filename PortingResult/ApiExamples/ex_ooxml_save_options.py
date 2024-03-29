# -*- coding: utf-8 -*-
import aspose.words as aw
import aspose.words.drawing
import aspose.words.saving
import aspose.words.settings
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR


class ExOoxmlSaveOptions(ApiExampleBase):
    def test_password(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_iso_29500_strict(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        doc.compatibility_options.optimize_for(aw.settings.MsWordVersion.WORD2003)
        builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
        self.assertEqual(aw.drawing.ShapeMarkupLanguage.VML, (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).markup_language)
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        save_options.save_format = aw.SaveFormat.DOCX
        doc.save(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.Iso29500Strict.docx", save_options=save_options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.Iso29500Strict.docx")
        self.assertEqual(aw.drawing.ShapeMarkupLanguage.DML, (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).markup_language)

    def test_restarting_document_list(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_last_saved_time(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_document_compression(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_check_file_signatures(self):
        raise NotImplementedError("Unsupported member target type - System.String[] for expression: fileSignatures")

    def test_export_generator_name(self):
        doc = aw.Document()
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.export_generator_name = False
        doc.save(file_name=ARTIFACTS_DIR + "OoxmlSaveOptions.ExportGeneratorName.docx", save_options=save_options)

    def test_zip_64_mode_option(self):
        raise NotImplementedError("Unsupported ctor for type Random")
