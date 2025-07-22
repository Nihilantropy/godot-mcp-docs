github_url
:   hide

# Geometry2D {#class_Geometry2D}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides methods for some common 2D geometric operations.

::: rst-class
classref-introduction-group
:::

## Description

Provides a set of helper functions to create geometric shapes, compute
intersections between shapes, and process various other geometric
operations in 2D.

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

:::: {#enum_Geometry2D_PolyBooleanOperation}
::: rst-class
classref-enumeration
:::
::::

enum **PolyBooleanOperation**:
`🔗<enum_Geometry2D_PolyBooleanOperation>`{.interpreted-text role="ref"}

:::: {#class_Geometry2D_constant_OPERATION_UNION}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>`{.interpreted-text
role="ref"} **OPERATION_UNION** = `0`

Create regions where either subject or clip polygons (or both) are
filled.

:::: {#class_Geometry2D_constant_OPERATION_DIFFERENCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>`{.interpreted-text
role="ref"} **OPERATION_DIFFERENCE** = `1`

Create regions where subject polygons are filled except where clip
polygons are filled.

:::: {#class_Geometry2D_constant_OPERATION_INTERSECTION}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>`{.interpreted-text
role="ref"} **OPERATION_INTERSECTION** = `2`

Create regions where both subject and clip polygons are filled.

:::: {#class_Geometry2D_constant_OPERATION_XOR}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>`{.interpreted-text
role="ref"} **OPERATION_XOR** = `3`

Create regions where either subject or clip polygons are filled but not
where both are filled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Geometry2D_PolyJoinType}
::: rst-class
classref-enumeration
:::
::::

enum **PolyJoinType**:
`🔗<enum_Geometry2D_PolyJoinType>`{.interpreted-text role="ref"}

:::: {#class_Geometry2D_constant_JOIN_SQUARE}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} **JOIN_SQUARE** = `0`

Squaring is applied uniformally at all convex edge joins at `1 * delta`.

:::: {#class_Geometry2D_constant_JOIN_ROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} **JOIN_ROUND** = `1`

While flattened paths can never perfectly trace an arc, they are
approximated by a series of arc chords.

:::: {#class_Geometry2D_constant_JOIN_MITER}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} **JOIN_MITER** = `2`

There\'s a necessary limit to mitered joins since offsetting edges that
join at very acute angles will produce excessively long and narrow
\"spikes\". For any given edge join, when miter offsetting would exceed
that maximum distance, \"square\" joining is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Geometry2D_PolyEndType}
::: rst-class
classref-enumeration
:::
::::

enum **PolyEndType**:
`🔗<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}

:::: {#class_Geometry2D_constant_END_POLYGON}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyEndType<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}
**END_POLYGON** = `0`

Endpoints are joined using the
`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} value and the path filled as a polygon.

:::: {#class_Geometry2D_constant_END_JOINED}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyEndType<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}
**END_JOINED** = `1`

Endpoints are joined using the
`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} value and the path filled as a polyline.

:::: {#class_Geometry2D_constant_END_BUTT}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyEndType<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}
**END_BUTT** = `2`

Endpoints are squared off with no extension.

:::: {#class_Geometry2D_constant_END_SQUARE}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyEndType<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}
**END_SQUARE** = `3`

Endpoints are squared off and extended by `delta` units.

:::: {#class_Geometry2D_constant_END_ROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`PolyEndType<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}
**END_ROUND** = `4`

Endpoints are rounded off and extended by `delta` units.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Geometry2D_method_bresenham_line}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**bresenham_line**(from: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, to: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_bresenham_line>`{.interpreted-text
role="ref"}

Returns the [Bresenham
line](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)
between the `from` and `to` points. A Bresenham line is a series of
pixels that draws a line and is always 1-pixel thick on every row and
column of the drawing (never more, never less).

Example code to draw a line between two
`Marker2D<class_Marker2D>`{.interpreted-text role="ref"} nodes using a
series of
`CanvasItem.draw_rect()<class_CanvasItem_method_draw_rect>`{.interpreted-text
role="ref"} calls:

    func _draw():
        for pixel in Geometry2D.bresenham_line($MarkerA.position, $MarkerB.position):
            draw_rect(Rect2(pixel, Vector2.ONE), Color.WHITE)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_clip_polygons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **clip_polygons**(polygon_a:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, polygon_b:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_clip_polygons>`{.interpreted-text
role="ref"}

Clips `polygon_a` against `polygon_b` and returns an array of clipped
polygons. This performs
`OPERATION_DIFFERENCE<class_Geometry2D_constant_OPERATION_DIFFERENCE>`{.interpreted-text
role="ref"} between polygons. Returns an empty array if `polygon_b`
completely overlaps `polygon_a`.

If `polygon_b` is enclosed by `polygon_a`, returns an outer polygon
(boundary) and inner polygon (hole) which could be distinguished by
calling
`is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_clip_polyline_with_polygon}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **clip_polyline_with_polygon**(polyline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_clip_polyline_with_polygon>`{.interpreted-text
role="ref"}

Clips `polyline` against `polygon` and returns an array of clipped
polylines. This performs
`OPERATION_DIFFERENCE<class_Geometry2D_constant_OPERATION_DIFFERENCE>`{.interpreted-text
role="ref"} between the polyline and the polygon. This operation can be
thought of as cutting a line with a closed shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_convex_hull}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **convex_hull**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}) `🔗<class_Geometry2D_method_convex_hull>`{.interpreted-text
role="ref"}

