github_url
:   hide

# Curve3D {#class_Curve3D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Describes a Bézier curve in 3D space.

::: rst-class
classref-introduction-group
:::

## Description

This class describes a Bézier curve in 3D space. It is mainly used to
give a shape to a `Path3D<class_Path3D>`{.interpreted-text role="ref"},
but can be manually sampled for other purposes.

It keeps a cache of precalculated points along the curve, to speed up
further calculations.

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

## Property Descriptions

:::: {#class_Curve3D_property_bake_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bake_interval** =
`0.2` `🔗<class_Curve3D_property_bake_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_interval**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bake_interval**()

The distance in meters between two adjacent cached points. Changing it
forces the cache to be recomputed the next time the
`get_baked_points()<class_Curve3D_method_get_baked_points>`{.interpreted-text
role="ref"} or
`get_baked_length()<class_Curve3D_method_get_baked_length>`{.interpreted-text
role="ref"} function is called. The smaller the distance, the more
points in the cache and the more memory it will consume, so use with
care.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_property_closed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **closed** = `false`
`🔗<class_Curve3D_property_closed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_closed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_closed**()

If `true`, and the curve has more than 2 control points, the last point
and the first one will be connected in a loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_property_point_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **point_count** = `0`
`🔗<class_Curve3D_property_point_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_point_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_point_count**()

The number of points describing the curve.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_property_up_vector_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **up_vector_enabled** =
`true` `🔗<class_Curve3D_property_up_vector_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_up_vector_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_up_vector_enabled**()

If `true`, the curve will bake up vectors used for orientation. This is
used when
`PathFollow3D.rotation_mode<class_PathFollow3D_property_rotation_mode>`{.interpreted-text
role="ref"} is set to
`PathFollow3D.ROTATION_ORIENTED<class_PathFollow3D_constant_ROTATION_ORIENTED>`{.interpreted-text
role="ref"}. Changing it forces the cache to be recomputed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Curve3D_method_add_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_point**(position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, in: `Vector3<class_Vector3>`{.interpreted-text role="ref"}
= Vector3(0, 0, 0), out: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0), index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_Curve3D_method_add_point>`{.interpreted-text role="ref"}

Adds a point with the specified `position` relative to the curve\'s own
position, with control points `in` and `out`. Appends the new point at
the end of the point list.

If `index` is given, the new point is inserted before the existing point
identified by index `index`. Every existing point starting from `index`
is shifted further down the list of points. The index must be greater
than or equal to `0` and must not exceed the number of existing points
in the line. See
`point_count<class_Curve3D_property_point_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_clear_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_points**()
`🔗<class_Curve3D_method_clear_points>`{.interpreted-text role="ref"}

Removes all points from the curve.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_baked_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_baked_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_baked_length>`{.interpreted-text
role="ref"}

Returns the total length of the curve, based on the cached points. Given
enough density (see
`bake_interval<class_Curve3D_property_bake_interval>`{.interpreted-text
role="ref"}), it should be approximate enough.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_baked_points}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_baked_points**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_baked_points>`{.interpreted-text
role="ref"}

Returns the cache of points as a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_baked_tilts}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **get_baked_tilts**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_baked_tilts>`{.interpreted-text role="ref"}

Returns the cache of tilts as a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_baked_up_vectors}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_baked_up_vectors**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_baked_up_vectors>`{.interpreted-text
role="ref"}

Returns the cache of up vectors as a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}.

