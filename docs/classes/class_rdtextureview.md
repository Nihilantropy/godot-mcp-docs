github_url
:   hide

# RDTextureView {#class_RDTextureView}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Texture view (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

This object is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

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

:::: {#class_RDTextureView_property_format_override}
::: rst-class
classref-property
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **format_override** = `232`
`🔗<class_RDTextureView_property_format_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_format_override**(value:
  `DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
  role="ref"})
- `DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
  role="ref"} **get_format_override**()

Optional override for the data format to return sampled values in. The
corresponding `RDTextureFormat<class_RDTextureFormat>`{.interpreted-text
role="ref"} must have had this added as a shareable format. The default
value of
`RenderingDevice.DATA_FORMAT_MAX<class_RenderingDevice_constant_DATA_FORMAT_MAX>`{.interpreted-text
role="ref"} does not override the format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureView_property_swizzle_a}
::: rst-class
classref-property
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **swizzle_a** = `6`
`🔗<class_RDTextureView_property_swizzle_a>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_swizzle_a**(value:
  `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"})
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"} **get_swizzle_a**()

The channel to sample when sampling the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureView_property_swizzle_b}
::: rst-class
classref-property
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **swizzle_b** = `5`
`🔗<class_RDTextureView_property_swizzle_b>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_swizzle_b**(value:
  `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"})
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"} **get_swizzle_b**()

The channel to sample when sampling the blue color channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureView_property_swizzle_g}
::: rst-class
classref-property
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **swizzle_g** = `4`
`🔗<class_RDTextureView_property_swizzle_g>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_swizzle_g**(value:
  `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"})
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"} **get_swizzle_g**()

The channel to sample when sampling the green color channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureView_property_swizzle_r}
::: rst-class
classref-property
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **swizzle_r** = `3`
`🔗<class_RDTextureView_property_swizzle_r>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_swizzle_r**(value:
  `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"})
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
  role="ref"} **get_swizzle_r**()

The channel to sample when sampling the red color channel.
