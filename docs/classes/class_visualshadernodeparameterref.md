github_url
:   hide

# VisualShaderNodeParameterRef {#class_VisualShaderNodeParameterRef}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A reference to an existing
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Creating a reference to a
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} allows you to reuse this parameter in different shaders or
shader stages easily.

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

:::: {#class_VisualShaderNodeParameterRef_property_parameter_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **parameter_name**
= `"[None]"`
`🔗<class_VisualShaderNodeParameterRef_property_parameter_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parameter_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_parameter_name**()

The name of the parameter which this reference points to.
