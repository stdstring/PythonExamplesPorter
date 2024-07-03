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
import aspose.words.drawing.charts
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, MY_DIR


class ExCharts(ApiExampleBase):
    def test_chart_title(self):
        #ExStart:ChartTitle
        #ExFor:Chart
        #ExFor:Chart.title
        #ExFor:ChartTitle
        #ExFor:ChartTitle.overlay
        #ExFor:ChartTitle.show
        #ExFor:ChartTitle.text
        #ExFor:ChartTitle.font
        #ExSummary:Shows how to insert a chart and set a title.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Insert a chart shape with a document builder and get its chart.
        chart_shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.BAR, width=400, height=300)
        chart = chart_shape.chart
        # Use the "Title" property to give our chart a title, which appears at the top center of the chart area.
        title = chart.title
        title.text = "My Chart"
        title.font.size = 15
        title.font.color = aspose.pydrawing.Color.blue
        # Set the "Show" property to "true" to make the title visible.
        title.show = True
        # Set the "Overlay" property to "true" Give other chart elements more room by allowing them to overlap the title
        title.overlay = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartTitle.docx")
        #ExEnd:ChartTitle
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.ChartTitle.docx")
        chart_shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(aw.drawing.ShapeType.NON_PRIMITIVE, chart_shape.shape_type)
        self.assertTrue(chart_shape.has_chart)
        title = chart_shape.chart.title
        self.assertEqual("My Chart", title.text)
        self.assertTrue(title.overlay)
        self.assertTrue(title.show)

    def test_data_label_number_format(self):
        #ExStart
        #ExFor:ChartDataLabelCollection.number_format
        #ExFor:ChartDataLabelCollection.font
        #ExFor:ChartNumberFormat.format_code
        #ExSummary:Shows how to enable and configure data labels for a chart series.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        # Add a line chart, then clear its demo data series to start with a clean chart,
        # and then set a title.
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.LINE, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.title.text = "Monthly sales report"
        # Insert a custom chart series with months as categories for the X-axis,
        # and respective decimal amounts for the Y-axis.
        series = chart.series.add(series_name="Revenue", categories=["January", "February", "March"], values=[25.611, 21.439, 33.75])
        # Enable data labels, and then apply a custom number format for values displayed in the data labels.
        # This format will treat displayed decimal values as millions of US Dollars.
        series.has_data_labels = True
        data_labels = series.data_labels
        data_labels.show_value = True
        data_labels.number_format.format_code = "\"US$\" #,##0.000\"M\""
        data_labels.font.size = 12
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataLabelNumberFormat.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.DataLabelNumberFormat.docx")
        series = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        self.assertTrue(series.has_data_labels)
        self.assertTrue(series.data_labels.show_value)
        self.assertEqual("\"US$\" #,##0.000\"M\"", series.data_labels.number_format.format_code)

    def test_axis_properties(self):
        #ExStart
        #ExFor:ChartAxis
        #ExFor:ChartAxis.category_type
        #ExFor:ChartAxis.crosses
        #ExFor:ChartAxis.reverse_order
        #ExFor:ChartAxis.major_tick_mark
        #ExFor:ChartAxis.minor_tick_mark
        #ExFor:ChartAxis.major_unit
        #ExFor:ChartAxis.minor_unit
        #ExFor:AxisTickLabels.offset
        #ExFor:AxisTickLabels.position
        #ExFor:AxisTickLabels.is_auto_spacing
        #ExFor:ChartAxis.tick_mark_spacing
        #ExFor:AxisCategoryType
        #ExFor:AxisCrosses
        #ExFor:Chart.axis_x
        #ExFor:Chart.axis_y
        #ExFor:Chart.axis_z
        #ExSummary:Shows how to insert a chart and modify the appearance of its axes.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=500, height=300)
        chart = shape.chart
        # Clear the chart's demo data series to start with a clean chart.
        chart.series.clear()
        # Insert a chart series with categories for the X-axis and respective numeric values for the Y-axis.
        chart.series.add(series_name="Aspose Test Series", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[640, 320, 280, 120, 150])
        # Chart axes have various options that can change their appearance,
        # such as their direction, major/minor unit ticks, and tick marks.
        x_axis = chart.axis_x
        x_axis.category_type = aw.drawing.charts.AxisCategoryType.CATEGORY
        x_axis.crosses = aw.drawing.charts.AxisCrosses.MINIMUM
        x_axis.reverse_order = False
        x_axis.major_tick_mark = aw.drawing.charts.AxisTickMark.INSIDE
        x_axis.minor_tick_mark = aw.drawing.charts.AxisTickMark.CROSS
        x_axis.major_unit = 10
        x_axis.minor_unit = 15
        x_axis.tick_labels.offset = 50
        x_axis.tick_labels.position = aw.drawing.charts.AxisTickLabelPosition.LOW
        x_axis.tick_labels.is_auto_spacing = False
        x_axis.tick_mark_spacing = 1
        y_axis = chart.axis_y
        y_axis.category_type = aw.drawing.charts.AxisCategoryType.AUTOMATIC
        y_axis.crosses = aw.drawing.charts.AxisCrosses.MAXIMUM
        y_axis.reverse_order = True
        y_axis.major_tick_mark = aw.drawing.charts.AxisTickMark.INSIDE
        y_axis.minor_tick_mark = aw.drawing.charts.AxisTickMark.CROSS
        y_axis.major_unit = 100
        y_axis.minor_unit = 20
        y_axis.tick_labels.position = aw.drawing.charts.AxisTickLabelPosition.NEXT_TO_AXIS
        # Column charts do not have a Z-axis.
        self.assertIsNone(chart.axis_z)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisProperties.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.AxisProperties.docx")
        chart = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual(aw.drawing.charts.AxisCategoryType.CATEGORY, chart.axis_x.category_type)
        self.assertEqual(aw.drawing.charts.AxisCrosses.MINIMUM, chart.axis_x.crosses)
        self.assertFalse(chart.axis_x.reverse_order)
        self.assertEqual(aw.drawing.charts.AxisTickMark.INSIDE, chart.axis_x.major_tick_mark)
        self.assertEqual(aw.drawing.charts.AxisTickMark.CROSS, chart.axis_x.minor_tick_mark)
        self.assertEqual(1, chart.axis_x.major_unit)
        self.assertEqual(0.5, chart.axis_x.minor_unit)
        self.assertEqual(50, chart.axis_x.tick_labels.offset)
        self.assertEqual(aw.drawing.charts.AxisTickLabelPosition.LOW, chart.axis_x.tick_labels.position)
        self.assertFalse(chart.axis_x.tick_labels.is_auto_spacing)
        self.assertEqual(1, chart.axis_x.tick_mark_spacing)
        self.assertEqual(aw.drawing.charts.AxisCategoryType.CATEGORY, chart.axis_y.category_type)
        self.assertEqual(aw.drawing.charts.AxisCrosses.MAXIMUM, chart.axis_y.crosses)
        self.assertTrue(chart.axis_y.reverse_order)
        self.assertEqual(aw.drawing.charts.AxisTickMark.INSIDE, chart.axis_y.major_tick_mark)
        self.assertEqual(aw.drawing.charts.AxisTickMark.CROSS, chart.axis_y.minor_tick_mark)
        self.assertEqual(100, chart.axis_y.major_unit)
        self.assertEqual(20, chart.axis_y.minor_unit)
        self.assertEqual(aw.drawing.charts.AxisTickLabelPosition.NEXT_TO_AXIS, chart.axis_y.tick_labels.position)

    def test_axis_collection(self):
        #ExStart
        #ExFor:ChartAxisCollection
        #ExFor:Chart.axes
        #ExSummary:Shows how to work with axes collection.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=500, height=300)
        chart = shape.chart
        # Hide the major grid lines on the primary and secondary Y axes.
        for axis in chart.axes:
            if axis.type == aw.drawing.charts.ChartAxisType.VALUE:
                axis.has_major_gridlines = False
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisCollection.docx")
        #ExEnd

    def test_date_time_values(self):
        raise NotImplementedError("Unsupported ctor for type DateTime")

    def test_hide_chart_axis(self):
        #ExStart
        #ExFor:ChartAxis.hidden
        #ExSummary:Shows how to hide chart axes.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.LINE, width=500, height=300)
        chart = shape.chart
        # Clear the chart's demo data series to start with a clean chart.
        chart.series.clear()
        # Add a custom series with categories for the X-axis, and respective decimal values for the Y-axis.
        chart.series.add(series_name="AW Series 1", categories=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"], values=[1.2, 0.3, 2.1, 2.9, 4.2])
        # Hide the chart axes to simplify the appearance of the chart.
        chart.axis_x.hidden = True
        chart.axis_y.hidden = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.HideChartAxis.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.HideChartAxis.docx")
        chart = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertTrue(chart.axis_x.hidden)
        self.assertTrue(chart.axis_y.hidden)

    def test_set_number_format_to_chart_axis(self):
        #ExStart
        #ExFor:ChartAxis.number_format
        #ExFor:ChartNumberFormat
        #ExFor:ChartNumberFormat.format_code
        #ExFor:ChartNumberFormat.is_linked_to_source
        #ExSummary:Shows how to set formatting for chart values.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=500, height=300)
        chart = shape.chart
        # Clear the chart's demo data series to start with a clean chart.
        chart.series.clear()
        # Add a custom series to the chart with categories for the X-axis,
        # and large respective numeric values for the Y-axis.
        chart.series.add(series_name="Aspose Test Series", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[1900000, 850000, 2100000, 600000, 1500000])
        # Set the number format of the Y-axis tick labels to not group digits with commas.
        chart.axis_y.number_format.format_code = "#,##0"
        # This flag can override the above value and draw the number format from the source cell.
        self.assertFalse(chart.axis_y.number_format.is_linked_to_source)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SetNumberFormatToChartAxis.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.SetNumberFormatToChartAxis.docx")
        chart = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual("#,##0", chart.axis_y.number_format.format_code)

    def test_display_charts_with_conversion(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_surface_3d_chart(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.SURFACE_3D, width=500, height=300)
        chart = shape.chart
        chart.series.clear()
        chart.series.add(series_name="Aspose Test Series 1", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[1900000, 850000, 2100000, 600000, 1500000])
        chart.series.add(series_name="Aspose Test Series 2", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[900000, 50000, 1100000, 400000, 2500000])
        chart.series.add(series_name="Aspose Test Series 3", categories=["Word", "PDF", "Excel", "GoogleDocs", "Note"], values=[500000, 820000, 1500000, 400000, 100000])
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SurfaceChart.docx")
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SurfaceChart.pdf")

    def test_data_labels_bubble_chart(self):
        #ExStart
        #ExFor:ChartDataLabelCollection.separator
        #ExFor:ChartDataLabelCollection.show_bubble_size
        #ExFor:ChartDataLabelCollection.show_category_name
        #ExFor:ChartDataLabelCollection.show_series_name
        #ExSummary:Shows how to work with data labels of a bubble chart.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        chart = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.BUBBLE, width=500, height=300).chart
        # Clear the chart's demo data series to start with a clean chart.
        chart.series.clear()
        # Add a custom series with X/Y coordinates and diameter of each of the bubbles.
        series = chart.series.add(series_name="Aspose Test Series", x_values=[2.9, 3.5, 1.1, 4, 4], y_values=[1.9, 8.5, 2.1, 6, 1.5], bubble_sizes=[9, 4.5, 2.5, 8, 5])
        # Enable data labels, and then modify their appearance.
        series.has_data_labels = True
        data_labels = series.data_labels
        data_labels.show_bubble_size = True
        data_labels.show_category_name = True
        data_labels.show_series_name = True
        data_labels.separator = " & "
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataLabelsBubbleChart.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.DataLabelsBubbleChart.docx")
        data_labels = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.series[0].data_labels
        self.assertTrue(data_labels.show_bubble_size)
        self.assertTrue(data_labels.show_category_name)
        self.assertTrue(data_labels.show_series_name)
        self.assertEqual(" & ", data_labels.separator)

    def test_data_labels_pie_chart(self):
        #ExStart
        #ExFor:ChartDataLabelCollection.separator
        #ExFor:ChartDataLabelCollection.show_leader_lines
        #ExFor:ChartDataLabelCollection.show_legend_key
        #ExFor:ChartDataLabelCollection.show_percentage
        #ExFor:ChartDataLabelCollection.show_value
        #ExSummary:Shows how to work with data labels of a pie chart.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        chart = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.PIE, width=500, height=300).chart
        # Clear the chart's demo data series to start with a clean chart.
        chart.series.clear()
        # Insert a custom chart series with a category name for each of the sectors, and their frequency table.
        series = chart.series.add(series_name="Aspose Test Series", categories=["Word", "PDF", "Excel"], values=[2.7, 3.2, 0.8])
        # Enable data labels that will display both percentage and frequency of each sector, and modify their appearance.
        series.has_data_labels = True
        data_labels = series.data_labels
        data_labels.show_leader_lines = True
        data_labels.show_legend_key = True
        data_labels.show_percentage = True
        data_labels.show_value = True
        data_labels.separator = "; "
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataLabelsPieChart.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.DataLabelsPieChart.docx")
        data_labels = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.series[0].data_labels
        self.assertTrue(data_labels.show_leader_lines)
        self.assertTrue(data_labels.show_legend_key)
        self.assertTrue(data_labels.show_percentage)
        self.assertTrue(data_labels.show_value)
        self.assertEqual("; ", data_labels.separator)

    def test_data_labels(self):
        raise NotImplementedError("ignored method body")

    def test_chart_data_point(self):
        raise NotImplementedError("ignored method body")

    def test_pie_chart_explosion(self):
        #ExStart
        #ExFor:IChartDataPoint.explosion
        #ExSummary:Shows how to move the slices of a pie chart away from the center.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.PIE, width=500, height=350)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Sales", chart.series[0].name)
        # "Slices" of a pie chart may be moved away from the center by a distance via the respective data point's Explosion attribute.
        # Add a data point to the first portion of the pie chart and move it away from the center by 10 points.
        # Aspose.Words create data points automatically if them does not exist.
        data_point = chart.series[0].data_points[0]
        data_point.explosion = 10
        # Displace the second portion by a greater distance.
        data_point = chart.series[0].data_points[1]
        data_point.explosion = 40
        doc.save(file_name=ARTIFACTS_DIR + "Charts.PieChartExplosion.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.PieChartExplosion.docx")
        series = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        self.assertEqual(10, series.data_points[0].explosion)
        self.assertEqual(40, series.data_points[1].explosion)

    def test_bubble_3d(self):
        #ExStart
        #ExFor:ChartDataLabel.show_bubble_size
        #ExFor:ChartDataLabel.font
        #ExFor:IChartDataPoint.bubble_3d
        #ExSummary:Shows how to use 3D effects with bubble charts.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.BUBBLE_3D, width=500, height=350)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Y-Values", chart.series[0].name)
        self.assertTrue(chart.series[0].bubble_3d)
        # Apply a data label to each bubble that displays its diameter.
        i = 0
        while i < 3:
            chart.series[0].has_data_labels = True
            chart.series[0].data_labels[i].show_bubble_size = True
            chart.series[0].data_labels[i].font.size = 12
            i += 1
        doc.save(file_name=ARTIFACTS_DIR + "Charts.Bubble3D.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.Bubble3D.docx")
        series = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.series[0]
        i = 0
        while i < 3:
            self.assertTrue(series.data_labels[i].show_bubble_size)
            i += 1

    def test_chart_series_collection(self):
        raise NotImplementedError("ignored method body")

    def test_chart_series_collection_modify(self):
        raise NotImplementedError("Unsupported statement type: UsingStatement")

    def test_axis_scaling(self):
        #ExStart
        #ExFor:AxisScaleType
        #ExFor:AxisScaling
        #ExFor:AxisScaling.log_base
        #ExFor:AxisScaling.type
        #ExSummary:Shows how to apply logarithmic scaling to a chart axis.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        chart_shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.SCATTER, width=450, height=300)
        chart = chart_shape.chart
        # Clear the chart's demo data series to start with a clean chart.
        chart.series.clear()
        # Insert a series with X/Y coordinates for five points.
        chart.series.add(series_name="Series 1", x_values=[1, 2, 3, 4, 5], y_values=[1, 20, 400, 8000, 160000])
        # The scaling of the X-axis is linear by default,
        # displaying evenly incrementing values that cover our X-value range (0, 1, 2, 3...).
        # A linear axis is not ideal for our Y-values
        # since the points with the smaller Y-values will be harder to read.
        # A logarithmic scaling with a base of 20 (1, 20, 400, 8000...)
        # will spread the plotted points, allowing us to read their values on the chart more easily.
        chart.axis_y.scaling.type = aw.drawing.charts.AxisScaleType.LOGARITHMIC
        chart.axis_y.scaling.log_base = 20
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisScaling.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.AxisScaling.docx")
        chart = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart
        self.assertEqual(aw.drawing.charts.AxisScaleType.LINEAR, chart.axis_x.scaling.type)
        self.assertEqual(aw.drawing.charts.AxisScaleType.LOGARITHMIC, chart.axis_y.scaling.type)
        self.assertEqual(20, chart.axis_y.scaling.log_base)

    def test_axis_bound(self):
        raise NotImplementedError("Unsupported ctor for type DateTime")

    def test_chart_legend(self):
        #ExStart
        #ExFor:Chart.legend
        #ExFor:ChartLegend
        #ExFor:ChartLegend.overlay
        #ExFor:ChartLegend.position
        #ExFor:LegendPosition
        #ExSummary:Shows how to edit the appearance of a chart's legend.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.LINE, width=450, height=300)
        chart = shape.chart
        self.assertEqual(3, chart.series.count)
        self.assertEqual("Series 1", chart.series[0].name)
        self.assertEqual("Series 2", chart.series[1].name)
        self.assertEqual("Series 3", chart.series[2].name)
        # Move the chart's legend to the top right corner.
        legend = chart.legend
        legend.position = aw.drawing.charts.LegendPosition.TOP_RIGHT
        # Give other chart elements, such as the graph, more room by allowing them to overlap the legend.
        legend.overlay = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartLegend.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.ChartLegend.docx")
        legend = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.legend
        self.assertTrue(legend.overlay)
        self.assertEqual(aw.drawing.charts.LegendPosition.TOP_RIGHT, legend.position)

    def test_axis_cross(self):
        #ExStart
        #ExFor:ChartAxis.axis_between_categories
        #ExFor:ChartAxis.crosses_at
        #ExSummary:Shows how to get a graph axis to cross at a custom location.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=450, height=250)
        chart = shape.chart
        self.assertEqual(3, chart.series.count)
        self.assertEqual("Series 1", chart.series[0].name)
        self.assertEqual("Series 2", chart.series[1].name)
        self.assertEqual("Series 3", chart.series[2].name)
        # For column charts, the Y-axis crosses at zero by default,
        # which means that columns for all values below zero point down to represent negative values.
        # We can set a different value for the Y-axis crossing. In this case, we will set it to 3.
        axis = chart.axis_x
        axis.crosses = aw.drawing.charts.AxisCrosses.CUSTOM
        axis.crosses_at = 3
        axis.axis_between_categories = True
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisCross.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.AxisCross.docx")
        axis = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart.axis_x
        self.assertTrue(axis.axis_between_categories)
        self.assertEqual(aw.drawing.charts.AxisCrosses.CUSTOM, axis.crosses)
        self.assertEqual(3, axis.crosses_at)

    def test_axis_display_unit(self):
        #ExStart
        #ExFor:AxisBuiltInUnit
        #ExFor:ChartAxis.display_unit
        #ExFor:ChartAxis.major_unit_is_auto
        #ExFor:ChartAxis.major_unit_scale
        #ExFor:ChartAxis.minor_unit_is_auto
        #ExFor:ChartAxis.minor_unit_scale
        #ExFor:ChartAxis.tick_label_spacing
        #ExFor:ChartAxis.tick_label_alignment
        #ExFor:AxisDisplayUnit
        #ExFor:AxisDisplayUnit.custom_unit
        #ExFor:AxisDisplayUnit.unit
        #ExSummary:Shows how to manipulate the tick marks and displayed values of a chart axis.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.SCATTER, width=450, height=250)
        chart = shape.chart
        self.assertEqual(1, chart.series.count)
        self.assertEqual("Y-Values", chart.series[0].name)
        # Set the minor tick marks of the Y-axis to point away from the plot area,
        # and the major tick marks to cross the axis.
        axis = chart.axis_y
        axis.major_tick_mark = aw.drawing.charts.AxisTickMark.CROSS
        axis.minor_tick_mark = aw.drawing.charts.AxisTickMark.OUTSIDE
        # Set they Y-axis to show a major tick every 10 units, and a minor tick every 1 unit.
        axis.major_unit = 10
        axis.minor_unit = 1
        # Set the Y-axis bounds to -10 and 20.
        # This Y-axis will now display 4 major tick marks and 27 minor tick marks.
        axis.scaling.minimum = aw.drawing.charts.AxisBound(value=-10)
        axis.scaling.maximum = aw.drawing.charts.AxisBound(value=20)
        # For the X-axis, set the major tick marks at every 10 units,
        # every minor tick mark at 2.5 units.
        axis = chart.axis_x
        axis.major_unit = 10
        axis.minor_unit = 2.5
        # Configure both types of tick marks to appear inside the graph plot area.
        axis.major_tick_mark = aw.drawing.charts.AxisTickMark.INSIDE
        axis.minor_tick_mark = aw.drawing.charts.AxisTickMark.INSIDE
        # Set the X-axis bounds so that the X-axis spans 5 major tick marks and 12 minor tick marks.
        axis.scaling.minimum = aw.drawing.charts.AxisBound(value=-10)
        axis.scaling.maximum = aw.drawing.charts.AxisBound(value=30)
        axis.tick_labels.alignment = aw.ParagraphAlignment.RIGHT
        self.assertEqual(1, axis.tick_labels.spacing)
        # Set the tick labels to display their value in millions.
        axis.display_unit.unit = aw.drawing.charts.AxisBuiltInUnit.MILLIONS
        # We can set a more specific value by which tick labels will display their values.
        # This statement is equivalent to the one above.
        axis.display_unit.custom_unit = 1000000
        self.assertEqual(aw.drawing.charts.AxisBuiltInUnit.CUSTOM, axis.display_unit.unit) #ExSkip
        doc.save(file_name=ARTIFACTS_DIR + "Charts.AxisDisplayUnit.docx")
        #ExEnd
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.AxisDisplayUnit.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        self.assertEqual(450, shape.width)
        self.assertEqual(250, shape.height)
        axis = shape.chart.axis_x
        self.assertEqual(aw.drawing.charts.AxisTickMark.INSIDE, axis.major_tick_mark)
        self.assertEqual(aw.drawing.charts.AxisTickMark.INSIDE, axis.minor_tick_mark)
        self.assertEqual(10, axis.major_unit)
        self.assertEqual(-10, axis.scaling.minimum.value)
        self.assertEqual(30, axis.scaling.maximum.value)
        self.assertEqual(1, axis.tick_labels.spacing)
        self.assertEqual(aw.ParagraphAlignment.RIGHT, axis.tick_labels.alignment)
        self.assertEqual(aw.drawing.charts.AxisBuiltInUnit.CUSTOM, axis.display_unit.unit)
        self.assertEqual(1000000, axis.display_unit.custom_unit)
        axis = shape.chart.axis_y
        self.assertEqual(aw.drawing.charts.AxisTickMark.CROSS, axis.major_tick_mark)
        self.assertEqual(aw.drawing.charts.AxisTickMark.OUTSIDE, axis.minor_tick_mark)
        self.assertEqual(10, axis.major_unit)
        self.assertEqual(1, axis.minor_unit)
        self.assertEqual(-10, axis.scaling.minimum.value)
        self.assertEqual(20, axis.scaling.maximum.value)

    def test_marker_formatting(self):
        #ExStart
        #ExFor:ChartMarker.format
        #ExFor:ChartFormat.fill
        #ExFor:ChartFormat.stroke
        #ExFor:Stroke.fore_color
        #ExFor:Stroke.back_color
        #ExFor:Stroke.visible
        #ExFor:Stroke.transparency
        #ExFor:Fill.preset_textured(PresetTexture)
        #ExSummary:Show how to set marker formatting.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.SCATTER, width=432, height=252)
        chart = shape.chart
        # Delete default generated series.
        chart.series.clear()
        series = chart.series.add(series_name="AW Series 1", x_values=[0.7, 1.8, 2.6, 3.9], y_values=[2.7, 3.2, 0.8, 1.7])
        # Set marker formatting.
        series.marker.size = 40
        series.marker.symbol = aw.drawing.charts.MarkerSymbol.SQUARE
        data_points = series.data_points
        data_points[0].marker.format.fill.preset_textured(aw.drawing.PresetTexture.DENIM)
        data_points[0].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[0].marker.format.stroke.back_color = aspose.pydrawing.Color.red
        data_points[1].marker.format.fill.preset_textured(aw.drawing.PresetTexture.WATER_DROPLETS)
        data_points[1].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[1].marker.format.stroke.visible = False
        data_points[2].marker.format.fill.preset_textured(aw.drawing.PresetTexture.GREEN_MARBLE)
        data_points[2].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[3].marker.format.fill.preset_textured(aw.drawing.PresetTexture.OAK)
        data_points[3].marker.format.stroke.fore_color = aspose.pydrawing.Color.yellow
        data_points[3].marker.format.stroke.transparency = 0.5
        doc.save(file_name=ARTIFACTS_DIR + "Charts.MarkerFormatting.docx")
        #ExEnd

    def test_series_color(self):
        #ExStart
        #ExFor:ChartSeries.format
        #ExSummary:Sows how to set series color.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series_coll = chart.series
        # Delete default generated series.
        series_coll.clear()
        # Create category names array.
        categories = ["Category 1", "Category 2"]
        # Adding new series. Value and category arrays must be the same size.
        series1 = series_coll.add(series_name="Series 1", categories=categories, values=[1, 2])
        series2 = series_coll.add(series_name="Series 2", categories=categories, values=[3, 4])
        series3 = series_coll.add(series_name="Series 3", categories=categories, values=[5, 6])
        # Set series color.
        series1.format.fill.fore_color = aspose.pydrawing.Color.red
        series2.format.fill.fore_color = aspose.pydrawing.Color.yellow
        series3.format.fill.fore_color = aspose.pydrawing.Color.blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.SeriesColor.docx")
        #ExEnd

    def test_data_points_formatting(self):
        #ExStart
        #ExFor:ChartDataPoint.format
        #ExSummary:Shows how to set individual formatting for categories of a column chart.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        # Delete default generated series.
        chart.series.clear()
        # Adding new series.
        series = chart.series.add(series_name="Series 1", categories=["Category 1", "Category 2", "Category 3", "Category 4"], values=[1, 2, 3, 4])
        # Set column formatting.
        data_points = series.data_points
        data_points[0].format.fill.preset_textured(aw.drawing.PresetTexture.DENIM)
        data_points[1].format.fill.fore_color = aspose.pydrawing.Color.red
        data_points[2].format.fill.fore_color = aspose.pydrawing.Color.yellow
        data_points[3].format.fill.fore_color = aspose.pydrawing.Color.blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataPointsFormatting.docx")
        #ExEnd

    def test_legend_entries(self):
        #ExStart
        #ExFor:ChartLegendEntryCollection
        #ExFor:ChartLegend.legend_entries
        #ExFor:ChartLegendEntry.is_hidden
        #ExSummary:Shows how to work with a legend entry for chart series.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
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
        #ExEnd

    def test_legend_font(self):
        #ExStart:LegendFont
        #ExFor:ChartLegendEntry.font
        #ExFor:ChartLegend.font
        #ExSummary:Shows how to work with a legend font.
        doc = aw.Document(file_name=MY_DIR + "Reporting engine template - Chart series.docx")
        chart = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart
        chart_legend = chart.legend
        # Set default font size all legend entries.
        chart_legend.font.size = 14
        # Change font for specific legend entry.
        chart_legend.legend_entries[1].font.italic = True
        chart_legend.legend_entries[1].font.size = 12
        doc.save(file_name=ARTIFACTS_DIR + "Charts.LegendFont.docx")
        #ExEnd:LegendFont

    def test_remove_specific_chart_series(self):
        #ExStart
        #ExFor:ChartSeries.series_type
        #ExFor:ChartSeriesType
        #ExSummary:Shows how to remove specific chart serie.
        doc = aw.Document(file_name=MY_DIR + "Reporting engine template - Chart series.docx")
        chart = (doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()).chart
        # Remove all series of the Column type.
        i = chart.series.count - 1
        while i >= 0:
            if chart.series[i].series_type == aw.drawing.charts.ChartSeriesType.COLUMN:
                chart.series.remove_at(i)
            i -= 1
        chart.series.add(series_name="Aspose Series", categories=["Category 1", "Category 2", "Category 3", "Category 4"], values=[5.6, 7.1, 2.9, 8.9])
        doc.save(file_name=ARTIFACTS_DIR + "Charts.RemoveSpecificChartSeries.docx")
        #ExEnd

    def test_populate_chart_with_data(self):
        #ExStart
        #ExFor:ChartXValue.from_double(float)
        #ExFor:ChartYValue.from_double(float)
        #ExFor:ChartSeries.add(ChartXValue,ChartYValue)
        #ExSummary:Shows how to populate chart series with data.
        doc = aw.Document()
        builder = aw.DocumentBuilder()
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series1 = chart.series[0]
        # Clear X and Y values of the first series.
        series1.clear_values()
        # Populate the series with data.
        series1.add(x_value=aw.drawing.charts.ChartXValue.from_double(3), y_value=aw.drawing.charts.ChartYValue.from_double(10))
        series1.add(x_value=aw.drawing.charts.ChartXValue.from_double(5), y_value=aw.drawing.charts.ChartYValue.from_double(5))
        series1.add(x_value=aw.drawing.charts.ChartXValue.from_double(7), y_value=aw.drawing.charts.ChartYValue.from_double(11))
        series1.add(x_value=aw.drawing.charts.ChartXValue.from_double(9), y_value=aw.drawing.charts.ChartYValue.from_double(17))
        series2 = chart.series[1]
        # Clear X and Y values of the second series.
        series2.clear_values()
        # Populate the series with data.
        series2.add(x_value=aw.drawing.charts.ChartXValue.from_double(2), y_value=aw.drawing.charts.ChartYValue.from_double(4))
        series2.add(x_value=aw.drawing.charts.ChartXValue.from_double(4), y_value=aw.drawing.charts.ChartYValue.from_double(7))
        series2.add(x_value=aw.drawing.charts.ChartXValue.from_double(6), y_value=aw.drawing.charts.ChartYValue.from_double(14))
        series2.add(x_value=aw.drawing.charts.ChartXValue.from_double(8), y_value=aw.drawing.charts.ChartYValue.from_double(7))
        doc.save(file_name=ARTIFACTS_DIR + "Charts.PopulateChartWithData.docx")
        #ExEnd

    def test_get_chart_series_data(self):
        #ExStart
        #ExFor:ChartXValueCollection
        #ExFor:ChartYValueCollection
        #ExSummary:Shows how to get chart series data.
        doc = aw.Document()
        builder = aw.DocumentBuilder()
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series = chart.series[0]
        min_value = 1.7976931348623157E+308
        min_value_index = 0
        max_value = -1.7976931348623157E+308
        max_value_index = 0
        i = 0
        while i < series.y_values.count:
        # Clear individual format of all data points.
        # Data points and data values are one-to-one in column charts.
            series.data_points[i].clear_format()
        # Get Y value.
            y_value = series.y_values[i].double_value
            if y_value < min_value:
                min_value = y_value
                min_value_index = i
            if y_value > max_value:
                max_value = y_value
                max_value_index = i
            i += 1
        # Change colors of the max and min values.
        series.data_points[min_value_index].format.fill.fore_color = aspose.pydrawing.Color.red
        series.data_points[max_value_index].format.fill.fore_color = aspose.pydrawing.Color.green
        doc.save(file_name=ARTIFACTS_DIR + "Charts.GetChartSeriesData.docx")
        #ExEnd

    def test_chart_data_values(self):
        #ExStart
        #ExFor:ChartXValue.from_string(str)
        #ExFor:ChartSeries.remove(int)
        #ExFor:ChartSeries.add(ChartXValue,ChartYValue)
        #ExSummary:Shows how to add/remove chart data values.
        doc = aw.Document()
        builder = aw.DocumentBuilder()
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        department_1_series = chart.series[0]
        department_2_series = chart.series[1]
        # Remove the first value in the both series.
        department_1_series.remove(0)
        department_2_series.remove(0)
        # Add new values to the both series.
        new_x_category = aw.drawing.charts.ChartXValue.from_string("Q1, 2023")
        department_1_series.add(x_value=new_x_category, y_value=aw.drawing.charts.ChartYValue.from_double(10.3))
        department_2_series.add(x_value=new_x_category, y_value=aw.drawing.charts.ChartYValue.from_double(5.7))
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartDataValues.docx")
        #ExEnd

    def test_format_data_lables(self):
        #ExStart
        #ExFor:ChartDataLabelCollection.format
        #ExFor:ChartFormat.shape_type
        #ExFor:ChartShapeType
        #ExSummary:Shows how to set fill, stroke and callout formatting for chart data labels.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        # Delete default generated series.
        chart.series.clear()
        # Add new series.
        series = chart.series.add(series_name="AW Series 1", categories=["AW Category 1", "AW Category 2", "AW Category 3", "AW Category 4"], values=[100, 200, 300, 400])
        # Show data labels.
        series.has_data_labels = True
        series.data_labels.show_value = True
        # Format data labels as callouts.
        format = series.data_labels.format
        format.shape_type = aw.drawing.charts.ChartShapeType.WEDGE_RECT_CALLOUT
        format.stroke.color = aspose.pydrawing.Color.dark_green
        format.fill.solid(aspose.pydrawing.Color.green)
        series.data_labels.font.color = aspose.pydrawing.Color.yellow
        # Change fill and stroke of an individual data label.
        label_format = series.data_labels[0].format
        label_format.stroke.color = aspose.pydrawing.Color.dark_blue
        label_format.fill.solid(aspose.pydrawing.Color.blue)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.FormatDataLables.docx")
        #ExEnd

    def test_chart_axis_title(self):
        #ExStart:ChartAxisTitle
        #ExFor:ChartAxisTitle
        #ExFor:ChartAxisTitle.text
        #ExFor:ChartAxisTitle.show
        #ExFor:ChartAxisTitle.overlay
        #ExFor:ChartAxisTitle.font
        #ExSummary:Shows how to set chart axis title.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        series_coll = chart.series
        # Delete default generated series.
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
        #ExEnd:ChartAxisTitle

    def test_data_arrays_wrong_size(self):
        raise NotImplementedError("Unsupported NUnit.Framework.TestCaseAttribute attributes")

    def test_copy_data_point_format(self):
        #ExStart:CopyDataPointFormat
        #ExFor:ChartSeries.copy_format_from(int)
        #ExFor:ChartDataPointCollection.has_default_format(int)
        #ExFor:ChartDataPointCollection.copy_format(int,int)
        #ExSummary:Shows how to copy data point format.
        doc = aw.Document(file_name=MY_DIR + "DataPoint format.docx")
        # Get the chart and series to update format.
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        series = shape.chart.series[0]
        data_points = series.data_points
        self.assertTrue(data_points.has_default_format(0))
        self.assertFalse(data_points.has_default_format(1))
        # Copy format of the data point with index 1 to the data point with index 2
        # so that the data point 2 looks the same as the data point 1.
        data_points.copy_format(0, 1)
        self.assertTrue(data_points.has_default_format(0))
        self.assertTrue(data_points.has_default_format(1))
        # Copy format of the data point with index 0 to the series defaults so that all data points
        # in the series that have the default format look the same as the data point 0.
        series.copy_format_from(1)
        self.assertTrue(data_points.has_default_format(0))
        self.assertTrue(data_points.has_default_format(1))
        doc.save(file_name=ARTIFACTS_DIR + "Charts.CopyDataPointFormat.docx")
        #ExEnd:CopyDataPointFormat

    def test_reset_data_point_fill(self):
        #ExStart:ResetDataPointFill
        #ExFor:ChartFormat.is_defined
        #ExFor:ChartFormat.set_default_fill
        #ExSummary:Shows how to reset the fill to the default value defined in the series.
        doc = aw.Document(file_name=MY_DIR + "DataPoint format.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        series = shape.chart.series[0]
        data_point = series.data_points[1]
        self.assertTrue(data_point.format.is_defined)
        data_point.format.set_default_fill()
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ResetDataPointFill.docx")
        #ExEnd:ResetDataPointFill

    def test_data_table(self):
        #ExStart:DataTable
        #ExFor:ChartDataTable
        #ExFor:ChartDataTable.show
        #ExSummary:Shows how to show data table with chart series data.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
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
        data_table.format.stroke.dash_style = aw.drawing.DashStyle.SHORT_DOT
        data_table.format.stroke.color = aspose.pydrawing.Color.dark_blue
        doc.save(file_name=ARTIFACTS_DIR + "Charts.DataTable.docx")
        #ExEnd:DataTable

    def test_chart_format(self):
        #ExStart:ChartFormat
        #ExFor:Chart.format
        #ExFor:ChartTitle.format
        #ExFor:ChartAxisTitle.format
        #ExFor:ChartLegend.format
        #ExSummary:Shows how to use chart formating.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_chart(chart_type=aw.drawing.charts.ChartType.COLUMN, width=432, height=252)
        chart = shape.chart
        # Delete series generated by default.
        series = chart.series
        series.clear()
        categories = ["Category 1", "Category 2"]
        series.add(series_name="Series 1", categories=categories, values=[1, 2])
        series.add(series_name="Series 2", categories=categories, values=[3, 4])
        # Format chart background.
        chart.format.fill.solid(aspose.pydrawing.Color.dark_slate_gray)
        # Hide axis tick labels.
        chart.axis_x.tick_labels.position = aw.drawing.charts.AxisTickLabelPosition.NONE
        chart.axis_y.tick_labels.position = aw.drawing.charts.AxisTickLabelPosition.NONE
        # Format chart title.
        chart.title.format.fill.solid(aspose.pydrawing.Color.light_goldenrod_yellow)
        # Format axis title.
        chart.axis_x.title.show = True
        chart.axis_x.title.format.fill.solid(aspose.pydrawing.Color.light_goldenrod_yellow)
        # Format legend.
        chart.legend.format.fill.solid(aspose.pydrawing.Color.light_goldenrod_yellow)
        doc.save(file_name=ARTIFACTS_DIR + "Charts.ChartFormat.docx")
        #ExEnd:ChartFormat
        doc = aw.Document(file_name=ARTIFACTS_DIR + "Charts.ChartFormat.docx")
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()
        chart = shape.chart
        self.assertEqual(aspose.pydrawing.Color.dark_slate_gray.to_argb(), chart.format.fill.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.light_goldenrod_yellow.to_argb(), chart.title.format.fill.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.light_goldenrod_yellow.to_argb(), chart.axis_x.title.format.fill.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.light_goldenrod_yellow.to_argb(), chart.legend.format.fill.color.to_argb())
