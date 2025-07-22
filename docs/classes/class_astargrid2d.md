github_url
:   hide

# AStarGrid2D {#class_AStarGrid2D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An implementation of A\* for finding the shortest path between two
points on a partial 2D grid.

::: rst-class
classref-introduction-group
:::

## Description

**AStarGrid2D** is a variant of
`AStar2D<class_AStar2D>`{.interpreted-text role="ref"} that is
specialized for partial 2D grids. It is simpler to use because it
doesn\'t require you to manually create points and connect them
together. This class also supports multiple types of heuristics, modes
for diagonal movement, and a jumping mode to speed up calculations.

To use **AStarGrid2D**, you only need to set the
`region<class_AStarGrid2D_property_region>`{.interpreted-text
role="ref"} of the grid, optionally set the
`cell_size<class_AStarGrid2D_property_cell_size>`{.interpreted-text
role="ref"}, and then call the
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} method:

::::: tabs
::: code-tab
gdscript

var astar_grid = AStarGrid2D.new() astar_grid.region = Rect2i(0, 0, 32,
32) astar_grid.cell_size = Vector2(16, 16) astar_grid.update()
print(astar_grid.get_id_path(Vector2i(0, 0), Vector2i(3, 4))) \# Prints
\[(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)\]
print(astar_grid.get_point_path(Vector2i(0, 0), Vector2i(3, 4))) \#
Prints \[(0, 0), (16, 16), (32, 32), (48, 48), (48, 64)\]
:::

::: code-tab
csharp

AStarGrid2D astarGrid = new AStarGrid2D(); astarGrid.Region = new
Rect2I(0, 0, 32, 32); astarGrid.CellSize = new Vector2I(16, 16);
astarGrid.Update(); GD.Print(astarGrid.GetIdPath(Vector2I.Zero, new
Vector2I(3, 4))); // Prints \[(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)\]
GD.Print(astarGrid.GetPointPath(Vector2I.Zero, new Vector2I(3, 4))); //
Prints \[(0, 0), (16, 16), (32, 32), (48, 48), (48, 64)\]
:::
:::::

To remove a point from the pathfinding grid, it must be set as \"solid\"
with
`set_point_solid()<class_AStarGrid2D_method_set_point_solid>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Grid-based Navigation with AStarGrid2D
  Demo](https://godotengine.org/asset-library/asset/2723)

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

:::: {#enum_AStarGrid2D_Heuristic}
::: rst-class
classref-enumeration
:::
::::

enum **Heuristic**: `🔗<enum_AStarGrid2D_Heuristic>`{.interpreted-text
role="ref"}

:::: {#class_AStarGrid2D_constant_HEURISTIC_EUCLIDEAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**HEURISTIC_EUCLIDEAN** = `0`

The [Euclidean
heuristic](https://en.wikipedia.org/wiki/Euclidean_distance) to be used
for the pathfinding using the following formula:

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    result = sqrt(dx * dx + dy * dy)

\*\*Note:\*\* This is also the internal heuristic used in
`AStar3D<class_AStar3D>`{.interpreted-text role="ref"} and
`AStar2D<class_AStar2D>`{.interpreted-text role="ref"} by default (with
the inclusion of possible z-axis coordinate).

:::: {#class_AStarGrid2D_constant_HEURISTIC_MANHATTAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**HEURISTIC_MANHATTAN** = `1`

The [Manhattan
heuristic](https://en.wikipedia.org/wiki/Taxicab_geometry) to be used
for the pathfinding using the following formula:

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    result = dx + dy

\*\*Note:\*\* This heuristic is intended to be used with 4-side
orthogonal movements, provided by setting the
`diagonal_mode<class_AStarGrid2D_property_diagonal_mode>`{.interpreted-text
role="ref"} to
`DIAGONAL_MODE_NEVER<class_AStarGrid2D_constant_DIAGONAL_MODE_NEVER>`{.interpreted-text
role="ref"}.

:::: {#class_AStarGrid2D_constant_HEURISTIC_OCTILE}
::: rst-class
classref-enumeration-constant
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**HEURISTIC_OCTILE** = `2`

The Octile heuristic to be used for the pathfinding using the following
formula:

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    f = sqrt(2) - 1
    result = (dx < dy) ? f * dx + dy : f * dy + dx;

:::: {#class_AStarGrid2D_constant_HEURISTIC_CHEBYSHEV}
::: rst-class
classref-enumeration-constant
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**HEURISTIC_CHEBYSHEV** = `3`

The [Chebyshev
heuristic](https://en.wikipedia.org/wiki/Chebyshev_distance) to be used
for the pathfinding using the following formula:

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    result = max(dx, dy)

:::: {#class_AStarGrid2D_constant_HEURISTIC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**HEURISTIC_MAX** = `4`

Represents the size of the
`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AStarGrid2D_DiagonalMode}
::: rst-class
classref-enumeration
:::
::::

