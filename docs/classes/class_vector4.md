github_url
:   hide

# Vector4 {#class_Vector4}

A 4D vector using floating-point coordinates.

::: rst-class
classref-introduction-group
:::

## Description

A 4-element structure that can be used to represent 4D coordinates or
any other quadruplet of numeric values.

It uses floating-point coordinates. By default, these floating-point
values use 32-bit precision, unlike
`float<class_float>`{.interpreted-text role="ref"} which is always
64-bit. If double precision is needed, compile the engine with the
option `precision=double`.

See `Vector4i<class_Vector4i>`{.interpreted-text role="ref"} for its
integer counterpart.

\*\*Note:\*\* In a boolean context, a Vector4 will evaluate to `false`
if it\'s equal to `Vector4(0, 0, 0, 0)`. Otherwise, a Vector4 will
always evaluate to `true`.

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

:::: {#enum_Vector4_Axis}
::: rst-class
classref-enumeration
:::
::::

enum **Axis**: `🔗<enum_Vector4_Axis>`{.interpreted-text role="ref"}

:::: {#class_Vector4_constant_AXIS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4_Axis>`{.interpreted-text role="ref"} **AXIS_X** = `0`

Enumerated value for the X axis. Returned by
`max_axis_index()<class_Vector4_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector4_constant_AXIS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4_Axis>`{.interpreted-text role="ref"} **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by
`max_axis_index()<class_Vector4_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector4_constant_AXIS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4_Axis>`{.interpreted-text role="ref"} **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by
`max_axis_index()<class_Vector4_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector4_constant_AXIS_W}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4_Axis>`{.interpreted-text role="ref"} **AXIS_W** = `3`

Enumerated value for the W axis. Returned by
`max_axis_index()<class_Vector4_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4_method_min_axis_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Vector4_constant_ZERO}
::: rst-class
classref-constant
:::
::::

**ZERO** = `Vector4(0, 0, 0, 0)`
`🔗<class_Vector4_constant_ZERO>`{.interpreted-text role="ref"}

Zero vector, a vector with all components set to `0`.

:::: {#class_Vector4_constant_ONE}
::: rst-class
classref-constant
:::
::::

**ONE** = `Vector4(1, 1, 1, 1)`
`🔗<class_Vector4_constant_ONE>`{.interpreted-text role="ref"}

One vector, a vector with all components set to `1`.

:::: {#class_Vector4_constant_INF}
::: rst-class
classref-constant
:::
::::

**INF** = `Vector4(inf, inf, inf, inf)`
`🔗<class_Vector4_constant_INF>`{.interpreted-text role="ref"}

Infinity vector, a vector with all components set to
`@GDScript.INF<class_@GDScript_constant_INF>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Vector4_property_w}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **w** = `0.0`
`🔗<class_Vector4_property_w>`{.interpreted-text role="ref"}

The vector\'s W component. Also accessible by using the index position
`[3]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_property_x}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **x** = `0.0`
`🔗<class_Vector4_property_x>`{.interpreted-text role="ref"}

The vector\'s X component. Also accessible by using the index position
`[0]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_property_y}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **y** = `0.0`
`🔗<class_Vector4_property_y>`{.interpreted-text role="ref"}

The vector\'s Y component. Also accessible by using the index position
`[1]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_property_z}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **z** = `0.0`
`🔗<class_Vector4_property_z>`{.interpreted-text role="ref"}

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

:::: {#class_Vector4_constructor_Vector4}
::: rst-class
classref-constructor
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **Vector4**()
`🔗<class_Vector4_constructor_Vector4>`{.interpreted-text role="ref"}

Constructs a default-initialized **Vector4** with all components set to
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **Vector4**(from:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})

Constructs a **Vector4** as a copy of the given **Vector4**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **Vector4**(from:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})

Constructs a new **Vector4** from the given
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **Vector4**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"}, z:
`float<class_float>`{.interpreted-text role="ref"}, w:
`float<class_float>`{.interpreted-text role="ref"})

Returns a **Vector4** with the given components.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Vector4_method_abs}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **abs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_abs>`{.interpreted-text
role="ref"}

Returns a new vector with all components in absolute values (i.e.
positive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_ceil}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **ceil**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_ceil>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded up (towards positive
infinity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_clamp}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **clamp**(min:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, max:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_clamp>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between the components
of `min` and `max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_clampf}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **clampf**(min:
`float<class_float>`{.interpreted-text role="ref"}, max:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_clampf>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between `min` and
`max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_cubic_interpolate}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**cubic_interpolate**(b: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}, pre_a: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}, post_b: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}, weight: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4_method_cubic_interpolate>`{.interpreted-text
role="ref"}

Performs a cubic interpolation between this vector and `b` using `pre_a`
and `post_b` as handles, and returns the result at position `weight`.
`weight` is on the range of 0.0 to 1.0, representing the amount of
interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_cubic_interpolate_in_time}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**cubic_interpolate_in_time**(b:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, pre_a:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, post_b:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"}, b_t:
`float<class_float>`{.interpreted-text role="ref"}, pre_a_t:
`float<class_float>`{.interpreted-text role="ref"}, post_b_t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4_method_cubic_interpolate_in_time>`{.interpreted-text
role="ref"}

