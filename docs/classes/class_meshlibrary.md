github_url
:   hide

# MeshLibrary {#class_MeshLibrary}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Library of meshes.

::: rst-class
classref-introduction-group
:::

## Description

A library of meshes. Contains a list of
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resources, each with a
name and ID. Each item can also include collision and navigation shapes.
This resource is used in `GridMap<class_GridMap>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)

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

:::: {#class_MeshLibrary_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_MeshLibrary_method_clear>`{.interpreted-text role="ref"}

Clears the library.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_create_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_item**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_create_item>`{.interpreted-text role="ref"}

Creates a new item in the library with the given ID.

You can get an unused ID from
`get_last_unused_item_id()<class_MeshLibrary_method_get_last_unused_item_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_find_item_by_name}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**find_item_by_name**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_find_item_by_name>`{.interpreted-text
role="ref"}

Returns the first item with the given name, or `-1` if no item is found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_list}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_item_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_list>`{.interpreted-text
role="ref"}

Returns the list of item IDs in use.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_mesh}
::: rst-class
classref-method
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_item_mesh**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_mesh>`{.interpreted-text
role="ref"}

Returns the item\'s mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_mesh_cast_shadow}
::: rst-class
classref-method
:::
::::

`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"} **get_item_mesh_cast_shadow**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_mesh_cast_shadow>`{.interpreted-text
role="ref"}

Returns the item\'s shadow casting mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_mesh_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_item_mesh_transform**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_mesh_transform>`{.interpreted-text
role="ref"}

Returns the transform applied to the item\'s mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_name**(id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_name>`{.interpreted-text
role="ref"}

Returns the item\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_navigation_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_navigation_layers**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_navigation_layers>`{.interpreted-text
role="ref"}

Returns the item\'s navigation layers bitmask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_navigation_mesh}
::: rst-class
classref-method
:::
::::

`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
**get_item_navigation_mesh**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_navigation_mesh>`{.interpreted-text
role="ref"}

Returns the item\'s navigation mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_navigation_mesh_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_item_navigation_mesh_transform**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_navigation_mesh_transform>`{.interpreted-text
role="ref"}

Returns the transform applied to the item\'s navigation mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_preview}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_item_preview**(id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_preview>`{.interpreted-text
role="ref"}

When running in the editor, returns a generated item preview (a 3D
rendering in isometric perspective). When used in a running project,
returns the manually-defined item preview which can be set using
`set_item_preview()<class_MeshLibrary_method_set_item_preview>`{.interpreted-text
role="ref"}. Returns an empty
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} if no preview
was manually set in a running project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_item_shapes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_item_shapes**(id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_item_shapes>`{.interpreted-text
role="ref"}

Returns an item\'s collision shapes.

The array consists of each `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"} followed by its
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_get_last_unused_item_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_last_unused_item_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshLibrary_method_get_last_unused_item_id>`{.interpreted-text
role="ref"}

Gets an unused ID for a new item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_remove_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_item**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_remove_item>`{.interpreted-text role="ref"}

Removes the item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_mesh**(id: `int<class_int>`{.interpreted-text role="ref"},
mesh: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_mesh>`{.interpreted-text
role="ref"}

Sets the item\'s mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_mesh_cast_shadow}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_mesh_cast_shadow**(id: `int<class_int>`{.interpreted-text
role="ref"}, shadow_casting_setting:
`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"})
`🔗<class_MeshLibrary_method_set_item_mesh_cast_shadow>`{.interpreted-text
role="ref"}

Sets the item\'s shadow casting mode to `shadow_casting_setting`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_mesh_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_mesh_transform**(id: `int<class_int>`{.interpreted-text
role="ref"}, mesh_transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_mesh_transform>`{.interpreted-text
role="ref"}

Sets the transform to apply to the item\'s mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_name**(id: `int<class_int>`{.interpreted-text role="ref"},
name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_name>`{.interpreted-text
role="ref"}

Sets the item\'s name.

This name is shown in the editor. It can also be used to look up the
item later using
`find_item_by_name()<class_MeshLibrary_method_find_item_by_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_navigation_layers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_navigation_layers**(id: `int<class_int>`{.interpreted-text
role="ref"}, navigation_layers: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_MeshLibrary_method_set_item_navigation_layers>`{.interpreted-text
role="ref"}

Sets the item\'s navigation layers bitmask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_navigation_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_navigation_mesh**(id: `int<class_int>`{.interpreted-text
role="ref"}, navigation_mesh:
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_navigation_mesh>`{.interpreted-text
role="ref"}

Sets the item\'s navigation mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_navigation_mesh_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_navigation_mesh_transform**(id:
`int<class_int>`{.interpreted-text role="ref"}, navigation_mesh:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_navigation_mesh_transform>`{.interpreted-text
role="ref"}

Sets the transform to apply to the item\'s navigation mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_preview}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_preview**(id: `int<class_int>`{.interpreted-text role="ref"},
texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_preview>`{.interpreted-text
role="ref"}

Sets a texture to use as the item\'s preview icon in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshLibrary_method_set_item_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_shapes**(id: `int<class_int>`{.interpreted-text role="ref"},
shapes: `Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_MeshLibrary_method_set_item_shapes>`{.interpreted-text
role="ref"}

Sets an item\'s collision shapes.

The array should consist of `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"} objects, each followed by a
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} that will
be applied to it. For shapes that should not have a transform, use
`Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>`{.interpreted-text
role="ref"}.
