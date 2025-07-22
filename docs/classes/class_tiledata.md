github_url
:   hide

# TileData {#class_TileData}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Settings for a single tile in a
`TileSet<class_TileSet>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**TileData** object represents a single tile in a
`TileSet<class_TileSet>`{.interpreted-text role="ref"}. It is usually
edited using the tileset editor, but it can be modified at runtime using
`TileMapLayer._tile_data_runtime_update()<class_TileMapLayer_private_method__tile_data_runtime_update>`{.interpreted-text
role="ref"}.

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

:::: {#class_TileData_signal_changed}
::: rst-class
classref-signal
:::
::::

**changed**() `🔗<class_TileData_signal_changed>`{.interpreted-text
role="ref"}

Emitted when any of the properties are changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TileData_property_flip_h}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_h** = `false`
`🔗<class_TileData_property_flip_h>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_h**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flip_h**()

If `true`, the tile will have its texture flipped horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_flip_v}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_v** = `false`
`🔗<class_TileData_property_flip_v>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_v**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flip_v**()

If `true`, the tile will have its texture flipped vertically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_TileData_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The `Material<class_Material>`{.interpreted-text role="ref"} to use for
this **TileData**. This can be a
`CanvasItemMaterial<class_CanvasItemMaterial>`{.interpreted-text
role="ref"} to use the default shader, or a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"} to
use a custom shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **modulate** =
`Color(1, 1, 1, 1)`
`🔗<class_TileData_property_modulate>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_modulate**()

Color modulation of the tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_probability}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **probability** =
`1.0` `🔗<class_TileData_property_probability>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_probability**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_probability**()

Relative probability of this tile being selected when drawing a pattern
of random tiles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_terrain}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **terrain** = `-1`
`🔗<class_TileData_property_terrain>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_terrain**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_terrain**()

ID of the terrain from the terrain set that the tile uses.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_terrain_set}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **terrain_set** = `-1`
`🔗<class_TileData_property_terrain_set>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_terrain_set**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_terrain_set**()

ID of the terrain set that the tile uses.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_texture_origin}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**texture_origin** = `Vector2i(0, 0)`
`🔗<class_TileData_property_texture_origin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_origin**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_texture_origin**()

Offsets the position of where the tile is drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_transpose}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **transpose** = `false`
`🔗<class_TileData_property_transpose>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transpose**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_transpose**()

If `true`, the tile will display transposed, i.e. with horizontal and
vertical texture UVs swapped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_y_sort_origin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **y_sort_origin** = `0`
`🔗<class_TileData_property_y_sort_origin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_y_sort_origin**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_y_sort_origin**()

Vertical point of the tile used for determining y-sorted order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_property_z_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **z_index** = `0`
`🔗<class_TileData_property_z_index>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_z_index**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_z_index**()

Ordering index of this tile, relative to
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TileData_method_add_collision_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_collision_polygon**(layer_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_add_collision_polygon>`{.interpreted-text
role="ref"}

Adds a collision polygon to the tile on the given TileSet physics layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_add_occluder_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_occluder_polygon**(layer_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_add_occluder_polygon>`{.interpreted-text
role="ref"}

Adds an occlusion polygon to the tile on the TileSet occlusion layer
with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_collision_polygon_one_way_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_collision_polygon_one_way_margin**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_collision_polygon_one_way_margin>`{.interpreted-text
role="ref"}

Returns the one-way margin (for one-way platforms) of the polygon at
index `polygon_index` for TileSet physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_collision_polygon_points}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_collision_polygon_points**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_collision_polygon_points>`{.interpreted-text
role="ref"}

Returns the points of the polygon at index `polygon_index` for TileSet
physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_collision_polygons_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collision_polygons_count**(layer_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_collision_polygons_count>`{.interpreted-text
role="ref"}

