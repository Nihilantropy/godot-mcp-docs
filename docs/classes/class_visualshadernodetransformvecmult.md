github_url
:   hide

# VisualShaderNodeTransformVecMult {#class_VisualShaderNodeTransformVecMult}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Multiplies a `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} and a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

A multiplication operation on a transform (4×4 matrix) and a vector,
with support for different multiplication operators.

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

:::: {#enum_VisualShaderNodeTransformVecMult_Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Operator**:
`🔗<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTransformVecMult_constant_OP_AxB}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} **OP_AxB** = `0`

Multiplies transform `a` by the vector `b`.

:::: {#class_VisualShaderNodeTransformVecMult_constant_OP_BxA}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} **OP_BxA** = `1`

Multiplies vector `b` by the transform `a`.

:::: {#class_VisualShaderNodeTransformVecMult_constant_OP_3x3_AxB}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} **OP_3x3_AxB** = `2`

Multiplies transform `a` by the vector `b`, skipping the last row and
column of the transform.

:::: {#class_VisualShaderNodeTransformVecMult_constant_OP_3x3_BxA}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} **OP_3x3_BxA** = `3`

Multiplies vector `b` by the transform `a`, skipping the last row and
column of the transform.

:::: {#class_VisualShaderNodeTransformVecMult_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `4`

Represents the size of the
`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeTransformVecMult_property_operator}
::: rst-class
classref-property
:::
::::

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
role="ref"} **operator** = `0`
`🔗<class_VisualShaderNodeTransformVecMult_property_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operator**(value:
  `Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
  role="ref"})
- `Operator<enum_VisualShaderNodeTransformVecMult_Operator>`{.interpreted-text
  role="ref"} **get_operator**()

The multiplication type to be performed.
