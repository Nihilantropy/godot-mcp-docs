github_url
:   hide

# StyleBoxFlat {#class_StyleBoxFlat}

**Inherits:** `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A customizable `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
that doesn\'t use a texture.

::: rst-class
classref-introduction-group
:::

## Description

By configuring various properties of this style box, you can achieve
many common looks without the need of a texture. This includes
optionally rounded borders, antialiasing, shadows, and skew.

Setting corner radius to high values is allowed. As soon as corners
overlap, the stylebox will switch to a relative system:

``` text
height = 30
corner_radius_top_left = 50
corner_radius_bottom_left = 100
```

The relative system now would take the 1:2 ratio of the two left corners
to calculate the actual corner width. Both corners added will **never**
be more than the height. Result:

``` text
corner_radius_top_left: 10
corner_radius_bottom_left: 20
```

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

:::: {#class_StyleBoxFlat_property_anti_aliasing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **anti_aliasing** =
`true` `🔗<class_StyleBoxFlat_property_anti_aliasing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_anti_aliased**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_anti_aliased**()

Antialiasing draws a small ring around the edges, which fades to
transparency. As a result, edges look much smoother. This is only
noticeable when using rounded corners or
`skew<class_StyleBoxFlat_property_skew>`{.interpreted-text role="ref"}.

\*\*Note:\*\* When using beveled corners with 45-degree angles
(`corner_detail<class_StyleBoxFlat_property_corner_detail>`{.interpreted-text
role="ref"} = 1), it is recommended to set
`anti_aliasing<class_StyleBoxFlat_property_anti_aliasing>`{.interpreted-text
role="ref"} to `false` to ensure crisp visuals and avoid possible visual
glitches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_anti_aliasing_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**anti_aliasing_size** = `1.0`
`🔗<class_StyleBoxFlat_property_anti_aliasing_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_aa_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_aa_size**()

This changes the size of the antialiasing effect. `1.0` is recommended
for an optimal result at 100% scale, identical to how rounded rectangles
are rendered in web browsers and most vector drawing software.

\*\*Note:\*\* Higher values may produce a blur effect but can also
create undesired artifacts on small boxes with large-radius corners.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_bg_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **bg_color** =
`Color(0.6, 0.6, 0.6, 1)`
`🔗<class_StyleBoxFlat_property_bg_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bg_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_bg_color**()

The background color of the stylebox.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_border_blend}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **border_blend** =
`false` `🔗<class_StyleBoxFlat_property_border_blend>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_blend**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_border_blend**()

If `true`, the border will fade into the background color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_border_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **border_color** =
`Color(0.8, 0.8, 0.8, 1)`
`🔗<class_StyleBoxFlat_property_border_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_border_color**()

Sets the color of the border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_border_width_bottom}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **border_width_bottom** =
`0`
`🔗<class_StyleBoxFlat_property_border_width_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, width:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Border width for the bottom border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_border_width_left}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **border_width_left** =
`0`
`🔗<class_StyleBoxFlat_property_border_width_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, width:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Border width for the left border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_border_width_right}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **border_width_right** =
`0`
`🔗<class_StyleBoxFlat_property_border_width_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, width:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Border width for the right border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_border_width_top}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **border_width_top** =
`0` `🔗<class_StyleBoxFlat_property_border_width_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, width:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_border_width**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Border width for the top border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_corner_detail}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **corner_detail** = `8`
`🔗<class_StyleBoxFlat_property_corner_detail>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_corner_detail**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_corner_detail**()

This sets the number of vertices used for each corner. Higher values
result in rounder corners but take more processing power to compute.
When choosing a value, you should take the corner radius
(`set_corner_radius_all()<class_StyleBoxFlat_method_set_corner_radius_all>`{.interpreted-text
role="ref"}) into account.

For corner radii less than 10, `4` or `5` should be enough. For corner
radii less than 30, values between `8` and `12` should be enough.

