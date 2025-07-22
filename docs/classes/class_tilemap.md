github_url
:   hide

::: {.meta keywords="gridmap"}
:::

# TileMap {#class_TileMap}

**Deprecated:** Use multiple
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"} nodes
instead. To convert a TileMap to a set of TileMapLayer nodes, open the
TileMap bottom panel with the node selected, click the toolbox icon in
the top-right corner and choose \'Extract TileMap layers as individual
TileMapLayer nodes\'.

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node for 2D tile-based maps.

::: rst-class
classref-introduction-group
:::

## Description

Node for 2D tile-based maps. Tilemaps use a
`TileSet<class_TileSet>`{.interpreted-text role="ref"} which contain a
list of tiles which are used to create grid-based maps. A TileMap may
have several layers, layouting tiles on top of each other.

For performance reasons, all TileMap updates are batched at the end of a
frame. Notably, this means that scene tiles from a
`TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
role="ref"} may be initialized after their parent. This is only queued
when inside the scene tree.

To force an update earlier on, call
`update_internals()<class_TileMap_method_update_internals>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For performance and compatibility reasons, the coordinates
serialized by **TileMap** are limited to 16-bit signed integers, i.e.
the range for X and Y coordinates is from `-32768` to `32767`. When
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

:::: {#class_TileMap_signal_changed}
::: rst-class
classref-signal
:::
::::

**changed**() `🔗<class_TileMap_signal_changed>`{.interpreted-text
role="ref"}

Emitted when the `TileSet<class_TileSet>`{.interpreted-text role="ref"}
of this TileMap changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_TileMap_VisibilityMode}
::: rst-class
classref-enumeration
:::
::::

enum **VisibilityMode**:
`🔗<enum_TileMap_VisibilityMode>`{.interpreted-text role="ref"}

:::: {#class_TileMap_constant_VISIBILITY_MODE_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
role="ref"} **VISIBILITY_MODE_DEFAULT** = `0`

Use the debug settings to determine visibility.

:::: {#class_TileMap_constant_VISIBILITY_MODE_FORCE_HIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
role="ref"} **VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide.

:::: {#class_TileMap_constant_VISIBILITY_MODE_FORCE_SHOW}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
role="ref"} **VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TileMap_property_collision_animatable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**collision_animatable** = `false`
`🔗<class_TileMap_property_collision_animatable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_animatable**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collision_animatable**()

If enabled, the TileMap will see its collisions synced to the physics
tick and change its collision type from static to kinematic. This is
required to create TileMap-based moving platform.

\*\*Note:\*\* Enabling
`collision_animatable<class_TileMap_property_collision_animatable>`{.interpreted-text
role="ref"} may have a small performance impact, only do it if the
TileMap is moving and has colliding tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_property_collision_visibility_mode}
::: rst-class
classref-property
:::
::::

`VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
role="ref"} **collision_visibility_mode** = `0`
`🔗<class_TileMap_property_collision_visibility_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_visibility_mode**(value:
  `VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
  role="ref"})
- `VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
  role="ref"} **get_collision_visibility_mode**()

Show or hide the TileMap\'s collision shapes. If set to
`VISIBILITY_MODE_DEFAULT<class_TileMap_constant_VISIBILITY_MODE_DEFAULT>`{.interpreted-text
role="ref"}, this depends on the show collision debug settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_property_navigation_visibility_mode}
::: rst-class
classref-property
:::
::::

`VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
role="ref"} **navigation_visibility_mode** = `0`
`🔗<class_TileMap_property_navigation_visibility_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_visibility_mode**(value:
  `VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
  role="ref"})
- `VisibilityMode<enum_TileMap_VisibilityMode>`{.interpreted-text
  role="ref"} **get_navigation_visibility_mode**()

