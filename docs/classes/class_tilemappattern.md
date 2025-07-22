github_url
:   hide

# TileMapPattern {#class_TileMapPattern}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds a pattern to be copied from or pasted into
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

This resource holds a set of cells to help bulk manipulations of
`TileMap<class_TileMap>`{.interpreted-text role="ref"}.

A pattern always starts at the `(0, 0)` coordinates and cannot have
cells with negative coordinates.

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

:::: {#class_TileMapPattern_method_get_cell_alternative_tile}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_alternative_tile**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_get_cell_alternative_tile>`{.interpreted-text
role="ref"}

Returns the tile alternative ID of the cell at `coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_get_cell_atlas_coords}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_cell_atlas_coords**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_get_cell_atlas_coords>`{.interpreted-text
role="ref"}

Returns the tile atlas coordinates ID of the cell at `coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_get_cell_source_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_cell_source_id**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_get_cell_source_id>`{.interpreted-text
role="ref"}

Returns the tile source ID of the cell at `coords`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_get_size>`{.interpreted-text role="ref"}

Returns the size, in cells, of the pattern.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_get_used_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_used_cells**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_get_used_cells>`{.interpreted-text
role="ref"}

Returns the list of used cell coordinates in the pattern.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_has_cell}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_cell**(coords:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_has_cell>`{.interpreted-text role="ref"}

Returns whether the pattern has a tile at the given coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileMapPattern_method_is_empty>`{.interpreted-text role="ref"}

Returns whether the pattern is empty or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_remove_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_cell**(coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, update_size: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TileMapPattern_method_remove_cell>`{.interpreted-text
role="ref"}

Remove the cell at the given coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_set_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell**(coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, source_id: `int<class_int>`{.interpreted-text role="ref"} =
-1, atlas_coords: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} = Vector2i(-1, -1), alternative_tile:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TileMapPattern_method_set_cell>`{.interpreted-text role="ref"}

Sets the tile identifiers for the cell at coordinates `coords`. See
`TileMap.set_cell()<class_TileMap_method_set_cell>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileMapPattern_method_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_size**(size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_TileMapPattern_method_set_size>`{.interpreted-text role="ref"}

Sets the size of the pattern.
