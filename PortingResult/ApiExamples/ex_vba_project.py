# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.vba
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExVbaProject(ApiExampleBase):
    def test_create_new_vba_project(self):
        #ExStart
        #ExFor:VbaProject.__init__
        #ExFor:VbaProject.name
        #ExFor:VbaModule.__init__
        #ExFor:VbaModule.name
        #ExFor:VbaModule.type
        #ExFor:VbaModule.source_code
        #ExFor:VbaModuleCollection.add(VbaModule)
        #ExFor:VbaModuleType
        #ExSummary:Shows how to create a VBA project using macros.
        doc = aw.Document()
        # Create a new VBA project.
        project = aw.vba.VbaProject()
        project.name = "Aspose.Project"
        doc.vba_project = project
        # Create a new module and specify a macro source code.
        module = aw.vba.VbaModule()
        module.name = "Aspose.Module"
        module.type = aw.vba.VbaModuleType.PROCEDURAL_MODULE
        module.source_code = "New source code"
        # Add the module to the VBA project.
        doc.vba_project.modules.add(module)
        doc.save(file_name=ARTIFACTS_DIR + "VbaProject.CreateVBAMacros.docm")
        #ExEnd
        project = aw.Document(file_name=ARTIFACTS_DIR + "VbaProject.CreateVBAMacros.docm").vba_project
        self.assertEqual("Aspose.Project", project.name)
        modules = doc.vba_project.modules
        self.assertEqual(2, modules.count)
        self.assertEqual("ThisDocument", modules[0].name)
        self.assertEqual(aw.vba.VbaModuleType.DOCUMENT_MODULE, modules[0].type)
        self.assertIsNone(modules[0].source_code)
        self.assertEqual("Aspose.Module", modules[1].name)
        self.assertEqual(aw.vba.VbaModuleType.PROCEDURAL_MODULE, modules[1].type)
        self.assertEqual("New source code", modules[1].source_code)

    def test_clone_vba_project(self):
        #ExStart
        #ExFor:VbaProject.clone
        #ExFor:VbaModule.clone
        #ExSummary:Shows how to deep clone a VBA project and module.
        doc = aw.Document(file_name=MY_DIR + "VBA project.docm")
        dest_doc = aw.Document()
        copy_vba_project = doc.vba_project.clone()
        dest_doc.vba_project = copy_vba_project
        # In the destination document, we already have a module named "Module1"
        # because we cloned it along with the project. We will need to remove the module.
        old_vba_module = dest_doc.vba_project.modules.get_by_name("Module1")
        copy_vba_module = doc.vba_project.modules.get_by_name("Module1").clone()
        dest_doc.vba_project.modules.remove(old_vba_module)
        dest_doc.vba_project.modules.add(copy_vba_module)
        dest_doc.save(file_name=ARTIFACTS_DIR + "VbaProject.CloneVbaProject.docm")
        #ExEnd
        original_vba_project = aw.Document(file_name=ARTIFACTS_DIR + "VbaProject.CloneVbaProject.docm").vba_project
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
