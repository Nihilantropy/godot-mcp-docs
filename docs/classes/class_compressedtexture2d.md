github_url
:   hide

# CompressedTexture2D {#class_CompressedTexture2D}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture with 2 dimensions, optionally compressed.

::: rst-class
classref-introduction-group
:::

## Description

A texture that is loaded from a `.ctex` file. This file format is
internal to Godot; it is created by importing other image formats with
the import system. **CompressedTexture2D** can use one of 4 compression
methods (including a lack of any compression):

- Lossless (WebP or PNG, uncompressed on the GPU)
- Lossy (WebP, uncompressed on the GPU)
- VRAM Compressed (compressed on the GPU)
- VRAM Uncompressed (uncompressed on the GPU)
- Basis Universal (compressed on the GPU. Lower file sizes than VRAM
  Compressed, but slower to compress and lower quality than VRAM
  Compressed)

Only **VRAM Compressed** actually reduces the memory usage on the GPU.
The **Lossless** and **Lossy** compression methods will reduce the
required storage on disk, but they will not reduce memory usage on the
GPU as the texture is sent to the GPU uncompressed.

Using **VRAM Compressed** also improves loading times, as
VRAM-compressed textures are faster to load compared to textures using
lossless or lossy compression. VRAM compression can exhibit noticeable
artifacts and is intended to be used for 3D rendering, not 2D.

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

:::: {#class_CompressedTexture2D_property_load_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **load_path** =
`""`
`🔗<class_CompressedTexture2D_property_load_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
  **load**(path: `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_load_path**()

The **CompressedTexture2D**\'s file path to a `.ctex` file.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CompressedTexture2D_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CompressedTexture2D_method_load>`{.interpreted-text
role="ref"}

Loads the texture from the specified `path`.