Performs a cubic interpolation between this vector and `b` using `pre_a`
and `post_b` as handles, and returns the result at position `weight`.
`weight` is on the range of 0.0 to 1.0, representing the amount of
interpolation.

It can perform smoother interpolation than
`cubic_interpolate()<class_Vector4_method_cubic_interpolate>`{.interpreted-text
role="ref"} by the time values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_direction_to}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**direction_to**(to: `Vector4<class_Vector4>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_direction_to>`{.interpreted-text
role="ref"}

Returns the normalized vector pointing from this vector to `to`. This is
equivalent to using `(b - a).normalized()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_distance_squared_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_squared_to**(to: `Vector4<class_Vector4>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4_method_distance_squared_to>`{.interpreted-text
role="ref"}

Returns the squared distance between this vector and `to`.

This method runs faster than
`distance_to()<class_Vector4_method_distance_to>`{.interpreted-text
role="ref"}, so prefer it if you need to compare vectors or need the
squared distance for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_distance_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **distance_to**(to:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_distance_to>`{.interpreted-text
role="ref"}

Returns the distance between this vector and `to`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_dot}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dot**(with:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_dot>`{.interpreted-text
role="ref"}

Returns the dot product of this vector and `with`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_floor}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **floor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_floor>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded down (towards negative
infinity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_inverse}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_inverse>`{.interpreted-text
role="ref"}

Returns the inverse of the vector. This is the same as
`Vector4(1.0 / v.x, 1.0 / v.y, 1.0 / v.z, 1.0 / v.w)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(to:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4_method_is_equal_approx>`{.interpreted-text role="ref"}

Returns `true` if this vector and `to` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this vector is finite, by calling
`@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_is_normalized}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_is_normalized>`{.interpreted-text
role="ref"}

Returns `true` if the vector is normalized, i.e. its length is
approximately equal to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_is_zero_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_zero_approx**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_is_zero_approx>`{.interpreted-text
role="ref"}

Returns `true` if this vector\'s values are approximately zero, by
running
`@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>`{.interpreted-text
role="ref"} on each component.

This method is faster than using
`is_equal_approx()<class_Vector4_method_is_equal_approx>`{.interpreted-text
role="ref"} with one value as a zero vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_length>`{.interpreted-text
role="ref"}

Returns the length (magnitude) of this vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_length_squared}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length_squared**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_length_squared>`{.interpreted-text
role="ref"}

Returns the squared length (squared magnitude) of this vector.

This method runs faster than
`length()<class_Vector4_method_length>`{.interpreted-text role="ref"},
so prefer it if you need to compare vectors or need the squared distance
for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_lerp}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **lerp**(to:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_lerp>`{.interpreted-text
role="ref"}

Returns the result of the linear interpolation between this vector and
`to` by amount `weight`. `weight` is on the range of `0.0` to `1.0`,
representing the amount of interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_max}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **max**(with:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_max>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector4(maxf(x, with.x), maxf(y, with.y), maxf(z, with.z), maxf(w, with.w))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_max_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_max_axis_index>`{.interpreted-text
role="ref"}

Returns the axis of the vector\'s highest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_X<class_Vector4_constant_AXIS_X>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_maxf}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **maxf**(with:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_maxf>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector4(maxf(x, with), maxf(y, with), maxf(z, with), maxf(w, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_min}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **min**(with:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_min>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector4(minf(x, with.x), minf(y, with.y), minf(z, with.z), minf(w, with.w))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_min_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **min_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_min_axis_index>`{.interpreted-text
role="ref"}

Returns the axis of the vector\'s lowest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_W<class_Vector4_constant_AXIS_W>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_minf}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **minf**(with:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_minf>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector4(minf(x, with), minf(y, with), minf(z, with), minf(w, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_normalized}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_normalized>`{.interpreted-text
role="ref"}

Returns the result of scaling the vector to unit length. Equivalent to
`v / v.length()`. Returns `(0, 0, 0, 0)` if `v.length() == 0`. See also
`is_normalized()<class_Vector4_method_is_normalized>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This function may return incorrect values if the input
vector length is near zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_posmod}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **posmod**(mod:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_posmod>`{.interpreted-text
role="ref"}

Returns a vector composed of the
`@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} of this vector\'s components and `mod`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_posmodv}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **posmodv**(modv:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_posmodv>`{.interpreted-text
role="ref"}

Returns a vector composed of the
`@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} of this vector\'s components and `modv`\'s components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_round}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **round**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_round>`{.interpreted-text
role="ref"}

