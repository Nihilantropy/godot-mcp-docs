github_url
:   hide

# Vector2 {#class_Vector2}

A 2D vector using floating-point coordinates.

::: rst-class
classref-introduction-group
:::

## Description

A 2-element structure that can be used to represent 2D coordinates or
any other pair of numeric values.

It uses floating-point coordinates. By default, these floating-point
values use 32-bit precision, unlike
`float<class_float>`{.interpreted-text role="ref"} which is always
64-bit. If double precision is needed, compile the engine with the
option `precision=double`.

See `Vector2i<class_Vector2i>`{.interpreted-text role="ref"} for its
integer counterpart.

\*\*Note:\*\* In a boolean context, a Vector2 will evaluate to `false`
if it\'s equal to `Vector2(0, 0)`. Otherwise, a Vector2 will always
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
- [All 2D
  Demos](https://github.com/godotengine/godot-demo-projects/tree/master/2d)

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

:::: {#enum_Vector2_Axis}
::: rst-class
classref-enumeration
:::
::::

enum **Axis**: `🔗<enum_Vector2_Axis>`{.interpreted-text role="ref"}

:::: {#class_Vector2_constant_AXIS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector2_Axis>`{.interpreted-text role="ref"} **AXIS_X** = `0`

Enumerated value for the X axis. Returned by
`max_axis_index()<class_Vector2_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector2_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector2_constant_AXIS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector2_Axis>`{.interpreted-text role="ref"} **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by
`max_axis_index()<class_Vector2_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector2_method_min_axis_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Vector2_constant_ZERO}
::: rst-class
classref-constant
:::
::::

**ZERO** = `Vector2(0, 0)`
`🔗<class_Vector2_constant_ZERO>`{.interpreted-text role="ref"}

Zero vector, a vector with all components set to `0`.

:::: {#class_Vector2_constant_ONE}
::: rst-class
classref-constant
:::
::::

**ONE** = `Vector2(1, 1)`
`🔗<class_Vector2_constant_ONE>`{.interpreted-text role="ref"}

One vector, a vector with all components set to `1`.

:::: {#class_Vector2_constant_INF}
::: rst-class
classref-constant
:::
::::

**INF** = `Vector2(inf, inf)`
`🔗<class_Vector2_constant_INF>`{.interpreted-text role="ref"}

Infinity vector, a vector with all components set to
`@GDScript.INF<class_@GDScript_constant_INF>`{.interpreted-text
role="ref"}.

:::: {#class_Vector2_constant_LEFT}
::: rst-class
classref-constant
:::
::::

**LEFT** = `Vector2(-1, 0)`
`🔗<class_Vector2_constant_LEFT>`{.interpreted-text role="ref"}

Left unit vector. Represents the direction of left.

:::: {#class_Vector2_constant_RIGHT}
::: rst-class
classref-constant
:::
::::

**RIGHT** = `Vector2(1, 0)`
`🔗<class_Vector2_constant_RIGHT>`{.interpreted-text role="ref"}

Right unit vector. Represents the direction of right.

:::: {#class_Vector2_constant_UP}
::: rst-class
classref-constant
:::
::::

**UP** = `Vector2(0, -1)`
`🔗<class_Vector2_constant_UP>`{.interpreted-text role="ref"}

Up unit vector. Y is down in 2D, so this vector points -Y.

:::: {#class_Vector2_constant_DOWN}
::: rst-class
classref-constant
:::
::::

**DOWN** = `Vector2(0, 1)`
`🔗<class_Vector2_constant_DOWN>`{.interpreted-text role="ref"}

Down unit vector. Y is down in 2D, so this vector points +Y.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Vector2_property_x}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **x** = `0.0`
`🔗<class_Vector2_property_x>`{.interpreted-text role="ref"}

The vector\'s X component. Also accessible by using the index position
`[0]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_property_y}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **y** = `0.0`
`🔗<class_Vector2_property_y>`{.interpreted-text role="ref"}

The vector\'s Y component. Also accessible by using the index position
`[1]`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Vector2_constructor_Vector2}
::: rst-class
classref-constructor
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **Vector2**()
`🔗<class_Vector2_constructor_Vector2>`{.interpreted-text role="ref"}

Constructs a default-initialized **Vector2** with all components set to
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **Vector2**(from:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})

