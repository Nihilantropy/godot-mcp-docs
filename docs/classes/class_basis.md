github_url
:   hide

# Basis {#class_Basis}

A 3×3 matrix for representing 3D rotation and scale.

::: rst-class
classref-introduction-group
:::

## Description

The **Basis** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type is a 3×3
[matrix](https://en.wikipedia.org/wiki/Matrix_(mathematics)) used to
represent 3D rotation, scale, and shear. It is frequently used within a
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

A **Basis** is composed by 3 axis vectors, each representing a column of
the matrix: `x<class_Basis_property_x>`{.interpreted-text role="ref"},
`y<class_Basis_property_y>`{.interpreted-text role="ref"}, and
`z<class_Basis_property_z>`{.interpreted-text role="ref"}. The length of
each axis
(`Vector3.length()<class_Vector3_method_length>`{.interpreted-text
role="ref"}) influences the basis\'s scale, while the direction of all
axes influence the rotation. Usually, these axes are perpendicular to
one another. However, when you rotate any axis individually, the basis
becomes sheared. Applying a sheared basis to a 3D model will make the
model appear distorted.

A **Basis** is:

- **Orthogonal** if its axes are perpendicular to each other.
- **Normalized** if the length of every axis is `1.0`.
- **Uniform** if all axes share the same length (see
  `get_scale()<class_Basis_method_get_scale>`{.interpreted-text
  role="ref"}).
- **Orthonormal** if it is both orthogonal and normalized, which allows
  it to only represent rotations (see
  `orthonormalized()<class_Basis_method_orthonormalized>`{.interpreted-text
  role="ref"}).
- **Conformal** if it is both orthogonal and uniform, which ensures it
  is not distorted.

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

\*\*Note:\*\* The basis matrices are exposed as
[column-major](https://www.mindcontrol.org/~hplus/graphics/matrix-layout.html)
order, which is the same as OpenGL. However, they are stored internally
in row-major order, which is the same as DirectX.

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
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)
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

:::: {#class_Basis_constant_IDENTITY}
::: rst-class
classref-constant
:::
::::

**IDENTITY** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`
`🔗<class_Basis_constant_IDENTITY>`{.interpreted-text role="ref"}

The identity **Basis**. This is an orthonormal basis with no rotation,
no shear, and a scale of
`Vector3.ONE<class_Vector3_constant_ONE>`{.interpreted-text role="ref"}.
This also means that:

- The `x<class_Basis_property_x>`{.interpreted-text role="ref"} points
  right (`Vector3.RIGHT<class_Vector3_constant_RIGHT>`{.interpreted-text
  role="ref"});
- The `y<class_Basis_property_y>`{.interpreted-text role="ref"} points
  up (`Vector3.UP<class_Vector3_constant_UP>`{.interpreted-text
  role="ref"});
- The `z<class_Basis_property_z>`{.interpreted-text role="ref"} points
  back (`Vector3.BACK<class_Vector3_constant_BACK>`{.interpreted-text
  role="ref"}).

<!-- -->

    var basis = Basis.IDENTITY
    print("| X | Y | Z")
    print("| %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x])
    print("| %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y])
    print("| %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z])
    # Prints:
    # | X | Y | Z
    # | 1 | 0 | 0
    # | 0 | 1 | 0
    # | 0 | 0 | 1

If a `Vector3<class_Vector3>`{.interpreted-text role="ref"} or another
**Basis** is transformed (multiplied) by this constant, no
transformation occurs.

\*\*Note:\*\* In GDScript, this constant is equivalent to creating a
`Basis<class_Basis_constructor_Basis>`{.interpreted-text role="ref"}
without any arguments. It can be used to make your code clearer, and for
consistency with C#.

:::: {#class_Basis_constant_FLIP_X}
::: rst-class
classref-constant
:::
::::

**FLIP_X** = `Basis(-1, 0, 0, 0, 1, 0, 0, 0, 1)`
`🔗<class_Basis_constant_FLIP_X>`{.interpreted-text role="ref"}

When any basis is multiplied by
`FLIP_X<class_Basis_constant_FLIP_X>`{.interpreted-text role="ref"}, it
negates all components of the
`x<class_Basis_property_x>`{.interpreted-text role="ref"} axis (the X
column).

When `FLIP_X<class_Basis_constant_FLIP_X>`{.interpreted-text role="ref"}
is multiplied by any basis, it negates the
`Vector3.x<class_Vector3_property_x>`{.interpreted-text role="ref"}
component of all axes (the X row).

:::: {#class_Basis_constant_FLIP_Y}
::: rst-class
classref-constant
:::
::::

**FLIP_Y** = `Basis(1, 0, 0, 0, -1, 0, 0, 0, 1)`
`🔗<class_Basis_constant_FLIP_Y>`{.interpreted-text role="ref"}

When any basis is multiplied by
`FLIP_Y<class_Basis_constant_FLIP_Y>`{.interpreted-text role="ref"}, it
negates all components of the
`y<class_Basis_property_y>`{.interpreted-text role="ref"} axis (the Y
column).

When `FLIP_Y<class_Basis_constant_FLIP_Y>`{.interpreted-text role="ref"}
is multiplied by any basis, it negates the
`Vector3.y<class_Vector3_property_y>`{.interpreted-text role="ref"}
component of all axes (the Y row).

:::: {#class_Basis_constant_FLIP_Z}
::: rst-class
classref-constant
:::
::::

**FLIP_Z** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, -1)`
`🔗<class_Basis_constant_FLIP_Z>`{.interpreted-text role="ref"}

When any basis is multiplied by
`FLIP_Z<class_Basis_constant_FLIP_Z>`{.interpreted-text role="ref"}, it
negates all components of the
`z<class_Basis_property_z>`{.interpreted-text role="ref"} axis (the Z
column).

When `FLIP_Z<class_Basis_constant_FLIP_Z>`{.interpreted-text role="ref"}
is multiplied by any basis, it negates the
`Vector3.z<class_Vector3_property_z>`{.interpreted-text role="ref"}
component of all axes (the Z row).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Basis_property_x}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **x** =
`Vector3(1, 0, 0)` `🔗<class_Basis_property_x>`{.interpreted-text
role="ref"}

The basis\'s X axis, and the column `0` of the matrix.

On the identity basis, this vector points right
(`Vector3.RIGHT<class_Vector3_constant_RIGHT>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_property_y}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **y** =
`Vector3(0, 1, 0)` `🔗<class_Basis_property_y>`{.interpreted-text
role="ref"}

The basis\'s Y axis, and the column `1` of the matrix.

On the identity basis, this vector points up
(`Vector3.UP<class_Vector3_constant_UP>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_property_z}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **z** =
`Vector3(0, 0, 1)` `🔗<class_Basis_property_z>`{.interpreted-text
role="ref"}

The basis\'s Z axis, and the column `2` of the matrix.

On the identity basis, this vector points back
(`Vector3.BACK<class_Vector3_constant_BACK>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Basis_constructor_Basis}
::: rst-class
classref-constructor
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **Basis**()
`🔗<class_Basis_constructor_Basis>`{.interpreted-text role="ref"}

Constructs a **Basis** identical to
`IDENTITY<class_Basis_constant_IDENTITY>`{.interpreted-text role="ref"}.

\*\*Note:\*\* In C#, this constructs a **Basis** with all of its
components set to
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Basis<class_Basis>`{.interpreted-text role="ref"} **Basis**(from:
`Basis<class_Basis>`{.interpreted-text role="ref"})

Constructs a **Basis** as a copy of the given **Basis**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Basis<class_Basis>`{.interpreted-text role="ref"} **Basis**(axis:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, angle:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **Basis** that only represents rotation, rotated around the
`axis` by the given `angle`, in radians. The axis must be a normalized
vector.

\*\*Note:\*\* This is the same as using
`rotated()<class_Basis_method_rotated>`{.interpreted-text role="ref"} on
the `IDENTITY<class_Basis_constant_IDENTITY>`{.interpreted-text
role="ref"} basis. With more than one angle consider using
`from_euler()<class_Basis_method_from_euler>`{.interpreted-text
role="ref"}, instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Basis<class_Basis>`{.interpreted-text role="ref"} **Basis**(from:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})

Constructs a **Basis** that only represents rotation from the given
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Quaternions *only* store rotation, not scale. Because of
this, conversions from **Basis** to
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} cannot
always be reversed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Basis<class_Basis>`{.interpreted-text role="ref"} **Basis**(x_axis:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, y_axis:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, z_axis:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})

Constructs a **Basis** from 3 axis vectors. These are the columns of the
basis matrix.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Basis_method_determinant}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **determinant**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_determinant>`{.interpreted-text
role="ref"}

