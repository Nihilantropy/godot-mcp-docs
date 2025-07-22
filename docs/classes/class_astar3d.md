github_url
:   hide

# AStar3D {#class_AStar3D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An implementation of A\* for finding the shortest path between two
vertices on a connected graph in 3D space.

::: rst-class
classref-introduction-group
:::

## Description

A\* (A star) is a computer algorithm used in pathfinding and graph
traversal, the process of plotting short paths among vertices (points),
passing through a given set of edges (segments). It enjoys widespread
use due to its performance and accuracy. Godot\'s A\* implementation
uses points in 3D space and Euclidean distances by default.

You must add points manually with
`add_point()<class_AStar3D_method_add_point>`{.interpreted-text
role="ref"} and create segments manually with
`connect_points()<class_AStar3D_method_connect_points>`{.interpreted-text
role="ref"}. Once done, you can test if there is a path between two
points with the
`are_points_connected()<class_AStar3D_method_are_points_connected>`{.interpreted-text
role="ref"} function, get a path containing indices by
`get_id_path()<class_AStar3D_method_get_id_path>`{.interpreted-text
role="ref"}, or one containing actual coordinates with
`get_point_path()<class_AStar3D_method_get_point_path>`{.interpreted-text
role="ref"}.

It is also possible to use non-Euclidean distances. To do so, create a
script that extends **AStar3D** and override the methods
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} and
`_estimate_cost()<class_AStar3D_private_method__estimate_cost>`{.interpreted-text
role="ref"}. Both should take two point IDs and return the distance
between the corresponding points.

\*\*Example:\*\* Use Manhattan distance instead of Euclidean distance:

::::: tabs
::: code-tab
gdscript

class_name MyAStar3D extends AStar3D

func [compute_cost]{#compute_cost}(u, v):

:   var u_pos = get_point_position(u) var v_pos = get_point_position(v)
    return abs(u_pos.x - v_pos.x) + abs(u_pos.y - v_pos.y) +
    abs(u_pos.z - v_pos.z)

func [estimate_cost]{#estimate_cost}(u, v):

:   var u_pos = get_point_position(u) var v_pos = get_point_position(v)
    return abs(u_pos.x - v_pos.x) + abs(u_pos.y - v_pos.y) +
    abs(u_pos.z - v_pos.z)
:::

::: code-tab
csharp

using Godot;

\[GlobalClass\] public partial class MyAStar3D : AStar3D { public
override float [ComputeCost]{#computecost}(long fromId, long toId) {
Vector3 fromPoint = GetPointPosition(fromId); Vector3 toPoint =
GetPointPosition(toId);

> return Mathf.Abs(fromPoint.X - toPoint.X) + Mathf.Abs(fromPoint.Y -
> toPoint.Y) + Mathf.Abs(fromPoint.Z - toPoint.Z); }
>
> public override float [EstimateCost]{#estimatecost}(long fromId, long
> toId) { Vector3 fromPoint = GetPointPosition(fromId); Vector3 toPoint
> = GetPointPosition(toId); return Mathf.Abs(fromPoint.X - toPoint.X) +
> Mathf.Abs(fromPoint.Y - toPoint.Y) + Mathf.Abs(fromPoint.Z -
> toPoint.Z); }

}
:::
:::::

`_estimate_cost()<class_AStar3D_private_method__estimate_cost>`{.interpreted-text
role="ref"} should return a lower bound of the distance, i.e.
`_estimate_cost(u, v) <= _compute_cost(u, v)`. This serves as a hint to
the algorithm because the custom
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} might be computation-heavy. If this is not the case, make
`_estimate_cost()<class_AStar3D_private_method__estimate_cost>`{.interpreted-text
role="ref"} return the same value as
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} to provide the algorithm with the most accurate information.

If the default
`_estimate_cost()<class_AStar3D_private_method__estimate_cost>`{.interpreted-text
role="ref"} and
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} methods are used, or if the supplied
`_estimate_cost()<class_AStar3D_private_method__estimate_cost>`{.interpreted-text
role="ref"} method returns a lower bound of the cost, then the paths
returned by A\* will be the lowest-cost paths. Here, the cost of a path
equals the sum of the
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} results of all segments in the path multiplied by the
`weight_scale`s of the endpoints of the respective segments. If the
default methods are used and the `weight_scale`s of all points are set
to `1.0`, then this equals the sum of Euclidean distances of all
segments in the path.

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

:::: {#class_AStar3D_private_method__compute_cost}
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
`🔗<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"}

Called when computing the cost between two connected points.

Note that this function is hidden in the default **AStar3D** class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_private_method__estimate_cost}
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
`🔗<class_AStar3D_private_method__estimate_cost>`{.interpreted-text
role="ref"}

Called when estimating the cost between a point and the path\'s ending
point.

Note that this function is hidden in the default **AStar3D** class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_add_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_point**(id: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
weight_scale: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_AStar3D_method_add_point>`{.interpreted-text role="ref"}

Adds a new point at the given position with the given identifier. The
`id` must be 0 or larger, and the `weight_scale` must be 0.0 or greater.

The `weight_scale` is multiplied by the result of
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} when determining the overall cost of traveling across a
segment from a neighboring point to this point. Thus, all else being
equal, the algorithm prefers points with lower `weight_scale`s to form a
path.

