github_url
:   hide

# MeshInstance2D {#class_MeshInstance2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node used for displaying a `Mesh<class_Mesh>`{.interpreted-text
role="ref"} in 2D.

::: rst-class
classref-introduction-group
:::

## Description

Node used for displaying a `Mesh<class_Mesh>`{.interpreted-text
role="ref"} in 2D. A **MeshInstance2D** can be automatically created
from an existing `Sprite2D<class_Sprite2D>`{.interpreted-text
role="ref"} via a tool in the editor toolbar. Select the
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} node, then
choose **Sprite2D \> Convert to MeshInstance2D** at the top of the 2D
editor viewport.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D meshes <../tutorials/2d/2d_meshes>`{.interpreted-text role="doc"}

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

## Signals

:::: {#class_MeshInstance2D_signal_texture_changed}
::: rst-class
classref-signal
:::
::::

**texture_changed**()
`🔗<class_MeshInstance2D_signal_texture_changed>`{.interpreted-text
role="ref"}

Emitted when the
`texture<class_MeshInstance2D_property_texture>`{.interpreted-text
role="ref"} is changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MeshInstance2D_property_mesh}
::: rst-class
classref-property
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **mesh**
`🔗<class_MeshInstance2D_property_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
- `Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_mesh**()

The `Mesh<class_Mesh>`{.interpreted-text role="ref"} that will be drawn
by the **MeshInstance2D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_MeshInstance2D_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The `Texture2D<class_Texture2D>`{.interpreted-text role="ref"} that will
be used if using the default
`CanvasItemMaterial<class_CanvasItemMaterial>`{.interpreted-text
role="ref"}. Can be accessed as `TEXTURE` in CanvasItem shader.
