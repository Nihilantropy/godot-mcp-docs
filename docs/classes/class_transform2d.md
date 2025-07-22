github_url
:   hide

# Transform2D {#class_Transform2D}

A 2×3 matrix representing a 2D transformation.

::: rst-class
classref-introduction-group
:::

## Description

The **Transform2D** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type is a 2×3
[matrix](https://en.wikipedia.org/wiki/Matrix_(mathematics))
representing a transformation in 2D space. It contains three
`Vector2<class_Vector2>`{.interpreted-text role="ref"} values:
`x<class_Transform2D_property_x>`{.interpreted-text role="ref"},
`y<class_Transform2D_property_y>`{.interpreted-text role="ref"}, and
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}. Together, they can represent translation, rotation, scale,
and skew.

The `x<class_Transform2D_property_x>`{.interpreted-text role="ref"} and
`y<class_Transform2D_property_y>`{.interpreted-text role="ref"} axes
form a 2×2 matrix, known as the transform\'s **basis**. The length of
each axis
(`Vector2.length()<class_Vector2_method_length>`{.interpreted-text
role="ref"}) influences the transform\'s scale, while the direction of
all axes influence the rotation. Usually, both axes are perpendicular to
one another. However, when you rotate one axis individually, the
transform becomes skewed. Applying a skewed transform to a 2D sprite
will make the sprite appear distorted.

For a general introduction, see the
`Matrices and transforms <../tutorials/math/matrices_and_transforms>`{.interpreted-text
role="doc"} tutorial.

\*\*Note:\*\* Unlike `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, there is no 2D equivalent to the
`Basis<class_Basis>`{.interpreted-text role="ref"} type. All mentions of
\"basis\" refer to the
`x<class_Transform2D_property_x>`{.interpreted-text role="ref"} and
`y<class_Transform2D_property_y>`{.interpreted-text role="ref"}
components of **Transform2D**.

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
- [Matrix Transform
  Demo](https://godotengine.org/asset-library/asset/2787)
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

:::: {#class_Transform2D_constant_IDENTITY}
::: rst-class
classref-constant
:::
::::

**IDENTITY** = `Transform2D(1, 0, 0, 1, 0, 0)`
`🔗<class_Transform2D_constant_IDENTITY>`{.interpreted-text role="ref"}

The identity **Transform2D**. This is a transform with no translation,
no rotation, and a scale of
`Vector2.ONE<class_Vector2_constant_ONE>`{.interpreted-text role="ref"}.
This also means that:

- The `x<class_Transform2D_property_x>`{.interpreted-text role="ref"}
  points right
  (`Vector2.RIGHT<class_Vector2_constant_RIGHT>`{.interpreted-text
  role="ref"});
- The `y<class_Transform2D_property_y>`{.interpreted-text role="ref"}
  points down
  (`Vector2.DOWN<class_Vector2_constant_DOWN>`{.interpreted-text
  role="ref"}).

<!-- -->

    var transform = Transform2D.IDENTITY
    print("| X | Y | Origin")
    print("| %.f | %.f | %.f" % [transform.x.x, transform.y.x, transform.origin.x])
    print("| %.f | %.f | %.f" % [transform.x.y, transform.y.y, transform.origin.y])
    # Prints:
    # | X | Y | Origin
    # | 1 | 0 | 0
    # | 0 | 1 | 0

If a `Vector2<class_Vector2>`{.interpreted-text role="ref"}, a
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, or another **Transform2D** is transformed (multiplied) by
this constant, no transformation occurs.

\*\*Note:\*\* In GDScript, this constant is equivalent to creating a
`Transform2D<class_Transform2D_constructor_Transform2D>`{.interpreted-text
role="ref"} without any arguments. It can be used to make your code
clearer, and for consistency with C#.

:::: {#class_Transform2D_constant_FLIP_X}
::: rst-class
classref-constant
:::
::::

**FLIP_X** = `Transform2D(-1, 0, 0, 1, 0, 0)`
`🔗<class_Transform2D_constant_FLIP_X>`{.interpreted-text role="ref"}

When any transform is multiplied by
`FLIP_X<class_Transform2D_constant_FLIP_X>`{.interpreted-text
role="ref"}, it negates all components of the
`x<class_Transform2D_property_x>`{.interpreted-text role="ref"} axis
(the X column).

When `FLIP_X<class_Transform2D_constant_FLIP_X>`{.interpreted-text
role="ref"} is multiplied by any transform, it negates the
`Vector2.x<class_Vector2_property_x>`{.interpreted-text role="ref"}
component of all axes (the X row).

:::: {#class_Transform2D_constant_FLIP_Y}
::: rst-class
classref-constant
:::
::::

**FLIP_Y** = `Transform2D(1, 0, 0, -1, 0, 0)`
`🔗<class_Transform2D_constant_FLIP_Y>`{.interpreted-text role="ref"}

When any transform is multiplied by
`FLIP_Y<class_Transform2D_constant_FLIP_Y>`{.interpreted-text
role="ref"}, it negates all components of the
`y<class_Transform2D_property_y>`{.interpreted-text role="ref"} axis
(the Y column).

When `FLIP_Y<class_Transform2D_constant_FLIP_Y>`{.interpreted-text
role="ref"} is multiplied by any transform, it negates the
`Vector2.y<class_Vector2_property_y>`{.interpreted-text role="ref"}
component of all axes (the Y row).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Transform2D_property_origin}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **origin** =
`Vector2(0, 0)`
`🔗<class_Transform2D_property_origin>`{.interpreted-text role="ref"}

The translation offset of this transform, and the column `2` of the
matrix. In 2D space, this can be seen as the position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_property_x}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **x** =
`Vector2(1, 0)` `🔗<class_Transform2D_property_x>`{.interpreted-text
role="ref"}

The transform basis\'s X axis, and the column `0` of the matrix.
Combined with `y<class_Transform2D_property_y>`{.interpreted-text
role="ref"}, this represents the transform\'s rotation, scale, and skew.

On the identity transform, this vector points right
(`Vector2.RIGHT<class_Vector2_constant_RIGHT>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_property_y}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **y** =
`Vector2(0, 1)` `🔗<class_Transform2D_property_y>`{.interpreted-text
role="ref"}

