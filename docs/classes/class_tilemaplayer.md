github_url
:   hide

# TileMapLayer {#class_TileMapLayer}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node for 2D tile-based maps.

::: rst-class
classref-introduction-group
:::

## Description

Node for 2D tile-based maps. A **TileMapLayer** uses a
`TileSet<class_TileSet>`{.interpreted-text role="ref"} which contain a
list of tiles which are used to create grid-based maps. Unlike the
`TileMap<class_TileMap>`{.interpreted-text role="ref"} node, which is
deprecated, **TileMapLayer** has only one layer of tiles. You can use
several **TileMapLayer** to achieve the same result as a
`TileMap<class_TileMap>`{.interpreted-text role="ref"} node.

For performance reasons, all TileMap updates are batched at the end of a
frame. Notably, this means that scene tiles from a
`TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
role="ref"} are initialized after their parent. This is only queued when
inside the scene tree.

To force an update earlier on, call
`update_internals()<class_TileMapLayer_method_update_internals>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For performance and compatibility reasons, the coordinates
serialized by **TileMapLayer** are limited to 16-bit signed integers,
i.e. the range for X and Y coordinates is from `-32768` to `32767`. When
saving tile data, tiles outside this range are wrapped.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Tilemaps <../tutorials/2d/using_tilemaps>`{.interpreted-text
  role="doc"}
- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)
- [2D Isometric Demo](https://godotengine.org/asset-library/asset/2718)
- [2D Hexagonal Demo](https://godotengine.org/asset-library/asset/2717)
- [2D Grid-based Navigation with AStarGrid2D
  Demo](https://godotengine.org/asset-library/asset/2723)
- [2D Role Playing Game (RPG)
  Demo](https://godotengine.org/asset-library/asset/2729)
- [2D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2719)
- [2D Dynamic TileMap Layers
  Demo](https://godotengine.org/asset-library/asset/2713)

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

:::: {#class_TileMapLayer_signal_changed}
::: rst-class
classref-signal
:::
::::

**changed**() `🔗<class_TileMapLayer_signal_changed>`{.interpreted-text
role="ref"}

Emitted when this **TileMapLayer**\'s properties changes. This includes
modified cells, properties, or changes made to its assigned
`TileSet<class_TileSet>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This signal may be emitted very often when batch-modifying
a **TileMapLayer**. Avoid executing complex processing in a connected
function, and consider delaying it to the end of the frame instead (i.e.
calling
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_TileMapLayer_DebugVisibilityMode}
::: rst-class
classref-enumeration
:::
::::

enum **DebugVisibilityMode**:
`🔗<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
role="ref"}

:::: {#class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
role="ref"} **DEBUG_VISIBILITY_MODE_DEFAULT** = `0`

Hide the collisions or navigation debug shapes in the editor, and use
the debug settings to determine their visibility in game (i.e.
`SceneTree.debug_collisions_hint<class_SceneTree_property_debug_collisions_hint>`{.interpreted-text
role="ref"} or
`SceneTree.debug_navigation_hint<class_SceneTree_property_debug_navigation_hint>`{.interpreted-text
role="ref"}).

:::: {#class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_FORCE_HIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
role="ref"} **DEBUG_VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide the collisions or navigation debug shapes.

:::: {#class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_FORCE_SHOW}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
role="ref"} **DEBUG_VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show the collisions or navigation debug shapes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TileMapLayer_property_collision_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collision_enabled** =
`true`
`🔗<class_TileMapLayer_property_collision_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collision_enabled**()

Enable or disable collisions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_collision_visibility_mode}
::: rst-class
classref-property
:::
::::

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
role="ref"} **collision_visibility_mode** = `0`
`🔗<class_TileMapLayer_property_collision_visibility_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_visibility_mode**(value:
  `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
  role="ref"})
