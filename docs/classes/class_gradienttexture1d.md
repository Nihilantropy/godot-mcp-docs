github_url
:   hide

# GradientTexture1D {#class_GradientTexture1D}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 1D texture that uses colors obtained from a
`Gradient<class_Gradient>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A 1D texture that obtains colors from a
`Gradient<class_Gradient>`{.interpreted-text role="ref"} to fill the
texture data. The texture is filled by sampling the gradient for each
pixel. Therefore, the texture does not necessarily represent an exact
copy of the gradient, as it may miss some colors if there are not enough
pixels. See also
`GradientTexture2D<class_GradientTexture2D>`{.interpreted-text
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

## Property Descriptions

:::: {#class_GradientTexture1D_property_gradient}
::: rst-class
classref-property
:::
::::

`Gradient<class_Gradient>`{.interpreted-text role="ref"} **gradient**
`🔗<class_GradientTexture1D_property_gradient>`{.interpreted-text
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

:::: {#class_GradientTexture1D_property_use_hdr}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_hdr** = `false`
`🔗<class_GradientTexture1D_property_use_hdr>`{.interpreted-text
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

:::: {#class_GradientTexture1D_property_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **width** = `256`
`🔗<class_GradientTexture1D_property_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_width**()

The number of color samples that will be obtained from the
`Gradient<class_Gradient>`{.interpreted-text role="ref"}.
