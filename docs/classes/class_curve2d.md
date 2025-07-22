github_url
:   hide

# Curve2D {#class_Curve2D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Describes a Bézier curve in 2D space.

::: rst-class
classref-introduction-group
:::

## Description

This class describes a Bézier curve in 2D space. It is mainly used to
give a shape to a `Path2D<class_Path2D>`{.interpreted-text role="ref"},
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

:::: {#class_Curve2D_property_bake_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bake_interval** =
`5.0` `🔗<class_Curve2D_property_bake_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_interval**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bake_interval**()

The distance in pixels between two adjacent cached points. Changing it
forces the cache to be recomputed the next time the
`get_baked_points()<class_Curve2D_method_get_baked_points>`{.interpreted-text
role="ref"} or
`get_baked_length()<class_Curve2D_method_get_baked_length>`{.interpreted-text
role="ref"} function is called. The smaller the distance, the more
points in the cache and the more memory it will consume, so use with
care.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_property_point_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **point_count** = `0`
`🔗<class_Curve2D_property_point_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_point_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_point_count**()

The number of points describing the curve.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Curve2D_method_add_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_point**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, in: `Vector2<class_Vector2>`{.interpreted-text role="ref"}
= Vector2(0, 0), out: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0), index: `int<class_int>`{.interpreted-text
role="ref"} = -1) `🔗<class_Curve2D_method_add_point>`{.interpreted-text
role="ref"}

Adds a point with the specified `position` relative to the curve\'s own
position, with control points `in` and `out`. Appends the new point at
the end of the point list.

If `index` is given, the new point is inserted before the existing point
identified by index `index`. Every existing point starting from `index`
is shifted further down the list of points. The index must be greater
than or equal to `0` and must not exceed the number of existing points
in the line. See
`point_count<class_Curve2D_property_point_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_clear_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_points**()
`🔗<class_Curve2D_method_clear_points>`{.interpreted-text role="ref"}

Removes all points from the curve.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_baked_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_baked_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_get_baked_length>`{.interpreted-text
role="ref"}

Returns the total length of the curve, based on the cached points. Given
enough density (see
`bake_interval<class_Curve2D_property_bake_interval>`{.interpreted-text
role="ref"}), it should be approximate enough.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_baked_points}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_baked_points**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_get_baked_points>`{.interpreted-text
role="ref"}

Returns the cache of points as a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_closest_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_closest_offset**(to_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_get_closest_offset>`{.interpreted-text
role="ref"}

Returns the closest offset to `to_point`. This offset is meant to be
used in
`sample_baked()<class_Curve2D_method_sample_baked>`{.interpreted-text
role="ref"}.

`to_point` must be in this curve\'s local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_closest_point}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_closest_point**(to_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_get_closest_point>`{.interpreted-text
role="ref"}

Returns the closest point on baked segments (in curve\'s local space) to
`to_point`.

`to_point` must be in this curve\'s local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_point_in}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_in**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve2D_method_get_point_in>`{.interpreted-text
role="ref"}

Returns the position of the control point leading to the vertex `idx`.
The returned position is relative to the vertex `idx`. If the index is
out of bounds, the function sends an error to the console, and returns
`(0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_point_out}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_out**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve2D_method_get_point_out>`{.interpreted-text
role="ref"}

