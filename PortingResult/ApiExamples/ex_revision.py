# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.comparing
import aspose.words.drawing
import aspose.words.layout
import aspose.words.notes
import datetime
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExRevision(ApiExampleBase):
    def test_revisions(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_revision_collection(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_get_info_about_revisions_in_revision_groups(self):
        #ExStart
        #ExFor:RevisionGroup
        #ExFor:RevisionGroup.author
        #ExFor:RevisionGroup.revision_type
        #ExFor:RevisionGroup.text
        #ExFor:RevisionGroupCollection
        #ExFor:RevisionGroupCollection.count
        #ExSummary:Shows how to print info about a group of revisions in a document.
        doc = aw.Document(file_name=MY_DIR + "Revisions.docx")
        self.assertEqual(7, doc.revisions.groups.count)
        for group in doc.revisions.groups:
            print(f"Revision author: {group.author}; Revision type: {group.revision_type} \n\tRevision text: {group.text}")
        #ExEnd

    def test_get_specific_revision_group(self):
        #ExStart
        #ExFor:RevisionGroupCollection
        #ExFor:RevisionGroupCollection.__getitem__(int)
        #ExSummary:Shows how to get a group of revisions in a document.
        doc = aw.Document(file_name=MY_DIR + "Revisions.docx")
        revision_group = doc.revisions.groups[0]
        #ExEnd
        self.assertEqual(aw.RevisionType.DELETION, revision_group.revision_type)
        self.assertEqual("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ", revision_group.text)

    def test_show_revision_balloons(self):
        #ExStart
        #ExFor:RevisionOptions.show_in_balloons
        #ExSummary:Shows how to display revisions in balloons.
        doc = aw.Document(file_name=MY_DIR + "Revisions.docx")
        # By default, text that is a revision has a different color to differentiate it from the other non-revision text.
        # Set a revision option to show more details about each revision in a balloon on the page's right margin.
        doc.layout_options.revision_options.show_in_balloons = aw.layout.ShowInBalloons.FORMAT_AND_DELETE
        doc.save(file_name=ARTIFACTS_DIR + "Revision.ShowRevisionBalloons.pdf")
        #ExEnd

    def test_revision_options(self):
        #ExStart
        #ExFor:ShowInBalloons
        #ExFor:RevisionOptions.show_in_balloons
        #ExFor:RevisionOptions.comment_color
        #ExFor:RevisionOptions.deleted_text_color
        #ExFor:RevisionOptions.deleted_text_effect
        #ExFor:RevisionOptions.inserted_text_effect
        #ExFor:RevisionOptions.moved_from_text_color
        #ExFor:RevisionOptions.moved_from_text_effect
        #ExFor:RevisionOptions.moved_to_text_color
        #ExFor:RevisionOptions.moved_to_text_effect
        #ExFor:RevisionOptions.revised_properties_color
        #ExFor:RevisionOptions.revised_properties_effect
        #ExFor:RevisionOptions.revision_bars_color
        #ExFor:RevisionOptions.revision_bars_width
        #ExFor:RevisionOptions.show_original_revision
        #ExFor:RevisionOptions.show_revision_marks
        #ExFor:RevisionTextEffect
        #ExSummary:Shows how to modify the appearance of revisions.
        doc = aw.Document(file_name=MY_DIR + "Revisions.docx")
        # Get the RevisionOptions object that controls the appearance of revisions.
        revision_options = doc.layout_options.revision_options
        # Render insertion revisions in green and italic.
        revision_options.inserted_text_color = aw.layout.RevisionColor.GREEN
        revision_options.inserted_text_effect = aw.layout.RevisionTextEffect.ITALIC
        # Render deletion revisions in red and bold.
        revision_options.deleted_text_color = aw.layout.RevisionColor.RED
        revision_options.deleted_text_effect = aw.layout.RevisionTextEffect.BOLD
        # The same text will appear twice in a movement revision:
        # once at the departure point and once at the arrival destination.
        # Render the text at the moved-from revision yellow with a double strike through
        # and double-underlined blue at the moved-to revision.
        revision_options.moved_from_text_color = aw.layout.RevisionColor.YELLOW
        revision_options.moved_from_text_effect = aw.layout.RevisionTextEffect.DOUBLE_STRIKE_THROUGH
        revision_options.moved_to_text_color = aw.layout.RevisionColor.CLASSIC_BLUE
        revision_options.moved_to_text_effect = aw.layout.RevisionTextEffect.DOUBLE_UNDERLINE
        # Render format revisions in dark red and bold.
        revision_options.revised_properties_color = aw.layout.RevisionColor.DARK_RED
        revision_options.revised_properties_effect = aw.layout.RevisionTextEffect.BOLD
        # Place a thick dark blue bar on the left side of the page next to lines affected by revisions.
        revision_options.revision_bars_color = aw.layout.RevisionColor.DARK_BLUE
        revision_options.revision_bars_width = 15
        # Show revision marks and original text.
        revision_options.show_original_revision = True
        revision_options.show_revision_marks = True
        # Get movement, deletion, formatting revisions, and comments to show up in green balloons
        # on the right side of the page.
        revision_options.show_in_balloons = aw.layout.ShowInBalloons.FORMAT
        revision_options.comment_color = aw.layout.RevisionColor.BRIGHT_GREEN
        # These features are only applicable to formats such as .pdf or .jpg.
        doc.save(file_name=ARTIFACTS_DIR + "Revision.RevisionOptions.pdf")
        #ExEnd

    def test_track_revisions(self):
        raise NotImplementedError("Unsupported target type System.TimeSpan")

    def test_accept_all_revisions(self):
        #ExStart
        #ExFor:Document.accept_all_revisions
        #ExSummary:Shows how to accept all tracking changes in the document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Edit the document while tracking changes to create a few revisions.
        doc.start_track_revisions(author="John Doe")
        builder.write("Hello world! ")
        builder.write("Hello again! ")
        builder.write("This is another revision.")
        doc.stop_track_revisions()
        self.assertEqual(3, doc.revisions.count)
        # We can iterate through every revision and accept/reject it as a part of our document.
        # If we know we wish to accept every revision, we can do it more straightforwardly so by calling this method.
        doc.accept_all_revisions()
        self.assertEqual(0, doc.revisions.count)
        self.assertEqual("Hello world! Hello again! This is another revision.", doc.get_text().strip())
        #ExEnd

    def test_get_revised_properties_of_list(self):
        #ExStart
        #ExFor:RevisionsView
        #ExFor:Document.revisions_view
        #ExSummary:Shows how to switch between the revised and the original view of a document.
        doc = aw.Document(file_name=MY_DIR + "Revisions at list levels.docx")
        doc.update_list_labels()
        paragraphs = doc.first_section.body.paragraphs
        self.assertEqual("1.", paragraphs[0].list_label.label_string)
        self.assertEqual("a.", paragraphs[1].list_label.label_string)
        self.assertEqual("", paragraphs[2].list_label.label_string)
        # View the document object as if all the revisions are accepted. Currently supports list labels.
        doc.revisions_view = aw.RevisionsView.FINAL
        self.assertEqual("", paragraphs[0].list_label.label_string)
        self.assertEqual("1.", paragraphs[1].list_label.label_string)
        self.assertEqual("a.", paragraphs[2].list_label.label_string)
        #ExEnd
        doc.revisions_view = aw.RevisionsView.ORIGINAL
        doc.accept_all_revisions()
        self.assertEqual("a.", paragraphs[0].list_label.label_string)
        self.assertEqual("", paragraphs[1].list_label.label_string)
        self.assertEqual("b.", paragraphs[2].list_label.label_string)

    def test_compare(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_compare_document_with_revisions(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_compare_options(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_ignore_dml_unique_id(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_layout_options_revisions(self):
        #ExStart
        #ExFor:Document.layout_options
        #ExFor:LayoutOptions
        #ExFor:LayoutOptions.revision_options
        #ExFor:RevisionColor
        #ExFor:RevisionOptions
        #ExFor:RevisionOptions.inserted_text_color
        #ExFor:RevisionOptions.show_revision_bars
        #ExFor:RevisionOptions.revision_bars_position
        #ExSummary:Shows how to alter the appearance of revisions in a rendered output document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert a revision, then change the color of all revisions to green.
        builder.writeln("This is not a revision.")
        doc.start_track_revisions(author="John Doe", date_time=datetime.datetime.now())
        self.assertEqual(aw.layout.RevisionColor.BY_AUTHOR, doc.layout_options.revision_options.inserted_text_color) #ExSkip
        self.assertTrue(doc.layout_options.revision_options.show_revision_bars) #ExSkip
        builder.writeln("This is a revision.")
        doc.stop_track_revisions()
        builder.writeln("This is not a revision.")
        # Remove the bar that appears to the left of every revised line.
        doc.layout_options.revision_options.inserted_text_color = aw.layout.RevisionColor.BRIGHT_GREEN
        doc.layout_options.revision_options.show_revision_bars = False
        doc.layout_options.revision_options.revision_bars_position = aw.drawing.HorizontalAlignment.RIGHT
        doc.save(file_name=ARTIFACTS_DIR + "Document.LayoutOptionsRevisions.pdf")
        #ExEnd

    def test_granularity_compare_option(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_ignore_store_item_id(self):
        #ExStart:IgnoreStoreItemId
        #ExFor:AdvancedCompareOptions
        #ExFor:AdvancedCompareOptions.ignore_store_item_id
        #ExSummary:Shows how to compare SDT with same content but different store item id.
        doc_a = aw.Document(file_name=MY_DIR + "Document with SDT 1.docx")
        doc_b = aw.Document(file_name=MY_DIR + "Document with SDT 2.docx")
        # Configure options to compare SDT with same content but different store item id.
        compare_options = aw.comparing.CompareOptions()
        compare_options.advanced_options.ignore_store_item_id = False
        doc_a.compare(document=doc_b, author="user", date_time=datetime.datetime.now(), options=compare_options)
        self.assertEqual(8, doc_a.revisions.count)
        compare_options.advanced_options.ignore_store_item_id = True
        doc_a.revisions.reject_all()
        doc_a.compare(document=doc_b, author="user", date_time=datetime.datetime.now(), options=compare_options)
        self.assertEqual(0, doc_a.revisions.count)
        #ExEnd:IgnoreStoreItemId
