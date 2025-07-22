github_url
:   hide

# StyleBoxTexture {#class_StyleBoxTexture}

**Inherits:** `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A texture-based nine-patch `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A texture-based nine-patch `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}, in a way similar to
`NinePatchRect<class_NinePatchRect>`{.interpreted-text role="ref"}. This
stylebox performs a 3×3 scaling of a texture, where only the center cell
is fully stretched. This makes it possible to design bordered styles
regardless of the stylebox\'s size.

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

:::: {#enum_StyleBoxTexture_AxisStretchMode}
::: rst-class
classref-enumeration
:::
::::

enum **AxisStretchMode**:
`🔗<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text role="ref"}

:::: {#class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_STRETCH}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
role="ref"} **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretch the stylebox\'s texture. This results in visible distortion
unless the texture size matches the stylebox\'s size perfectly.

:::: {#class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
role="ref"} **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the stylebox\'s texture to match the stylebox\'s size according
to the nine-patch system.

:::: {#class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE_FIT}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
role="ref"} **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the stylebox\'s texture to match the stylebox\'s size according
to the nine-patch system. Unlike
`AXIS_STRETCH_MODE_TILE<class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE>`{.interpreted-text
role="ref"}, the texture may be slightly stretched to make the
nine-patch texture tile seamlessly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_StyleBoxTexture_property_axis_stretch_horizontal}
::: rst-class
classref-property
:::
::::

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
role="ref"} **axis_stretch_horizontal** = `0`
`🔗<class_StyleBoxTexture_property_axis_stretch_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_axis_stretch_mode**(value:
  `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
  role="ref"})
- `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
  role="ref"} **get_h_axis_stretch_mode**()

Controls how the stylebox\'s texture will be stretched or tiled
horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_axis_stretch_vertical}
::: rst-class
classref-property
:::
::::

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
role="ref"} **axis_stretch_vertical** = `0`
`🔗<class_StyleBoxTexture_property_axis_stretch_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_axis_stretch_mode**(value:
  `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
  role="ref"})
- `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`{.interpreted-text
  role="ref"} **get_v_axis_stretch_mode**()

Controls how the stylebox\'s texture will be stretched or tiled
vertically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_draw_center}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_center** =
`true`
`🔗<class_StyleBoxTexture_property_draw_center>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_center**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_draw_center_enabled**()

If `true`, the nine-patch texture\'s center tile will be drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_expand_margin_bottom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**expand_margin_bottom** = `0.0`
`🔗<class_StyleBoxTexture_property_expand_margin_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Expands the bottom margin of this style box when drawing, causing it to
be drawn larger than requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_expand_margin_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**expand_margin_left** = `0.0`
`🔗<class_StyleBoxTexture_property_expand_margin_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Expands the left margin of this style box when drawing, causing it to be
drawn larger than requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_expand_margin_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**expand_margin_right** = `0.0`
`🔗<class_StyleBoxTexture_property_expand_margin_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Expands the right margin of this style box when drawing, causing it to
be drawn larger than requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_expand_margin_top}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **expand_margin_top**
= `0.0`
`🔗<class_StyleBoxTexture_property_expand_margin_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_expand_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Expands the top margin of this style box when drawing, causing it to be
drawn larger than requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_modulate_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **modulate_color** =
`Color(1, 1, 1, 1)`
`🔗<class_StyleBoxTexture_property_modulate_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_modulate**()

Modulates the color of the texture when this style box is drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_region_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **region_rect** =
`Rect2(0, 0, 0, 0)`
`🔗<class_StyleBoxTexture_property_region_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_region_rect**()

The region to use from the
`texture<class_StyleBoxTexture_property_texture>`{.interpreted-text
role="ref"}.

This is equivalent to first wrapping the
`texture<class_StyleBoxTexture_property_texture>`{.interpreted-text
role="ref"} in an `AtlasTexture<class_AtlasTexture>`{.interpreted-text
role="ref"} with the same region.

If empty (`Rect2(0, 0, 0, 0)`), the whole
`texture<class_StyleBoxTexture_property_texture>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_StyleBoxTexture_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The texture to use when drawing this style box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_texture_margin_bottom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**texture_margin_bottom** = `0.0`
`🔗<class_StyleBoxTexture_property_texture_margin_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Increases the bottom margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part
of the bottom border of the 3×3 box.

This is also the value used as fallback for
`StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"} if it is negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_texture_margin_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**texture_margin_left** = `0.0`
`🔗<class_StyleBoxTexture_property_texture_margin_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Increases the left margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part
of the left border of the 3×3 box.

This is also the value used as fallback for
`StyleBox.content_margin_left<class_StyleBox_property_content_margin_left>`{.interpreted-text
role="ref"} if it is negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_texture_margin_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**texture_margin_right** = `0.0`
`🔗<class_StyleBoxTexture_property_texture_margin_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Increases the right margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part
of the right border of the 3×3 box.

This is also the value used as fallback for
`StyleBox.content_margin_right<class_StyleBox_property_content_margin_right>`{.interpreted-text
role="ref"} if it is negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_property_texture_margin_top}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**texture_margin_top** = `0.0`
`🔗<class_StyleBoxTexture_property_texture_margin_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Increases the top margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part
of the top border of the 3×3 box.

This is also the value used as fallback for
`StyleBox.content_margin_top<class_StyleBox_property_content_margin_top>`{.interpreted-text
role="ref"} if it is negative.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StyleBoxTexture_method_get_expand_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_expand_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBoxTexture_method_get_expand_margin>`{.interpreted-text
role="ref"}

Returns the expand margin size of the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_method_get_texture_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_texture_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBoxTexture_method_get_texture_margin>`{.interpreted-text
role="ref"}

Returns the margin size of the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_method_set_expand_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_expand_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StyleBoxTexture_method_set_expand_margin>`{.interpreted-text
role="ref"}

Sets the expand margin to `size` pixels for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_method_set_expand_margin_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_expand_margin_all**(size: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_StyleBoxTexture_method_set_expand_margin_all>`{.interpreted-text
role="ref"}

Sets the expand margin to `size` pixels for all sides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_method_set_texture_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StyleBoxTexture_method_set_texture_margin>`{.interpreted-text
role="ref"}

Sets the margin to `size` pixels for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxTexture_method_set_texture_margin_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture_margin_all**(size: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_StyleBoxTexture_method_set_texture_margin_all>`{.interpreted-text
role="ref"}

Sets the margin to `size` pixels for all sides.
