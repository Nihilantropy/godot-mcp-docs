github_url
:   hide

# MeshTexture {#class_MeshTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Simple texture that uses a mesh to draw itself.

::: rst-class
classref-introduction-group
:::

## Description

Simple texture that uses a mesh to draw itself. It\'s limited because
flags can\'t be changed and region drawing is not supported.

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

:::: {#class_MeshTexture_property_base_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**base_texture**
`🔗<class_MeshTexture_property_base_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_base_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_base_texture**()

Sets the base texture that the Mesh will use to draw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshTexture_property_image_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **image_size** =
`Vector2(0, 0)`
`🔗<class_MeshTexture_property_image_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_image_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_image_size**()

Sets the size of the image, needed for reference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshTexture_property_mesh}
::: rst-class
classref-property
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **mesh**
`🔗<class_MeshTexture_property_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
- `Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_mesh**()

Sets the mesh used to draw. It must be a mesh using 2D vertices.
