github_url
:   hide

# Font {#class_Font}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `FontFile<class_FontFile>`{.interpreted-text
role="ref"}, `FontVariation<class_FontVariation>`{.interpreted-text
role="ref"}, `SystemFont<class_SystemFont>`{.interpreted-text
role="ref"}

Abstract base class for fonts and font variations.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for different font types. It has methods for drawing
text and font character introspection.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Font_property_fallbacks}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Font<class_Font>`{.interpreted-text role="ref"}\]
**fallbacks** = `[]`
`🔗<class_Font_property_fallbacks>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallbacks**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Font<class_Font>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Font<class_Font>`{.interpreted-text role="ref"}\]
  **get_fallbacks**()

Array of fallback **Font**s to use as a substitute if a glyph is not
found in this current **Font**.

If this array is empty in a
`FontVariation<class_FontVariation>`{.interpreted-text role="ref"}, the
`FontVariation.base_font<class_FontVariation_property_base_font>`{.interpreted-text
role="ref"}\'s fallbacks are used instead.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Font_method_draw_char}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**draw_char**(canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, char: `int<class_int>`{.interpreted-text role="ref"},
font_size: `int<class_int>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_draw_char>`{.interpreted-text
role="ref"}

Draw a single Unicode character `char` into a canvas item using the
font, at a given position, with `modulate` color. `pos` specifies the
baseline, not the top. To draw from the top, *ascent* must be added to
the Y axis. If `oversampling` is greater than zero, it is used as font
oversampling factor, otherwise viewport oversampling settings are used.

\*\*Note:\*\* Do not use this function to draw strings character by
character, use
`draw_string()<class_Font_method_draw_string>`{.interpreted-text
role="ref"} or `TextLine<class_TextLine>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_draw_char_outline}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**draw_char_outline**(canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, char: `int<class_int>`{.interpreted-text role="ref"},
font_size: `int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"} = -1, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_draw_char_outline>`{.interpreted-text
role="ref"}

Draw a single Unicode character `char` outline into a canvas item using
the font, at a given position, with `modulate` color and `size` outline
size. `pos` specifies the baseline, not the top. To draw from the top,
*ascent* must be added to the Y axis. If `oversampling` is greater than
zero, it is used as font oversampling factor, otherwise viewport
oversampling settings are used.

\*\*Note:\*\* Do not use this function to draw strings character by
character, use
`draw_string()<class_Font_method_draw_string>`{.interpreted-text
role="ref"} or `TextLine<class_TextLine>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_draw_multiline_string}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multiline_string**(canvas_item:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"}, alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, max_lines: `int<class_int>`{.interpreted-text
role="ref"} = -1, modulate: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1), brk_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_draw_multiline_string>`{.interpreted-text
role="ref"}

Breaks `text` into lines using rules specified by `brk_flags` and draws
it into a canvas item using the font, at a given position, with
`modulate` color, optionally clipping the width and aligning
horizontally. `pos` specifies the baseline of the first line, not the
top. To draw from the top, *ascent* must be added to the Y axis. If
`oversampling` is greater than zero, it is used as font oversampling
factor, otherwise viewport oversampling settings are used.

See also
`CanvasItem.draw_multiline_string()<class_CanvasItem_method_draw_multiline_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_draw_multiline_string_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multiline_string_outline**(canvas_item:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"}, alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, max_lines: `int<class_int>`{.interpreted-text
role="ref"} = -1, size: `int<class_int>`{.interpreted-text role="ref"} =
1, modulate: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(1, 1, 1, 1), brk_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_draw_multiline_string_outline>`{.interpreted-text
role="ref"}

Breaks `text` to the lines using rules specified by `brk_flags` and
draws text outline into a canvas item using the font, at a given
position, with `modulate` color and `size` outline size, optionally
clipping the width and aligning horizontally. `pos` specifies the
baseline of the first line, not the top. To draw from the top, *ascent*
must be added to the Y axis. If `oversampling` is greater than zero, it
is used as font oversampling factor, otherwise viewport oversampling
settings are used.

See also
`CanvasItem.draw_multiline_string_outline()<class_CanvasItem_method_draw_multiline_string_outline>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_draw_string}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_string**(canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"},
alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, modulate: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1), justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_draw_string>`{.interpreted-text
role="ref"}

Draw `text` into a canvas item using the font, at a given position, with
`modulate` color, optionally clipping the width and aligning
horizontally. `pos` specifies the baseline, not the top. To draw from
the top, *ascent* must be added to the Y axis. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

See also
`CanvasItem.draw_string()<class_CanvasItem_method_draw_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_draw_string_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_string_outline**(canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"},
alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, size: `int<class_int>`{.interpreted-text role="ref"} =
1, modulate: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(1, 1, 1, 1), justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_draw_string_outline>`{.interpreted-text
role="ref"}

Draw `text` outline into a canvas item using the font, at a given
position, with `modulate` color and `size` outline size, optionally
clipping the width and aligning horizontally. `pos` specifies the
baseline, not the top. To draw from the top, *ascent* must be added to
the Y axis. If `oversampling` is greater than zero, it is used as font
oversampling factor, otherwise viewport oversampling settings are used.

See also
`CanvasItem.draw_string_outline()<class_CanvasItem_method_draw_string_outline>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_find_variation}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**find_variation**(variation_coordinates:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
face_index: `int<class_int>`{.interpreted-text role="ref"} = 0,
strength: `float<class_float>`{.interpreted-text role="ref"} = 0.0,
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} = Transform2D(1, 0, 0, 1, 0, 0), spacing_top:
`int<class_int>`{.interpreted-text role="ref"} = 0, spacing_bottom:
`int<class_int>`{.interpreted-text role="ref"} = 0, spacing_space:
`int<class_int>`{.interpreted-text role="ref"} = 0, spacing_glyph:
`int<class_int>`{.interpreted-text role="ref"} = 0, baseline_offset:
`float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_find_variation>`{.interpreted-text
role="ref"}

Returns `TextServer<class_TextServer>`{.interpreted-text role="ref"} RID
of the font cache for specific variation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_ascent**(font_size: `int<class_int>`{.interpreted-text role="ref"}
= 16)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_ascent>`{.interpreted-text
role="ref"}

Returns the average font ascent (number of pixels above the baseline).

\*\*Note:\*\* Real ascent of the string is context-dependent and can be
significantly different from the value returned by this function. Use it
only as rough estimate (e.g. as the ascent of empty line).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_char_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_char_size**(char: `int<class_int>`{.interpreted-text role="ref"},
font_size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_char_size>`{.interpreted-text
role="ref"}

Returns the size of a character. Does not take kerning into account.

\*\*Note:\*\* Do not use this function to calculate width of the string
character by character, use
`get_string_size()<class_Font_method_get_string_size>`{.interpreted-text
role="ref"} or `TextLine<class_TextLine>`{.interpreted-text role="ref"}
instead. The height returned is the font height (see also
`get_height()<class_Font_method_get_height>`{.interpreted-text
role="ref"}) and has no relation to the glyph height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_descent**(font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_descent>`{.interpreted-text
role="ref"}

Returns the average font descent (number of pixels below the baseline).

\*\*Note:\*\* Real descent of the string is context-dependent and can be
significantly different from the value returned by this function. Use it
only as rough estimate (e.g. as the descent of empty line).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_face_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_face_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_face_count>`{.interpreted-text
role="ref"}

Returns number of faces in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_font_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_font_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_font_name>`{.interpreted-text
role="ref"}

Returns font family name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_font_stretch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_font_stretch**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_font_stretch>`{.interpreted-text
role="ref"}

Returns font stretch amount, compared to a normal width. A percentage
value between `50%` and `200%`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_font_style}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}\] **get_font_style**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_font_style>`{.interpreted-text
role="ref"}

Returns font style flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_font_style_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_font_style_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_font_style_name>`{.interpreted-text
role="ref"}

Returns font style name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_font_weight}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_font_weight**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_font_weight>`{.interpreted-text
role="ref"}

Returns weight (boldness) of the font. A value in the `100...999` range,
normal font weight is `400`, bold font weight is `700`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_height}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_height**(font_size: `int<class_int>`{.interpreted-text role="ref"}
= 16)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_height>`{.interpreted-text
role="ref"}

Returns the total average font height (ascent plus descent) in pixels.

\*\*Note:\*\* Real height of the string is context-dependent and can be
significantly different from the value returned by this function. Use it
only as rough estimate (e.g. as the height of empty line).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_multiline_string_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_multiline_string_size**(text:
`String<class_String>`{.interpreted-text role="ref"}, alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, max_lines: `int<class_int>`{.interpreted-text
role="ref"} = -1, brk_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_multiline_string_size>`{.interpreted-text
role="ref"}

Returns the size of a bounding box of a string broken into the lines,
taking kerning and advance into account.

See also
`draw_multiline_string()<class_Font_method_draw_multiline_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_opentype_features}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_opentype_features**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_opentype_features>`{.interpreted-text
role="ref"}

Returns a set of OpenType feature tags. More info: [OpenType feature
tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_ot_name_strings}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_ot_name_strings**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_ot_name_strings>`{.interpreted-text
role="ref"}

Returns `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
with OpenType font name strings (localized font names, version,
description, license information, sample text, etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_rids}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**get_rids**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_rids>`{.interpreted-text
role="ref"}

Returns `Array<class_Array>`{.interpreted-text role="ref"} of valid
**Font** `RID<class_RID>`{.interpreted-text role="ref"}s, which can be
passed to the `TextServer<class_TextServer>`{.interpreted-text
role="ref"} methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_spacing}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_spacing**(spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_spacing>`{.interpreted-text
role="ref"}

Returns the amount of spacing for the given `spacing` type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_string_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_string_size**(text: `String<class_String>`{.interpreted-text
role="ref"}, alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_get_string_size>`{.interpreted-text
role="ref"}

Returns the size of a bounding box of a single-line string, taking
kerning, advance and subpixel positioning into account. See also
`get_multiline_string_size()<class_Font_method_get_multiline_string_size>`{.interpreted-text
role="ref"} and
`draw_string()<class_Font_method_draw_string>`{.interpreted-text
role="ref"}.

For example, to get the string size as displayed by a single-line Label,
use:

::::: tabs
::: code-tab
gdscript

var string_size =
\$Label.get_theme_font(\"font\").get_string_size(\$Label.text,
HORIZONTAL_ALIGNMENT_LEFT, -1,
\$Label.get_theme_font_size(\"font_size\"))
:::

::: code-tab
csharp

Label label = GetNode\<Label\>(\"Label\"); Vector2 stringSize =
label.GetThemeFont(\"font\").GetStringSize(label.Text,
HorizontalAlignment.Left, -1, label.GetThemeFontSize(\"font_size\"));
:::
:::::

\*\*Note:\*\* Since kerning, advance and subpixel positioning are taken
into account by
`get_string_size()<class_Font_method_get_string_size>`{.interpreted-text
role="ref"}, using separate
`get_string_size()<class_Font_method_get_string_size>`{.interpreted-text
role="ref"} calls on substrings of a string then adding the results
together will return a different result compared to using a single
`get_string_size()<class_Font_method_get_string_size>`{.interpreted-text
role="ref"} call on the full string.

\*\*Note:\*\* Real height of the string is context-dependent and can be
significantly different from the value returned by
`get_height()<class_Font_method_get_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_supported_chars}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_supported_chars**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_supported_chars>`{.interpreted-text
role="ref"}

Returns a string containing all the characters available in the font.

If a given character is included in more than one font data source, it
appears only once in the returned string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_supported_feature_list}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_supported_feature_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_supported_feature_list>`{.interpreted-text
role="ref"}

Returns list of OpenType features supported by font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_supported_variation_list}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_supported_variation_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_supported_variation_list>`{.interpreted-text
role="ref"}

Returns list of supported [variation
coordinates](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg),
each coordinate is returned as
`tag: Vector3i(min_value,max_value,default_value)`.

Font variations allow for continuous change of glyph characteristics
along some given design axis, such as weight, width or slant.

To print available variation axes of a variable font:

    var fv = FontVariation.new()
    fv.base_font = load("res://RobotoFlex.ttf")
    var variation_list = fv.get_supported_variation_list()
    for tag in variation_list:
        var name = TextServerManager.get_primary_interface().tag_to_name(tag)
        var values = variation_list[tag]
        print("variation axis: %s (%d)\n\tmin, max, default: %s" % [name, tag, values])

\*\*Note:\*\* To set and get variation coordinates of a
`FontVariation<class_FontVariation>`{.interpreted-text role="ref"}, use
`FontVariation.variation_opentype<class_FontVariation_property_variation_opentype>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_underline_position**(font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_underline_position>`{.interpreted-text
role="ref"}

Returns average pixel offset of the underline below the baseline.

\*\*Note:\*\* Real underline position of the string is context-dependent
and can be significantly different from the value returned by this
function. Use it only as rough estimate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_get_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_underline_thickness**(font_size:
`int<class_int>`{.interpreted-text role="ref"} = 16)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_get_underline_thickness>`{.interpreted-text
role="ref"}

Returns average thickness of the underline.

\*\*Note:\*\* Real underline thickness of the string is
context-dependent and can be significantly different from the value
returned by this function. Use it only as rough estimate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_has_char}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_char**(char:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Font_method_has_char>`{.interpreted-text
role="ref"}

Returns `true` if a Unicode `char` is available in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_is_language_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_language_supported**(language:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_is_language_supported>`{.interpreted-text
role="ref"}

Returns `true`, if font supports given language ([ISO
639](https://en.wikipedia.org/wiki/ISO_639-1) code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_is_script_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_script_supported**(script: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Font_method_is_script_supported>`{.interpreted-text
role="ref"}

Returns `true`, if font supports given script ([ISO
15924](https://en.wikipedia.org/wiki/ISO_15924) code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Font_method_set_cache_capacity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cache_capacity**(single_line: `int<class_int>`{.interpreted-text
role="ref"}, multi_line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Font_method_set_cache_capacity>`{.interpreted-text role="ref"}

Sets LRU cache capacity for `draw_*` methods.
