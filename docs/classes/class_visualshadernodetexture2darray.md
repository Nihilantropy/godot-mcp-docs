github_url
:   hide

# VisualShaderNodeTexture2DArray {#class_VisualShaderNodeTexture2DArray}

**Inherits:**
`VisualShaderNodeSample3D<class_VisualShaderNodeSample3D>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D texture uniform array to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translated to `uniform sampler2DArray` in the shader language.

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

:::: {#class_VisualShaderNodeTexture2DArray_property_texture_array}
::: rst-class
classref-property
:::
::::

`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**texture_array**
`🔗<class_VisualShaderNodeTexture2DArray_property_texture_array>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_array**(value:
  `TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"})
- `TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
  **get_texture_array**()

A source texture array. Used if
`VisualShaderNodeSample3D.source<class_VisualShaderNodeSample3D_property_source>`{.interpreted-text
role="ref"} is set to
`VisualShaderNodeSample3D.SOURCE_TEXTURE<class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE>`{.interpreted-text
role="ref"}.