enum **DiagonalMode**:
`🔗<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text role="ref"}

:::: {#class_AStarGrid2D_constant_DIAGONAL_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} **DIAGONAL_MODE_ALWAYS** = `0`

The pathfinding algorithm will ignore solid neighbors around the target
cell and allow passing using diagonals.

:::: {#class_AStarGrid2D_constant_DIAGONAL_MODE_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} **DIAGONAL_MODE_NEVER** = `1`

The pathfinding algorithm will ignore all diagonals and the way will be
always orthogonal.

:::: {#class_AStarGrid2D_constant_DIAGONAL_MODE_AT_LEAST_ONE_WALKABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} **DIAGONAL_MODE_AT_LEAST_ONE_WALKABLE** = `2`

The pathfinding algorithm will avoid using diagonals if at least two
obstacles have been placed around the neighboring cells of the specific
path segment.

:::: {#class_AStarGrid2D_constant_DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES}
::: rst-class
classref-enumeration-constant
:::
::::

`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} **DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES** = `3`

The pathfinding algorithm will avoid using diagonals if any obstacle has
been placed around the neighboring cells of the specific path segment.

:::: {#class_AStarGrid2D_constant_DIAGONAL_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} **DIAGONAL_MODE_MAX** = `4`

Represents the size of the
`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AStarGrid2D_CellShape}
::: rst-class
classref-enumeration
:::
::::

enum **CellShape**: `🔗<enum_AStarGrid2D_CellShape>`{.interpreted-text
role="ref"}

:::: {#class_AStarGrid2D_constant_CELL_SHAPE_SQUARE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
**CELL_SHAPE_SQUARE** = `0`

Rectangular cell shape.

:::: {#class_AStarGrid2D_constant_CELL_SHAPE_ISOMETRIC_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
**CELL_SHAPE_ISOMETRIC_RIGHT** = `1`

Diamond cell shape (for isometric look). Cell coordinates layout where
the horizontal axis goes up-right, and the vertical one goes down-right.

:::: {#class_AStarGrid2D_constant_CELL_SHAPE_ISOMETRIC_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
**CELL_SHAPE_ISOMETRIC_DOWN** = `2`

Diamond cell shape (for isometric look). Cell coordinates layout where
the horizontal axis goes down-right, and the vertical one goes
down-left.

:::: {#class_AStarGrid2D_constant_CELL_SHAPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
**CELL_SHAPE_MAX** = `3`

Represents the size of the
`CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AStarGrid2D_property_cell_shape}
::: rst-class
classref-property
:::
::::

`CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
**cell_shape** = `0`
`🔗<class_AStarGrid2D_property_cell_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_shape**(value:
  `CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"})
- `CellShape<enum_AStarGrid2D_CellShape>`{.interpreted-text role="ref"}
  **get_cell_shape**()

The cell shape. Affects how the positions are placed in the grid. If
changed, `update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} needs to be called before finding the next path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_cell_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **cell_size** =
`Vector2(1, 1)`
`🔗<class_AStarGrid2D_property_cell_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_cell_size**()

The size of the point cell which will be applied to calculate the
resulting point position returned by
`get_point_path()<class_AStarGrid2D_method_get_point_path>`{.interpreted-text
role="ref"}. If changed,
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} needs to be called before finding the next path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_default_compute_heuristic}
::: rst-class
classref-property
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**default_compute_heuristic** = `0`
`🔗<class_AStarGrid2D_property_default_compute_heuristic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_compute_heuristic**(value:
  `Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"})
- `Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
  **get_default_compute_heuristic**()

The default `Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text
role="ref"} which will be used to calculate the cost between two points
if
`_compute_cost()<class_AStarGrid2D_private_method__compute_cost>`{.interpreted-text
role="ref"} was not overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_default_estimate_heuristic}
::: rst-class
classref-property
:::
::::

`Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
**default_estimate_heuristic** = `0`
`🔗<class_AStarGrid2D_property_default_estimate_heuristic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_estimate_heuristic**(value:
  `Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"})
- `Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text role="ref"}
  **get_default_estimate_heuristic**()

The default `Heuristic<enum_AStarGrid2D_Heuristic>`{.interpreted-text
role="ref"} which will be used to calculate the cost between the point
and the end point if
`_estimate_cost()<class_AStarGrid2D_private_method__estimate_cost>`{.interpreted-text
role="ref"} was not overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_diagonal_mode}
::: rst-class
classref-property
:::
::::

`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} **diagonal_mode** = `0`
`🔗<class_AStarGrid2D_property_diagonal_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_diagonal_mode**(value:
  `DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
  role="ref"})
