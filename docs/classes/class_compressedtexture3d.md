github_url
:   hide

# CompressedTexture3D {#class_CompressedTexture3D}

**Inherits:** `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture with 3 dimensions, optionally compressed.

::: rst-class
classref-introduction-group
:::

## Description

**CompressedTexture3D** is the VRAM-compressed counterpart of
`ImageTexture3D<class_ImageTexture3D>`{.interpreted-text role="ref"}.
The file extension for **CompressedTexture3D** files is `.ctex3d`. This
file format is internal to Godot; it is created by importing other image
formats with the import system.

\*\*CompressedTexture3D\*\* uses VRAM compression, which allows to
reduce memory usage on the GPU when rendering the texture. This also
improves loading times, as VRAM-compressed textures are faster to load
compared to textures using lossless compression. VRAM compression can
exhibit noticeable artifacts and is intended to be used for 3D
rendering, not 2D.

See `Texture3D<class_Texture3D>`{.interpreted-text role="ref"} for a
general description of 3D textures.

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

:::: {#class_CompressedTexture3D_property_load_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **load_path** =
`""`
`🔗<class_CompressedTexture3D_property_load_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
  **load**(path: `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_load_path**()

The **CompressedTexture3D**\'s file path to a `.ctex3d` file.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CompressedTexture3D_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CompressedTexture3D_method_load>`{.interpreted-text
role="ref"}

Loads the texture from the specified `path`.