Returns how many polygons the tile has for TileSet physics layer with
index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_constant_angular_velocity}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_constant_angular_velocity**(layer_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_constant_angular_velocity>`{.interpreted-text
role="ref"}

Returns the constant angular velocity applied to objects colliding with
this tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_constant_linear_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_constant_linear_velocity**(layer_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_constant_linear_velocity>`{.interpreted-text
role="ref"}

Returns the constant linear velocity applied to objects colliding with
this tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_custom_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_custom_data**(layer_name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_custom_data>`{.interpreted-text
role="ref"}

Returns the custom data value for custom data layer named `layer_name`.
To check if a custom data layer exists, use
`has_custom_data()<class_TileData_method_has_custom_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_custom_data_by_layer_id}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_custom_data_by_layer_id**(layer_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_custom_data_by_layer_id>`{.interpreted-text
role="ref"}

Returns the custom data value for custom data layer with index
`layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_navigation_polygon}
::: rst-class
classref-method
:::
::::

`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"} **get_navigation_polygon**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, flip_h:
`bool<class_bool>`{.interpreted-text role="ref"} = false, flip_v:
`bool<class_bool>`{.interpreted-text role="ref"} = false, transpose:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_navigation_polygon>`{.interpreted-text
role="ref"}

Returns the navigation polygon of the tile for the TileSet navigation
layer with index `layer_id`.

`flip_h`, `flip_v`, and `transpose` allow transforming the returned
polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_occluder}
::: rst-class
classref-method
:::
::::

`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"} **get_occluder**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, flip_h:
`bool<class_bool>`{.interpreted-text role="ref"} = false, flip_v:
`bool<class_bool>`{.interpreted-text role="ref"} = false, transpose:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileData_method_get_occluder>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`get_occluder_polygon()<class_TileData_method_get_occluder_polygon>`{.interpreted-text
role="ref"} instead.

Returns the occluder polygon of the tile for the TileSet occlusion layer
with index `layer_id`.

`flip_h`, `flip_v`, and `transpose` allow transforming the returned
polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_occluder_polygon}
::: rst-class
classref-method
:::
::::

`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"} **get_occluder_polygon**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"}, flip_h:
`bool<class_bool>`{.interpreted-text role="ref"} = false, flip_v:
`bool<class_bool>`{.interpreted-text role="ref"} = false, transpose:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_occluder_polygon>`{.interpreted-text
role="ref"}

Returns the occluder polygon at index `polygon_index` from the TileSet
occlusion layer with index `layer_id`.

The `flip_h`, `flip_v`, and `transpose` parameters can be `true` to
transform the returned polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_occluder_polygons_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_occluder_polygons_count**(layer_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_occluder_polygons_count>`{.interpreted-text
role="ref"}

Returns the number of occluder polygons of the tile in the TileSet
occlusion layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_get_terrain_peering_bit}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_terrain_peering_bit**(peering_bit:
`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_get_terrain_peering_bit>`{.interpreted-text
role="ref"}

Returns the tile\'s terrain bit for the given `peering_bit` direction.
To check that a direction is valid, use
`is_valid_terrain_peering_bit()<class_TileData_method_is_valid_terrain_peering_bit>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_has_custom_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_custom_data**(layer_name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_has_custom_data>`{.interpreted-text
role="ref"}

Returns whether there exists a custom data layer named `layer_name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_is_collision_polygon_one_way}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_collision_polygon_one_way**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_is_collision_polygon_one_way>`{.interpreted-text
role="ref"}

Returns whether one-way collisions are enabled for the polygon at index
`polygon_index` for TileSet physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_is_valid_terrain_peering_bit}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_terrain_peering_bit**(peering_bit:
`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileData_method_is_valid_terrain_peering_bit>`{.interpreted-text
role="ref"}

Returns whether the given `peering_bit` direction is valid for this
tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_remove_collision_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_collision_polygon**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_remove_collision_polygon>`{.interpreted-text
role="ref"}

Removes the polygon at index `polygon_index` for TileSet physics layer
with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_remove_occluder_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_occluder_polygon**(layer_id: `int<class_int>`{.interpreted-text
role="ref"}, polygon_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_remove_occluder_polygon>`{.interpreted-text
role="ref"}

Removes the polygon at index `polygon_index` for TileSet occlusion layer
with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_collision_polygon_one_way}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_polygon_one_way**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"}, one_way:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_collision_polygon_one_way>`{.interpreted-text
role="ref"}

