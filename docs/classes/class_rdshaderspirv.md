github_url
:   hide

# RDShaderSPIRV {#class_RDShaderSPIRV}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

SPIR-V intermediate representation as part of an
`RDShaderFile<class_RDShaderFile>`{.interpreted-text role="ref"} (used
by `RenderingDevice<class_RenderingDevice>`{.interpreted-text
role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

**RDShaderSPIRV** represents an
`RDShaderFile<class_RDShaderFile>`{.interpreted-text role="ref"}\'s
[SPIR-V](https://www.khronos.org/spir/) code for various shader stages,
as well as possible compilation error messages. SPIR-V is a low-level
intermediate shader representation. This intermediate representation is
not used directly by GPUs for rendering, but it can be compiled into
binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V
is portable across GPU models and driver versions.

This object is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

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

:::: {#class_RDShaderSPIRV_property_bytecode_compute}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**bytecode_compute** = `PackedByteArray()`
`🔗<class_RDShaderSPIRV_property_bytecode_compute>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, bytecode:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The SPIR-V bytecode for the compute shader stage.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_bytecode_fragment}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**bytecode_fragment** = `PackedByteArray()`
`🔗<class_RDShaderSPIRV_property_bytecode_fragment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, bytecode:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The SPIR-V bytecode for the fragment shader stage.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_bytecode_tesselation_control}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**bytecode_tesselation_control** = `PackedByteArray()`
`🔗<class_RDShaderSPIRV_property_bytecode_tesselation_control>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, bytecode:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The SPIR-V bytecode for the tessellation control shader stage.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_bytecode_tesselation_evaluation}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**bytecode_tesselation_evaluation** = `PackedByteArray()`
`🔗<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, bytecode:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The SPIR-V bytecode for the tessellation evaluation shader stage.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_bytecode_vertex}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**bytecode_vertex** = `PackedByteArray()`
`🔗<class_RDShaderSPIRV_property_bytecode_vertex>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, bytecode:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_stage_bytecode**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The SPIR-V bytecode for the vertex shader stage.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_compile_error_compute}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**compile_error_compute** = `""`
`🔗<class_RDShaderSPIRV_property_compile_error_compute>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, compile_error: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The compilation error message for the compute shader stage (set by the
SPIR-V compiler and Godot). If empty, shader compilation was successful.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_compile_error_fragment}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**compile_error_fragment** = `""`
`🔗<class_RDShaderSPIRV_property_compile_error_fragment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, compile_error: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The compilation error message for the fragment shader stage (set by the
SPIR-V compiler and Godot). If empty, shader compilation was successful.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_compile_error_tesselation_control}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**compile_error_tesselation_control** = `""`
`🔗<class_RDShaderSPIRV_property_compile_error_tesselation_control>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, compile_error: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The compilation error message for the tessellation control shader stage
(set by the SPIR-V compiler and Godot). If empty, shader compilation was
successful.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_compile_error_tesselation_evaluation}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**compile_error_tesselation_evaluation** = `""`
`🔗<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, compile_error: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The compilation error message for the tessellation evaluation shader
stage (set by the SPIR-V compiler and Godot). If empty, shader
compilation was successful.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_property_compile_error_vertex}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**compile_error_vertex** = `""`
`🔗<class_RDShaderSPIRV_property_compile_error_vertex>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, compile_error: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_compile_error**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The compilation error message for the vertex shader stage (set by the
SPIR-V compiler and Godot). If empty, shader compilation was successful.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RDShaderSPIRV_method_get_stage_bytecode}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_stage_bytecode**(stage:
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RDShaderSPIRV_method_get_stage_bytecode>`{.interpreted-text
role="ref"}

Equivalent to getting one of
`bytecode_compute<class_RDShaderSPIRV_property_bytecode_compute>`{.interpreted-text
role="ref"},
`bytecode_fragment<class_RDShaderSPIRV_property_bytecode_fragment>`{.interpreted-text
role="ref"},
`bytecode_tesselation_control<class_RDShaderSPIRV_property_bytecode_tesselation_control>`{.interpreted-text
role="ref"},
`bytecode_tesselation_evaluation<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>`{.interpreted-text
role="ref"},
`bytecode_vertex<class_RDShaderSPIRV_property_bytecode_vertex>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_method_get_stage_compile_error}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_stage_compile_error**(stage:
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RDShaderSPIRV_method_get_stage_compile_error>`{.interpreted-text
role="ref"}

Returns the compilation error message for the given shader `stage`.
Equivalent to getting one of
`compile_error_compute<class_RDShaderSPIRV_property_compile_error_compute>`{.interpreted-text
role="ref"},
`compile_error_fragment<class_RDShaderSPIRV_property_compile_error_fragment>`{.interpreted-text
role="ref"},
`compile_error_tesselation_control<class_RDShaderSPIRV_property_compile_error_tesselation_control>`{.interpreted-text
role="ref"},
`compile_error_tesselation_evaluation<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>`{.interpreted-text
role="ref"},
`compile_error_vertex<class_RDShaderSPIRV_property_compile_error_vertex>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_method_set_stage_bytecode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stage_bytecode**(stage:
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"}, bytecode:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_RDShaderSPIRV_method_set_stage_bytecode>`{.interpreted-text
role="ref"}

Sets the SPIR-V `bytecode` for the given shader `stage`. Equivalent to
setting one of
`bytecode_compute<class_RDShaderSPIRV_property_bytecode_compute>`{.interpreted-text
role="ref"},
`bytecode_fragment<class_RDShaderSPIRV_property_bytecode_fragment>`{.interpreted-text
role="ref"},
`bytecode_tesselation_control<class_RDShaderSPIRV_property_bytecode_tesselation_control>`{.interpreted-text
role="ref"},
`bytecode_tesselation_evaluation<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>`{.interpreted-text
role="ref"},
`bytecode_vertex<class_RDShaderSPIRV_property_bytecode_vertex>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSPIRV_method_set_stage_compile_error}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stage_compile_error**(stage:
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"}, compile_error: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RDShaderSPIRV_method_set_stage_compile_error>`{.interpreted-text
role="ref"}

Sets the compilation error message for the given shader `stage` to
`compile_error`. Equivalent to setting one of
`compile_error_compute<class_RDShaderSPIRV_property_compile_error_compute>`{.interpreted-text
role="ref"},
`compile_error_fragment<class_RDShaderSPIRV_property_compile_error_fragment>`{.interpreted-text
role="ref"},
`compile_error_tesselation_control<class_RDShaderSPIRV_property_compile_error_tesselation_control>`{.interpreted-text
role="ref"},
`compile_error_tesselation_evaluation<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>`{.interpreted-text
role="ref"},
`compile_error_vertex<class_RDShaderSPIRV_property_compile_error_vertex>`{.interpreted-text
role="ref"}.
