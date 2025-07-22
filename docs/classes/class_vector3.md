github_url
:   hide

# Vector3 {#class_Vector3}

A 3D vector using floating-point coordinates.

::: rst-class
classref-introduction-group
:::

## Description

A 3-element structure that can be used to represent 3D coordinates or
any other triplet of numeric values.

It uses floating-point coordinates. By default, these floating-point
values use 32-bit precision, unlike
`float<class_float>`{.interpreted-text role="ref"} which is always
64-bit. If double precision is needed, compile the engine with the
option `precision=double`.

See `Vector3i<class_Vector3i>`{.interpreted-text role="ref"} for its
integer counterpart.

\*\*Note:\*\* In a boolean context, a Vector3 will evaluate to `false`
if it\'s equal to `Vector3(0, 0, 0)`. Otherwise, a Vector3 will always
evaluate to `true`.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Math documentation index <../tutorials/math/index>`{.interpreted-text
  role="doc"}
- `Vector math <../tutorials/math/vector_math>`{.interpreted-text
  role="doc"}
- `Advanced vector math <../tutorials/math/vectors_advanced>`{.interpreted-text
  role="doc"}
- [3Blue1Brown Essence of Linear
  Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Matrix Transform
  Demo](https://godotengine.org/asset-library/asset/2787)
- [All 3D
  Demos](https://github.com/godotengine/godot-demo-projects/tree/master/3d)

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

## Enumerations

:::: {#enum_Vector3_Axis}
::: rst-class
classref-enumeration
:::
::::

enum **Axis**: `🔗<enum_Vector3_Axis>`{.interpreted-text role="ref"}

:::: {#class_Vector3_constant_AXIS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} **AXIS_X** = `0`

Enumerated value for the X axis. Returned by
`max_axis_index()<class_Vector3_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector3_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector3_constant_AXIS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by
`max_axis_index()<class_Vector3_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector3_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector3_constant_AXIS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by
`max_axis_index()<class_Vector3_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector3_method_min_axis_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Vector3_constant_ZERO}
::: rst-class
classref-constant
:::
::::

**ZERO** = `Vector3(0, 0, 0)`
`🔗<class_Vector3_constant_ZERO>`{.interpreted-text role="ref"}

Zero vector, a vector with all components set to `0`.