A corner detail of `1` will result in chamfered corners instead of
rounded corners, which is useful for some artistic effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_corner_radius_bottom_left}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**corner_radius_bottom_left** = `0`
`🔗<class_StyleBoxFlat_property_corner_radius_bottom_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"},
  radius: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The bottom-left corner\'s radius. If `0`, the corner is not rounded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_corner_radius_bottom_right}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**corner_radius_bottom_right** = `0`
`🔗<class_StyleBoxFlat_property_corner_radius_bottom_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"},
  radius: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The bottom-right corner\'s radius. If `0`, the corner is not rounded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_corner_radius_top_left}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**corner_radius_top_left** = `0`
`🔗<class_StyleBoxFlat_property_corner_radius_top_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"},
  radius: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The top-left corner\'s radius. If `0`, the corner is not rounded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_corner_radius_top_right}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**corner_radius_top_right** = `0`
`🔗<class_StyleBoxFlat_property_corner_radius_top_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"},
  radius: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_corner_radius**(corner:
  `Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The top-right corner\'s radius. If `0`, the corner is not rounded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_draw_center}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_center** =
`true` `🔗<class_StyleBoxFlat_property_draw_center>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_center**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_draw_center_enabled**()

Toggles drawing of the inner part of the stylebox.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_expand_margin_bottom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**expand_margin_bottom** = `0.0`
`🔗<class_StyleBoxFlat_property_expand_margin_bottom>`{.interpreted-text
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

Expands the stylebox outside of the control rect on the bottom edge.
Useful in combination with
`border_width_bottom<class_StyleBoxFlat_property_border_width_bottom>`{.interpreted-text
role="ref"} to draw a border outside the control rect.

\*\*Note:\*\* Unlike
`StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"},
`expand_margin_bottom<class_StyleBoxFlat_property_expand_margin_bottom>`{.interpreted-text
role="ref"} does *not* affect the size of the clickable area for
`Control<class_Control>`{.interpreted-text role="ref"}s. This can
negatively impact usability if used wrong, as the user may try to click
an area of the StyleBox that cannot actually receive clicks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_expand_margin_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**expand_margin_left** = `0.0`
`🔗<class_StyleBoxFlat_property_expand_margin_left>`{.interpreted-text
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

Expands the stylebox outside of the control rect on the left edge.
Useful in combination with
`border_width_left<class_StyleBoxFlat_property_border_width_left>`{.interpreted-text
role="ref"} to draw a border outside the control rect.

\*\*Note:\*\* Unlike
`StyleBox.content_margin_left<class_StyleBox_property_content_margin_left>`{.interpreted-text
role="ref"},
`expand_margin_left<class_StyleBoxFlat_property_expand_margin_left>`{.interpreted-text
role="ref"} does *not* affect the size of the clickable area for
`Control<class_Control>`{.interpreted-text role="ref"}s. This can
negatively impact usability if used wrong, as the user may try to click
an area of the StyleBox that cannot actually receive clicks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_expand_margin_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**expand_margin_right** = `0.0`
`🔗<class_StyleBoxFlat_property_expand_margin_right>`{.interpreted-text
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

Expands the stylebox outside of the control rect on the right edge.
Useful in combination with
`border_width_right<class_StyleBoxFlat_property_border_width_right>`{.interpreted-text
role="ref"} to draw a border outside the control rect.

\*\*Note:\*\* Unlike
`StyleBox.content_margin_right<class_StyleBox_property_content_margin_right>`{.interpreted-text
role="ref"},
`expand_margin_right<class_StyleBoxFlat_property_expand_margin_right>`{.interpreted-text
role="ref"} does *not* affect the size of the clickable area for
`Control<class_Control>`{.interpreted-text role="ref"}s. This can
negatively impact usability if used wrong, as the user may try to click
an area of the StyleBox that cannot actually receive clicks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_expand_margin_top}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **expand_margin_top**
= `0.0`
`🔗<class_StyleBoxFlat_property_expand_margin_top>`{.interpreted-text
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

Expands the stylebox outside of the control rect on the top edge. Useful
in combination with
`border_width_top<class_StyleBoxFlat_property_border_width_top>`{.interpreted-text
role="ref"} to draw a border outside the control rect.

\*\*Note:\*\* Unlike
`StyleBox.content_margin_top<class_StyleBox_property_content_margin_top>`{.interpreted-text
role="ref"},
`expand_margin_top<class_StyleBoxFlat_property_expand_margin_top>`{.interpreted-text
role="ref"} does *not* affect the size of the clickable area for
`Control<class_Control>`{.interpreted-text role="ref"}s. This can
negatively impact usability if used wrong, as the user may try to click
an area of the StyleBox that cannot actually receive clicks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_shadow_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **shadow_color** =
`Color(0, 0, 0, 0.6)`
`🔗<class_StyleBoxFlat_property_shadow_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_shadow_color**()

The color of the shadow. This has no effect if
`shadow_size<class_StyleBoxFlat_property_shadow_size>`{.interpreted-text
role="ref"} is lower than 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_shadow_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **shadow_offset**
= `Vector2(0, 0)`
`🔗<class_StyleBoxFlat_property_shadow_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_shadow_offset**()

The shadow offset in pixels. Adjusts the position of the shadow
relatively to the stylebox.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_shadow_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_size** = `0`
`🔗<class_StyleBoxFlat_property_shadow_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_shadow_size**()

The shadow size in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_property_skew}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **skew** =
`Vector2(0, 0)` `🔗<class_StyleBoxFlat_property_skew>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skew**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_skew**()

If set to a non-zero value on either axis,
`skew<class_StyleBoxFlat_property_skew>`{.interpreted-text role="ref"}
distorts the StyleBox horizontally and/or vertically. This can be used
for \"futuristic\"-style UIs. Positive values skew the StyleBox towards
the right (X axis) and upwards (Y axis), while negative values skew the
StyleBox towards the left (X axis) and downwards (Y axis).

\*\*Note:\*\* To ensure text does not touch the StyleBox\'s edges,
consider increasing the `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}\'s content margin (see
`StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"}). It is preferable to increase the content margin instead of
the expand margin (see
`expand_margin_bottom<class_StyleBoxFlat_property_expand_margin_bottom>`{.interpreted-text
role="ref"}), as increasing the expand margin does not increase the size
of the clickable area for `Control<class_Control>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StyleBoxFlat_method_get_border_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_border_width**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBoxFlat_method_get_border_width>`{.interpreted-text
role="ref"}

Returns the specified `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}\'s border width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_get_border_width_min}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_border_width_min**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBoxFlat_method_get_border_width_min>`{.interpreted-text
role="ref"}

