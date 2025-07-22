github_url
:   hide

# VisualShaderNodeVec4Parameter {#class_VisualShaderNodeVec4Parameter}

**Inherits:**
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 4D vector parameter to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translated to `uniform vec4` in the shader language.

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

:::: {#class_VisualShaderNodeVec4Parameter_property_default_value}
::: rst-class
classref-property
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **default_value**
= `Vector4(0, 0, 0, 0)`
`🔗<class_VisualShaderNodeVec4Parameter_property_default_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value**(value:
  `Vector4<class_Vector4>`{.interpreted-text role="ref"})
- `Vector4<class_Vector4>`{.interpreted-text role="ref"}
  **get_default_value**()

A default value to be assigned within the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeVec4Parameter_property_default_value_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**default_value_enabled** = `false`
`🔗<class_VisualShaderNodeVec4Parameter_property_default_value_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_default_value_enabled**()

Enables usage of the
`default_value<class_VisualShaderNodeVec4Parameter_property_default_value>`{.interpreted-text
role="ref"}.
