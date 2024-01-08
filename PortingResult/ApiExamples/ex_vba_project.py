# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.vba
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExVbaProject(ApiExampleBase):
    def test_create_new_vba_project(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

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
        # for loop begin
        i = 0
        while i < original_vba_project.modules.count:
            self.assertEqual(copy_vba_project.modules[i].name, original_vba_project.modules[i].name)
            self.assertEqual(copy_vba_project.modules[i].type, original_vba_project.modules[i].type)
            self.assertEqual(copy_vba_project.modules[i].source_code, original_vba_project.modules[i].source_code)
            i += 1
        # for loop end

    def test_remove_vba_reference(self):
        raise NotImplementedError("Unsupported call of method named GetLibIdPath")