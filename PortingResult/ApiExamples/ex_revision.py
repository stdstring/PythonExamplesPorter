# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.words as aw
import aspose.words.layout
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExRevision(ApiExampleBase):
    def test_revisions(self):
        raise NotImplementedError("Unsupported target type System.DateTime")

    def test_revision_collection(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_get_info_about_revisions_in_revision_groups(self):
        raise NotImplementedError("Unsupported target type System.Console")

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
        revision_options.moved_from_text_effect = aw.layout.RevisionTextEffect.DOUBLE_UNDERLINE
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