Show or hide the TileMap\'s navigation meshes. If set to
`VISIBILITY_MODE_DEFAULT<class_TileMap_constant_VISIBILITY_MODE_DEFAULT>`{.interpreted-text
role="ref"}, this depends on the show navigation debug settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_property_rendering_quadrant_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering_quadrant_size** = `16`
`🔗<class_TileMap_property_rendering_quadrant_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rendering_quadrant_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_rendering_quadrant_size**()

The TileMap\'s quadrant size. A quadrant is a group of tiles to be drawn
together on a single canvas item, for optimization purposes.
`rendering_quadrant_size<class_TileMap_property_rendering_quadrant_size>`{.interpreted-text
role="ref"} defines the length of a square\'s side, in the map\'s
coordinate system, that forms the quadrant. Thus, the default quadrant
size groups together `16 * 16 = 256` tiles.

The quadrant size does not apply on Y-sorted layers, as tiles are
grouped by Y position instead in that case.

\*\*Note:\*\* As quadrants are created according to the map\'s
coordinate system, the quadrant\'s \"square shape\" might not look like
square in the TileMap\'s local coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_property_tile_set}
::: rst-class
classref-property
:::
::::

`TileSet<class_TileSet>`{.interpreted-text role="ref"} **tile_set**
`🔗<class_TileMap_property_tile_set>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tileset**(value: `TileSet<class_TileSet>`{.interpreted-text
  role="ref"})
- `TileSet<class_TileSet>`{.interpreted-text role="ref"}
  **get_tileset**()

The `TileSet<class_TileSet>`{.interpreted-text role="ref"} used by this
**TileMap**. The textures, collisions, and additional behavior of all
available tiles are stored here.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TileMap_private_method__tile_data_runtime_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_tile_data_runtime_update**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, tile_data: `TileData<class_TileData>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_private_method__tile_data_runtime_update>`{.interpreted-text
role="ref"}

Called with a TileData object about to be used internally by the
TileMap, allowing its modification at runtime.

This method is only called if
`_use_tile_data_runtime_update()<class_TileMap_private_method__use_tile_data_runtime_update>`{.interpreted-text
role="ref"} is implemented and returns `true` for the given tile
`coords` and `layer`.

\*\*Warning:\*\* The `tile_data` object\'s sub-resources are the same as
the one in the TileSet. Modifying them might impact the whole TileSet.
Instead, make sure to duplicate those resources.

\*\*Note:\*\* If the properties of `tile_data` object should change over
time, use
`notify_runtime_tile_data_update()<class_TileMap_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"} to notify the TileMap it needs an update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_private_method__use_tile_data_runtime_update}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_use_tile_data_runtime_update**(layer:
`int<class_int>`{.interpreted-text role="ref"}, coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_private_method__use_tile_data_runtime_update>`{.interpreted-text
role="ref"}

Should return `true` if the tile at coordinates `coords` on layer
`layer` requires a runtime update.

\*\*Warning:\*\* Make sure this function only return `true` when needed.
Any tile processed at runtime without a need for it will imply a
significant performance penalty.

\*\*Note:\*\* If the result of this function should changed, use
`notify_runtime_tile_data_update()<class_TileMap_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"} to notify the TileMap it needs an update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_add_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_layer**(to_position: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TileMap_method_add_layer>`{.interpreted-text
role="ref"}

Adds a layer at the given position `to_position` in the array. If
`to_position` is negative, the position is counted from the end, with
`-1` adding the layer at the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_TileMap_method_clear>`{.interpreted-text role="ref"}

Clears all cells.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_clear_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_layer**(layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_clear_layer>`{.interpreted-text role="ref"}

