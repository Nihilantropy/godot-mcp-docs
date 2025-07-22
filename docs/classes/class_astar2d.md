github_url
:   hide

# AStar2D {#class_AStar2D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An implementation of A\* for finding the shortest path between two
vertices on a connected graph in 2D space.

::: rst-class
classref-introduction-group
:::

## Description

An implementation of the A\* algorithm, used to find the shortest path
between two vertices on a connected graph in 2D space.

See `AStar3D<class_AStar3D>`{.interpreted-text role="ref"} for a more
thorough explanation on how to use this class. **AStar2D** is a wrapper
for `AStar3D<class_AStar3D>`{.interpreted-text role="ref"} that enforces
2D coordinates.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Grid-based Navigation with AStarGrid2D
  Demo](https://godotengine.org/asset-library/asset/2723)

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

:::: {#class_AStar2D_private_method__compute_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_compute_cost**(from_id: `int<class_int>`{.interpreted-text
role="ref"}, to_id: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_private_method__compute_cost>`{.interpreted-text
role="ref"}

Called when computing the cost between two connected points.

Note that this function is hidden in the default **AStar2D** class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_private_method__estimate_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_estimate_cost**(from_id: `int<class_int>`{.interpreted-text
role="ref"}, end_id: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_private_method__estimate_cost>`{.interpreted-text
role="ref"}

Called when estimating the cost between a point and the path\'s ending
point.

Note that this function is hidden in the default **AStar2D** class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_add_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_point**(id: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
weight_scale: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_AStar2D_method_add_point>`{.interpreted-text role="ref"}

Adds a new point at the given position with the given identifier. The
`id` must be 0 or larger, and the `weight_scale` must be 0.0 or greater.

The `weight_scale` is multiplied by the result of
`_compute_cost()<class_AStar2D_private_method__compute_cost>`{.interpreted-text
role="ref"} when determining the overall cost of traveling across a
segment from a neighboring point to this point. Thus, all else being
equal, the algorithm prefers points with lower `weight_scale`s to form a
path.

::::: tabs
::: code-tab
gdscript

var astar = AStar2D.new() astar.add_point(1, Vector2(1, 0), 4) \# Adds
the point (1, 0) with weight_scale 4 and id 1
:::

::: code-tab
csharp

var astar = new AStar2D(); astar.AddPoint(1, new Vector2(1, 0), 4); //
Adds the point (1, 0) with weight_scale 4 and id 1
:::
:::::

If there already exists a point for the given `id`, its position and
weight scale are updated to the given values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_are_points_connected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**are_points_connected**(id: `int<class_int>`{.interpreted-text
role="ref"}, to_id: `int<class_int>`{.interpreted-text role="ref"},
bidirectional: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_are_points_connected>`{.interpreted-text
role="ref"}

Returns whether there is a connection/segment between the given points.
If `bidirectional` is `false`, returns whether movement from `id` to
`to_id` is possible through this segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_AStar2D_method_clear>`{.interpreted-text role="ref"}

Clears all the points and segments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_connect_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**connect_points**(id: `int<class_int>`{.interpreted-text role="ref"},
to_id: `int<class_int>`{.interpreted-text role="ref"}, bidirectional:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_AStar2D_method_connect_points>`{.interpreted-text role="ref"}

Creates a segment between the given points. If `bidirectional` is
`false`, only movement from `id` to `to_id` is allowed, not the reverse
direction.

::::: tabs
::: code-tab
gdscript

var astar = AStar2D.new() astar.add_point(1, Vector2(1, 1))
astar.add_point(2, Vector2(0, 5)) astar.connect_points(1, 2, false)
:::

::: code-tab
csharp

var astar = new AStar2D(); astar.AddPoint(1, new Vector2(1, 1));
astar.AddPoint(2, new Vector2(0, 5)); astar.ConnectPoints(1, 2, false);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_disconnect_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_points**(id: `int<class_int>`{.interpreted-text
role="ref"}, to_id: `int<class_int>`{.interpreted-text role="ref"},
bidirectional: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_AStar2D_method_disconnect_points>`{.interpreted-text
role="ref"}

Deletes the segment between the given points. If `bidirectional` is
`false`, only movement from `id` to `to_id` is prevented, and a
unidirectional segment possibly remains.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_available_point_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_available_point_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_available_point_id>`{.interpreted-text
role="ref"}

Returns the next available point ID with no point associated to it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_closest_point}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_closest_point**(to_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
include_disabled: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_closest_point>`{.interpreted-text
role="ref"}

Returns the ID of the closest point to `to_position`, optionally taking
disabled points into account. Returns `-1` if there are no points in the
points pool.

\*\*Note:\*\* If several points are the closest to `to_position`, the
one with the smallest ID will be returned, ensuring a deterministic
result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_closest_position_in_segment}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_closest_position_in_segment**(to_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_closest_position_in_segment>`{.interpreted-text
role="ref"}

Returns the closest position to `to_position` that resides inside a
segment between two connected points.

::::: tabs
::: code-tab
gdscript

var astar = AStar2D.new() astar.add_point(1, Vector2(0, 0))
astar.add_point(2, Vector2(0, 5)) astar.connect_points(1, 2) var res =
astar.get_closest_position_in_segment(Vector2(3, 3)) \# Returns (0, 3)
:::

::: code-tab
csharp

var astar = new AStar2D(); astar.AddPoint(1, new Vector2(0, 0));
astar.AddPoint(2, new Vector2(0, 5)); astar.ConnectPoints(1, 2); Vector2
res = astar.GetClosestPositionInSegment(new Vector2(3, 3)); // Returns
(0, 3)
:::
:::::

The result is in the segment that goes from `y = 0` to `y = 5`. It\'s
the closest position in the segment to the given point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_id_path}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**get_id_path**(from_id: `int<class_int>`{.interpreted-text role="ref"},
to_id: `int<class_int>`{.interpreted-text role="ref"},
allow_partial_path: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_AStar2D_method_get_id_path>`{.interpreted-text
role="ref"}

Returns an array with the IDs of the points that form the path found by
AStar2D between the given points. The array is ordered from the starting
point to the ending point of the path.

If there is no valid path to the target, and `allow_partial_path` is
`true`, returns a path to the point closest to the target that can be
reached.

\*\*Note:\*\* When `allow_partial_path` is `true` and `to_id` is
disabled the search may take an unusually long time to finish.

::::: tabs
::: code-tab
gdscript

var astar = AStar2D.new() astar.add_point(1, Vector2(0, 0))
astar.add_point(2, Vector2(0, 1), 1) \# Default weight is 1
astar.add_point(3, Vector2(1, 1)) astar.add_point(4, Vector2(2, 0))

astar.connect_points(1, 2, false) astar.connect_points(2, 3, false)
astar.connect_points(4, 3, false) astar.connect_points(1, 4, false)

var res = astar.get_id_path(1, 3) \# Returns \[1, 2, 3\]
:::

::: code-tab
csharp

var astar = new AStar2D(); astar.AddPoint(1, new Vector2(0, 0));
astar.AddPoint(2, new Vector2(0, 1), 1); // Default weight is 1
astar.AddPoint(3, new Vector2(1, 1)); astar.AddPoint(4, new Vector2(2,
0));

astar.ConnectPoints(1, 2, false); astar.ConnectPoints(2, 3, false);
astar.ConnectPoints(4, 3, false); astar.ConnectPoints(1, 4, false);
long\[\] res = astar.GetIdPath(1, 3); // Returns \[1, 2, 3\]
:::
:::::

If you change the 2nd point\'s weight to 3, then the result will be
`[1, 4, 3]` instead, because now even though the distance is longer,
it\'s \"easier\" to get through point 4 than through point 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_capacity}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_point_capacity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_point_capacity>`{.interpreted-text
role="ref"}

Returns the capacity of the structure backing the points, useful in
conjunction with
`reserve_space()<class_AStar2D_method_reserve_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_connections}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**get_point_connections**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AStar2D_method_get_point_connections>`{.interpreted-text
role="ref"}

Returns an array with the IDs of the points that form the connection
with the given point.

::::: tabs
::: code-tab
gdscript

var astar = AStar2D.new() astar.add_point(1, Vector2(0, 0))
astar.add_point(2, Vector2(0, 1)) astar.add_point(3, Vector2(1, 1))
astar.add_point(4, Vector2(2, 0))

astar.connect_points(1, 2, true) astar.connect_points(1, 3, true)

var neighbors = astar.get_point_connections(1) \# Returns \[2, 3\]
:::

::: code-tab
csharp

var astar = new AStar2D(); astar.AddPoint(1, new Vector2(0, 0));
astar.AddPoint(2, new Vector2(0, 1)); astar.AddPoint(3, new Vector2(1,
1)); astar.AddPoint(4, new Vector2(2, 0));

astar.ConnectPoints(1, 2, true); astar.ConnectPoints(1, 3, true);

long\[\] neighbors = astar.GetPointConnections(1); // Returns \[2, 3\]
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_point_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_point_count>`{.interpreted-text role="ref"}

Returns the number of points currently in the points pool.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_ids}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**get_point_ids**()
`🔗<class_AStar2D_method_get_point_ids>`{.interpreted-text role="ref"}

Returns an array of all point IDs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_path}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_point_path**(from_id:
`int<class_int>`{.interpreted-text role="ref"}, to_id:
`int<class_int>`{.interpreted-text role="ref"}, allow_partial_path:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_AStar2D_method_get_point_path>`{.interpreted-text role="ref"}

Returns an array with the points that are in the path found by AStar2D
between the given points. The array is ordered from the starting point
to the ending point of the path.

If there is no valid path to the target, and `allow_partial_path` is
`true`, returns a path to the point closest to the target that can be
reached.

\*\*Note:\*\* This method is not thread-safe. If called from a
`Thread<class_Thread>`{.interpreted-text role="ref"}, it will return an
empty array and will print an error message.

Additionally, when `allow_partial_path` is `true` and `to_id` is
disabled the search may take an unusually long time to finish.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_position**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the position of the point associated with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_get_point_weight_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_weight_scale**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_get_point_weight_scale>`{.interpreted-text
role="ref"}

Returns the weight scale of the point associated with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_has_point}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_point**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AStar2D_method_has_point>`{.interpreted-text
role="ref"}

Returns whether a point associated with the given `id` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_is_point_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_disabled**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar2D_method_is_point_disabled>`{.interpreted-text
role="ref"}

Returns whether a point is disabled or not for pathfinding. By default,
all points are enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_remove_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AStar2D_method_remove_point>`{.interpreted-text role="ref"}

Removes the point associated with the given `id` from the points pool.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_reserve_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reserve_space**(num_nodes: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_AStar2D_method_reserve_space>`{.interpreted-text
role="ref"}

Reserves space internally for `num_nodes` points. Useful if you\'re
adding a known large number of points at once, such as points on a grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_set_point_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_disabled**(id: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"}
= true) `🔗<class_AStar2D_method_set_point_disabled>`{.interpreted-text
role="ref"}

Disables or enables the specified point for pathfinding. Useful for
making a temporary obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_set_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_position**(id: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_AStar2D_method_set_point_position>`{.interpreted-text
role="ref"}

Sets the `position` for the point with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar2D_method_set_point_weight_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_weight_scale**(id: `int<class_int>`{.interpreted-text
role="ref"}, weight_scale: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AStar2D_method_set_point_weight_scale>`{.interpreted-text
role="ref"}

Sets the `weight_scale` for the point with the given `id`. The
`weight_scale` is multiplied by the result of
`_compute_cost()<class_AStar2D_private_method__compute_cost>`{.interpreted-text
role="ref"} when determining the overall cost of traveling across a
segment from a neighboring point to this point.
