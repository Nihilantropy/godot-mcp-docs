github_url
:   hide

# TileSet {#class_TileSet}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Tile library for tilemaps.

::: rst-class
classref-introduction-group
:::

## Description

A TileSet is a library of tiles for a
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"}. A
TileSet handles a list of
`TileSetSource<class_TileSetSource>`{.interpreted-text role="ref"}, each
of them storing a set of tiles.

Tiles can either be from a
`TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"}, which renders tiles out of a texture with support for
physics, navigation, etc., or from a
`TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
role="ref"}, which exposes scene-based tiles.

Tiles are referenced by using three IDs: their source ID, their atlas
coordinates ID, and their alternative tile ID.

A TileSet can be configured so that its tiles expose more or fewer
properties. To do so, the TileSet resources use property layers, which
you can add or remove depending on your needs.

For example, adding a physics layer allows giving collision shapes to
your tiles. Each layer has dedicated properties (physics layer and
mask), so you may add several TileSet physics layers for each type of
collision you need.

See the functions to add new layers for more information.

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

## Enumerations

:::: {#enum_TileSet_TileShape}
::: rst-class
classref-enumeration
:::
::::

enum **TileShape**: `🔗<enum_TileSet_TileShape>`{.interpreted-text
role="ref"}

:::: {#class_TileSet_constant_TILE_SHAPE_SQUARE}
::: rst-class
classref-enumeration-constant
:::
::::

`TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"}
**TILE_SHAPE_SQUARE** = `0`

Rectangular tile shape.

:::: {#class_TileSet_constant_TILE_SHAPE_ISOMETRIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"}
**TILE_SHAPE_ISOMETRIC** = `1`

Diamond tile shape (for isometric look).

\*\*Note:\*\* Isometric **TileSet** works best if all sibling
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"}s and
their parent inheriting from `Node2D<class_Node2D>`{.interpreted-text
role="ref"} have Y-sort enabled.

:::: {#class_TileSet_constant_TILE_SHAPE_HALF_OFFSET_SQUARE}
::: rst-class
classref-enumeration-constant
:::
::::

`TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"}
**TILE_SHAPE_HALF_OFFSET_SQUARE** = `2`

Rectangular tile shape with one row/column out of two offset by half a
tile.

:::: {#class_TileSet_constant_TILE_SHAPE_HEXAGON}
::: rst-class
classref-enumeration-constant
:::
::::

`TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"}
**TILE_SHAPE_HEXAGON** = `3`

Hexagonal tile shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TileSet_TileLayout}
::: rst-class
classref-enumeration
:::
::::

enum **TileLayout**: `🔗<enum_TileSet_TileLayout>`{.interpreted-text
role="ref"}

:::: {#class_TileSet_constant_TILE_LAYOUT_STACKED}
::: rst-class
classref-enumeration-constant
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**TILE_LAYOUT_STACKED** = `0`

Tile coordinates layout where both axis stay consistent with their
respective local horizontal and vertical axis.

:::: {#class_TileSet_constant_TILE_LAYOUT_STACKED_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**TILE_LAYOUT_STACKED_OFFSET** = `1`

Same as
`TILE_LAYOUT_STACKED<class_TileSet_constant_TILE_LAYOUT_STACKED>`{.interpreted-text
role="ref"}, but the first half-offset is negative instead of positive.

:::: {#class_TileSet_constant_TILE_LAYOUT_STAIRS_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**TILE_LAYOUT_STAIRS_RIGHT** = `2`

Tile coordinates layout where the horizontal axis stay horizontal, and
the vertical one goes down-right.

:::: {#class_TileSet_constant_TILE_LAYOUT_STAIRS_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**TILE_LAYOUT_STAIRS_DOWN** = `3`

Tile coordinates layout where the vertical axis stay vertical, and the
horizontal one goes down-right.

:::: {#class_TileSet_constant_TILE_LAYOUT_DIAMOND_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**TILE_LAYOUT_DIAMOND_RIGHT** = `4`

Tile coordinates layout where the horizontal axis goes up-right, and the
vertical one goes down-right.

:::: {#class_TileSet_constant_TILE_LAYOUT_DIAMOND_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**TILE_LAYOUT_DIAMOND_DOWN** = `5`

Tile coordinates layout where the horizontal axis goes down-right, and
the vertical one goes down-left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TileSet_TileOffsetAxis}
::: rst-class
classref-enumeration
:::
::::

enum **TileOffsetAxis**:
`🔗<enum_TileSet_TileOffsetAxis>`{.interpreted-text role="ref"}

:::: {#class_TileSet_constant_TILE_OFFSET_AXIS_HORIZONTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`TileOffsetAxis<enum_TileSet_TileOffsetAxis>`{.interpreted-text
role="ref"} **TILE_OFFSET_AXIS_HORIZONTAL** = `0`

Horizontal half-offset.

:::: {#class_TileSet_constant_TILE_OFFSET_AXIS_VERTICAL}
::: rst-class
classref-enumeration-constant
:::
::::

`TileOffsetAxis<enum_TileSet_TileOffsetAxis>`{.interpreted-text
role="ref"} **TILE_OFFSET_AXIS_VERTICAL** = `1`

Vertical half-offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TileSet_CellNeighbor}
::: rst-class
classref-enumeration
:::
::::

enum **CellNeighbor**: `🔗<enum_TileSet_CellNeighbor>`{.interpreted-text
role="ref"}

:::: {#class_TileSet_constant_CELL_NEIGHBOR_RIGHT_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_RIGHT_SIDE** = `0`

Neighbor on the right side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_RIGHT_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_RIGHT_CORNER** = `1`

Neighbor in the right corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_RIGHT_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_BOTTOM_RIGHT_SIDE** = `2`

Neighbor on the bottom right side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_RIGHT_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_BOTTOM_RIGHT_CORNER** = `3`

Neighbor in the bottom right corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_BOTTOM_SIDE** = `4`

Neighbor on the bottom side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_BOTTOM_CORNER** = `5`

Neighbor in the bottom corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_LEFT_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_BOTTOM_LEFT_SIDE** = `6`

Neighbor on the bottom left side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_LEFT_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_BOTTOM_LEFT_CORNER** = `7`

Neighbor in the bottom left corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_LEFT_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_LEFT_SIDE** = `8`

Neighbor on the left side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_LEFT_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_LEFT_CORNER** = `9`

Neighbor in the left corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_TOP_LEFT_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_TOP_LEFT_SIDE** = `10`

Neighbor on the top left side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_TOP_LEFT_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_TOP_LEFT_CORNER** = `11`

Neighbor in the top left corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_TOP_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_TOP_SIDE** = `12`

Neighbor on the top side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_TOP_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_TOP_CORNER** = `13`

Neighbor in the top corner.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_TOP_RIGHT_SIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_TOP_RIGHT_SIDE** = `14`

Neighbor on the top right side.

:::: {#class_TileSet_constant_CELL_NEIGHBOR_TOP_RIGHT_CORNER}
::: rst-class
classref-enumeration-constant
:::
::::

`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"}
**CELL_NEIGHBOR_TOP_RIGHT_CORNER** = `15`

Neighbor in the top right corner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TileSet_TerrainMode}
::: rst-class
classref-enumeration
:::
::::

enum **TerrainMode**: `🔗<enum_TileSet_TerrainMode>`{.interpreted-text
role="ref"}

:::: {#class_TileSet_constant_TERRAIN_MODE_MATCH_CORNERS_AND_SIDES}
::: rst-class
classref-enumeration-constant
:::
::::

`TerrainMode<enum_TileSet_TerrainMode>`{.interpreted-text role="ref"}
**TERRAIN_MODE_MATCH_CORNERS_AND_SIDES** = `0`

Requires both corners and side to match with neighboring tiles\'
terrains.

:::: {#class_TileSet_constant_TERRAIN_MODE_MATCH_CORNERS}
::: rst-class
classref-enumeration-constant
:::
::::

`TerrainMode<enum_TileSet_TerrainMode>`{.interpreted-text role="ref"}
**TERRAIN_MODE_MATCH_CORNERS** = `1`

Requires corners to match with neighboring tiles\' terrains.

:::: {#class_TileSet_constant_TERRAIN_MODE_MATCH_SIDES}
::: rst-class
classref-enumeration-constant
:::
::::

`TerrainMode<enum_TileSet_TerrainMode>`{.interpreted-text role="ref"}
**TERRAIN_MODE_MATCH_SIDES** = `2`

Requires sides to match with neighboring tiles\' terrains.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TileSet_property_tile_layout}
::: rst-class
classref-property
:::
::::

`TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
**tile_layout** = `0`
`🔗<class_TileSet_property_tile_layout>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tile_layout**(value:
  `TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"})
- `TileLayout<enum_TileSet_TileLayout>`{.interpreted-text role="ref"}
  **get_tile_layout**()

For all half-offset shapes (Isometric, Hexagonal and Half-Offset
square), changes the way tiles are indexed in the
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"} grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_property_tile_offset_axis}
::: rst-class
classref-property
:::
::::

`TileOffsetAxis<enum_TileSet_TileOffsetAxis>`{.interpreted-text
role="ref"} **tile_offset_axis** = `0`
`🔗<class_TileSet_property_tile_offset_axis>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tile_offset_axis**(value:
  `TileOffsetAxis<enum_TileSet_TileOffsetAxis>`{.interpreted-text
  role="ref"})
- `TileOffsetAxis<enum_TileSet_TileOffsetAxis>`{.interpreted-text
  role="ref"} **get_tile_offset_axis**()

For all half-offset shapes (Isometric, Hexagonal and Half-Offset
square), determines the offset axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_property_tile_shape}
::: rst-class
classref-property
:::
::::

`TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"}
**tile_shape** = `0`
`🔗<class_TileSet_property_tile_shape>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tile_shape**(value:
  `TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"})
- `TileShape<enum_TileSet_TileShape>`{.interpreted-text role="ref"}
  **get_tile_shape**()

The tile shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_property_tile_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **tile_size** =
`Vector2i(16, 16)`
`🔗<class_TileSet_property_tile_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tile_size**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_tile_size**()

The tile size, in pixels. For all tile shapes, this size corresponds to
the encompassing rectangle of the tile shape. This is thus the minimal
cell size required in an atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_property_uv_clipping}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **uv_clipping** =
`false` `🔗<class_TileSet_property_uv_clipping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uv_clipping**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_uv_clipping**()

Enables/Disable uv clipping when rendering the tiles.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TileSet_method_add_custom_data_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_custom_data_layer**(to_position:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TileSet_method_add_custom_data_layer>`{.interpreted-text
role="ref"}

Adds a custom data layer to the TileSet at the given position
`to_position` in the array. If `to_position` is -1, adds it at the end
of the array.

Custom data layers allow assigning custom properties to atlas tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_navigation_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_navigation_layer**(to_position: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TileSet_method_add_navigation_layer>`{.interpreted-text
role="ref"}

Adds a navigation layer to the TileSet at the given position
`to_position` in the array. If `to_position` is -1, adds it at the end
of the array.

Navigation layers allow assigning a navigable area to atlas tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_occlusion_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_occlusion_layer**(to_position: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TileSet_method_add_occlusion_layer>`{.interpreted-text
role="ref"}

Adds an occlusion layer to the TileSet at the given position
`to_position` in the array. If `to_position` is -1, adds it at the end
of the array.

Occlusion layers allow assigning occlusion polygons to atlas tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_pattern}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_pattern**(pattern:
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"},
index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TileSet_method_add_pattern>`{.interpreted-text role="ref"}

Adds a `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"} to be stored in the TileSet resource. If provided, insert it
at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_physics_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_physics_layer**(to_position: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TileSet_method_add_physics_layer>`{.interpreted-text
role="ref"}

Adds a physics layer to the TileSet at the given position `to_position`
in the array. If `to_position` is -1, adds it at the end of the array.

Physics layers allow assigning collision polygons to atlas tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_source}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_source**(source:
`TileSetSource<class_TileSetSource>`{.interpreted-text role="ref"},
atlas_source_id_override: `int<class_int>`{.interpreted-text role="ref"}
= -1) `🔗<class_TileSet_method_add_source>`{.interpreted-text
role="ref"}

Adds a `TileSetSource<class_TileSetSource>`{.interpreted-text
role="ref"} to the TileSet. If `atlas_source_id_override` is not -1,
also set its source ID. Otherwise, a unique identifier is automatically
generated.

The function returns the added source ID or -1 if the source could not
be added.

\*\*Warning:\*\* A source cannot belong to two TileSets at the same
time. If the added source was attached to another **TileSet**, it will
be removed from that one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_terrain}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_terrain**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text role="ref"}
= -1) `🔗<class_TileSet_method_add_terrain>`{.interpreted-text
role="ref"}

Adds a new terrain to the given terrain set `terrain_set` at the given
position `to_position` in the array. If `to_position` is -1, adds it at
the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_add_terrain_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_terrain_set**(to_position: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TileSet_method_add_terrain_set>`{.interpreted-text role="ref"}

Adds a new terrain set at the given position `to_position` in the array.
If `to_position` is -1, adds it at the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_cleanup_invalid_tile_proxies}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cleanup_invalid_tile_proxies**()
`🔗<class_TileSet_method_cleanup_invalid_tile_proxies>`{.interpreted-text
role="ref"}

Clears tile proxies pointing to invalid tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_clear_tile_proxies}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_tile_proxies**()
`🔗<class_TileSet_method_clear_tile_proxies>`{.interpreted-text
role="ref"}

Clears all tile proxies.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_alternative_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_alternative_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_from: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_get_alternative_level_tile_proxy>`{.interpreted-text
role="ref"}

Returns the alternative-level proxy for the given identifiers. The
returned array contains the three proxie\'s target identifiers (source
ID, atlas coords ID and alternative tile ID).

If the TileSet has no proxy for the given identifiers, returns an empty
Array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_coords_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_coords_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_get_coords_level_tile_proxy>`{.interpreted-text
role="ref"}

Returns the coordinate-level proxy for the given identifiers. The
returned array contains the two target identifiers of the proxy (source
ID and atlas coordinates ID).

If the TileSet has no proxy for the given identifiers, returns an empty
Array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_custom_data_layer_by_name}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_custom_data_layer_by_name**(layer_name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_custom_data_layer_by_name>`{.interpreted-text
role="ref"}

Returns the index of the custom data layer identified by the given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_custom_data_layer_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_custom_data_layer_name**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_custom_data_layer_name>`{.interpreted-text
role="ref"}

Returns the name of the custom data layer identified by the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_custom_data_layer_type}
::: rst-class
classref-method
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **get_custom_data_layer_type**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_custom_data_layer_type>`{.interpreted-text
role="ref"}

Returns the type of the custom data layer identified by the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_custom_data_layers_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_custom_data_layers_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_custom_data_layers_count>`{.interpreted-text
role="ref"}

Returns the custom data layers count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_navigation_layer_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_navigation_layer_layer_value**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_navigation_layer_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified navigation layer of the TileSet
navigation data layer identified by the given `layer_index` is enabled,
given a navigation_layers `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_navigation_layer_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_navigation_layer_layers**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_navigation_layer_layers>`{.interpreted-text
role="ref"}

Returns the navigation layers (as in the Navigation server) of the given
TileSet navigation layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_navigation_layers_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_navigation_layers_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_navigation_layers_count>`{.interpreted-text
role="ref"}

Returns the navigation layers count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_next_source_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_next_source_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_next_source_id>`{.interpreted-text
role="ref"}

Returns a new unused source ID. This generated ID is the same that a
call to
`add_source()<class_TileSet_method_add_source>`{.interpreted-text
role="ref"} would return.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_occlusion_layer_light_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_occlusion_layer_light_mask**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_occlusion_layer_light_mask>`{.interpreted-text
role="ref"}

Returns the light mask of the occlusion layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_occlusion_layer_sdf_collision}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_occlusion_layer_sdf_collision**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_occlusion_layer_sdf_collision>`{.interpreted-text
role="ref"}

Returns if the occluders from this layer use `sdf_collision`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_occlusion_layers_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_occlusion_layers_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_occlusion_layers_count>`{.interpreted-text
role="ref"}

Returns the occlusion layers count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_pattern}
::: rst-class
classref-method
:::
::::

`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"}
**get_pattern**(index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_TileSet_method_get_pattern>`{.interpreted-text role="ref"}

Returns the `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"} at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_patterns_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_patterns_count**()
`🔗<class_TileSet_method_get_patterns_count>`{.interpreted-text
role="ref"}

Returns the number of
`TileMapPattern<class_TileMapPattern>`{.interpreted-text role="ref"}
this tile set handles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_physics_layer_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_physics_layer_collision_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_physics_layer_collision_layer>`{.interpreted-text
role="ref"}

Returns the collision layer (as in the physics server) bodies on the
given TileSet\'s physics layer are in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_physics_layer_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_physics_layer_collision_mask**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_physics_layer_collision_mask>`{.interpreted-text
role="ref"}

Returns the collision mask of bodies on the given TileSet\'s physics
layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_physics_layer_collision_priority}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_physics_layer_collision_priority**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_physics_layer_collision_priority>`{.interpreted-text
role="ref"}

Returns the collision priority of bodies on the given TileSet\'s physics
layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_physics_layer_physics_material}
::: rst-class
classref-method
:::
::::

`PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"}
**get_physics_layer_physics_material**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_physics_layer_physics_material>`{.interpreted-text
role="ref"}

Returns the physics material of bodies on the given TileSet\'s physics
layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_physics_layers_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_physics_layers_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_physics_layers_count>`{.interpreted-text
role="ref"}

Returns the physics layers count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_source}
::: rst-class
classref-method
:::
::::

`TileSetSource<class_TileSetSource>`{.interpreted-text role="ref"}
**get_source**(source_id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileSet_method_get_source>`{.interpreted-text
role="ref"}

Returns the `TileSetSource<class_TileSetSource>`{.interpreted-text
role="ref"} with ID `source_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_source_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_source_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_source_count>`{.interpreted-text
role="ref"}

Returns the number of
`TileSetSource<class_TileSetSource>`{.interpreted-text role="ref"} in
this TileSet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_source_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_source_id**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileSet_method_get_source_id>`{.interpreted-text
role="ref"}

Returns the source ID for source with index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_source_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_source_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_get_source_level_tile_proxy>`{.interpreted-text
role="ref"}

Returns the source-level proxy for the given source identifier.

If the TileSet has no proxy for the given identifier, returns -1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_terrain_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_terrain_color**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, terrain_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_terrain_color>`{.interpreted-text
role="ref"}

Returns a terrain\'s color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_terrain_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_terrain_name**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, terrain_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_terrain_name>`{.interpreted-text
role="ref"}

Returns a terrain\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_terrain_set_mode}
::: rst-class
classref-method
:::
::::

`TerrainMode<enum_TileSet_TerrainMode>`{.interpreted-text role="ref"}
**get_terrain_set_mode**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_terrain_set_mode>`{.interpreted-text
role="ref"}

Returns a terrain set mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_terrain_sets_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_terrain_sets_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_terrain_sets_count>`{.interpreted-text
role="ref"}

Returns the terrain sets count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_get_terrains_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_terrains_count**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_get_terrains_count>`{.interpreted-text
role="ref"}

Returns the number of terrains in the given terrain set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_has_alternative_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_alternative_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_from: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_has_alternative_level_tile_proxy>`{.interpreted-text
role="ref"}

Returns if there is an alternative-level proxy for the given
identifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_has_coords_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_coords_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_has_coords_level_tile_proxy>`{.interpreted-text
role="ref"}

Returns if there is a coodinates-level proxy for the given identifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_has_custom_data_layer_by_name}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_custom_data_layer_by_name**(layer_name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSet_method_has_custom_data_layer_by_name>`{.interpreted-text
role="ref"}

Returns if there is a custom data layer named `layer_name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_has_source}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_source**(source_id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileSet_method_has_source>`{.interpreted-text
role="ref"}

Returns if this TileSet has a source for the given source ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_has_source_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_source_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_has_source_level_tile_proxy>`{.interpreted-text
role="ref"}

Returns if there is a source-level proxy for the given source ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_map_tile_proxy}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**map_tile_proxy**(source_from: `int<class_int>`{.interpreted-text
role="ref"}, coords_from: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, alternative_from: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileSet_method_map_tile_proxy>`{.interpreted-text
role="ref"}

According to the configured proxies, maps the provided identifiers to a
new set of identifiers. The source ID, atlas coordinates ID and
alternative tile ID are returned as a 3 elements Array.

This function first look for matching alternative-level proxies, then
coordinates-level proxies, then source-level proxies.

If no proxy corresponding to provided identifiers are found, returns the
same values the ones used as arguments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_move_custom_data_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_custom_data_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, to_position:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_move_custom_data_layer>`{.interpreted-text
role="ref"}

Moves the custom data layer at index `layer_index` to the given position
`to_position` in the array. Also updates the atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_move_navigation_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_navigation_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, to_position:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_move_navigation_layer>`{.interpreted-text
role="ref"}

Moves the navigation layer at index `layer_index` to the given position
`to_position` in the array. Also updates the atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_move_occlusion_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_occlusion_layer**(layer_index: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSet_method_move_occlusion_layer>`{.interpreted-text
role="ref"}

Moves the occlusion layer at index `layer_index` to the given position
`to_position` in the array. Also updates the atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_move_physics_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_physics_layer**(layer_index: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSet_method_move_physics_layer>`{.interpreted-text
role="ref"}

Moves the physics layer at index `layer_index` to the given position
`to_position` in the array. Also updates the atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_move_terrain}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_terrain**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, terrain_index: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TileSet_method_move_terrain>`{.interpreted-text
role="ref"}

Moves the terrain at index `terrain_index` for terrain set `terrain_set`
to the given position `to_position` in the array. Also updates the atlas
tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_move_terrain_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_terrain_set**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSet_method_move_terrain_set>`{.interpreted-text
role="ref"}

Moves the terrain set at index `terrain_set` to the given position
`to_position` in the array. Also updates the atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_alternative_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_alternative_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_from: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_remove_alternative_level_tile_proxy>`{.interpreted-text
role="ref"}

Removes an alternative-level proxy for the given identifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_coords_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_coords_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_remove_coords_level_tile_proxy>`{.interpreted-text
role="ref"}

Removes a coordinates-level proxy for the given identifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_custom_data_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_custom_data_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_remove_custom_data_layer>`{.interpreted-text
role="ref"}

Removes the custom data layer at index `layer_index`. Also updates the
atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_navigation_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_navigation_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_remove_navigation_layer>`{.interpreted-text
role="ref"}

Removes the navigation layer at index `layer_index`. Also updates the
atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_occlusion_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_occlusion_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_remove_occlusion_layer>`{.interpreted-text
role="ref"}

Removes the occlusion layer at index `layer_index`. Also updates the
atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_pattern}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_pattern**(index: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TileSet_method_remove_pattern>`{.interpreted-text
role="ref"}

Remove the `TileMapPattern<class_TileMapPattern>`{.interpreted-text
role="ref"} at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_physics_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_physics_layer**(layer_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSet_method_remove_physics_layer>`{.interpreted-text
role="ref"}

Removes the physics layer at index `layer_index`. Also updates the atlas
tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_source}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_source**(source_id: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TileSet_method_remove_source>`{.interpreted-text
role="ref"}

Removes the source with the given source ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_source_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_source_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_remove_source_level_tile_proxy>`{.interpreted-text
role="ref"}

Removes a source-level tile proxy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_terrain}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_terrain**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, terrain_index: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TileSet_method_remove_terrain>`{.interpreted-text
role="ref"}

Removes the terrain at index `terrain_index` in the given terrain set
`terrain_set`. Also updates the atlas tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_remove_terrain_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_terrain_set**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSet_method_remove_terrain_set>`{.interpreted-text
role="ref"}

Removes the terrain set at index `terrain_set`. Also updates the atlas
tiles accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_alternative_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_alternative_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_from: `int<class_int>`{.interpreted-text role="ref"},
source_to: `int<class_int>`{.interpreted-text role="ref"}, coords_to:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_to: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_alternative_level_tile_proxy>`{.interpreted-text
role="ref"}

Create an alternative-level proxy for the given identifiers. A proxy
will map set of tile identifiers to another set of identifiers.

Proxied tiles can be automatically replaced in TileMapLayer nodes using
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_coords_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_coords_level_tile_proxy**(p_source_from:
`int<class_int>`{.interpreted-text role="ref"}, coords_from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, source_to:
`int<class_int>`{.interpreted-text role="ref"}, coords_to:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_coords_level_tile_proxy>`{.interpreted-text
role="ref"}

Creates a coordinates-level proxy for the given identifiers. A proxy
will map set of tile identifiers to another set of identifiers. The
alternative tile ID is kept the same when using coordinates-level
proxies.

Proxied tiles can be automatically replaced in TileMapLayer nodes using
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_custom_data_layer_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_data_layer_name**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, layer_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_custom_data_layer_name>`{.interpreted-text
role="ref"}

Sets the name of the custom data layer identified by the given index.
Names are identifiers of the layer therefore if the name is already
taken it will fail and raise an error.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_custom_data_layer_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_data_layer_type**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, layer_type:
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"})
`🔗<class_TileSet_method_set_custom_data_layer_type>`{.interpreted-text
role="ref"}

Sets the type of the custom data layer identified by the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_navigation_layer_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_layer_layer_value**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_navigation_layer_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified navigation layer of
the TileSet navigation data layer identified by the given `layer_index`,
given a navigation_layers `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_navigation_layer_layers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_layer_layers**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_navigation_layer_layers>`{.interpreted-text
role="ref"}

Sets the navigation layers (as in the navigation server) for navigation
regions in the given TileSet navigation layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_occlusion_layer_light_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_occlusion_layer_light_mask**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, light_mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_occlusion_layer_light_mask>`{.interpreted-text
role="ref"}

Sets the occlusion layer (as in the rendering server) for occluders in
the given TileSet occlusion layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_occlusion_layer_sdf_collision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_occlusion_layer_sdf_collision**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, sdf_collision:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_occlusion_layer_sdf_collision>`{.interpreted-text
role="ref"}

Enables or disables SDF collision for occluders in the given TileSet
occlusion layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_physics_layer_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physics_layer_collision_layer**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_physics_layer_collision_layer>`{.interpreted-text
role="ref"}

Sets the collision layer (as in the physics server) for bodies in the
given TileSet physics layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_physics_layer_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physics_layer_collision_mask**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_physics_layer_collision_mask>`{.interpreted-text
role="ref"}

Sets the collision mask for bodies in the given TileSet physics layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_physics_layer_collision_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physics_layer_collision_priority**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, priority:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_physics_layer_collision_priority>`{.interpreted-text
role="ref"}

Sets the collision priority for bodies in the given TileSet physics
layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_physics_layer_physics_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physics_layer_physics_material**(layer_index:
`int<class_int>`{.interpreted-text role="ref"}, physics_material:
`PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_physics_layer_physics_material>`{.interpreted-text
role="ref"}

Sets the physics material for bodies in the given TileSet physics layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_source_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_source_id**(source_id: `int<class_int>`{.interpreted-text
role="ref"}, new_source_id: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TileSet_method_set_source_id>`{.interpreted-text
role="ref"}

Changes a source\'s ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_source_level_tile_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_source_level_tile_proxy**(source_from:
`int<class_int>`{.interpreted-text role="ref"}, source_to:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_source_level_tile_proxy>`{.interpreted-text
role="ref"}

Creates a source-level proxy for the given source ID. A proxy will map
set of tile identifiers to another set of identifiers. Both the atlas
coordinates ID and the alternative tile ID are kept the same when using
source-level proxies.

Proxied tiles can be automatically replaced in TileMapLayer nodes using
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_terrain_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_terrain_color**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, terrain_index: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_terrain_color>`{.interpreted-text
role="ref"}

Sets a terrain\'s color. This color is used for identifying the
different terrains in the TileSet editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_terrain_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_terrain_name**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, terrain_index: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_terrain_name>`{.interpreted-text
role="ref"}

Sets a terrain\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSet_method_set_terrain_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_terrain_set_mode**(terrain_set: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`TerrainMode<enum_TileSet_TerrainMode>`{.interpreted-text role="ref"})
`🔗<class_TileSet_method_set_terrain_set_mode>`{.interpreted-text
role="ref"}

Sets a terrain mode. Each mode determines which bits of a tile shape is
used to match the neighboring tiles\' terrains.
