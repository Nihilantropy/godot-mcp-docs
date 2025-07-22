github_url
:   hide

::: {.meta keywords="text"}
:::

# Label3D {#class_Label3D}

**Inherits:**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node for displaying plain text in 3D space.

::: rst-class
classref-introduction-group
:::

## Description

A node for displaying plain text in 3D space. By adjusting various
properties of this node, you can configure things such as the text\'s
appearance and whether it always faces the camera.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D text <../tutorials/3d/3d_text>`{.interpreted-text role="doc"}

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

## Enumerations

:::: {#enum_Label3D_DrawFlags}
::: rst-class
classref-enumeration
:::
::::

enum **DrawFlags**: `🔗<enum_Label3D_DrawFlags>`{.interpreted-text
role="ref"}

:::: {#class_Label3D_constant_FLAG_SHADED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_SHADED** = `0`

If set, lights in the environment affect the label.

:::: {#class_Label3D_constant_FLAG_DOUBLE_SIDED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_DOUBLE_SIDED** = `1`

If set, text can be seen from the back as well. If not, the text is
invisible when looking at it from behind.

:::: {#class_Label3D_constant_FLAG_DISABLE_DEPTH_TEST}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_DISABLE_DEPTH_TEST** = `2`

Disables the depth test, so this object is drawn on top of all others.
However, objects drawn after it in the draw order may cover it.

:::: {#class_Label3D_constant_FLAG_FIXED_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_FIXED_SIZE** = `3`

Label is scaled by depth so that it always appears the same size on
screen.

:::: {#class_Label3D_constant_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_MAX** = `4`

Represents the size of the
`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Label3D_AlphaCutMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlphaCutMode**: `🔗<enum_Label3D_AlphaCutMode>`{.interpreted-text
role="ref"}

