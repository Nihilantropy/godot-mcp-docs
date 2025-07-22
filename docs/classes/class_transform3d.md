github_url
:   hide

# Transform3D {#class_Transform3D}

A 3×4 matrix representing a 3D transformation.

::: rst-class
classref-introduction-group
:::

## Description

The **Transform3D** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type is a 3×4 matrix representing a transformation in 3D
space. It contains a `Basis<class_Basis>`{.interpreted-text role="ref"},
which on its own can represent rotation, scale, and shear. Additionally,
combined with its own
`origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}, the transform can also represent a translation.

For a general introduction, see the
`Matrices and transforms <../tutorials/math/matrices_and_transforms>`{.interpreted-text
role="doc"} tutorial.

\*\*Note:\*\* Godot uses a [right-handed coordinate
system](https://en.wikipedia.org/wiki/Right-hand_rule), which is a
common standard. For directions, the convention for built-in types like
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} is for -Z to
point forward (+X is right, +Y is up, and +Z is back). Other objects may
use different direction conventions. For more information, see the [3D
asset direction
conventions](../tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html#d-asset-direction-conventions)
tutorial.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Math documentation index <../tutorials/math/index>`{.interpreted-text
  role="doc"}
- `Matrices and transforms <../tutorials/math/matrices_and_transforms>`{.interpreted-text
  role="doc"}
- `Using 3D transforms <../tutorials/3d/using_transforms>`{.interpreted-text
  role="doc"}