Given an array of `Vector2<class_Vector2>`{.interpreted-text
role="ref"}s, returns the convex hull as a list of points in
counterclockwise order. The last point is the same as the first one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_decompose_polygon_in_convex}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **decompose_polygon_in_convex**(polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_decompose_polygon_in_convex>`{.interpreted-text
role="ref"}

Decomposes the `polygon` into multiple convex hulls and returns an array
of `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_exclude_polygons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **exclude_polygons**(polygon_a:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, polygon_b:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_exclude_polygons>`{.interpreted-text
role="ref"}

Mutually excludes common area defined by intersection of `polygon_a` and
`polygon_b` (see
`intersect_polygons()<class_Geometry2D_method_intersect_polygons>`{.interpreted-text
role="ref"}) and returns an array of excluded polygons. This performs
`OPERATION_XOR<class_Geometry2D_constant_OPERATION_XOR>`{.interpreted-text
role="ref"} between polygons. In other words, returns all but common
area between polygons.

The operation may result in an outer polygon (boundary) and inner
polygon (hole) produced which could be distinguished by calling
`is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_get_closest_point_to_segment}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_closest_point_to_segment**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, s1:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, s2:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Geometry2D_method_get_closest_point_to_segment>`{.interpreted-text
role="ref"}

Returns the 2D point on the 2D segment (`s1`, `s2`) that is closest to
`point`. The returned point will always be inside the specified segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_get_closest_point_to_segment_uncapped}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_closest_point_to_segment_uncapped**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, s1:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, s2:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Geometry2D_method_get_closest_point_to_segment_uncapped>`{.interpreted-text
role="ref"}

Returns the 2D point on the 2D line defined by (`s1`, `s2`) that is
closest to `point`. The returned point can be inside the segment (`s1`,
`s2`) or outside of it, i.e. somewhere on the line extending from the
segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_get_closest_points_between_segments}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_closest_points_between_segments**(p1:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, q1:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, p2:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, q2:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Geometry2D_method_get_closest_points_between_segments>`{.interpreted-text
role="ref"}

Given the two 2D segments (`p1`, `q1`) and (`p2`, `q2`), finds those two
points on the two segments that are closest to each other. Returns a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} that contains this point on (`p1`, `q1`) as well the
accompanying point on (`p2`, `q2`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_intersect_polygons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **intersect_polygons**(polygon_a:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, polygon_b:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_intersect_polygons>`{.interpreted-text
role="ref"}

Intersects `polygon_a` with `polygon_b` and returns an array of
intersected polygons. This performs
`OPERATION_INTERSECTION<class_Geometry2D_constant_OPERATION_INTERSECTION>`{.interpreted-text
role="ref"} between polygons. In other words, returns common area shared
by polygons. Returns an empty array if no intersection occurs.

The operation may result in an outer polygon (boundary) and inner
polygon (hole) produced which could be distinguished by calling
`is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_intersect_polyline_with_polygon}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **intersect_polyline_with_polygon**(polyline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_intersect_polyline_with_polygon>`{.interpreted-text
role="ref"}

Intersects `polyline` with `polygon` and returns an array of intersected
polylines. This performs
`OPERATION_INTERSECTION<class_Geometry2D_constant_OPERATION_INTERSECTION>`{.interpreted-text
role="ref"} between the polyline and the polygon. This operation can be
thought of as chopping a line with a closed shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_is_point_in_circle}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_in_circle**(point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, circle_position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, circle_radius: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_is_point_in_circle>`{.interpreted-text
role="ref"}

Returns `true` if `point` is inside the circle or if it\'s located
exactly *on* the circle\'s boundary, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_is_point_in_polygon}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_in_polygon**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_is_point_in_polygon>`{.interpreted-text
role="ref"}

Returns `true` if `point` is inside `polygon` or if it\'s located
exactly *on* polygon\'s boundary, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_is_polygon_clockwise}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_polygon_clockwise**(polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}

Returns `true` if `polygon`\'s vertices are ordered in clockwise order,
otherwise returns `false`.

\*\*Note:\*\* Assumes a Cartesian coordinate system where `+x` is right
and `+y` is up. If using screen coordinates (`+y` is down), the result
will need to be flipped (i.e. a `true` result will indicate
counter-clockwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_line_intersects_line}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**line_intersects_line**(from_a:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, dir_a:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, from_b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, dir_b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Geometry2D_method_line_intersects_line>`{.interpreted-text
role="ref"}

Returns the point of intersection between the two lines (`from_a`,
`dir_a`) and (`from_b`, `dir_b`). Returns a
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, or `null` if the
lines are parallel.

`from` and `dir` are *not* endpoints of a line segment or ray but the
slope (`dir`) and a known point (`from`) on that line.

::::: tabs
::: code-tab
gdscript

var from_a = Vector2.ZERO var dir_a = Vector2.RIGHT var from_b =
Vector2.DOWN

\# Returns Vector2(1, 0) Geometry2D.line_intersects_line(from_a, dir_a,
from_b, Vector2(1, -1)) \# Returns Vector2(-1, 0)
Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2(-1, -1))
\# Returns null Geometry2D.line_intersects_line(from_a, dir_a, from_b,
Vector2.RIGHT)
:::

::: code-tab
csharp

var fromA = Vector2.Zero; var dirA = Vector2.Right; var fromB =
Vector2.Down;

// Returns new Vector2(1, 0) Geometry2D.LineIntersectsLine(fromA, dirA,
fromB, new Vector2(1, -1)); // Returns new Vector2(-1, 0)
Geometry2D.LineIntersectsLine(fromA, dirA, fromB, new Vector2(-1, -1));
// Returns null Geometry2D.LineIntersectsLine(fromA, dirA, fromB,
Vector2.Right);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_make_atlas}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**make_atlas**(sizes:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}) `🔗<class_Geometry2D_method_make_atlas>`{.interpreted-text
role="ref"}

Given an array of `Vector2<class_Vector2>`{.interpreted-text
role="ref"}s representing tiles, builds an atlas. The returned
dictionary has two keys: `points` is a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} that specifies the positions of each tile, `size` contains
the overall size of the whole atlas as
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_merge_polygons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **merge_polygons**(polygon_a:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, polygon_b:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_merge_polygons>`{.interpreted-text
role="ref"}

Merges (combines) `polygon_a` and `polygon_b` and returns an array of
merged polygons. This performs
`OPERATION_UNION<class_Geometry2D_constant_OPERATION_UNION>`{.interpreted-text
role="ref"} between polygons.

The operation may result in an outer polygon (boundary) and multiple
inner polygons (holes) produced which could be distinguished by calling
`is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_offset_polygon}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **offset_polygon**(polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, delta: `float<class_float>`{.interpreted-text role="ref"},
join_type:
`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} = 0)
`🔗<class_Geometry2D_method_offset_polygon>`{.interpreted-text
role="ref"}

