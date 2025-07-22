github_url
:   hide

# Plane {#class_Plane}

A plane in Hessian normal form.

::: rst-class
classref-introduction-group
:::

## Description

Represents a normalized plane equation.
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"} is
the normal of the plane (a, b, c normalized), and
`d<class_Plane_property_d>`{.interpreted-text role="ref"} is the
distance from the origin to the plane (in the direction of \"normal\").
\"Over\" or \"Above\" the plane is considered the side of the plane
towards where the normal is pointing.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Math documentation index <../tutorials/math/index>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Plane_constant_PLANE_YZ}
::: rst-class
classref-constant
:::
::::

**PLANE_YZ** = `Plane(1, 0, 0, 0)`
`🔗<class_Plane_constant_PLANE_YZ>`{.interpreted-text role="ref"}

A plane that extends in the Y and Z axes (normal vector points +X).

:::: {#class_Plane_constant_PLANE_XZ}
::: rst-class
classref-constant
:::
::::

**PLANE_XZ** = `Plane(0, 1, 0, 0)`
`🔗<class_Plane_constant_PLANE_XZ>`{.interpreted-text role="ref"}

A plane that extends in the X and Z axes (normal vector points +Y).

:::: {#class_Plane_constant_PLANE_XY}
::: rst-class
classref-constant
:::
::::

**PLANE_XY** = `Plane(0, 0, 1, 0)`
`🔗<class_Plane_constant_PLANE_XY>`{.interpreted-text role="ref"}

A plane that extends in the X and Y axes (normal vector points +Z).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Plane_property_d}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **d** = `0.0`
`🔗<class_Plane_property_d>`{.interpreted-text role="ref"}

The distance from the origin to the plane, expressed in terms of
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"}
(according to its direction and magnitude). Actual absolute distance
from the origin to the plane can be calculated as
`abs(d) / normal.length()` (if
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"} has
zero length then this **Plane** does not represent a valid plane).

In the scalar equation of the plane `ax + by + cz = d`, this is `d`,
while the `(a, b, c)` coordinates are represented by the
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"}
property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_property_normal}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **normal** =
`Vector3(0, 0, 0)` `🔗<class_Plane_property_normal>`{.interpreted-text
role="ref"}

The normal of the plane, typically a unit vector. Shouldn\'t be a zero
vector as **Plane** with such
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"} does
not represent a valid plane.

In the scalar equation of the plane `ax + by + cz = d`, this is the
vector `(a, b, c)`, where `d` is the
`d<class_Plane_property_d>`{.interpreted-text role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_property_x}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **x** = `0.0`
`🔗<class_Plane_property_x>`{.interpreted-text role="ref"}

The X component of the plane\'s
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"}
vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_property_y}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **y** = `0.0`
`🔗<class_Plane_property_y>`{.interpreted-text role="ref"}

The Y component of the plane\'s
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"}
vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_property_z}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **z** = `0.0`
`🔗<class_Plane_property_z>`{.interpreted-text role="ref"}

The Z component of the plane\'s
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"}
vector.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Plane_constructor_Plane}
::: rst-class
classref-constructor
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**()
`🔗<class_Plane_constructor_Plane>`{.interpreted-text role="ref"}

Constructs a default-initialized **Plane** with all components set to
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**(from:
`Plane<class_Plane>`{.interpreted-text role="ref"})

Constructs a **Plane** as a copy of the given **Plane**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**(a:
`float<class_float>`{.interpreted-text role="ref"}, b:
`float<class_float>`{.interpreted-text role="ref"}, c:
`float<class_float>`{.interpreted-text role="ref"}, d:
`float<class_float>`{.interpreted-text role="ref"})

Creates a plane from the four parameters. The three components of the
resulting plane\'s
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"} are
`a`, `b` and `c`, and the plane has a distance of `d` from the origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**(normal:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})

Creates a plane from the normal vector. The plane will intersect the
origin.

The `normal` of the plane must be a unit vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**(normal:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, d:
`float<class_float>`{.interpreted-text role="ref"})