::::: tabs
::: code-tab
gdscript

var astar = AStar3D.new() astar.add_point(1, Vector3(1, 0, 0), 4) \#
Adds the point (1, 0, 0) with weight_scale 4 and id 1
:::

::: code-tab
csharp

var astar = new AStar3D(); astar.AddPoint(1, new Vector3(1, 0, 0), 4);
// Adds the point (1, 0, 0) with weight_scale 4 and id 1
:::
:::::

If there already exists a point for the given `id`, its position and
weight scale are updated to the given values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_are_points_connected}
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
`🔗<class_AStar3D_method_are_points_connected>`{.interpreted-text
role="ref"}

Returns whether the two given points are directly connected by a
segment. If `bidirectional` is `false`, returns whether movement from
`id` to `to_id` is possible through this segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_AStar3D_method_clear>`{.interpreted-text role="ref"}

Clears all the points and segments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_connect_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**connect_points**(id: `int<class_int>`{.interpreted-text role="ref"},
to_id: `int<class_int>`{.interpreted-text role="ref"}, bidirectional:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_AStar3D_method_connect_points>`{.interpreted-text role="ref"}

Creates a segment between the given points. If `bidirectional` is
`false`, only movement from `id` to `to_id` is allowed, not the reverse
direction.

::::: tabs
::: code-tab
gdscript

var astar = AStar3D.new() astar.add_point(1, Vector3(1, 1, 0))
astar.add_point(2, Vector3(0, 5, 0)) astar.connect_points(1, 2, false)
:::

::: code-tab
csharp

var astar = new AStar3D(); astar.AddPoint(1, new Vector3(1, 1, 0));
astar.AddPoint(2, new Vector3(0, 5, 0)); astar.ConnectPoints(1, 2,
false);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_disconnect_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_points**(id: `int<class_int>`{.interpreted-text
role="ref"}, to_id: `int<class_int>`{.interpreted-text role="ref"},
bidirectional: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_AStar3D_method_disconnect_points>`{.interpreted-text
role="ref"}

Deletes the segment between the given points. If `bidirectional` is
`false`, only movement from `id` to `to_id` is prevented, and a
unidirectional segment possibly remains.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_available_point_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_available_point_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_available_point_id>`{.interpreted-text
role="ref"}

Returns the next available point ID with no point associated to it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_closest_point}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_closest_point**(to_position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
include_disabled: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_closest_point>`{.interpreted-text
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

:::: {#class_AStar3D_method_get_closest_position_in_segment}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_closest_position_in_segment**(to_position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_closest_position_in_segment>`{.interpreted-text
role="ref"}

Returns the closest position to `to_position` that resides inside a
segment between two connected points.

::::: tabs
::: code-tab
gdscript

var astar = AStar3D.new() astar.add_point(1, Vector3(0, 0, 0))
astar.add_point(2, Vector3(0, 5, 0)) astar.connect_points(1, 2) var res
= astar.get_closest_position_in_segment(Vector3(3, 3, 0)) \# Returns (0,
3, 0)
:::

::: code-tab
csharp

var astar = new AStar3D(); astar.AddPoint(1, new Vector3(0, 0, 0));
astar.AddPoint(2, new Vector3(0, 5, 0)); astar.ConnectPoints(1, 2);
Vector3 res = astar.GetClosestPositionInSegment(new Vector3(3, 3, 0));
// Returns (0, 3, 0)
:::
:::::

