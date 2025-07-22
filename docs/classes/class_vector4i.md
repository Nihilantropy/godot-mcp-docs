github_url
:   hide

# Vector4i {#class_Vector4i}

A 4D vector using integer coordinates.

::: rst-class
classref-introduction-group
:::

## Description

A 4-element structure that can be used to represent 4D grid coordinates
or any other quadruplet of integers.

It uses integer coordinates and is therefore preferable to
`Vector4<class_Vector4>`{.interpreted-text role="ref"} when exact
precision is required. Note that the values are limited to 32 bits, and
unlike `Vector4<class_Vector4>`{.interpreted-text role="ref"} this
cannot be configured with an engine build option. Use
`int<class_int>`{.interpreted-text role="ref"} or
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
if 64-bit values are needed.

\*\*Note:\*\* In a boolean context, a Vector4i will evaluate to `false`
if it\'s equal to `Vector4i(0, 0, 0, 0)`. Otherwise, a Vector4i will
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

:::: {#enum_Vector4i_Axis}
::: rst-class
classref-enumeration
:::
::::

enum **Axis**: `🔗<enum_Vector4i_Axis>`{.interpreted-text role="ref"}

:::: {#class_Vector4i_constant_AXIS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4i_Axis>`{.interpreted-text role="ref"} **AXIS_X** =
`0`

Enumerated value for the X axis. Returned by
`max_axis_index()<class_Vector4i_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4i_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector4i_constant_AXIS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4i_Axis>`{.interpreted-text role="ref"} **AXIS_Y** =
`1`

Enumerated value for the Y axis. Returned by
`max_axis_index()<class_Vector4i_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4i_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector4i_constant_AXIS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4i_Axis>`{.interpreted-text role="ref"} **AXIS_Z** =
`2`

Enumerated value for the Z axis. Returned by
`max_axis_index()<class_Vector4i_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4i_method_min_axis_index>`{.interpreted-text
role="ref"}.

:::: {#class_Vector4i_constant_AXIS_W}
::: rst-class
classref-enumeration-constant
:::
::::

`Axis<enum_Vector4i_Axis>`{.interpreted-text role="ref"} **AXIS_W** =
`3`

Enumerated value for the W axis. Returned by
`max_axis_index()<class_Vector4i_method_max_axis_index>`{.interpreted-text
role="ref"} and
`min_axis_index()<class_Vector4i_method_min_axis_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Vector4i_constant_ZERO}
::: rst-class
classref-constant
:::
::::

**ZERO** = `Vector4i(0, 0, 0, 0)`
`🔗<class_Vector4i_constant_ZERO>`{.interpreted-text role="ref"}

Zero vector, a vector with all components set to `0`.

:::: {#class_Vector4i_constant_ONE}
::: rst-class
classref-constant
:::
::::

**ONE** = `Vector4i(1, 1, 1, 1)`
`🔗<class_Vector4i_constant_ONE>`{.interpreted-text role="ref"}

One vector, a vector with all components set to `1`.

:::: {#class_Vector4i_constant_MIN}
::: rst-class
classref-constant
:::
::::

**MIN** = `Vector4i(-2147483648, -2147483648, -2147483648, -2147483648)`
`🔗<class_Vector4i_constant_MIN>`{.interpreted-text role="ref"}

Min vector, a vector with all components equal to `INT32_MIN`. Can be
used as a negative integer equivalent of
`Vector4.INF<class_Vector4_constant_INF>`{.interpreted-text role="ref"}.

:::: {#class_Vector4i_constant_MAX}
::: rst-class
classref-constant
:::
::::

**MAX** = `Vector4i(2147483647, 2147483647, 2147483647, 2147483647)`
`🔗<class_Vector4i_constant_MAX>`{.interpreted-text role="ref"}

Max vector, a vector with all components equal to `INT32_MAX`. Can be
used as an integer equivalent of
`Vector4.INF<class_Vector4_constant_INF>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Vector4i_property_w}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **w** = `0`
`🔗<class_Vector4i_property_w>`{.interpreted-text role="ref"}

The vector\'s W component. Also accessible by using the index position
`[3]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_property_x}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **x** = `0`
`🔗<class_Vector4i_property_x>`{.interpreted-text role="ref"}

The vector\'s X component. Also accessible by using the index position
`[0]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_property_y}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **y** = `0`
`🔗<class_Vector4i_property_y>`{.interpreted-text role="ref"}

The vector\'s Y component. Also accessible by using the index position
`[1]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_property_z}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **z** = `0`
`🔗<class_Vector4i_property_z>`{.interpreted-text role="ref"}

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

:::: {#class_Vector4i_constructor_Vector4i}
::: rst-class
classref-constructor
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **Vector4i**()
`🔗<class_Vector4i_constructor_Vector4i>`{.interpreted-text role="ref"}

Constructs a default-initialized **Vector4i** with all components set to
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**Vector4i**(from: `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"})

Constructs a **Vector4i** as a copy of the given **Vector4i**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**Vector4i**(from: `Vector4<class_Vector4>`{.interpreted-text
role="ref"})

Constructs a new **Vector4i** from the given
`Vector4<class_Vector4>`{.interpreted-text role="ref"} by truncating
components\' fractional parts (rounding towards zero). For a different
behavior consider passing the result of
`Vector4.ceil()<class_Vector4_method_ceil>`{.interpreted-text
role="ref"},
`Vector4.floor()<class_Vector4_method_floor>`{.interpreted-text
role="ref"} or
`Vector4.round()<class_Vector4_method_round>`{.interpreted-text
role="ref"} to this constructor instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **Vector4i**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"}, z:
`int<class_int>`{.interpreted-text role="ref"}, w:
`int<class_int>`{.interpreted-text role="ref"})

