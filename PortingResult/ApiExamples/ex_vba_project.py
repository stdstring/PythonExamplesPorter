# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.vba
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExVbaProject(ApiExampleBase):
    def test_create_new_vba_project(self):
        doc = aspose.words.Document()
        project = aspose.words.vba.VbaProject()
        project.name = "Aspose.Project"
        doc.vba_project = project
        module = aspose.words.vba.VbaModule()
        module.name = "Aspose.Module"
        module.type = aspose.words.vba.VbaModuleType.PROCEDURAL_MODULE
        module.source_code = "New source code"
        doc.vba_project.modules.add(module)
        doc.save(file_name = ARTIFACTS_DIR + "VbaProject.CreateVBAMacros.docm")
        project = aspose.words.Document(file_name = ARTIFACTS_DIR + "VbaProject.CreateVBAMacros.docm").vba_project
        self.assertEqual("Aspose.Project", project.name)
        modules = doc.vba_project.modules
        self.assertEqual(2, modules.count)
        self.assertEqual("ThisDocument", modules[0].name)
        self.assertEqual(aspose.words.vba.VbaModuleType.DOCUMENT_MODULE, modules[0].type)
        self.assertIsNone(modules[0].source_code)
        self.assertEqual("Aspose.Module", modules[1].name)
        self.assertEqual(aspose.words.vba.VbaModuleType.PROCEDURAL_MODULE, modules[1].type)
        self.assertEqual("New source code", modules[1].source_code)

    def test_clone_vba_project(self):
        doc = aspose.words.Document(file_name = MY_DIR + "VBA project.docm")
        dest_doc = aspose.words.Document()
        copy_vba_project = doc.vba_project.clone()
        dest_doc.vba_project = copy_vba_project
        old_vba_module = dest_doc.vba_project.modules.get_by_name("Module1")
        copy_vba_module = doc.vba_project.modules.get_by_name("Module1").clone()
        dest_doc.vba_project.modules.remove(old_vba_module)
        dest_doc.vba_project.modules.add(copy_vba_module)
        dest_doc.save(file_name = ARTIFACTS_DIR + "VbaProject.CloneVbaProject.docm")
        original_vba_project = aspose.words.Document(file_name = ARTIFACTS_DIR + "VbaProject.CloneVbaProject.docm").vba_project
        self.assertEqual(copy_vba_project.name, original_vba_project.name)
        self.assertEqual(copy_vba_project.code_page, original_vba_project.code_page)
        self.assertEqual(copy_vba_project.is_signed, original_vba_project.is_signed)
        self.assertEqual(copy_vba_project.modules.count, original_vba_project.modules.count)
        i = 0
        while i < original_vba_project.modules.count:
            self.assertEqual(copy_vba_project.modules[i].name, original_vba_project.modules[i].name)
            self.assertEqual(copy_vba_project.modules[i].type, original_vba_project.modules[i].type)
            self.assertEqual(copy_vba_project.modules[i].source_code, original_vba_project.modules[i].source_code)
            i += 1

    def test_remove_vba_reference(self):
        raise NotImplementedError("Unsupported call of method named GetLibIdPath")