Returns the smallest border width out of all four borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_get_corner_radius}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_corner_radius**(corner:
`Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBoxFlat_method_get_corner_radius>`{.interpreted-text
role="ref"}

Returns the given `corner`\'s radius.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_get_expand_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_expand_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBoxFlat_method_get_expand_margin>`{.interpreted-text
role="ref"}

Returns the size of the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}\'s expand
margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_set_border_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_border_width**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, width:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StyleBoxFlat_method_set_border_width>`{.interpreted-text
role="ref"}

Sets the specified `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}\'s border width to `width` pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_set_border_width_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_border_width_all**(width: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_StyleBoxFlat_method_set_border_width_all>`{.interpreted-text
role="ref"}

Sets the border width to `width` pixels for all sides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_set_corner_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_corner_radius**(corner:
`Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"},
radius: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StyleBoxFlat_method_set_corner_radius>`{.interpreted-text
role="ref"}

Sets the corner radius to `radius` pixels for the given `corner`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_set_corner_radius_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_corner_radius_all**(radius: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_StyleBoxFlat_method_set_corner_radius_all>`{.interpreted-text
role="ref"}

Sets the corner radius to `radius` pixels for all corners.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_set_expand_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_expand_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, size:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StyleBoxFlat_method_set_expand_margin>`{.interpreted-text
role="ref"}

Sets the expand margin to `size` pixels for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxFlat_method_set_expand_margin_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_expand_margin_all**(size: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_StyleBoxFlat_method_set_expand_margin_all>`{.interpreted-text
role="ref"}

Sets the expand margin to `size` pixels for all sides.
