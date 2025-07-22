github_url
:   hide

# VisualShaderNodeTexture3D {#class_VisualShaderNodeTexture3D}

**Inherits:**
`VisualShaderNodeSample3D<class_VisualShaderNodeSample3D>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Performs a 3D texture lookup within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Performs a lookup operation on the provided texture, with support for
multiple texture sources to choose from.

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

:::: {#class_VisualShaderNodeTexture3D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture3D<class_Texture3D>`{.interpreted-text role="ref"} **texture**
`🔗<class_VisualShaderNodeTexture3D_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture3D<class_Texture3D>`{.interpreted-text
  role="ref"})
- `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
  **get_texture**()

A source texture. Used if
`VisualShaderNodeSample3D.source<class_VisualShaderNodeSample3D_property_source>`{.interpreted-text
role="ref"} is set to
`VisualShaderNodeSample3D.SOURCE_TEXTURE<class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE>`{.interpreted-text
role="ref"}.
