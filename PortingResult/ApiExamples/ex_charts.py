# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.drawing
import aspose.words.drawing.charts
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExCharts(ApiExampleBase):
    def test_chart_title(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        chart_shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.BAR, width=400, height=300)
        chart = chart_shape.chart
        title = chart.title
        title.text = "My Chart"
        title.font.size = 15
        title.font.color = aspose.pydrawing.Color.blue
        title.show = True
        title.overlay = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartTitle.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.ChartTitle.docx")
        chart_shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aspose.words.drawing.ShapeType.NON_PRIMITIVE, chart_shape.shape_type)
        self.assertTrue(chart_shape.has_chart)
        title = chart_shape.chart.title
        self.assertEqual("My Chart", title.text)
        self.assertTrue(title.overlay)
        self.assertTrue(title.show)

    def test_data_label_number_format(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.LINE, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.title.text = "Monthly sales report"
        series = chart.series.add(series_name="Revenue", categories=["January", "February", "March"], values=[25.611, 21.439, 33.75])
        series.has_data_labels = True
        data_labels = series.data_labels
        data_labels.show_value = True
        data_labels.number_format.format_code = "\"US$\" #,##0.000\"M\""
        data_labels.font.size = 12
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataLabelNumberFormat.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.DataLabelNumberFormat.docx")
        series = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        self.assertTrue(series.has_data_labels)
        self.assertTrue(series.data_labels.show_value)
        self.assertEqual("\"US$\" #,##0.000\"M\"", series.data_labels.number_format.format_code)

    def test_axis_properties(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.series.add(series_name="Aspose Test Series", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[640, 320, 280, 120, 150])
        x_axis = chart.axis_x
        x_axis.category_type = aspose.words.drawing.charts.AxisCategoryType.CATEGORY
        x_axis.crosses = aspose.words.drawing.charts.AxisCrosses.MINIMUM
        x_axis.reverse_order = False
        x_axis.major_tick_mark = aspose.words.drawing.charts.AxisTickMark.INSIDE
        x_axis.minor_tick_mark = aspose.words.drawing.charts.AxisTickMark.CROSS
        x_axis.major_unit = 10
        x_axis.minor_unit = 15
        x_axis.tick_label_offset = 50
        x_axis.tick_label_position = aspose.words.drawing.charts.AxisTickLabelPosition.LOW
        x_axis.tick_label_spacing_is_auto = False
        x_axis.tick_mark_spacing = 1
        y_axis = chart.axis_y
        y_axis.category_type = aspose.words.drawing.charts.AxisCategoryType.AUTOMATIC
        y_axis.crosses = aspose.words.drawing.charts.AxisCrosses.MAXIMUM
        y_axis.reverse_order = True
        y_axis.major_tick_mark = aspose.words.drawing.charts.AxisTickMark.INSIDE
        y_axis.minor_tick_mark = aspose.words.drawing.charts.AxisTickMark.CROSS
        y_axis.major_unit = 100
        y_axis.minor_unit = 20
        y_axis.tick_label_position = aspose.words.drawing.charts.AxisTickLabelPosition.NEXT_TO_AXIS
        self.assertIsNone(chart.axis_z)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisProperties.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.AxisProperties.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual(aspose.words.drawing.charts.AxisCategoryType.CATEGORY, chart.axis_x.category_type)
        self.assertEqual(aspose.words.drawing.charts.AxisCrosses.MINIMUM, chart.axis_x.crosses)
        self.assertFalse(chart.axis_x.reverse_order)
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.INSIDE, chart.axis_x.major_tick_mark)
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.CROSS, chart.axis_x.minor_tick_mark)
        self.assertEqual(1, chart.axis_x.major_unit)
        self.assertEqual(0.5, chart.axis_x.minor_unit)
        self.assertEqual(50, chart.axis_x.tick_label_offset)
        self.assertEqual(aspose.words.drawing.charts.AxisTickLabelPosition.LOW, chart.axis_x.tick_label_position)
        self.assertFalse(chart.axis_x.tick_label_spacing_is_auto)
        self.assertEqual(1, chart.axis_x.tick_mark_spacing)
        self.assertEqual(aspose.words.drawing.charts.AxisCategoryType.CATEGORY, chart.axis_y.category_type)
        self.assertEqual(aspose.words.drawing.charts.AxisCrosses.MAXIMUM, chart.axis_y.crosses)
        self.assertTrue(chart.axis_y.reverse_order)
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.INSIDE, chart.axis_y.major_tick_mark)
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.CROSS, chart.axis_y.minor_tick_mark)
        self.assertEqual(100, chart.axis_y.major_unit)
        self.assertEqual(20, chart.axis_y.minor_unit)
        self.assertEqual(aspose.words.drawing.charts.AxisTickLabelPosition.NEXT_TO_AXIS, chart.axis_y.tick_label_position)

    def test_axis_collection(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=500, height=300)
        chart = shape.chart
        for axis in chart.axes:
            if axis.type == aspose.words.drawing.charts.ChartAxisType.VALUE:
                axis.has_major_gridlines = False
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisCollection.docx")

    def test_date_time_values(self):
        raise NotImplementedError("Unsupported ctor for type DateTime")

    def test_hide_chart_axis(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.LINE, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.series.add(series_name="AW Series 1", categories=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"], values=[1.2, 0.3, 2.1, 2.9, 4.2])
        chart.axis_x.hidden = True
        chart.axis_y.hidden = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.HideChartAxis.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.HideChartAxis.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertTrue(chart.axis_x.hidden)
        self.assertTrue(chart.axis_y.hidden)

    def test_set_number_format_to_chart_axis(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.series.add(series_name="Aspose Test Series", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[1900000, 850000, 2100000, 600000, 1500000])
        chart.axis_y.number_format.format_code = "#,##0"
        self.assertFalse(chart.axis_y.number_format.is_linked_to_source)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SetNumberFormatToChartAxis.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.SetNumberFormatToChartAxis.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual("#,##0", chart.axis_y.number_format.format_code)

    def test_display_charts_with_conversion(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_surface_3d_chart(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.SURFACE_3D, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.series.add(series_name="Aspose Test Series 1", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[1900000, 850000, 2100000, 600000, 1500000])
        chart.series.add(series_name="Aspose Test Series 2", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[900000, 50000, 1100000, 400000, 2500000])
        chart.series.add(series_name="Aspose Test Series 3", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[500000, 820000, 1500000, 400000, 100000])
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SurfaceChart.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SurfaceChart.pdf")

    def test_data_labels_bubble_chart(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        chart = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.BUBBLE, width=500, height=300).chart
        chart.series.clear()
        series = chart.series.add(series_name="Aspose Test Series", x_values=[2.9, 3.5, 1.1, 4, 4], y_values=[1.9, 8.5, 2.1, 6, 1.5], bubble_sizes=[9, 4.5, 2.5, 8, 5])
        series.has_data_labels = True
        data_labels = series.data_labels
        data_labels.show_bubble_size = True
        data_labels.show_category_name = True
        data_labels.show_series_name = True
        data_labels.separator = " & "
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataLabelsBubbleChart.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.DataLabelsBubbleChart.docx")
        data_labels = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.series[0].data_labels
        self.assertTrue(data_labels.show_bubble_size)
        self.assertTrue(data_labels.show_category_name)
        self.assertTrue(data_labels.show_series_name)
        self.assertEqual(" & ", data_labels.separator)

    def test_data_labels_pie_chart(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        chart = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.PIE, width=500, height=300).chart
        chart.series.clear()
        series = chart.series.add(series_name="Aspose Test Series", categories=["Word", "PDF", "Excel"], values=[2.7, 3.2, 0.8])
        series.has_data_labels = True
        data_labels = series.data_labels
        data_labels.show_leader_lines = True
        data_labels.show_legend_key = True
        data_labels.show_percentage = True
        data_labels.show_value = True
        data_labels.separator = "; "
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataLabelsPieChart.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.DataLabelsPieChart.docx")
        data_labels = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.series[0].data_labels
        self.assertTrue(data_labels.show_leader_lines)
        self.assertTrue(data_labels.show_legend_key)
        self.assertTrue(data_labels.show_percentage)
        self.assertTrue(data_labels.show_value)
        self.assertEqual("; ", data_labels.separator)

    def test_data_labels(self):
        raise NotImplementedError("Unsupported call of method named ApplyDataLabels")

    def test_chart_data_point(self):
        raise NotImplementedError("Unsupported call of method named ApplyDataPoints")

    def test_pie_chart_explosion(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.PIE, width=500, height=350)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Sales", chart.series[0].name)
        data_point = chart.series[0].data_points[0]
        data_point.explosion = 10
        data_point = chart.series[0].data_points[1]
        data_point.explosion = 40
        doc.save(file_name=ARTIFACTS_DIR + "Charts.PieChartExplosion.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.PieChartExplosion.docx")
        series = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        self.assertEqual(10, series.data_points[0].explosion)
        self.assertEqual(40, series.data_points[1].explosion)

    def test_bubble_3d(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.BUBBLE_3D, width=500, height=350)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Y-Values", chart.series[0].name)
        self.assertTrue(chart.series[0].bubble_3d)
        i = 0
        while i < 3:
            chart.series[0].has_data_labels = True
            chart.series[0].data_labels[i].show_bubble_size = True
            chart.series[0].data_labels[i].font.size = 12
            i += 1
        doc.save(file_name=ARTIFACTS_DIR + "Charts.Bubble3D.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.Bubble3D.docx")
        series = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        i = 0
        while i < 3:
            self.assertTrue(series.data_labels[i].show_bubble_size)
            i += 1

    def test_chart_series_collection(self):
        raise NotImplementedError("Unsupported call of method named AppendChart")

    def test_chart_series_collection_modify(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_axis_scaling(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        chart_shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.SCATTER, width=450, height=300)
        chart = chart_shape.chart
        chart.series.clear()
        chart.series.add(series_name="Series 1", x_values=[1, 2, 3, 4, 5], y_values=[1, 20, 400, 8000, 160000])
        chart.axis_y.scaling.type = aspose.words.drawing.charts.AxisScaleType.LOGARITHMIC
        chart.axis_y.scaling.log_base = 20
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisScaling.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.AxisScaling.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual(aspose.words.drawing.charts.AxisScaleType.LINEAR, chart.axis_x.scaling.type)
        self.assertEqual(aspose.words.drawing.charts.AxisScaleType.LOGARITHMIC, chart.axis_y.scaling.type)
        self.assertEqual(20, chart.axis_y.scaling.log_base)

    def test_axis_bound(self):
        raise NotImplementedError("Unsupported ctor for type DateTime")

    def test_chart_legend(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.LINE, width=450, height=300)
        chart = shape.chart
        self.assertEqual(3, chart.series.count)
        self.assertEqual("Series 1", chart.series[0].name)
        self.assertEqual("Series 2", chart.series[1].name)
        self.assertEqual("Series 3", chart.series[2].name)
        legend = chart.legend
        legend.position = aspose.words.drawing.charts.LegendPosition.TOP_RIGHT
        legend.overlay = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartLegend.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.ChartLegend.docx")
        legend = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.legend
        self.assertTrue(legend.overlay)
        self.assertEqual(aspose.words.drawing.charts.LegendPosition.TOP_RIGHT, legend.position)

    def test_axis_cross(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=450, height=250)
        chart = shape.chart
        self.assertEqual(3, chart.series.count)
        self.assertEqual("Series 1", chart.series[0].name)
        self.assertEqual("Series 2", chart.series[1].name)
        self.assertEqual("Series 3", chart.series[2].name)
        axis = chart.axis_x
        axis.crosses = aspose.words.drawing.charts.AxisCrosses.CUSTOM
        axis.crosses_at = 3
        axis.axis_between_categories = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisCross.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.AxisCross.docx")
        axis = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.axis_x
        self.assertTrue(axis.axis_between_categories)
        self.assertEqual(aspose.words.drawing.charts.AxisCrosses.CUSTOM, axis.crosses)
        self.assertEqual(3, axis.crosses_at)

    def test_axis_display_unit(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.SCATTER, width=450, height=250)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Y-Values", chart.series[0].name)
        axis = chart.axis_y
        axis.major_tick_mark = aspose.words.drawing.charts.AxisTickMark.CROSS
        axis.minor_tick_mark = aspose.words.drawing.charts.AxisTickMark.OUTSIDE
        axis.major_unit = 10
        axis.minor_unit = 1
        axis.scaling.minimum = aspose.words.drawing.charts.AxisBound(value=-10)
        axis.scaling.maximum = aspose.words.drawing.charts.AxisBound(value=20)
        axis = chart.axis_x
        axis.major_unit = 10
        axis.minor_unit = 2.5
        axis.major_tick_mark = aspose.words.drawing.charts.AxisTickMark.INSIDE
        axis.minor_tick_mark = aspose.words.drawing.charts.AxisTickMark.INSIDE
        axis.scaling.minimum = aspose.words.drawing.charts.AxisBound(value=-10)
        axis.scaling.maximum = aspose.words.drawing.charts.AxisBound(value=30)
        axis.tick_label_alignment = aspose.words.ParagraphAlignment.RIGHT
        self.assertEqual(1, axis.tick_label_spacing)
        axis.display_unit.unit = aspose.words.drawing.charts.AxisBuiltInUnit.MILLIONS
        axis.display_unit.custom_unit = 1000000
        self.assertEqual(aspose.words.drawing.charts.AxisBuiltInUnit.CUSTOM, axis.display_unit.unit)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisDisplayUnit.docx")
        doc = aspose.words.Document(file_name=ARTIFACTS_DIR + "Charts.AxisDisplayUnit.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(450, shape.width)
        self.assertEqual(250, shape.height)
        axis = shape.chart.axis_x
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.INSIDE, axis.major_tick_mark)
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.INSIDE, axis.minor_tick_mark)
        self.assertEqual(10, axis.major_unit)
        self.assertEqual(-10, axis.scaling.minimum.value)
        self.assertEqual(30, axis.scaling.maximum.value)
        self.assertEqual(1, axis.tick_label_spacing)
        self.assertEqual(aspose.words.ParagraphAlignment.RIGHT, axis.tick_label_alignment)
        self.assertEqual(aspose.words.drawing.charts.AxisBuiltInUnit.CUSTOM, axis.display_unit.unit)
        self.assertEqual(1000000, axis.display_unit.custom_unit)
        axis = shape.chart.axis_y
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.CROSS, axis.major_tick_mark)
        self.assertEqual(aspose.words.drawing.charts.AxisTickMark.OUTSIDE, axis.minor_tick_mark)
        self.assertEqual(10, axis.major_unit)
        self.assertEqual(1, axis.minor_unit)
        self.assertEqual(-10, axis.scaling.minimum.value)
        self.assertEqual(20, axis.scaling.maximum.value)

    def test_marker_formatting(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.SCATTER, width=432, height=252)
        chart = shape.chart
        chart.series.clear()
        series = chart.series.add(series_name="AW Series 1", x_values=[0.7, 1.8, 2.6, 3.9], y_values=[2.7, 3.2, 0.8, 1.7])
        series.marker.size = 40
        series.marker.symbol = aspose.words.drawing.charts.MarkerSymbol.SQUARE
        data_points = series.data_points
        data_points[0].marker.format.fill.preset_textured(aspose.words.drawing.PresetTexture.DENIM)
        data_points[0].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[0].marker.format.stroke.back_color = aspose.pydrawing.Color.red
        data_points[1].marker.format.fill.preset_textured(aspose.words.drawing.PresetTexture.WATER_DROPLETS)
        data_points[1].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[1].marker.format.stroke.visible = False
        data_points[2].marker.format.fill.preset_textured(aspose.words.drawing.PresetTexture.GREEN_MARBLE)
        data_points[2].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[3].marker.format.fill.preset_textured(aspose.words.drawing.PresetTexture.OAK)
        data_points[3].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[3].marker.format.stroke.transparency = 0.5
        doc.save(file_name=ARTIFACTS_DIR + "Charts.MarkerFormatting.docx")

    def test_series_color(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series_coll = chart.series
        series_coll.clear()
        categories = ["Category 1", "Category 2"]
        series1 = series_coll.add(series_name="Series 1", categories=categories, values=[1, 2])
        series2 = series_coll.add(series_name="Series 2", categories=categories, values=[3, 4])
        series3 = series_coll.add(series_name="Series 3", categories=categories, values=[5, 6])
        series1.format.fill.fore_color = aspose.pydrawing.Color.red
        series2.format.fill.fore_color = aspose.pydrawing.Color.yellow
        series3.format.fill.fore_color = aspose.pydrawing.Color.blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SeriesColor.docx")

    def test_data_points_formatting(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        chart.series.clear()
        series = chart.series.add(series_name="Series 1", categories=["Category 1", "Category 2", "Category 3", "Category 4"], values=[1, 2, 3, 4])
        data_points = series.data_points
        data_points[0].format.fill.preset_textured(aspose.words.drawing.PresetTexture.DENIM)
        data_points[1].format.fill.fore_color = aspose.pydrawing.Color.red
        data_points[2].format.fill.fore_color = aspose.pydrawing.Color.yellow
        data_points[3].format.fill.fore_color = aspose.pydrawing.Color.blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataPointsFormatting.docx")

    def test_legend_entries(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series = chart.series
        series.clear()
        categories = ["AW Category 1", "AW Category 2"]
        series1 = series.add(series_name="Series 1", categories=categories, values=[1, 2])
        series.add(series_name="Series 2", categories=categories, values=[3, 4])
        series.add(series_name="Series 3", categories=categories, values=[5, 6])
        series.add(series_name="Series 4", categories=categories, values=[0, 0])
        legend_entries = chart.legend.legend_entries
        legend_entries[3].is_hidden = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.LegendEntries.docx")

    def test_legend_font(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Reporting engine template - Chart series.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        chart_legend = chart.legend
        chart_legend.font.size = 14
        chart_legend.legend_entries[1].font.italic = True
        chart_legend.legend_entries[1].font.size = 12
        doc.save(file_name=ARTIFACTS_DIR + "Charts.LegendFont.docx")

    def test_remove_specific_chart_series(self):
        doc = aspose.words.Document(file_name=MY_DIR + "Reporting engine template - Chart series.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        i = chart.series.count - 1
        while i >= 0:
            if chart.series[i].series_type == aspose.words.drawing.charts.ChartSeriesType.COLUMN:
                chart.series.remove_at(i)
            i -= 1
        chart.series.add(series_name="Aspose Series", categories=["Category 1", "Category 2", "Category 3", "Category 4"], values=[5.6, 7.1, 2.9, 8.9])
        doc.save(file_name=ARTIFACTS_DIR + "Charts.RemoveSpecificChartSeries.docx")

    def test_populate_chart_with_data(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder()
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series1 = chart.series[0]
        series1.clear_values()
        series1.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(3), y_value=aspose.words.drawing.charts.ChartYValue.from_double(10))
        series1.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(5), y_value=aspose.words.drawing.charts.ChartYValue.from_double(5))
        series1.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(7), y_value=aspose.words.drawing.charts.ChartYValue.from_double(11))
        series1.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(9), y_value=aspose.words.drawing.charts.ChartYValue.from_double(17))
        series2 = chart.series[1]
        series2.clear_values()
        series2.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(2), y_value=aspose.words.drawing.charts.ChartYValue.from_double(4))
        series2.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(4), y_value=aspose.words.drawing.charts.ChartYValue.from_double(7))
        series2.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(6), y_value=aspose.words.drawing.charts.ChartYValue.from_double(14))
        series2.add(x_value=aspose.words.drawing.charts.ChartXValue.from_double(8), y_value=aspose.words.drawing.charts.ChartYValue.from_double(7))
        doc.save(file_name=ARTIFACTS_DIR + "Charts.PopulateChartWithData.docx")

    def test_get_chart_series_data(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder()
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series = chart.series[0]
        min_value = 1.7976931348623157E+308
        min_value_index = 0
        max_value = -1.7976931348623157E+308
        max_value_index = 0
        i = 0
        while i < series.y_values.count:
            series.data_points[i].clear_format()
            y_value = series.y_values[i].double_value
            if y_value < min_value:
                min_value = y_value
                min_value_index = i
            if y_value > max_value:
                max_value = y_value
                max_value_index = i
            i += 1
        series.data_points[min_value_index].format.fill.fore_color = aspose.pydrawing.Color.red
        series.data_points[max_value_index].format.fill.fore_color = aspose.pydrawing.Color.green
        doc.save(file_name=ARTIFACTS_DIR + "Charts.GetChartSeriesData.docx")

    def test_chart_data_values(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder()
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        department_1_series = chart.series[0]
        department_2_series = chart.series[1]
        department_1_series.remove(0)
        department_2_series.remove(0)
        new_x_category = aspose.words.drawing.charts.ChartXValue.from_string("Q1, 2023")
        department_1_series.add(x_value=new_x_category, y_value=aspose.words.drawing.charts.ChartYValue.from_double(10.3))
        department_2_series.add(x_value=new_x_category, y_value=aspose.words.drawing.charts.ChartYValue.from_double(5.7))
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartDataValues.docx")

    def test_format_data_lables(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        chart.series.clear()
        series = chart.series.add(series_name="AW Series 1", categories=["AW Category 1", "AW Category 2", "AW Category 3", "AW Category 4"], values=[100, 200, 300, 400])
        series.has_data_labels = True
        series.data_labels.show_value = True
        format = series.data_labels.format
        format.shape_type = aspose.words.drawing.charts.ChartShapeType.WEDGE_RECT_CALLOUT
        format.stroke.color = aspose.pydrawing.Color.dark_green
        format.fill.solid(aspose.pydrawing.Color.green)
        series.data_labels.font.color = aspose.pydrawing.Color.yellow
        label_format = series.data_labels[0].format
        label_format.stroke.color = aspose.pydrawing.Color.dark_blue
        label_format.fill.solid(aspose.pydrawing.Color.blue)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.FormatDataLables.docx")

    def test_chart_axis_title(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series_coll = chart.series
        series_coll.clear()
        series_coll.add(series_name="AW Series 1", categories=["AW Category 1", "AW Category 2"], values=[1, 2])
        chart_axis_x_title = chart.axis_x.title
        chart_axis_x_title.text = "Categories"
        chart_axis_x_title.show = True
        chart_axis_y_title = chart.axis_y.title
        chart_axis_y_title.text = "Values"
        chart_axis_y_title.show = True
        chart_axis_y_title.overlay = True
        chart_axis_y_title.font.size = 12
        chart_axis_y_title.font.color = aspose.pydrawing.Color.blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartAxisTitle.docx")

    def test_data_arrays_wrong_size(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_copy_data_point_format(self):
        doc = aspose.words.Document(file_name=MY_DIR + "DataPoint format.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        series = shape.chart.series[0]
        data_points = series.data_points
        self.assertTrue(data_points.has_default_format(0))
        self.assertFalse(data_points.has_default_format(1))
        data_points.copy_format(0, 1)
        self.assertTrue(data_points.has_default_format(0))
        self.assertTrue(data_points.has_default_format(1))
        series.copy_format_from(1)
        self.assertTrue(data_points.has_default_format(0))
        self.assertTrue(data_points.has_default_format(1))
        doc.save(file_name=ARTIFACTS_DIR + "Charts.CopyDataPointFormat.docx")

    def test_reset_data_point_fill(self):
        doc = aspose.words.Document(file_name=MY_DIR + "DataPoint format.docx")
        shape = doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()
        series = shape.chart.series[0]
        data_point = series.data_points[1]
        self.assertTrue(data_point.format.is_defined)
        data_point.format.set_default_fill()
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ResetDataPointFill.docx")

    def test_data_table(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aspose.words.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series = chart.series
        series.clear()
        x_values = [2020, 2021, 2022, 2023]
        series.add(series_name="Series1", x_values=x_values, y_values=[5, 11, 2, 7])
        series.add(series_name="Series2", x_values=x_values, y_values=[6, 5.5, 7, 7.8])
        series.add(series_name="Series3", x_values=x_values, y_values=[10, 8, 7, 9])
        data_table = chart.data_table
        data_table.show = True
        data_table.has_legend_keys = False
        data_table.has_horizontal_border = False
        data_table.has_vertical_border = False
        data_table.font.italic = True
        data_table.format.stroke.weight = 1
        data_table.format.stroke.dash_style = aspose.words.drawing.DashStyle.SHORT_DOT
        data_table.format.stroke.color = aspose.pydrawing.Color.dark_blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataTable.docx")
