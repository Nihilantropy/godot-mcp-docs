github_url
:   hide

# TextLine {#class_TextLine}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds a line of text.

::: rst-class
classref-introduction-group
:::

## Description

Abstraction over `TextServer<class_TextServer>`{.interpreted-text
role="ref"} for handling a single line of text.

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

:::: {#class_TextLine_property_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **alignment** = `0`
`🔗<class_TextLine_property_alignment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_horizontal_alignment**()

Sets text alignment within the line as if the line was horizontal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_direction}
::: rst-class
classref-property
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**direction** = `0`
`🔗<class_TextLine_property_direction>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_direction**(value:
  `Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"})
- `Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
  **get_direction**()

Text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_ellipsis_char}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **ellipsis_char** =
`"…"` `🔗<class_TextLine_property_ellipsis_char>`{.interpreted-text
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

:::: {#class_TextLine_property_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] **flags** = `3`
`🔗<class_TextLine_property_flags>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
  role="ref"}\] **get_flags**()

Line alignment rules. For more info see
`TextServer<class_TextServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_orientation}
::: rst-class
classref-property
:::
::::

`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
**orientation** = `0`
`🔗<class_TextLine_property_orientation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_orientation**(value:
  `Orientation<enum_TextServer_Orientation>`{.interpreted-text
  role="ref"})
- `Orientation<enum_TextServer_Orientation>`{.interpreted-text
  role="ref"} **get_orientation**()

Text orientation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_preserve_control}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **preserve_control** =
`false` `🔗<class_TextLine_property_preserve_control>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_preserve_control**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_preserve_control**()

If set to `true` text will display control characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_preserve_invalid}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **preserve_invalid** =
`true` `🔗<class_TextLine_property_preserve_invalid>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_preserve_invalid**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_preserve_invalid**()

If set to `true` text will display invalid characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_text_overrun_behavior}
::: rst-class
classref-property
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **text_overrun_behavior** = `3`
`🔗<class_TextLine_property_text_overrun_behavior>`{.interpreted-text
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

The clipping behavior when the text exceeds the text line\'s set width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_property_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **width** = `-1.0`
`🔗<class_TextLine_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_width**()

Text line width.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TextLine_method_add_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **add_object**(key:
`Variant<class_Variant>`{.interpreted-text role="ref"}, size:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 5, length: `int<class_int>`{.interpreted-text role="ref"}
= 1, baseline: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`🔗<class_TextLine_method_add_object>`{.interpreted-text role="ref"}

Adds inline object to the text buffer, `key` must be unique. In the
text, object is represented as `length` object replacement characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_add_string}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **add_string**(text:
`String<class_String>`{.interpreted-text role="ref"}, font:
`Font<class_Font>`{.interpreted-text role="ref"}, font_size:
`int<class_int>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"} = \"\", meta:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`🔗<class_TextLine_method_add_string>`{.interpreted-text role="ref"}

Adds text span and font to draw it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_TextLine_method_clear>`{.interpreted-text role="ref"}

Clears text line (removes text and inline objects).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw**(canvas: `RID<class_RID>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextLine_method_draw>`{.interpreted-text
role="ref"}

Draw text into a canvas item at a given position, with `color`. `pos`
specifies the top left corner of the bounding box. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_draw_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_outline**(canvas: `RID<class_RID>`{.interpreted-text role="ref"},
pos: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
outline_size: `int<class_int>`{.interpreted-text role="ref"} = 1, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextLine_method_draw_outline>`{.interpreted-text
role="ref"}

Draw text into a canvas item at a given position, with `color`. `pos`
specifies the top left corner of the bounding box. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_inferred_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**get_inferred_direction**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_inferred_direction>`{.interpreted-text
role="ref"}

Returns the text writing direction inferred by the BiDi algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_line_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_line_ascent**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_line_ascent>`{.interpreted-text
role="ref"}

Returns the text ascent (number of pixels above the baseline for
horizontal layout or to the left of baseline for vertical).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_line_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_line_descent**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_line_descent>`{.interpreted-text
role="ref"}

Returns the text descent (number of pixels below the baseline for
horizontal layout or to the right of baseline for vertical).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_line_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_line_underline_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_line_underline_position>`{.interpreted-text
role="ref"}

Returns pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_line_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_line_underline_thickness**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_line_underline_thickness>`{.interpreted-text
role="ref"}

Returns thickness of the underline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_line_width}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_line_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_line_width>`{.interpreted-text role="ref"}

Returns width (for horizontal layout) or height (for vertical) of the
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_object_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_object_rect**(key: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextLine_method_get_object_rect>`{.interpreted-text
role="ref"}

Returns bounding rectangle of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_objects}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_objects**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextLine_method_get_objects>`{.interpreted-text
role="ref"}

Returns array of inline objects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextLine_method_get_rid>`{.interpreted-text
role="ref"}

Returns TextServer buffer RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextLine_method_get_size>`{.interpreted-text
role="ref"}

Returns size of the bounding box of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_hit_test}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hit_test**(coords:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextLine_method_hit_test>`{.interpreted-text
role="ref"}

Returns caret character offset at the specified pixel offset at the
baseline. This function always returns a valid position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_resize_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **resize_object**(key:
`Variant<class_Variant>`{.interpreted-text role="ref"}, size:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 5, baseline: `float<class_float>`{.interpreted-text
role="ref"} = 0.0)
`🔗<class_TextLine_method_resize_object>`{.interpreted-text role="ref"}

Sets new size and alignment of embedded object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_set_bidi_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bidi_override**(override: `Array<class_Array>`{.interpreted-text
role="ref"})
`🔗<class_TextLine_method_set_bidi_override>`{.interpreted-text
role="ref"}

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi
algorithm will be used on each range separately.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextLine_method_tab_align}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**tab_align**(tab_stops:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}) `🔗<class_TextLine_method_tab_align>`{.interpreted-text
role="ref"}

Aligns text to the given tab-stops.
