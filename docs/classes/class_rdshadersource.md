github_url
:   hide

# RDShaderSource {#class_RDShaderSource}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Shader source code (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

Shader source code in text form.

See also `RDShaderFile<class_RDShaderFile>`{.interpreted-text
role="ref"}. **RDShaderSource** is only meant to be used with the
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

:::: {#class_RDShaderSource_property_language}
::: rst-class
classref-property
:::
::::

`ShaderLanguage<enum_RenderingDevice_ShaderLanguage>`{.interpreted-text
role="ref"} **language** = `0`
`🔗<class_RDShaderSource_property_language>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value:
  `ShaderLanguage<enum_RenderingDevice_ShaderLanguage>`{.interpreted-text
  role="ref"})
- `ShaderLanguage<enum_RenderingDevice_ShaderLanguage>`{.interpreted-text
  role="ref"} **get_language**()

The language the shader is written in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSource_property_source_compute}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **source_compute**
= `""`
`🔗<class_RDShaderSource_property_source_compute>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, source: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Source code for the shader\'s compute stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSource_property_source_fragment}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **source_fragment**
= `""`
`🔗<class_RDShaderSource_property_source_fragment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, source: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Source code for the shader\'s fragment stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSource_property_source_tesselation_control}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**source_tesselation_control** = `""`
`🔗<class_RDShaderSource_property_source_tesselation_control>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, source: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Source code for the shader\'s tessellation control stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSource_property_source_tesselation_evaluation}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**source_tesselation_evaluation** = `""`
`🔗<class_RDShaderSource_property_source_tesselation_evaluation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, source: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Source code for the shader\'s tessellation evaluation stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSource_property_source_vertex}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **source_vertex** =
`""` `🔗<class_RDShaderSource_property_source_vertex>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"}, source: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_stage_source**(stage:
  `ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Source code for the shader\'s vertex stage.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RDShaderSource_method_get_stage_source}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_stage_source**(stage:
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RDShaderSource_method_get_stage_source>`{.interpreted-text
role="ref"}

Returns source code for the specified shader `stage`. Equivalent to
getting one of
`source_compute<class_RDShaderSource_property_source_compute>`{.interpreted-text
role="ref"},
`source_fragment<class_RDShaderSource_property_source_fragment>`{.interpreted-text
role="ref"},
`source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>`{.interpreted-text
role="ref"},
`source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>`{.interpreted-text
role="ref"} or
`source_vertex<class_RDShaderSource_property_source_vertex>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDShaderSource_method_set_stage_source}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stage_source**(stage:
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"}, source: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RDShaderSource_method_set_stage_source>`{.interpreted-text
role="ref"}

Sets `source` code for the specified shader `stage`. Equivalent to
setting one of
`source_compute<class_RDShaderSource_property_source_compute>`{.interpreted-text
role="ref"},
`source_fragment<class_RDShaderSource_property_source_fragment>`{.interpreted-text
role="ref"},
`source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>`{.interpreted-text
role="ref"},
`source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>`{.interpreted-text
role="ref"} or
`source_vertex<class_RDShaderSource_property_source_vertex>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If you set the compute shader source code using this
method directly, remember to remove the Godot-specific hint
`#[compute]`.
