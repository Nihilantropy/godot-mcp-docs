github_url
:   hide

# VisualShaderNodeTransformConstant {#class_VisualShaderNodeTransformConstant}

**Inherits:**
`VisualShaderNodeConstant<class_VisualShaderNodeConstant>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
constant for use within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

A constant `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, which can be used as an input node.

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

:::: {#class_VisualShaderNodeTransformConstant_property_constant}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**constant** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_VisualShaderNodeTransformConstant_property_constant>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_constant**()

A `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
constant which represents the state of this node.
