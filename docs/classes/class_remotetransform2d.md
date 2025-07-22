github_url
:   hide

# RemoteTransform2D {#class_RemoteTransform2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

RemoteTransform2D pushes its own
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} to
another `Node2D<class_Node2D>`{.interpreted-text role="ref"} derived
node in the scene.

::: rst-class
classref-introduction-group
:::

## Description

RemoteTransform2D pushes its own
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} to
another `Node2D<class_Node2D>`{.interpreted-text role="ref"} derived
node (called the remote node) in the scene.

It can be set to update another node\'s position, rotation and/or scale.
It can use either global or local coordinates.

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

:::: {#class_RemoteTransform2D_property_remote_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **remote_path**
= `NodePath("")`
`🔗<class_RemoteTransform2D_property_remote_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_remote_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_remote_node**()

The `NodePath<class_NodePath>`{.interpreted-text role="ref"} to the
remote node, relative to the RemoteTransform2D\'s position in the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RemoteTransform2D_property_update_position}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **update_position** =
`true`
`🔗<class_RemoteTransform2D_property_update_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_position**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_update_position**()

If `true`, the remote node\'s position is updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RemoteTransform2D_property_update_rotation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **update_rotation** =
`true`
`🔗<class_RemoteTransform2D_property_update_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_rotation**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_update_rotation**()

If `true`, the remote node\'s rotation is updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RemoteTransform2D_property_update_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **update_scale** =
`true`
`🔗<class_RemoteTransform2D_property_update_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_scale**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_update_scale**()

If `true`, the remote node\'s scale is updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RemoteTransform2D_property_use_global_coordinates}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_global_coordinates** = `true`
`🔗<class_RemoteTransform2D_property_use_global_coordinates>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_global_coordinates**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_global_coordinates**()

If `true`, global coordinates are used. If `false`, local coordinates
are used.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RemoteTransform2D_method_force_update_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_cache**()
`🔗<class_RemoteTransform2D_method_force_update_cache>`{.interpreted-text
role="ref"}

**RemoteTransform2D** caches the remote node. It may not notice if the
remote node disappears;
`force_update_cache()<class_RemoteTransform2D_method_force_update_cache>`{.interpreted-text
role="ref"} forces it to update the cache again.
