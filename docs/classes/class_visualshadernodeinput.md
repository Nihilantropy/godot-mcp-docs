github_url
:   hide

# VisualShaderNodeInput {#class_VisualShaderNodeInput}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Represents the input shader parameter within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Gives access to input variables (built-ins) available for the shader.
See the shading reference for the list of available built-ins for each
shader type (check `Tutorials` section for link).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Shading reference index <../tutorials/shaders/shader_reference/index>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_VisualShaderNodeInput_signal_input_type_changed}
::: rst-class
classref-signal
:::
::::

**input_type_changed**()
`🔗<class_VisualShaderNodeInput_signal_input_type_changed>`{.interpreted-text
role="ref"}

Emitted when input is changed via
`input_name<class_VisualShaderNodeInput_property_input_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeInput_property_input_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **input_name** =
`"[None]"`
`🔗<class_VisualShaderNodeInput_property_input_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_input_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_input_name**()

One of the several input constants in lower-case style like: \"vertex\"
(`VERTEX`) or \"point_size\" (`POINT_SIZE`).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VisualShaderNodeInput_method_get_input_real_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_input_real_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeInput_method_get_input_real_name>`{.interpreted-text
role="ref"}

Returns a translated name of the current constant in the Godot Shader
Language. E.g. `"ALBEDO"` if the
`input_name<class_VisualShaderNodeInput_property_input_name>`{.interpreted-text
role="ref"} equal to `"albedo"`.