- `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
  role="ref"} **get_collision_visibility_mode**()

Show or hide the **TileMapLayer**\'s collision shapes. If set to
`DEBUG_VISIBILITY_MODE_DEFAULT<class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT>`{.interpreted-text
role="ref"}, this depends on the show collision debug settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_TileMapLayer_property_enabled>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

If `false`, disables this **TileMapLayer** completely (rendering,
collision, navigation, scene tiles, etc.)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_navigation_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **navigation_enabled**
= `true`
`🔗<class_TileMapLayer_property_navigation_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_navigation_enabled**()

If `true`, navigation regions are enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_navigation_visibility_mode}
::: rst-class
classref-property
:::
::::

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
role="ref"} **navigation_visibility_mode** = `0`
`🔗<class_TileMapLayer_property_navigation_visibility_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_visibility_mode**(value:
  `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
  role="ref"})
- `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`{.interpreted-text
  role="ref"} **get_navigation_visibility_mode**()

Show or hide the **TileMapLayer**\'s navigation meshes. If set to
`DEBUG_VISIBILITY_MODE_DEFAULT<class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT>`{.interpreted-text
role="ref"}, this depends on the show navigation debug settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_occlusion_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **occlusion_enabled** =
`true`
`🔗<class_TileMapLayer_property_occlusion_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_occlusion_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_occlusion_enabled**()

Enable or disable light occlusion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_physics_quadrant_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **physics_quadrant_size**
= `16`
`🔗<class_TileMapLayer_property_physics_quadrant_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_quadrant_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_physics_quadrant_size**()

The **TileMapLayer**\'s physics quadrant size. Within a physics
quadrant, cells with similar physics properties are grouped together and
their collision shapes get merged.
`physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>`{.interpreted-text
role="ref"} defines the length of a square\'s side, in the map\'s
coordinate system, that forms the quadrant. Thus, the default quadrant
size groups together `16 * 16 = 256` tiles.

\*\*Note:\*\* As quadrants are created according to the map\'s
coordinate system, the quadrant\'s \"square shape\" might not look like
square in the **TileMapLayer**\'s local coordinate system.

\*\*Note:\*\* This impacts the value returned by
`get_coords_for_body_rid()<class_TileMapLayer_method_get_coords_for_body_rid>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_rendering_quadrant_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering_quadrant_size** = `16`
`🔗<class_TileMapLayer_property_rendering_quadrant_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rendering_quadrant_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_rendering_quadrant_size**()

The **TileMapLayer**\'s rendering quadrant size. A quadrant is a group
of tiles to be drawn together on a single canvas item, for optimization
purposes.
`rendering_quadrant_size<class_TileMapLayer_property_rendering_quadrant_size>`{.interpreted-text
role="ref"} defines the length of a square\'s side, in the map\'s
coordinate system, that forms the quadrant. Thus, the default quadrant
size groups together `16 * 16 = 256` tiles.

The quadrant size does not apply on a Y-sorted **TileMapLayer**, as
tiles are grouped by Y position instead in that case.

\*\*Note:\*\* As quadrants are created according to the map\'s
coordinate system, the quadrant\'s \"square shape\" might not look like
square in the **TileMapLayer**\'s local coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_tile_map_data}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**tile_map_data** = `PackedByteArray()`
`🔗<class_TileMapLayer_property_tile_map_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tile_map_data_from_array**(value:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_tile_map_data_as_array**()

The raw tile map data as a byte array.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_tile_set}
::: rst-class
classref-property
:::
::::

`TileSet<class_TileSet>`{.interpreted-text role="ref"} **tile_set**
`🔗<class_TileMapLayer_property_tile_set>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tile_set**(value: `TileSet<class_TileSet>`{.interpreted-text
  role="ref"})
- `TileSet<class_TileSet>`{.interpreted-text role="ref"}
  **get_tile_set**()

The `TileSet<class_TileSet>`{.interpreted-text role="ref"} used by this
layer. The textures, collisions, and additional behavior of all
available tiles are stored here.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_use_kinematic_bodies}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_kinematic_bodies** = `false`
`🔗<class_TileMapLayer_property_use_kinematic_bodies>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_kinematic_bodies**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_kinematic_bodies**()

If `true`, this **TileMapLayer** collision shapes will be instantiated
as kinematic bodies. This can be needed for moving **TileMapLayer**
nodes (i.e. moving platforms).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_x_draw_order_reversed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**x_draw_order_reversed** = `false`
`🔗<class_TileMapLayer_property_x_draw_order_reversed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_x_draw_order_reversed**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_x_draw_order_reversed**()

