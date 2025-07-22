github_url
:   hide

# Gradient {#class_Gradient}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A color transition.

::: rst-class
classref-introduction-group
:::

## Description

This resource describes a color transition by defining a set of colored
points and how to interpolate between them.

See also `Curve<class_Curve>`{.interpreted-text role="ref"} which
supports more complex easing methods, but does not support colors.

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

:::: {#enum_Gradient_InterpolationMode}
::: rst-class
classref-enumeration
:::
::::

enum **InterpolationMode**:
`🔗<enum_Gradient_InterpolationMode>`{.interpreted-text role="ref"}

:::: {#class_Gradient_constant_GRADIENT_INTERPOLATE_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationMode<enum_Gradient_InterpolationMode>`{.interpreted-text
role="ref"} **GRADIENT_INTERPOLATE_LINEAR** = `0`

Linear interpolation.

:::: {#class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationMode<enum_Gradient_InterpolationMode>`{.interpreted-text
role="ref"} **GRADIENT_INTERPOLATE_CONSTANT** = `1`

Constant interpolation, color changes abruptly at each point and stays
uniform between. This might cause visible aliasing when used for a
gradient texture in some cases.

:::: {#class_Gradient_constant_GRADIENT_INTERPOLATE_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationMode<enum_Gradient_InterpolationMode>`{.interpreted-text
role="ref"} **GRADIENT_INTERPOLATE_CUBIC** = `2`

Cubic interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Gradient_ColorSpace}
::: rst-class
classref-enumeration
:::
::::

enum **ColorSpace**: `🔗<enum_Gradient_ColorSpace>`{.interpreted-text
role="ref"}

:::: {#class_Gradient_constant_GRADIENT_COLOR_SPACE_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorSpace<enum_Gradient_ColorSpace>`{.interpreted-text role="ref"}
**GRADIENT_COLOR_SPACE_SRGB** = `0`

sRGB color space.

:::: {#class_Gradient_constant_GRADIENT_COLOR_SPACE_LINEAR_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorSpace<enum_Gradient_ColorSpace>`{.interpreted-text role="ref"}
**GRADIENT_COLOR_SPACE_LINEAR_SRGB** = `1`

Linear sRGB color space.

:::: {#class_Gradient_constant_GRADIENT_COLOR_SPACE_OKLAB}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorSpace<enum_Gradient_ColorSpace>`{.interpreted-text role="ref"}
**GRADIENT_COLOR_SPACE_OKLAB** = `2`

[Oklab](https://bottosson.github.io/posts/oklab/) color space. This
color space provides a smooth and uniform-looking transition between
colors.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Gradient_property_colors}
::: rst-class
classref-property
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**colors** = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`
`🔗<class_Gradient_property_colors>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_colors**(value:
  `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"})
- `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"} **get_colors**()

Gradient\'s colors as a
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Setting this property updates all colors at once. To
update any color individually use
`set_color()<class_Gradient_method_set_color>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_property_interpolation_color_space}
::: rst-class
classref-property
:::
::::

`ColorSpace<enum_Gradient_ColorSpace>`{.interpreted-text role="ref"}
**interpolation_color_space** = `0`
`🔗<class_Gradient_property_interpolation_color_space>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interpolation_color_space**(value:
  `ColorSpace<enum_Gradient_ColorSpace>`{.interpreted-text role="ref"})
- `ColorSpace<enum_Gradient_ColorSpace>`{.interpreted-text role="ref"}
  **get_interpolation_color_space**()

The color space used to interpolate between points of the gradient. It
does not affect the returned colors, which will always be in sRGB space.

\*\*Note:\*\* This setting has no effect when
`interpolation_mode<class_Gradient_property_interpolation_mode>`{.interpreted-text
role="ref"} is set to
`GRADIENT_INTERPOLATE_CONSTANT<class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_property_interpolation_mode}
::: rst-class
classref-property
:::
::::

`InterpolationMode<enum_Gradient_InterpolationMode>`{.interpreted-text
role="ref"} **interpolation_mode** = `0`
`🔗<class_Gradient_property_interpolation_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interpolation_mode**(value:
  `InterpolationMode<enum_Gradient_InterpolationMode>`{.interpreted-text
  role="ref"})
- `InterpolationMode<enum_Gradient_InterpolationMode>`{.interpreted-text
  role="ref"} **get_interpolation_mode**()

The algorithm used to interpolate between points of the gradient.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_property_offsets}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **offsets** = `PackedFloat32Array(0, 1)`
`🔗<class_Gradient_property_offsets>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offsets**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_offsets**()

Gradient\'s offsets as a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Setting this property updates all offsets at once. To
update any offset individually use
`set_offset()<class_Gradient_method_set_offset>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Gradient_method_add_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_point**(offset: `float<class_float>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_add_point>`{.interpreted-text role="ref"}

Adds the specified color to the gradient, with the specified offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_get_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **get_color**(point:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_get_color>`{.interpreted-text role="ref"}

Returns the color of the gradient color at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_get_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_offset**(point:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_get_offset>`{.interpreted-text role="ref"}

Returns the offset of the gradient color at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_get_point_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_point_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Gradient_method_get_point_count>`{.interpreted-text
role="ref"}

Returns the number of colors in the gradient.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_remove_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(point: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_remove_point>`{.interpreted-text role="ref"}

Removes the color at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_reverse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_Gradient_method_reverse>`{.interpreted-text role="ref"}

Reverses/mirrors the gradient.

\*\*Note:\*\* This method mirrors all points around the middle of the
gradient, which may produce unexpected results when
`interpolation_mode<class_Gradient_property_interpolation_mode>`{.interpreted-text
role="ref"} is set to
`GRADIENT_INTERPOLATE_CONSTANT<class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_sample}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **sample**(offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_sample>`{.interpreted-text role="ref"}

Returns the interpolated color specified by `offset`. `offset` should be
between `0.0` and `1.0` (inclusive). Using a value lower than `0.0` will
return the same color as `0.0`, and using a value higher than `1.0` will
return the same color as `1.0`. If your input value is not within this
range, consider using
`@GlobalScope.remap()<class_@GlobalScope_method_remap>`{.interpreted-text
role="ref"} on the input value with output values set to `0.0` and
`1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_color**(point: `int<class_int>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_set_color>`{.interpreted-text role="ref"}

Sets the color of the gradient color at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Gradient_method_set_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_offset**(point: `int<class_int>`{.interpreted-text role="ref"},
offset: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Gradient_method_set_offset>`{.interpreted-text role="ref"}

Sets the offset for the gradient color at index `point`.
