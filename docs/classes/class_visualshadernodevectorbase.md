github_url
:   hide

# VisualShaderNodeVectorBase {#class_VisualShaderNodeVectorBase}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeFaceForward<class_VisualShaderNodeFaceForward>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorCompose<class_VisualShaderNodeVectorCompose>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorDecompose<class_VisualShaderNodeVectorDecompose>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorDistance<class_VisualShaderNodeVectorDistance>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorFunc<class_VisualShaderNodeVectorFunc>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorLen<class_VisualShaderNodeVectorLen>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorOp<class_VisualShaderNodeVectorOp>`{.interpreted-text
role="ref"},
`VisualShaderNodeVectorRefract<class_VisualShaderNodeVectorRefract>`{.interpreted-text
role="ref"}

A base type for the nodes that perform vector operations within the
visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

This is an abstract class. See the derived types for descriptions of the
possible operations.

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

:::: {#enum_VisualShaderNodeVectorBase_OpType}
::: rst-class
classref-enumeration
:::
::::

enum **OpType**:
`🔗<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeVectorBase_constant_OP_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D** = `0`

A 2D vector type.

:::: {#class_VisualShaderNodeVectorBase_constant_OP_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D** = `1`

A 3D vector type.

:::: {#class_VisualShaderNodeVectorBase_constant_OP_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D** = `2`

A 4D vector type.

:::: {#class_VisualShaderNodeVectorBase_constant_OP_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_MAX** = `3`

Represents the size of the
`OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeVectorBase_property_op_type}
::: rst-class
classref-property
:::
::::

`OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
role="ref"} **op_type** = `1`
`🔗<class_VisualShaderNodeVectorBase_property_op_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_op_type**(value:
  `OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
  role="ref"})
- `OpType<enum_VisualShaderNodeVectorBase_OpType>`{.interpreted-text
  role="ref"} **get_op_type**()

A vector type that this operation is performed on.