If
`CanvasItem.y_sort_enabled<class_CanvasItem_property_y_sort_enabled>`{.interpreted-text
role="ref"} is enabled, setting this to `true` will reverse the order
the tiles are drawn on the X-axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_property_y_sort_origin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **y_sort_origin** = `0`
`🔗<class_TileMapLayer_property_y_sort_origin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_y_sort_origin**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_y_sort_origin**()

This Y-sort origin value is added to each tile\'s Y-sort origin value.
This allows, for example, to fake a different height level. This can be
useful for top-down view games.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TileMapLayer_private_method__tile_data_runtime_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_tile_data_runtime_update**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, tile_data:
`TileData<class_TileData>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_private_method__tile_data_runtime_update>`{.interpreted-text
role="ref"}

Called with a `TileData<class_TileData>`{.interpreted-text role="ref"}
object about to be used internally by the **TileMapLayer**, allowing its
modification at runtime.

This method is only called if
`_use_tile_data_runtime_update()<class_TileMapLayer_private_method__use_tile_data_runtime_update>`{.interpreted-text
role="ref"} is implemented and returns `true` for the given tile
`coords`.

\*\*Warning:\*\* The `tile_data` object\'s sub-resources are the same as
the one in the TileSet. Modifying them might impact the whole TileSet.
Instead, make sure to duplicate those resources.

\*\*Note:\*\* If the properties of `tile_data` object should change over
time, use
`notify_runtime_tile_data_update()<class_TileMapLayer_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"} to notify the **TileMapLayer** it needs an update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_private_method__update_cells}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_update_cells**(coords: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\],
forced_cleanup: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_private_method__update_cells>`{.interpreted-text
role="ref"}

Called when this **TileMapLayer**\'s cells need an internal update. This
update may be caused from individual cells being modified or by a change
in the
`tile_set<class_TileMapLayer_property_tile_set>`{.interpreted-text
role="ref"} (causing all cells to be queued for an update). The first
call to this function is always for initializing all the
**TileMapLayer**\'s cells. `coords` contains the coordinates of all
modified cells, roughly in the order they were modified.
`forced_cleanup` is `true` when the **TileMapLayer**\'s internals should
be fully cleaned up. This is the case when:

- The layer is disabled;
- The layer is not visible;
- `tile_set<class_TileMapLayer_property_tile_set>`{.interpreted-text
  role="ref"} is set to `null`;
- The node is removed from the tree;
- The node is freed.

Note that any internal update happening while one of these conditions is
verified is considered to be a \"cleanup\". See also
`update_internals()<class_TileMapLayer_method_update_internals>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* Implementing this method may degrade the
**TileMapLayer**\'s performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_private_method__use_tile_data_runtime_update}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_use_tile_data_runtime_update**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_private_method__use_tile_data_runtime_update>`{.interpreted-text
role="ref"}

Should return `true` if the tile at coordinates `coords` requires a
runtime update.

\*\*Warning:\*\* Make sure this function only returns `true` when
needed. Any tile processed at runtime without a need for it will imply a
significant performance penalty.

\*\*Note:\*\* If the result of this function should change, use
`notify_runtime_tile_data_update()<class_TileMapLayer_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"} to notify the **TileMapLayer** it needs an update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_TileMapLayer_method_clear>`{.interpreted-text role="ref"}