Returns the position of the control point leading out of the vertex
`idx`. The returned position is relative to the vertex `idx`. If the
index is out of bounds, the function sends an error to the console, and
returns `(0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_get_point_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_position**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the position of the vertex `idx`. If the index is out of bounds,
the function sends an error to the console, and returns `(0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_remove_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Curve2D_method_remove_point>`{.interpreted-text role="ref"}

Deletes the point `idx` from the curve. Sends an error to the console if
`idx` is out of bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_sample}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **sample**(idx:
`int<class_int>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve2D_method_sample>`{.interpreted-text
role="ref"}

Returns the position between the vertex `idx` and the vertex `idx + 1`,
where `t` controls if the point is the first vertex (`t = 0.0`), the
last vertex (`t = 1.0`), or in between. Values of `t` outside the range
(`0.0 <= t <= 1.0`) give strange, but predictable results.

If `idx` is out of bounds it is truncated to the first or last vertex,
and `t` is ignored. If the curve has no points, the function sends an
error to the console, and returns `(0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_sample_baked}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**sample_baked**(offset: `float<class_float>`{.interpreted-text
role="ref"} = 0.0, cubic: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve2D_method_sample_baked>`{.interpreted-text
role="ref"}

Returns a point within the curve at position `offset`, where `offset` is
measured as a pixel distance along the curve.

To do that, it finds the two cached points where the `offset` lies
between, then interpolates the values. This interpolation is cubic if
`cubic` is set to `true`, or linear if set to `false`.

Cubic interpolation tends to follow the curves better, but linear is
faster (and often, precise enough).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_sample_baked_with_rotation}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**sample_baked_with_rotation**(offset:
`float<class_float>`{.interpreted-text role="ref"} = 0.0, cubic:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_sample_baked_with_rotation>`{.interpreted-text
role="ref"}

Similar to
`sample_baked()<class_Curve2D_method_sample_baked>`{.interpreted-text
role="ref"}, but returns
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} that
includes a rotation along the curve, with
`Transform2D.origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"} as the point position and the
`Transform2D.x<class_Transform2D_property_x>`{.interpreted-text
role="ref"} vector pointing in the direction of the path at that point.
Returns an empty transform if the length of the curve is `0`.

    var baked = curve.sample_baked_with_rotation(offset)
    # The returned Transform2D can be set directly.
    transform = baked
    # You can also read the origin and rotation separately from the returned Transform2D.
    position = baked.get_origin()
    rotation = baked.get_rotation()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_samplef}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **samplef**(fofs:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve2D_method_samplef>`{.interpreted-text
role="ref"}

Returns the position at the vertex `fofs`. It calls
`sample()<class_Curve2D_method_sample>`{.interpreted-text role="ref"}
using the integer part of `fofs` as `idx`, and its fractional part as
`t`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_set_point_in}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_in**(idx: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Curve2D_method_set_point_in>`{.interpreted-text role="ref"}

Sets the position of the control point leading to the vertex `idx`. If
the index is out of bounds, the function sends an error to the console.
The position is relative to the vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_set_point_out}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_out**(idx: `int<class_int>`{.interpreted-text role="ref"},
position: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Curve2D_method_set_point_out>`{.interpreted-text role="ref"}

Sets the position of the control point leading out of the vertex `idx`.
If the index is out of bounds, the function sends an error to the
console. The position is relative to the vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_set_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_position**(idx: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_Curve2D_method_set_point_position>`{.interpreted-text
role="ref"}

Sets the position for the vertex `idx`. If the index is out of bounds,
the function sends an error to the console.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve2D_method_tessellate}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **tessellate**(max_stages:
`int<class_int>`{.interpreted-text role="ref"} = 5, tolerance_degrees:
`float<class_float>`{.interpreted-text role="ref"} = 4)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve2D_method_tessellate>`{.interpreted-text
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

:::: {#class_Curve2D_method_tessellate_even_length}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **tessellate_even_length**(max_stages:
`int<class_int>`{.interpreted-text role="ref"} = 5, tolerance_length:
`float<class_float>`{.interpreted-text role="ref"} = 20.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve2D_method_tessellate_even_length>`{.interpreted-text
role="ref"}

Returns a list of points along the curve, with almost uniform density.
`max_stages` controls how many subdivisions a curve segment may face
before it is considered approximate enough. Each subdivision splits the
segment in half, so the default 5 stages may mean up to 32 subdivisions
per curve segment. Increase with care!

`tolerance_length` controls the maximal distance between two neighboring
points, before the segment has to be subdivided.