:::: {#class_Label3D_constant_ALPHA_CUT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text role="ref"}
**ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent
areas, but transparency sorting issues may be visible when multiple
transparent materials are overlapping.
`GeometryInstance3D.cast_shadow<class_GeometryInstance3D_property_cast_shadow>`{.interpreted-text
role="ref"} has no effect when this transparency mode is used; the
**Label3D** will never cast shadows.

:::: {#class_Label3D_constant_ALPHA_CUT_DISCARD}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text role="ref"}
**ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh
edges will be visible unless some form of screen-space antialiasing is
enabled (see
`ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>`{.interpreted-text
role="ref"}). This mode is also known as *alpha testing* or *1-bit
transparency*.

\*\*Note:\*\* This mode might have issues with anti-aliased fonts and
outlines, try adjusting
`alpha_scissor_threshold<class_Label3D_property_alpha_scissor_threshold>`{.interpreted-text
role="ref"} or using MSDF font.

\*\*Note:\*\* When using text with overlapping glyphs (e.g., cursive
scripts), this mode might have transparency sorting issues between the
main text and the outline.

:::: {#class_Label3D_constant_ALPHA_CUT_OPAQUE_PREPASS}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text role="ref"}
**ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower
than
`ALPHA_CUT_DISABLED<class_Label3D_constant_ALPHA_CUT_DISABLED>`{.interpreted-text
role="ref"} or
`ALPHA_CUT_DISCARD<class_Label3D_constant_ALPHA_CUT_DISCARD>`{.interpreted-text
role="ref"}, but it allows displaying translucent areas and smooth edges
while using proper sorting.

\*\*Note:\*\* When using text with overlapping glyphs (e.g., cursive
scripts), this mode might have transparency sorting issues between the
main text and the outline.

:::: {#class_Label3D_constant_ALPHA_CUT_HASH}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text role="ref"}
**ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic
threshold, the rest will remain opaque.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Label3D_property_alpha_antialiasing_edge}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**alpha_antialiasing_edge** = `0.0`
`🔗<class_Label3D_property_alpha_antialiasing_edge>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_antialiasing_edge**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_alpha_antialiasing_edge**()

Threshold at which antialiasing will be applied on the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_alpha_antialiasing_mode}
::: rst-class
classref-property
:::
::::

`AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`{.interpreted-text
role="ref"} **alpha_antialiasing_mode** = `0`
`🔗<class_Label3D_property_alpha_antialiasing_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_antialiasing**(value:
  `AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`{.interpreted-text
  role="ref"})
- `AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`{.interpreted-text
  role="ref"} **get_alpha_antialiasing**()

The type of alpha antialiasing to apply.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_alpha_cut}
::: rst-class
classref-property
:::
::::

`AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text role="ref"}
**alpha_cut** = `0`
`🔗<class_Label3D_property_alpha_cut>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_cut_mode**(value:
  `AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text
  role="ref"})
- `AlphaCutMode<enum_Label3D_AlphaCutMode>`{.interpreted-text
  role="ref"} **get_alpha_cut_mode**()

The alpha cutting mode to use for the sprite.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_alpha_hash_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **alpha_hash_scale**
= `1.0` `🔗<class_Label3D_property_alpha_hash_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_hash_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_alpha_hash_scale**()

The hashing scale for Alpha Hash. Recommended values between `0` and
`2`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_alpha_scissor_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**alpha_scissor_threshold** = `0.5`
`🔗<class_Label3D_property_alpha_scissor_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_scissor_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_alpha_scissor_threshold**()

Threshold at which the alpha scissor will discard values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_autowrap_mode}
::: rst-class
classref-property
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **autowrap_mode** = `0`
`🔗<class_Label3D_property_autowrap_mode>`{.interpreted-text role="ref"}

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

:::: {#class_Label3D_property_autowrap_trim_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] **autowrap_trim_flags** = `192`
`🔗<class_Label3D_property_autowrap_trim_flags>`{.interpreted-text
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

:::: {#class_Label3D_property_billboard}
::: rst-class
classref-property
:::
::::

`BillboardMode<enum_BaseMaterial3D_BillboardMode>`{.interpreted-text
role="ref"} **billboard** = `0`
`🔗<class_Label3D_property_billboard>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_billboard_mode**(value:
  `BillboardMode<enum_BaseMaterial3D_BillboardMode>`{.interpreted-text
  role="ref"})
- `BillboardMode<enum_BaseMaterial3D_BillboardMode>`{.interpreted-text
  role="ref"} **get_billboard_mode**()

The billboard mode to use for the label.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_double_sided}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **double_sided** =
`true` `🔗<class_Label3D_property_double_sided>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"},
  enabled: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, text can be seen from the back as well, if `false`, it is
invisible when looking at it from behind.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_fixed_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fixed_size** =
`false` `🔗<class_Label3D_property_fixed_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"},
  enabled: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the label is rendered at the same size regardless of
distance. The label\'s size on screen is the same as if the camera was
`1.0` units away from the label\'s origin, regardless of the actual
distance from the camera. The
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}\'s field of
view (or `Camera3D.size<class_Camera3D_property_size>`{.interpreted-text
role="ref"} when in orthogonal/frustum mode) still affects the size the
label is drawn at.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_font}
::: rst-class
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_Label3D_property_font>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font**(value: `Font<class_Font>`{.interpreted-text role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"} **get_font**()

Font configuration used to display text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size** = `32`
`🔗<class_Label3D_property_font_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_size**()

Font size of the **Label3D**\'s text. To make the font look more
detailed when up close, increase
`font_size<class_Label3D_property_font_size>`{.interpreted-text
role="ref"} while decreasing
`pixel_size<class_Label3D_property_pixel_size>`{.interpreted-text
role="ref"} at the same time.

Higher font sizes require more time to render new characters, which can
cause stuttering during gameplay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_horizontal_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **horizontal_alignment** = `1`
`🔗<class_Label3D_property_horizontal_alignment>`{.interpreted-text
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

:::: {#class_Label3D_property_justification_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] **justification_flags** = `163`
`🔗<class_Label3D_property_justification_flags>`{.interpreted-text
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

:::: {#class_Label3D_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_Label3D_property_language>`{.interpreted-text role="ref"}

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

:::: {#class_Label3D_property_line_spacing}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **line_spacing** =
`0.0` `🔗<class_Label3D_property_line_spacing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_spacing**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **modulate** =
`Color(1, 1, 1, 1)`
`🔗<class_Label3D_property_modulate>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_modulate**()

Text `Color<class_Color>`{.interpreted-text role="ref"} of the
**Label3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_no_depth_test}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **no_depth_test** =
`false` `🔗<class_Label3D_property_no_depth_test>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"},
  enabled: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, depth testing is disabled and the object will be drawn in
render order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)` `🔗<class_Label3D_property_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The text drawing offset (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_outline_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **outline_modulate**
= `Color(0, 0, 0, 1)`
`🔗<class_Label3D_property_outline_modulate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_outline_modulate**()

The tint of text outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_outline_render_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**outline_render_priority** = `-1`
`🔗<class_Label3D_property_outline_render_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_render_priority**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_outline_render_priority**()

Sets the render priority for the text outline. Higher priority objects
will be sorted in front of lower priority objects.

\*\*Note:\*\* This only applies if
`alpha_cut<class_Label3D_property_alpha_cut>`{.interpreted-text
role="ref"} is set to
`ALPHA_CUT_DISABLED<class_Label3D_constant_ALPHA_CUT_DISABLED>`{.interpreted-text
role="ref"} (default value).

\*\*Note:\*\* This only applies to sorting of transparent objects. This
will not impact how transparent objects are sorted relative to opaque
objects. This is because opaque objects are not sorted, while
transparent objects are sorted from back to front (subject to priority).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_outline_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `12`
`🔗<class_Label3D_property_outline_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_outline_size**()

Text outline size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_pixel_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pixel_size** =
`0.005` `🔗<class_Label3D_property_pixel_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pixel_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pixel_size**()

The size of one pixel\'s width on the label to scale it in 3D. To make
the font look more detailed when up close, increase
`font_size<class_Label3D_property_font_size>`{.interpreted-text
role="ref"} while decreasing
`pixel_size<class_Label3D_property_pixel_size>`{.interpreted-text
role="ref"} at the same time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_render_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **render_priority** = `0`
`🔗<class_Label3D_property_render_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_render_priority**()

Sets the render priority for the text. Higher priority objects will be
sorted in front of lower priority objects.

\*\*Note:\*\* This only applies if
`alpha_cut<class_Label3D_property_alpha_cut>`{.interpreted-text
role="ref"} is set to
`ALPHA_CUT_DISABLED<class_Label3D_constant_ALPHA_CUT_DISABLED>`{.interpreted-text
role="ref"} (default value).

\*\*Note:\*\* This only applies to sorting of transparent objects. This
will not impact how transparent objects are sorted relative to opaque
objects. This is because opaque objects are not sorted, while
transparent objects are sorted from back to front (subject to priority).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_shaded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shaded** = `false`
`🔗<class_Label3D_property_shaded>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"},
  enabled: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the `Light3D<class_Light3D>`{.interpreted-text role="ref"} in
the `Environment<class_Environment>`{.interpreted-text role="ref"} has
effects on the label.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_Label3D_property_structured_text_bidi_override>`{.interpreted-text
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

:::: {#class_Label3D_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_Label3D_property_structured_text_bidi_override_options>`{.interpreted-text
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

:::: {#class_Label3D_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_Label3D_property_text>`{.interpreted-text role="ref"}

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

:::: {#class_Label3D_property_text_direction}
::: rst-class
classref-property
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**text_direction** = `0`
`🔗<class_Label3D_property_text_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_direction**(value:
  `Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"})
- `Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
  **get_text_direction**()

Base text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_texture_filter}
::: rst-class
classref-property
:::
::::

`TextureFilter<enum_BaseMaterial3D_TextureFilter>`{.interpreted-text
role="ref"} **texture_filter** = `3`
`🔗<class_Label3D_property_texture_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_filter**(value:
  `TextureFilter<enum_BaseMaterial3D_TextureFilter>`{.interpreted-text
  role="ref"})
- `TextureFilter<enum_BaseMaterial3D_TextureFilter>`{.interpreted-text
  role="ref"} **get_texture_filter**()

Filter flags for the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_uppercase}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **uppercase** = `false`
`🔗<class_Label3D_property_uppercase>`{.interpreted-text role="ref"}

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

:::: {#class_Label3D_property_vertical_alignment}
::: rst-class
classref-property
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **vertical_alignment** = `1`
`🔗<class_Label3D_property_vertical_alignment>`{.interpreted-text
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

Controls the text\'s vertical alignment. Supports top, center, and
bottom.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_property_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **width** = `500.0`
`🔗<class_Label3D_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_width**()

Text width (in pixels), used for autowrap and fill alignment.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Label3D_method_generate_triangle_mesh}
::: rst-class
classref-method
:::
::::

`TriangleMesh<class_TriangleMesh>`{.interpreted-text role="ref"}
**generate_triangle_mesh**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Label3D_method_generate_triangle_mesh>`{.interpreted-text
role="ref"}

Returns a `TriangleMesh<class_TriangleMesh>`{.interpreted-text
role="ref"} with the label\'s vertices following its current
configuration (such as its
`pixel_size<class_Label3D_property_pixel_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_method_get_draw_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_draw_flag**(flag:
`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Label3D_method_get_draw_flag>`{.interpreted-text
role="ref"}

Returns the value of the specified flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Label3D_method_set_draw_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_draw_flag**(flag:
`DrawFlags<enum_Label3D_DrawFlags>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Label3D_method_set_draw_flag>`{.interpreted-text role="ref"}

If `true`, the specified `flag` will be enabled.
