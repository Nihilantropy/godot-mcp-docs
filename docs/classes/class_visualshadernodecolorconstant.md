github_url
:   hide

# VisualShaderNodeColorConstant {#class_VisualShaderNodeColorConstant}

**Inherits:**
`VisualShaderNodeConstant<class_VisualShaderNodeConstant>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Color<class_Color>`{.interpreted-text role="ref"} constant to be used
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Has two output ports representing RGB and alpha channels of
`Color<class_Color>`{.interpreted-text role="ref"}.

Translated to `vec3 rgb` and `float alpha` in the shader language.

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

:::: {#class_VisualShaderNodeColorConstant_property_constant}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **constant** =
`Color(1, 1, 1, 1)`
`🔗<class_VisualShaderNodeColorConstant_property_constant>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_constant**()

A `Color<class_Color>`{.interpreted-text role="ref"} constant which
represents a state of this node.
