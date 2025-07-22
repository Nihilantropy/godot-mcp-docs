github_url
:   hide

# Geometry3D {#class_Geometry3D}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides methods for some common 3D geometric operations.

::: rst-class
classref-introduction-group
:::

## Description

Provides a set of helper functions to create geometric shapes, compute
intersections between shapes, and process various other geometric
operations in 3D.

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

:::: {#class_Geometry3D_method_build_box_planes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\]
**build_box_planes**(extents: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Geometry3D_method_build_box_planes>`{.interpreted-text
role="ref"}

Returns an array with 6 `Plane<class_Plane>`{.interpreted-text
role="ref"}s that describe the sides of a box centered at the origin.
The box size is defined by `extents`, which represents one (positive)
corner of the box (i.e. half its actual size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_build_capsule_planes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\]
**build_capsule_planes**(radius: `float<class_float>`{.interpreted-text
role="ref"}, height: `float<class_float>`{.interpreted-text role="ref"},
sides: `int<class_int>`{.interpreted-text role="ref"}, lats:
`int<class_int>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} = 2)
`🔗<class_Geometry3D_method_build_capsule_planes>`{.interpreted-text
role="ref"}

Returns an array of `Plane<class_Plane>`{.interpreted-text role="ref"}s
closely bounding a faceted capsule centered at the origin with radius
`radius` and height `height`. The parameter `sides` defines how many
planes will be generated for the side part of the capsule, whereas
`lats` gives the number of latitudinal steps at the bottom and top of
the capsule. The parameter `axis` describes the axis along which the
capsule is oriented (0 for X, 1 for Y, 2 for Z).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_build_cylinder_planes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\]
**build_cylinder_planes**(radius: `float<class_float>`{.interpreted-text
role="ref"}, height: `float<class_float>`{.interpreted-text role="ref"},
sides: `int<class_int>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} = 2)
`🔗<class_Geometry3D_method_build_cylinder_planes>`{.interpreted-text
role="ref"}

Returns an array of `Plane<class_Plane>`{.interpreted-text role="ref"}s
closely bounding a faceted cylinder centered at the origin with radius
`radius` and height `height`. The parameter `sides` defines how many
planes will be generated for the round part of the cylinder. The
parameter `axis` describes the axis along which the cylinder is oriented
(0 for X, 1 for Y, 2 for Z).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_clip_polygon}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **clip_polygon**(points:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, plane: `Plane<class_Plane>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_clip_polygon>`{.interpreted-text role="ref"}

Clips the polygon defined by the points in `points` against the `plane`
and returns the points of the clipped polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_compute_convex_mesh_points}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **compute_convex_mesh_points**(planes:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\])
`🔗<class_Geometry3D_method_compute_convex_mesh_points>`{.interpreted-text
role="ref"}

Calculates and returns all the vertex points of a convex shape defined
by an array of `planes`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_get_closest_point_to_segment}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_closest_point_to_segment**(point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, s1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, s2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_get_closest_point_to_segment>`{.interpreted-text
role="ref"}

Returns the 3D point on the 3D segment (`s1`, `s2`) that is closest to
`point`. The returned point will always be inside the specified segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_get_closest_point_to_segment_uncapped}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_closest_point_to_segment_uncapped**(point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, s1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, s2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_get_closest_point_to_segment_uncapped>`{.interpreted-text
role="ref"}

Returns the 3D point on the 3D line defined by (`s1`, `s2`) that is
closest to `point`. The returned point can be inside the segment (`s1`,
`s2`) or outside of it, i.e. somewhere on the line extending from the
segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_get_closest_points_between_segments}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_closest_points_between_segments**(p1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, p2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, q1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, q2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_get_closest_points_between_segments>`{.interpreted-text
role="ref"}

Given the two 3D segments (`p1`, `p2`) and (`q1`, `q2`), finds those two
points on the two segments that are closest to each other. Returns a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} that contains this point on (`p1`, `p2`) as well the
accompanying point on (`q1`, `q2`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_get_triangle_barycentric_coords}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_triangle_barycentric_coords**(point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, a:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, b:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, c:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_get_triangle_barycentric_coords>`{.interpreted-text
role="ref"}

Returns a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
containing weights based on how close a 3D position (`point`) is to a
triangle\'s different vertices (`a`, `b` and `c`). This is useful for
interpolating between the data of different vertices in a triangle. One
example use case is using this to smoothly rotate over a mesh instead of
relying solely on face normals.

\`Here is a more detailed explanation of barycentric coordinates.
\<https://en.wikipedia.org/wiki/Barycentric_coordinate_system\>\`\_\_

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_ray_intersects_triangle}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**ray_intersects_triangle**(from:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, dir:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, a:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, b:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, c:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_ray_intersects_triangle>`{.interpreted-text
role="ref"}

Tests if the 3D ray starting at `from` with the direction of `dir`
intersects the triangle specified by `a`, `b` and `c`. If yes, returns
the point of intersection as `Vector3<class_Vector3>`{.interpreted-text
role="ref"}. If no intersection takes place, returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_segment_intersects_convex}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **segment_intersects_convex**(from:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, planes:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\])
`🔗<class_Geometry3D_method_segment_intersects_convex>`{.interpreted-text
role="ref"}

Given a convex hull defined though the
`Plane<class_Plane>`{.interpreted-text role="ref"}s in the array
`planes`, tests if the segment (`from`, `to`) intersects with that hull.
If an intersection is found, returns a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} containing the point the intersection and the hull\'s
normal. Otherwise, returns an empty array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_segment_intersects_cylinder}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **segment_intersects_cylinder**(from:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, height:
`float<class_float>`{.interpreted-text role="ref"}, radius:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_segment_intersects_cylinder>`{.interpreted-text
role="ref"}

Checks if the segment (`from`, `to`) intersects the cylinder with height
`height` that is centered at the origin and has radius `radius`. If no,
returns an empty
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}. If an intersection takes place, the returned array contains
the point of intersection and the cylinder\'s normal at the point of
intersection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_segment_intersects_sphere}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **segment_intersects_sphere**(from:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, sphere_position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, sphere_radius:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_segment_intersects_sphere>`{.interpreted-text
role="ref"}

Checks if the segment (`from`, `to`) intersects the sphere that is
located at `sphere_position` and has radius `sphere_radius`. If no,
returns an empty
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}. If yes, returns a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} containing the point of intersection and the sphere\'s
normal at the point of intersection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_segment_intersects_triangle}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**segment_intersects_triangle**(from:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, a:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, b:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, c:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Geometry3D_method_segment_intersects_triangle>`{.interpreted-text
role="ref"}

Tests if the segment (`from`, `to`) intersects the triangle `a`, `b`,
`c`. If yes, returns the point of intersection as
`Vector3<class_Vector3>`{.interpreted-text role="ref"}. If no
intersection takes place, returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Geometry3D_method_tetrahedralize_delaunay}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**tetrahedralize_delaunay**(points:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})
`🔗<class_Geometry3D_method_tetrahedralize_delaunay>`{.interpreted-text
role="ref"}

Tetrahedralizes the volume specified by a discrete set of `points` in 3D
space, ensuring that no point lies within the circumsphere of any
resulting tetrahedron. The method returns a
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
where each tetrahedron consists of four consecutive point indices into
the `points` array (resulting in an array with `n * 4` elements, where
`n` is the number of tetrahedra found). If the tetrahedralization is
unsuccessful, an empty
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
is returned.
