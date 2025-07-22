github_url
:   hide

# GradientTexture2D {#class_GradientTexture2D}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D texture that creates a pattern with colors obtained from a
`Gradient<class_Gradient>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A 2D texture that obtains colors from a
`Gradient<class_Gradient>`{.interpreted-text role="ref"} to fill the
texture data. This texture is able to transform a color transition into
different patterns such as a linear or a radial gradient. The texture is
filled by interpolating colors starting from
`fill_from<class_GradientTexture2D_property_fill_from>`{.interpreted-text
role="ref"} to
`fill_to<class_GradientTexture2D_property_fill_to>`{.interpreted-text
role="ref"} offsets by default, but the gradient fill can be repeated to
cover the entire texture.

The gradient is sampled individually for each pixel so it does not
necessarily represent an exact copy of the gradient (see
`width<class_GradientTexture2D_property_width>`{.interpreted-text
role="ref"} and
`height<class_GradientTexture2D_property_height>`{.interpreted-text
role="ref"}). See also
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"}, `CurveTexture<class_CurveTexture>`{.interpreted-text
role="ref"} and
`CurveXYZTexture<class_CurveXYZTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_GradientTexture2D_Fill}
::: rst-class
classref-enumeration
:::
::::

enum **Fill**: `🔗<enum_GradientTexture2D_Fill>`{.interpreted-text
role="ref"}

:::: {#class_GradientTexture2D_constant_FILL_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Fill<enum_GradientTexture2D_Fill>`{.interpreted-text role="ref"}
**FILL_LINEAR** = `0`

The colors are linearly interpolated in a straight line.

:::: {#class_GradientTexture2D_constant_FILL_RADIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Fill<enum_GradientTexture2D_Fill>`{.interpreted-text role="ref"}
**FILL_RADIAL** = `1`

The colors are linearly interpolated in a circular pattern.

:::: {#class_GradientTexture2D_constant_FILL_SQUARE}
::: rst-class
classref-enumeration-constant
:::
::::

`Fill<enum_GradientTexture2D_Fill>`{.interpreted-text role="ref"}
**FILL_SQUARE** = `2`

The colors are linearly interpolated in a square pattern.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_GradientTexture2D_Repeat}
::: rst-class
classref-enumeration
:::
::::

enum **Repeat**: `🔗<enum_GradientTexture2D_Repeat>`{.interpreted-text
role="ref"}

:::: {#class_GradientTexture2D_constant_REPEAT_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Repeat<enum_GradientTexture2D_Repeat>`{.interpreted-text role="ref"}
**REPEAT_NONE** = `0`

The gradient fill is restricted to the range defined by
`fill_from<class_GradientTexture2D_property_fill_from>`{.interpreted-text
role="ref"} to
`fill_to<class_GradientTexture2D_property_fill_to>`{.interpreted-text
role="ref"} offsets.

:::: {#class_GradientTexture2D_constant_REPEAT}
::: rst-class
classref-enumeration-constant
:::
::::

`Repeat<enum_GradientTexture2D_Repeat>`{.interpreted-text role="ref"}
**REPEAT** = `1`

The texture is filled starting from
`fill_from<class_GradientTexture2D_property_fill_from>`{.interpreted-text
role="ref"} to
`fill_to<class_GradientTexture2D_property_fill_to>`{.interpreted-text
role="ref"} offsets, repeating the same pattern in both directions.

:::: {#class_GradientTexture2D_constant_REPEAT_MIRROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Repeat<enum_GradientTexture2D_Repeat>`{.interpreted-text role="ref"}
**REPEAT_MIRROR** = `2`

The texture is filled starting from
`fill_from<class_GradientTexture2D_property_fill_from>`{.interpreted-text
role="ref"} to
`fill_to<class_GradientTexture2D_property_fill_to>`{.interpreted-text
role="ref"} offsets, mirroring the pattern in both directions.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GradientTexture2D_property_fill}
::: rst-class
classref-property
:::
::::

`Fill<enum_GradientTexture2D_Fill>`{.interpreted-text role="ref"}
**fill** = `0`
`🔗<class_GradientTexture2D_property_fill>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fill**(value:
  `Fill<enum_GradientTexture2D_Fill>`{.interpreted-text role="ref"})
- `Fill<enum_GradientTexture2D_Fill>`{.interpreted-text role="ref"}
  **get_fill**()

The gradient\'s fill type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_fill_from}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **fill_from** =
`Vector2(0, 0)`
`🔗<class_GradientTexture2D_property_fill_from>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fill_from**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_fill_from**()

The initial offset used to fill the texture specified in UV coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_fill_to}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **fill_to** =
`Vector2(1, 0)`
`🔗<class_GradientTexture2D_property_fill_to>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fill_to**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_fill_to**()

The final offset used to fill the texture specified in UV coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_gradient}
::: rst-class
classref-property
:::
::::

`Gradient<class_Gradient>`{.interpreted-text role="ref"} **gradient**
`🔗<class_GradientTexture2D_property_gradient>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gradient**(value: `Gradient<class_Gradient>`{.interpreted-text
  role="ref"})
- `Gradient<class_Gradient>`{.interpreted-text role="ref"}
  **get_gradient**()

The `Gradient<class_Gradient>`{.interpreted-text role="ref"} used to
fill the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **height** = `64`
`🔗<class_GradientTexture2D_property_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_height**()

The number of vertical color samples that will be obtained from the
`Gradient<class_Gradient>`{.interpreted-text role="ref"}, which also
represents the texture\'s height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_repeat}
::: rst-class
classref-property
:::
::::

`Repeat<enum_GradientTexture2D_Repeat>`{.interpreted-text role="ref"}
**repeat** = `0`
`🔗<class_GradientTexture2D_property_repeat>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_repeat**(value:
  `Repeat<enum_GradientTexture2D_Repeat>`{.interpreted-text role="ref"})
- `Repeat<enum_GradientTexture2D_Repeat>`{.interpreted-text role="ref"}
  **get_repeat**()

The gradient\'s repeat type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_use_hdr}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_hdr** = `false`
`🔗<class_GradientTexture2D_property_use_hdr>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_hdr**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_hdr**()

If `true`, the generated texture will support high dynamic range
(`Image.FORMAT_RGBAF<class_Image_constant_FORMAT_RGBAF>`{.interpreted-text
role="ref"} format). This allows for glow effects to work if
`Environment.glow_enabled<class_Environment_property_glow_enabled>`{.interpreted-text
role="ref"} is `true`. If `false`, the generated texture will use low
dynamic range; overbright colors will be clamped
(`Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>`{.interpreted-text
role="ref"} format).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GradientTexture2D_property_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **width** = `64`
`🔗<class_GradientTexture2D_property_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_width**()

The number of horizontal color samples that will be obtained from the
`Gradient<class_Gradient>`{.interpreted-text role="ref"}, which also
represents the texture\'s width.
