# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.drawing.ole
import aspose.words.math
import aspose.words.saving
import aspose.words.settings
import aspose.words.themes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, IMAGE_DIR, MY_DIR


class ExShape(ApiExampleBase):
    def test_alt_text(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_coordinates(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_group_shape(self):
        raise NotImplementedError("Unsupported type: RectangleF")

    def test_is_top_level(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_local_to_parent(self):
        raise NotImplementedError("Unsupported type: RectangleF")

    def test_delete_all_shapes(self):
        raise NotImplementedError("Unsupported type: RectangleF")

    def test_is_inline(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_bounds(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_flip_shape_orientation(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_fill(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_texture_fill(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.RECTANGLE, width = 80, height = 80)
        shape.fill.preset_textured(aspose.words.drawing.PresetTexture.CANVAS)
        shape.fill.texture_alignment = aspose.words.drawing.TextureAlignment.TOP_RIGHT
        save_options = aspose.words.saving.OoxmlSaveOptions()
        save_options.compliance = aspose.words.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name = ARTIFACTS_DIR + "Shape.TextureFill.docx", save_options = save_options)
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Shape.TextureFill.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aspose.words.drawing.TextureAlignment.TOP_RIGHT, shape.fill.texture_alignment)

    def test_gradient_fill(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_gradient_stops(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_fill_pattern(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_fill_theme_color(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.ROUND_RECTANGLE, width = 80, height = 80)
        fill = shape.fill
        fill.fore_theme_color = aspose.words.themes.ThemeColor.DARK1
        fill.back_theme_color = aspose.words.themes.ThemeColor.BACKGROUND2
        # if begin
        if fill.back_tint_and_shade == 0:
            fill.back_tint_and_shade = 0.2
        # if end
        doc.save(file_name = ARTIFACTS_DIR + "Shape.FillThemeColor.docx")

    def test_fill_tint_and_shade(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Big document.docx")
        text_fill = doc.first_section.body.first_paragraph.runs[0].font.fill
        text_fill.fore_theme_color = aspose.words.themes.ThemeColor.ACCENT1
        # if begin
        if text_fill.fore_tint_and_shade == 0:
            text_fill.fore_tint_and_shade = 0.5
        # if end
        doc.save(file_name = ARTIFACTS_DIR + "Shape.FillTintAndShade.docx")

    def test_title(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_replace_textboxes_with_images(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_create_text_box(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_z_order(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_get_active_x_control_properties(self):
        doc = aspose.words.Document(file_name = MY_DIR + "ActiveX controls.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        ole_control = shape.ole_format.ole_control
        self.assertEqual("CheckBox1", ole_control.name)
        # if begin
        if ole_control.is_forms2_ole_control:
            check_box = ole_control.as_forms2_ole_control()
            self.assertEqual("Первый", check_box.caption)
            self.assertEqual("0", check_box.value)
            self.assertEqual(True, check_box.enabled)
            self.assertEqual(aspose.words.drawing.ole.Forms2OleControlType.CHECK_BOX, check_box.type)
            self.assertEqual(None, check_box.child_nodes)
            self.assertEqual("", check_box.group_name)
            check_box.group_name = "Aspose group name"
        # if end
        doc.save(file_name = ARTIFACTS_DIR + "Shape.GetActiveXControlProperties.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Shape.GetActiveXControlProperties.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        forms_2_ole_control = shape.ole_format.ole_control.as_forms2_ole_control()
        self.assertEqual("Aspose group name", forms_2_ole_control.group_name)

    def test_get_ole_object_raw_data(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_linked_chart_source_full_name(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_ole_control(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_ole_links(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_ole_control_collection(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_suggested_file_name(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_object_did_not_have_suggested_file_name(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Is")

    def test_resolution_default_values(self):
        image_options = aspose.words.saving.ImageSaveOptions(aspose.words.SaveFormat.JPEG)
        self.assertEqual(96, image_options.horizontal_resolution)
        self.assertEqual(96, image_options.vertical_resolution)

    def test_office_math_display_exception(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_office_math_default_value(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Office math.docx")
        office_math = doc.get_child(aspose.words.NodeType.OFFICE_MATH, 6, True).as_office_math()
        self.assertEqual(aspose.words.math.OfficeMathDisplayType.INLINE, office_math.display_type)
        self.assertEqual(aspose.words.math.OfficeMathJustification.INLINE, office_math.justification)

    def test_office_math(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_cannot_be_set_display_with_inline_justification(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_cannot_be_set_inline_display_with_justification(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_office_math_display_nested_objects(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Office math.docx")
        office_math = doc.get_child(aspose.words.NodeType.OFFICE_MATH, 0, True).as_office_math()
        self.assertEqual(aspose.words.math.OfficeMathDisplayType.DISPLAY, office_math.display_type)
        self.assertEqual(aspose.words.math.OfficeMathJustification.CENTER, office_math.justification)

    def test_markup_language_by_default(self):
        raise NotImplementedError("Unsupported type: SizeF")

    def test_stroke(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_insert_ole_object_as_html_file(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.insert_ole_object(file_name = "http://www.aspose.com", prog_id = "htmlfile", is_linked = True, as_icon = False, presentation = None)
        doc.save(file_name = ARTIFACTS_DIR + "Shape.InsertOleObjectAsHtmlFile.docx")

    def test_get_access_to_ole_package(self):
        raise NotImplementedError("Unsupported expression: TypeOfExpression")

    def test_resize(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.RECTANGLE, width = 200, height = 300)
        shape.height = 300
        shape.width = 500
        shape.rotation = 30
        doc.save(file_name = ARTIFACTS_DIR + "Shape.Resize.docx")

    def test_calendar(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_shape_insertion(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_signature_line(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_text_box_fit_shape_to_text(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_text_box_margins(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_text_box_shape_type(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        doc.compatibility_options.optimize_for(aspose.words.settings.MsWordVersion.WORD2016)
        text_box_shape = builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.TEXT_BOX, width = 100, height = 100)
        text_box_shape.text_box.vertical_anchor = aspose.words.drawing.TextBoxAnchor.BOTTOM
        builder.move_to(text_box_shape.last_paragraph)
        builder.write("Text placed bottom")
        doc.save(file_name = ARTIFACTS_DIR + "Shape.TextBoxShapeType.docx")

    def test_create_link_between_text_boxes(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_insert_text_paths(self):
        raise NotImplementedError("Unsupported call of method named AppendWordArt")

    def test_shape_revision(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_move_revisions(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_adjust_with_effects(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_render_all_shapes(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_document_has_smart_art_object(self):
        raise NotImplementedError("Unsupported expression: SimpleLambdaExpression")

    def test_shape_types(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_is_decorative(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_fill_image(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_shadow_format(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Shape stroke pattern border.docx")
        shape = doc.get_child_nodes(aspose.words.NodeType.SHAPE, True)[0].as_shape()
        # if begin
        if shape.shadow_format.visible and shape.shadow_format.type == aspose.words.drawing.ShadowType.SHADOW2:
            shape.shadow_format.type = aspose.words.drawing.ShadowType.SHADOW7
        # if end
        # if begin
        if shape.shadow_format.type == aspose.words.drawing.ShadowType.SHADOW_MIXED:
            shape.shadow_format.clear()
        # if end

    def test_no_text_rotation(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.ELLIPSE, width = 20, height = 20)
        shape.text_box.no_text_rotation = True
        doc.save(file_name = ARTIFACTS_DIR + "Shape.NoTextRotation.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Shape.NoTextRotation.docx")
        shape = doc.get_child_nodes(aspose.words.NodeType.SHAPE, True)[0].as_shape()
        self.assertEqual(True, shape.text_box.no_text_rotation)

    def test_relative_size_and_position(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type = aspose.words.drawing.ShapeType.RECTANGLE, width = 100, height = 40)
        shape.wrap_type = aspose.words.drawing.WrapType.NONE
        # if begin
        if shape.relative_horizontal_size == aspose.words.drawing.RelativeHorizontalSize.DEFAULT:
            shape.relative_horizontal_size = aspose.words.drawing.RelativeHorizontalSize.MARGIN
            shape.width_relative = 50
        # if end
        # if begin
        if shape.relative_vertical_size == aspose.words.drawing.RelativeVerticalSize.DEFAULT:
            shape.relative_vertical_size = aspose.words.drawing.RelativeVerticalSize.MARGIN
            shape.height_relative = 30
        # if end
        # if begin
        if shape.relative_vertical_position == aspose.words.drawing.RelativeVerticalPosition.PARAGRAPH:
            shape.relative_vertical_position = aspose.words.drawing.RelativeVerticalPosition.TOP_MARGIN
            shape.top_relative = 30
        # if end
        # if begin
        if shape.relative_horizontal_position == aspose.words.drawing.RelativeHorizontalPosition.DEFAULT:
            shape.relative_horizontal_position = aspose.words.drawing.RelativeHorizontalPosition.RIGHT_MARGIN
            shape.left_relative = -260
        # if end
        doc.save(file_name = ARTIFACTS_DIR + "Shape.RelativeSizeAndPosition.docx")