- `DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
  role="ref"} **get_diagonal_mode**()

A specific
`DiagonalMode<enum_AStarGrid2D_DiagonalMode>`{.interpreted-text
role="ref"} mode which will force the path to avoid or accept the
specified diagonals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_jumping_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **jumping_enabled** =
`false`
`🔗<class_AStarGrid2D_property_jumping_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_jumping_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_jumping_enabled**()

Enables or disables jumping to skip up the intermediate points and
speeds up the searching algorithm.

\*\*Note:\*\* Currently, toggling it on disables the consideration of
weight scaling in pathfinding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)`
`🔗<class_AStarGrid2D_property_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The offset of the grid which will be applied to calculate the resulting
point position returned by
`get_point_path()<class_AStarGrid2D_method_get_point_path>`{.interpreted-text
role="ref"}. If changed,
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} needs to be called before finding the next path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_region}
::: rst-class
classref-property
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **region** =
`Rect2i(0, 0, 0, 0)`
`🔗<class_AStarGrid2D_property_region>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region**(value: `Rect2i<class_Rect2i>`{.interpreted-text
  role="ref"})
- `Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **get_region**()

The region of grid cells available for pathfinding. If changed,
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} needs to be called before finding the next path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_property_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **size** =
`Vector2i(0, 0)` `🔗<class_AStarGrid2D_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_size**()

**Deprecated:** Use
`region<class_AStarGrid2D_property_region>`{.interpreted-text
role="ref"} instead.

The size of the grid (number of cells of size
`cell_size<class_AStarGrid2D_property_cell_size>`{.interpreted-text
role="ref"} on each axis). If changed,
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} needs to be called before finding the next path.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AStarGrid2D_private_method__compute_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_compute_cost**(from_id: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, to_id: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_private_method__compute_cost>`{.interpreted-text
role="ref"}

Called when computing the cost between two connected points.

Note that this function is hidden in the default **AStarGrid2D** class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_private_method__estimate_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_estimate_cost**(from_id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, end_id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_private_method__estimate_cost>`{.interpreted-text
role="ref"}

Called when estimating the cost between a point and the path\'s ending
point.

Note that this function is hidden in the default **AStarGrid2D** class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_AStarGrid2D_method_clear>`{.interpreted-text role="ref"}

Clears the grid and sets the
`region<class_AStarGrid2D_property_region>`{.interpreted-text
role="ref"} to `Rect2i(0, 0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_fill_solid_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fill_solid_region**(region: `Rect2i<class_Rect2i>`{.interpreted-text
role="ref"}, solid: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_AStarGrid2D_method_fill_solid_region>`{.interpreted-text
role="ref"}

Fills the given `region` on the grid with the specified value for the
solid flag.

\*\*Note:\*\* Calling
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} is not needed after the call of this function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_fill_weight_scale_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fill_weight_scale_region**(region:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}, weight_scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AStarGrid2D_method_fill_weight_scale_region>`{.interpreted-text
role="ref"}

Fills the given `region` on the grid with the specified value for the
weight scale.

\*\*Note:\*\* Calling
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} is not needed after the call of this function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_get_id_path}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_id_path**(from_id: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, to_id: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, allow_partial_path: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_AStarGrid2D_method_get_id_path>`{.interpreted-text role="ref"}

Returns an array with the IDs of the points that form the path found by
AStar2D between the given points. The array is ordered from the starting
point to the ending point of the path.

