github_url
:   hide

# TextureProgressBar {#class_TextureProgressBar}

**Inherits:** `Range<class_Range>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture-based progress bar. Useful for loading screens and life or
stamina bars.

::: rst-class
classref-introduction-group
:::

## Description

TextureProgressBar works like
`ProgressBar<class_ProgressBar>`{.interpreted-text role="ref"}, but uses
up to 3 textures instead of Godot\'s
`Theme<class_Theme>`{.interpreted-text role="ref"} resource. It can be
used to create horizontal, vertical and radial progress bars.

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

:::: {#enum_TextureProgressBar_FillMode}
::: rst-class
classref-enumeration
:::
::::

enum **FillMode**:
`🔗<enum_TextureProgressBar_FillMode>`{.interpreted-text role="ref"}

:::: {#class_TextureProgressBar_constant_FILL_LEFT_TO_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_LEFT_TO_RIGHT** = `0`

The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills from left to right.

:::: {#class_TextureProgressBar_constant_FILL_RIGHT_TO_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_RIGHT_TO_LEFT** = `1`

The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills from right to left.

:::: {#class_TextureProgressBar_constant_FILL_TOP_TO_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_TOP_TO_BOTTOM** = `2`

The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills from top to bottom.

:::: {#class_TextureProgressBar_constant_FILL_BOTTOM_TO_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_BOTTOM_TO_TOP** = `3`

The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills from bottom to top.

:::: {#class_TextureProgressBar_constant_FILL_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_CLOCKWISE** = `4`

Turns the node into a radial bar. The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills clockwise. See
`radial_center_offset<class_TextureProgressBar_property_radial_center_offset>`{.interpreted-text
role="ref"},
`radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>`{.interpreted-text
role="ref"} and
`radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>`{.interpreted-text
role="ref"} to control the way the bar fills up.

:::: {#class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_COUNTER_CLOCKWISE** = `5`

Turns the node into a radial bar. The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills counterclockwise. See
`radial_center_offset<class_TextureProgressBar_property_radial_center_offset>`{.interpreted-text
role="ref"},
`radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>`{.interpreted-text
role="ref"} and
`radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>`{.interpreted-text
role="ref"} to control the way the bar fills up.

:::: {#class_TextureProgressBar_constant_FILL_BILINEAR_LEFT_AND_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_BILINEAR_LEFT_AND_RIGHT** = `6`

The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills from the center, expanding both towards the left and
the right.

:::: {#class_TextureProgressBar_constant_FILL_BILINEAR_TOP_AND_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_BILINEAR_TOP_AND_BOTTOM** = `7`

The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills from the center, expanding both towards the top and
the bottom.

:::: {#class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} **FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE** = `8`

Turns the node into a radial bar. The
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} fills radially from the center, expanding both clockwise and
counterclockwise. See
`radial_center_offset<class_TextureProgressBar_property_radial_center_offset>`{.interpreted-text
role="ref"},
`radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>`{.interpreted-text
role="ref"} and
`radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>`{.interpreted-text
role="ref"} to control the way the bar fills up.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TextureProgressBar_property_fill_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fill_mode** = `0`
`🔗<class_TextureProgressBar_property_fill_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fill_mode**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_fill_mode**()

