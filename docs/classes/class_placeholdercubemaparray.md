github_url
:   hide

# PlaceholderCubemapArray {#class_PlaceholderCubemapArray}

**Inherits:**
`PlaceholderTextureLayered<class_PlaceholderTextureLayered>`{.interpreted-text
role="ref"} **\<**
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `CubemapArray<class_CubemapArray>`{.interpreted-text role="ref"}
without image data.

::: rst-class
classref-introduction-group
:::

## Description

This class replaces a
`CubemapArray<class_CubemapArray>`{.interpreted-text role="ref"} or a
`CubemapArray<class_CubemapArray>`{.interpreted-text role="ref"}-derived
class in 2 conditions:

- In dedicated server mode, where the image data shouldn\'t affect game
  logic. This allows reducing the exported PCK\'s size significantly.
- When the `CubemapArray<class_CubemapArray>`{.interpreted-text
  role="ref"}-derived class is missing, for example when using a
  different engine version.

\*\*Note:\*\* This class is not intended for rendering or for use in
shaders. Operations like calculating UV are not guaranteed to work.