Returns the [determinant](https://en.wikipedia.org/wiki/Determinant) of
this basis\'s matrix. For advanced math, this number can be used to
determine a few attributes:

- If the determinant is exactly `0.0`, the basis is not invertible (see
  `inverse()<class_Basis_method_inverse>`{.interpreted-text
  role="ref"}).
- If the determinant is a negative number, the basis represents a
  negative scale.

\*\*Note:\*\* If the basis\'s scale is the same for every axis, its
determinant is always that scale by the power of 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_from_euler}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **from_euler**(euler:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, order:
`int<class_int>`{.interpreted-text role="ref"} = 2)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_from_euler>`{.interpreted-text
role="ref"}

Constructs a new **Basis** that only represents rotation from the given
`Vector3<class_Vector3>`{.interpreted-text role="ref"} of [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles), in radians.

- The `Vector3.x<class_Vector3_property_x>`{.interpreted-text
  role="ref"} should contain the angle around the
  `x<class_Basis_property_x>`{.interpreted-text role="ref"} axis
  (pitch);
- The `Vector3.y<class_Vector3_property_y>`{.interpreted-text
  role="ref"} should contain the angle around the
  `y<class_Basis_property_y>`{.interpreted-text role="ref"} axis (yaw);
- The `Vector3.z<class_Vector3_property_z>`{.interpreted-text
  role="ref"} should contain the angle around the
  `z<class_Basis_property_z>`{.interpreted-text role="ref"} axis (roll).

::::: tabs
::: code-tab
gdscript

\# Creates a Basis whose z axis points down. var my_basis =
Basis.from_euler(Vector3(TAU / 4, 0, 0))

print(my_basis.z) \# Prints (0.0, -1.0, 0.0)
:::

::: code-tab
csharp

// Creates a Basis whose z axis points down. var myBasis =
Basis.FromEuler(new Vector3(Mathf.Tau / 4.0f, 0.0f, 0.0f));

GD.Print(myBasis.Z); // Prints (0, -1, 0)
:::
:::::

The order of each consecutive rotation can be changed with `order` (see
`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
constants). By default, the YXZ convention is used
(`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`{.interpreted-text
role="ref"}): the basis rotates first around the Y axis (yaw), then X
(pitch), and lastly Z (roll). When using the opposite method
`get_euler()<class_Basis_method_get_euler>`{.interpreted-text
role="ref"}, this order is reversed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_from_scale}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **from_scale**(scale:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_from_scale>`{.interpreted-text
role="ref"}

Constructs a new **Basis** that only represents scale, with no rotation
or shear, from the given `scale` vector.

::::: tabs
::: code-tab
gdscript

var my_basis = Basis.from_scale(Vector3(2, 4, 8))

print(my_basis.x) \# Prints (2.0, 0.0, 0.0) print(my_basis.y) \# Prints
(0.0, 4.0, 0.0) print(my_basis.z) \# Prints (0.0, 0.0, 8.0)
:::

::: code-tab
csharp

var myBasis = Basis.FromScale(new Vector3(2.0f, 4.0f, 8.0f));

GD.Print(myBasis.X); // Prints (2, 0, 0) GD.Print(myBasis.Y); // Prints
(0, 4, 0) GD.Print(myBasis.Z); // Prints (0, 0, 8)
:::
:::::

\*\*Note:\*\* In linear algebra, the matrix of this basis is also known
as a [diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_get_euler}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_euler**(order: `int<class_int>`{.interpreted-text role="ref"} = 2)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_get_euler>`{.interpreted-text
role="ref"}

Returns this basis\'s rotation as a
`Vector3<class_Vector3>`{.interpreted-text role="ref"} of [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles), in radians. For the
returned value:

- The `Vector3.x<class_Vector3_property_x>`{.interpreted-text
  role="ref"} contains the angle around the
  `x<class_Basis_property_x>`{.interpreted-text role="ref"} axis
  (pitch);
- The `Vector3.y<class_Vector3_property_y>`{.interpreted-text
  role="ref"} contains the angle around the
  `y<class_Basis_property_y>`{.interpreted-text role="ref"} axis (yaw);
- The `Vector3.z<class_Vector3_property_z>`{.interpreted-text
  role="ref"} contains the angle around the
  `z<class_Basis_property_z>`{.interpreted-text role="ref"} axis (roll).

The order of each consecutive rotation can be changed with `order` (see
`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
constants). By default, the YXZ convention is used
(`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`{.interpreted-text
role="ref"}): Z (roll) is calculated first, then X (pitch), and lastly Y
(yaw). When using the opposite method
`from_euler()<class_Basis_method_from_euler>`{.interpreted-text
role="ref"}, this order is reversed.

\*\*Note:\*\* For this method to return correctly, the basis needs to be
*orthonormal* (see
`orthonormalized()<class_Basis_method_orthonormalized>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Euler angles are much more intuitive but are not suitable
for 3D math. Because of this, consider using the
`get_rotation_quaternion()<class_Basis_method_get_rotation_quaternion>`{.interpreted-text
role="ref"} method instead, which returns a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}.

\*\*Note:\*\* In the Inspector dock, a basis\'s rotation is often
displayed in Euler angles (in degrees), as is the case with the
`Node3D.rotation<class_Node3D_property_rotation>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_get_rotation_quaternion}
::: rst-class
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**get_rotation_quaternion**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Basis_method_get_rotation_quaternion>`{.interpreted-text
role="ref"}

Returns this basis\'s rotation as a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Quaternions are much more suitable for 3D math but are
less intuitive. For user interfaces, consider using the
`get_euler()<class_Basis_method_get_euler>`{.interpreted-text
role="ref"} method, which returns Euler angles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_get_scale}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_get_scale>`{.interpreted-text
role="ref"}

Returns the length of each axis of this basis, as a
`Vector3<class_Vector3>`{.interpreted-text role="ref"}. If the basis is
not sheared, this value is the scaling factor. It is not affected by
rotation.

::::: tabs
::: code-tab
gdscript

var my_basis = Basis(

:   Vector3(2, 0, 0), Vector3(0, 4, 0), Vector3(0, 0, 8)

) \# Rotating the Basis in any way preserves its scale. my_basis =
my_basis.rotated(Vector3.UP, TAU / 2) my_basis =
my_basis.rotated(Vector3.RIGHT, TAU / 4)

print(my_basis.get_scale()) \# Prints (2.0, 4.0, 8.0)
:::

::: code-tab
csharp

var myBasis = new Basis(

:   Vector3(2.0f, 0.0f, 0.0f), Vector3(0.0f, 4.0f, 0.0f), Vector3(0.0f,
    0.0f, 8.0f)

); // Rotating the Basis in any way preserves its scale. myBasis =
myBasis.Rotated(Vector3.Up, Mathf.Tau / 2.0f); myBasis =
myBasis.Rotated(Vector3.Right, Mathf.Tau / 4.0f);

GD.Print(myBasis.Scale); // Prints (2, 4, 8)
:::
:::::

\*\*Note:\*\* If the value returned by
`determinant()<class_Basis_method_determinant>`{.interpreted-text
role="ref"} is negative, the scale is also negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_inverse}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_inverse>`{.interpreted-text
role="ref"}