Clears all cells on the given layer.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_erase_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_cell**(layer: `int<class_int>`{.interpreted-text role="ref"},
coords: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_erase_cell>`{.interpreted-text role="ref"}

Erases the cell on layer `layer` at coordinates `coords`.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_fix_invalid_tiles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fix_invalid_tiles**()
`🔗<class_TileMap_method_fix_invalid_tiles>`{.interpreted-text
role="ref"}

Clears cells that do not exist in the tileset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_force_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update**(layer: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_TileMap_method_force_update>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`notify_runtime_tile_data_update()<class_TileMap_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"} and/or
`update_internals()<class_TileMap_method_update_internals>`{.interpreted-text
role="ref"} instead.

Forces the TileMap and the layer `layer` to update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_cell_alternative_tile}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_alternative_tile**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_cell_alternative_tile>`{.interpreted-text
role="ref"}

Returns the tile alternative ID of the cell on layer `layer` at
`coords`.

If `use_proxies` is `false`, ignores the
`TileSet<class_TileSet>`{.interpreted-text role="ref"}\'s tile proxies,
returning the raw alternative identifier. See
`TileSet.map_tile_proxy()<class_TileSet_method_map_tile_proxy>`{.interpreted-text
role="ref"}.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_cell_atlas_coords}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_cell_atlas_coords**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_cell_atlas_coords>`{.interpreted-text
role="ref"}

Returns the tile atlas coordinates ID of the cell on layer `layer` at
coordinates `coords`. Returns `Vector2i(-1, -1)` if the cell does not
exist.

If `use_proxies` is `false`, ignores the
`TileSet<class_TileSet>`{.interpreted-text role="ref"}\'s tile proxies,
returning the raw atlas coordinate identifier. See
`TileSet.map_tile_proxy()<class_TileSet_method_map_tile_proxy>`{.interpreted-text
role="ref"}.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_cell_source_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_source_id**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_cell_source_id>`{.interpreted-text
role="ref"}

Returns the tile source ID of the cell on layer `layer` at coordinates
`coords`. Returns `-1` if the cell does not exist.

If `use_proxies` is `false`, ignores the
`TileSet<class_TileSet>`{.interpreted-text role="ref"}\'s tile proxies,
returning the raw source identifier. See
`TileSet.map_tile_proxy()<class_TileSet_method_map_tile_proxy>`{.interpreted-text
role="ref"}.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_cell_tile_data}
::: rst-class
classref-method
:::
::::

`TileData<class_TileData>`{.interpreted-text role="ref"}
**get_cell_tile_data**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_cell_tile_data>`{.interpreted-text
role="ref"}

Returns the `TileData<class_TileData>`{.interpreted-text role="ref"}
object associated with the given cell, or `null` if the cell does not
exist or is not a
`TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"}.

If `layer` is negative, the layers are accessed from the last one.

    func get_clicked_tile_power():
        var clicked_cell = tile_map.local_to_map(tile_map.get_local_mouse_position())
        var data = tile_map.get_cell_tile_data(0, clicked_cell)
        if data:
            return data.get_custom_data("power")
        else:
            return 0

If `use_proxies` is `false`, ignores the
`TileSet<class_TileSet>`{.interpreted-text role="ref"}\'s tile proxies.
See
`TileSet.map_tile_proxy()<class_TileSet_method_map_tile_proxy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_coords_for_body_rid}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_coords_for_body_rid**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_TileMap_method_get_coords_for_body_rid>`{.interpreted-text
role="ref"}

Returns the coordinates of the tile for given physics body RID. Such RID
can be retrieved from
`KinematicCollision2D.get_collider_rid()<class_KinematicCollision2D_method_get_collider_rid>`{.interpreted-text
role="ref"}, when colliding with a tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layer_for_body_rid}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_layer_for_body_rid**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_TileMap_method_get_layer_for_body_rid>`{.interpreted-text
role="ref"}

Returns the tilemap layer of the tile for given physics body RID. Such
RID can be retrieved from
`KinematicCollision2D.get_collider_rid()<class_KinematicCollision2D_method_get_collider_rid>`{.interpreted-text
role="ref"}, when colliding with a tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layer_modulate}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_layer_modulate**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_layer_modulate>`{.interpreted-text
role="ref"}

Returns a TileMap layer\'s modulate.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layer_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_layer_name**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileMap_method_get_layer_name>`{.interpreted-text
role="ref"}

