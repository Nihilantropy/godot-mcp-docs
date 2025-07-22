github_url
:   hide

# int {#class_int}

A built-in type for integers.

::: rst-class
classref-introduction-group
:::

## Description

Signed 64-bit integer type. This means that it can take values from
`-2^63` to `2^63 - 1`, i.e. from `-9223372036854775808` to
`9223372036854775807`. When it exceeds these bounds, it will wrap
around.

\*\*int\*\*s can be automatically converted to
`float<class_float>`{.interpreted-text role="ref"}s when necessary, for
example when passing them as arguments in functions. The
`float<class_float>`{.interpreted-text role="ref"} will be as close to
the original integer as possible.

Likewise, `float<class_float>`{.interpreted-text role="ref"}s can be
automatically converted into **int**s. This will truncate the
`float<class_float>`{.interpreted-text role="ref"}, discarding anything
after the floating-point.

\*\*Note:\*\* In a boolean context, an **int** will evaluate to `false`
if it equals `0`, and to `true` otherwise.

::::: tabs
::: code-tab
gdscript

var x: int = 1 \# x is 1 x = 4.2 \# x is 4, because 4.2 gets truncated
var max_int = 9223372036854775807 \# Biggest value an int can store
max_int += 1 \# max_int is -9223372036854775808, because it wrapped
around
:::

::: code-tab
csharp

int x = 1; // x is 1 x = (int)4.2; // x is 4, because 4.2 gets truncated
// We use long below, because GDScript\'s int is 64-bit while C#\'s int
is 32-bit. long maxLong = 9223372036854775807; // Biggest value a long
can store maxLong++; // maxLong is now -9223372036854775808, because it
wrapped around.

// Alternatively with C#\'s 32-bit int type, which has a smaller maximum
value. int maxInt = 2147483647; // Biggest value an int can store
maxInt++; // maxInt is now -2147483648, because it wrapped around
:::
:::::

You can use the `0b` literal for binary representation, the `0x` literal
for hexadecimal representation, and the `_` symbol to separate long
numbers and improve readability.

::::: tabs
::: code-tab
gdscript

var x = 0b1001 \# x is 9 var y = 0xF5 \# y is 245 var z = 10_000_000 \#
z is 10000000
:::

::: code-tab
csharp

int x = 0b1001; // x is 9 int y = 0xF5; // y is 245 int z = 10_000_000;
// z is 10000000
:::
:::::

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

:::: {#class_int_constructor_int}
::: rst-class
classref-constructor
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **int**()
`🔗<class_int_constructor_int>`{.interpreted-text role="ref"}

Constructs an **int** set to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`int<class_int>`{.interpreted-text role="ref"} **int**(from:
`int<class_int>`{.interpreted-text role="ref"})

Constructs an **int** as a copy of the given **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`int<class_int>`{.interpreted-text role="ref"} **int**(from:
`String<class_String>`{.interpreted-text role="ref"})

Constructs a new **int** from a `String<class_String>`{.interpreted-text
role="ref"}, following the same rules as
`String.to_int()<class_String_method_to_int>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`int<class_int>`{.interpreted-text role="ref"} **int**(from:
`bool<class_bool>`{.interpreted-text role="ref"})

Constructs a new **int** from a `bool<class_bool>`{.interpreted-text
role="ref"}. `true` is converted to `1` and `false` is converted to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`int<class_int>`{.interpreted-text role="ref"} **int**(from:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a new **int** from a `float<class_float>`{.interpreted-text
role="ref"}. This will truncate the
`float<class_float>`{.interpreted-text role="ref"}, discarding anything
after the floating point.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_int_operator_neq_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_neq_float>`{.interpreted-text role="ref"}

Returns `true` if the **int** is not equivalent to the
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_neq_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_neq_int>`{.interpreted-text role="ref"}

Returns `true` if the **int**s are not equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mod_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator %**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_mod_int>`{.interpreted-text role="ref"}

Returns the remainder after dividing two **int**s. Uses truncated
division, which returns a negative number if the dividend is negative.
If this is not desired, consider using
`@GlobalScope.posmod()<class_@GlobalScope_method_posmod>`{.interpreted-text
role="ref"}.

    print(6 % 2) # Prints 0
    print(11 % 4) # Prints 3
    print(-5 % 3) # Prints -2

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_bwand_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator &**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_bwand_int>`{.interpreted-text role="ref"}

Performs the bitwise `AND` operation.

    print(0b1100 & 0b1010) # Prints 8 (binary 1000)

This is useful for retrieving binary flags from a variable.

    var flags = 0b101
    # Check if the first or second bit are enabled.
    if flags & 0b011:
        do_stuff() # This line will run.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Color}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator**\*(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_int_operator_mul_Color>`{.interpreted-text role="ref"}

Multiplies each component of the `Color<class_Color>`{.interpreted-text
role="ref"} by the **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Quaternion}
::: rst-class
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**operator**\*(right: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Quaternion>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} by the
**int**. This operation is not meaningful on its own, but it can be used
as a part of a larger expression.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Vector2}
::: rst-class
classref-operator
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Vector2>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector2<class_Vector2>`{.interpreted-text role="ref"} by the **int**.

    print(2 * Vector2(1, 4)) # Prints (2, 8)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Vector2i}
::: rst-class
classref-operator
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Vector2i>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} by the **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Vector3}
::: rst-class
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Vector3>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector3<class_Vector3>`{.interpreted-text role="ref"} by the **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Vector3i}
::: rst-class
classref-operator
:::
::::

