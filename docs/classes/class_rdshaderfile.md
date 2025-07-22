github_url
:   hide

# RDShaderFile {#class_RDShaderFile}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Compiled shader file in SPIR-V form (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).
Not to be confused with Godot\'s own
`Shader<class_Shader>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Compiled shader file in SPIR-V form.

See also `RDShaderSource<class_RDShaderSource>`{.interpreted-text
role="ref"}. **RDShaderFile** is only meant to be used with the
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}
API. It should not be confused with Godot\'s own
`Shader<class_Shader>`{.interpreted-text role="ref"} resource, which is
what Godot\'s various nodes use for high-level shader programming.

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

## Property Descriptions

:::: {#class_RDShaderFile_property_base_error}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **base_error** =
`""` `🔗<class_RDShaderFile_property_base_error>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_base_error**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_base_error**()

The base compilation error message, which indicates errors not related
to a specific shader stage if non-empty. If empty, shader compilation is
not necessarily successful (check
`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"}\'s
error message members).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RDShaderFile_method_get_spirv}
::: rst-class
classref-method
:::
::::

`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"}
**get_spirv**(version: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RDShaderFile_method_get_spirv>`{.interpreted-text
role="ref"}

Returns the SPIR-V intermediate representation for the specified shader
`version`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderFile_method_get_version_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_version_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RDShaderFile_method_get_version_list>`{.interpreted-text
role="ref"}

Returns the list of compiled versions for this shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderFile_method_set_bytecode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bytecode**(bytecode:
`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"},
version: `StringName<class_StringName>`{.interpreted-text role="ref"} =
&\"\") `🔗<class_RDShaderFile_method_set_bytecode>`{.interpreted-text
role="ref"}

Sets the SPIR-V `bytecode` that will be compiled for the specified
`version`.
