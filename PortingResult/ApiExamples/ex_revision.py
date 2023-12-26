# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.layout
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExRevision(ApiExampleBase):
    def test_revisions(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_revision_collection(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_get_info_about_revisions_in_revision_groups(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_get_specific_revision_group(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Revisions.docx")
        revision_group = doc.revisions.groups[0]
        self.assertEqual(aspose.words.RevisionType.DELETION, revision_group.revision_type)
        self.assertEqual("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ", revision_group.text)

    def test_show_revision_balloons(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Revisions.docx")
        doc.layout_options.revision_options.show_in_balloons = aspose.words.layout.ShowInBalloons.FORMAT_AND_DELETE
        doc.save(file_name = ARTIFACTS_DIR + "Revision.ShowRevisionBalloons.pdf")

    def test_revision_options(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Revisions.docx")
        revision_options = doc.layout_options.revision_options
        revision_options.inserted_text_color = aspose.words.layout.RevisionColor.GREEN
        revision_options.inserted_text_effect = aspose.words.layout.RevisionTextEffect.ITALIC
        revision_options.deleted_text_color = aspose.words.layout.RevisionColor.RED
        revision_options.deleted_text_effect = aspose.words.layout.RevisionTextEffect.BOLD
        revision_options.moved_from_text_color = aspose.words.layout.RevisionColor.YELLOW
        revision_options.moved_from_text_effect = aspose.words.layout.RevisionTextEffect.DOUBLE_STRIKE_THROUGH
        revision_options.moved_to_text_color = aspose.words.layout.RevisionColor.CLASSIC_BLUE
        revision_options.moved_from_text_effect = aspose.words.layout.RevisionTextEffect.DOUBLE_UNDERLINE
        revision_options.revised_properties_color = aspose.words.layout.RevisionColor.DARK_RED
        revision_options.revised_properties_effect = aspose.words.layout.RevisionTextEffect.BOLD
        revision_options.revision_bars_color = aspose.words.layout.RevisionColor.DARK_BLUE
        revision_options.revision_bars_width = 15
        revision_options.show_original_revision = True
        revision_options.show_revision_marks = True
        revision_options.show_in_balloons = aspose.words.layout.ShowInBalloons.FORMAT
        revision_options.comment_color = aspose.words.layout.RevisionColor.BRIGHT_GREEN
        doc.save(file_name = ARTIFACTS_DIR + "Revision.RevisionOptions.pdf")