Returns a new vector with all components rounded to the nearest integer,
with halfway cases rounded away from zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_sign}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **sign**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_sign>`{.interpreted-text
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

:::: {#class_Vector4_method_snapped}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **snapped**(step:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_snapped>`{.interpreted-text
role="ref"}

Returns a new vector with each component snapped to the nearest multiple
of the corresponding component in `step`. This can also be used to round
the components to an arbitrary number of decimals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_method_snappedf}
::: rst-class
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**snappedf**(step: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4_method_snappedf>`{.interpreted-text
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

:::: {#class_Vector4_operator_neq_Vector4}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_neq_Vector4>`{.interpreted-text role="ref"}

Returns `true` if the vectors are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Vector4_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_mul_Projection}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `Projection<class_Projection>`{.interpreted-text
role="ref"})
`🔗<class_Vector4_operator_mul_Projection>`{.interpreted-text
role="ref"}

Transforms (multiplies) the **Vector4** by the transpose of the given
`Projection<class_Projection>`{.interpreted-text role="ref"} matrix.

For transforming by inverse of a projection
`projection.inverse() * vector` can be used instead. See
`Projection.inverse()<class_Projection_method_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_mul_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}) `🔗<class_Vector4_operator_mul_Vector4>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector4** by the components of the
given **Vector4**.

    print(Vector4(10, 20, 30, 40) * Vector4(3, 4, 5, 6)) # Prints (30.0, 80.0, 150.0, 240.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Vector4_operator_mul_float>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector4** by the given
`float<class_float>`{.interpreted-text role="ref"}.

    print(Vector4(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies each component of the **Vector4** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_sum_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
+**(right: `Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_sum_Vector4>`{.interpreted-text role="ref"}

Adds each component of the **Vector4** by the components of the given
**Vector4**.

    print(Vector4(10, 20, 30, 40) + Vector4(3, 4, 5, 6)) # Prints (13.0, 24.0, 35.0, 46.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_dif_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
-**(right: `Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_dif_Vector4>`{.interpreted-text role="ref"}

Subtracts each component of the **Vector4** by the components of the
given **Vector4**.

    print(Vector4(10, 20, 30, 40) - Vector4(3, 4, 5, 6)) # Prints (7.0, 16.0, 25.0, 34.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_div_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
/**(right: `Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_div_Vector4>`{.interpreted-text role="ref"}

Divides each component of the **Vector4** by the components of the given
**Vector4**.

    print(Vector4(10, 20, 30, 40) / Vector4(2, 5, 3, 4)) # Prints (5.0, 4.0, 10.0, 10.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
/**(right: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_div_float>`{.interpreted-text role="ref"}

Divides each component of the **Vector4** by the given
`float<class_float>`{.interpreted-text role="ref"}.

    print(Vector4(10, 20, 30, 40) / 2) # Prints (5.0, 10.0, 15.0, 20.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
/**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_div_int>`{.interpreted-text role="ref"}

Divides each component of the **Vector4** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_lt_Vector4}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_lt_Vector4>`{.interpreted-text role="ref"}

Compares two **Vector4** vectors by first checking if the X value of the
left vector is less than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors, Z values of the two vectors, and then with the W
values. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_lte_Vector4}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_lte_Vector4>`{.interpreted-text role="ref"}

Compares two **Vector4** vectors by first checking if the X value of the
left vector is less than or equal to the X value of the `right` vector.
If the X values are exactly equal, then it repeats this check with the Y
values of the two vectors, Z values of the two vectors, and then with
the W values. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_eq_Vector4}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_eq_Vector4>`{.interpreted-text role="ref"}

Returns `true` if the vectors are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Vector4_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_gt_Vector4}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_gt_Vector4>`{.interpreted-text role="ref"}

Compares two **Vector4** vectors by first checking if the X value of the
left vector is greater than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors, Z values of the two vectors, and then with the W
values. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_gte_Vector4}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_gte_Vector4>`{.interpreted-text role="ref"}

Compares two **Vector4** vectors by first checking if the X value of the
left vector is greater than or equal to the X value of the `right`
vector. If the X values are exactly equal, then it repeats this check
with the Y values of the two vectors, Z values of the two vectors, and
then with the W values. This operator is useful for sorting vectors.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4_operator_idx_int>`{.interpreted-text role="ref"}

Access vector components using their `index`. `v[0]` is equivalent to
`v.x`, `v[1]` is equivalent to `v.y`, `v[2]` is equivalent to `v.z`, and
`v[3]` is equivalent to `v.w`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_unplus}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
unary+**() `🔗<class_Vector4_operator_unplus>`{.interpreted-text
role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4_operator_unminus}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
unary-**() `🔗<class_Vector4_operator_unminus>`{.interpreted-text
role="ref"}

Returns the negative value of the **Vector4**. This is the same as
writing `Vector4(-v.x, -v.y, -v.z, -v.w)`. This operation flips the
direction of the vector while keeping the same magnitude. With floats,
the number zero can be either positive or negative.
