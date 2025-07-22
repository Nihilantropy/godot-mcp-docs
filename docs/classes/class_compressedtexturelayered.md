github_url
:   hide

# CompressedTextureLayered {#class_CompressedTextureLayered}

**Inherits:** `TextureLayered<class_TextureLayered>`{.interpreted-text
role="ref"} **\<** `Texture<class_Texture>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CompressedCubemap<class_CompressedCubemap>`{.interpreted-text
role="ref"},
`CompressedCubemapArray<class_CompressedCubemapArray>`{.interpreted-text
role="ref"},
`CompressedTexture2DArray<class_CompressedTexture2DArray>`{.interpreted-text
role="ref"}

Base class for texture arrays that can optionally be compressed.

::: rst-class
classref-introduction-group
:::

## Description

Base class for
`CompressedTexture2DArray<class_CompressedTexture2DArray>`{.interpreted-text
role="ref"} and
`CompressedTexture3D<class_CompressedTexture3D>`{.interpreted-text
role="ref"}. Cannot be used directly, but contains all the functions
necessary for accessing the derived resource types. See also
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}.

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

:::: {#class_CompressedTextureLayered_property_load_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **load_path** =
`""`
`🔗<class_CompressedTextureLayered_property_load_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
  **load**(path: `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_load_path**()

The path the texture should be loaded from.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CompressedTextureLayered_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CompressedTextureLayered_method_load>`{.interpreted-text
role="ref"}

Loads the texture at `path`.