Clears all cells.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_erase_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_cell**(coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_TileMapLayer_method_erase_cell>`{.interpreted-text role="ref"}

Erases the cell at coordinates `coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_fix_invalid_tiles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fix_invalid_tiles**()
`🔗<class_TileMapLayer_method_fix_invalid_tiles>`{.interpreted-text
role="ref"}

Clears cells containing tiles that do not exist in the
`tile_set<class_TileMapLayer_property_tile_set>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_cell_alternative_tile}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_alternative_tile**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_cell_alternative_tile>`{.interpreted-text
role="ref"}

Returns the tile alternative ID of the cell at coordinates `coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_cell_atlas_coords}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_cell_atlas_coords**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_cell_atlas_coords>`{.interpreted-text
role="ref"}

Returns the tile atlas coordinates ID of the cell at coordinates
`coords`. Returns `Vector2i(-1, -1)` if the cell does not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_cell_source_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_source_id**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_cell_source_id>`{.interpreted-text
role="ref"}

Returns the tile source ID of the cell at coordinates `coords`. Returns
`-1` if the cell does not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_cell_tile_data}
::: rst-class
classref-method
:::
::::

`TileData<class_TileData>`{.interpreted-text role="ref"}
**get_cell_tile_data**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_cell_tile_data>`{.interpreted-text
role="ref"}

Returns the `TileData<class_TileData>`{.interpreted-text role="ref"}
object associated with the given cell, or `null` if the cell does not
exist or is not a
`TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"}.

    func get_clicked_tile_power():
        var clicked_cell = tile_map_layer.local_to_map(tile_map_layer.get_local_mouse_position())
        var data = tile_map_layer.get_cell_tile_data(clicked_cell)
        if data:
            return data.get_custom_data("power")
        else:
            return 0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_coords_for_body_rid}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_coords_for_body_rid**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_coords_for_body_rid>`{.interpreted-text
role="ref"}

Returns the coordinates of the physics quadrant (see
`physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>`{.interpreted-text
role="ref"}) for given physics body `RID<class_RID>`{.interpreted-text
role="ref"}. Such an `RID<class_RID>`{.interpreted-text role="ref"} can
be retrieved from
`KinematicCollision2D.get_collider_rid()<class_KinematicCollision2D_method_get_collider_rid>`{.interpreted-text
role="ref"}, when colliding with a tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_navigation_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_navigation_map>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} navigation used by this **TileMapLayer**.

By default this returns the default
`World2D<class_World2D>`{.interpreted-text role="ref"} navigation map,
unless a custom map was provided using
`set_navigation_map()<class_TileMapLayer_method_set_navigation_map>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_neighbor_cell}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_neighbor_cell**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, neighbor:
`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_neighbor_cell>`{.interpreted-text
role="ref"}

Returns the neighboring cell to the one at coordinates `coords`,
identified by the `neighbor` direction. This method takes into account
the different layouts a TileMap can take.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_pattern}
::: rst-class
classref-method
:::
::::

`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"}
**get_pattern**(coords_array: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\])
`🔗<class_TileMapLayer_method_get_pattern>`{.interpreted-text
role="ref"}

Creates and returns a new
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"}
from the given array of cells. See also
`set_pattern()<class_TileMapLayer_method_set_pattern>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_surrounding_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_surrounding_cells**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileMapLayer_method_get_surrounding_cells>`{.interpreted-text
role="ref"}

Returns the list of all neighboring cells to the one at `coords`. Any
neighboring cell is one that is touching edges, so for a square cell 4
cells would be returned, for a hexagon 6 cells are returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_used_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_used_cells**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_used_cells>`{.interpreted-text
role="ref"}

Returns a `Vector2i<class_Vector2i>`{.interpreted-text role="ref"} array
with the positions of all cells containing a tile. A cell is considered
empty if its source identifier equals `-1`, its atlas coordinate
identifier is `Vector2(-1, -1)` and its alternative identifier is `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_used_cells_by_id}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_used_cells_by_id**(source_id: `int<class_int>`{.interpreted-text
role="ref"} = -1, atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(-1,
-1), alternative_tile: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_used_cells_by_id>`{.interpreted-text
role="ref"}

Returns a `Vector2i<class_Vector2i>`{.interpreted-text role="ref"} array
with the positions of all cells containing a tile. Tiles may be filtered
according to their source (`source_id`), their atlas coordinates
(`atlas_coords`), or alternative id (`alternative_tile`).

If a parameter has its value set to the default one, this parameter is
not used to filter a cell. Thus, if all parameters have their respective
default values, this method returns the same result as
`get_used_cells()<class_TileMapLayer_method_get_used_cells>`{.interpreted-text
role="ref"}.

A cell is considered empty if its source identifier equals `-1`, its
atlas coordinate identifier is `Vector2(-1, -1)` and its alternative
identifier is `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_get_used_rect}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **get_used_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_get_used_rect>`{.interpreted-text
role="ref"}

Returns a rectangle enclosing the used (non-empty) tiles of the map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_has_body_rid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_body_rid**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_has_body_rid>`{.interpreted-text
role="ref"}