The transform basis\'s Y axis, and the column `1` of the matrix.
Combined with `x<class_Transform2D_property_x>`{.interpreted-text
role="ref"}, this represents the transform\'s rotation, scale, and skew.

On the identity transform, this vector points down
(`Vector2.DOWN<class_Vector2_constant_DOWN>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Transform2D_constructor_Transform2D}
::: rst-class
classref-constructor
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**Transform2D**()
`🔗<class_Transform2D_constructor_Transform2D>`{.interpreted-text
role="ref"}

Constructs a **Transform2D** identical to
`IDENTITY<class_Transform2D_constant_IDENTITY>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In C#, this constructs a **Transform2D** with all of its
components set to
`Vector2.ZERO<class_Vector2_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**Transform2D**(from: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})

Constructs a **Transform2D** as a copy of the given **Transform2D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**Transform2D**(rotation: `float<class_float>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})

Constructs a **Transform2D** from a given angle (in radians) and
position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**Transform2D**(rotation: `float<class_float>`{.interpreted-text
role="ref"}, scale: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, skew: `float<class_float>`{.interpreted-text role="ref"},
position: `Vector2<class_Vector2>`{.interpreted-text role="ref"})

Constructs a **Transform2D** from a given angle (in radians), scale,
skew (in radians), and position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**Transform2D**(x_axis: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, y_axis: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, origin: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})

Constructs a **Transform2D** from 3
`Vector2<class_Vector2>`{.interpreted-text role="ref"} values
representing `x<class_Transform2D_property_x>`{.interpreted-text
role="ref"}, `y<class_Transform2D_property_y>`{.interpreted-text
role="ref"}, and the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"} (the three matrix columns).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Transform2D_method_affine_inverse}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**affine_inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_affine_inverse>`{.interpreted-text
role="ref"}

Returns the inverted version of this transform. Unlike
`inverse()<class_Transform2D_method_inverse>`{.interpreted-text
role="ref"}, this method works with almost any basis, including
non-uniform ones, but is slower.

\*\*Note:\*\* For this method to return correctly, the transform\'s
basis needs to have a determinant that is not exactly `0.0` (see
`determinant()<class_Transform2D_method_determinant>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_basis_xform}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**basis_xform**(v: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_basis_xform>`{.interpreted-text role="ref"}

Returns a copy of the `v` vector, transformed (multiplied) by the
transform basis\'s matrix. Unlike the multiplication operator (`*`),
this method ignores the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_basis_xform_inv}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**basis_xform_inv**(v: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_basis_xform_inv>`{.interpreted-text
role="ref"}

Returns a copy of the `v` vector, transformed (multiplied) by the
inverse transform basis\'s matrix (see
`inverse()<class_Transform2D_method_inverse>`{.interpreted-text
role="ref"}). This method ignores the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method assumes that this transform\'s basis is
*orthonormal* (see
`orthonormalized()<class_Transform2D_method_orthonormalized>`{.interpreted-text
role="ref"}). If the basis is not orthonormal,
`transform.affine_inverse().basis_xform(vector)` should be used instead
(see
`affine_inverse()<class_Transform2D_method_affine_inverse>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_determinant}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **determinant**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_determinant>`{.interpreted-text role="ref"}

Returns the [determinant](https://en.wikipedia.org/wiki/Determinant) of
this transform basis\'s matrix. For advanced math, this number can be
used to determine a few attributes:

- If the determinant is exactly `0.0`, the basis is not invertible (see
  `inverse()<class_Transform2D_method_inverse>`{.interpreted-text
  role="ref"}).
- If the determinant is a negative number, the basis represents a
  negative scale.

\*\*Note:\*\* If the basis\'s scale is the same for every axis, its
determinant is always that scale by the power of 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_get_origin}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_origin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_get_origin>`{.interpreted-text
role="ref"}

