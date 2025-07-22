github_url
:   hide

# VisualShaderNodeVectorOp {#class_VisualShaderNodeVectorOp}

**Inherits:**
`VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A vector operator to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

A visual shader node for use of vector operators. Operates on vector `a`
and vector `b`.

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

:::: {#enum_VisualShaderNodeVectorOp_Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Operator**:
`🔗<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeVectorOp_constant_OP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_ADD** = `0`

Adds two vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_SUB** = `1`

Subtracts a vector from a vector.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_MUL}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_MUL** = `2`

Multiplies two vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_DIV}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_DIV** = `3`

Divides vector by vector.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_MOD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_MOD** = `4`

Returns the remainder of the two vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_POW}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_POW** = `5`

Returns the value of the first parameter raised to the power of the
second, for each component of the vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `6`

Returns the greater of two values, for each component of the vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_MIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_MIN** = `7`

Returns the lesser of two values, for each component of the vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_CROSS}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_CROSS** = `8`

Calculates the cross product of two vectors.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_ATAN2}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_ATAN2** = `9`

Returns the arc-tangent of the parameters.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_REFLECT}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_REFLECT** = `10`

Returns the vector that points in the direction of reflection. `a` is
incident vector and `b` is the normal vector.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_STEP** = `11`

Vector step operator. Returns `0.0` if `a` is smaller than `b` and `1.0`
otherwise.

:::: {#class_VisualShaderNodeVectorOp_constant_OP_ENUM_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **OP_ENUM_SIZE** = `12`

Represents the size of the
`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeVectorOp_property_operator}
::: rst-class
classref-property
:::
::::

`Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
role="ref"} **operator** = `0`
`🔗<class_VisualShaderNodeVectorOp_property_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operator**(value:
  `Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
  role="ref"})
- `Operator<enum_VisualShaderNodeVectorOp_Operator>`{.interpreted-text
  role="ref"} **get_operator**()

The operator to be used.
