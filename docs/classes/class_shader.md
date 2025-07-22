github_url
:   hide

# Shader {#class_Shader}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `VisualShader<class_VisualShader>`{.interpreted-text
role="ref"}

A shader implemented in the Godot shading language.

::: rst-class
classref-introduction-group
:::

## Description

A custom shader program implemented in the Godot shading language, saved
with the `.gdshader` extension.

This class is used by a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"} and
allows you to write your own custom behavior for rendering visual items
or updating particle information. For a detailed explanation and usage,
please see the tutorials linked below.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Shaders documentation index <../tutorials/shaders/index>`{.interpreted-text
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

## Enumerations

:::: {#enum_Shader_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**: `🔗<enum_Shader_Mode>`{.interpreted-text role="ref"}

:::: {#class_Shader_constant_MODE_SPATIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"} **MODE_SPATIAL**
= `0`

Mode used to draw all 3D objects.

:::: {#class_Shader_constant_MODE_CANVAS_ITEM}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"}
**MODE_CANVAS_ITEM** = `1`

Mode used to draw all 2D objects.

:::: {#class_Shader_constant_MODE_PARTICLES}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"}
**MODE_PARTICLES** = `2`

Mode used to calculate particle information on a per-particle basis. Not
used for drawing.

:::: {#class_Shader_constant_MODE_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"} **MODE_SKY** =
`3`

Mode used for drawing skies. Only works with shaders attached to
`Sky<class_Sky>`{.interpreted-text role="ref"} objects.

:::: {#class_Shader_constant_MODE_FOG}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"} **MODE_FOG** =
`4`

Mode used for setting the color and density of volumetric fog effect.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Shader_property_code}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **code** = `""`
`🔗<class_Shader_property_code>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_code**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_code**()

Returns the shader\'s code as the user has written it, not the full
generated code used internally.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Shader_method_get_default_texture_parameter}
::: rst-class
classref-method
:::
::::

`Texture<class_Texture>`{.interpreted-text role="ref"}
**get_default_texture_parameter**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Shader_method_get_default_texture_parameter>`{.interpreted-text
role="ref"}

Returns the texture that is set as default for the specified parameter.

\*\*Note:\*\* `name` must match the name of the uniform in the code
exactly.

\*\*Note:\*\* If the sampler array is used use `index` to access the
specified texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shader_method_get_mode}
::: rst-class
classref-method
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"} **get_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Shader_method_get_mode>`{.interpreted-text
role="ref"}

Returns the shader mode for the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shader_method_get_shader_uniform_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_shader_uniform_list**(get_groups:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Shader_method_get_shader_uniform_list>`{.interpreted-text
role="ref"}

Returns the list of shader uniforms that can be assigned to a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
for use with
`ShaderMaterial.set_shader_parameter()<class_ShaderMaterial_method_set_shader_parameter>`{.interpreted-text
role="ref"} and
`ShaderMaterial.get_shader_parameter()<class_ShaderMaterial_method_get_shader_parameter>`{.interpreted-text
role="ref"}. The parameters returned are contained in dictionaries in a
similar format to the ones returned by
`Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}.

If argument `get_groups` is `true`, parameter grouping hints are also
included in the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shader_method_inspect_native_shader_code}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**inspect_native_shader_code**()
`🔗<class_Shader_method_inspect_native_shader_code>`{.interpreted-text
role="ref"}

Only available when running in the editor. Opens a popup that visualizes
the generated shader code, including all variants and internal shader
code. See also
`Material.inspect_native_shader_code()<class_Material_method_inspect_native_shader_code>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shader_method_set_default_texture_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_default_texture_parameter**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, texture:
`Texture<class_Texture>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_Shader_method_set_default_texture_parameter>`{.interpreted-text
role="ref"}

Sets the default texture to be used with a texture uniform. The default
is used if a texture is not set in the
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}.

\*\*Note:\*\* `name` must match the name of the uniform in the code
exactly.

\*\*Note:\*\* If the sampler array is used use `index` to access the
specified texture.