The result is in the segment that goes from `y = 0` to `y = 5`. It\'s
the closest position in the segment to the given point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_id_path}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**get_id_path**(from_id: `int<class_int>`{.interpreted-text role="ref"},
to_id: `int<class_int>`{.interpreted-text role="ref"},
allow_partial_path: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_AStar3D_method_get_id_path>`{.interpreted-text
role="ref"}

Returns an array with the IDs of the points that form the path found by
AStar3D between the given points. The array is ordered from the starting
point to the ending point of the path.

If there is no valid path to the target, and `allow_partial_path` is
`true`, returns a path to the point closest to the target that can be
reached.

\*\*Note:\*\* When `allow_partial_path` is `true` and `to_id` is
disabled the search may take an unusually long time to finish.

::::: tabs
::: code-tab
gdscript

var astar = AStar3D.new() astar.add_point(1, Vector3(0, 0, 0))
astar.add_point(2, Vector3(0, 1, 0), 1) \# Default weight is 1
astar.add_point(3, Vector3(1, 1, 0)) astar.add_point(4, Vector3(2, 0,
0))

astar.connect_points(1, 2, false) astar.connect_points(2, 3, false)
astar.connect_points(4, 3, false) astar.connect_points(1, 4, false)

var res = astar.get_id_path(1, 3) \# Returns \[1, 2, 3\]
:::

::: code-tab
csharp

var astar = new AStar3D(); astar.AddPoint(1, new Vector3(0, 0, 0));
astar.AddPoint(2, new Vector3(0, 1, 0), 1); // Default weight is 1
astar.AddPoint(3, new Vector3(1, 1, 0)); astar.AddPoint(4, new
Vector3(2, 0, 0)); astar.ConnectPoints(1, 2, false);
astar.ConnectPoints(2, 3, false); astar.ConnectPoints(4, 3, false);
astar.ConnectPoints(1, 4, false); long\[\] res = astar.GetIdPath(1, 3);
// Returns \[1, 2, 3\]
:::
:::::

If you change the 2nd point\'s weight to 3, then the result will be
`[1, 4, 3]` instead, because now even though the distance is longer,
it\'s \"easier\" to get through point 4 than through point 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_point_capacity}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_point_capacity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_point_capacity>`{.interpreted-text
role="ref"}

Returns the capacity of the structure backing the points, useful in
conjunction with
`reserve_space()<class_AStar3D_method_reserve_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_point_connections}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**get_point_connections**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AStar3D_method_get_point_connections>`{.interpreted-text
role="ref"}

Returns an array with the IDs of the points that form the connection
with the given point.

::::: tabs
::: code-tab
gdscript

var astar = AStar3D.new() astar.add_point(1, Vector3(0, 0, 0))
astar.add_point(2, Vector3(0, 1, 0)) astar.add_point(3, Vector3(1, 1,
0)) astar.add_point(4, Vector3(2, 0, 0))

astar.connect_points(1, 2, true) astar.connect_points(1, 3, true)

var neighbors = astar.get_point_connections(1) \# Returns \[2, 3\]
:::

::: code-tab
csharp

var astar = new AStar3D(); astar.AddPoint(1, new Vector3(0, 0, 0));
astar.AddPoint(2, new Vector3(0, 1, 0)); astar.AddPoint(3, new
Vector3(1, 1, 0)); astar.AddPoint(4, new Vector3(2, 0, 0));
astar.ConnectPoints(1, 2, true); astar.ConnectPoints(1, 3, true);

long\[\] neighbors = astar.GetPointConnections(1); // Returns \[2, 3\]
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_point_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_point_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_point_count>`{.interpreted-text role="ref"}

Returns the number of points currently in the points pool.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_point_ids}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**get_point_ids**()
`🔗<class_AStar3D_method_get_point_ids>`{.interpreted-text role="ref"}

Returns an array of all point IDs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_point_path}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_point_path**(from_id:
`int<class_int>`{.interpreted-text role="ref"}, to_id:
`int<class_int>`{.interpreted-text role="ref"}, allow_partial_path:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_AStar3D_method_get_point_path>`{.interpreted-text role="ref"}

Returns an array with the points that are in the path found by AStar3D
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

:::: {#class_AStar3D_method_get_point_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_point_position**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the position of the point associated with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_get_point_weight_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_weight_scale**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_get_point_weight_scale>`{.interpreted-text
role="ref"}

Returns the weight scale of the point associated with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_has_point}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_point**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AStar3D_method_has_point>`{.interpreted-text
role="ref"}

Returns whether a point associated with the given `id` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_is_point_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_disabled**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AStar3D_method_is_point_disabled>`{.interpreted-text
role="ref"}

Returns whether a point is disabled or not for pathfinding. By default,
all points are enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_remove_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AStar3D_method_remove_point>`{.interpreted-text role="ref"}

Removes the point associated with the given `id` from the points pool.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_reserve_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reserve_space**(num_nodes: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_AStar3D_method_reserve_space>`{.interpreted-text
role="ref"}

Reserves space internally for `num_nodes` points. Useful if you\'re
adding a known large number of points at once, such as points on a grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_set_point_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_disabled**(id: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"}
= true) `🔗<class_AStar3D_method_set_point_disabled>`{.interpreted-text
role="ref"}

Disables or enables the specified point for pathfinding. Useful for
making a temporary obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_set_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_position**(id: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_AStar3D_method_set_point_position>`{.interpreted-text
role="ref"}

Sets the `position` for the point with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AStar3D_method_set_point_weight_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_weight_scale**(id: `int<class_int>`{.interpreted-text
role="ref"}, weight_scale: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AStar3D_method_set_point_weight_scale>`{.interpreted-text
role="ref"}

Sets the `weight_scale` for the point with the given `id`. The
`weight_scale` is multiplied by the result of
`_compute_cost()<class_AStar3D_private_method__compute_cost>`{.interpreted-text
role="ref"} when determining the overall cost of traveling across a
segment from a neighboring point to this point.
