github_url
:   hide

# VisualShaderNodeParticleRandomness {#class_VisualShaderNodeParticleRandomness}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Visual shader node for randomizing particle values.

::: rst-class
classref-introduction-group
:::

## Description

Randomness node will output pseudo-random values of the given type based
on the specified minimum and maximum values.

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

:::: {#enum_VisualShaderNodeParticleRandomness_OpType}
::: rst-class
classref-enumeration
:::
::::

enum **OpType**:
`🔗<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

:::: {#class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

:::: {#class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

:::: {#class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

:::: {#class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_MAX** = `4`

Represents the size of the
`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeParticleRandomness_property_op_type}
::: rst-class
classref-property
:::
::::

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
role="ref"} **op_type** = `0`
`🔗<class_VisualShaderNodeParticleRandomness_property_op_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_op_type**(value:
  `OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
  role="ref"})
- `OpType<enum_VisualShaderNodeParticleRandomness_OpType>`{.interpreted-text
  role="ref"} **get_op_type**()

A type of operands and returned value.