Constructs a **Vector2** as a copy of the given **Vector2**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **Vector2**(from:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})

Constructs a new **Vector2** from
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **Vector2**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a new **Vector2** from the given `x` and `y`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Vector2_method_abs}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **abs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_abs>`{.interpreted-text
role="ref"}

Returns a new vector with all components in absolute values (i.e.
positive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_angle>`{.interpreted-text
role="ref"}

Returns this vector\'s angle with respect to the positive X axis, or
`(1, 0)` vector, in radians.

For example, `Vector2.RIGHT.angle()` will return zero,
`Vector2.DOWN.angle()` will return `PI / 2` (a quarter turn, or 90
degrees), and `Vector2(1, -1).angle()` will return `-PI / 4` (a negative
eighth turn, or -45 degrees).

\`Illustration of the returned angle.
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/vector2_angle.png\>\`\_\_

Equivalent to the result of
`@GlobalScope.atan2()<class_@GlobalScope_method_atan2>`{.interpreted-text
role="ref"} when called with the vector\'s
`y<class_Vector2_property_y>`{.interpreted-text role="ref"} and
`x<class_Vector2_property_x>`{.interpreted-text role="ref"} as
parameters: `atan2(y, x)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_angle_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_to**(to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_angle_to>`{.interpreted-text
role="ref"}

Returns the signed angle to the given vector, in radians.

\`Illustration of the returned angle.
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/vector2_angle_to.png\>\`\_\_

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_angle_to_point}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angle_to_point**(to: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_angle_to_point>`{.interpreted-text
role="ref"}

Returns the angle between the line connecting the two points and the X
axis, in radians.

`a.angle_to_point(b)` is equivalent of doing `(b - a).angle()`.

\`Illustration of the returned angle.
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/vector2_angle_to_point.png\>\`\_\_

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_aspect}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **aspect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_aspect>`{.interpreted-text
role="ref"}

Returns the aspect ratio of this vector, the ratio of
`x<class_Vector2_property_x>`{.interpreted-text role="ref"} to
`y<class_Vector2_property_y>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_bezier_derivative}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**bezier_derivative**(control_1:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, control_2:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, end:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector2_method_bezier_derivative>`{.interpreted-text
role="ref"}

Returns the derivative at the given `t` on the [Bézier
curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by this
vector and the given `control_1`, `control_2`, and `end` points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_bezier_interpolate}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**bezier_interpolate**(control_1:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, control_2:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, end:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector2_method_bezier_interpolate>`{.interpreted-text
role="ref"}

Returns the point at the given `t` on the [Bézier
curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by this
vector and the given `control_1`, `control_2`, and `end` points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_bounce}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **bounce**(n:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_bounce>`{.interpreted-text
role="ref"}

Returns the vector \"bounced off\" from a line defined by the given
normal `n` perpendicular to the line.

\*\*Note:\*\* `bounce()<class_Vector2_method_bounce>`{.interpreted-text
role="ref"} performs the operation that most engines and frameworks call
`reflect()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_ceil}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **ceil**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_ceil>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded up (towards positive
infinity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_clamp}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **clamp**(min:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, max:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_clamp>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between the components
of `min` and `max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_clampf}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **clampf**(min:
`float<class_float>`{.interpreted-text role="ref"}, max:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_clampf>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between `min` and
`max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_cross}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cross**(with:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_cross>`{.interpreted-text
role="ref"}

Returns the 2D analog of the cross product for this vector and `with`.

This is the signed area of the parallelogram formed by the two vectors.
If the second vector is clockwise from the first vector, then the cross
product is the positive area. If counter-clockwise, the cross product is
the negative area. If the two vectors are parallel this returns zero,
making it useful for testing if two vectors are parallel.

\*\*Note:\*\* Cross product is not defined in 2D mathematically. This
method embeds the 2D vectors in the XY plane of 3D space and uses their
cross product\'s Z component as the analog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_cubic_interpolate}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**cubic_interpolate**(b: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, pre_a: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, post_b: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, weight: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector2_method_cubic_interpolate>`{.interpreted-text
role="ref"}

Performs a cubic interpolation between this vector and `b` using `pre_a`
and `post_b` as handles, and returns the result at position `weight`.
`weight` is on the range of 0.0 to 1.0, representing the amount of
interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_cubic_interpolate_in_time}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**cubic_interpolate_in_time**(b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, pre_a:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, post_b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"}, b_t:
`float<class_float>`{.interpreted-text role="ref"}, pre_a_t:
`float<class_float>`{.interpreted-text role="ref"}, post_b_t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector2_method_cubic_interpolate_in_time>`{.interpreted-text
role="ref"}

Performs a cubic interpolation between this vector and `b` using `pre_a`
and `post_b` as handles, and returns the result at position `weight`.
`weight` is on the range of 0.0 to 1.0, representing the amount of
interpolation.

It can perform smoother interpolation than
`cubic_interpolate()<class_Vector2_method_cubic_interpolate>`{.interpreted-text
role="ref"} by the time values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_direction_to}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**direction_to**(to: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_direction_to>`{.interpreted-text
role="ref"}

Returns the normalized vector pointing from this vector to `to`. This is
equivalent to using `(b - a).normalized()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_distance_squared_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_squared_to**(to: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector2_method_distance_squared_to>`{.interpreted-text
role="ref"}

Returns the squared distance between this vector and `to`.

This method runs faster than
`distance_to()<class_Vector2_method_distance_to>`{.interpreted-text
role="ref"}, so prefer it if you need to compare vectors or need the
squared distance for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_distance_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **distance_to**(to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_distance_to>`{.interpreted-text
role="ref"}

Returns the distance between this vector and `to`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_dot}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dot**(with:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_dot>`{.interpreted-text
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

:::: {#class_Vector2_method_floor}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **floor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_floor>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded down (towards negative
infinity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_from_angle}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**from_angle**(angle: `float<class_float>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_from_angle>`{.interpreted-text
role="ref"}

Creates a **Vector2** rotated to the given `angle` in radians. This is
equivalent to doing `Vector2(cos(angle), sin(angle))` or
`Vector2.RIGHT.rotated(angle)`.

    print(Vector2.from_angle(0)) # Prints (1.0, 0.0)
    print(Vector2(1, 0).angle()) # Prints 0.0, which is the angle used above.
    print(Vector2.from_angle(PI / 2)) # Prints (0.0, 1.0)

\*\*Note:\*\* The length of the returned **Vector2** is *approximately*
`1.0`, but is is not guaranteed to be exactly `1.0` due to
floating-point precision issues. Call
`normalized()<class_Vector2_method_normalized>`{.interpreted-text
role="ref"} on the returned **Vector2** if you require a unit vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector2_method_is_equal_approx>`{.interpreted-text role="ref"}

Returns `true` if this vector and `to` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this vector is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_is_normalized}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_is_normalized>`{.interpreted-text
role="ref"}

Returns `true` if the vector is normalized, i.e. its length is
approximately equal to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_is_zero_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_zero_approx**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_is_zero_approx>`{.interpreted-text
role="ref"}

Returns `true` if this vector\'s values are approximately zero, by
running
`@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>`{.interpreted-text
role="ref"} on each component.

This method is faster than using
`is_equal_approx()<class_Vector2_method_is_equal_approx>`{.interpreted-text
role="ref"} with one value as a zero vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_length>`{.interpreted-text
role="ref"}

Returns the length (magnitude) of this vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_length_squared}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length_squared**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_length_squared>`{.interpreted-text
role="ref"}

Returns the squared length (squared magnitude) of this vector.

This method runs faster than
`length()<class_Vector2_method_length>`{.interpreted-text role="ref"},
so prefer it if you need to compare vectors or need the squared distance
for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_lerp}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **lerp**(to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_lerp>`{.interpreted-text
role="ref"}

Returns the result of the linear interpolation between this vector and
`to` by amount `weight`. `weight` is on the range of `0.0` to `1.0`,
representing the amount of interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_limit_length}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**limit_length**(length: `float<class_float>`{.interpreted-text
role="ref"} = 1.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_limit_length>`{.interpreted-text
role="ref"}

Returns the vector with a maximum length by limiting its length to
`length`. If the vector is non-finite, the result is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_max}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **max**(with:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_max>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector2(maxf(x, with.x), maxf(y, with.y))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_max_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_max_axis_index>`{.interpreted-text
role="ref"}

Returns the axis of the vector\'s highest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_X<class_Vector2_constant_AXIS_X>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_maxf}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **maxf**(with:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_maxf>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector2(maxf(x, with), maxf(y, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_min}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **min**(with:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_min>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector2(minf(x, with.x), minf(y, with.y))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_min_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **min_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_min_axis_index>`{.interpreted-text
role="ref"}

Returns the axis of the vector\'s lowest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_Y<class_Vector2_constant_AXIS_Y>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_minf}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **minf**(with:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_minf>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector2(minf(x, with), minf(y, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_move_toward}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**move_toward**(to: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, delta: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_move_toward>`{.interpreted-text
role="ref"}

Returns a new vector moved toward `to` by the fixed `delta` amount. Will
not go past the final value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_normalized}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_normalized>`{.interpreted-text
role="ref"}

Returns the result of scaling the vector to unit length. Equivalent to
`v / v.length()`. Returns `(0, 0)` if `v.length() == 0`. See also
`is_normalized()<class_Vector2_method_is_normalized>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This function may return incorrect values if the input
vector length is near zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_orthogonal}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **orthogonal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_orthogonal>`{.interpreted-text
role="ref"}

Returns a perpendicular vector rotated 90 degrees counter-clockwise
compared to the original, with the same length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_posmod}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **posmod**(mod:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_posmod>`{.interpreted-text
role="ref"}

