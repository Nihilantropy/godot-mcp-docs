github_url
:   hide

# VisualShaderNodeClamp {#class_VisualShaderNodeClamp}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Clamps a value within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Constrains a value to lie between `min` and `max` values.

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

:::: {#enum_VisualShaderNodeClamp_OpType}
::: rst-class
classref-enumeration
:::
::::

enum **OpType**:
`🔗<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_FLOAT** = `0`

A floating-point scalar.

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_INT** = `1`

An integer scalar.

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_UINT** = `2`

An unsigned integer scalar.

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

:::: {#class_VisualShaderNodeClamp_constant_OP_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_MAX** = `6`

Represents the size of the
`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeClamp_property_op_type}
::: rst-class
classref-property
:::
::::

`OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
role="ref"} **op_type** = `0`
`🔗<class_VisualShaderNodeClamp_property_op_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_op_type**(value:
  `OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
  role="ref"})
- `OpType<enum_VisualShaderNodeClamp_OpType>`{.interpreted-text
  role="ref"} **get_op_type**()

A type of operands and returned value.
