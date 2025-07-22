github_url
:   hide

# CurveTexture {#class_CurveTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 1D texture where pixel brightness corresponds to points on a curve.

::: rst-class
classref-introduction-group
:::

## Description

A 1D texture where pixel brightness corresponds to points on a unit
`Curve<class_Curve>`{.interpreted-text role="ref"} resource, either in
grayscale or in red. This visual representation simplifies the task of
saving curves as image files.

If you need to store up to 3 curves within a single texture, use
`CurveXYZTexture<class_CurveXYZTexture>`{.interpreted-text role="ref"}
instead. See also
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"} and
`GradientTexture2D<class_GradientTexture2D>`{.interpreted-text
role="ref"}.

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

:::: {#enum_CurveTexture_TextureMode}
::: rst-class
classref-enumeration
:::
::::

enum **TextureMode**:
`🔗<enum_CurveTexture_TextureMode>`{.interpreted-text role="ref"}

:::: {#class_CurveTexture_constant_TEXTURE_MODE_RGB}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureMode<enum_CurveTexture_TextureMode>`{.interpreted-text
role="ref"} **TEXTURE_MODE_RGB** = `0`

Store the curve equally across the red, green and blue channels. This
uses more video memory, but is more compatible with shaders that only
read the green and blue values.

:::: {#class_CurveTexture_constant_TEXTURE_MODE_RED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureMode<enum_CurveTexture_TextureMode>`{.interpreted-text
role="ref"} **TEXTURE_MODE_RED** = `1`

Store the curve only in the red channel. This saves video memory, but
some custom shaders may not be able to work with this.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CurveTexture_property_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **curve**
`🔗<class_CurveTexture_property_curve>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve**()

The `Curve<class_Curve>`{.interpreted-text role="ref"} that is rendered
onto the texture. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CurveTexture_property_texture_mode}
::: rst-class
classref-property
:::
::::

`TextureMode<enum_CurveTexture_TextureMode>`{.interpreted-text
role="ref"} **texture_mode** = `0`
`🔗<class_CurveTexture_property_texture_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_mode**(value:
  `TextureMode<enum_CurveTexture_TextureMode>`{.interpreted-text
  role="ref"})
- `TextureMode<enum_CurveTexture_TextureMode>`{.interpreted-text
  role="ref"} **get_texture_mode**()

The format the texture should be generated with. When passing a
CurveTexture as an input to a `Shader<class_Shader>`{.interpreted-text
role="ref"}, this may need to be adjusted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CurveTexture_property_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **width** = `256`
`🔗<class_CurveTexture_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_width**()

The width of the texture (in pixels). Higher values make it possible to
represent high-frequency data better (such as sudden direction changes),
at the cost of increased generation time and memory usage.
