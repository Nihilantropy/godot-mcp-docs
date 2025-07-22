github_url
:   hide

# VisualShaderNodeVarying {#class_VisualShaderNodeVarying}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeVaryingGetter<class_VisualShaderNodeVaryingGetter>`{.interpreted-text
role="ref"},
`VisualShaderNodeVaryingSetter<class_VisualShaderNodeVaryingSetter>`{.interpreted-text
role="ref"}

A visual shader node that represents a \"varying\" shader value.

::: rst-class
classref-introduction-group
:::

## Description

Varying values are shader variables that can be passed between shader
functions, e.g. from Vertex shader to Fragment shader.

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

:::: {#class_VisualShaderNodeVarying_property_varying_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **varying_name** =
`"[None]"`
`🔗<class_VisualShaderNodeVarying_property_varying_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_varying_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_varying_name**()

Name of the variable. Must be unique.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeVarying_property_varying_type}
::: rst-class
classref-property
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **varying_type** = `0`
`🔗<class_VisualShaderNodeVarying_property_varying_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_varying_type**(value:
  `VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
  role="ref"})
- `VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
  role="ref"} **get_varying_type**()

Type of the variable. Determines where the variable can be accessed.
