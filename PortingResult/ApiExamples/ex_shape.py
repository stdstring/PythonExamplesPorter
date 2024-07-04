# -*- coding: utf-8 -*-

# Copyright (c) 2001-2024 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.
#####################################

import aspose.pydrawing
import aspose.words as aw
import aspose.words.drawing
import aspose.words.drawing.ole
import aspose.words.math
import aspose.words.rendering
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

    def test_rotate(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_coordinates(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_group_shape(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_is_top_level(self):
        #ExStart
        #ExFor:ShapeBase.is_top_level
        #ExSummary:Shows how to tell whether a shape is a part of a group shape.
        doc = aw.Document()
        shape = aw.drawing.Shape(doc, aw.drawing.ShapeType.RECTANGLE)
        shape.width = 200
        shape.height = 200
        shape.wrap_type = aw.drawing.WrapType.NONE
        # A shape by default is not part of any group shape, and therefore has the "IsTopLevel" property set to "true".
        self.assertTrue(shape.is_top_level)
        group = aw.drawing.GroupShape(doc)
        group.append_child(shape)
        # Once we assimilate a shape into a group shape, the "IsTopLevel" property changes to "false".
        self.assertFalse(shape.is_top_level)
        #ExEnd

    def test_local_to_parent(self):
        #ExStart
        #ExFor:ShapeBase.coord_origin
        #ExFor:ShapeBase.coord_size
        #ExFor:ShapeBase.local_to_parent(PointF)
        #ExSummary:Shows how to translate the x and y coordinate location on a shape's coordinate plane to a location on the parent shape's coordinate plane.
        doc = aw.Document()
        # Insert a group shape, and place it 100 points below and to the right of
        # the document's x and Y coordinate origin point.
        group = aw.drawing.GroupShape(doc)
        group.bounds = aspose.pydrawing.RectangleF(100, 100, 500, 500)
        # Use the "LocalToParent" method to determine that (0, 0) on the group's internal x and y coordinates
        # lies on (100, 100) of its parent shape's coordinate system. The group shape's parent is the document itself.
        self.assertEqual(aspose.pydrawing.PointF(100, 100), group.local_to_parent(aspose.pydrawing.PointF(0, 0)))
        # By default, a shape's internal coordinate plane has the top left corner at (0, 0),
        # and the bottom right corner at (1000, 1000). Due to its size, our group shape covers an area of 500pt x 500pt
        # in the document's plane. This means that a movement of 1pt on the document's coordinate plane will translate
        # to a movement of 2pts on the group shape's coordinate plane.
        self.assertEqual(aspose.pydrawing.PointF(150, 150), group.local_to_parent(aspose.pydrawing.PointF(100, 100)))
        self.assertEqual(aspose.pydrawing.PointF(200, 200), group.local_to_parent(aspose.pydrawing.PointF(200, 200)))
        self.assertEqual(aspose.pydrawing.PointF(250, 250), group.local_to_parent(aspose.pydrawing.PointF(300, 300)))
        # Move the group shape's x and y axis origin from the top left corner to the center.
        # This will offset the group's internal coordinates relative to the document's coordinates even further.
        group.coord_origin = aspose.pydrawing.Point(-250, -250)
        self.assertEqual(aspose.pydrawing.PointF(375, 375), group.local_to_parent(aspose.pydrawing.PointF(300, 300)))
        # Changing the scale of the coordinate plane will also affect relative locations.
        group.coord_size = aspose.pydrawing.Size(500, 500)
        self.assertEqual(aspose.pydrawing.PointF(650, 650), group.local_to_parent(aspose.pydrawing.PointF(300, 300)))
        # If we wish to add a shape to this group while defining its location based on a location in the document,
        # we will need to first confirm a location in the group shape that will match the document's location.
        self.assertEqual(aspose.pydrawing.PointF(700, 700), group.local_to_parent(aspose.pydrawing.PointF(350, 350)))
        shape = aw.drawing.Shape(doc, aw.drawing.ShapeType.RECTANGLE)
        shape.width = 100
        shape.height = 100
        shape.left = 700
        shape.top = 700
        group.append_child(shape)
        doc.first_section.body.first_paragraph.append_child(group)
        doc.save(file_name=ARTIFACTS_DIR + "Shape.LocalToParent.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.LocalToParent.docx")
        group = doc.get_child(aw.NodeType.GROUP_SHAPE, 0, True).as_group_shape()
        self.assertEqual(aspose.pydrawing.RectangleF(100, 100, 500, 500), group.bounds)
        self.assertEqual(aspose.pydrawing.Size(500, 500), group.coord_size)
        self.assertEqual(aspose.pydrawing.Point(-250, -250), group.coord_origin)

    def test_anchor_locked(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_delete_all_shapes(self):
        #ExStart
        #ExFor:Shape
        #ExSummary:Shows how to delete all shapes from a document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert two shapes along with a group shape with another shape inside it.
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
        # Remove all Shape nodes from the document.
        shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
        shapes.clear()
        # All shapes are gone, but the group shape is still in the document.
        self.assertEqual(1, doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True).count)
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
        # Remove all group shapes separately.
        group_shapes = doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True)
        group_shapes.clear()
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.GROUP_SHAPE, True).count)
        self.assertEqual(0, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
        #ExEnd

    def test_is_inline(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_bounds(self):
        raise NotImplementedError("Forbidden object initializer")

    def test_flip_shape_orientation(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_fill(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_texture_fill(self):
        #ExStart
        #ExFor:Fill.texture_alignment
        #ExFor:TextureAlignment
        #ExSummary:Shows how to fill and tiling the texture inside the shape.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        # Apply texture alignment to the shape fill.
        shape.fill.preset_textured(aw.drawing.PresetTexture.CANVAS)
        shape.fill.texture_alignment = aw.drawing.TextureAlignment.TOP_RIGHT
        # Use the compliance option to define the shape using DML if you want to get "TextureAlignment"
        # property after the document saves.
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name=ARTIFACTS_DIR + "Shape.TextureFill.docx", save_options=save_options)
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.TextureFill.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.drawing.TextureAlignment.TOP_RIGHT, shape.fill.texture_alignment)

    def test_gradient_fill(self):
        #ExStart
        #ExFor:Fill.one_color_gradient(Color,GradientStyle,GradientVariant,float)
        #ExFor:Fill.one_color_gradient(GradientStyle,GradientVariant,float)
        #ExFor:Fill.two_color_gradient(Color,Color,GradientStyle,GradientVariant)
        #ExFor:Fill.two_color_gradient(GradientStyle,GradientVariant)
        #ExFor:Fill.gradient_style
        #ExFor:Fill.gradient_variant
        #ExFor:Fill.gradient_angle
        #ExFor:GradientStyle
        #ExFor:GradientVariant
        #ExSummary:Shows how to fill a shape with a gradients.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        # Apply One-color gradient fill to the shape with ForeColor of gradient fill.
        shape.fill.one_color_gradient(color=aspose.pydrawing.Color.red, style=aw.drawing.GradientStyle.HORIZONTAL, variant=aw.drawing.GradientVariant.VARIANT2, degree=0.1)
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), shape.fill.fore_color.to_argb())
        self.assertEqual(aw.drawing.GradientStyle.HORIZONTAL, shape.fill.gradient_style)
        self.assertEqual(aw.drawing.GradientVariant.VARIANT2, shape.fill.gradient_variant)
        self.assertEqual(270, shape.fill.gradient_angle)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        # Apply Two-color gradient fill to the shape.
        shape.fill.two_color_gradient(style=aw.drawing.GradientStyle.FROM_CORNER, variant=aw.drawing.GradientVariant.VARIANT4)
        # Change BackColor of gradient fill.
        shape.fill.back_color = aspose.pydrawing.Color.yellow
        # Note that changes "GradientAngle" for "GradientStyle.FromCorner/GradientStyle.FromCenter"
        # gradient fill don't get any effect, it will work only for linear gradient.
        shape.fill.gradient_angle = 15
        self.assertEqual(aspose.pydrawing.Color.yellow.to_argb(), shape.fill.back_color.to_argb())
        self.assertEqual(aw.drawing.GradientStyle.FROM_CORNER, shape.fill.gradient_style)
        self.assertEqual(aw.drawing.GradientVariant.VARIANT4, shape.fill.gradient_variant)
        self.assertEqual(0, shape.fill.gradient_angle)
        # Use the compliance option to define the shape using DML if you want to get "GradientStyle",
        # "GradientVariant" and "GradientAngle" properties after the document saves.
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name=ARTIFACTS_DIR + "Shape.GradientFill.docx", save_options=save_options)
        #ExEnd
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
        #ExStart
        #ExFor:Fill.gradient_stops
        #ExFor:GradientStopCollection
        #ExFor:GradientStopCollection.insert(int,GradientStop)
        #ExFor:GradientStopCollection.add(GradientStop)
        #ExFor:GradientStopCollection.remove_at(int)
        #ExFor:GradientStopCollection.remove(GradientStop)
        #ExFor:GradientStopCollection.__getitem__(int)
        #ExFor:GradientStopCollection.count
        #ExFor:GradientStop.__init__(Color,float)
        #ExFor:GradientStop.__init__(Color,float,float)
        #ExFor:GradientStop.base_color
        #ExFor:GradientStop.color
        #ExFor:GradientStop.position
        #ExFor:GradientStop.transparency
        #ExFor:GradientStop.remove
        #ExSummary:Shows how to add gradient stops to the gradient fill.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=80, height=80)
        shape.fill.two_color_gradient(color1=aspose.pydrawing.Color.green, color2=aspose.pydrawing.Color.red, style=aw.drawing.GradientStyle.HORIZONTAL, variant=aw.drawing.GradientVariant.VARIANT2)
        # Get gradient stops collection.
        gradient_stops = shape.fill.gradient_stops
        # Change first gradient stop.
        gradient_stops[0].color = aspose.pydrawing.Color.aqua
        gradient_stops[0].position = 0.1
        gradient_stops[0].transparency = 0.25
        # Add new gradient stop to the end of collection.
        gradient_stop = aw.drawing.GradientStop(color=aspose.pydrawing.Color.brown, position=0.5)
        gradient_stops.add(gradient_stop)
        # Remove gradient stop at index 1.
        gradient_stops.remove_at(1)
        # And insert new gradient stop at the same index 1.
        gradient_stops.insert(1, aw.drawing.GradientStop(color=aspose.pydrawing.Color.chocolate, position=0.75, transparency=0.3))
        # Remove last gradient stop in the collection.
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
        # Use the compliance option to define the shape using DML
        # if you want to get "GradientStops" property after the document saves.
        save_options = aw.saving.OoxmlSaveOptions()
        save_options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT
        doc.save(file_name=ARTIFACTS_DIR + "Shape.GradientStops.docx", save_options=save_options)
        #ExEnd
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
        #ExStart
        #ExFor:Fill.fore_theme_color
        #ExFor:Fill.back_theme_color
        #ExFor:Fill.back_tint_and_shade
        #ExSummary:Shows how to set theme color for foreground/background shape color.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.ROUND_RECTANGLE, width=80, height=80)
        fill = shape.fill
        fill.fore_theme_color = aw.themes.ThemeColor.DARK1
        fill.back_theme_color = aw.themes.ThemeColor.BACKGROUND2
        # Note: do not use "BackThemeColor" and "BackTintAndShade" for font fill.
        if fill.back_tint_and_shade == 0:
            fill.back_tint_and_shade = 0.2
        doc.save(file_name=ARTIFACTS_DIR + "Shape.FillThemeColor.docx")
        #ExEnd

    def test_fill_tint_and_shade(self):
        #ExStart
        #ExFor:Fill.fore_tint_and_shade
        #ExSummary:Shows how to manage lightening and darkening foreground font color.
        doc = aw.Document(file_name=MY_DIR + "Big document.docx")
        text_fill = doc.first_section.body.first_paragraph.runs[0].font.fill
        text_fill.fore_theme_color = aw.themes.ThemeColor.ACCENT1
        if text_fill.fore_tint_and_shade == 0:
            text_fill.fore_tint_and_shade = 0.5
        doc.save(file_name=ARTIFACTS_DIR + "Shape.FillTintAndShade.docx")
        #ExEnd

    def test_title(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_replace_textboxes_with_images(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_create_text_box(self):
        raise NotImplementedError("Unsupported type: ApiExamples.TestUtil")

    def test_z_order(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_get_active_x_control_properties(self):
        #ExStart
        #ExFor:OleControl
        #ExFor:OleControl.is_forms2_ole_control
        #ExFor:OleControl.name
        #ExFor:OleFormat.ole_control
        #ExFor:Forms2OleControl
        #ExFor:Forms2OleControl.caption
        #ExFor:Forms2OleControl.value
        #ExFor:Forms2OleControl.enabled
        #ExFor:Forms2OleControl.type
        #ExFor:Forms2OleControl.child_nodes
        #ExFor:Forms2OleControl.group_name
        #ExSummary:Shows how to verify the properties of an ActiveX control.
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
        # Note, that you can't set GroupName for a Frame.
            check_box.group_name = "Aspose group name"
        #ExEnd
        doc.save(file_name=ARTIFACTS_DIR + "Shape.GetActiveXControlProperties.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.GetActiveXControlProperties.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        forms_2_ole_control = shape.ole_format.ole_control.as_forms2_ole_control()
        self.assertEqual("Aspose group name", forms_2_ole_control.group_name)

    def test_get_ole_object_raw_data(self):
        raise NotImplementedError("Unsupported expression: ConditionalExpression")

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

    def test_render_office_math(self):
        raise NotImplementedError("Unsupported call of method named IsRunningOnMono")

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

    def test_aspect_ratio(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_markup_language_by_default(self):
        #ExStart
        #ExFor:ShapeBase.markup_language
        #ExFor:ShapeBase.size_in_points
        #ExSummary:Shows how to verify a shape's size and markup language.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_image(file_name=IMAGE_DIR + "Transparent background logo.png")
        self.assertEqual(aw.drawing.ShapeMarkupLanguage.DML, shape.markup_language)
        self.assertEqual(aspose.pydrawing.SizeF(300, 300), shape.size_in_points)
        #ExEnd

    def test_markup_language_for_different_ms_word_versions(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_stroke(self):
        #ExStart
        #ExFor:Stroke
        #ExFor:Stroke.on
        #ExFor:Stroke.weight
        #ExFor:Stroke.join_style
        #ExFor:Stroke.line_style
        #ExFor:Stroke.fill
        #ExFor:ShapeLineStyle
        #ExSummary:Shows how change stroke properties.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, horz_pos=aw.drawing.RelativeHorizontalPosition.LEFT_MARGIN, left=100, vert_pos=aw.drawing.RelativeVerticalPosition.TOP_MARGIN, top=100, width=200, height=200, wrap_type=aw.drawing.WrapType.NONE)
        # Basic shapes, such as the rectangle, have two visible parts.
        # 1 -  The fill, which applies to the area within the outline of the shape:
        shape.fill.fore_color = aspose.pydrawing.Color.white
        # 2 -  The stroke, which marks the outline of the shape:
        # Modify various properties of this shape's stroke.
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
        #ExEnd
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
        # Set compatibility options to correctly using of VerticalAnchor property.
        doc.compatibility_options.optimize_for(aw.settings.MsWordVersion.WORD2016)
        text_box_shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.TEXT_BOX, width=100, height=100)
        # Not all formats are compatible with this one.
        # For most of the incompatible formats, AW generated warnings on save, so use doc.WarningCallback to check it.
        text_box_shape.text_box.vertical_anchor = aw.drawing.TextBoxAnchor.BOTTOM
        builder.move_to(text_box_shape.last_paragraph)
        builder.write("Text placed bottom")
        doc.save(file_name=ARTIFACTS_DIR + "Shape.TextBoxShapeType.docx")

    def test_create_link_between_text_boxes(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_vertical_anchor(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_insert_text_paths(self):
        raise NotImplementedError("ignored method body")

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

    def test_office_math_renderer(self):
        #ExStart
        #ExFor:NodeRendererBase
        #ExFor:NodeRendererBase.bounds_in_points
        #ExFor:NodeRendererBase.get_bounds_in_pixels(float,float)
        #ExFor:NodeRendererBase.get_bounds_in_pixels(float,float,float)
        #ExFor:NodeRendererBase.get_opaque_bounds_in_pixels(float,float)
        #ExFor:NodeRendererBase.get_opaque_bounds_in_pixels(float,float,float)
        #ExFor:NodeRendererBase.get_size_in_pixels(float,float)
        #ExFor:NodeRendererBase.get_size_in_pixels(float,float,float)
        #ExFor:NodeRendererBase.opaque_bounds_in_points
        #ExFor:NodeRendererBase.size_in_points
        #ExFor:OfficeMathRenderer
        #ExFor:OfficeMathRenderer.__init__(OfficeMath)
        #ExSummary:Shows how to measure and scale shapes.
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        office_math = doc.get_child(aw.NodeType.OFFICE_MATH, 0, True).as_office_math()
        renderer = aw.rendering.OfficeMathRenderer(office_math)
        # Verify the size of the image that the OfficeMath object will create when we render it.
        self.assertAlmostEqual(119, renderer.size_in_points.width, delta=0.25)
        self.assertAlmostEqual(13, renderer.size_in_points.height, delta=0.1)
        self.assertAlmostEqual(119, renderer.bounds_in_points.width, delta=0.25)
        self.assertAlmostEqual(13, renderer.bounds_in_points.height, delta=0.1)
        # Shapes with transparent parts may contain different values in the "OpaqueBoundsInPoints" properties.
        self.assertAlmostEqual(119, renderer.opaque_bounds_in_points.width, delta=0.25)
        self.assertAlmostEqual(14.2, renderer.opaque_bounds_in_points.height, delta=0.1)
        # Get the shape size in pixels, with linear scaling to a specific DPI.
        bounds = renderer.get_bounds_in_pixels(scale=1, dpi=96)
        self.assertEqual(159, bounds.width)
        self.assertEqual(18, bounds.height)
        # Get the shape size in pixels, but with a different DPI for the horizontal and vertical dimensions.
        bounds = renderer.get_bounds_in_pixels(scale=1, horizontal_dpi=96, vertical_dpi=150)
        self.assertEqual(159, bounds.width)
        self.assertEqual(28, bounds.height)
        # The opaque bounds may vary here also.
        bounds = renderer.get_opaque_bounds_in_pixels(scale=1, dpi=96)
        self.assertEqual(159, bounds.width)
        self.assertEqual(18, bounds.height)
        bounds = renderer.get_opaque_bounds_in_pixels(scale=1, horizontal_dpi=96, vertical_dpi=150)
        self.assertEqual(159, bounds.width)
        self.assertEqual(30, bounds.height)
        #ExEnd

    def test_shape_types(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerable")

    def test_is_decorative(self):
        #ExStart
        #ExFor:ShapeBase.is_decorative
        #ExSummary:Shows how to set that the shape is decorative.
        doc = aw.Document(file_name=MY_DIR + "Decorative shapes.docx")
        shape = doc.get_child_nodes(aw.NodeType.SHAPE, True)[0].as_shape()
        self.assertTrue(shape.is_decorative)
        # If "AlternativeText" is not empty, the shape cannot be decorative.
        # That's why our value has changed to 'false'.
        shape.alternative_text = "Alternative text."
        self.assertFalse(shape.is_decorative)
        builder = aw.DocumentBuilder(doc)
        builder.move_to_document_end()
        # Create a new shape as decorative.
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=100, height=100)
        shape.is_decorative = True
        doc.save(file_name=ARTIFACTS_DIR + "Shape.IsDecorative.docx")
        #ExEnd

    def test_fill_image(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_shadow_format(self):
        #ExStart
        #ExFor:ShadowFormat.visible
        #ExFor:ShadowFormat.clear()
        #ExFor:ShadowType
        #ExSummary:Shows how to work with a shadow formatting for the shape.
        doc = aw.Document(file_name=MY_DIR + "Shape stroke pattern border.docx")
        shape = doc.get_child_nodes(aw.NodeType.SHAPE, True)[0].as_shape()
        if shape.shadow_format.visible and shape.shadow_format.type == aw.drawing.ShadowType.SHADOW2:
            shape.shadow_format.type = aw.drawing.ShadowType.SHADOW7
        if shape.shadow_format.type == aw.drawing.ShadowType.SHADOW_MIXED:
            shape.shadow_format.clear()
        #ExEnd

    def test_no_text_rotation(self):
        #ExStart
        #ExFor:TextBox.no_text_rotation
        #ExSummary:Shows how to disable text rotation when the shape is rotate.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.ELLIPSE, width=20, height=20)
        shape.text_box.no_text_rotation = True
        doc.save(file_name=ARTIFACTS_DIR + "Shape.NoTextRotation.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.NoTextRotation.docx")
        shape = doc.get_child_nodes(aw.NodeType.SHAPE, True)[0].as_shape()
        self.assertEqual(True, shape.text_box.no_text_rotation)

    def test_relative_size_and_position(self):
        #ExStart
        #ExFor:ShapeBase.relative_horizontal_size
        #ExFor:ShapeBase.relative_vertical_size
        #ExFor:ShapeBase.width_relative
        #ExFor:ShapeBase.height_relative
        #ExFor:ShapeBase.top_relative
        #ExFor:ShapeBase.left_relative
        #ExFor:RelativeHorizontalSize
        #ExFor:RelativeVerticalSize
        #ExSummary:Shows how to set relative size and position.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Adding a simple shape with absolute size and position.
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=100, height=40)
        # Set WrapType to WrapType.None since Inline shapes are automatically converted to absolute units.
        shape.wrap_type = aw.drawing.WrapType.NONE
        # Checking and setting the relative horizontal size.
        if shape.relative_horizontal_size == aw.drawing.RelativeHorizontalSize.DEFAULT:
        # Setting the horizontal size binding to Margin.
            shape.relative_horizontal_size = aw.drawing.RelativeHorizontalSize.MARGIN
        # Setting the width to 50% of Margin width.
            shape.width_relative = 50
        # Checking and setting the relative vertical size.
        if shape.relative_vertical_size == aw.drawing.RelativeVerticalSize.DEFAULT:
        # Setting the vertical size binding to Margin.
            shape.relative_vertical_size = aw.drawing.RelativeVerticalSize.MARGIN
        # Setting the heigh to 30% of Margin height.
            shape.height_relative = 30
        # Checking and setting the relative vertical position.
        if shape.relative_vertical_position == aw.drawing.RelativeVerticalPosition.PARAGRAPH:
        # etting the position binding to TopMargin.
            shape.relative_vertical_position = aw.drawing.RelativeVerticalPosition.TOP_MARGIN
        # Setting relative Top to 30% of TopMargin position.
            shape.top_relative = 30
        # Checking and setting the relative horizontal position.
        if shape.relative_horizontal_position == aw.drawing.RelativeHorizontalPosition.DEFAULT:
        # Setting the position binding to RightMargin.
            shape.relative_horizontal_position = aw.drawing.RelativeHorizontalPosition.RIGHT_MARGIN
        # The position relative value can be negative.
            shape.left_relative = -260
        doc.save(file_name=ARTIFACTS_DIR + "Shape.RelativeSizeAndPosition.docx")
        #ExEnd

    def test_fill_base_color(self):
        #ExStart:FillBaseColor
        #ExFor:Fill.base_fore_color
        #ExFor:Stroke.base_fore_color
        #ExSummary:Shows how to get foreground color without modifiers.
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
        #ExEnd:FillBaseColor

    def test_fit_image_to_shape(self):
        #ExStart:FitImageToShape
        #ExFor:ImageData.fit_image_to_shape
        #ExSummary:Shows hot to fit the image data to Shape frame.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert an image shape and leave its orientation in its default state.
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.RECTANGLE, width=300, height=450)
        shape.image_data.set_image(file_name=IMAGE_DIR + "Barcode.png")
        shape.image_data.fit_image_to_shape()
        doc.save(file_name=ARTIFACTS_DIR + "Shape.FitImageToShape.docx")
        #ExEnd:FitImageToShape

    def test_stroke_fore_theme_colors(self):
        #ExStart:StrokeForeThemeColors
        #ExFor:Stroke.fore_theme_color
        #ExFor:Stroke.fore_tint_and_shade
        #ExSummary:Shows how to set fore theme color and tint and shade.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_shape(shape_type=aw.drawing.ShapeType.TEXT_BOX, width=100, height=40)
        stroke = shape.stroke
        stroke.fore_theme_color = aw.themes.ThemeColor.DARK1
        stroke.fore_tint_and_shade = 0.5
        doc.save(file_name=ARTIFACTS_DIR + "Shape.StrokeForeThemeColors.docx")
        #ExEnd:StrokeForeThemeColors
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.StrokeForeThemeColors.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.themes.ThemeColor.DARK1, shape.stroke.fore_theme_color)
        self.assertEqual(0.5, shape.stroke.fore_tint_and_shade)

    def test_stroke_back_theme_colors(self):
        #ExStart:StrokeBackThemeColors
        #ExFor:Stroke.back_theme_color
        #ExFor:Stroke.back_tint_and_shade
        #ExSummary:Shows how to set back theme color and tint and shade.
        doc = aw.Document(file_name=MY_DIR + "Stroke gradient outline.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        stroke = shape.stroke
        stroke.back_theme_color = aw.themes.ThemeColor.DARK2
        stroke.back_tint_and_shade = 0.2
        doc.save(file_name=ARTIFACTS_DIR + "Shape.StrokeBackThemeColors.docx")
        #ExEnd:StrokeBackThemeColors
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.StrokeBackThemeColors.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.themes.ThemeColor.DARK2, shape.stroke.back_theme_color)
        precision = 1E-06
        self.assertAlmostEqual(0.2, shape.stroke.back_tint_and_shade, delta=precision)

    def test_text_box_ole_control(self):
        #ExStart:TextBoxOleControl
        #ExFor:TextBoxControl
        #ExFor:TextBoxControl.text
        #ExSummary:Shows how to change text of the TextBox OLE control.
        doc = aw.Document(file_name=MY_DIR + "Textbox control.docm")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        text_box_control = shape.ole_format.ole_control.as_text_box_control()
        self.assertEqual("Aspose.Words test", text_box_control.text)
        text_box_control.text = "Updated text"
        self.assertEqual("Updated text", text_box_control.text)
        #ExEnd:TextBoxOleControl

    def test_glow(self):
        #ExStart:Glow
        #ExFor:ShapeBase.glow
        #ExFor:GlowFormat.color
        #ExFor:GlowFormat.radius
        #ExFor:GlowFormat.transparency
        #ExFor:GlowFormat.remove()
        #ExSummary:Shows how to interact with glow shape effect.
        doc = aw.Document(file_name=MY_DIR + "Various shapes.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        shape.glow.color = aspose.pydrawing.Color.salmon
        shape.glow.radius = 30
        shape.glow.transparency = 0.15
        doc.save(file_name=ARTIFACTS_DIR + "Shape.Glow.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.Glow.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aspose.pydrawing.Color.from_argb(217, 250, 128, 114).to_argb(), shape.glow.color.to_argb())
        self.assertEqual(30, shape.glow.radius)
        self.assertAlmostEqual(0.15, shape.glow.transparency, delta=0.01)
        shape.glow.remove()
        self.assertEqual(aspose.pydrawing.Color.black.to_argb(), shape.glow.color.to_argb())
        self.assertEqual(0, shape.glow.radius)
        self.assertEqual(0, shape.glow.transparency)
        #ExEnd:Glow

    def test_reflection(self):
        #ExStart:Reflection
        #ExFor:ShapeBase.reflection
        #ExFor:ReflectionFormat.size
        #ExFor:ReflectionFormat.blur
        #ExFor:ReflectionFormat.transparency
        #ExFor:ReflectionFormat.distance
        #ExFor:ReflectionFormat.remove()
        #ExSummary:Shows how to interact with reflection shape effect.
        doc = aw.Document(file_name=MY_DIR + "Various shapes.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        shape.reflection.transparency = 0.37
        shape.reflection.size = 0.48
        shape.reflection.blur = 17.5
        shape.reflection.distance = 9.2
        doc.save(file_name=ARTIFACTS_DIR + "Shape.Reflection.docx")
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Shape.Reflection.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertAlmostEqual(0.37, shape.reflection.transparency, delta=0.01)
        self.assertAlmostEqual(0.48, shape.reflection.size, delta=0.01)
        self.assertAlmostEqual(17.5, shape.reflection.blur, delta=0.01)
        self.assertAlmostEqual(9.2, shape.reflection.distance, delta=0.01)
        shape.reflection.remove()
        self.assertEqual(0, shape.reflection.transparency)
        self.assertEqual(0, shape.reflection.size)
        self.assertEqual(0, shape.reflection.blur)
        self.assertEqual(0, shape.reflection.distance)
        #ExEnd:Reflection