:::: {#class_Vector3_constant_ONE}
::: rst-class
classref-constant
:::
::::

**ONE** = `Vector3(1, 1, 1)`
`🔗<class_Vector3_constant_ONE>`{.interpreted-text role="ref"}

One vector, a vector with all components set to `1`.

:::: {#class_Vector3_constant_INF}
::: rst-class
classref-constant
:::
::::

**INF** = `Vector3(inf, inf, inf)`
`🔗<class_Vector3_constant_INF>`{.interpreted-text role="ref"}

Infinity vector, a vector with all components set to
`@GDScript.INF<class_@GDScript_constant_INF>`{.interpreted-text
role="ref"}.

:::: {#class_Vector3_constant_LEFT}
::: rst-class
classref-constant
:::
::::

**LEFT** = `Vector3(-1, 0, 0)`
`🔗<class_Vector3_constant_LEFT>`{.interpreted-text role="ref"}

Left unit vector. Represents the local direction of left, and the global
direction of west.

:::: {#class_Vector3_constant_RIGHT}
::: rst-class
classref-constant
:::
::::

**RIGHT** = `Vector3(1, 0, 0)`
`🔗<class_Vector3_constant_RIGHT>`{.interpreted-text role="ref"}

Right unit vector. Represents the local direction of right, and the
global direction of east.

:::: {#class_Vector3_constant_UP}
::: rst-class
classref-constant
:::
::::

**UP** = `Vector3(0, 1, 0)`
`🔗<class_Vector3_constant_UP>`{.interpreted-text role="ref"}

Up unit vector.

:::: {#class_Vector3_constant_DOWN}
::: rst-class
classref-constant
:::
::::

**DOWN** = `Vector3(0, -1, 0)`
`🔗<class_Vector3_constant_DOWN>`{.interpreted-text role="ref"}

Down unit vector.

:::: {#class_Vector3_constant_FORWARD}
::: rst-class
classref-constant
:::
::::

**FORWARD** = `Vector3(0, 0, -1)`
`🔗<class_Vector3_constant_FORWARD>`{.interpreted-text role="ref"}

Forward unit vector. Represents the local direction of forward, and the
global direction of north. Keep in mind that the forward direction for
lights, cameras, etc is different from 3D assets like characters, which
face towards the camera by convention. Use
`MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>`{.interpreted-text
role="ref"} and similar constants when working in 3D asset space.

:::: {#class_Vector3_constant_BACK}
::: rst-class
classref-constant
:::
::::

**BACK** = `Vector3(0, 0, 1)`
`🔗<class_Vector3_constant_BACK>`{.interpreted-text role="ref"}

Back unit vector. Represents the local direction of back, and the global
direction of south.

:::: {#class_Vector3_constant_MODEL_LEFT}
::: rst-class
classref-constant
:::
::::

**MODEL_LEFT** = `Vector3(1, 0, 0)`
`🔗<class_Vector3_constant_MODEL_LEFT>`{.interpreted-text role="ref"}

Unit vector pointing towards the left side of imported 3D assets.

:::: {#class_Vector3_constant_MODEL_RIGHT}
::: rst-class
classref-constant
:::
::::

**MODEL_RIGHT** = `Vector3(-1, 0, 0)`
`🔗<class_Vector3_constant_MODEL_RIGHT>`{.interpreted-text role="ref"}

Unit vector pointing towards the right side of imported 3D assets.

:::: {#class_Vector3_constant_MODEL_TOP}
::: rst-class
classref-constant
:::
::::

**MODEL_TOP** = `Vector3(0, 1, 0)`
`🔗<class_Vector3_constant_MODEL_TOP>`{.interpreted-text role="ref"}

Unit vector pointing towards the top side (up) of imported 3D assets.

:::: {#class_Vector3_constant_MODEL_BOTTOM}
::: rst-class
classref-constant
:::
::::

**MODEL_BOTTOM** = `Vector3(0, -1, 0)`
`🔗<class_Vector3_constant_MODEL_BOTTOM>`{.interpreted-text role="ref"}

Unit vector pointing towards the bottom side (down) of imported 3D
assets.

:::: {#class_Vector3_constant_MODEL_FRONT}
::: rst-class
classref-constant
:::
::::

**MODEL_FRONT** = `Vector3(0, 0, 1)`
`🔗<class_Vector3_constant_MODEL_FRONT>`{.interpreted-text role="ref"}

Unit vector pointing towards the front side (facing forward) of imported
3D assets.

:::: {#class_Vector3_constant_MODEL_REAR}
::: rst-class
classref-constant
:::
::::

**MODEL_REAR** = `Vector3(0, 0, -1)`
`🔗<class_Vector3_constant_MODEL_REAR>`{.interpreted-text role="ref"}

Unit vector pointing towards the rear side (back) of imported 3D assets.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Vector3_property_x}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **x** = `0.0`
`🔗<class_Vector3_property_x>`{.interpreted-text role="ref"}

The vector\'s X component. Also accessible by using the index position
`[0]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_property_y}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **y** = `0.0`
`🔗<class_Vector3_property_y>`{.interpreted-text role="ref"}

The vector\'s Y component. Also accessible by using the index position
`[1]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_property_z}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **z** = `0.0`
`🔗<class_Vector3_property_z>`{.interpreted-text role="ref"}

The vector\'s Z component. Also accessible by using the index position
`[2]`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Vector3_constructor_Vector3}
::: rst-class
classref-constructor
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **Vector3**()
`🔗<class_Vector3_constructor_Vector3>`{.interpreted-text role="ref"}

Constructs a default-initialized **Vector3** with all components set to
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **Vector3**(from:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})

Constructs a **Vector3** as a copy of the given **Vector3**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **Vector3**(from:
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"})

Constructs a new **Vector3** from
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **Vector3**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"}, z:
`float<class_float>`{.interpreted-text role="ref"})

Returns a **Vector3** with the given components.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Vector3_method_abs}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **abs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_abs>`{.interpreted-text
role="ref"}

Returns a new vector with all components in absolute values (i.e.
positive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_angle_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_to**(to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_angle_to>`{.interpreted-text
role="ref"}

Returns the unsigned minimum angle to the given vector, in radians.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_bezier_derivative}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**bezier_derivative**(control_1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, control_2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, end:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_bezier_derivative>`{.interpreted-text
role="ref"}

Returns the derivative at the given `t` on the [Bézier
curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by this
vector and the given `control_1`, `control_2`, and `end` points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_bezier_interpolate}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**bezier_interpolate**(control_1:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, control_2:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, end:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_bezier_interpolate>`{.interpreted-text
role="ref"}

Returns the point at the given `t` on the [Bézier
curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by this
vector and the given `control_1`, `control_2`, and `end` points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_bounce}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **bounce**(n:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_bounce>`{.interpreted-text
role="ref"}

Returns the vector \"bounced off\" from a plane defined by the given
normal `n`.

\*\*Note:\*\* `bounce()<class_Vector3_method_bounce>`{.interpreted-text
role="ref"} performs the operation that most engines and frameworks call
`reflect()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_ceil}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **ceil**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_ceil>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded up (towards positive
infinity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_clamp}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **clamp**(min:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, max:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_clamp>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between the components
of `min` and `max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_clampf}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **clampf**(min:
`float<class_float>`{.interpreted-text role="ref"}, max:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_clampf>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between `min` and
`max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_cross}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **cross**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_cross>`{.interpreted-text
role="ref"}

Returns the cross product of this vector and `with`.

This returns a vector perpendicular to both this and `with`, which would
be the normal vector of the plane defined by the two vectors. As there
are two such vectors, in opposite directions, this method returns the
vector defined by a right-handed coordinate system. If the two vectors
are parallel this returns an empty vector, making it useful for testing
if two vectors are parallel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_cubic_interpolate}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**cubic_interpolate**(b: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, pre_a: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, post_b: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, weight: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_cubic_interpolate>`{.interpreted-text
role="ref"}

Performs a cubic interpolation between this vector and `b` using `pre_a`
and `post_b` as handles, and returns the result at position `weight`.
`weight` is on the range of 0.0 to 1.0, representing the amount of
interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_cubic_interpolate_in_time}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**cubic_interpolate_in_time**(b:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, pre_a:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, post_b:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"}, b_t:
`float<class_float>`{.interpreted-text role="ref"}, pre_a_t:
`float<class_float>`{.interpreted-text role="ref"}, post_b_t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_cubic_interpolate_in_time>`{.interpreted-text
role="ref"}

Performs a cubic interpolation between this vector and `b` using `pre_a`
and `post_b` as handles, and returns the result at position `weight`.
`weight` is on the range of 0.0 to 1.0, representing the amount of
interpolation.

It can perform smoother interpolation than
`cubic_interpolate()<class_Vector3_method_cubic_interpolate>`{.interpreted-text
role="ref"} by the time values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_direction_to}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**direction_to**(to: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_direction_to>`{.interpreted-text
role="ref"}

Returns the normalized vector pointing from this vector to `to`. This is
equivalent to using `(b - a).normalized()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_distance_squared_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_squared_to**(to: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_distance_squared_to>`{.interpreted-text
role="ref"}

Returns the squared distance between this vector and `to`.

This method runs faster than
`distance_to()<class_Vector3_method_distance_to>`{.interpreted-text
role="ref"}, so prefer it if you need to compare vectors or need the
squared distance for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_distance_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **distance_to**(to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_distance_to>`{.interpreted-text
role="ref"}

Returns the distance between this vector and `to`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_dot}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dot**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_dot>`{.interpreted-text
role="ref"}

Returns the dot product of this vector and `with`. This can be used to
compare the angle between two vectors. For example, this can be used to
determine whether an enemy is facing the player.

The dot product will be `0` for a right angle (90 degrees), greater than
0 for angles narrower than 90 degrees and lower than 0 for angles wider
than 90 degrees.

When using unit (normalized) vectors, the result will always be between
`-1.0` (180 degree angle) when the vectors are facing opposite
directions, and `1.0` (0 degree angle) when the vectors are aligned.

\*\*Note:\*\* `a.dot(b)` is equivalent to `b.dot(a)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_floor}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **floor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_floor>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded down (towards negative
infinity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_inverse}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_inverse>`{.interpreted-text
role="ref"}

Returns the inverse of the vector. This is the same as
`Vector3(1.0 / v.x, 1.0 / v.y, 1.0 / v.z)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_is_equal_approx>`{.interpreted-text role="ref"}

Returns `true` if this vector and `to` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this vector is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_is_normalized}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_is_normalized>`{.interpreted-text
role="ref"}

Returns `true` if the vector is normalized, i.e. its length is
approximately equal to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_is_zero_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_zero_approx**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_is_zero_approx>`{.interpreted-text
role="ref"}

Returns `true` if this vector\'s values are approximately zero, by
running
`@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>`{.interpreted-text
role="ref"} on each component.

This method is faster than using
`is_equal_approx()<class_Vector3_method_is_equal_approx>`{.interpreted-text
role="ref"} with one value as a zero vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_length>`{.interpreted-text
role="ref"}

Returns the length (magnitude) of this vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_length_squared}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length_squared**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_length_squared>`{.interpreted-text
role="ref"}

Returns the squared length (squared magnitude) of this vector.

This method runs faster than
`length()<class_Vector3_method_length>`{.interpreted-text role="ref"},
so prefer it if you need to compare vectors or need the squared distance
for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_lerp}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **lerp**(to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_lerp>`{.interpreted-text
role="ref"}

Returns the result of the linear interpolation between this vector and
`to` by amount `weight`. `weight` is on the range of `0.0` to `1.0`,
representing the amount of interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_limit_length}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**limit_length**(length: `float<class_float>`{.interpreted-text
role="ref"} = 1.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_limit_length>`{.interpreted-text
role="ref"}

Returns the vector with a maximum length by limiting its length to
`length`. If the vector is non-finite, the result is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_max}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **max**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_max>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector3(maxf(x, with.x), maxf(y, with.y), maxf(z, with.z))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_max_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_max_axis_index>`{.interpreted-text
role="ref"}

Returns the axis of the vector\'s highest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_X<class_Vector3_constant_AXIS_X>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_maxf}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **maxf**(with:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_maxf>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector3(maxf(x, with), maxf(y, with), maxf(z, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_min}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **min**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_min>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector3(minf(x, with.x), minf(y, with.y), minf(z, with.z))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_min_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **min_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_min_axis_index>`{.interpreted-text
role="ref"}

Returns the axis of the vector\'s lowest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_Z<class_Vector3_constant_AXIS_Z>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_minf}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **minf**(with:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_minf>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector3(minf(x, with), minf(y, with), minf(z, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_move_toward}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**move_toward**(to: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, delta: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_move_toward>`{.interpreted-text
role="ref"}

Returns a new vector moved toward `to` by the fixed `delta` amount. Will
not go past the final value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_normalized}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_normalized>`{.interpreted-text
role="ref"}

Returns the result of scaling the vector to unit length. Equivalent to
`v / v.length()`. Returns `(0, 0, 0)` if `v.length() == 0`. See also
`is_normalized()<class_Vector3_method_is_normalized>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This function may return incorrect values if the input
vector length is near zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_octahedron_decode}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**octahedron_decode**(uv: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_octahedron_decode>`{.interpreted-text
role="ref"}

Returns the **Vector3** from an octahedral-compressed form created using
`octahedron_encode()<class_Vector3_method_octahedron_encode>`{.interpreted-text
role="ref"} (stored as a `Vector2<class_Vector2>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_octahedron_encode}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**octahedron_encode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_octahedron_encode>`{.interpreted-text
role="ref"}

Returns the octahedral-encoded (oct32) form of this **Vector3** as a
`Vector2<class_Vector2>`{.interpreted-text role="ref"}. Since a
`Vector2<class_Vector2>`{.interpreted-text role="ref"} occupies 1/3 less
memory compared to **Vector3**, this form of compression can be used to
pass greater amounts of
`normalized()<class_Vector3_method_normalized>`{.interpreted-text
role="ref"} **Vector3**s without increasing storage or memory
requirements. See also
`octahedron_decode()<class_Vector3_method_octahedron_decode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`octahedron_encode()<class_Vector3_method_octahedron_encode>`{.interpreted-text
role="ref"} can only be used for
`normalized()<class_Vector3_method_normalized>`{.interpreted-text
role="ref"} vectors.
`octahedron_encode()<class_Vector3_method_octahedron_encode>`{.interpreted-text
role="ref"} does *not* check whether this **Vector3** is normalized, and
will return a value that does not decompress to the original value if
the **Vector3** is not normalized.

\*\*Note:\*\* Octahedral compression is *lossy*, although visual
differences are rarely perceptible in real world scenarios.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_outer}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **outer**(with:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_outer>`{.interpreted-text
role="ref"}

Returns the outer product with `with`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_posmod}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **posmod**(mod:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_posmod>`{.interpreted-text
role="ref"}

Returns a vector composed of the
`@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} of this vector\'s components and `mod`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_posmodv}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **posmodv**(modv:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_posmodv>`{.interpreted-text
role="ref"}

Returns a vector composed of the
`@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} of this vector\'s components and `modv`\'s components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_project}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **project**(b:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_project>`{.interpreted-text
role="ref"}

Returns a new vector resulting from projecting this vector onto the
given vector `b`. The resulting new vector is parallel to `b`. See also
`slide()<class_Vector3_method_slide>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If the vector `b` is a zero vector, the components of the
resulting new vector will be
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_reflect}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **reflect**(n:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_reflect>`{.interpreted-text
role="ref"}

Returns the result of reflecting the vector through a plane defined by
the given normal vector `n`.

\*\*Note:\*\*
`reflect()<class_Vector3_method_reflect>`{.interpreted-text role="ref"}
differs from what other engines and frameworks call `reflect()`. In
other engines, `reflect()` returns the result of the vector reflected by
the given plane. The reflection thus passes through the given normal.
While in Godot the reflection passes through the plane and can be
thought of as bouncing off the normal. See also
`bounce()<class_Vector3_method_bounce>`{.interpreted-text role="ref"}
which does what most engines call `reflect()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_rotated}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **rotated**(axis:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, angle:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_rotated>`{.interpreted-text
role="ref"}

Returns the result of rotating this vector around a given axis by
`angle` (in radians). The axis must be a normalized vector. See also
`@GlobalScope.deg_to_rad()<class_@GlobalScope_method_deg_to_rad>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_round}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **round**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_round>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded to the nearest integer,
with halfway cases rounded away from zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_sign}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **sign**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_sign>`{.interpreted-text
role="ref"}

Returns a new vector with each component set to `1.0` if it\'s positive,
`-1.0` if it\'s negative, and `0.0` if it\'s zero. The result is
identical to calling
`@GlobalScope.sign()<class_@GlobalScope_method_sign>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_signed_angle_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**signed_angle_to**(to: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector3_method_signed_angle_to>`{.interpreted-text role="ref"}

Returns the signed angle to the given vector, in radians. The sign of
the angle is positive in a counter-clockwise direction and negative in a
clockwise direction when viewed from the side specified by the `axis`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_slerp}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **slerp**(to:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_slerp>`{.interpreted-text
role="ref"}

Returns the result of spherical linear interpolation between this vector
and `to`, by amount `weight`. `weight` is on the range of 0.0 to 1.0,
representing the amount of interpolation.

This method also handles interpolating the lengths if the input vectors
have different lengths. For the special case of one or both input
vectors having zero length, this method behaves like
`lerp()<class_Vector3_method_lerp>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_slide}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **slide**(n:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_slide>`{.interpreted-text
role="ref"}

Returns a new vector resulting from sliding this vector along a plane
with normal `n`. The resulting new vector is perpendicular to `n`, and
is equivalent to this vector minus its projection on `n`. See also
`project()<class_Vector3_method_project>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The vector `n` must be normalized. See also
`normalized()<class_Vector3_method_normalized>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_snapped}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **snapped**(step:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_snapped>`{.interpreted-text
role="ref"}

Returns a new vector with each component snapped to the nearest multiple
of the corresponding component in `step`. This can also be used to round
the components to an arbitrary number of decimals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_method_snappedf}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**snappedf**(step: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector3_method_snappedf>`{.interpreted-text
role="ref"}

Returns a new vector with each component snapped to the nearest multiple
of `step`. This can also be used to round the components to an arbitrary
number of decimals.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Vector3_operator_neq_Vector3}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_neq_Vector3>`{.interpreted-text role="ref"}

Returns `true` if the vectors are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Vector3_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_mul_Basis}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Basis<class_Basis>`{.interpreted-text
role="ref"}) `🔗<class_Vector3_operator_mul_Basis>`{.interpreted-text
role="ref"}

Inversely transforms (multiplies) the **Vector3** by the given
`Basis<class_Basis>`{.interpreted-text role="ref"} matrix, under the
assumption that the basis is orthonormal (i.e. rotation/reflection is
fine, scaling/skew is not).

`vector * basis` is equivalent to `basis.transposed() * vector`. See
`Basis.transposed()<class_Basis_method_transposed>`{.interpreted-text
role="ref"}.

For transforming by inverse of a non-orthonormal basis (e.g. with
scaling) `basis.inverse() * vector` can be used instead. See
`Basis.inverse()<class_Basis_method_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_mul_Quaternion}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"})
`🔗<class_Vector3_operator_mul_Quaternion>`{.interpreted-text
role="ref"}

Inversely transforms (multiplies) the **Vector3** by the given
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}.

`vector * quaternion` is equivalent to `quaternion.inverse() * vector`.
See
`Quaternion.inverse()<class_Quaternion_method_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_mul_Transform3D}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_Vector3_operator_mul_Transform3D>`{.interpreted-text
role="ref"}

Inversely transforms (multiplies) the **Vector3** by the given
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
transformation matrix, under the assumption that the transformation
basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is
not).

`vector * transform` is equivalent to `transform.inverse() * vector`.
See
`Transform3D.inverse()<class_Transform3D_method_inverse>`{.interpreted-text
role="ref"}.

For transforming by inverse of an affine transformation (e.g. with
scaling) `transform.affine_inverse() * vector` can be used instead. See
`Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_mul_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Vector3_operator_mul_Vector3>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector3** by the components of the
given **Vector3**.

    print(Vector3(10, 20, 30) * Vector3(3, 4, 5)) # Prints (30.0, 80.0, 150.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Vector3_operator_mul_float>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector3** by the given
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies each component of the **Vector3** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_sum_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
+**(right: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_sum_Vector3>`{.interpreted-text role="ref"}

Adds each component of the **Vector3** by the components of the given
**Vector3**.

    print(Vector3(10, 20, 30) + Vector3(3, 4, 5)) # Prints (13.0, 24.0, 35.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_dif_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
-**(right: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_dif_Vector3>`{.interpreted-text role="ref"}

Subtracts each component of the **Vector3** by the components of the
given **Vector3**.

    print(Vector3(10, 20, 30) - Vector3(3, 4, 5)) # Prints (7.0, 16.0, 25.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_div_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
/**(right: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_div_Vector3>`{.interpreted-text role="ref"}

Divides each component of the **Vector3** by the components of the given
**Vector3**.

    print(Vector3(10, 20, 30) / Vector3(2, 5, 3)) # Prints (5.0, 4.0, 10.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
/**(right: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_div_float>`{.interpreted-text role="ref"}

Divides each component of the **Vector3** by the given
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
/**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_div_int>`{.interpreted-text role="ref"}

Divides each component of the **Vector3** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_lt_Vector3}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_lt_Vector3>`{.interpreted-text role="ref"}

Compares two **Vector3** vectors by first checking if the X value of the
left vector is less than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors, and then with the Z values. This operator is useful
for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_lte_Vector3}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_lte_Vector3>`{.interpreted-text role="ref"}

Compares two **Vector3** vectors by first checking if the X value of the
left vector is less than or equal to the X value of the `right` vector.
If the X values are exactly equal, then it repeats this check with the Y
values of the two vectors, and then with the Z values. This operator is
useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_eq_Vector3}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_eq_Vector3>`{.interpreted-text role="ref"}

Returns `true` if the vectors are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Vector3_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_gt_Vector3}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_gt_Vector3>`{.interpreted-text role="ref"}

Compares two **Vector3** vectors by first checking if the X value of the
left vector is greater than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors, and then with the Z values. This operator is useful
for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_gte_Vector3}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_gte_Vector3>`{.interpreted-text role="ref"}

Compares two **Vector3** vectors by first checking if the X value of the
left vector is greater than or equal to the X value of the `right`
vector. If the X values are exactly equal, then it repeats this check
with the Y values of the two vectors, and then with the Z values. This
operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector3_operator_idx_int>`{.interpreted-text role="ref"}

Access vector components using their `index`. `v[0]` is equivalent to
`v.x`, `v[1]` is equivalent to `v.y`, and `v[2]` is equivalent to `v.z`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_unplus}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
unary+**() `🔗<class_Vector3_operator_unplus>`{.interpreted-text
role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector3_operator_unminus}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **operator
unary-**() `🔗<class_Vector3_operator_unminus>`{.interpreted-text
role="ref"}

Returns the negative value of the **Vector3**. This is the same as
writing `Vector3(-v.x, -v.y, -v.z)`. This operation flips the direction
of the vector while keeping the same magnitude. With floats, the number
zero can be either positive or negative.
