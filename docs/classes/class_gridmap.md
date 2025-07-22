github_url
:   hide

::: {.meta keywords="tilemap"}
:::

# GridMap {#class_GridMap}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node for 3D tile-based maps.

::: rst-class
classref-introduction-group
:::

## Description

GridMap lets you place meshes on a grid interactively. It works both
from the editor and from scripts, which can help you create in-game
level editors.

GridMaps use a `MeshLibrary<class_MeshLibrary>`{.interpreted-text
role="ref"} which contains a list of tiles. Each tile is a mesh with
materials plus optional collision and navigation shapes.

A GridMap contains a collection of cells. Each grid cell refers to a
tile in the `MeshLibrary<class_MeshLibrary>`{.interpreted-text
role="ref"}. All cells in the map have the same dimensions.

Internally, a GridMap is split into a sparse collection of octants for
efficient rendering and physics processing. Every octant has the same
dimensions and can contain several cells.

\*\*Note:\*\* GridMap doesn\'t extend
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
and therefore can\'t be hidden or cull masked based on
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"}. If you make a light not affect the first layer, the whole
GridMap won\'t be lit by the light in question.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using gridmaps <../tutorials/3d/using_gridmaps>`{.interpreted-text
  role="doc"}
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [3D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2739)

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

## Signals

:::: {#class_GridMap_signal_cell_size_changed}
::: rst-class
classref-signal
:::
::::

**cell_size_changed**(cell_size:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_GridMap_signal_cell_size_changed>`{.interpreted-text
role="ref"}

Emitted when
`cell_size<class_GridMap_property_cell_size>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_signal_changed}
::: rst-class
classref-signal
:::
::::

**changed**() `🔗<class_GridMap_signal_changed>`{.interpreted-text
role="ref"}

Emitted when the `MeshLibrary<class_MeshLibrary>`{.interpreted-text
role="ref"} of this GridMap changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_GridMap_constant_INVALID_CELL_ITEM}
::: rst-class
classref-constant
:::
::::

**INVALID_CELL_ITEM** = `-1`
`🔗<class_GridMap_constant_INVALID_CELL_ITEM>`{.interpreted-text
role="ref"}

Invalid cell item that can be used in
`set_cell_item()<class_GridMap_method_set_cell_item>`{.interpreted-text
role="ref"} to clear cells (or represent an empty cell in
`get_cell_item()<class_GridMap_method_get_cell_item>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GridMap_property_bake_navigation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **bake_navigation** =
`false` `🔗<class_GridMap_property_bake_navigation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_navigation**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_baking_navigation**()

If `true`, this GridMap creates a navigation region for each cell that
uses a
`mesh_library<class_GridMap_property_mesh_library>`{.interpreted-text
role="ref"} item with a navigation mesh. The created navigation region
will use the navigation layers bitmask assigned to the
`MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"}\'s item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_cell_center_x}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cell_center_x** =
`true` `🔗<class_GridMap_property_cell_center_x>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_x**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_center_x**()

If `true`, grid items are centered on the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_cell_center_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cell_center_y** =
`true` `🔗<class_GridMap_property_cell_center_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_y**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_center_y**()

If `true`, grid items are centered on the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_cell_center_z}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cell_center_z** =
`true` `🔗<class_GridMap_property_cell_center_z>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_z**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_center_z**()

If `true`, grid items are centered on the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_cell_octant_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **cell_octant_size** =
`8` `🔗<class_GridMap_property_cell_octant_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_octant_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_octant_size**()

The size of each octant measured in number of cells. This applies to all
three axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_cell_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cell_scale** =
`1.0` `🔗<class_GridMap_property_cell_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_cell_scale**()

The scale of the cell items.

This does not affect the size of the grid cells themselves, only the
items in them. This can be used to make cell items overlap their
neighbors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_cell_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **cell_size** =
`Vector3(2, 2, 2)`
`🔗<class_GridMap_property_cell_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_cell_size**()

The dimensions of the grid\'s cells.

This does not affect the size of the meshes. See
`cell_scale<class_GridMap_property_cell_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_collision_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_layer** = `1`
`🔗<class_GridMap_property_collision_layer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_layer**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_layer**()

The physics layers this GridMap is in.

GridMaps act as static bodies, meaning they aren\'t affected by gravity
or other forces. They only affect other physics bodies that collide with
them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_GridMap_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The physics layers this GridMap detects collisions in. See [Collision
layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_collision_priority}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**collision_priority** = `1.0`
`🔗<class_GridMap_property_collision_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_priority**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_collision_priority**()

The priority used to solve colliding when occurring penetration. The
higher the priority is, the lower the penetration into the object will
be. This can for example be used to prevent the player from breaking
through the boundaries of a level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_mesh_library}
::: rst-class
classref-property
:::
::::

`MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"}
**mesh_library**
`🔗<class_GridMap_property_mesh_library>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh_library**(value:
  `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"})
- `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"}
  **get_mesh_library**()

The assigned `MeshLibrary<class_MeshLibrary>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_property_physics_material}
::: rst-class
classref-property
:::
::::

`PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"}
**physics_material**
`🔗<class_GridMap_property_physics_material>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_material**(value:
  `PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text
  role="ref"})
- `PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"}
  **get_physics_material**()

Overrides the default friction and bounce physics properties for the
whole **GridMap**.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GridMap_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_GridMap_method_clear>`{.interpreted-text role="ref"}

Clear all cells.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_clear_baked_meshes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_baked_meshes**()
`🔗<class_GridMap_method_clear_baked_meshes>`{.interpreted-text
role="ref"}