Creates a plane from the normal vector and the plane\'s distance from
the origin.

The `normal` of the plane must be a unit vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**(normal:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})

Creates a plane from the normal vector and a point on the plane.

The `normal` of the plane must be a unit vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Plane<class_Plane>`{.interpreted-text role="ref"} **Plane**(point1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, point2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, point3:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})

Creates a plane from the three points, given in clockwise order.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Plane_method_distance_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_to**(point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_distance_to>`{.interpreted-text
role="ref"}

Returns the shortest distance from the plane to the position `point`. If
the point is above the plane, the distance will be positive. If below,
the distance will be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_get_center}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_center**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_get_center>`{.interpreted-text
role="ref"}

Returns the center of the plane.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_has_point}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_point**(point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, tolerance:
`float<class_float>`{.interpreted-text role="ref"} = 1e-05)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_has_point>`{.interpreted-text
role="ref"}

Returns `true` if `point` is inside the plane. Comparison uses a custom
minimum `tolerance` threshold.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_intersect_3}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**intersect_3**(b: `Plane<class_Plane>`{.interpreted-text role="ref"},
c: `Plane<class_Plane>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_intersect_3>`{.interpreted-text
role="ref"}

Returns the intersection point of the three planes `b`, `c` and this
plane. If no intersection is found, `null` is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_intersects_ray}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**intersects_ray**(from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, dir: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_intersects_ray>`{.interpreted-text
role="ref"}

Returns the intersection point of a ray consisting of the position
`from` and the direction normal `dir` with this plane. If no
intersection is found, `null` is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_intersects_segment}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**intersects_segment**(from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, to: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Plane_method_intersects_segment>`{.interpreted-text
role="ref"}

Returns the intersection point of a segment from position `from` to
position `to` with this plane. If no intersection is found, `null` is
returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_equal_approx**(to_plane: `Plane<class_Plane>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this plane and `to_plane` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this plane is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_is_point_over}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_over**(point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_is_point_over>`{.interpreted-text
role="ref"}

Returns `true` if `point` is located above the plane.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_normalized}
::: rst-class
classref-method
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_normalized>`{.interpreted-text
role="ref"}

Returns a copy of the plane, with normalized
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"} (so
it\'s a unit vector). Returns `Plane(0, 0, 0, 0)` if
`normal<class_Plane_property_normal>`{.interpreted-text role="ref"}
can\'t be normalized (it has zero length).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_method_project}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**project**(point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Plane_method_project>`{.interpreted-text
role="ref"}

Returns the orthogonal projection of `point` into a point in the plane.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Plane_operator_neq_Plane}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Plane<class_Plane>`{.interpreted-text role="ref"})
`🔗<class_Plane_operator_neq_Plane>`{.interpreted-text role="ref"}

Returns `true` if the planes are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Plane_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_operator_mul_Transform3D}
::: rst-class
classref-operator
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **operator**\*(right:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_Plane_operator_mul_Transform3D>`{.interpreted-text role="ref"}

Inversely transforms (multiplies) the **Plane** by the given
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
transformation matrix.

`plane * transform` is equivalent to
`transform.affine_inverse() * plane`. See
`Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_operator_eq_Plane}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Plane<class_Plane>`{.interpreted-text role="ref"})
`🔗<class_Plane_operator_eq_Plane>`{.interpreted-text role="ref"}

Returns `true` if the planes are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Plane_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_operator_unplus}
::: rst-class
classref-operator
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **operator unary+**()
`🔗<class_Plane_operator_unplus>`{.interpreted-text role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Plane_operator_unminus}
::: rst-class
classref-operator
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **operator unary-**()
`🔗<class_Plane_operator_unminus>`{.interpreted-text role="ref"}

Returns the negative value of the **Plane**. This is the same as writing
`Plane(-p.normal, -p.d)`. This operation flips the direction of the
normal vector and also flips the distance value, resulting in a Plane
that is in the same place, but facing the opposite direction.
