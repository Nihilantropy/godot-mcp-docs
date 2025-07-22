github_url
:   hide

# TileSetAtlasSource {#class_TileSetAtlasSource}

**Inherits:** `TileSetSource<class_TileSetSource>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exposes a 2D atlas texture as a set of tiles for a
`TileSet<class_TileSet>`{.interpreted-text role="ref"} resource.

::: rst-class
classref-introduction-group
:::

## Description

An atlas is a grid of tiles laid out on a texture. Each tile in the grid
must be exposed using
`create_tile()<class_TileSetAtlasSource_method_create_tile>`{.interpreted-text
role="ref"}. Those tiles are then indexed using their coordinates in the
grid.

Each tile can also have a size in the grid coordinates, making it more
or less cells in the atlas.

Alternatives version of a tile can be created using
`create_alternative_tile()<class_TileSetAtlasSource_method_create_alternative_tile>`{.interpreted-text
role="ref"}, which are then indexed using an alternative ID. The main
tile (the one in the grid), is accessed with an alternative ID equal to
0.

Each tile alternate has a set of properties that is defined by the
source\'s `TileSet<class_TileSet>`{.interpreted-text role="ref"} layers.
Those properties are stored in a TileData object that can be accessed
and modified using
`get_tile_data()<class_TileSetAtlasSource_method_get_tile_data>`{.interpreted-text
role="ref"}.

As TileData properties are stored directly in the TileSetAtlasSource
resource, their properties might also be set using
`TileSetAtlasSource.set("<coords_x>:<coords_y>/<alternative_id>/<tile_data_property>")`.

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

:::: {#enum_TileSetAtlasSource_TileAnimationMode}
::: rst-class
classref-enumeration
:::
::::

enum **TileAnimationMode**:
`🔗<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"}

