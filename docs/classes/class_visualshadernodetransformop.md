github_url
:   hide

# VisualShaderNodeTransformOp {#class_VisualShaderNodeTransformOp}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
operator to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Applies
`operator<class_VisualShaderNodeTransformOp_property_operator>`{.interpreted-text
role="ref"} to two transform (4×4 matrices) inputs.

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

:::: {#enum_VisualShaderNodeTransformOp_Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Operator**:
`🔗<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTransformOp_constant_OP_AxB}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_AxB** = `0`

Multiplies transform `a` by the transform `b`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_BxA}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_BxA** = `1`

Multiplies transform `b` by the transform `a`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_AxB_COMP}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_AxB_COMP** = `2`

Performs a component-wise multiplication of transform `a` by the
transform `b`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_BxA_COMP}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_BxA_COMP** = `3`

Performs a component-wise multiplication of transform `b` by the
transform `a`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_ADD** = `4`

Adds two transforms.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_A_MINUS_B}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_A_MINUS_B** = `5`

Subtracts the transform `a` from the transform `b`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_B_MINUS_A}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_B_MINUS_A** = `6`

Subtracts the transform `b` from the transform `a`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_A_DIV_B}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_A_DIV_B** = `7`

Divides the transform `a` by the transform `b`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_B_DIV_A}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_B_DIV_A** = `8`

Divides the transform `b` by the transform `a`.

:::: {#class_VisualShaderNodeTransformOp_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `9`

Represents the size of the
`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeTransformOp_property_operator}
::: rst-class
classref-property
:::
::::

`Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
role="ref"} **operator** = `0`
`🔗<class_VisualShaderNodeTransformOp_property_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operator**(value:
  `Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
  role="ref"})
- `Operator<enum_VisualShaderNodeTransformOp_Operator>`{.interpreted-text
  role="ref"} **get_operator**()

The type of the operation to be performed on the transforms.