Returns this transform\'s translation. Equivalent to
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_get_rotation}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_rotation**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_get_rotation>`{.interpreted-text
role="ref"}

Returns this transform\'s rotation (in radians). This is equivalent to
`x<class_Transform2D_property_x>`{.interpreted-text role="ref"}\'s angle
(see `Vector2.angle()<class_Vector2_method_angle>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_get_scale}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_get_scale>`{.interpreted-text
role="ref"}

Returns the length of both
`x<class_Transform2D_property_x>`{.interpreted-text role="ref"} and
`y<class_Transform2D_property_y>`{.interpreted-text role="ref"}, as a
`Vector2<class_Vector2>`{.interpreted-text role="ref"}. If this
transform\'s basis is not skewed, this value is the scaling factor. It
is not affected by rotation.

::::: tabs
::: code-tab
gdscript

var my_transform = Transform2D(

:   Vector2(2, 0), Vector2(0, 4), Vector2(0, 0)

) \# Rotating the Transform2D in any way preserves its scale.
my_transform = my_transform.rotated(TAU / 2)

print(my_transform.get_scale()) \# Prints (2.0, 4.0)
:::

::: code-tab
csharp

var myTransform = new Transform2D(

:   Vector3(2.0f, 0.0f), Vector3(0.0f, 4.0f), Vector3(0.0f, 0.0f)

); // Rotating the Transform2D in any way preserves its scale.
myTransform = myTransform.Rotated(Mathf.Tau / 2.0f);

GD.Print(myTransform.GetScale()); // Prints (2, 4)
:::
:::::

\*\*Note:\*\* If the value returned by
`determinant()<class_Transform2D_method_determinant>`{.interpreted-text
role="ref"} is negative, the scale is also negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_get_skew}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_skew**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_get_skew>`{.interpreted-text
role="ref"}

Returns this transform\'s skew (in radians).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_interpolate_with}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**interpolate_with**(xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_interpolate_with>`{.interpreted-text
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

:::: {#class_Transform2D_method_inverse}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_inverse>`{.interpreted-text
role="ref"}