Returns whether the provided `body` `RID<class_RID>`{.interpreted-text
role="ref"} belongs to one of this **TileMapLayer**\'s cells.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_is_cell_flipped_h}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_cell_flipped_h**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_is_cell_flipped_h>`{.interpreted-text
role="ref"}

Returns `true` if the cell at coordinates `coords` is flipped
horizontally. The result is valid only for atlas sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_is_cell_flipped_v}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_cell_flipped_v**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_is_cell_flipped_v>`{.interpreted-text
role="ref"}

Returns `true` if the cell at coordinates `coords` is flipped
vertically. The result is valid only for atlas sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_is_cell_transposed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_cell_transposed**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_is_cell_transposed>`{.interpreted-text
role="ref"}

Returns `true` if the cell at coordinates `coords` is transposed. The
result is valid only for atlas sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_local_to_map}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**local_to_map**(local_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_local_to_map>`{.interpreted-text
role="ref"}

Returns the map coordinates of the cell containing the given
`local_position`. If `local_position` is in global coordinates, consider
using
`Node2D.to_local()<class_Node2D_method_to_local>`{.interpreted-text
role="ref"} before passing it to this method. See also
`map_to_local()<class_TileMapLayer_method_map_to_local>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_map_pattern}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**map_pattern**(position_in_tilemap:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
coords_in_pattern: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, pattern:
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"})
`🔗<class_TileMapLayer_method_map_pattern>`{.interpreted-text
role="ref"}

Returns for the given coordinates `coords_in_pattern` in a
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"} the
corresponding cell coordinates if the pattern was pasted at the
`position_in_tilemap` coordinates (see
`set_pattern()<class_TileMapLayer_method_set_pattern>`{.interpreted-text
role="ref"}). This mapping is required as in half-offset tile shapes,
the mapping might not work by calculating
`position_in_tile_map + coords_in_pattern`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_map_to_local}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**map_to_local**(map_position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapLayer_method_map_to_local>`{.interpreted-text
role="ref"}

Returns the centered position of a cell in the **TileMapLayer**\'s local
coordinate space. To convert the returned value into global coordinates,
use
`Node2D.to_global()<class_Node2D_method_to_global>`{.interpreted-text
role="ref"}. See also
`local_to_map()<class_TileMapLayer_method_local_to_map>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This may not correspond to the visual position of the
tile, i.e. it ignores the
`TileData.texture_origin<class_TileData_property_texture_origin>`{.interpreted-text
role="ref"} property of individual tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_notify_runtime_tile_data_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_runtime_tile_data_update**()
`🔗<class_TileMapLayer_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"}

Notifies the **TileMapLayer** node that calls to
`_use_tile_data_runtime_update()<class_TileMapLayer_private_method__use_tile_data_runtime_update>`{.interpreted-text
role="ref"} or
`_tile_data_runtime_update()<class_TileMapLayer_private_method__tile_data_runtime_update>`{.interpreted-text
role="ref"} will lead to different results. This will thus trigger a
**TileMapLayer** update.

\*\*Warning:\*\* Updating the **TileMapLayer** is computationally
expensive and may impact performance. Try to limit the number of calls
to this function to avoid unnecessary update.

\*\*Note:\*\* This does not trigger a direct update of the
**TileMapLayer**, the update will be done at the end of the frame as
usual (unless you call
`update_internals()<class_TileMapLayer_method_update_internals>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_set_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell**(coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, source_id: `int<class_int>`{.interpreted-text role="ref"} =
-1, atlas_coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} = Vector2i(-1, -1), alternative_tile:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_TileMapLayer_method_set_cell>`{.interpreted-text role="ref"}

Sets the tile identifiers for the cell at coordinates `coords`. Each
tile of the `TileSet<class_TileSet>`{.interpreted-text role="ref"} is
identified using three parts:

- The source identifier `source_id` identifies a
  `TileSetSource<class_TileSetSource>`{.interpreted-text role="ref"}
  identifier. See
  `TileSet.set_source_id()<class_TileSet_method_set_source_id>`{.interpreted-text
  role="ref"},
- The atlas coordinate identifier `atlas_coords` identifies a tile
  coordinates in the atlas (if the source is a
  `TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
  role="ref"}). For
  `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
  role="ref"} it should always be `Vector2i(0, 0)`,
- The alternative tile identifier `alternative_tile` identifies a tile
  alternative in the atlas (if the source is a
  `TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
  role="ref"}), and the scene for a
  `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
  role="ref"}.

If `source_id` is set to `-1`, `atlas_coords` to `Vector2i(-1, -1)`, or
`alternative_tile` to `-1`, the cell will be erased. An erased cell gets
**all** its identifiers automatically set to their respective invalid
values, namely `-1`, `Vector2i(-1, -1)` and `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_set_cells_terrain_connect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cells_terrain_connect**(cells:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\],
terrain_set: `int<class_int>`{.interpreted-text role="ref"}, terrain:
`int<class_int>`{.interpreted-text role="ref"}, ignore_empty_terrains:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_TileMapLayer_method_set_cells_terrain_connect>`{.interpreted-text
role="ref"}

Update all the cells in the `cells` coordinates array so that they use
the given `terrain` for the given `terrain_set`. If an updated cell has
the same terrain as one of its neighboring cells, this function tries to
join the two. This function might update neighboring tiles if needed to
create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored
when trying to find the best fitting tile for the given terrain
constraints.

\*\*Note:\*\* To work correctly, this method requires the
**TileMapLayer**\'s TileSet to have terrains set up with all required
terrain combinations. Otherwise, it may produce unexpected results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_set_cells_terrain_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cells_terrain_path**(path: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\],
terrain_set: `int<class_int>`{.interpreted-text role="ref"}, terrain:
`int<class_int>`{.interpreted-text role="ref"}, ignore_empty_terrains:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_TileMapLayer_method_set_cells_terrain_path>`{.interpreted-text
role="ref"}