Returns a TileMap layer\'s name.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layer_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_layer_navigation_map**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_layer_navigation_map>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} navigation map assigned to the specified TileMap layer
`layer`.

By default the TileMap uses the default
`World2D<class_World2D>`{.interpreted-text role="ref"} navigation map
for the first TileMap layer. For each additional TileMap layer a new
navigation map is created for the additional layer.

In order to make
`NavigationAgent2D<class_NavigationAgent2D>`{.interpreted-text
role="ref"} switch between TileMap layer navigation maps use
`NavigationAgent2D.set_navigation_map()<class_NavigationAgent2D_method_set_navigation_map>`{.interpreted-text
role="ref"} with the navigation map received from
`get_layer_navigation_map()<class_TileMap_method_get_layer_navigation_map>`{.interpreted-text
role="ref"}.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layer_y_sort_origin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_layer_y_sort_origin**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_layer_y_sort_origin>`{.interpreted-text
role="ref"}

Returns a TileMap layer\'s Y sort origin.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layer_z_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_layer_z_index**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_layer_z_index>`{.interpreted-text
role="ref"}

Returns a TileMap layer\'s Z-index value.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_layers_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_layers_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_layers_count>`{.interpreted-text
role="ref"}

Returns the number of layers in the TileMap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_navigation_map**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_navigation_map>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`get_layer_navigation_map()<class_TileMap_method_get_layer_navigation_map>`{.interpreted-text
role="ref"} instead.

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} navigation map assigned to the specified TileMap layer
`layer`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_neighbor_cell}
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
`🔗<class_TileMap_method_get_neighbor_cell>`{.interpreted-text
role="ref"}

Returns the neighboring cell to the one at coordinates `coords`,
identified by the `neighbor` direction. This method takes into account
the different layouts a TileMap can take.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_pattern}
::: rst-class
classref-method
:::
::::

`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"}
**get_pattern**(layer: `int<class_int>`{.interpreted-text role="ref"},
coords_array: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\])
`🔗<class_TileMap_method_get_pattern>`{.interpreted-text role="ref"}

Creates a new `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"} from the given layer and set of cells.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_surrounding_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_surrounding_cells**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_get_surrounding_cells>`{.interpreted-text
role="ref"}

Returns the list of all neighbourings cells to the one at `coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_used_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_used_cells**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileMap_method_get_used_cells>`{.interpreted-text
role="ref"}

Returns a `Vector2i<class_Vector2i>`{.interpreted-text role="ref"} array
with the positions of all cells containing a tile in the given layer. A
cell is considered empty if its source identifier equals -1, its atlas
coordinates identifiers is `Vector2(-1, -1)` and its alternative
identifier is -1.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_used_cells_by_id}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_used_cells_by_id**(layer: `int<class_int>`{.interpreted-text
role="ref"}, source_id: `int<class_int>`{.interpreted-text role="ref"} =
-1, atlas_coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} = Vector2i(-1, -1), alternative_tile:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_get_used_cells_by_id>`{.interpreted-text
role="ref"}

Returns a `Vector2i<class_Vector2i>`{.interpreted-text role="ref"} array
with the positions of all cells containing a tile in the given layer.
Tiles may be filtered according to their source (`source_id`), their
atlas coordinates (`atlas_coords`) or alternative id
(`alternative_tile`).

If a parameter has its value set to the default one, this parameter is
not used to filter a cell. Thus, if all parameters have their respective
default value, this method returns the same result as
`get_used_cells()<class_TileMap_method_get_used_cells>`{.interpreted-text
role="ref"}.

A cell is considered empty if its source identifier equals -1, its atlas
coordinates identifiers is `Vector2(-1, -1)` and its alternative
identifier is -1.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_get_used_rect}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **get_used_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileMap_method_get_used_rect>`{.interpreted-text
role="ref"}

