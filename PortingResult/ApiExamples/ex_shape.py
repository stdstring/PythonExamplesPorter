# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words as aw
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

    def test_font(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_coordinates(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_group_shape(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_is_top_level(self):
        doc = aw.Document()
        shape = aw.drawing.Shape(doc, aw.drawing.ShapeType.RECTANGLE)
        shape.width = 200
        shape.height = 200
        shape.wrap_type = aw.drawing.WrapType.NONE
        self.assertTrue(shape.is_top_level)
        group = aw.drawing.GroupShape(doc)
        group.append_child(shape)
        self.assertFalse(shape.is_top_level)

    def test_local_to_parent(self):
        doc = aw.Document()
        group = aw.drawing.GroupShape(doc)
        group.bounds = aspose.pydrawing.RectangleF(100, 100, 500, 500)
        self.assertEqual(aspose.pydrawing.PointF(100, 100), group.local_to_parent(aspose.pydrawing.PointF(0, 0)))
        self.assertEqual(aspose.pydrawing.PointF(150, 150), group.local_to_parent(aspose.pydrawing.PointF(100, 100)))
        self.assertEqual(aspose.pydrawing.PointF(200, 200), group.local_to_parent(aspose.pydrawing.PointF(200, 200)))
        self.assertEqual(aspose.pydrawing.PointF(250, 250), group.local_to_parent(aspose.pydrawing.PointF(300, 300)))
        group.coord_origin = aspose.pydrawing.Point(-250, -250)
        self.assertEqual(aspose.pydrawing.PointF(375, 375), group.local_to_parent(aspose.pydrawing.PointF(300, 300)))
        group.coord_size = aspose.pydrawing.Size(500, 500)
        self.assertEqual(aspose.pydrawing.PointF(650, 650), group.local_to_parent(aspose.pydrawing.PointF(300, 300)))
        self.assertEqual(aspose.pydrawing.PointF(700, 700), group.local_to_parent(aspose.pydrawing.PointF(350, 350)))
        shape = aw.drawing.Shape(doc, aw.drawing.ShapeType.RECTANGLE)
        shape.width = 100
        shape.height = 100
        shape.left = 700
        shape.top = 700
        group.append_child(shape)
        doc.first_section.body.first_paragraph.append_child(group)
        doc.save(file_name=ARTIFACTS_DIR + "Shape.LocalToParent.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.LocalToParent.docx")
        group = doc.get_child(aw.NodeType.GROUP_SHAPE, 0, True).as_group_shape()
        self.assertEqual(aspose.pydrawing.RectangleF(100, 100, 500, 500), group.bounds)
        self.assertEqual(aspose.pydrawing.Size(500, 500), group.coord_size)
        self.assertEqual(aspose.pydrawing.Point(-250, -250), group.coord_origin)

    def test_anchor_locked(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_delete_all_shapes(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=400, height=200)
        builder.insert_shape(shape_type=aw.drawing.ShapeType.STAR, width=300, height=300)
        group = aw.drawing.GroupShape(doc)
        group.bounds = aspose.pydrawing.RectangleF(100, 50, 200, 100)
        group.coord_origin = aspose.pydrawing.Point(-1000, -500)
        sub_shape = aw.drawing.Shape(doc, aw.drawing.ShapeType.CUBE)
        sub_shape.width = 500
        sub_shape.height = 700
        sub_shape.left = 0
        sub_shape.top = 0
        group.append_child(sub_shape)
        builder.insert_node(group)
        self.assertEqual(3, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True).count)
        shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
        shapes.clear()
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True).count)
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
        group_shapes = doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True)
        group_shapes.clear()
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True).count)
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)

    def test_is_inline(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_bounds(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_flip_shape_orientation(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_fill(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_texture_fill(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        shape.fill.preset_textured(aw.drawing.PresetTexture.CANVAS)
        shape.fill.texture_alignment = aw.drawing.TextureAlignment.TOP_RIGHT
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name=ARTIFACTS_DIR + "Shape.TextureFill.docx", save_options=save_options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.TextureFill.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.drawing.TextureAlignment.TOP_RIGHT, shape.fill.texture_alignment)

    def test_gradient_fill(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        shape.fill.one_color_gradient(color=aspose.pydrawing.Color.red, style=aw.drawing.GradientStyle.HORIZONTAL, variant=aw.drawing.GradientVariant.VARIANT2, degree=0.1)
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), shape.fill.fore_color.to_argb())
        self.assertEqual(aw.drawing.GradientStyle.HORIZONTAL, shape.fill.gradient_style)
        self.assertEqual(aw.drawing.GradientVariant.VARIANT2, shape.fill.gradient_variant)
        self.assertEqual(270, shape.fill.gradient_angle)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        shape.fill.two_color_gradient(style=aw.drawing.GradientStyle.FROM_CORNER, variant=aw.drawing.GradientVariant.VARIANT4)
        shape.fill.back_color = aspose.pydrawing.Color.yellow
        shape.fill.gradient_angle = 15
        self.assertEqual(aspose.pydrawing.Color.yellow.to_argb(), shape.fill.back_color.to_argb())
        self.assertEqual(aw.drawing.GradientStyle.FROM_CORNER, shape.fill.gradient_style)
        self.assertEqual(aw.drawing.GradientVariant.VARIANT4, shape.fill.gradient_variant)
        self.assertEqual(0, shape.fill.gradient_angle)
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name=ARTIFACTS_DIR + "Shape.GradientFill.docx", save_options=save_options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.GradientFill.docx")
        first_shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), first_shape.fill.fore_color.to_argb())
        self.assertEqual(aw.drawing.GradientStyle.HORIZONTAL, first_shape.fill.gradient_style)
        self.assertEqual(aw.drawing.GradientVariant.VARIANT2, first_shape.fill.gradient_variant)
        self.assertEqual(270, first_shape.fill.gradient_angle)
        second_shape = doc.get_child(aw.NodeType.SHAPE, 1, True).as_shape()
        self.assertEqual(aspose.pydrawing.Color.yellow.to_argb(), second_shape.fill.back_color.to_argb())
        self.assertEqual(aw.drawing.GradientStyle.FROM_CORNER, second_shape.fill.gradient_style)
        self.assertEqual(aw.drawing.GradientVariant.VARIANT4, second_shape.fill.gradient_variant)
        self.assertEqual(0, second_shape.fill.gradient_angle)

    def test_gradient_stops(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        shape.fill.two_color_gradient(color1=aspose.pydrawing.Color.green, color2=aspose.pydrawing.Color.red, style=aw.drawing.GradientStyle.HORIZONTAL, variant=aw.drawing.GradientVariant.VARIANT2)
        gradient_stops = shape.fill.gradient_stops
        gradient_stops[0].color = aspose.pydrawing.Color.aqua
        gradient_stops[0].position = 0.1
        gradient_stops[0].transparency = 0.25
        gradient_stop = aw.drawing.GradientStop(color=aspose.pydrawing.Color.brown, position=0.5)
        gradient_stops.add(gradient_stop)
        gradient_stops.remove_at(1)
        gradient_stops.insert(1, aw.drawing.GradientStop(color=aspose.pydrawing.Color.chocolate, position=0.75, transparency=0.3))
        gradient_stop = gradient_stops[2]
        gradient_stops.remove(gradient_stop)
        self.assertEqual(2, gradient_stops.count)
        self.assertEqual(aspose.pydrawing.Color.from_argb(255, 0, 255, 255), gradient_stops[0].base_color)
        self.assertEqual(aspose.pydrawing.Color.aqua.to_argb(), gradient_stops[0].color.to_argb())
        self.assertAlmostEqual(0.1, gradient_stops[0].position, delta=0.01)
        self.assertAlmostEqual(0.25, gradient_stops[0].transparency, delta=0.01)
        self.assertEqual(aspose.pydrawing.Color.chocolate.to_argb(), gradient_stops[1].color.to_argb())
        self.assertAlmostEqual(0.75, gradient_stops[1].position, delta=0.01)
        self.assertAlmostEqual(0.3, gradient_stops[1].transparency, delta=0.01)
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name=ARTIFACTS_DIR + "Shape.GradientStops.docx", save_options=save_options)
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.GradientStops.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        gradient_stops = shape.fill.gradient_stops
        self.assertEqual(2, gradient_stops.count)
        self.assertEqual(aspose.pydrawing.Color.aqua.to_argb(), gradient_stops[0].color.to_argb())
        self.assertAlmostEqual(0.1, gradient_stops[0].position, delta=0.01)
        self.assertAlmostEqual(0.25, gradient_stops[0].transparency, delta=0.01)
        self.assertEqual(aspose.pydrawing.Color.chocolate.to_argb(), gradient_stops[1].color.to_argb())
        self.assertAlmostEqual(0.75, gradient_stops[1].position, delta=0.01)
        self.assertAlmostEqual(0.3, gradient_stops[1].transparency, delta=0.01)

    def test_fill_pattern(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_fill_theme_color(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.ROUND_RECTANGLE, width=80, height=80)
        fill = shape.fill
        fill.fore_theme_color = aw.themes.ThemeColor.DARK1
        fill.back_theme_color = aw.themes.ThemeColor.BACKGROUND2
        if fill.back_tint_and_shade == 0:
            fill.back_tint_and_shade = 0.2
        doc.save(file_name=ARTIFACTS_DIR + "Shape.FillThemeColor.docx")

    def test_fill_tint_and_shade(self):
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        text_fill = doc.first_section.body.first_paragraph.runs[0].font.fill
        text_fill.fore_theme_color = aw.themes.ThemeColor.ACCENT1
        if text_fill.fore_tint_and_shade == 0:
            text_fill.fore_tint_and_shade = 0.5
        doc.save(file_name=ARTIFACTS_DIR + "Shape.FillTintAndShade.docx")

    def test_title(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_replace_textboxes_with_images(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_create_text_box(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_z_order(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_get_active_x_control_properties(self):
        doc = aw.Document(file_name=MY_DIR + "ActiveX controls.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        ole_control = shape.ole_format.ole_control
        self.assertEqual("CheckBox1", ole_control.name)
        if ole_control.is_forms2_ole_control:
            check_box = ole_control.as_forms2_ole_control()
            self.assertEqual("First", check_box.caption)
            self.assertEqual("0", check_box.value)
            self.assertEqual(True, check_box.enabled)
            self.assertEqual(aw.drawing.ole.Forms2OleControlType.CHECK_BOX, check_box.type)
            self.assertEqual(None, check_box.child_nodes)
            self.assertEqual("", check_box.group_name)
            check_box.group_name = "Aspose group name"
        doc.save(file_name=ARTIFACTS_DIR + "Shape.GetActiveXControlProperties.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.GetActiveXControlProperties.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        forms_2_ole_control = shape.ole_format.ole_control.as_forms2_ole_control()
        self.assertEqual("Aspose group name", forms_2_ole_control.group_name)

    def test_get_ole_object_raw_data(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_linked_chart_source_full_name(self):
        raise NotImplementedError("Unsupported target type System.StringComparison")

    def test_ole_control(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_ole_links(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_ole_control_collection(self):
        raise NotImplementedError("Unsupported target type System.Guid")

    def test_suggested_file_name(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_object_did_not_have_suggested_file_name(self):
        doc = aw.Document(file_name=MY_DIR + "ActiveX controls.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual("", shape.ole_format.suggested_file_name)

    def test_office_math_display_exception(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_office_math_default_value(self):
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        office_math = doc.get_child(aw.NodeType.OFFICE_MATH, 6, True).as_office_math()
        self.assertEqual(aw.math.OfficeMathDisplayType.INLINE, office_math.display_type)
        self.assertEqual(aw.math.OfficeMathJustification.INLINE, office_math.justification)

    def test_office_math(self):
        raise NotImplementedError("Unsupported type: ApiExamples.DocumentHelper")

    def test_cannot_be_set_display_with_inline_justification(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_cannot_be_set_inline_display_with_justification(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_office_math_display_nested_objects(self):
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        office_math = doc.get_child(aw.NodeType.OFFICE_MATH, 0, True).as_office_math()
        self.assertEqual(aw.math.OfficeMathDisplayType.DISPLAY, office_math.display_type)
        self.assertEqual(aw.math.OfficeMathJustification.CENTER, office_math.justification)

    def test_work_with_math_object_type(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_aspect_ratio(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_markup_language_by_default(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
        self.assertEqual(aw.drawing.ShapeMarkupLanguage.DML, shape.markup_language)
        self.assertEqual(aspose.pydrawing.SizeF(300, 300), shape.size_in_points)

    def test_markup_language_for_different_ms_word_versions(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_stroke(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, horz_pos=aw.drawing.RelativeHorizontalPosition.LEFT_MARGIN, left=100, vert_pos=aw.drawing.RelativeVerticalPosition.TOP_MARGIN, top=100, width=200, height=200, wrap_type=aw.drawing.WrapType.NONE)
        shape.fill.fore_color = aspose.pydrawing.Color.white
        stroke = shape.stroke
        stroke.on = True
        stroke.weight = 5
        stroke.color = aspose.pydrawing.Color.red
        stroke.dash_style = aw.drawing.DashStyle.SHORT_DASH_DOT_DOT
        stroke.join_style = aw.drawing.JoinStyle.MITER
        stroke.end_cap = aw.drawing.EndCap.SQUARE
        stroke.line_style = aw.drawing.ShapeLineStyle.TRIPLE
        stroke.fill.two_color_gradient(color1=aspose.pydrawing.Color.red, color2=aspose.pydrawing.Color.blue, style=aw.drawing.GradientStyle.VERTICAL, variant=aw.drawing.GradientVariant.VARIANT1)
        doc.save(file_name=ARTIFACTS_DIR + "Shape.Stroke.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.Stroke.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        stroke = shape.stroke
        self.assertEqual(True, stroke.on)
        self.assertEqual(5, stroke.weight)
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), stroke.color.to_argb())
        self.assertEqual(aw.drawing.DashStyle.SHORT_DASH_DOT_DOT, stroke.dash_style)
        self.assertEqual(aw.drawing.JoinStyle.MITER, stroke.join_style)
        self.assertEqual(aw.drawing.EndCap.SQUARE, stroke.end_cap)
        self.assertEqual(aw.drawing.ShapeLineStyle.TRIPLE, stroke.line_style)

    def test_insert_ole_object_as_html_file(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_ole_object(file_name="http://www.aspose.com", prog_id="htmlfile", is_linked=True, as_icon=False, presentation=None)
        doc.save(file_name=ARTIFACTS_DIR + "Shape.InsertOleObjectAsHtmlFile.docx")

    def test_get_access_to_ole_package(self):
        raise NotImplementedError("Unsupported expression: TypeOfExpression")

    def test_resize(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=200, height=300)
        shape.height = 300
        shape.width = 500
        shape.rotation = 30
        doc.save(file_name=ARTIFACTS_DIR + "Shape.Resize.docx")

    def test_calendar(self):
        raise NotImplementedError("Unsupported target type System.String")

    def test_is_layout_in_cell(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_shape_insertion(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_signature_line(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_text_box_layout_flow(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_text_box_fit_shape_to_text(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_text_box_margins(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_text_box_contents_wrap_mode(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_text_box_shape_type(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        doc.compatibility_options.optimize_for(aw.settings.MsWordVersion.WORD2016)
        text_box_shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.TEXT_BOX, width=100, height=100)
        text_box_shape.text_box.vertical_anchor = aw.drawing.TextBoxAnchor.BOTTOM
        builder.move_to(text_box_shape.last_paragraph)
        builder.write("Text placed bottom")
        doc.save(file_name=ARTIFACTS_DIR + "Shape.TextBoxShapeType.docx")

    def test_create_link_between_text_boxes(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_vertical_anchor(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_insert_text_paths(self):
        raise NotImplementedError("Unsupported call of method named AppendWordArt")

    def test_shape_revision(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

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
        doc = aw.Document(file_name=MY_DIR + "Decorative shapes.docx")
        shape = doc.get_child_nodes(aw.NodeType.SHAPE, True)[0].as_shape()
        self.assertTrue(shape.is_decorative)
        shape.alternative_text = "Alternative text."
        self.assertFalse(shape.is_decorative)
        builder = aw.DocumentBuilder(doc)
        builder.move_to_document_end()
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=100, height=100)
        shape.is_decorative = True
        doc.save(file_name=ARTIFACTS_DIR + "Shape.IsDecorative.docx")

    def test_fill_image(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_shadow_format(self):
        doc = aw.Document(file_name=MY_DIR + "Shape stroke pattern border.docx")
        shape = doc.get_child_nodes(aw.NodeType.SHAPE, True)[0].as_shape()
        if shape.shadow_format.visible and shape.shadow_format.type == aw.drawing.ShadowType.SHADOW2:
            shape.shadow_format.type = aw.drawing.ShadowType.SHADOW7
        if shape.shadow_format.type == aw.drawing.ShadowType.SHADOW_MIXED:
            shape.shadow_format.clear()

    def test_no_text_rotation(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.ELLIPSE, width=20, height=20)
        shape.text_box.no_text_rotation = True
        doc.save(file_name=ARTIFACTS_DIR + "Shape.NoTextRotation.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.NoTextRotation.docx")
        shape = doc.get_child_nodes(aw.NodeType.SHAPE, True)[0].as_shape()
        self.assertEqual(True, shape.text_box.no_text_rotation)

    def test_relative_size_and_position(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=100, height=40)
        shape.wrap_type = aw.drawing.WrapType.NONE
        if shape.relative_horizontal_size == aw.drawing.RelativeHorizontalSize.DEFAULT:
            shape.relative_horizontal_size = aw.drawing.RelativeHorizontalSize.MARGIN
            shape.width_relative = 50
        if shape.relative_vertical_size == aw.drawing.RelativeVerticalSize.DEFAULT:
            shape.relative_vertical_size = aw.drawing.RelativeVerticalSize.MARGIN
            shape.height_relative = 30
        if shape.relative_vertical_position == aw.drawing.RelativeVerticalPosition.PARAGRAPH:
            shape.relative_vertical_position = aw.drawing.RelativeVerticalPosition.TOP_MARGIN
            shape.top_relative = 30
        if shape.relative_horizontal_position == aw.drawing.RelativeHorizontalPosition.DEFAULT:
            shape.relative_horizontal_position = aw.drawing.RelativeHorizontalPosition.RIGHT_MARGIN
            shape.left_relative = -260
        doc.save(file_name=ARTIFACTS_DIR + "Shape.RelativeSizeAndPosition.docx")

    def test_fill_base_color(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder()
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=100, height=40)
        shape.fill.fore_color = aspose.pydrawing.Color.red
        shape.fill.fore_tint_and_shade = 0.5
        shape.stroke.fill.fore_color = aspose.pydrawing.Color.green
        shape.stroke.fill.transparency = 0.5
        self.assertEqual(aspose.pydrawing.Color.from_argb(255, 255, 188, 188).to_argb(), shape.fill.fore_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), shape.fill.base_fore_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.from_argb(128, 0, 128, 0).to_argb(), shape.stroke.fore_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), shape.stroke.base_fore_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), shape.stroke.fill.fore_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.green.to_argb(), shape.stroke.fill.base_fore_color.to_argb())

    def test_fit_image_to_shape(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=300, height=450)
        shape.image_data.set_image(file_name=IMAGE_DIR + "Barcode.png")
        shape.image_data.fit_image_to_shape()
        doc.save(file_name=ARTIFACTS_DIR + "Shape.FitImageToShape.docx")

    def test_stroke_fore_theme_colors(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.TEXT_BOX, width=100, height=40)
        stroke = shape.stroke
        stroke.fore_theme_color = aw.themes.ThemeColor.DARK1
        stroke.fore_tint_and_shade = 0.5
        doc.save(file_name=ARTIFACTS_DIR + "Shape.StrokeForeThemeColors.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.StrokeForeThemeColors.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.themes.ThemeColor.DARK1, shape.stroke.fore_theme_color)
        self.assertEqual(0.5, shape.stroke.fore_tint_and_shade)

    def test_stroke_back_theme_colors(self):
        doc = aw.Document(file_name=MY_DIR + "Stroke gradient outline.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        stroke = shape.stroke
        stroke.back_theme_color = aw.themes.ThemeColor.DARK2
        stroke.back_tint_and_shade = 0.2
        doc.save(file_name=ARTIFACTS_DIR + "Shape.StrokeBackThemeColors.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.StrokeBackThemeColors.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.themes.ThemeColor.DARK2, shape.stroke.back_theme_color)
        precision = 1E-06
        self.assertAlmostEqual(0.2, shape.stroke.back_tint_and_shade, delta=precision)

    def test_text_box_ole_control(self):
        doc = aw.Document(file_name=MY_DIR + "Textbox control.docm")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        text_box_control = shape.ole_format.ole_control.as_text_box_control()
        self.assertEqual("Aspose.Words test", text_box_control.text)
        text_box_control.text = "Updated text"
        self.assertEqual("Updated text", text_box_control.text)
