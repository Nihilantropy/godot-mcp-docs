github_url
:   hide

# VisualShaderNodeParameter {#class_VisualShaderNodeParameter}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeBooleanParameter<class_VisualShaderNodeBooleanParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeColorParameter<class_VisualShaderNodeColorParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeFloatParameter<class_VisualShaderNodeFloatParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeIntParameter<class_VisualShaderNodeIntParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeTextureParameter<class_VisualShaderNodeTextureParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeTransformParameter<class_VisualShaderNodeTransformParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeUIntParameter<class_VisualShaderNodeUIntParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeVec2Parameter<class_VisualShaderNodeVec2Parameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeVec3Parameter<class_VisualShaderNodeVec3Parameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeVec4Parameter<class_VisualShaderNodeVec4Parameter>`{.interpreted-text
role="ref"}

A base type for the parameters within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

A parameter represents a variable in the shader which is set externally,
i.e. from the `ShaderMaterial<class_ShaderMaterial>`{.interpreted-text
role="ref"}. Parameters are exposed as properties in the
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"} and
can be assigned from the Inspector or from a script.

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

:::: {#enum_VisualShaderNodeParameter_Qualifier}
::: rst-class
classref-enumeration
:::
::::

enum **Qualifier**:
`🔗<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeParameter_constant_QUAL_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"} **QUAL_NONE** = `0`

The parameter will be tied to the
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}
using this shader.

:::: {#class_VisualShaderNodeParameter_constant_QUAL_GLOBAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"} **QUAL_GLOBAL** = `1`

The parameter will use a global value, defined in Project Settings.

:::: {#class_VisualShaderNodeParameter_constant_QUAL_INSTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"} **QUAL_INSTANCE** = `2`

The parameter will be tied to the node with attached
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}
using this shader.

:::: {#class_VisualShaderNodeParameter_constant_QUAL_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"} **QUAL_MAX** = `3`

Represents the size of the
`Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeParameter_property_parameter_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **parameter_name**
= `""`
`🔗<class_VisualShaderNodeParameter_property_parameter_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parameter_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_parameter_name**()

Name of the parameter, by which it can be accessed through the
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}
properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeParameter_property_qualifier}
::: rst-class
classref-property
:::
::::

`Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
role="ref"} **qualifier** = `0`
`🔗<class_VisualShaderNodeParameter_property_qualifier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_qualifier**(value:
  `Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
  role="ref"})
- `Qualifier<enum_VisualShaderNodeParameter_Qualifier>`{.interpreted-text
  role="ref"} **get_qualifier**()

Defines the scope of the parameter.
