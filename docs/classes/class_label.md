github_url
:   hide

::: {.meta keywords="text"}
:::

# Label {#class_Label}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control for displaying plain text.

::: rst-class
classref-introduction-group
:::

## Description

A control for displaying plain text. It gives you control over the
horizontal and vertical alignment and can wrap the text inside the
node\'s bounding rectangle. It doesn\'t support bold, italics, or other
rich text formatting. For that, use
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Label_property_autowrap_mode}
::: rst-class
classref-property
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **autowrap_mode** = `0`
`🔗<class_Label_property_autowrap_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap_mode**(value:
  `AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
  role="ref"})
- `AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
  role="ref"} **get_autowrap_mode**()

If set to something other than
`TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`{.interpreted-text
role="ref"}, the text gets wrapped inside the node\'s bounding
rectangle. If you resize the node, it will change its height
automatically to show all the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_autowrap_trim_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] **autowrap_trim_flags** = `192`
`🔗<class_Label_property_autowrap_trim_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap_trim_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
  role="ref"}\] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See
`TextServer.BREAK_TRIM_START_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES>`{.interpreted-text
role="ref"} and
`TextServer.BREAK_TRIM_END_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES>`{.interpreted-text
role="ref"} for more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_clip_text}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **clip_text** = `false`
`🔗<class_Label_property_clip_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clip_text**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_clipping_text**()

If `true`, the Label only shows the text that fits inside its bounding
rectangle and will clip text horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_ellipsis_char}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **ellipsis_char** =
`"…"` `🔗<class_Label_property_ellipsis_char>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ellipsis_char**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_ellipsis_char**()

Ellipsis character used for text clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_horizontal_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **horizontal_alignment** = `0`
`🔗<class_Label_property_horizontal_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_horizontal_alignment**()

Controls the text\'s horizontal alignment. Supports left, center, right,
and fill (also known as justify).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_justification_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] **justification_flags** = `163`
`🔗<class_Label_property_justification_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_justification_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
  role="ref"}\] **get_justification_flags**()

Line fill alignment rules.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_label_settings}
::: rst-class
classref-property
:::
::::

`LabelSettings<class_LabelSettings>`{.interpreted-text role="ref"}
**label_settings**
`🔗<class_Label_property_label_settings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_label_settings**(value:
  `LabelSettings<class_LabelSettings>`{.interpreted-text role="ref"})
- `LabelSettings<class_LabelSettings>`{.interpreted-text role="ref"}
  **get_label_settings**()

A `LabelSettings<class_LabelSettings>`{.interpreted-text role="ref"}
resource that can be shared between multiple **Label** nodes. Takes
priority over theme properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_Label_property_language>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_language**()

Language code used for line-breaking and text shaping algorithms, if
left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_lines_skipped}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **lines_skipped** = `0`
`🔗<class_Label_property_lines_skipped>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lines_skipped**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_lines_skipped**()

The number of the lines ignored and not displayed from the start of the
`text<class_Label_property_text>`{.interpreted-text role="ref"} value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_max_lines_visible}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_lines_visible** =
`-1` `🔗<class_Label_property_max_lines_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_lines_visible**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_lines_visible**()

Limits the lines of text the node shows on screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_paragraph_separator}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**paragraph_separator** = `"\\n"`
`🔗<class_Label_property_paragraph_separator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_paragraph_separator**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_paragraph_separator**()

String used as a paragraph separator. Each paragraph is processed
independently, in its own BiDi context.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_Label_property_structured_text_bidi_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_structured_text_bidi_override**(value:
  `StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
  role="ref"})
- `StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
  role="ref"} **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_Label_property_structured_text_bidi_override_options>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_structured_text_bidi_override_options**(value:
  `Array<class_Array>`{.interpreted-text role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_tab_stops}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **tab_stops** = `PackedFloat32Array()`
`🔗<class_Label_property_tab_stops>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_stops**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_tab_stops**()

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_Label_property_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

The text to display on screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_Label_property_text_direction>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_direction**(value:
  `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"})
- `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"} **get_text_direction**()

Base text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_text_overrun_behavior}
::: rst-class
classref-property
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **text_overrun_behavior** = `0`
`🔗<class_Label_property_text_overrun_behavior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_overrun_behavior**(value:
  `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"})
- `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"} **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the node\'s bounding
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_uppercase}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **uppercase** = `false`
`🔗<class_Label_property_uppercase>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uppercase**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_vertical_alignment}
::: rst-class
classref-property
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **vertical_alignment** = `0`
`🔗<class_Label_property_vertical_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical_alignment**(value:
  `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
  role="ref"})
- `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
  role="ref"} **get_vertical_alignment**()

Controls the text\'s vertical alignment. Supports top, center, bottom,
and fill.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_visible_characters}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **visible_characters** =
`-1` `🔗<class_Label_property_visible_characters>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_characters**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_visible_characters**()

The number of characters to display. If set to `-1`, all characters are
displayed. This can be useful when animating the text appearing in a
dialog box.

\*\*Note:\*\* Setting this property updates
`visible_ratio<class_Label_property_visible_ratio>`{.interpreted-text
role="ref"} accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_visible_characters_behavior}
::: rst-class
classref-property
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **visible_characters_behavior** = `0`
`🔗<class_Label_property_visible_characters_behavior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_characters_behavior**(value:
  `VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
  role="ref"})
- `VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
  role="ref"} **get_visible_characters_behavior**()

