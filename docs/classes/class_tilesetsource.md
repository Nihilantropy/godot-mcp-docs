github_url
:   hide

# TileSetSource {#class_TileSetSource}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"},
`TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`{.interpreted-text
role="ref"}

Exposes a set of tiles for a `TileSet<class_TileSet>`{.interpreted-text
role="ref"} resource.

::: rst-class
classref-introduction-group
:::

## Description

Exposes a set of tiles for a `TileSet<class_TileSet>`{.interpreted-text
role="ref"} resource.

Tiles in a source are indexed with two IDs, coordinates ID (of type
Vector2i) and an alternative ID (of type int), named according to their
use in the
`TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"} class.

Depending on the TileSet source type, those IDs might have restrictions
on their values, this is why the base **TileSetSource** class only
exposes getters for them.

You can iterate over all tiles exposed by a TileSetSource by first
iterating over coordinates IDs using
`get_tiles_count()<class_TileSetSource_method_get_tiles_count>`{.interpreted-text
role="ref"} and
`get_tile_id()<class_TileSetSource_method_get_tile_id>`{.interpreted-text
role="ref"}, then over alternative IDs using
`get_alternative_tiles_count()<class_TileSetSource_method_get_alternative_tiles_count>`{.interpreted-text
role="ref"} and
`get_alternative_tile_id()<class_TileSetSource_method_get_alternative_tile_id>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* **TileSetSource** can only be added to one TileSet at
the same time. Calling
`TileSet.add_source()<class_TileSet_method_add_source>`{.interpreted-text
role="ref"} on a second `TileSet<class_TileSet>`{.interpreted-text
role="ref"} will remove the source from the first one.

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

:::: {#class_TileSetSource_method_get_alternative_tile_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_alternative_tile_id**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetSource_method_get_alternative_tile_id>`{.interpreted-text
role="ref"}

Returns the alternative ID for the tile with coordinates ID
`atlas_coords` at index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetSource_method_get_alternative_tiles_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_alternative_tiles_count**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetSource_method_get_alternative_tiles_count>`{.interpreted-text
role="ref"}

Returns the number of alternatives tiles for the coordinates ID
`atlas_coords`.

For `TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"}, this always return at least 1, as the base tile with ID 0
is always part of the alternatives list.

Returns -1 if there is not tile at the given coords.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetSource_method_get_tile_id}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_tile_id**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetSource_method_get_tile_id>`{.interpreted-text
role="ref"}

Returns the tile coordinates ID of the tile with index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetSource_method_get_tiles_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_tiles_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetSource_method_get_tiles_count>`{.interpreted-text
role="ref"}

Returns how many tiles this atlas source defines (not including
alternative tiles).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetSource_method_has_alternative_tile}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_alternative_tile**(atlas_coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
alternative_tile: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetSource_method_has_alternative_tile>`{.interpreted-text
role="ref"}

Returns if the base tile at coordinates `atlas_coords` has an
alternative with ID `alternative_tile`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetSource_method_has_tile}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_tile**(atlas_coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TileSetSource_method_has_tile>`{.interpreted-text
role="ref"}

Returns if this atlas has a tile with coordinates ID `atlas_coords`.