:::: {#class_TileSetAtlasSource_constant_TILE_ANIMATION_MODE_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"} **TILE_ANIMATION_MODE_DEFAULT** = `0`

Tile animations start at same time, looking identical.

:::: {#class_TileSetAtlasSource_constant_TILE_ANIMATION_MODE_RANDOM_START_TIMES}
::: rst-class
classref-enumeration-constant
:::
::::

`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"} **TILE_ANIMATION_MODE_RANDOM_START_TIMES** = `1`

Tile animations start at random times, looking varied.

:::: {#class_TileSetAtlasSource_constant_TILE_ANIMATION_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"} **TILE_ANIMATION_MODE_MAX** = `2`

Represents the size of the
`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H}
::: rst-class
classref-constant
:::
::::

**TRANSFORM_FLIP_H** = `4096`
`🔗<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H>`{.interpreted-text
role="ref"}

Represents cell\'s horizontal flip flag. Should be used directly with
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"} to flip
placed tiles by altering their alternative IDs.

    var alternate_id = $TileMapLayer.get_cell_alternative_tile(Vector2i(2, 2))
    if not alternate_id & TileSetAtlasSource.TRANSFORM_FLIP_H:
        # If tile is not already flipped, flip it.
        $TileMapLayer.set_cell(Vector2i(2, 2), source_id, atlas_coords, alternate_id | TileSetAtlasSource.TRANSFORM_FLIP_H)

\*\*Note:\*\* These transformations can be combined to do the equivalent
of 0, 90, 180, and 270 degree rotations, as shown below:

    enum TileTransform {
        ROTATE_0 = 0,
        ROTATE_90 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_H,
        ROTATE_180 = TileSetAtlasSource.TRANSFORM_FLIP_H | TileSetAtlasSource.TRANSFORM_FLIP_V,
        ROTATE_270 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_V,
    }

:::: {#class_TileSetAtlasSource_constant_TRANSFORM_FLIP_V}
::: rst-class
classref-constant
:::
::::

**TRANSFORM_FLIP_V** = `8192`
`🔗<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_V>`{.interpreted-text
role="ref"}

Represents cell\'s vertical flip flag. See
`TRANSFORM_FLIP_H<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H>`{.interpreted-text
role="ref"} for usage.

:::: {#class_TileSetAtlasSource_constant_TRANSFORM_TRANSPOSE}
::: rst-class
classref-constant
:::
::::

**TRANSFORM_TRANSPOSE** = `16384`
`🔗<class_TileSetAtlasSource_constant_TRANSFORM_TRANSPOSE>`{.interpreted-text
role="ref"}

Represents cell\'s transposed flag. See
`TRANSFORM_FLIP_H<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H>`{.interpreted-text
role="ref"} for usage.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TileSetAtlasSource_property_margins}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **margins** =
`Vector2i(0, 0)`
`🔗<class_TileSetAtlasSource_property_margins>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margins**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_margins**()

Margins, in pixels, to offset the origin of the grid in the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_property_separation}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **separation**
= `Vector2i(0, 0)`
`🔗<class_TileSetAtlasSource_property_separation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_separation**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_separation**()

Separation, in pixels, between each tile texture region of the grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_TileSetAtlasSource_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The atlas texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_property_texture_region_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**texture_region_size** = `Vector2i(16, 16)`
`🔗<class_TileSetAtlasSource_property_texture_region_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_region_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_texture_region_size**()

The base tile size in the texture (in pixel). This size must be bigger
than or equal to the TileSet\'s `tile_size` value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_property_use_texture_padding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_texture_padding**
= `true`
`🔗<class_TileSetAtlasSource_property_use_texture_padding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_texture_padding**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_texture_padding**()

If `true`, generates an internal texture with an additional one pixel
padding around each tile. Texture padding avoids a common artifact where
lines appear between tiles.

Disabling this setting might lead a small performance improvement, as
generating the internal texture requires both memory and processing time
when the TileSetAtlasSource resource is modified.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TileSetAtlasSource_method_clear_tiles_outside_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_tiles_outside_texture**()
`🔗<class_TileSetAtlasSource_method_clear_tiles_outside_texture>`{.interpreted-text
role="ref"}

Removes all tiles that don\'t fit the available texture area. This
method iterates over all the source\'s tiles, so it\'s advised to use
`has_tiles_outside_texture()<class_TileSetAtlasSource_method_has_tiles_outside_texture>`{.interpreted-text
role="ref"} beforehand.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_create_alternative_tile}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**create_alternative_tile**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_id_override: `int<class_int>`{.interpreted-text role="ref"}
= -1)
`🔗<class_TileSetAtlasSource_method_create_alternative_tile>`{.interpreted-text
role="ref"}

Creates an alternative tile for the tile at coordinates `atlas_coords`.
If `alternative_id_override` is -1, give it an automatically generated
unique ID, or assigns it the given ID otherwise.

Returns the new alternative identifier, or -1 if the alternative could
not be created with a provided `alternative_id_override`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_create_tile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_tile**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(1,
1)) `🔗<class_TileSetAtlasSource_method_create_tile>`{.interpreted-text
role="ref"}

Creates a new tile at coordinates `atlas_coords` with the given `size`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_atlas_grid_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_atlas_grid_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_atlas_grid_size>`{.interpreted-text
role="ref"}

Returns the atlas grid size, which depends on how many tiles can fit in
the texture. It thus depends on the
`texture<class_TileSetAtlasSource_property_texture>`{.interpreted-text
role="ref"}\'s size, the atlas
`margins<class_TileSetAtlasSource_property_margins>`{.interpreted-text
role="ref"}, and the tiles\'
`texture_region_size<class_TileSetAtlasSource_property_texture_region_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_next_alternative_tile_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_next_alternative_tile_id**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_next_alternative_tile_id>`{.interpreted-text
role="ref"}

Returns the alternative ID a following call to
`create_alternative_tile()<class_TileSetAtlasSource_method_create_alternative_tile>`{.interpreted-text
role="ref"} would return.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_runtime_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_runtime_texture**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_runtime_texture>`{.interpreted-text
role="ref"}

