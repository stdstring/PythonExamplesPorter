# -*- coding: utf-8 -*-
import aspose.words
import aspose.words.drawing
import aspose.words.drawing.charts
import math
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExCharts(ApiExampleBase):
    def test_chart_title(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_data_label_number_format(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_data_arrays_wrong_size(self):
        raise NotImplementedError("Unsupported expression: ParenthesizedLambdaExpression")

    def test_empty_values_in_chart_data(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.LINE, width = 500, height = 300)
        chart = shape.chart
        series_coll = chart.series
        series_coll.clear()
        categories = ["Cat1", None, "Cat3", "Cat4", "Cat5", None]
        series_coll.add(series_name = "AW Series 1", categories = categories, values = [1, 2, math.nan, 4, 5, 6])
        series_coll.add(series_name = "AW Series 2", categories = categories, values = [2, 3, math.nan, 5, 6, 7])
        series_coll.add(series_name = "AW Series 3", categories = categories, values = [math.nan, 4, 5, math.nan, 7, 8])
        series_coll.add(series_name = "AW Series 4", categories = categories, values = [math.nan, math.nan, math.nan, math.nan, math.nan, 9])
        doc.save(file_name = ARTIFACTS_DIR + "Charts.EmptyValuesInChartData.docx")

    def test_axis_properties(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_axis_collection(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.COLUMN, width = 500, height = 300)
        chart = shape.chart
        # for each loop begin
        for axis in chart.axes:
            # if begin
            if axis.type == aspose.words.drawing.charts.ChartAxisType.VALUE:
                axis.has_major_gridlines = False
            # if end
        # for loop end
        doc.save(file_name = ARTIFACTS_DIR + "Charts.AxisCollection.docx")

    def test_date_time_values(self):
        raise NotImplementedError("Unsupported type: DateTime")

    def test_hide_chart_axis(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_set_number_format_to_chart_axis(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_surface_3d_chart(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.SURFACE_3D, width = 500, height = 300)
        chart = shape.chart
        chart.series.clear()
        chart.series.add(series_name = "Aspose Test Series 1", categories = ["Word", "PDF", "Excel", "GoogleDocs", "Note"], values = [1900000, 850000, 2100000, 600000, 1500000])
        chart.series.add(series_name = "Aspose Test Series 2", categories = ["Word", "PDF", "Excel", "GoogleDocs", "Note"], values = [900000, 50000, 1100000, 400000, 2500000])
        chart.series.add(series_name = "Aspose Test Series 3", categories = ["Word", "PDF", "Excel", "GoogleDocs", "Note"], values = [500000, 820000, 1500000, 400000, 100000])
        doc.save(file_name = ARTIFACTS_DIR + "Charts.SurfaceChart.docx")
        doc.save(file_name = ARTIFACTS_DIR + "Charts.SurfaceChart.pdf")

    def test_data_labels_bubble_chart(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_data_labels_pie_chart(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_data_labels(self):
        raise NotImplementedError("Unsupported call of method named ApplyDataLabels")

    def test_chart_data_point(self):
        raise NotImplementedError("Unsupported call of method named ApplyDataPoints")

    def test_pie_chart_explosion(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.PIE, width = 500, height = 350)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Sales", chart.series[0].name)
        data_point = chart.series[0].data_points[0]
        data_point.explosion = 10
        data_point = chart.series[0].data_points[1]
        data_point.explosion = 40
        doc.save(file_name = ARTIFACTS_DIR + "Charts.PieChartExplosion.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Charts.PieChartExplosion.docx")
        series = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        self.assertEqual(10, series.data_points[0].explosion)
        self.assertEqual(40, series.data_points[1].explosion)

    def test_bubble_3d(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_chart_series_collection(self):
        raise NotImplementedError("Unsupported call of method named AppendChart")

    def test_chart_series_collection_modify(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_axis_scaling(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        chart_shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.SCATTER, width = 450, height = 300)
        chart = chart_shape.chart
        chart.series.clear()
        chart.series.add(series_name = "Series 1", x_values = [1, 2, 3, 4, 5], y_values = [1, 20, 400, 8000, 160000])
        chart.axis_y.scaling.type = aspose.words.drawing.charts.AxisScaleType.LOGARITHMIC
        chart.axis_y.scaling.log_base = 20
        doc.save(file_name = ARTIFACTS_DIR + "Charts.AxisScaling.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Charts.AxisScaling.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual(aspose.words.drawing.charts.AxisScaleType.LINEAR, chart.axis_x.scaling.type)
        self.assertEqual(aspose.words.drawing.charts.AxisScaleType.LOGARITHMIC, chart.axis_y.scaling.type)
        self.assertEqual(20, chart.axis_y.scaling.log_base)

    def test_axis_bound(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_chart_legend(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_axis_cross(self):
        raise NotImplementedError("Unsupported target type NUnit.Framework.Assert")

    def test_axis_display_unit(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.SCATTER, width = 450, height = 250)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Y-Values", chart.series[0].name)
        axis = chart.axis_y
        axis.major_tick_mark = aspose.words.drawing.charts.AxisTickMark.CROSS
        axis.minor_tick_mark = aspose.words.drawing.charts.AxisTickMark.OUTSIDE
        axis.major_unit = 10
        axis.minor_unit = 1
        axis.scaling.minimum = aspose.words.drawing.charts.AxisBound(value = -10)
        axis.scaling.maximum = aspose.words.drawing.charts.AxisBound(value = 20)
        axis = chart.axis_x
        axis.major_unit = 10
        axis.minor_unit = 2.5
        axis.major_tick_mark = aspose.words.drawing.charts.AxisTickMark.INSIDE
        axis.minor_tick_mark = aspose.words.drawing.charts.AxisTickMark.INSIDE
        axis.scaling.minimum = aspose.words.drawing.charts.AxisBound(value = -10)
        axis.scaling.maximum = aspose.words.drawing.charts.AxisBound(value = 30)
        axis.tick_label_alignment = aspose.words.ParagraphAlignment.RIGHT
        self.assertEqual(1, axis.tick_label_spacing)
        axis.display_unit.unit = aspose.words.drawing.charts.AxisBuiltInUnit.MILLIONS
        axis.display_unit.custom_unit = 1000000
        self.assertEqual(aspose.words.drawing.charts.AxisBuiltInUnit.CUSTOM, axis.display_unit.unit)
        doc.save(file_name = ARTIFACTS_DIR + "Charts.AxisDisplayUnit.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Charts.AxisDisplayUnit.docx")
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
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_series_color(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_data_points_formatting(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_legend_entries(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.COLUMN, width = 432, height = 252)
        chart = shape.chart
        series = chart.series
        series.clear()
        categories = ["AW Category 1", "AW Category 2"]
        series1 = series.add(series_name = "Series 1", categories = categories, values = [1, 2])
        series.add(series_name = "Series 2", categories = categories, values = [3, 4])
        series.add(series_name = "Series 3", categories = categories, values = [5, 6])
        series.add(series_name = "Series 4", categories = categories, values = [0, 0])
        legend_entries = chart.legend.legend_entries
        legend_entries[3].is_hidden = True
        # for each loop begin
        for legend_entry in legend_entries:
            legend_entry.font.size = 12
        # for loop end
        series1.legend_entry.font.italic = True
        doc.save(file_name = ARTIFACTS_DIR + "Charts.LegendEntries.docx")

    def test_remove_specific_chart_series(self):
        doc = aspose.words.Document(file_name = MY_DIR + "Reporting engine template - Chart series.docx")
        chart = (doc.get_child(aspose.words.NodeType.SHAPE, 0, True).as_shape()).chart
        # for loop begin
        i = chart.series.count - 1
        while i >= 0:
            # if begin
            if chart.series[i].series_type == aspose.words.drawing.charts.ChartSeriesType.COLUMN:
                chart.series.remove_at(i)
            # if end
            i -= 1
        # for loop end
        chart.series.add(series_name = "Aspose Series", categories = ["Category 1", "Category 2", "Category 3", "Category 4"], values = [5.6, 7.1, 2.9, 8.9])
        doc.save(file_name = ARTIFACTS_DIR + "Charts.RemoveSpecificChartSeries.docx")

    def test_populate_chart_with_data(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder()
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.COLUMN, width = 432, height = 252)
        chart = shape.chart
        series1 = chart.series[0]
        series1.clear_values()
        series1.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(3), y_value = aspose.words.drawing.charts.ChartYValue.from_double(10))
        series1.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(5), y_value = aspose.words.drawing.charts.ChartYValue.from_double(5))
        series1.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(7), y_value = aspose.words.drawing.charts.ChartYValue.from_double(11))
        series1.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(9), y_value = aspose.words.drawing.charts.ChartYValue.from_double(17))
        series2 = chart.series[1]
        series2.clear_values()
        series2.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(2), y_value = aspose.words.drawing.charts.ChartYValue.from_double(4))
        series2.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(4), y_value = aspose.words.drawing.charts.ChartYValue.from_double(7))
        series2.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(6), y_value = aspose.words.drawing.charts.ChartYValue.from_double(14))
        series2.add(x_value = aspose.words.drawing.charts.ChartXValue.from_double(8), y_value = aspose.words.drawing.charts.ChartYValue.from_double(7))
        doc.save(file_name = ARTIFACTS_DIR + "Charts.PopulateChartWithData.docx")

    def test_get_chart_series_data(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")

    def test_chart_data_values(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder()
        shape = builder.insert_chart(chart_type = aspose.words.drawing.charts.ChartType.COLUMN, width = 432, height = 252)
        chart = shape.chart
        department_1_series = chart.series[0]
        department_2_series = chart.series[1]
        department_1_series.remove(0)
        department_2_series.remove(0)
        new_x_category = aspose.words.drawing.charts.ChartXValue.from_string("Q1, 2023")
        department_1_series.add(x_value = new_x_category, y_value = aspose.words.drawing.charts.ChartYValue.from_double(10.3))
        department_2_series.add(x_value = new_x_category, y_value = aspose.words.drawing.charts.ChartYValue.from_double(5.7))
        doc.save(file_name = ARTIFACTS_DIR + "Charts.ChartDataValues.docx")

    def test_format_data_lables(self):
        raise NotImplementedError("Unsupported target type System.Drawing.Color")