Returns the [inverted version of this
transform](https://en.wikipedia.org/wiki/Invertible_matrix).

\*\*Note:\*\* For this method to return correctly, the transform\'s
basis needs to be *orthonormal* (see
`orthonormalized()<class_Transform2D_method_orthonormalized>`{.interpreted-text
role="ref"}). That means the basis should only represent a rotation. If
it does not, use
`affine_inverse()<class_Transform2D_method_affine_inverse>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_is_conformal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_conformal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_is_conformal>`{.interpreted-text
role="ref"}

Returns `true` if this transform\'s basis is conformal. A conformal
basis is both *orthogonal* (the axes are perpendicular to each other)
and *uniform* (the axes share the same length). This method can be
especially useful during physics calculations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_equal_approx**(xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this transform and `xform` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this transform is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_looking_at}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**looking_at**(target: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_looking_at>`{.interpreted-text
role="ref"}

Returns a copy of the transform rotated such that the rotated X-axis
points towards the `target` position, in global space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_orthonormalized}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**orthonormalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_orthonormalized>`{.interpreted-text
role="ref"}

Returns a copy of this transform with its basis orthonormalized. An
orthonormal basis is both *orthogonal* (the axes are perpendicular to
each other) and *normalized* (the axes have a length of `1.0`), which
also means it can only represent a rotation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_rotated}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**rotated**(angle: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_rotated>`{.interpreted-text
role="ref"}

Returns a copy of this transform rotated by the given `angle` (in
radians).

If `angle` is positive, the transform is rotated clockwise.

This method is an optimized version of multiplying the given transform
`X` with a corresponding rotation transform `R` from the left, i.e.,
`R * X`.

This can be seen as transforming with respect to the global/parent
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_rotated_local}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**rotated_local**(angle: `float<class_float>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_rotated_local>`{.interpreted-text
role="ref"}

Returns a copy of the transform rotated by the given `angle` (in
radians).

This method is an optimized version of multiplying the given transform
`X` with a corresponding rotation transform `R` from the right, i.e.,
`X * R`.

This can be seen as transforming with respect to the local frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_scaled}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**scaled**(scale: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_scaled>`{.interpreted-text
role="ref"}

Returns a copy of the transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform
`X` with a corresponding scaling transform `S` from the left, i.e.,
`S * X`.

This can be seen as transforming with respect to the global/parent
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_scaled_local}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**scaled_local**(scale: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_scaled_local>`{.interpreted-text
role="ref"}

Returns a copy of the transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform
`X` with a corresponding scaling transform `S` from the right, i.e.,
`X * S`.

This can be seen as transforming with respect to the local frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_translated}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**translated**(offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Transform2D_method_translated>`{.interpreted-text
role="ref"}

Returns a copy of the transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform
`X` with a corresponding translation transform `T` from the left, i.e.,
`T * X`.

This can be seen as transforming with respect to the global/parent
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_method_translated_local}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**translated_local**(offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Transform2D_method_translated_local>`{.interpreted-text
role="ref"}

Returns a copy of the transform translated by the given `offset`.

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

:::: {#class_Transform2D_operator_neq_Transform2D}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_Transform2D_operator_neq_Transform2D>`{.interpreted-text
role="ref"}

Returns `true` if the components of both transforms are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Transform2D_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_mul_PackedVector2Array}
::: rst-class
classref-operator
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **operator**\*(right:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_Transform2D_operator_mul_PackedVector2Array>`{.interpreted-text
role="ref"}

Transforms (multiplies) every `Vector2<class_Vector2>`{.interpreted-text
role="ref"} element of the given
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} by this transformation matrix.

On larger arrays, this operation is much faster than transforming each
`Vector2<class_Vector2>`{.interpreted-text role="ref"} individually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_mul_Rect2}
::: rst-class
classref-operator
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **operator**\*(right:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_Transform2D_operator_mul_Rect2>`{.interpreted-text role="ref"}

Transforms (multiplies) the `Rect2<class_Rect2>`{.interpreted-text
role="ref"} by this transformation matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_mul_Transform2D}
::: rst-class
classref-operator
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**operator**\*(right: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`🔗<class_Transform2D_operator_mul_Transform2D>`{.interpreted-text
role="ref"}

Transforms (multiplies) this transform by the `right` transform.

This is the operation performed between parent and child
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} nodes.

\*\*Note:\*\* If you need to only modify one attribute of this
transform, consider using one of the following methods, instead:

- For translation, see
  `translated()<class_Transform2D_method_translated>`{.interpreted-text
  role="ref"} or
  `translated_local()<class_Transform2D_method_translated_local>`{.interpreted-text
  role="ref"}.
- For rotation, see
  `rotated()<class_Transform2D_method_rotated>`{.interpreted-text
  role="ref"} or
  `rotated_local()<class_Transform2D_method_rotated_local>`{.interpreted-text
  role="ref"}.
- For scale, see
  `scaled()<class_Transform2D_method_scaled>`{.interpreted-text
  role="ref"} or
  `scaled_local()<class_Transform2D_method_scaled_local>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_mul_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_Transform2D_operator_mul_Vector2>`{.interpreted-text
role="ref"}

Transforms (multiplies) the `Vector2<class_Vector2>`{.interpreted-text
role="ref"} by this transformation matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Transform2D_operator_mul_float>`{.interpreted-text role="ref"}

Multiplies all components of the **Transform2D** by the given
`float<class_float>`{.interpreted-text role="ref"}, including the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Transform2D_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies all components of the **Transform2D** by the given
`int<class_int>`{.interpreted-text role="ref"}, including the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**operator /**(right: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Transform2D_operator_div_float>`{.interpreted-text role="ref"}

Divides all components of the **Transform2D** by the given
`float<class_float>`{.interpreted-text role="ref"}, including the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**operator /**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Transform2D_operator_div_int>`{.interpreted-text role="ref"}

Divides all components of the **Transform2D** by the given
`int<class_int>`{.interpreted-text role="ref"}, including the
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}. This affects the transform\'s scale uniformly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_eq_Transform2D}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_Transform2D_operator_eq_Transform2D>`{.interpreted-text
role="ref"}

Returns `true` if the components of both transforms are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Transform2D_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Transform2D_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Transform2D_operator_idx_int>`{.interpreted-text role="ref"}

Accesses each axis (column) of this transform by their index. Index `0`
is the same as `x<class_Transform2D_property_x>`{.interpreted-text
role="ref"}, index `1` is the same as
`y<class_Transform2D_property_y>`{.interpreted-text role="ref"}, and
index `2` is the same as
`origin<class_Transform2D_property_origin>`{.interpreted-text
role="ref"}.