Returns a **Vector4i** with the given components.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Vector4i_method_abs}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **abs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_abs>`{.interpreted-text
role="ref"}

Returns a new vector with all components in absolute values (i.e.
positive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_clamp}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **clamp**(min:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}, max:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_clamp>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between the components
of `min` and `max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_clampi}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **clampi**(min:
`int<class_int>`{.interpreted-text role="ref"}, max:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_clampi>`{.interpreted-text
role="ref"}

Returns a new vector with all components clamped between `min` and
`max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_distance_squared_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**distance_squared_to**(to: `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4i_method_distance_squared_to>`{.interpreted-text
role="ref"}

Returns the squared distance between this vector and `to`.

This method runs faster than
`distance_to()<class_Vector4i_method_distance_to>`{.interpreted-text
role="ref"}, so prefer it if you need to compare vectors or need the
squared distance for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_distance_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **distance_to**(to:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_distance_to>`{.interpreted-text
role="ref"}

Returns the distance between this vector and `to`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_length>`{.interpreted-text
role="ref"}

Returns the length (magnitude) of this vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_length_squared}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **length_squared**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4i_method_length_squared>`{.interpreted-text role="ref"}

Returns the squared length (squared magnitude) of this vector.

This method runs faster than
`length()<class_Vector4i_method_length>`{.interpreted-text role="ref"},
so prefer it if you need to compare vectors or need the squared distance
for some formula.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_max}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **max**(with:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_max>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector4i(maxi(x, with.x), maxi(y, with.y), maxi(z, with.z), maxi(w, with.w))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_max_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4i_method_max_axis_index>`{.interpreted-text role="ref"}

Returns the axis of the vector\'s highest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_X<class_Vector4i_constant_AXIS_X>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_maxi}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **maxi**(with:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_maxi>`{.interpreted-text
role="ref"}

Returns the component-wise maximum of this and `with`, equivalent to
`Vector4i(maxi(x, with), maxi(y, with), maxi(z, with), maxi(w, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_min}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **min**(with:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_min>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector4i(mini(x, with.x), mini(y, with.y), mini(z, with.z), mini(w, with.w))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_min_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **min_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Vector4i_method_min_axis_index>`{.interpreted-text role="ref"}

Returns the axis of the vector\'s lowest value. See `AXIS_*` constants.
If all components are equal, this method returns
`AXIS_W<class_Vector4i_constant_AXIS_W>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_mini}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **mini**(with:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_mini>`{.interpreted-text
role="ref"}

Returns the component-wise minimum of this and `with`, equivalent to
`Vector4i(mini(x, with), mini(y, with), mini(z, with), mini(w, with))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_sign}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **sign**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_sign>`{.interpreted-text
role="ref"}

Returns a new vector with each component set to `1` if it\'s positive,
`-1` if it\'s negative, and `0` if it\'s zero. The result is identical
to calling
`@GlobalScope.sign()<class_@GlobalScope_method_sign>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_snapped}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**snapped**(step: `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_snapped>`{.interpreted-text
role="ref"}

Returns a new vector with each component snapped to the closest multiple
of the corresponding component in `step`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_method_snappedi}
::: rst-class
classref-method
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**snappedi**(step: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Vector4i_method_snappedi>`{.interpreted-text
role="ref"}

Returns a new vector with each component snapped to the closest multiple
of `step`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Vector4i_operator_neq_Vector4i}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_neq_Vector4i>`{.interpreted-text role="ref"}

Returns `true` if the vectors are not equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_mod_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
%**(right: `Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_mod_Vector4i>`{.interpreted-text role="ref"}

Gets the remainder of each component of the **Vector4i** with the
components of the given **Vector4i**. This operation uses truncated
division, which is often not desired as it does not work well with
negative numbers. Consider using
`@GlobalScope.posmod()<class_@GlobalScope_method_posmod>`{.interpreted-text
role="ref"} instead if you want to handle negative numbers.

    print(Vector4i(10, -20, 30, -40) % Vector4i(7, 8, 9, 10)) # Prints (3, -4, 3, 0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_mod_int}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
%**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_mod_int>`{.interpreted-text role="ref"}

