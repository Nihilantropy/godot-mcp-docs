github_url
:   hide

# PortableCompressedTexture2D {#class_PortableCompressedTexture2D}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Provides a compressed texture for disk and/or VRAM in a way that is
portable.

::: rst-class
classref-introduction-group
:::

## Description

This class allows storing compressed textures as self contained (not
imported) resources.

For 2D usage (compressed on disk, uncompressed on VRAM), the lossy and
lossless modes are recommended. For 3D usage (compressed on VRAM) it
depends on the target platform.

If you intend to only use desktop, S3TC or BPTC are recommended. For
only mobile, ETC2 is recommended.

For portable, self contained 3D textures that work on both desktop and
mobile, Basis Universal is recommended (although it has a small quality
cost and longer compression time as a tradeoff).

This resource is intended to be created from code.

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

:::: {#enum_PortableCompressedTexture2D_CompressionMode}
::: rst-class
classref-enumeration
:::
::::

enum **CompressionMode**:
`🔗<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"}

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_LOSSLESS}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_LOSSLESS** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_LOSSY}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_LOSSY** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_BASIS_UNIVERSAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_BASIS_UNIVERSAL** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_S3TC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_S3TC** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_ETC2}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_ETC2** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_BPTC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_BPTC** = `5`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_ASTC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_MODE_ASTC** = `6`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PortableCompressedTexture2D_property_keep_compressed_buffer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**keep_compressed_buffer** = `false`
`🔗<class_PortableCompressedTexture2D_property_keep_compressed_buffer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_compressed_buffer**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_keeping_compressed_buffer**()

When running on the editor, this class will keep the source compressed
data in memory. Otherwise, the source compressed data is lost after
loading and the resource can\'t be re saved.

This flag allows to keep the compressed data in memory if you intend it
to persist after loading.

\*\*Note:\*\* This must be set before
`create_from_image()<class_PortableCompressedTexture2D_method_create_from_image>`{.interpreted-text
role="ref"} to take effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PortableCompressedTexture2D_property_size_override}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size_override**
= `Vector2(0, 0)`
`🔗<class_PortableCompressedTexture2D_property_size_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size_override**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_size_override**()

Allow overriding the texture size (for 2D only).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PortableCompressedTexture2D_method_create_from_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_from_image**(image: `Image<class_Image>`{.interpreted-text
role="ref"}, compression_mode:
`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"}, normal_map: `bool<class_bool>`{.interpreted-text
role="ref"} = false, lossy_quality:
`float<class_float>`{.interpreted-text role="ref"} = 0.8)
`🔗<class_PortableCompressedTexture2D_method_create_from_image>`{.interpreted-text
role="ref"}

Initializes the compressed texture from a base image. The compression
mode must be provided.

`normal_map` is recommended to ensure optimum quality if this image will
be used as a normal map.

If lossy compression is requested, the quality setting can optionally be
provided. This maps to Lossy WebP compression quality.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PortableCompressedTexture2D_method_get_compression_mode}
::: rst-class
classref-method
:::
::::

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`{.interpreted-text
role="ref"} **get_compression_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PortableCompressedTexture2D_method_get_compression_mode>`{.interpreted-text
role="ref"}

Return the compression mode used (valid after initialized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PortableCompressedTexture2D_method_get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**get_format**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PortableCompressedTexture2D_method_get_format>`{.interpreted-text
role="ref"}

Return the image format used (valid after initialized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PortableCompressedTexture2D_method_is_keeping_all_compressed_buffers}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_keeping_all_compressed_buffers**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_PortableCompressedTexture2D_method_is_keeping_all_compressed_buffers>`{.interpreted-text
role="ref"}

Return whether the flag is overridden for all textures of this type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PortableCompressedTexture2D_method_set_basisu_compressor_params}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_basisu_compressor_params**(uastc_level:
`int<class_int>`{.interpreted-text role="ref"}, rdo_quality_loss:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PortableCompressedTexture2D_method_set_basisu_compressor_params>`{.interpreted-text
role="ref"}

Sets the compressor parameters for Basis Universal compression. See also
the settings in
`ResourceImporterTexture<class_ResourceImporterTexture>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This must be set before
`create_from_image()<class_PortableCompressedTexture2D_method_create_from_image>`{.interpreted-text
role="ref"} to take effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PortableCompressedTexture2D_method_set_keep_all_compressed_buffers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_keep_all_compressed_buffers**(keep:
`bool<class_bool>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_PortableCompressedTexture2D_method_set_keep_all_compressed_buffers>`{.interpreted-text
role="ref"}

Overrides the flag globally for all textures of this type. This is used
primarily by the editor.