The fill direction. See
`FillMode<enum_TextureProgressBar_FillMode>`{.interpreted-text
role="ref"} for possible values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_nine_patch_stretch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **nine_patch_stretch**
= `false`
`🔗<class_TextureProgressBar_property_nine_patch_stretch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_nine_patch_stretch**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_nine_patch_stretch**()

If `true`, Godot treats the bar\'s textures like in
`NinePatchRect<class_NinePatchRect>`{.interpreted-text role="ref"}. Use
the `stretch_margin_*` properties like
`stretch_margin_bottom<class_TextureProgressBar_property_stretch_margin_bottom>`{.interpreted-text
role="ref"} to set up the nine patch\'s 3×3 grid. When using a radial
`fill_mode<class_TextureProgressBar_property_fill_mode>`{.interpreted-text
role="ref"}, this setting will only enable stretching for
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"}, while
`texture_under<class_TextureProgressBar_property_texture_under>`{.interpreted-text
role="ref"} and
`texture_over<class_TextureProgressBar_property_texture_over>`{.interpreted-text
role="ref"} will be treated like in
`NinePatchRect<class_NinePatchRect>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_radial_center_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**radial_center_offset** = `Vector2(0, 0)`
`🔗<class_TextureProgressBar_property_radial_center_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_center_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_radial_center_offset**()

Offsets
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} if
`fill_mode<class_TextureProgressBar_property_fill_mode>`{.interpreted-text
role="ref"} is
`FILL_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE>`{.interpreted-text
role="ref"},
`FILL_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE>`{.interpreted-text
role="ref"}, or
`FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The effective radial center always stays within the
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} bounds. If you need to move it outside the texture\'s
bounds, modify the
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} to contain additional empty space where needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_radial_fill_degrees}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**radial_fill_degrees** = `360.0`
`🔗<class_TextureProgressBar_property_radial_fill_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fill_degrees**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fill_degrees**()

Upper limit for the fill of
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} if
`fill_mode<class_TextureProgressBar_property_fill_mode>`{.interpreted-text
role="ref"} is
`FILL_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE>`{.interpreted-text
role="ref"},
`FILL_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE>`{.interpreted-text
role="ref"}, or
`FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE>`{.interpreted-text
role="ref"}. When the node\'s `value` is equal to its `max_value`, the
texture fills up to this angle.

See `Range.value<class_Range_property_value>`{.interpreted-text
role="ref"},
`Range.max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_radial_initial_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**radial_initial_angle** = `0.0`
`🔗<class_TextureProgressBar_property_radial_initial_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_initial_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_radial_initial_angle**()

Starting angle for the fill of
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} if
`fill_mode<class_TextureProgressBar_property_fill_mode>`{.interpreted-text
role="ref"} is
`FILL_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE>`{.interpreted-text
role="ref"},
`FILL_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE>`{.interpreted-text
role="ref"}, or
`FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE>`{.interpreted-text
role="ref"}. When the node\'s `value` is equal to its `min_value`, the
texture doesn\'t show up at all. When the `value` increases, the texture
fills and tends towards
`radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>`{.interpreted-text
role="ref"} is wrapped between `0` and `360` degrees (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_stretch_margin_bottom}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stretch_margin_bottom**
= `0`
`🔗<class_TextureProgressBar_property_stretch_margin_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The height of the 9-patch\'s bottom row. A margin of 16 means the
9-slice\'s bottom corners and side will have a height of 16 pixels. You
can set all 4 margin values individually to create panels with
non-uniform borders. Only effective if
`nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_stretch_margin_left}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stretch_margin_left** =
`0`
`🔗<class_TextureProgressBar_property_stretch_margin_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The width of the 9-patch\'s left column. Only effective if
`nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_stretch_margin_right}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stretch_margin_right**
= `0`
`🔗<class_TextureProgressBar_property_stretch_margin_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The width of the 9-patch\'s right column. Only effective if
`nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_stretch_margin_top}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stretch_margin_top** =
`0`
`🔗<class_TextureProgressBar_property_stretch_margin_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stretch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The height of the 9-patch\'s top row. Only effective if
`nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_texture_over}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_over**
`🔗<class_TextureProgressBar_property_texture_over>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_over_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_over_texture**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} that draws
over the progress bar. Use it to add highlights or an upper-frame that
hides part of
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_texture_progress}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_progress**
`🔗<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_progress_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_progress_texture**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} that clips
based on the node\'s `value` and
`fill_mode<class_TextureProgressBar_property_fill_mode>`{.interpreted-text
role="ref"}. As `value` increased, the texture fills up. It shows
entirely when `value` reaches `max_value`. It doesn\'t show at all if
`value` is equal to `min_value`.

The `value` property comes from `Range<class_Range>`{.interpreted-text
role="ref"}. See
`Range.value<class_Range_property_value>`{.interpreted-text role="ref"},
`Range.min_value<class_Range_property_min_value>`{.interpreted-text
role="ref"},
`Range.max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_texture_progress_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**texture_progress_offset** = `Vector2(0, 0)`
`🔗<class_TextureProgressBar_property_texture_progress_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_progress_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_texture_progress_offset**()

The offset of
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"}. Useful for
`texture_over<class_TextureProgressBar_property_texture_over>`{.interpreted-text
role="ref"} and
`texture_under<class_TextureProgressBar_property_texture_under>`{.interpreted-text
role="ref"} with fancy borders, to avoid transparent margins in your
progress texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_texture_under}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_under**
`🔗<class_TextureProgressBar_property_texture_under>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_under_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_under_texture**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} that draws
under the progress bar. The bar\'s background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_tint_over}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **tint_over** =
`Color(1, 1, 1, 1)`
`🔗<class_TextureProgressBar_property_tint_over>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_over**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_tint_over**()

Multiplies the color of the bar\'s
`texture_over<class_TextureProgressBar_property_texture_over>`{.interpreted-text
role="ref"} texture. The effect is similar to
`CanvasItem.modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"}, except it only affects this specific texture instead of the
entire node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_tint_progress}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **tint_progress** =
`Color(1, 1, 1, 1)`
`🔗<class_TextureProgressBar_property_tint_progress>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_progress**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_tint_progress**()

Multiplies the color of the bar\'s
`texture_progress<class_TextureProgressBar_property_texture_progress>`{.interpreted-text
role="ref"} texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_property_tint_under}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **tint_under** =
`Color(1, 1, 1, 1)`
`🔗<class_TextureProgressBar_property_tint_under>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_under**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_tint_under**()

Multiplies the color of the bar\'s
`texture_under<class_TextureProgressBar_property_texture_under>`{.interpreted-text
role="ref"} texture.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TextureProgressBar_method_get_stretch_margin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_stretch_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureProgressBar_method_get_stretch_margin>`{.interpreted-text
role="ref"}

Returns the stretch margin with the specified index. See
`stretch_margin_bottom<class_TextureProgressBar_property_stretch_margin_bottom>`{.interpreted-text
role="ref"} and related properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureProgressBar_method_set_stretch_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stretch_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextureProgressBar_method_set_stretch_margin>`{.interpreted-text
role="ref"}

Sets the stretch margin with the specified index. See
`stretch_margin_bottom<class_TextureProgressBar_property_stretch_margin_bottom>`{.interpreted-text
role="ref"} and related properties.
