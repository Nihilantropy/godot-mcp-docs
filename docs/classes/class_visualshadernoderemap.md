github_url
:   hide

# VisualShaderNodeRemap {#class_VisualShaderNodeRemap}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node for remap function.

::: rst-class
classref-introduction-group
:::

## Description

Remap will transform the input range into output range, e.g. you can
change a `0..1` value to `-2..2` etc. See
`@GlobalScope.remap()<class_@GlobalScope_method_remap>`{.interpreted-text
role="ref"} for more details.

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

:::: {#enum_VisualShaderNodeRemap_OpType}
::: rst-class
classref-enumeration
:::
::::

enum **OpType**:
`🔗<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_2D_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `value` port uses a 2D vector type, while the `input min`,
`input max`, `output min`, and `output max` ports use a floating-point
scalar type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_3D_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `value` port uses a 3D vector type, while the `input min`,
`input max`, `output min`, and `output max` ports use a floating-point
scalar type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_4D_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `value` port uses a 4D vector type, while the `input min`,
`input max`, `output min`, and `output max` ports use a floating-point
scalar type.

:::: {#class_VisualShaderNodeRemap_constant_OP_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_MAX** = `7`

Represents the size of the
`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeRemap_property_op_type}
::: rst-class
classref-property
:::
::::

`OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
role="ref"} **op_type** = `0`
`🔗<class_VisualShaderNodeRemap_property_op_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_op_type**(value:
  `OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
  role="ref"})
- `OpType<enum_VisualShaderNodeRemap_OpType>`{.interpreted-text
  role="ref"} **get_op_type**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