Returns the [inverse of this basis\'s
matrix](https://en.wikipedia.org/wiki/Invertible_matrix).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_is_conformal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_conformal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_is_conformal>`{.interpreted-text
role="ref"}

Returns `true` if this basis is conformal. A conformal basis is both
*orthogonal* (the axes are perpendicular to each other) and *uniform*
(the axes share the same length). This method can be especially useful
during physics calculations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(b:
`Basis<class_Basis>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this basis and `b` are approximately equal, by calling
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on all vector components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this basis is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on all vector components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_looking_at}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**looking_at**(target: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, up: `Vector3<class_Vector3>`{.interpreted-text role="ref"}
= Vector3(0, 1, 0), use_model_front:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_looking_at>`{.interpreted-text
role="ref"}

Creates a new **Basis** with a rotation such that the forward axis (-Z)
points towards the `target` position.

By default, the -Z axis (camera forward) is treated as forward (implies
+X is right). If `use_model_front` is `true`, the +Z axis (asset front)
is treated as forward (implies +X is left) and points toward the
`target` position.

The up axis (+Y) points as close to the `up` vector as possible while
staying perpendicular to the forward axis. The returned basis is
orthonormalized (see
`orthonormalized()<class_Basis_method_orthonormalized>`{.interpreted-text
role="ref"}).

The `target` and the `up` cannot be
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}, and shouldn\'t be colinear to avoid unintended rotation
around local Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_orthonormalized}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **orthonormalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_orthonormalized>`{.interpreted-text
role="ref"}

Returns the orthonormalized version of this basis. An orthonormal basis
is both *orthogonal* (the axes are perpendicular to each other) and
*normalized* (the axes have a length of `1.0`), which also means it can
only represent a rotation.

It is often useful to call this method to avoid rounding errors on a
rotating basis:

::::: tabs
::: code-tab
gdscript

\# Rotate this Node3D every frame. func [process]{#process}(delta):
basis = basis.rotated(Vector3.UP, TAU \* delta) basis =
basis.rotated(Vector3.RIGHT, TAU \* delta) basis =
basis.orthonormalized()
:::

::: code-tab
csharp

// Rotate this Node3D every frame. public override void
[Process]{#process}(double delta) { Basis = Basis.Rotated(Vector3.Up,
Mathf.Tau \* (float)delta) .Rotated(Vector3.Right, Mathf.Tau \*
(float)delta) .Orthonormalized(); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_rotated}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **rotated**(axis:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, angle:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_rotated>`{.interpreted-text
role="ref"}

