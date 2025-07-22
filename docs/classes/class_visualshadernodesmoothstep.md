github_url
:   hide

# VisualShaderNodeSmoothStep {#class_VisualShaderNodeSmoothStep}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Calculates a SmoothStep function within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translates to `smoothstep(edge0, edge1, x)` in the shader language.

Returns `0.0` if `x` is smaller than `edge0` and `1.0` if `x` is larger
than `edge1`. Otherwise, the return value is interpolated between `0.0`
and `1.0` using Hermite polynomials.

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

:::: {#enum_VisualShaderNodeSmoothStep_OpType}
::: rst-class
classref-enumeration
:::
::::

enum **OpType**:
`🔗<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_2D_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `x` port uses a 2D vector type. The first two ports use a
floating-point scalar type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_3D_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `x` port uses a 3D vector type. The first two ports use a
floating-point scalar type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_4D_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a
scalar type.

:::: {#class_VisualShaderNodeSmoothStep_constant_OP_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_MAX** = `7`

Represents the size of the
`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeSmoothStep_property_op_type}
::: rst-class
classref-property
:::
::::

`OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
role="ref"} **op_type** = `0`
`🔗<class_VisualShaderNodeSmoothStep_property_op_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_op_type**(value:
  `OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
  role="ref"})
- `OpType<enum_VisualShaderNodeSmoothStep_OpType>`{.interpreted-text
  role="ref"} **get_op_type**()

A type of operands and returned value.
