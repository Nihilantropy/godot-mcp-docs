github_url
:   hide

# VisualShaderNodeFloatFunc {#class_VisualShaderNodeFloatFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A scalar floating-point function to be used within the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

Accept a floating-point scalar (`x`) to the input port and transform it
according to
`function<class_VisualShaderNodeFloatFunc_property_function>`{.interpreted-text
role="ref"}.

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

:::: {#enum_VisualShaderNodeFloatFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_SIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SIN** = `0`

Returns the sine of the parameter. Translates to `sin(x)` in the Godot
Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_COS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_COS** = `1`

Returns the cosine of the parameter. Translates to `cos(x)` in the Godot
Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_TAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TAN** = `2`

Returns the tangent of the parameter. Translates to `tan(x)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ASIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ASIN** = `3`

Returns the arc-sine of the parameter. Translates to `asin(x)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ACOS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ACOS** = `4`

Returns the arc-cosine of the parameter. Translates to `acos(x)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ATAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ATAN** = `5`

Returns the arc-tangent of the parameter. Translates to `atan(x)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_SINH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SINH** = `6`

Returns the hyperbolic sine of the parameter. Translates to `sinh(x)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_COSH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_COSH** = `7`

Returns the hyperbolic cosine of the parameter. Translates to `cosh(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_TANH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TANH** = `8`

Returns the hyperbolic tangent of the parameter. Translates to `tanh(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_LOG}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_LOG** = `9`

Returns the natural logarithm of the parameter. Translates to `log(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_EXP}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_EXP** = `10`

Returns the natural exponentiation of the parameter. Translates to
`exp(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_SQRT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SQRT** = `11`

Returns the square root of the parameter. Translates to `sqrt(x)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ABS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ABS** = `12`

Returns the absolute value of the parameter. Translates to `abs(x)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_SIGN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SIGN** = `13`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot
Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_FLOOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_FLOOR** = `14`

Finds the nearest integer less than or equal to the parameter.
Translates to `floor(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ROUND** = `15`

Finds the nearest integer to the parameter. Translates to `round(x)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_CEIL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_CEIL** = `16`

Finds the nearest integer that is greater than or equal to the
parameter. Translates to `ceil(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_FRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_FRACT** = `17`

Computes the fractional part of the argument. Translates to `fract(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_SATURATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SATURATE** = `18`

Clamps the value between `0.0` and `1.0` using `min(max(x, 0.0), 1.0)`.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_NEGATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_NEGATE** = `19`

Negates the `x` using `-(x)`.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ACOSH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ACOSH** = `20`

Returns the arc-hyperbolic-cosine of the parameter. Translates to
`acosh(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ASINH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ASINH** = `21`

Returns the arc-hyperbolic-sine of the parameter. Translates to
`asinh(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ATANH}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ATANH** = `22`

Returns the arc-hyperbolic-tangent of the parameter. Translates to
`atanh(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_DEGREES}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_DEGREES** = `23`

Convert a quantity in radians to degrees. Translates to `degrees(x)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_EXP2}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_EXP2** = `24`

Returns 2 raised by the power of the parameter. Translates to `exp2(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_INVERSE_SQRT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_INVERSE_SQRT** = `25`

Returns the inverse of the square root of the parameter. Translates to
`inversesqrt(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_LOG2}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_LOG2** = `26`

Returns the base 2 logarithm of the parameter. Translates to `log2(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_RADIANS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_RADIANS** = `27`

Convert a quantity in degrees to radians. Translates to `radians(x)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_RECIPROCAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_RECIPROCAL** = `28`

Finds reciprocal value of dividing 1 by `x` (i.e. `1 / x`).

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ROUNDEVEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ROUNDEVEN** = `29`

Finds the nearest even integer to the parameter. Translates to
`roundEven(x)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_TRUNC}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TRUNC** = `30`

Returns a value equal to the nearest integer to `x` whose absolute value
is not larger than the absolute value of `x`. Translates to `trunc(x)`
in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_ONEMINUS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ONEMINUS** = `31`

Subtracts scalar `x` from 1 (i.e. `1 - x`).

:::: {#class_VisualShaderNodeFloatFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `32`

Represents the size of the
`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeFloatFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
role="ref"} **function** = `13`
`🔗<class_VisualShaderNodeFloatFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeFloatFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A function to be applied to the scalar.