`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Vector3i>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"} by the **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Vector4>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector4<class_Vector4>`{.interpreted-text role="ref"} by the **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_Vector4i}
::: rst-class
classref-operator
:::
::::

`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_mul_Vector4i>`{.interpreted-text
role="ref"}

Multiplies each component of the
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"} by the **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator**\*(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_mul_float>`{.interpreted-text role="ref"}

Multiplies the `float<class_float>`{.interpreted-text role="ref"} by the
**int**. The result is a `float<class_float>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator**\*(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies the two **int**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_pow_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**operator**\*\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_int_operator_pow_float>`{.interpreted-text
role="ref"}

Raises an **int** to a power of a `float<class_float>`{.interpreted-text
role="ref"}. The result is a `float<class_float>`{.interpreted-text
role="ref"}.

    print(2 ** 0.5) # Prints 1.4142135623731

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_pow_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator**\*\*(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_pow_int>`{.interpreted-text role="ref"}

Raises the left **int** to a power of the right **int**.

    print(3 ** 4) # Prints 81

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_sum_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator +**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_sum_float>`{.interpreted-text role="ref"}

Adds the **int** and the `float<class_float>`{.interpreted-text
role="ref"}. The result is a `float<class_float>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_sum_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator +**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_sum_int>`{.interpreted-text role="ref"}

Adds the two **int**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_dif_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator -**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_dif_float>`{.interpreted-text role="ref"}

Subtracts the `float<class_float>`{.interpreted-text role="ref"} from
the **int**. The result is a `float<class_float>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_dif_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator -**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_dif_int>`{.interpreted-text role="ref"}

Subtracts the two **int**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_div_float}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator /**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_div_float>`{.interpreted-text role="ref"}

Divides the **int** by the `float<class_float>`{.interpreted-text
role="ref"}. The result is a `float<class_float>`{.interpreted-text
role="ref"}.

    print(10 / 3.0) # Prints 3.33333333333333

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_div_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator /**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_div_int>`{.interpreted-text role="ref"}

Divides the two **int**s. The result is an **int**. This will truncate
the `float<class_float>`{.interpreted-text role="ref"}, discarding
anything after the floating point.

    print(6 / 2) # Prints 3
    print(5 / 3) # Prints 1

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_lt_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_lt_float>`{.interpreted-text role="ref"}

Returns `true` if the **int** is less than the
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_lt_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_lt_int>`{.interpreted-text role="ref"}

Returns `true` if the left **int** is less than the right **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_bwsl_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \<\<**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_bwsl_int>`{.interpreted-text role="ref"}

Performs the bitwise shift left operation. Effectively the same as
multiplying by a power of 2.

    print(0b1010 << 1) # Prints 20 (binary 10100)
    print(0b1010 << 3) # Prints 80 (binary 1010000)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_lte_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_lte_float>`{.interpreted-text role="ref"}

Returns `true` if the **int** is less than or equal to the
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_lte_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_lte_int>`{.interpreted-text role="ref"}

Returns `true` if the left **int** is less than or equal to the right
**int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_eq_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_eq_float>`{.interpreted-text role="ref"}

Returns `true` if the **int** is equal to the
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_eq_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_eq_int>`{.interpreted-text role="ref"}

Returns `true` if the two **int**s are equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_gt_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_gt_float>`{.interpreted-text role="ref"}

Returns `true` if the **int** is greater than the
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_gt_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_gt_int>`{.interpreted-text role="ref"}

Returns `true` if the left **int** is greater than the right **int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_gte_float}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_int_operator_gte_float>`{.interpreted-text role="ref"}

Returns `true` if the **int** is greater than or equal to the
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_gte_int}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_gte_int>`{.interpreted-text role="ref"}

Returns `true` if the left **int** is greater than or equal to the right
**int**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_bwsr_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \>\>**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_bwsr_int>`{.interpreted-text role="ref"}

Performs the bitwise shift right operation. Effectively the same as
dividing by a power of 2.

    print(0b1010 >> 1) # Prints 5 (binary 101)
    print(0b1010 >> 2) # Prints 2 (binary 10)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_bwxor_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \^**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_bwxor_int>`{.interpreted-text role="ref"}

Performs the bitwise `XOR` operation.

    print(0b1100 ^ 0b1010) # Prints 6 (binary 110)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_unplus}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator unary+**()
`🔗<class_int_operator_unplus>`{.interpreted-text role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_unminus}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator unary-**()
`🔗<class_int_operator_unminus>`{.interpreted-text role="ref"}

Returns the negated value of the **int**. If positive, turns the number
negative. If negative, turns the number positive. If zero, does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_bwor_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \|**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_int_operator_bwor_int>`{.interpreted-text role="ref"}

Performs the bitwise `OR` operation.

    print(0b1100 | 0b1010) # Prints 14 (binary 1110)

This is useful for storing binary flags in a variable.

    var flags = 0
    flags |= 0b101 # Turn the first and third bits on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_int_operator_bwnot}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \~**()
`🔗<class_int_operator_bwnot>`{.interpreted-text role="ref"}

Performs the bitwise `NOT` operation on the **int**. Due to [2\'s
complement](https://en.wikipedia.org/wiki/Two%27s_complement), it\'s
effectively equal to `-(int + 1)`.

    print(~4) # Prints -5
    print(~(-7)) # Prints 6
