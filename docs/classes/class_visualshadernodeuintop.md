github_url
:   hide

# VisualShaderNodeUIntOp {#class_VisualShaderNodeUIntOp}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An unsigned integer scalar operator to be used within the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

Applies
`operator<class_VisualShaderNodeUIntOp_property_operator>`{.interpreted-text
role="ref"} to two unsigned integer inputs: `a` and `b`.

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

:::: {#enum_VisualShaderNodeUIntOp_Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Operator**:
`🔗<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeUIntOp_constant_OP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_ADD** = `0`

Sums two numbers using `a + b`.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_MUL}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_DIV}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_DIV** = `3`

Divides two numbers using `a / b`.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_MOD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_MOD** = `4`

Calculates the remainder of two numbers using `a % b`.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `5`

Returns the greater of two numbers. Translates to `max(a, b)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_MIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_MIN** = `6`

Returns the lesser of two numbers. Translates to `max(a, b)` in the
Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_BITWISE_AND}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_BITWISE_AND** = `7`

Returns the result of bitwise `AND` operation on the integer. Translates
to `a & b` in the Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_BITWISE_OR}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_BITWISE_OR** = `8`

Returns the result of bitwise `OR` operation for two integers.
Translates to `a | b` in the Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_BITWISE_XOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_BITWISE_XOR** = `9`

Returns the result of bitwise `XOR` operation for two integers.
Translates to `a ^ b` in the Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_BITWISE_LEFT_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_BITWISE_LEFT_SHIFT** = `10`

Returns the result of bitwise left shift operation on the integer.
Translates to `a << b` in the Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_BITWISE_RIGHT_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_BITWISE_RIGHT_SHIFT** = `11`

Returns the result of bitwise right shift operation on the integer.
Translates to `a >> b` in the Godot Shader Language.

:::: {#class_VisualShaderNodeUIntOp_constant_OP_ENUM_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **OP_ENUM_SIZE** = `12`

Represents the size of the
`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeUIntOp_property_operator}
::: rst-class
classref-property
:::
::::

`Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
role="ref"} **operator** = `0`
`🔗<class_VisualShaderNodeUIntOp_property_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operator**(value:
  `Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
  role="ref"})
- `Operator<enum_VisualShaderNodeUIntOp_Operator>`{.interpreted-text
  role="ref"} **get_operator**()

An operator to be applied to the inputs.
