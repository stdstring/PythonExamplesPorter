# -*- coding: utf-8 -*-
import aspose.pydrawing
import aspose.words
import aspose.words.fonts
import aspose.words.themes
import unittest
from api_example_base import ApiExampleBase, ARTIFACTS_DIR, FONTS_DIR, MY_DIR


class ExFont(ApiExampleBase):
    def test_create_formatted_run(self):
        doc = aspose.words.Document()
        run = aspose.words.Run(doc = doc, text = "Hello world!")
        font = run.font
        font.name = "Courier New"
        font.size = 36
        font.highlight_color = aspose.pydrawing.Color.yellow
        doc.first_section.body.first_paragraph.append_child(run)
        doc.save(file_name = ARTIFACTS_DIR + "Font.CreateFormattedRun.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.CreateFormattedRun.docx")
        run = doc.first_section.body.first_paragraph.runs[0]
        self.assertEqual("Hello world!", run.get_text().strip())
        self.assertEqual("Courier New", run.font.name)
        self.assertEqual(36, run.font.size)
        self.assertEqual(aspose.pydrawing.Color.yellow.to_argb(), run.font.highlight_color.to_argb())

    def test_caps(self):
        doc = aspose.words.Document()
        para = doc.get_child(aspose.words.NodeType.PARAGRAPH, 0, True).as_paragraph()
        run = aspose.words.Run(doc = doc, text = "all capitals")
        run.font.all_caps = True
        para.append_child(run)
        para = para.parent_node.append_child(aspose.words.Paragraph(doc)).as_paragraph()
        run = aspose.words.Run(doc = doc, text = "Small Capitals")
        run.font.small_caps = True
        para.append_child(run)
        doc.save(file_name = ARTIFACTS_DIR + "Font.Caps.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Caps.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("all capitals", run.get_text().strip())
        self.assertTrue(run.font.all_caps)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("Small Capitals", run.get_text().strip())
        self.assertTrue(run.font.small_caps)

    def test_get_document_fonts(self):
        raise NotImplementedError("Unsupported expression: InterpolatedStringExpression")

    def test_default_values_embedded_fonts_parameters(self):
        doc = aspose.words.Document()
        self.assertFalse(doc.font_infos.embed_true_type_fonts)
        self.assertFalse(doc.font_infos.embed_system_fonts)
        self.assertFalse(doc.font_infos.save_subset_fonts)

    def test_strike_through(self):
        doc = aspose.words.Document()
        para = doc.get_child(aspose.words.NodeType.PARAGRAPH, 0, True).as_paragraph()
        run = aspose.words.Run(doc = doc, text = "Text with a single-line strikethrough.")
        run.font.strike_through = True
        para.append_child(run)
        para = para.parent_node.append_child(aspose.words.Paragraph(doc)).as_paragraph()
        run = aspose.words.Run(doc = doc, text = "Text with a double-line strikethrough.")
        run.font.double_strike_through = True
        para.append_child(run)
        doc.save(file_name = ARTIFACTS_DIR + "Font.StrikeThrough.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.StrikeThrough.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Text with a single-line strikethrough.", run.get_text().strip())
        self.assertTrue(run.font.strike_through)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("Text with a double-line strikethrough.", run.get_text().strip())
        self.assertTrue(run.font.double_strike_through)

    def test_position_subscript(self):
        doc = aspose.words.Document()
        para = doc.get_child(aspose.words.NodeType.PARAGRAPH, 0, True).as_paragraph()
        run = aspose.words.Run(doc = doc, text = "Raised text. ")
        run.font.position = 5
        para.append_child(run)
        run = aspose.words.Run(doc = doc, text = "Lowered text. ")
        run.font.position = -10
        para.append_child(run)
        run = aspose.words.Run(doc = doc, text = "Text in its default position. ")
        para.append_child(run)
        run = aspose.words.Run(doc = doc, text = "Subscript. ")
        run.font.subscript = True
        para.append_child(run)
        run = aspose.words.Run(doc = doc, text = "Superscript.")
        run.font.superscript = True
        para.append_child(run)
        doc.save(file_name = ARTIFACTS_DIR + "Font.PositionSubscript.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.PositionSubscript.docx")
        run = doc.first_section.body.first_paragraph.runs[0]
        self.assertEqual("Raised text.", run.get_text().strip())
        self.assertEqual(5, run.font.position)
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.PositionSubscript.docx")
        run = doc.first_section.body.first_paragraph.runs[1]
        self.assertEqual("Lowered text.", run.get_text().strip())
        self.assertEqual(-10, run.font.position)
        run = doc.first_section.body.first_paragraph.runs[3]
        self.assertEqual("Subscript.", run.get_text().strip())
        self.assertTrue(run.font.subscript)
        run = doc.first_section.body.first_paragraph.runs[4]
        self.assertEqual("Superscript.", run.get_text().strip())
        self.assertTrue(run.font.superscript)

    def test_scaling_spacing(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.scaling = 150
        builder.writeln("Wide characters")
        builder.font.spacing = 1
        builder.writeln("Expanded by 1pt")
        builder.font.spacing = -1
        builder.writeln("Condensed by 1pt")
        doc.save(file_name = ARTIFACTS_DIR + "Font.ScalingSpacing.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.ScalingSpacing.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Wide characters", run.get_text().strip())
        self.assertEqual(150, run.font.scaling)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("Expanded by 1pt", run.get_text().strip())
        self.assertEqual(1, run.font.spacing)
        run = doc.first_section.body.paragraphs[2].runs[0]
        self.assertEqual("Condensed by 1pt", run.get_text().strip())
        self.assertEqual(-1, run.font.spacing)

    def test_italic(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.size = 36
        builder.font.italic = True
        builder.writeln("Hello world!")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Italic.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Italic.docx")
        run = doc.first_section.body.first_paragraph.runs[0]
        self.assertEqual("Hello world!", run.get_text().strip())
        self.assertTrue(run.font.italic)

    def test_engrave_emboss(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.size = 36
        builder.font.color = aspose.pydrawing.Color.light_blue
        builder.font.engrave = True
        builder.writeln("This text is engraved.")
        builder.font.engrave = False
        builder.font.emboss = True
        builder.writeln("This text is embossed.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.EngraveEmboss.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.EngraveEmboss.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("This text is engraved.", run.get_text().strip())
        self.assertTrue(run.font.engrave)
        self.assertFalse(run.font.emboss)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("This text is embossed.", run.get_text().strip())
        self.assertFalse(run.font.engrave)
        self.assertTrue(run.font.emboss)

    def test_shadow(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.shadow = True
        builder.font.size = 36
        builder.writeln("This text has a shadow.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Shadow.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Shadow.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("This text has a shadow.", run.get_text().strip())
        self.assertTrue(run.font.shadow)

    def test_outline(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.outline = True
        builder.font.color = aspose.pydrawing.Color.blue
        builder.font.size = 36
        builder.writeln("This text has an outline.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Outline.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Outline.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("This text has an outline.", run.get_text().strip())
        self.assertTrue(run.font.outline)

    def test_hidden(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.hidden = True
        builder.font.size = 36
        builder.writeln("This text will not be visible in the document.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Hidden.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Hidden.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("This text will not be visible in the document.", run.get_text().strip())
        self.assertTrue(run.font.hidden)

    def test_kerning(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.name = "Arial Black"
        builder.font.size = 18
        builder.font.kerning = 24
        builder.writeln("TALLY. (Kerning not applied)")
        builder.font.kerning = 12
        builder.writeln("TALLY. (Kerning applied)")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Kerning.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Kerning.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("TALLY. (Kerning not applied)", run.get_text().strip())
        self.assertEqual(24, run.font.kerning)
        self.assertEqual(18, run.font.size)
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("TALLY. (Kerning applied)", run.get_text().strip())
        self.assertEqual(12, run.font.kerning)
        self.assertEqual(18, run.font.size)

    def test_no_proofing(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.no_proofing = True
        builder.writeln("Proofing has been disabled, so these spelking errrs will not display red lines underneath.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.NoProofing.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.NoProofing.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Proofing has been disabled, so these spelking errrs will not display red lines underneath.", run.get_text().strip())
        self.assertTrue(run.font.no_proofing)

    def test_locale_id(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_underlines(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.underline = aspose.words.Underline.DOTTED
        builder.font.underline_color = aspose.pydrawing.Color.red
        builder.writeln("Underlined text.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Underlines.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Underlines.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Underlined text.", run.get_text().strip())
        self.assertEqual(aspose.words.Underline.DOTTED, run.font.underline)
        self.assertEqual(aspose.pydrawing.Color.red.to_argb(), run.font.underline_color.to_argb())

    def test_complex_script(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.complex_script = True
        builder.writeln("Text treated as complex script.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.ComplexScript.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.ComplexScript.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Text treated as complex script.", run.get_text().strip())
        self.assertTrue(run.font.complex_script)

    def test_sparkling_text(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.size = 36
        builder.font.text_effect = aspose.words.TextEffect.SPARKLE_TEXT
        builder.writeln("Text with a sparkle effect.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.SparklingText.doc")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.SparklingText.doc")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Text with a sparkle effect.", run.get_text().strip())
        self.assertEqual(aspose.words.TextEffect.SPARKLE_TEXT, run.font.text_effect)

    def test_foreground_and_background(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        shading = doc.first_section.body.first_paragraph.paragraph_format.shading
        shading.texture = aspose.words.TextureIndex.TEXTURE_12PT5_PERCENT
        shading.foreground_pattern_theme_color = aspose.words.themes.ThemeColor.DARK1
        shading.background_pattern_theme_color = aspose.words.themes.ThemeColor.DARK2
        shading.foreground_tint_and_shade = 0.5
        shading.background_tint_and_shade = -0.2
        builder.font.border.color = aspose.pydrawing.Color.green
        builder.font.border.line_width = 2.5
        builder.font.border.line_style = aspose.words.LineStyle.DASH_DOT_STROKER
        builder.writeln("Foreground and background pattern colors for shading texture.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.ForegroundAndBackground.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.ForegroundAndBackground.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Foreground and background pattern colors for shading texture.", run.get_text().strip())
        self.assertEqual(aspose.words.themes.ThemeColor.DARK1, doc.first_section.body.paragraphs[0].paragraph_format.shading.foreground_pattern_theme_color)
        self.assertEqual(aspose.words.themes.ThemeColor.DARK2, doc.first_section.body.paragraphs[0].paragraph_format.shading.background_pattern_theme_color)
        self.assertAlmostEqual(0.5, doc.first_section.body.paragraphs[0].paragraph_format.shading.foreground_tint_and_shade, delta=0.1)
        self.assertAlmostEqual(-0.2, doc.first_section.body.paragraphs[0].paragraph_format.shading.background_tint_and_shade, delta=0.1)

    def test_shading(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.color = aspose.pydrawing.Color.white
        shading = builder.font.shading
        shading.texture = aspose.words.TextureIndex.TEXTURE_DIAGONAL_UP
        shading.background_pattern_color = aspose.pydrawing.Color.orange_red
        shading.foreground_pattern_color = aspose.pydrawing.Color.dark_blue
        builder.writeln("White text on an orange background with a two-tone texture.")
        doc.save(file_name = ARTIFACTS_DIR + "Font.Shading.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Shading.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("White text on an orange background with a two-tone texture.", run.get_text().strip())
        self.assertEqual(aspose.pydrawing.Color.white.to_argb(), run.font.color.to_argb())
        self.assertEqual(aspose.words.TextureIndex.TEXTURE_DIAGONAL_UP, run.font.shading.texture)
        self.assertEqual(aspose.pydrawing.Color.orange_red.to_argb(), run.font.shading.background_pattern_color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.dark_blue.to_argb(), run.font.shading.foreground_pattern_color.to_argb())

    def test_bidi(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_far_east(self):
        raise NotImplementedError("Unsupported ctor for type CultureInfo")

    def test_name_ascii(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.name_ascii = "Calibri"
        self.assertEqual("Calibri", builder.font.name)
        builder.font.name_other = "Courier New"
        builder.writeln("Hello, Привет")
        doc.save(file_name = ARTIFACTS_DIR + "Font.NameAscii.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.NameAscii.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Hello, Привет", run.get_text().strip())
        self.assertEqual("Calibri", run.font.name)
        self.assertEqual("Calibri", run.font.name_ascii)
        self.assertEqual("Courier New", run.font.name_other)

    def test_change_style(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.font.style_name = "Emphasis"
        builder.writeln("Text originally in \"Emphasis\" style")
        builder.font.style_identifier = aspose.words.StyleIdentifier.INTENSE_EMPHASIS
        builder.writeln("Text originally in \"Intense Emphasis\" style")
        for run in doc.get_child_nodes(aspose.words.NodeType.RUN, True).of_type():
            if run.font.style_name == "Emphasis":
                run.font.style_name = "Strong"
            if run.font.style_identifier == aspose.words.StyleIdentifier.INTENSE_EMPHASIS:
                run.font.style_identifier = aspose.words.StyleIdentifier.STRONG
        doc.save(file_name = ARTIFACTS_DIR + "Font.ChangeStyle.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.ChangeStyle.docx")
        doc_run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("Text originally in \"Emphasis\" style", doc_run.get_text().strip())
        self.assertEqual(aspose.words.StyleIdentifier.STRONG, doc_run.font.style_identifier)
        self.assertEqual("Strong", doc_run.font.style_name)
        doc_run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("Text originally in \"Intense Emphasis\" style", doc_run.get_text().strip())
        self.assertEqual(aspose.words.StyleIdentifier.STRONG, doc_run.font.style_identifier)
        self.assertEqual("Strong", doc_run.font.style_name)

    def test_built_in(self):
        doc = aspose.words.Document()
        style = doc.styles.get_by_name("Emphasis")
        self.assertTrue(style.built_in)
        style = doc.styles.add(aspose.words.StyleType.CHARACTER, "MyStyle")
        style.font.color = aspose.pydrawing.Color.navy
        style.font.name = "Courier New"
        self.assertFalse(style.built_in)

    def test_style(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        style = doc.styles.add(aspose.words.StyleType.CHARACTER, "MyStyle")
        style.font.color = aspose.pydrawing.Color.red
        style.font.name = "Courier New"
        builder.font.style_name = "MyStyle"
        builder.write("This text is in a custom style.")
        for run in doc.get_child_nodes(aspose.words.NodeType.RUN, True).of_type():
            char_style = run.font.style
            if not char_style.built_in:
                run.font.underline = aspose.words.Underline.DOUBLE
        doc.save(file_name = ARTIFACTS_DIR + "Font.Style.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.Style.docx")
        doc_run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("This text is in a custom style.", doc_run.get_text().strip())
        self.assertEqual("MyStyle", doc_run.font.style_name)
        self.assertFalse(doc_run.font.style.built_in)
        self.assertEqual(aspose.words.Underline.DOUBLE, doc_run.font.underline)

    def test_get_available_fonts(self):
        raise NotImplementedError("Unrecognizable type of expression: folderFontSource[0]")

    def test_set_font_auto_color(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), builder.font.color.to_argb())
        builder.font.shading.background_pattern_color = aspose.pydrawing.Color.dark_blue
        builder.writeln("The text color automatically chosen for this run is white.")
        self.assertEqual(aspose.pydrawing.Color.white.to_argb(), doc.first_section.body.paragraphs[0].runs[0].font.auto_color.to_argb())
        builder.font.shading.background_pattern_color = aspose.pydrawing.Color.light_blue
        builder.writeln("The text color automatically chosen for this run is black.")
        self.assertEqual(aspose.pydrawing.Color.black.to_argb(), doc.first_section.body.paragraphs[1].runs[0].font.auto_color.to_argb())
        doc.save(file_name = ARTIFACTS_DIR + "Font.SetFontAutoColor.docx")
        doc = aspose.words.Document(file_name = ARTIFACTS_DIR + "Font.SetFontAutoColor.docx")
        run = doc.first_section.body.paragraphs[0].runs[0]
        self.assertEqual("The text color automatically chosen for this run is white.", run.get_text().strip())
        self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), run.font.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.dark_blue.to_argb(), run.font.shading.background_pattern_color.to_argb())
        run = doc.first_section.body.paragraphs[1].runs[0]
        self.assertEqual("The text color automatically chosen for this run is black.", run.get_text().strip())
        self.assertEqual(aspose.pydrawing.Color.empty().to_argb(), run.font.color.to_argb())
        self.assertEqual(aspose.pydrawing.Color.light_blue.to_argb(), run.font.shading.background_pattern_color.to_argb())

    def test_default_fonts(self):
        doc = aspose.words.Document()
        self.assertEqual(3, doc.font_infos.count)
        self.assertTrue(doc.font_infos.contains("Times New Roman"))
        self.assertEqual(204, doc.font_infos.get_by_name("Times New Roman").charset)
        self.assertTrue(doc.font_infos.contains("Symbol"))
        self.assertTrue(doc.font_infos.contains("Arial"))

    def test_extract_embedded_font(self):
        raise NotImplementedError("Unsupported target type System.IO.File")

    def test_get_font_info_from_file(self):
        raise NotImplementedError("Unsupported target type System.Collections.Generic.IEnumerator")

    def test_has_dml_effect(self):
        doc = aspose.words.Document(file_name = MY_DIR + "DrawingML text effects.docx")
        runs = doc.first_section.body.first_paragraph.runs
        self.assertTrue(runs[0].font.has_dml_effect(aspose.words.TextDmlEffect.SHADOW))
        self.assertTrue(runs[1].font.has_dml_effect(aspose.words.TextDmlEffect.SHADOW))
        self.assertTrue(runs[2].font.has_dml_effect(aspose.words.TextDmlEffect.REFLECTION))
        self.assertTrue(runs[3].font.has_dml_effect(aspose.words.TextDmlEffect.EFFECT_3D))
        self.assertTrue(runs[4].font.has_dml_effect(aspose.words.TextDmlEffect.FILL))

    def test_theme_fonts_colors(self):
        raise NotImplementedError("Unsupported target type System.Console")

    def test_create_themed_style(self):
        doc = aspose.words.Document()
        builder = aspose.words.DocumentBuilder(doc)
        builder.writeln()
        style = doc.styles.add(aspose.words.StyleType.PARAGRAPH, "ThemedStyle")
        style.font.theme_font = aspose.words.themes.ThemeFont.MAJOR
        style.font.theme_color = aspose.words.themes.ThemeColor.ACCENT5
        style.font.tint_and_shade = 0.3
        builder.paragraph_format.style_name = "ThemedStyle"
        builder.writeln("Text with themed style")
        run = (builder.current_paragraph.previous_sibling.as_paragraph()).first_child.as_run()
        self.assertEqual(aspose.words.themes.ThemeFont.MAJOR, run.font.theme_font)
        self.assertEqual("Times New Roman", run.font.name)
        self.assertEqual(aspose.words.themes.ThemeFont.MAJOR, run.font.theme_font_ascii)
        self.assertEqual("Times New Roman", run.font.name_ascii)
        self.assertEqual(aspose.words.themes.ThemeFont.MAJOR, run.font.theme_font_bi)
        self.assertEqual("Times New Roman", run.font.name_bi)
        self.assertEqual(aspose.words.themes.ThemeFont.MAJOR, run.font.theme_font_far_east)
        self.assertEqual("Times New Roman", run.font.name_far_east)
        self.assertEqual(aspose.words.themes.ThemeFont.MAJOR, run.font.theme_font_other)
        self.assertEqual("Times New Roman", run.font.name_other)
        self.assertEqual(aspose.words.themes.ThemeColor.ACCENT5, run.font.theme_color)
        self.assertEqual(aspose.pydrawing.Color.empty(), run.font.color)
