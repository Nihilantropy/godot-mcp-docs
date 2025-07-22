github_url
:   hide

# float {#class_float}

A built-in type for floating-point numbers.

::: rst-class
classref-introduction-group
:::

## Description

The **float** built-in type is a 64-bit double-precision floating-point
number, equivalent to `double` in C++. This type has 14 reliable decimal
digits of precision. The maximum value of **float** is approximately
`1.79769e308`, and the minimum is approximately `-1.79769e308`.

Many methods and properties in the engine use 32-bit single-precision
floating-point numbers instead, equivalent to `float` in C++, which have
6 reliable decimal digits of precision. For data structures such as
`Vector2<class_Vector2>`{.interpreted-text role="ref"} and
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, Godot uses
32-bit floating-point numbers by default, but it can be changed to use
64-bit doubles if Godot is compiled with the `precision=double` option.

Math done using the **float** type is not guaranteed to be exact and
will often result in small errors. You should usually use the
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} and
`@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>`{.interpreted-text
role="ref"} methods instead of `==` to compare **float** values for
equality.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Wikipedia: Double-precision floating-point
  format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Wikipedia: Single-precision floating-point
  format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)

::: rst-class
classref-reftable-group
:::

## Constructors

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

## Constructor Descriptions

:::: {#class_float_constructor_float}
::: rst-class
classref-constructor
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **float**()
`🔗<class_float_constructor_float>`{.interpreted-text role="ref"}

Constructs a default-initialized **float** set to `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`float<class_float>`{.interpreted-text role="ref"} **float**(from:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **float** as a copy of the given **float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`float<class_float>`{.interpreted-text role="ref"} **float**(from:
`String<class_String>`{.interpreted-text role="ref"})

Converts a `String<class_String>`{.interpreted-text role="ref"} to a
**float**, following the same rules as
`String.to_float()<class_String_method_to_float>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`float<class_float>`{.interpreted-text role="ref"} **float**(from:
`bool<class_bool>`{.interpreted-text role="ref"})

Cast a `bool<class_bool>`{.interpreted-text role="ref"} value to a
floating-point value, `float(true)` will be equal to 1.0 and
`float(false)` will be equal to 0.0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`float<class_float>`{.interpreted-text role="ref"} **float**(from:
`int<class_int>`{.interpreted-text role="ref"})

Cast an `int<class_int>`{.interpreted-text role="ref"} value to a
floating-point value, `float(1)` will be equal to `1.0`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_float_operator_neq_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_neq_float>`{.interpreted-text role="ref"}

Returns `true` if two floats are different from each other.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_neq_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_neq_int>`{.interpreted-text role="ref"}

Returns `true` if the integer has different value than the float.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Color}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator**\*(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_float_operator_mul_Color>`{.interpreted-text role="ref"}

Multiplies each component of the `Color<class_Color>`{.interpreted-text
role="ref"}, including the alpha, by the given **float**.

    print(1.5 * Color(0.5, 0.5, 0.5)) # Prints (0.75, 0.75, 0.75, 1.5)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Quaternion}
::: rst-class
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**operator**\*(right: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Quaternion>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} by the
given **float**. This operation is not meaningful on its own, but it can
be used as a part of a larger expression.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Vector2>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector2<class_Vector2>`{.interpreted-text role="ref"} by the given
**float**.

    print(2.5 * Vector2(1, 3)) # Prints (2.5, 7.5)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Vector2i}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Vector2i>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} by the given
**float**. Returns a `Vector2<class_Vector2>`{.interpreted-text
role="ref"}.

    print(0.9 * Vector2i(10, 15)) # Prints (9.0, 13.5)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Vector3>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector3<class_Vector3>`{.interpreted-text role="ref"} by the given
**float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Vector3i}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Vector3i>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"} by the given
**float**. Returns a `Vector3<class_Vector3>`{.interpreted-text
role="ref"}.

    print(0.9 * Vector3i(10, 15, 20)) # Prints (9.0, 13.5, 18.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Vector4>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector4<class_Vector4>`{.interpreted-text role="ref"} by the given
**float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_mul_Vector4i>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} by the given
**float**. Returns a `Vector4<class_Vector4>`{.interpreted-text
role="ref"}.

    print(0.9 * Vector4i(10, 15, 20, -10)) # Prints (9.0, 13.5, 18.0, -9.0)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator**\*(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_mul_float>`{.interpreted-text role="ref"}

Multiplies two **float**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator**\*(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies a **float** and an `int<class_int>`{.interpreted-text
role="ref"}. The result is a **float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_pow_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**operator**\*\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_float_operator_pow_float>`{.interpreted-text
role="ref"}

Raises a **float** to a power of a **float**.

    print(39.0625**0.25) # 2.5

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_pow_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**operator**\*\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_pow_int>`{.interpreted-text role="ref"}

Raises a **float** to a power of an `int<class_int>`{.interpreted-text
role="ref"}. The result is a **float**.

    print(0.9**3) # 0.729

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_sum_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator +**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_sum_float>`{.interpreted-text role="ref"}

Adds two floats.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_sum_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator +**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_sum_int>`{.interpreted-text role="ref"}

Adds a **float** and an `int<class_int>`{.interpreted-text role="ref"}.
The result is a **float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_dif_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator -**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_dif_float>`{.interpreted-text role="ref"}

Subtracts a float from a float.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_dif_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator -**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_dif_int>`{.interpreted-text role="ref"}

Subtracts an `int<class_int>`{.interpreted-text role="ref"} from a
**float**. The result is a **float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_div_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator /**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_div_float>`{.interpreted-text role="ref"}

Divides two floats.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_div_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator /**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_div_int>`{.interpreted-text role="ref"}

Divides a **float** by an `int<class_int>`{.interpreted-text
role="ref"}. The result is a **float**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_lt_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_lt_float>`{.interpreted-text role="ref"}

Returns `true` if the left float is less than the right one.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_lt_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_lt_int>`{.interpreted-text role="ref"}

Returns `true` if this **float** is less than the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_lte_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_lte_float>`{.interpreted-text role="ref"}

Returns `true` if the left float is less than or equal to the right one.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_lte_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_lte_int>`{.interpreted-text role="ref"}

Returns `true` if this **float** is less than or equal to the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_eq_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_eq_float>`{.interpreted-text role="ref"}

Returns `true` if both floats are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} or
`@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>`{.interpreted-text
role="ref"} instead, which are more reliable.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_eq_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_eq_int>`{.interpreted-text role="ref"}

Returns `true` if the **float** and the given
`int<class_int>`{.interpreted-text role="ref"} are equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_gt_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_gt_float>`{.interpreted-text role="ref"}

Returns `true` if the left float is greater than the right one.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_gt_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_gt_int>`{.interpreted-text role="ref"}

Returns `true` if this **float** is greater than the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_gte_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_float_operator_gte_float>`{.interpreted-text role="ref"}

Returns `true` if the left float is greater than or equal to the right
one.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this operator may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_gte_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_float_operator_gte_int>`{.interpreted-text role="ref"}

Returns `true` if this **float** is greater than or equal to the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_unplus}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator unary+**()
`🔗<class_float_operator_unplus>`{.interpreted-text role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_float_operator_unminus}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator unary-**()
`🔗<class_float_operator_unminus>`{.interpreted-text role="ref"}

Returns the negative value of the **float**. If positive, turns the
number negative. If negative, turns the number positive. With floats,
the number zero can be either positive or negative.