If
`up_vector_enabled<class_Curve3D_property_up_vector_enabled>`{.interpreted-text
role="ref"} is `false`, the cache will be empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_closest_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_closest_offset**(to_point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_closest_offset>`{.interpreted-text
role="ref"}

Returns the closest offset to `to_point`. This offset is meant to be
used in
`sample_baked()<class_Curve3D_method_sample_baked>`{.interpreted-text
role="ref"} or
`sample_baked_up_vector()<class_Curve3D_method_sample_baked_up_vector>`{.interpreted-text
role="ref"}.

`to_point` must be in this curve\'s local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_closest_point}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_closest_point**(to_point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_closest_point>`{.interpreted-text
role="ref"}

Returns the closest point on baked segments (in curve\'s local space) to
`to_point`.

`to_point` must be in this curve\'s local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_point_in}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_point_in**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_get_point_in>`{.interpreted-text
role="ref"}

Returns the position of the control point leading to the vertex `idx`.
The returned position is relative to the vertex `idx`. If the index is
out of bounds, the function sends an error to the console, and returns
`(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_point_out}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_point_out**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_get_point_out>`{.interpreted-text
role="ref"}

Returns the position of the control point leading out of the vertex
`idx`. The returned position is relative to the vertex `idx`. If the
index is out of bounds, the function sends an error to the console, and
returns `(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_point_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_point_position**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the position of the vertex `idx`. If the index is out of bounds,
the function sends an error to the console, and returns `(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_get_point_tilt}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_tilt**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_get_point_tilt>`{.interpreted-text
role="ref"}

Returns the tilt angle in radians for the point `idx`. If the index is
out of bounds, the function sends an error to the console, and returns
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_remove_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Curve3D_method_remove_point>`{.interpreted-text role="ref"}

Deletes the point `idx` from the curve. Sends an error to the console if
`idx` is out of bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_sample}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **sample**(idx:
`int<class_int>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_sample>`{.interpreted-text
role="ref"}

Returns the position between the vertex `idx` and the vertex `idx + 1`,
where `t` controls if the point is the first vertex (`t = 0.0`), the
last vertex (`t = 1.0`), or in between. Values of `t` outside the range
(`0.0 >= t <=1`) give strange, but predictable results.

If `idx` is out of bounds it is truncated to the first or last vertex,
and `t` is ignored. If the curve has no points, the function sends an
error to the console, and returns `(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_sample_baked}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**sample_baked**(offset: `float<class_float>`{.interpreted-text
role="ref"} = 0.0, cubic: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_sample_baked>`{.interpreted-text
role="ref"}

Returns a point within the curve at position `offset`, where `offset` is
measured as a distance in 3D units along the curve. To do that, it finds
the two cached points where the `offset` lies between, then interpolates
the values. This interpolation is cubic if `cubic` is set to `true`, or
linear if set to `false`.

Cubic interpolation tends to follow the curves better, but linear is
faster (and often, precise enough).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_sample_baked_up_vector}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**sample_baked_up_vector**(offset:
`float<class_float>`{.interpreted-text role="ref"}, apply_tilt:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_sample_baked_up_vector>`{.interpreted-text
role="ref"}

Returns an up vector within the curve at position `offset`, where
`offset` is measured as a distance in 3D units along the curve. To do
that, it finds the two cached up vectors where the `offset` lies
between, then interpolates the values. If `apply_tilt` is `true`, an
interpolated tilt is applied to the interpolated up vector.

If the curve has no up vectors, the function sends an error to the
console, and returns `(0, 1, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_sample_baked_with_rotation}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**sample_baked_with_rotation**(offset:
`float<class_float>`{.interpreted-text role="ref"} = 0.0, cubic:
`bool<class_bool>`{.interpreted-text role="ref"} = false, apply_tilt:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_sample_baked_with_rotation>`{.interpreted-text
role="ref"}

Returns a `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
with `origin` as point position, `basis.x` as sideway vector, `basis.y`
as up vector, `basis.z` as forward vector. When the curve length is 0,
there is no reasonable way to calculate the rotation, all vectors
aligned with global space axes. See also
`sample_baked()<class_Curve3D_method_sample_baked>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_samplef}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **samplef**(fofs:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_samplef>`{.interpreted-text
role="ref"}

Returns the position at the vertex `fofs`. It calls
`sample()<class_Curve3D_method_sample>`{.interpreted-text role="ref"}
using the integer part of `fofs` as `idx`, and its fractional part as
`t`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_set_point_in}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_in**(idx: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Curve3D_method_set_point_in>`{.interpreted-text role="ref"}

Sets the position of the control point leading to the vertex `idx`. If
the index is out of bounds, the function sends an error to the console.
The position is relative to the vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_set_point_out}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_out**(idx: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Curve3D_method_set_point_out>`{.interpreted-text role="ref"}

Sets the position of the control point leading out of the vertex `idx`.
If the index is out of bounds, the function sends an error to the
console. The position is relative to the vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_set_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_position**(idx: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Curve3D_method_set_point_position>`{.interpreted-text
role="ref"}

Sets the position for the vertex `idx`. If the index is out of bounds,
the function sends an error to the console.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_set_point_tilt}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_tilt**(idx: `int<class_int>`{.interpreted-text role="ref"},
tilt: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Curve3D_method_set_point_tilt>`{.interpreted-text role="ref"}

Sets the tilt angle in radians for the point `idx`. If the index is out
of bounds, the function sends an error to the console.

The tilt controls the rotation along the look-at axis an object
traveling the path would have. In the case of a curve controlling a
`PathFollow3D<class_PathFollow3D>`{.interpreted-text role="ref"}, this
tilt is an offset over the natural tilt the
`PathFollow3D<class_PathFollow3D>`{.interpreted-text role="ref"}
calculates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_tessellate}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **tessellate**(max_stages:
`int<class_int>`{.interpreted-text role="ref"} = 5, tolerance_degrees:
`float<class_float>`{.interpreted-text role="ref"} = 4)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve3D_method_tessellate>`{.interpreted-text
role="ref"}

Returns a list of points along the curve, with a curvature controlled
point density. That is, the curvier parts will have more points than the
straighter parts.

This approximation makes straight segments between each point, then
subdivides those segments until the resulting shape is similar enough.

`max_stages` controls how many subdivisions a curve segment may face
before it is considered approximate enough. Each subdivision splits the
segment in half, so the default 5 stages may mean up to 32 subdivisions
per curve segment. Increase with care!

`tolerance_degrees` controls how many degrees the midpoint of a segment
may deviate from the real curve, before the segment has to be
subdivided.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve3D_method_tessellate_even_length}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **tessellate_even_length**(max_stages:
`int<class_int>`{.interpreted-text role="ref"} = 5, tolerance_length:
`float<class_float>`{.interpreted-text role="ref"} = 0.2)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve3D_method_tessellate_even_length>`{.interpreted-text
role="ref"}

Returns a list of points along the curve, with almost uniform density.
`max_stages` controls how many subdivisions a curve segment may face
before it is considered approximate enough. Each subdivision splits the
segment in half, so the default 5 stages may mean up to 32 subdivisions
per curve segment. Increase with care!

`tolerance_length` controls the maximal distance between two neighboring
points, before the segment has to be subdivided.