Update all the cells in the `path` coordinates array so that they use
the given `terrain` for the given `terrain_set`. The function will also
connect two successive cell in the path with the same terrain. This
function might update neighboring tiles if needed to create correct
terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored
when trying to find the best fitting tile for the given terrain
constraints.

\*\*Note:\*\* To work correctly, this method requires the
**TileMapLayer**\'s TileSet to have terrains set up with all required
terrain combinations. Otherwise, it may produce unexpected results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_set_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_TileMapLayer_method_set_navigation_map>`{.interpreted-text
role="ref"}

Sets a custom `map` as a
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} navigation map. If not set, uses the default
`World2D<class_World2D>`{.interpreted-text role="ref"} navigation map
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_set_pattern}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_pattern**(position: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, pattern:
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"})
`🔗<class_TileMapLayer_method_set_pattern>`{.interpreted-text
role="ref"}

Pastes the `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"} at the given `position` in the tile map. See also
`get_pattern()<class_TileMapLayer_method_get_pattern>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapLayer_method_update_internals}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_internals**()
`🔗<class_TileMapLayer_method_update_internals>`{.interpreted-text
role="ref"}

Triggers a direct update of the **TileMapLayer**. Usually, calling this
function is not needed, as **TileMapLayer** node updates automatically
when one of its properties or cells is modified.

However, for performance reasons, those updates are batched and delayed
to the end of the frame. Calling this function will force the
**TileMapLayer** to update right away instead.

\*\*Warning:\*\* Updating the **TileMapLayer** is computationally
expensive and may impact performance. Try to limit the number of updates
and how many tiles they impact.