Returns a rectangle enclosing the used (non-empty) tiles of the map,
including all layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_is_cell_flipped_h}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_cell_flipped_h**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_is_cell_flipped_h>`{.interpreted-text
role="ref"}

Returns `true` if the cell on layer `layer` at coordinates `coords` is
flipped horizontally. The result is valid only for atlas sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_is_cell_flipped_v}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_cell_flipped_v**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_is_cell_flipped_v>`{.interpreted-text
role="ref"}

Returns `true` if the cell on layer `layer` at coordinates `coords` is
flipped vertically. The result is valid only for atlas sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_is_cell_transposed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_cell_transposed**(layer: `int<class_int>`{.interpreted-text
role="ref"}, coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, use_proxies: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_is_cell_transposed>`{.interpreted-text
role="ref"}

Returns `true` if the cell on layer `layer` at coordinates `coords` is
transposed. The result is valid only for atlas sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_is_layer_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_layer_enabled**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_is_layer_enabled>`{.interpreted-text
role="ref"}

Returns if a layer is enabled.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_is_layer_navigation_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_layer_navigation_enabled**(layer:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_is_layer_navigation_enabled>`{.interpreted-text
role="ref"}

Returns if a layer\'s built-in navigation regions generation is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_is_layer_y_sort_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_layer_y_sort_enabled**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMap_method_is_layer_y_sort_enabled>`{.interpreted-text
role="ref"}

Returns if a layer Y-sorts its tiles.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_local_to_map}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**local_to_map**(local_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileMap_method_local_to_map>`{.interpreted-text
role="ref"}

Returns the map coordinates of the cell containing the given
`local_position`. If `local_position` is in global coordinates, consider
using
`Node2D.to_local()<class_Node2D_method_to_local>`{.interpreted-text
role="ref"} before passing it to this method. See also
`map_to_local()<class_TileMap_method_map_to_local>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_map_pattern}
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
`🔗<class_TileMap_method_map_pattern>`{.interpreted-text role="ref"}

Returns for the given coordinate `coords_in_pattern` in a
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"} the
corresponding cell coordinates if the pattern was pasted at the
`position_in_tilemap` coordinates (see
`set_pattern()<class_TileMap_method_set_pattern>`{.interpreted-text
role="ref"}). This mapping is required as in half-offset tile shapes,
the mapping might not work by calculating
`position_in_tile_map + coords_in_pattern`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_map_to_local}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**map_to_local**(map_position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileMap_method_map_to_local>`{.interpreted-text
role="ref"}

Returns the centered position of a cell in the TileMap\'s local
coordinate space. To convert the returned value into global coordinates,
use
`Node2D.to_global()<class_Node2D_method_to_global>`{.interpreted-text
role="ref"}. See also
`local_to_map()<class_TileMap_method_local_to_map>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This may not correspond to the visual position of the
tile, i.e. it ignores the
`TileData.texture_origin<class_TileData_property_texture_origin>`{.interpreted-text
role="ref"} property of individual tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_move_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_layer**(layer: `int<class_int>`{.interpreted-text role="ref"},
to_position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_move_layer>`{.interpreted-text role="ref"}

Moves the layer at index `layer` to the given position `to_position` in
the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_notify_runtime_tile_data_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_runtime_tile_data_update**(layer:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TileMap_method_notify_runtime_tile_data_update>`{.interpreted-text
role="ref"}

Notifies the TileMap node that calls to
`_use_tile_data_runtime_update()<class_TileMap_private_method__use_tile_data_runtime_update>`{.interpreted-text
role="ref"} or
`_tile_data_runtime_update()<class_TileMap_private_method__tile_data_runtime_update>`{.interpreted-text
role="ref"} will lead to different results. This will thus trigger a
TileMap update.

If `layer` is provided, only notifies changes for the given layer.
Providing the `layer` argument (when applicable) is usually preferred
for performance reasons.

\*\*Warning:\*\* Updating the TileMap is computationally expensive and
may impact performance. Try to limit the number of calls to this
function to avoid unnecessary update.

\*\*Note:\*\* This does not trigger a direct update of the TileMap, the
update will be done at the end of the frame as usual (unless you call
`update_internals()<class_TileMap_method_update_internals>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_remove_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_layer**(layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_remove_layer>`{.interpreted-text role="ref"}

Removes the layer at index `layer`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell**(layer: `int<class_int>`{.interpreted-text role="ref"},
coords: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
source_id: `int<class_int>`{.interpreted-text role="ref"} = -1,
atlas_coords: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"} =
Vector2i(-1, -1), alternative_tile: `int<class_int>`{.interpreted-text
role="ref"} = 0) `🔗<class_TileMap_method_set_cell>`{.interpreted-text
role="ref"}

Sets the tile identifiers for the cell on layer `layer` at coordinates
`coords`. Each tile of the `TileSet<class_TileSet>`{.interpreted-text
role="ref"} is identified using three parts:

- The source identifier `source_id` identifies a
  `TileSetSource<class_TileSetSource>`{.interpreted-text role="ref"}
  identifier. See
  `TileSet.set_source_id()<class_TileSet_method_set_source_id>`{.interpreted-text
  role="ref"},
- The atlas coordinates identifier `atlas_coords` identifies a tile
  coordinates in the atlas (if the source is a
  `TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
  role="ref"}). For
  `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
  role="ref"} it should always be `Vector2i(0, 0)`),
- The alternative tile identifier `alternative_tile` identifies a tile
  alternative in the atlas (if the source is a
  `TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
  role="ref"}), and the scene for a
  `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
  role="ref"}.

If `source_id` is set to `-1`, `atlas_coords` to `Vector2i(-1, -1)` or
`alternative_tile` to `-1`, the cell will be erased. An erased cell gets
**all** its identifiers automatically set to their respective invalid
values, namely `-1`, `Vector2i(-1, -1)` and `-1`.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_cells_terrain_connect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cells_terrain_connect**(layer: `int<class_int>`{.interpreted-text
role="ref"}, cells: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\],
terrain_set: `int<class_int>`{.interpreted-text role="ref"}, terrain:
`int<class_int>`{.interpreted-text role="ref"}, ignore_empty_terrains:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_TileMap_method_set_cells_terrain_connect>`{.interpreted-text
role="ref"}

Update all the cells in the `cells` coordinates array so that they use
the given `terrain` for the given `terrain_set`. If an updated cell has
the same terrain as one of its neighboring cells, this function tries to
join the two. This function might update neighboring tiles if needed to
create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored
when trying to find the best fitting tile for the given terrain
constraints.

If `layer` is negative, the layers are accessed from the last one.

\*\*Note:\*\* To work correctly, this method requires the TileMap\'s
TileSet to have terrains set up with all required terrain combinations.
Otherwise, it may produce unexpected results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_cells_terrain_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cells_terrain_path**(layer: `int<class_int>`{.interpreted-text
role="ref"}, path: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\],
terrain_set: `int<class_int>`{.interpreted-text role="ref"}, terrain:
`int<class_int>`{.interpreted-text role="ref"}, ignore_empty_terrains:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_TileMap_method_set_cells_terrain_path>`{.interpreted-text
role="ref"}

Update all the cells in the `path` coordinates array so that they use
the given `terrain` for the given `terrain_set`. The function will also
connect two successive cell in the path with the same terrain. This
function might update neighboring tiles if needed to create correct
terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored
when trying to find the best fitting tile for the given terrain
constraints.

If `layer` is negative, the layers are accessed from the last one.

\*\*Note:\*\* To work correctly, this method requires the TileMap\'s
TileSet to have terrains set up with all required terrain combinations.
Otherwise, it may produce unexpected results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_enabled**(layer: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_set_layer_enabled>`{.interpreted-text
role="ref"}

Enables or disables the layer `layer`. A disabled layer is not processed
at all (no rendering, no physics, etc.).

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_modulate**(layer: `int<class_int>`{.interpreted-text
role="ref"}, modulate: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_TileMap_method_set_layer_modulate>`{.interpreted-text
role="ref"}

Sets a layer\'s color. It will be multiplied by tile\'s color and
TileMap\'s modulate.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_name**(layer: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_set_layer_name>`{.interpreted-text role="ref"}

Sets a layer\'s name. This is mostly useful in the editor.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_navigation_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_navigation_enabled**(layer:
`int<class_int>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_set_layer_navigation_enabled>`{.interpreted-text
role="ref"}

Enables or disables a layer\'s built-in navigation regions generation.
Disable this if you need to bake navigation regions from a TileMap using
a `NavigationRegion2D<class_NavigationRegion2D>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_navigation_map**(layer: `int<class_int>`{.interpreted-text
role="ref"}, map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_set_layer_navigation_map>`{.interpreted-text
role="ref"}

Assigns `map` as a
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} navigation map for the specified TileMap layer `layer`.

By default the TileMap uses the default
`World2D<class_World2D>`{.interpreted-text role="ref"} navigation map
for the first TileMap layer. For each additional TileMap layer a new
navigation map is created for the additional layer.

In order to make
`NavigationAgent2D<class_NavigationAgent2D>`{.interpreted-text
role="ref"} switch between TileMap layer navigation maps use
`NavigationAgent2D.set_navigation_map()<class_NavigationAgent2D_method_set_navigation_map>`{.interpreted-text
role="ref"} with the navigation map received from
`get_layer_navigation_map()<class_TileMap_method_get_layer_navigation_map>`{.interpreted-text
role="ref"}.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_y_sort_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_y_sort_enabled**(layer: `int<class_int>`{.interpreted-text
role="ref"}, y_sort_enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TileMap_method_set_layer_y_sort_enabled>`{.interpreted-text
role="ref"}

Enables or disables a layer\'s Y-sorting. If a layer is Y-sorted, the
layer will behave as a CanvasItem node where each of its tile gets
Y-sorted.

Y-sorted layers should usually be on different Z-index values than not
Y-sorted layers, otherwise, each of those layer will be Y-sorted as
whole with the Y-sorted one. This is usually an undesired behavior.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_y_sort_origin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_y_sort_origin**(layer: `int<class_int>`{.interpreted-text
role="ref"}, y_sort_origin: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileMap_method_set_layer_y_sort_origin>`{.interpreted-text
role="ref"}

Sets a layer\'s Y-sort origin value. This Y-sort origin value is added
to each tile\'s Y-sort origin value.

This allows, for example, to fake a different height level on each
layer. This can be useful for top-down view games.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_layer_z_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_z_index**(layer: `int<class_int>`{.interpreted-text
role="ref"}, z_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_set_layer_z_index>`{.interpreted-text
role="ref"}

Sets a layers Z-index value. This Z-index is added to each tile\'s
Z-index value.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(layer: `int<class_int>`{.interpreted-text
role="ref"}, map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TileMap_method_set_navigation_map>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`set_layer_navigation_map()<class_TileMap_method_set_layer_navigation_map>`{.interpreted-text
role="ref"} instead.

Assigns `map` as a
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} navigation map for the specified TileMap layer `layer`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_set_pattern}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_pattern**(layer: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
pattern: `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"}) `🔗<class_TileMap_method_set_pattern>`{.interpreted-text
role="ref"}

Paste the given `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"} at the given `position` and `layer` in the tile map.

If `layer` is negative, the layers are accessed from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMap_method_update_internals}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_internals**()
`🔗<class_TileMap_method_update_internals>`{.interpreted-text
role="ref"}

Triggers a direct update of the TileMap. Usually, calling this function
is not needed, as TileMap node updates automatically when one of its
properties or cells is modified.

However, for performance reasons, those updates are batched and delayed
to the end of the frame. Calling this function will force the TileMap to
update right away instead.

\*\*Warning:\*\* Updating the TileMap is computationally expensive and
may impact performance. Try to limit the number of updates and how many
tiles they impact.