If
`use_texture_padding<class_TileSetAtlasSource_property_use_texture_padding>`{.interpreted-text
role="ref"} is `false`, returns
`texture<class_TileSetAtlasSource_property_texture>`{.interpreted-text
role="ref"}. Otherwise, returns and internal
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} created
that includes the padding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_runtime_tile_texture_region}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**get_runtime_tile_texture_region**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, frame:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_runtime_tile_texture_region>`{.interpreted-text
role="ref"}

Returns the region of the tile at coordinates `atlas_coords` for the
given `frame` inside the texture returned by
`get_runtime_texture()<class_TileSetAtlasSource_method_get_runtime_texture>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`use_texture_padding<class_TileSetAtlasSource_property_use_texture_padding>`{.interpreted-text
role="ref"} is `false`, returns the same as
`get_tile_texture_region()<class_TileSetAtlasSource_method_get_tile_texture_region>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_columns}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tile_animation_columns**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_columns>`{.interpreted-text
role="ref"}

Returns how many columns the tile at `atlas_coords` has in its animation
layout.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_frame_duration}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_tile_animation_frame_duration**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, frame_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_frame_duration>`{.interpreted-text
role="ref"}

Returns the animation frame duration of frame `frame_index` for the tile
at coordinates `atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_frames_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tile_animation_frames_count**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_frames_count>`{.interpreted-text
role="ref"}

Returns how many animation frames has the tile at coordinates
`atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_mode}
::: rst-class
classref-method
:::
::::

`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"} **get_tile_animation_mode**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_mode>`{.interpreted-text
role="ref"}

Returns the tile animation mode of the tile at `atlas_coords`. See also
`set_tile_animation_mode()<class_TileSetAtlasSource_method_set_tile_animation_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_separation}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_tile_animation_separation**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_separation>`{.interpreted-text
role="ref"}

Returns the separation (as in the atlas grid) between each frame of an
animated tile at coordinates `atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_speed}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_tile_animation_speed**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_speed>`{.interpreted-text
role="ref"}

Returns the animation speed of the tile at coordinates `atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_animation_total_duration}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_tile_animation_total_duration**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_animation_total_duration>`{.interpreted-text
role="ref"}

Returns the sum of the sum of the frame durations of the tile at
coordinates `atlas_coords`. This value needs to be divided by the
animation speed to get the actual animation loop duration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_at_coords}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_tile_at_coords**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_at_coords>`{.interpreted-text
role="ref"}

If there is a tile covering the `atlas_coords` coordinates, returns the
top-left coordinates of the tile (thus its coordinate ID). Returns
`Vector2i(-1, -1)` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_data}
::: rst-class
classref-method
:::
::::

`TileData<class_TileData>`{.interpreted-text role="ref"}
**get_tile_data**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_tile: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_data>`{.interpreted-text
role="ref"}

Returns the `TileData<class_TileData>`{.interpreted-text role="ref"}
object for the given atlas coordinates and alternative ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_size_in_atlas}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_tile_size_in_atlas**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_size_in_atlas>`{.interpreted-text
role="ref"}

Returns the size of the tile (in the grid coordinates system) at
coordinates `atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tile_texture_region}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**get_tile_texture_region**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, frame:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_get_tile_texture_region>`{.interpreted-text
role="ref"}

Returns a tile\'s texture region in the atlas texture. For animated
tiles, a `frame` argument might be provided for the different frames of
the animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_get_tiles_to_be_removed_on_change}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_tiles_to_be_removed_on_change**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, margins:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, separation:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
texture_region_size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_TileSetAtlasSource_method_get_tiles_to_be_removed_on_change>`{.interpreted-text
role="ref"}

