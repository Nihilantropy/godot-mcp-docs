github_url
:   hide

# Texture3DRD {#class_Texture3DRD}

**Inherits:** `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture for 3D that is bound to a texture created on the
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This texture class allows you to use a 3D texture created directly on
the `RenderingDevice<class_RenderingDevice>`{.interpreted-text
role="ref"} as a texture for materials, meshes, etc.

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

:::: {#class_Texture3DRD_property_texture_rd_rid}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **texture_rd_rid**
`🔗<class_Texture3DRD_property_texture_rd_rid>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_rd_rid**(value: `RID<class_RID>`{.interpreted-text
  role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"}
  **get_texture_rd_rid**()

The RID of the texture object created on the
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.
