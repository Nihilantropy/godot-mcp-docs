github_url
:   hide

# VisualShaderNodeFloatOp {#class_VisualShaderNodeFloatOp}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A floating-point scalar operator to be used within the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

Applies
`operator<class_VisualShaderNodeFloatOp_property_operator>`{.interpreted-text
role="ref"} to two floating-point inputs: `a` and `b`.

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

:::: {#enum_VisualShaderNodeFloatOp_Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Operator**:
`🔗<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeFloatOp_constant_OP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_ADD** = `0`

Sums two numbers using `a + b`.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_MUL}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_DIV}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_DIV** = `3`

Divides two numbers using `a / b`.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_MOD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_MOD** = `4`

Calculates the remainder of two numbers. Translates to `mod(a, b)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_POW}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_POW** = `5`

Raises the `a` to the power of `b`. Translates to `pow(a, b)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `6`

Returns the greater of two numbers. Translates to `max(a, b)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_MIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_MIN** = `7`

Returns the lesser of two numbers. Translates to `min(a, b)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_ATAN2}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_ATAN2** = `8`

Returns the arc-tangent of the parameters. Translates to `atan(a, b)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_STEP** = `9`

Generates a step function by comparing `b`(x) to `a`(edge). Returns 0.0
if `x` is smaller than `edge` and otherwise 1.0. Translates to
`step(a, b)` in the Godot Shader Language.

:::: {#class_VisualShaderNodeFloatOp_constant_OP_ENUM_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **OP_ENUM_SIZE** = `10`

Represents the size of the
`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeFloatOp_property_operator}
::: rst-class
classref-property
:::
::::

`Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
role="ref"} **operator** = `0`
`🔗<class_VisualShaderNodeFloatOp_property_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operator**(value:
  `Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
  role="ref"})
- `Operator<enum_VisualShaderNodeFloatOp_Operator>`{.interpreted-text
  role="ref"} **get_operator**()

An operator to be applied to the inputs.
