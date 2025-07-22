github_url
:   hide

# RDTextureFormat {#class_RDTextureFormat}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Texture format (used by
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

:::: {#class_RDTextureFormat_property_array_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **array_layers** = `1`
`🔗<class_RDTextureFormat_property_array_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_array_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_array_layers**()

The number of layers in the texture. Only relevant for 2D texture
arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_depth}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **depth** = `1`
`🔗<class_RDTextureFormat_property_depth>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_depth**()

The texture\'s depth (in pixels). This is always `1` for 2D textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_format}
::: rst-class
classref-property
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **format** = `8`
`🔗<class_RDTextureFormat_property_format>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_format**(value:
  `DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
  role="ref"})
- `DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
  role="ref"} **get_format**()

The texture\'s pixel data format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **height** = `1`
`🔗<class_RDTextureFormat_property_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_height**()

The texture\'s height (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_is_discardable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_discardable** =
`false`
`🔗<class_RDTextureFormat_property_is_discardable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_is_discardable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_is_discardable**()

If a texture is discardable, its contents do not need to be preserved
between frames. This flag is only relevant when the texture is used as
target in a draw list.

This information is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}
to figure out if a texture\'s contents can be discarded, eliminating
unnecessary writes to memory and boosting performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_is_resolve_buffer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_resolve_buffer** =
`false`
`🔗<class_RDTextureFormat_property_is_resolve_buffer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_is_resolve_buffer**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_is_resolve_buffer**()

The texture will be used as the destination of a resolve operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_mipmaps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mipmaps** = `1`
`🔗<class_RDTextureFormat_property_mipmaps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mipmaps**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_mipmaps**()

The number of mipmaps available in the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_samples}
::: rst-class
classref-property
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **samples** = `0`
`🔗<class_RDTextureFormat_property_samples>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_samples**(value:
  `TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
  role="ref"})
- `TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
  role="ref"} **get_samples**()

The number of samples used when sampling the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_texture_type}
::: rst-class
classref-property
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **texture_type** = `1`
`🔗<class_RDTextureFormat_property_texture_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_type**(value:
  `TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
  role="ref"})
- `TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
  role="ref"} **get_texture_type**()

The texture type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_usage_bits}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"}\] **usage_bits** = `0`
`🔗<class_RDTextureFormat_property_usage_bits>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_usage_bits**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
  role="ref"}\] **get_usage_bits**()

The texture\'s usage bits, which determine what can be done using the
texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_property_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **width** = `1`
`🔗<class_RDTextureFormat_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_width**()

The texture\'s width (in pixels).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RDTextureFormat_method_add_shareable_format}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_shareable_format**(format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"})
`🔗<class_RDTextureFormat_method_add_shareable_format>`{.interpreted-text
role="ref"}

Adds `format` as a valid format for the corresponding
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"}\'s
`RDTextureView.format_override<class_RDTextureView_property_format_override>`{.interpreted-text
role="ref"} property. If any format is added as shareable, then the main
`format<class_RDTextureFormat_property_format>`{.interpreted-text
role="ref"} must also be added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDTextureFormat_method_remove_shareable_format}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_shareable_format**(format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"})
`🔗<class_RDTextureFormat_method_remove_shareable_format>`{.interpreted-text
role="ref"}

Removes `format` from the list of valid formats that the corresponding
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"}\'s
`RDTextureView.format_override<class_RDTextureView_property_format_override>`{.interpreted-text
role="ref"} property can be set to.