Enables/disables one-way collisions on the polygon at index
`polygon_index` for TileSet physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_collision_polygon_one_way_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_polygon_one_way_margin**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"}, one_way_margin:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_collision_polygon_one_way_margin>`{.interpreted-text
role="ref"}

Sets the one-way margin (for one-way platforms) of the polygon at index
`polygon_index` for TileSet physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_collision_polygon_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_polygon_points**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygon_index:
`int<class_int>`{.interpreted-text role="ref"}, polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_set_collision_polygon_points>`{.interpreted-text
role="ref"}

Sets the points of the polygon at index `polygon_index` for TileSet
physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_collision_polygons_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_polygons_count**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygons_count:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_collision_polygons_count>`{.interpreted-text
role="ref"}

Sets the polygons count for TileSet physics layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_constant_angular_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constant_angular_velocity**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, velocity:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_constant_angular_velocity>`{.interpreted-text
role="ref"}

Sets the constant angular velocity. This does not rotate the tile. This
angular velocity is applied to objects colliding with this tile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_constant_linear_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constant_linear_velocity**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, velocity:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_constant_linear_velocity>`{.interpreted-text
role="ref"}

Sets the constant linear velocity. This does not move the tile. This
linear velocity is applied to objects colliding with this tile. This is
useful to create conveyor belts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_custom_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_data**(layer_name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_set_custom_data>`{.interpreted-text
role="ref"}

Sets the tile\'s custom data value for the TileSet custom data layer
with name `layer_name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_custom_data_by_layer_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_data_by_layer_id**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_custom_data_by_layer_id>`{.interpreted-text
role="ref"}

Sets the tile\'s custom data value for the TileSet custom data layer
with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_navigation_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_polygon**(layer_id: `int<class_int>`{.interpreted-text
role="ref"}, navigation_polygon:
`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_set_navigation_polygon>`{.interpreted-text
role="ref"}

Sets the navigation polygon for the TileSet navigation layer with index
`layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_occluder}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_occluder**(layer_id: `int<class_int>`{.interpreted-text
role="ref"}, occluder_polygon:
`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"}) `🔗<class_TileData_method_set_occluder>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`set_occluder_polygon()<class_TileData_method_set_occluder_polygon>`{.interpreted-text
role="ref"} instead.

Sets the occluder for the TileSet occlusion layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_occluder_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_occluder_polygon**(layer_id: `int<class_int>`{.interpreted-text
role="ref"}, polygon_index: `int<class_int>`{.interpreted-text
role="ref"}, polygon:
`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"})
`🔗<class_TileData_method_set_occluder_polygon>`{.interpreted-text
role="ref"}

Sets the occluder for polygon with index `polygon_index` in the TileSet
occlusion layer with index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_occluder_polygons_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_occluder_polygons_count**(layer_id:
`int<class_int>`{.interpreted-text role="ref"}, polygons_count:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_occluder_polygons_count>`{.interpreted-text
role="ref"}

Sets the occluder polygon count in the TileSet occlusion layer with
index `layer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileData_method_set_terrain_peering_bit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_terrain_peering_bit**(peering_bit:
`CellNeighbor<enum_TileSet_CellNeighbor>`{.interpreted-text role="ref"},
terrain: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileData_method_set_terrain_peering_bit>`{.interpreted-text
role="ref"}

Sets the tile\'s terrain bit for the given `peering_bit` direction. To
check that a direction is valid, use
`is_valid_terrain_peering_bit()<class_TileData_method_is_valid_terrain_peering_bit>`{.interpreted-text
role="ref"}.