Returns a copy of this basis rotated around the given `axis` by the
given `angle` (in radians).

The `axis` must be a normalized vector (see
`Vector3.normalized()<class_Vector3_method_normalized>`{.interpreted-text
role="ref"}). If `angle` is positive, the basis is rotated
counter-clockwise around the axis.

::::: tabs
::: code-tab
gdscript

var my_basis = Basis.IDENTITY var angle = TAU / 2

my_basis = my_basis.rotated(Vector3.UP, angle) \# Rotate around the up
axis (yaw). my_basis = my_basis.rotated(Vector3.RIGHT, angle) \# Rotate
around the right axis (pitch). my_basis = my_basis.rotated(Vector3.BACK,
angle) \# Rotate around the back axis (roll).
:::

::: code-tab
csharp

var myBasis = Basis.Identity; var angle = Mathf.Tau / 2.0f;

myBasis = myBasis.Rotated(Vector3.Up, angle); // Rotate around the up
axis (yaw). myBasis = myBasis.Rotated(Vector3.Right, angle); // Rotate
around the right axis (pitch). myBasis = myBasis.Rotated(Vector3.Back,
angle); // Rotate around the back axis (roll).
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_scaled}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **scaled**(scale:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_scaled>`{.interpreted-text
role="ref"}

Returns this basis with each axis\'s components scaled by the given
`scale`\'s components.

The basis matrix\'s rows are multiplied by `scale`\'s components. This
operation is a global scale (relative to the parent).

::::: tabs
::: code-tab
gdscript

var my_basis = Basis(

:   Vector3(1, 1, 1), Vector3(2, 2, 2), Vector3(3, 3, 3)

) my_basis = my_basis.scaled(Vector3(0, 2, -2))

print(my_basis.x) \# Prints (0.0, 2.0, -2.0) print(my_basis.y) \# Prints
(0.0, 4.0, -4.0) print(my_basis.z) \# Prints (0.0, 6.0, -6.0)
:::

::: code-tab
csharp

var myBasis = new Basis(

:   new Vector3(1.0f, 1.0f, 1.0f), new Vector3(2.0f, 2.0f, 2.0f), new
    Vector3(3.0f, 3.0f, 3.0f)

); myBasis = myBasis.Scaled(new Vector3(0.0f, 2.0f, -2.0f));

GD.Print(myBasis.X); // Prints (0, 2, -2) GD.Print(myBasis.Y); // Prints
(0, 4, -4) GD.Print(myBasis.Z); // Prints (0, 6, -6)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_scaled_local}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**scaled_local**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_scaled_local>`{.interpreted-text
role="ref"}

Returns this basis with each axis scaled by the corresponding component
in the given `scale`.

The basis matrix\'s columns are multiplied by `scale`\'s components.
This operation is a local scale (relative to self).

::::: tabs
::: code-tab
gdscript

var my_basis = Basis(

:   Vector3(1, 1, 1), Vector3(2, 2, 2), Vector3(3, 3, 3)

) my_basis = my_basis.scaled_local(Vector3(0, 2, -2))

print(my_basis.x) \# Prints (0.0, 0.0, 0.0) print(my_basis.y) \# Prints
(4.0, 4.0, 4.0) print(my_basis.z) \# Prints (-6.0, -6.0, -6.0)
:::

::: code-tab
csharp

var myBasis = new Basis(

:   new Vector3(1.0f, 1.0f, 1.0f), new Vector3(2.0f, 2.0f, 2.0f), new
    Vector3(3.0f, 3.0f, 3.0f)

); myBasis = myBasis.ScaledLocal(new Vector3(0.0f, 2.0f, -2.0f));

GD.Print(myBasis.X); // Prints (0, 0, 0) GD.Print(myBasis.Y); // Prints
(4, 4, 4) GD.Print(myBasis.Z); // Prints (-6, -6, -6)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_slerp}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **slerp**(to:
`Basis<class_Basis>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_slerp>`{.interpreted-text
role="ref"}

Performs a spherical-linear interpolation with the `to` basis, given a
`weight`. Both this basis and `to` should represent a rotation.

\*\*Example:\*\* Smoothly rotate a
`Node3D<class_Node3D>`{.interpreted-text role="ref"} to the target basis
over time, with a `Tween<class_Tween>`{.interpreted-text role="ref"}:

    var start_basis = Basis.IDENTITY
    var target_basis = Basis.IDENTITY.rotated(Vector3.UP, TAU / 2)

    func _ready():
        create_tween().tween_method(interpolate, 0.0, 1.0, 5.0).set_trans(Tween.TRANS_EXPO)

    func interpolate(weight):
        basis = start_basis.slerp(target_basis, weight)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_tdotx}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tdotx**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_tdotx>`{.interpreted-text
role="ref"}

Returns the transposed dot product between `with` and the
`x<class_Basis_property_x>`{.interpreted-text role="ref"} axis (see
`transposed()<class_Basis_method_transposed>`{.interpreted-text
role="ref"}).

This is equivalent to `basis.x.dot(vector)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_tdoty}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tdoty**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_tdoty>`{.interpreted-text
role="ref"}

Returns the transposed dot product between `with` and the
`y<class_Basis_property_y>`{.interpreted-text role="ref"} axis (see
`transposed()<class_Basis_method_transposed>`{.interpreted-text
role="ref"}).

This is equivalent to `basis.y.dot(vector)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_tdotz}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tdotz**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_tdotz>`{.interpreted-text
role="ref"}

Returns the transposed dot product between `with` and the
`z<class_Basis_property_z>`{.interpreted-text role="ref"} axis (see
`transposed()<class_Basis_method_transposed>`{.interpreted-text
role="ref"}).

This is equivalent to `basis.z.dot(vector)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_method_transposed}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **transposed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Basis_method_transposed>`{.interpreted-text
role="ref"}

Returns the transposed version of this basis. This turns the basis
matrix\'s columns into rows, and its rows into columns.

::::: tabs
::: code-tab
gdscript

var my_basis = Basis(

:   Vector3(1, 2, 3), Vector3(4, 5, 6), Vector3(7, 8, 9)

) my_basis = my_basis.transposed()

print(my_basis.x) \# Prints (1.0, 4.0, 7.0) print(my_basis.y) \# Prints
(2.0, 5.0, 8.0) print(my_basis.z) \# Prints (3.0, 6.0, 9.0)
:::

::: code-tab
csharp

var myBasis = new Basis(

:   new Vector3(1.0f, 2.0f, 3.0f), new Vector3(4.0f, 5.0f, 6.0f), new
    Vector3(7.0f, 8.0f, 9.0f)

); myBasis = myBasis.Transposed();

GD.Print(myBasis.X); // Prints (1, 4, 7) GD.Print(myBasis.Y); // Prints
(2, 5, 8) GD.Print(myBasis.Z); // Prints (3, 6, 9)
:::
:::::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Basis_operator_neq_Basis}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Basis<class_Basis>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_neq_Basis>`{.interpreted-text role="ref"}