The clipping behavior when
`visible_characters<class_Label_property_visible_characters>`{.interpreted-text
role="ref"} or
`visible_ratio<class_Label_property_visible_ratio>`{.interpreted-text
role="ref"} is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_property_visible_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **visible_ratio** =
`1.0` `🔗<class_Label_property_visible_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_visible_ratio**()

The fraction of characters to display, relative to the total number of
characters (see
`get_total_character_count()<class_Label_method_get_total_character_count>`{.interpreted-text
role="ref"}). If set to `1.0`, all characters are displayed. If set to
`0.5`, only half of the characters will be displayed. This can be useful
when animating the text appearing in a dialog box.

\*\*Note:\*\* Setting this property updates
`visible_characters<class_Label_property_visible_characters>`{.interpreted-text
role="ref"} accordingly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Label_method_get_character_bounds}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_character_bounds**(pos: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Label_method_get_character_bounds>`{.interpreted-text
role="ref"}

Returns the bounding rectangle of the character at position `pos` in the
label\'s local coordinate system. If the character is a non-visual
character or `pos` is outside the valid range, an empty
`Rect2<class_Rect2>`{.interpreted-text role="ref"} is returned. If the
character is a part of a composite grapheme, the bounding rectangle of
the whole grapheme is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_method_get_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Label_method_get_line_count>`{.interpreted-text
role="ref"}

Returns the number of lines of text the Label has.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_method_get_line_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_height**(line:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Label_method_get_line_height>`{.interpreted-text
role="ref"}

Returns the height of the line `line`.

If `line` is set to `-1`, returns the biggest line height.

If there are no lines, returns font size in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_method_get_total_character_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_total_character_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Label_method_get_total_character_count>`{.interpreted-text
role="ref"}

Returns the total number of printable characters in the text (excluding
spaces and newlines).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_method_get_visible_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_visible_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Label_method_get_visible_line_count>`{.interpreted-text
role="ref"}

Returns the number of lines shown. Useful if the **Label**\'s height
cannot currently display all lines.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_Label_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(1, 1, 1, 1)`
`🔗<class_Label_theme_color_font_color>`{.interpreted-text role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
**Label**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_Label_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The color of text outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_color_font_shadow_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_shadow_color**
= `Color(0, 0, 0, 0)`
`🔗<class_Label_theme_color_font_shadow_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the text\'s shadow
effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_constant_line_spacing}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **line_spacing** = `3`
`🔗<class_Label_theme_constant_line_spacing>`{.interpreted-text
role="ref"}

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_Label_theme_constant_outline_size>`{.interpreted-text
role="ref"}

Text outline size.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_Label_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

\*\*Note:\*\* Using a value that is larger than half the font size is
not recommended, as the font outline may fail to be fully closed in this
case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_constant_paragraph_spacing}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **paragraph_spacing** =
`0` `🔗<class_Label_theme_constant_paragraph_spacing>`{.interpreted-text
role="ref"}

Vertical space between paragraphs. Added on top of
`line_spacing<class_Label_theme_constant_line_spacing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_constant_shadow_offset_x}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_offset_x** = `1`
`🔗<class_Label_theme_constant_shadow_offset_x>`{.interpreted-text
role="ref"}

The horizontal offset of the text\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_constant_shadow_offset_y}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_offset_y** = `1`
`🔗<class_Label_theme_constant_shadow_offset_y>`{.interpreted-text
role="ref"}

The vertical offset of the text\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_constant_shadow_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_outline_size** =
`1`
`🔗<class_Label_theme_constant_shadow_outline_size>`{.interpreted-text
role="ref"}

The size of the shadow outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_Label_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} used for the
**Label**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_Label_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the **Label**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_Label_theme_style_focus>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Label** is focused (when used with assistive apps).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label_theme_style_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **normal**
`🔗<class_Label_theme_style_normal>`{.interpreted-text role="ref"}

Background `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for
the **Label**.
