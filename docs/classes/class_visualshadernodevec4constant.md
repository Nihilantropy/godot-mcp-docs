github_url
:   hide

# VisualShaderNodeVec4Constant {#class_VisualShaderNodeVec4Constant}

**Inherits:**
`VisualShaderNodeConstant<class_VisualShaderNodeConstant>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 4D vector constant to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

A constant 4D vector, which can be used as an input node.

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

## Property Descriptions

:::: {#class_VisualShaderNodeVec4Constant_property_constant}
::: rst-class
classref-property
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**constant** = `Quaternion(0, 0, 0, 1)`
`🔗<class_VisualShaderNodeVec4Constant_property_constant>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant**(value:
  `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
- `Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
  **get_constant**()

A 4D vector (represented as a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}) constant
which represents the state of this node.