- [Matrix Transform
  Demo](https://godotengine.org/asset-library/asset/2787)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [2.5D Game Demo](https://godotengine.org/asset-library/asset/2783)

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

:::: {#class_Transform3D_constant_IDENTITY}
::: rst-class
classref-constant
:::
::::

**IDENTITY** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_Transform3D_constant_IDENTITY>`{.interpreted-text role="ref"}

The identity **Transform3D**. This is a transform with no translation,
no rotation, and a scale of
`Vector3.ONE<class_Vector3_constant_ONE>`{.interpreted-text role="ref"}.
Its `basis<class_Transform3D_property_basis>`{.interpreted-text
role="ref"} is equal to
`Basis.IDENTITY<class_Basis_constant_IDENTITY>`{.interpreted-text
role="ref"}. This also means that:

- Its `Basis.x<class_Basis_property_x>`{.interpreted-text role="ref"}
  points right
  (`Vector3.RIGHT<class_Vector3_constant_RIGHT>`{.interpreted-text
  role="ref"});
- Its `Basis.y<class_Basis_property_y>`{.interpreted-text role="ref"}
  points up (`Vector3.UP<class_Vector3_constant_UP>`{.interpreted-text
  role="ref"});
- Its `Basis.z<class_Basis_property_z>`{.interpreted-text role="ref"}
  points back
  (`Vector3.BACK<class_Vector3_constant_BACK>`{.interpreted-text
  role="ref"}).

<!-- -->

    var transform = Transform3D.IDENTITY
    var basis = transform.basis
    print("| X | Y | Z | Origin")
    print("| %.f | %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x, transform.origin.x])
    print("| %.f | %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y, transform.origin.y])
    print("| %.f | %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z, transform.origin.z])
    # Prints:
    # | X | Y | Z | Origin
    # | 1 | 0 | 0 | 0
    # | 0 | 1 | 0 | 0
    # | 0 | 0 | 1 | 0

If a `Vector3<class_Vector3>`{.interpreted-text role="ref"}, an
`AABB<class_AABB>`{.interpreted-text role="ref"}, a
`Plane<class_Plane>`{.interpreted-text role="ref"}, a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, or another **Transform3D** is transformed (multiplied) by
this constant, no transformation occurs.

\*\*Note:\*\* In GDScript, this constant is equivalent to creating a
`Transform3D<class_Transform3D_constructor_Transform3D>`{.interpreted-text
role="ref"} without any arguments. It can be used to make your code
clearer, and for consistency with C#.

:::: {#class_Transform3D_constant_FLIP_X}
::: rst-class
classref-constant
:::
::::

**FLIP_X** = `Transform3D(-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_Transform3D_constant_FLIP_X>`{.interpreted-text role="ref"}

**Transform3D** with mirroring applied perpendicular to the YZ plane.
Its `basis<class_Transform3D_property_basis>`{.interpreted-text
role="ref"} is equal to
`Basis.FLIP_X<class_Basis_constant_FLIP_X>`{.interpreted-text
role="ref"}.

:::: {#class_Transform3D_constant_FLIP_Y}
::: rst-class
classref-constant
:::
::::

**FLIP_Y** = `Transform3D(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_Transform3D_constant_FLIP_Y>`{.interpreted-text role="ref"}

**Transform3D** with mirroring applied perpendicular to the XZ plane.
Its `basis<class_Transform3D_property_basis>`{.interpreted-text
role="ref"} is equal to
`Basis.FLIP_Y<class_Basis_constant_FLIP_Y>`{.interpreted-text
role="ref"}.

:::: {#class_Transform3D_constant_FLIP_Z}
::: rst-class
classref-constant
:::
::::

**FLIP_Z** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0)`
`🔗<class_Transform3D_constant_FLIP_Z>`{.interpreted-text role="ref"}

**Transform3D** with mirroring applied perpendicular to the XY plane.
Its `basis<class_Transform3D_property_basis>`{.interpreted-text
role="ref"} is equal to
`Basis.FLIP_Z<class_Basis_constant_FLIP_Z>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Transform3D_property_basis}
::: rst-class
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **basis** =
`Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`
`🔗<class_Transform3D_property_basis>`{.interpreted-text role="ref"}

The `Basis<class_Basis>`{.interpreted-text role="ref"} of this
transform. It is composed by 3 axes
(`Basis.x<class_Basis_property_x>`{.interpreted-text role="ref"},
`Basis.y<class_Basis_property_y>`{.interpreted-text role="ref"}, and
`Basis.z<class_Basis_property_z>`{.interpreted-text role="ref"}).
Together, these represent the transform\'s rotation, scale, and shear.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_property_origin}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **origin** =
`Vector3(0, 0, 0)`
`🔗<class_Transform3D_property_origin>`{.interpreted-text role="ref"}

The translation offset of this transform. In 3D space, this can be seen
as the position.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Transform3D_constructor_Transform3D}
::: rst-class
classref-constructor
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**Transform3D**()
`🔗<class_Transform3D_constructor_Transform3D>`{.interpreted-text
role="ref"}

Constructs a **Transform3D** identical to
`IDENTITY<class_Transform3D_constant_IDENTITY>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In C#, this constructs a **Transform3D** with its
`origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"} and the components of its
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}
set to `Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**Transform3D**(from: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})

Constructs a **Transform3D** as a copy of the given **Transform3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**Transform3D**(basis: `Basis<class_Basis>`{.interpreted-text
role="ref"}, origin: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})

Constructs a **Transform3D** from a
`Basis<class_Basis>`{.interpreted-text role="ref"} and
`Vector3<class_Vector3>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**Transform3D**(from: `Projection<class_Projection>`{.interpreted-text
role="ref"})

Constructs a **Transform3D** from a
`Projection<class_Projection>`{.interpreted-text role="ref"}. Because
**Transform3D** is a 3×4 matrix and
`Projection<class_Projection>`{.interpreted-text role="ref"} is a 4×4
matrix, this operation trims the last row of the projection matrix
(`from.x.w`, `from.y.w`, `from.z.w`, and `from.w.w` are not included in
the new transform).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**Transform3D**(x_axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, y_axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, z_axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, origin: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})

Constructs a **Transform3D** from four
`Vector3<class_Vector3>`{.interpreted-text role="ref"} values (also
called matrix columns).

The first three arguments are the
`basis<class_Transform3D_property_basis>`{.interpreted-text
role="ref"}\'s axes (`Basis.x<class_Basis_property_x>`{.interpreted-text
role="ref"}, `Basis.y<class_Basis_property_y>`{.interpreted-text
role="ref"}, and `Basis.z<class_Basis_property_z>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Transform3D_method_affine_inverse}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**affine_inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_affine_inverse>`{.interpreted-text
role="ref"}

Returns the inverted version of this transform. Unlike
`inverse()<class_Transform3D_method_inverse>`{.interpreted-text
role="ref"}, this method works with almost any
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"},
including non-uniform ones, but is slower. See also
`Basis.inverse()<class_Basis_method_inverse>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For this method to return correctly, the transform\'s
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}
needs to have a determinant that is not exactly `0.0` (see
`Basis.determinant()<class_Basis_method_determinant>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_interpolate_with}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**interpolate_with**(xform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_interpolate_with>`{.interpreted-text
role="ref"}

Returns the result of the linear interpolation between this transform
and `xform` by the given `weight`.

The `weight` should be between `0.0` and `1.0` (inclusive). Values
outside this range are allowed and can be used to perform
*extrapolation* instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_inverse}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform3D_method_inverse>`{.interpreted-text
role="ref"}

Returns the [inverted version of this
transform](https://en.wikipedia.org/wiki/Invertible_matrix). See also
`Basis.inverse()<class_Basis_method_inverse>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For this method to return correctly, the transform\'s
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}
needs to be *orthonormal* (see
`orthonormalized()<class_Transform3D_method_orthonormalized>`{.interpreted-text
role="ref"}). That means the basis should only represent a rotation. If
it does not, use
`affine_inverse()<class_Transform3D_method_affine_inverse>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_equal_approx**(xform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this transform and `xform` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform3D_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this transform is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_looking_at}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**looking_at**(target: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, up: `Vector3<class_Vector3>`{.interpreted-text role="ref"}
= Vector3(0, 1, 0), use_model_front:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform3D_method_looking_at>`{.interpreted-text
role="ref"}