Clears all baked meshes. See
`make_baked_meshes()<class_GridMap_method_make_baked_meshes>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_bake_mesh_instance}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_bake_mesh_instance**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GridMap_method_get_bake_mesh_instance>`{.interpreted-text
role="ref"}

Returns `RID<class_RID>`{.interpreted-text role="ref"} of a baked mesh
with the given `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_bake_meshes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_bake_meshes**()
`🔗<class_GridMap_method_get_bake_meshes>`{.interpreted-text role="ref"}

Returns an array of `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"}es and `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} references of all bake meshes that exist within the current
GridMap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_basis_with_orthogonal_index}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**get_basis_with_orthogonal_index**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_basis_with_orthogonal_index>`{.interpreted-text
role="ref"}

Returns one of 24 possible rotations that lie along the vectors (x,y,z)
with each component being either -1, 0, or 1. For further details, refer
to the Godot source code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_cell_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_item**(position: `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GridMap_method_get_cell_item>`{.interpreted-text
role="ref"}

The `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"} item
index located at the given grid coordinates. If the cell is empty,
`INVALID_CELL_ITEM<class_GridMap_constant_INVALID_CELL_ITEM>`{.interpreted-text
role="ref"} will be returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_cell_item_basis}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**get_cell_item_basis**(position:
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_cell_item_basis>`{.interpreted-text
role="ref"}

Returns the basis that gives the specified cell its orientation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_cell_item_orientation}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_item_orientation**(position:
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_cell_item_orientation>`{.interpreted-text
role="ref"}

The orientation of the cell at the given grid coordinates. `-1` is
returned if the cell is empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_collision_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_collision_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_layer<class_GridMap_property_collision_layer>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_mask<class_GridMap_property_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_meshes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_meshes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GridMap_method_get_meshes>`{.interpreted-text
role="ref"}

Returns an array of `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} and `Mesh<class_Mesh>`{.interpreted-text role="ref"}
references corresponding to the non-empty cells in the grid. The
transforms are specified in local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_navigation_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_navigation_map>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map this GridMap node uses for its cell baked navigation
meshes.

This function returns always the map set on the GridMap node and not the
map on the NavigationServer. If the map is changed directly with the
NavigationServer API the GridMap node will not be aware of the map
change.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_orthogonal_index_from_basis}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_orthogonal_index_from_basis**(basis:
`Basis<class_Basis>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_orthogonal_index_from_basis>`{.interpreted-text
role="ref"}

This function considers a discretization of rotations into 24 points on
unit sphere, lying along the vectors (x,y,z) with each component being
either -1, 0, or 1, and returns the index (in the range from 0 to 23) of
the point best representing the orientation of the object. For further
details, refer to the Godot source code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_used_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}\]
**get_used_cells**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GridMap_method_get_used_cells>`{.interpreted-text
role="ref"}

Returns an array of `Vector3<class_Vector3>`{.interpreted-text
role="ref"} with the non-empty cell coordinates in the grid map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_get_used_cells_by_item}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}\]
**get_used_cells_by_item**(item: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMap_method_get_used_cells_by_item>`{.interpreted-text
role="ref"}

Returns an array of all cells with the given item index specified in
`item`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_local_to_map}
::: rst-class
classref-method
:::
::::

`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}
**local_to_map**(local_position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GridMap_method_local_to_map>`{.interpreted-text
role="ref"}

Returns the map coordinates of the cell containing the given
`local_position`. If `local_position` is in global coordinates, consider
using
`Node3D.to_local()<class_Node3D_method_to_local>`{.interpreted-text
role="ref"} before passing it to this method. See also
`map_to_local()<class_GridMap_method_map_to_local>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_make_baked_meshes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_baked_meshes**(gen_lightmap_uv:
`bool<class_bool>`{.interpreted-text role="ref"} = false,
lightmap_uv_texel_size: `float<class_float>`{.interpreted-text
role="ref"} = 0.1)
`🔗<class_GridMap_method_make_baked_meshes>`{.interpreted-text
role="ref"}

Bakes lightmap data for all meshes in the assigned
`MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_map_to_local}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**map_to_local**(map_position:
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GridMap_method_map_to_local>`{.interpreted-text
role="ref"}

Returns the position of a grid cell in the GridMap\'s local coordinate
space. To convert the returned value into global coordinates, use
`Node3D.to_global()<class_Node3D_method_to_global>`{.interpreted-text
role="ref"}. See also
`local_to_map()<class_GridMap_method_local_to_map>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_resource_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resource_changed**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_GridMap_method_resource_changed>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`Resource.changed<class_Resource_signal_changed>`{.interpreted-text
role="ref"} instead.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_set_cell_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell_item**(position: `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"}, item: `int<class_int>`{.interpreted-text role="ref"},
orientation: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_GridMap_method_set_cell_item>`{.interpreted-text role="ref"}

Sets the mesh index for the cell referenced by its grid coordinates.

A negative item index such as
`INVALID_CELL_ITEM<class_GridMap_constant_INVALID_CELL_ITEM>`{.interpreted-text
role="ref"} will clear the cell.

Optionally, the item\'s orientation can be passed. For valid orientation
values, see
`get_orthogonal_index_from_basis()<class_GridMap_method_get_orthogonal_index_from_basis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_set_collision_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GridMap_method_set_collision_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_layer<class_GridMap_property_collision_layer>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_set_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GridMap_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_mask<class_GridMap_property_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMap_method_set_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(navigation_map:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_GridMap_method_set_navigation_map>`{.interpreted-text
role="ref"}

Sets the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map this GridMap node should use for its cell baked
navigation meshes.