Returns an array of tiles coordinates ID that will be automatically
removed when modifying one or several of those properties: `texture`,
`margins`, `separation` or `texture_region_size`. This can be used to
undo changes that would have caused tiles data loss.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_has_room_for_tile}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_room_for_tile**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
animation_columns: `int<class_int>`{.interpreted-text role="ref"},
animation_separation: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, frames_count: `int<class_int>`{.interpreted-text
role="ref"}, ignored_tile: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} = Vector2i(-1, -1))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_has_room_for_tile>`{.interpreted-text
role="ref"}

Returns whether there is enough room in an atlas to create/modify a tile
with the given properties. If `ignored_tile` is provided, act as is the
given tile was not present in the atlas. This may be used when you want
to modify a tile\'s properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_has_tiles_outside_texture}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_tiles_outside_texture**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetAtlasSource_method_has_tiles_outside_texture>`{.interpreted-text
role="ref"}

Checks if the source has any tiles that don\'t fit the texture area
(either partially or completely).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_move_tile_in_atlas}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_tile_in_atlas**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
new_atlas_coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} = Vector2i(-1, -1), new_size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(-1,
-1))
`🔗<class_TileSetAtlasSource_method_move_tile_in_atlas>`{.interpreted-text
role="ref"}

Move the tile and its alternatives at the `atlas_coords` coordinates to
the `new_atlas_coords` coordinates with the `new_size` size. This
functions will fail if a tile is already present in the given area.

If `new_atlas_coords` is `Vector2i(-1, -1)`, keeps the tile\'s
coordinates. If `new_size` is `Vector2i(-1, -1)`, keeps the tile\'s
size.

To avoid an error, first check if a move is possible using
`has_room_for_tile()<class_TileSetAtlasSource_method_has_room_for_tile>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_remove_alternative_tile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_alternative_tile**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_tile: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_remove_alternative_tile>`{.interpreted-text
role="ref"}

Remove a tile\'s alternative with alternative ID `alternative_tile`.

Calling this function with `alternative_tile` equals to 0 will fail, as
the base tile alternative cannot be removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_remove_tile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_tile**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_remove_tile>`{.interpreted-text
role="ref"}

Remove a tile and its alternative at coordinates `atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_alternative_tile_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_alternative_tile_id**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_tile: `int<class_int>`{.interpreted-text role="ref"},
new_id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_set_alternative_tile_id>`{.interpreted-text
role="ref"}

Change a tile\'s alternative ID from `alternative_tile` to `new_id`.

Calling this function with `new_id` of 0 will fail, as the base tile
alternative cannot be moved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_tile_animation_columns}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tile_animation_columns**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, frame_columns:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_set_tile_animation_columns>`{.interpreted-text
role="ref"}

Sets the number of columns in the animation layout of the tile at
coordinates `atlas_coords`. If set to 0, then the different frames of
the animation are laid out as a single horizontal line in the atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_tile_animation_frame_duration}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tile_animation_frame_duration**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, frame_index:
`int<class_int>`{.interpreted-text role="ref"}, duration:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_set_tile_animation_frame_duration>`{.interpreted-text
role="ref"}

Sets the animation frame `duration` of frame `frame_index` for the tile
at coordinates `atlas_coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_tile_animation_frames_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tile_animation_frames_count**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, frames_count:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_set_tile_animation_frames_count>`{.interpreted-text
role="ref"}

Sets how many animation frames the tile at coordinates `atlas_coords`
has.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_tile_animation_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tile_animation_mode**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, mode:
`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`{.interpreted-text
role="ref"})
`🔗<class_TileSetAtlasSource_method_set_tile_animation_mode>`{.interpreted-text
role="ref"}

Sets the tile animation mode of the tile at `atlas_coords` to `mode`.
See also
`get_tile_animation_mode()<class_TileSetAtlasSource_method_get_tile_animation_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_tile_animation_separation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tile_animation_separation**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, separation:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_set_tile_animation_separation>`{.interpreted-text
role="ref"}

Sets the margin (in grid tiles) between each tile in the animation
layout of the tile at coordinates `atlas_coords` has.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetAtlasSource_method_set_tile_animation_speed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tile_animation_speed**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, speed:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TileSetAtlasSource_method_set_tile_animation_speed>`{.interpreted-text
role="ref"}

Sets the animation speed of the tile at coordinates `atlas_coords` has.