Returns a copy of this transform rotated so that the forward axis (-Z)
points towards the `target` position.

The up axis (+Y) points as close to the `up` vector as possible while
staying perpendicular to the forward axis. The resulting transform is
orthonormalized. The existing rotation, scale, and skew information from
the original transform is discarded. The `target` and `up` vectors
cannot be zero, cannot be parallel to each other, and are defined in
global/parent space.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as
forward (implies +X is left) and points toward the `target` position. By
default, the -Z axis (camera forward) is treated as forward (implies +X
is right).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_orthonormalized}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**orthonormalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_orthonormalized>`{.interpreted-text
role="ref"}

Returns a copy of this transform with its
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}
orthonormalized. An orthonormal basis is both *orthogonal* (the axes are
perpendicular to each other) and *normalized* (the axes have a length of
`1.0`), which also means it can only represent a rotation. See also
`Basis.orthonormalized()<class_Basis_method_orthonormalized>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_rotated}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**rotated**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform3D_method_rotated>`{.interpreted-text
role="ref"}

Returns a copy of this transform rotated around the given `axis` by the
given `angle` (in radians).

The `axis` must be a normalized vector (see
`Vector3.normalized()<class_Vector3_method_normalized>`{.interpreted-text
role="ref"}). If `angle` is positive, the basis is rotated
counter-clockwise around the axis.

This method is an optimized version of multiplying the given transform
`X` with a corresponding rotation transform `R` from the left, i.e.,
`R * X`.

This can be seen as transforming with respect to the global/parent
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_rotated_local}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**rotated_local**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_rotated_local>`{.interpreted-text
role="ref"}

Returns a copy of this transform rotated around the given `axis` by the
given `angle` (in radians).

The `axis` must be a normalized vector in the transform\'s local
coordinate system. For example, to rotate around the local X-axis, use
`Vector3.RIGHT<class_Vector3_constant_RIGHT>`{.interpreted-text
role="ref"}.

This method is an optimized version of multiplying the given transform
`X` with a corresponding rotation transform `R` from the right, i.e.,
`X * R`.

This can be seen as transforming with respect to the local frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_scaled}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**scaled**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform3D_method_scaled>`{.interpreted-text
role="ref"}

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform
`X` with a corresponding scaling transform `S` from the left, i.e.,
`S * X`.

This can be seen as transforming with respect to the global/parent
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_scaled_local}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**scaled_local**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_scaled_local>`{.interpreted-text
role="ref"}

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform
`X` with a corresponding scaling transform `S` from the right, i.e.,
`X * S`.