If there is no valid path to the target, and `allow_partial_path` is
`true`, returns a path to the point closest to the target that can be
reached.

\*\*Note:\*\* When `allow_partial_path` is `true` and `to_id` is solid
the search may take an unusually long time to finish.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_get_point_data_in_region}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_point_data_in_region**(region:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_method_get_point_data_in_region>`{.interpreted-text
role="ref"}

Returns an array of dictionaries with point data (`id`:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, `position`:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, `solid`:
`bool<class_bool>`{.interpreted-text role="ref"}, `weight_scale`:
`float<class_float>`{.interpreted-text role="ref"}) within a `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_get_point_path}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_point_path**(from_id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, to_id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
allow_partial_path: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_AStarGrid2D_method_get_point_path>`{.interpreted-text
role="ref"}

Returns an array with the points that are in the path found by
**AStarGrid2D** between the given points. The array is ordered from the
starting point to the ending point of the path.

If there is no valid path to the target, and `allow_partial_path` is
`true`, returns a path to the point closest to the target that can be
reached.

\*\*Note:\*\* This method is not thread-safe. If called from a
`Thread<class_Thread>`{.interpreted-text role="ref"}, it will return an
empty array and will print an error message.

Additionally, when `allow_partial_path` is `true` and `to_id` is solid
the search may take an unusually long time to finish.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_get_point_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_position**(id: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the position of the point associated with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_get_point_weight_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_weight_scale**(id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_method_get_point_weight_scale>`{.interpreted-text
role="ref"}

Returns the weight scale of the point associated with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_is_dirty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_dirty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AStarGrid2D_method_is_dirty>`{.interpreted-text
role="ref"}

Indicates that the grid parameters were changed and
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} needs to be called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_is_in_bounds}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_in_bounds**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_method_is_in_bounds>`{.interpreted-text
role="ref"}

Returns `true` if the `x` and `y` is a valid grid coordinate (id), i.e.
if it is inside
`region<class_AStarGrid2D_property_region>`{.interpreted-text
role="ref"}. Equivalent to `region.has_point(Vector2i(x, y))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_is_in_boundsv}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_in_boundsv**(id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_method_is_in_boundsv>`{.interpreted-text
role="ref"}

Returns `true` if the `id` vector is a valid grid coordinate, i.e. if it
is inside `region<class_AStarGrid2D_property_region>`{.interpreted-text
role="ref"}. Equivalent to `region.has_point(id)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_is_point_solid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_point_solid**(id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStarGrid2D_method_is_point_solid>`{.interpreted-text
role="ref"}

Returns `true` if a point is disabled for pathfinding. By default, all
points are enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_set_point_solid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_solid**(id: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, solid: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_AStarGrid2D_method_set_point_solid>`{.interpreted-text
role="ref"}

Disables or enables the specified point for pathfinding. Useful for
making an obstacle. By default, all points are enabled.

\*\*Note:\*\* Calling
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} is not needed after the call of this function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_set_point_weight_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_weight_scale**(id:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, weight_scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AStarGrid2D_method_set_point_weight_scale>`{.interpreted-text
role="ref"}

Sets the `weight_scale` for the point with the given `id`. The
`weight_scale` is multiplied by the result of
`_compute_cost()<class_AStarGrid2D_private_method__compute_cost>`{.interpreted-text
role="ref"} when determining the overall cost of traveling across a
segment from a neighboring point to this point.

\*\*Note:\*\* Calling
`update()<class_AStarGrid2D_method_update>`{.interpreted-text
role="ref"} is not needed after the call of this function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStarGrid2D_method_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **update**()
`🔗<class_AStarGrid2D_method_update>`{.interpreted-text role="ref"}

Updates the internal state of the grid according to the parameters to
prepare it to search the path. Needs to be called if parameters like
`region<class_AStarGrid2D_property_region>`{.interpreted-text
role="ref"},
`cell_size<class_AStarGrid2D_property_cell_size>`{.interpreted-text
role="ref"} or
`offset<class_AStarGrid2D_property_offset>`{.interpreted-text
role="ref"} are changed.
`is_dirty()<class_AStarGrid2D_method_is_dirty>`{.interpreted-text
role="ref"} will return `true` if this is the case and this needs to be
called.

\*\*Note:\*\* All point data (solidity and weight scale) will be
cleared.