Gets the remainder of each component of the **Vector4i** with the given
`int<class_int>`{.interpreted-text role="ref"}. This operation uses
truncated division, which is often not desired as it does not work well
with negative numbers. Consider using
`@GlobalScope.posmod()<class_@GlobalScope_method_posmod>`{.interpreted-text
role="ref"} instead if you want to handle negative numbers.

    print(Vector4i(10, -20, 30, -40) % 7) # Prints (3, -6, 2, -5)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_mul_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"})
`🔗<class_Vector4i_operator_mul_Vector4i>`{.interpreted-text role="ref"}

Multiplies each component of the **Vector4i** by the components of the
given **Vector4i**.

    print(Vector4i(10, 20, 30, 40) * Vector4i(3, 4, 5, 6)) # Prints (30, 80, 150, 240)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Vector4i_operator_mul_float>`{.interpreted-text
role="ref"}

Multiplies each component of the **Vector4i** by the given
`float<class_float>`{.interpreted-text role="ref"}.

Returns a Vector4 value due to floating-point operations.

    print(Vector4i(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies each component of the **Vector4i** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_sum_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
+**(right: `Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_sum_Vector4i>`{.interpreted-text role="ref"}

Adds each component of the **Vector4i** by the components of the given
**Vector4i**.

    print(Vector4i(10, 20, 30, 40) + Vector4i(3, 4, 5, 6)) # Prints (13, 24, 35, 46)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_dif_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
-**(right: `Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_dif_Vector4i>`{.interpreted-text role="ref"}

Subtracts each component of the **Vector4i** by the components of the
given **Vector4i**.

    print(Vector4i(10, 20, 30, 40) - Vector4i(3, 4, 5, 6)) # Prints (7, 16, 25, 34)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_div_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
/**(right: `Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_div_Vector4i>`{.interpreted-text role="ref"}

Divides each component of the **Vector4i** by the components of the
given **Vector4i**.

    print(Vector4i(10, 20, 30, 40) / Vector4i(2, 5, 3, 4)) # Prints (5, 4, 10, 10)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
/**(right: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_div_float>`{.interpreted-text role="ref"}

Divides each component of the **Vector4i** by the given
`float<class_float>`{.interpreted-text role="ref"}.

Returns a Vector4 value due to floating-point operations.

    print(Vector4i(10, 20, 30, 40) / 2) # Prints (5.0, 10.0, 15.0, 20.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
/**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_div_int>`{.interpreted-text role="ref"}

Divides each component of the **Vector4i** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_lt_Vector4i}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_lt_Vector4i>`{.interpreted-text role="ref"}

Compares two **Vector4i** vectors by first checking if the X value of
the left vector is less than the X value of the `right` vector. If the X
values are exactly equal, then it repeats this check with the Y values
of the two vectors, Z values of the two vectors, and then with the W
values. This operator is useful for sorting vectors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_lte_Vector4i}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_lte_Vector4i>`{.interpreted-text role="ref"}

Compares two **Vector4i** vectors by first checking if the X value of
the left vector is less than or equal to the X value of the `right`
vector. If the X values are exactly equal, then it repeats this check
with the Y values of the two vectors, Z values of the two vectors, and
then with the W values. This operator is useful for sorting vectors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_eq_Vector4i}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_eq_Vector4i>`{.interpreted-text role="ref"}

Returns `true` if the vectors are exactly equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_gt_Vector4i}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_gt_Vector4i>`{.interpreted-text role="ref"}

Compares two **Vector4i** vectors by first checking if the X value of
the left vector is greater than the X value of the `right` vector. If
the X values are exactly equal, then it repeats this check with the Y
values of the two vectors, Z values of the two vectors, and then with
the W values. This operator is useful for sorting vectors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_gte_Vector4i}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_gte_Vector4i>`{.interpreted-text role="ref"}

Compares two **Vector4i** vectors by first checking if the X value of
the left vector is greater than or equal to the X value of the `right`
vector. If the X values are exactly equal, then it repeats this check
with the Y values of the two vectors, Z values of the two vectors, and
then with the W values. This operator is useful for sorting vectors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \[\]**(index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Vector4i_operator_idx_int>`{.interpreted-text role="ref"}

Access vector components using their `index`. `v[0]` is equivalent to
`v.x`, `v[1]` is equivalent to `v.y`, `v[2]` is equivalent to `v.z`, and
`v[3]` is equivalent to `v.w`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_unplus}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
unary+**() `🔗<class_Vector4i_operator_unplus>`{.interpreted-text
role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Vector4i_operator_unminus}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} **operator
unary-**() `🔗<class_Vector4i_operator_unminus>`{.interpreted-text
role="ref"}

Returns the negative value of the **Vector4i**. This is the same as
writing `Vector4i(-v.x, -v.y, -v.z, -v.w)`. This operation flips the
direction of the vector while keeping the same magnitude.