Returns `true` if the components of both **Basis** matrices are not
equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Basis_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_mul_Basis}
::: rst-class
classref-operator
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **operator**\*(right:
`Basis<class_Basis>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_mul_Basis>`{.interpreted-text role="ref"}

Transforms (multiplies) the `right` basis by this basis.

This is the operation performed between parent and child
`Node3D<class_Node3D>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_mul_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Basis_operator_mul_Vector3>`{.interpreted-text
role="ref"}

Transforms (multiplies) the `right` vector by this basis, returning a
`Vector3<class_Vector3>`{.interpreted-text role="ref"}.

::::: tabs
::: code-tab
gdscript

\# Basis that swaps the X/Z axes and doubles the scale. var my_basis =
Basis(Vector3(0, 2, 0), Vector3(2, 0, 0), Vector3(0, 0, 2))
print(my_basis \* Vector3(1, 2, 3)) \# Prints (4.0, 2.0, 6.0)
:::

::: code-tab
csharp

// Basis that swaps the X/Z axes and doubles the scale. var myBasis =
new Basis(new Vector3(0, 2, 0), new Vector3(2, 0, 0), new Vector3(0, 0,
2)); GD.Print(myBasis \* new Vector3(1, 2, 3)); // Prints (4, 2, 6)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **operator**\*(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_mul_float>`{.interpreted-text role="ref"}

Multiplies all components of the **Basis** by the given
`float<class_float>`{.interpreted-text role="ref"}. This affects the
basis\'s scale uniformly, resizing all 3 axes by the `right` value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **operator**\*(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies all components of the **Basis** by the given
`int<class_int>`{.interpreted-text role="ref"}. This affects the
basis\'s scale uniformly, resizing all 3 axes by the `right` value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **operator /**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_div_float>`{.interpreted-text role="ref"}

Divides all components of the **Basis** by the given
`float<class_float>`{.interpreted-text role="ref"}. This affects the
basis\'s scale uniformly, resizing all 3 axes by the `right` value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **operator /**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_div_int>`{.interpreted-text role="ref"}

Divides all components of the **Basis** by the given
`int<class_int>`{.interpreted-text role="ref"}. This affects the
basis\'s scale uniformly, resizing all 3 axes by the `right` value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_eq_Basis}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Basis<class_Basis>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_eq_Basis>`{.interpreted-text role="ref"}

Returns `true` if the components of both **Basis** matrices are exactly
equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Basis_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Basis_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Basis_operator_idx_int>`{.interpreted-text role="ref"}

Accesses each axis (column) of this basis by their index. Index `0` is
the same as `x<class_Basis_property_x>`{.interpreted-text role="ref"},
index `1` is the same as `y<class_Basis_property_y>`{.interpreted-text
role="ref"}, and index `2` is the same as
`z<class_Basis_property_z>`{.interpreted-text role="ref"}.

\*\*Note:\*\* In C++, this operator accesses the rows of the basis
matrix, *not* the columns. For the same behavior as scripting languages,
use the `set_column` and `get_column` methods.