Inflates or deflates `polygon` by `delta` units (pixels). If `delta` is
positive, makes the polygon grow outward. If `delta` is negative,
shrinks the polygon inward. Returns an array of polygons because
inflating/deflating may result in multiple discrete polygons. Returns an
empty array if `delta` is negative and the absolute value of it
approximately exceeds the minimum bounding rectangle dimensions of the
polygon.

Each polygon\'s vertices will be rounded as determined by `join_type`.

The operation may result in an outer polygon (boundary) and inner
polygon (hole) produced which could be distinguished by calling
`is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* To translate the polygon\'s vertices specifically,
multiply them to a `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

var polygon = PackedVector2Array(\[Vector2(0, 0), Vector2(100, 0),
Vector2(100, 100), Vector2(0, 100)\]) var offset = Vector2(50, 50)
polygon = Transform2D(0, offset) \* polygon print(polygon) \# Prints
\[(50.0, 50.0), (150.0, 50.0), (150.0, 150.0), (50.0, 150.0)\]
:::

::: code-tab
csharp

Vector2\[\] polygon = \[new Vector2(0, 0), new Vector2(100, 0), new
Vector2(100, 100), new Vector2(0, 100)\]; var offset = new Vector2(50,
50); polygon = new Transform2D(0, offset) \* polygon;
GD.Print((Variant)polygon); // Prints \[(50, 50), (150, 50), (150, 150),
(50, 150)\]
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_offset_polyline}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **offset_polyline**(polyline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, delta: `float<class_float>`{.interpreted-text role="ref"},
join_type:
`PolyJoinType<enum_Geometry2D_PolyJoinType>`{.interpreted-text
role="ref"} = 0, end_type:
`PolyEndType<enum_Geometry2D_PolyEndType>`{.interpreted-text role="ref"}
= 3) `🔗<class_Geometry2D_method_offset_polyline>`{.interpreted-text
role="ref"}

