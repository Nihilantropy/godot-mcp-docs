github_url
:   hide

# Texture2DArray {#class_Texture2DArray}

**Inherits:**
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"} **\<**
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A single texture resource which consists of multiple, separate images.
Each image has the same dimensions and number of mipmap levels.

::: rst-class
classref-introduction-group
:::

## Description

A Texture2DArray is different from a Texture3D: The Texture2DArray does
not support trilinear interpolation between the
`Image<class_Image>`{.interpreted-text role="ref"}s, i.e. no blending.
See also `Cubemap<class_Cubemap>`{.interpreted-text role="ref"} and
`CubemapArray<class_CubemapArray>`{.interpreted-text role="ref"}, which
are texture arrays with specialized cubemap functions.

A Texture2DArray is also different from an
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"}: In a
Texture2DArray, all images are treated separately. In an atlas, the
regions (i.e. the single images) can be of different sizes. Furthermore,
you usually need to add a padding around the regions, to prevent
accidental UV mapping to more than one region. The same goes for
mipmapping: Mipmap chains are handled separately for each layer. In an
atlas, the slicing has to be done manually in the fragment shader.

To create such a texture file yourself, reimport your image files using
the Godot Editor import presets. To create a Texture2DArray from code,
use
`ImageTextureLayered.create_from_images()<class_ImageTextureLayered_method_create_from_images>`{.interpreted-text
role="ref"} on an instance of the Texture2DArray class.

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

## Method Descriptions

:::: {#class_Texture2DArray_method_create_placeholder}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2DArray_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderTexture2DArray<class_PlaceholderTexture2DArray>`{.interpreted-text
role="ref"}).