Returns a vector composed of the
`@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} of this vector\'s components and `mod`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_posmodv}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **posmodv**(modv:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_posmodv>`{.interpreted-text
role="ref"}

Returns a vector composed of the
`@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} of this vector\'s components and `modv`\'s components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_project}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **project**(b:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_project>`{.interpreted-text
role="ref"}

Returns a new vector resulting from projecting this vector onto the
given vector `b`. The resulting new vector is parallel to `b`. See also
`slide()<class_Vector2_method_slide>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If the vector `b` is a zero vector, the components of the
resulting new vector will be
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_reflect}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **reflect**(line:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_reflect>`{.interpreted-text
role="ref"}

Returns the result of reflecting the vector from a line defined by the
given direction vector `line`.

\*\*Note:\*\*
`reflect()<class_Vector2_method_reflect>`{.interpreted-text role="ref"}
differs from what other engines and frameworks call `reflect()`. In
other engines, `reflect()` takes a normal direction which is a direction
perpendicular to the line. In Godot, you specify the direction of the
line directly. See also
`bounce()<class_Vector2_method_bounce>`{.interpreted-text role="ref"}
which does what most engines call `reflect()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_rotated}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**rotated**(angle: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_rotated>`{.interpreted-text
role="ref"}

Returns the result of rotating this vector by `angle` (in radians). See
also
`@GlobalScope.deg_to_rad()<class_@GlobalScope_method_deg_to_rad>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_round}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **round**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_round>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded to the nearest integer,
with halfway cases rounded away from zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_sign}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **sign**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_sign>`{.interpreted-text
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

:::: {#class_Vector2_method_slerp}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **slerp**(to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_slerp>`{.interpreted-text
role="ref"}

Returns the result of spherical linear interpolation between this vector
and `to`, by amount `weight`. `weight` is on the range of 0.0 to 1.0,
representing the amount of interpolation.

This method also handles interpolating the lengths if the input vectors
have different lengths. For the special case of one or both input
vectors having zero length, this method behaves like
`lerp()<class_Vector2_method_lerp>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_slide}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **slide**(n:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_slide>`{.interpreted-text
role="ref"}

Returns a new vector resulting from sliding this vector along a line
with normal `n`. The resulting new vector is perpendicular to `n`, and
is equivalent to this vector minus its projection on `n`. See also
`project()<class_Vector2_method_project>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The vector `n` must be normalized. See also
`normalized()<class_Vector2_method_normalized>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_snapped}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **snapped**(step:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_snapped>`{.interpreted-text
role="ref"}

Returns a new vector with each component snapped to the nearest multiple
of the corresponding component in `step`. This can also be used to round
the components to an arbitrary number of decimals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_method_snappedf}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**snappedf**(step: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector2_method_snappedf>`{.interpreted-text
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

:::: {#class_Vector2_operator_neq_Vector2}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_neq_Vector2>`{.interpreted-text role="ref"}

Returns `true` if the vectors are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Vector2_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_mul_Transform2D}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`🔗<class_Vector2_operator_mul_Transform2D>`{.interpreted-text
role="ref"}

Inversely transforms (multiplies) the **Vector2** by the given
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
transformation matrix, under the assumption that the transformation
basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is
not).

`vector * transform` is equivalent to `transform.inverse() * vector`.
See
`Transform2D.inverse()<class_Transform2D_method_inverse>`{.interpreted-text
role="ref"}.

For transforming by inverse of an affine transformation (e.g. with
scaling) `transform.affine_inverse() * vector` can be used instead. See
`Transform2D.affine_inverse()<class_Transform2D_method_affine_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_mul_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Vector2_operator_mul_Vector2>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector2** by the components of the
given **Vector2**.

    print(Vector2(10, 20) * Vector2(3, 4)) # Prints (30.0, 80.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Vector2_operator_mul_float>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector2** by the given
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies each component of the **Vector2** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_sum_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
+**(right: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_sum_Vector2>`{.interpreted-text role="ref"}

Adds each component of the **Vector2** by the components of the given
**Vector2**.

    print(Vector2(10, 20) + Vector2(3, 4)) # Prints (13.0, 24.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_dif_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
-**(right: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_dif_Vector2>`{.interpreted-text role="ref"}

Subtracts each component of the **Vector2** by the components of the
given **Vector2**.

    print(Vector2(10, 20) - Vector2(3, 4)) # Prints (7.0, 16.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_div_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
/**(right: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_div_Vector2>`{.interpreted-text role="ref"}

Divides each component of the **Vector2** by the components of the given
**Vector2**.

    print(Vector2(10, 20) / Vector2(2, 5)) # Prints (5.0, 4.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
/**(right: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_div_float>`{.interpreted-text role="ref"}

Divides each component of the **Vector2** by the given
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
/**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_div_int>`{.interpreted-text role="ref"}

Divides each component of the **Vector2** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_lt_Vector2}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_lt_Vector2>`{.interpreted-text role="ref"}

Compares two **Vector2** vectors by first checking if the X value of the
left vector is less than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_lte_Vector2}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_lte_Vector2>`{.interpreted-text role="ref"}

Compares two **Vector2** vectors by first checking if the X value of the
left vector is less than or equal to the X value of the `right` vector.
If the X values are exactly equal, then it repeats this check with the Y
values of the two vectors. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_eq_Vector2}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_eq_Vector2>`{.interpreted-text role="ref"}

Returns `true` if the vectors are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Vector2_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_gt_Vector2}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_gt_Vector2>`{.interpreted-text role="ref"}

Compares two **Vector2** vectors by first checking if the X value of the
left vector is greater than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_gte_Vector2}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_gte_Vector2>`{.interpreted-text role="ref"}

Compares two **Vector2** vectors by first checking if the X value of the
left vector is greater than or equal to the X value of the `right`
vector. If the X values are exactly equal, then it repeats this check
with the Y values of the two vectors. This operator is useful for
sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector2_operator_idx_int>`{.interpreted-text role="ref"}

Access vector components using their `index`. `v[0]` is equivalent to
`v.x`, and `v[1]` is equivalent to `v.y`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_unplus}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
unary+**() `🔗<class_Vector2_operator_unplus>`{.interpreted-text
role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector2_operator_unminus}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **operator
unary-**() `🔗<class_Vector2_operator_unminus>`{.interpreted-text
role="ref"}

Returns the negative value of the **Vector2**. This is the same as
writing `Vector2(-v.x, -v.y)`. This operation flips the direction of the
vector while keeping the same magnitude. With floats, the number zero
can be either positive or negative.