Inflates or deflates `polyline` by `delta` units (pixels), producing
polygons. If `delta` is positive, makes the polyline grow outward.
Returns an array of polygons because inflating/deflating may result in
multiple discrete polygons. If `delta` is negative, returns an empty
array.

Each polygon\'s vertices will be rounded as determined by `join_type`.

Each polygon\'s endpoints will be rounded as determined by `end_type`.

The operation may result in an outer polygon (boundary) and inner
polygon (hole) produced which could be distinguished by calling
`is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_point_is_inside_triangle}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**point_is_inside_triangle**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, a:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, c:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Geometry2D_method_point_is_inside_triangle>`{.interpreted-text
role="ref"}

Returns if `point` is inside the triangle specified by `a`, `b` and `c`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_segment_intersects_circle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**segment_intersects_circle**(segment_from:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, segment_to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, circle_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, circle_radius:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Geometry2D_method_segment_intersects_circle>`{.interpreted-text
role="ref"}

Given the 2D segment (`segment_from`, `segment_to`), returns the
position on the segment (as a number between 0 and 1) at which the
segment hits the circle that is located at position `circle_position`
and has radius `circle_radius`. If the segment does not intersect the
circle, -1 is returned (this is also the case if the line extending the
segment would intersect the circle, but the segment does not).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_segment_intersects_segment}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**segment_intersects_segment**(from_a:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, to_a:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, from_b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, to_b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Geometry2D_method_segment_intersects_segment>`{.interpreted-text
role="ref"}

Checks if the two segments (`from_a`, `to_a`) and (`from_b`, `to_b`)
intersect. If yes, return the point of intersection as
`Vector2<class_Vector2>`{.interpreted-text role="ref"}. If no
intersection takes place, returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_triangulate_delaunay}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**triangulate_delaunay**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_triangulate_delaunay>`{.interpreted-text
role="ref"}

Triangulates the area specified by discrete set of `points` such that no
point is inside the circumcircle of any resulting triangle. Returns a
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
where each triangle consists of three consecutive point indices into
`points` (i.e. the returned array will have `n * 3` elements, with `n`
being the number of found triangles). If the triangulation did not
succeed, an empty
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry2D_method_triangulate_polygon}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**triangulate_polygon**(polygon:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry2D_method_triangulate_polygon>`{.interpreted-text
role="ref"}

Triangulates the polygon specified by the points in `polygon`. Returns a
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
where each triangle consists of three consecutive point indices into
`polygon` (i.e. the returned array will have `n * 3` elements, with `n`
being the number of found triangles). Output triangles will always be
counter clockwise, and the contour will be flipped if it\'s clockwise.
If the triangulation did not succeed, an empty
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
is returned.
