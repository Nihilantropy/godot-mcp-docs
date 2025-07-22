github_url
:   hide

# VisualShaderNodeVectorFunc {#class_VisualShaderNodeVectorFunc}

**Inherits:**
`VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A vector function to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

A visual shader node able to perform different functions using vectors.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_VisualShaderNodeVectorFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_NORMALIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_NORMALIZE** = `0`

Normalizes the vector so that it has a length of `1` but points in the
same direction.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_SATURATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SATURATE** = `1`

Clamps the value between `0.0` and `1.0`.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_NEGATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_NEGATE** = `2`

Returns the opposite value of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_RECIPROCAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_RECIPROCAL** = `3`

Returns `1/vector`.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ABS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ABS** = `4`

Returns the absolute value of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ACOS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ACOS** = `5`

Returns the arc-cosine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ACOSH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ACOSH** = `6`

Returns the inverse hyperbolic cosine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ASIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ASIN** = `7`

Returns the arc-sine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ASINH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ASINH** = `8`

Returns the inverse hyperbolic sine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ATAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ATAN** = `9`

Returns the arc-tangent of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ATANH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ATANH** = `10`

Returns the inverse hyperbolic tangent of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_CEIL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_CEIL** = `11`

Finds the nearest integer that is greater than or equal to the
parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_COS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_COS** = `12`

Returns the cosine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_COSH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_COSH** = `13`

Returns the hyperbolic cosine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_DEGREES}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_DEGREES** = `14`

Converts a quantity in radians to degrees.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_EXP}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_EXP** = `15`

Base-e Exponential.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_EXP2}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_EXP2** = `16`

Base-2 Exponential.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_FLOOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_FLOOR** = `17`

Finds the nearest integer less than or equal to the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_FRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_FRACT** = `18`

Computes the fractional part of the argument.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_INVERSE_SQRT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_INVERSE_SQRT** = `19`

Returns the inverse of the square root of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_LOG}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_LOG** = `20`

Natural logarithm.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_LOG2}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_LOG2** = `21`

Base-2 logarithm.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_RADIANS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_RADIANS** = `22`

Converts a quantity in degrees to radians.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ROUND** = `23`

Finds the nearest integer to the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ROUNDEVEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ROUNDEVEN** = `24`

Finds the nearest even integer to the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_SIGN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SIGN** = `25`

Extracts the sign of the parameter, i.e. returns `-1` if the parameter
is negative, `1` if it\'s positive and `0` otherwise.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_SIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SIN** = `26`

Returns the sine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_SINH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SINH** = `27`

Returns the hyperbolic sine of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_SQRT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SQRT** = `28`

Returns the square root of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_TAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TAN** = `29`

Returns the tangent of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_TANH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TANH** = `30`

Returns the hyperbolic tangent of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_TRUNC}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TRUNC** = `31`

Returns a value equal to the nearest integer to the parameter whose
absolute value is not larger than the absolute value of the parameter.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_ONEMINUS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ONEMINUS** = `32`

Returns `1.0 - vector`.

:::: {#class_VisualShaderNodeVectorFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `33`

Represents the size of the
`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeVectorFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeVectorFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeVectorFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

The function to be performed.