This can be seen as transforming with respect to the local frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_translated}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**translated**(offset: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform3D_method_translated>`{.interpreted-text
role="ref"}

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform
`X` with a corresponding translation transform `T` from the left, i.e.,
`T * X`.

This can be seen as transforming with respect to the global/parent
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_method_translated_local}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**translated_local**(offset: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform3D_method_translated_local>`{.interpreted-text
role="ref"}

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform
`X` with a corresponding translation transform `T` from the right, i.e.,
`X * T`.

This can be seen as transforming with respect to the local frame.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Transform3D_operator_neq_Transform3D}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_Transform3D_operator_neq_Transform3D>`{.interpreted-text
role="ref"}

Returns `true` if the components of both transforms are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Transform3D_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_AABB}
::: rst-class
classref-operator
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **operator**\*(right:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_Transform3D_operator_mul_AABB>`{.interpreted-text role="ref"}

Transforms (multiplies) the `AABB<class_AABB>`{.interpreted-text
role="ref"} by this transformation matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_PackedVector3Array}
::: rst-class
classref-operator
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **operator**\*(right:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})
`🔗<class_Transform3D_operator_mul_PackedVector3Array>`{.interpreted-text
role="ref"}

Transforms (multiplies) every `Vector3<class_Vector3>`{.interpreted-text
role="ref"} element of the given
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} by this transformation matrix.

On larger arrays, this operation is much faster than transforming each
`Vector3<class_Vector3>`{.interpreted-text role="ref"} individually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_Plane}
::: rst-class
classref-operator
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **operator**\*(right:
`Plane<class_Plane>`{.interpreted-text role="ref"})
`🔗<class_Transform3D_operator_mul_Plane>`{.interpreted-text role="ref"}

Transforms (multiplies) the `Plane<class_Plane>`{.interpreted-text
role="ref"} by this transformation matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_Transform3D}
::: rst-class
classref-operator
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**operator**\*(right: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_Transform3D_operator_mul_Transform3D>`{.interpreted-text
role="ref"}

Transforms (multiplies) this transform by the `right` transform.

This is the operation performed between parent and child
`Node3D<class_Node3D>`{.interpreted-text role="ref"}s.

\*\*Note:\*\* If you need to only modify one attribute of this
transform, consider using one of the following methods, instead:

- For translation, see
  `translated()<class_Transform3D_method_translated>`{.interpreted-text
  role="ref"} or
  `translated_local()<class_Transform3D_method_translated_local>`{.interpreted-text
  role="ref"}.
- For rotation, see
  `rotated()<class_Transform3D_method_rotated>`{.interpreted-text
  role="ref"} or
  `rotated_local()<class_Transform3D_method_rotated_local>`{.interpreted-text
  role="ref"}.
- For scale, see
  `scaled()<class_Transform3D_method_scaled>`{.interpreted-text
  role="ref"} or
  `scaled_local()<class_Transform3D_method_scaled_local>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Transform3D_operator_mul_Vector3>`{.interpreted-text
role="ref"}

Transforms (multiplies) the `Vector3<class_Vector3>`{.interpreted-text
role="ref"} by this transformation matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Transform3D_operator_mul_float>`{.interpreted-text role="ref"}

Multiplies all components of the **Transform3D** by the given
`float<class_float>`{.interpreted-text role="ref"}, including the
`origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly, scaling the
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Transform3D_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies all components of the **Transform3D** by the given
`int<class_int>`{.interpreted-text role="ref"}, including the
`origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly, scaling the
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**operator /**(right: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Transform3D_operator_div_float>`{.interpreted-text role="ref"}

Divides all components of the **Transform3D** by the given
`float<class_float>`{.interpreted-text role="ref"}, including the
`origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly, scaling the
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**operator /**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Transform3D_operator_div_int>`{.interpreted-text role="ref"}

Divides all components of the **Transform3D** by the given
`int<class_int>`{.interpreted-text role="ref"}, including the
`origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly, scaling the
`basis<class_Transform3D_property_basis>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform3D_operator_eq_Transform3D}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_Transform3D_operator_eq_Transform3D>`{.interpreted-text
role="ref"}

Returns `true` if the components of both transforms are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Transform3D_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.
