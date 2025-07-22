github_url
:   hide

# ShaderMaterial {#class_ShaderMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A material defined by a custom `Shader<class_Shader>`{.interpreted-text
role="ref"} program and the values of its shader parameters.

::: rst-class
classref-introduction-group
:::

## Description

A material that uses a custom `Shader<class_Shader>`{.interpreted-text
role="ref"} program to render visual items (canvas items, meshes, skies,
fog), or to process particles. Compared to other materials,
**ShaderMaterial** gives deeper control over the generated shader code.
For more information, see the shaders documentation index below.

Multiple **ShaderMaterial**s can use the same shader and configure
different values for the shader uniforms.

\*\*Note:\*\* For performance reasons, the
`Resource.changed<class_Resource_signal_changed>`{.interpreted-text
role="ref"} signal is only emitted when the
`Resource.resource_name<class_Resource_property_resource_name>`{.interpreted-text
role="ref"} changes. Only in editor, it is also emitted for
`shader<class_ShaderMaterial_property_shader>`{.interpreted-text
role="ref"} changes.

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

## Property Descriptions

:::: {#class_ShaderMaterial_property_shader}
::: rst-class
classref-property
:::
::::

`Shader<class_Shader>`{.interpreted-text role="ref"} **shader**
`🔗<class_ShaderMaterial_property_shader>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shader**(value: `Shader<class_Shader>`{.interpreted-text
  role="ref"})
- `Shader<class_Shader>`{.interpreted-text role="ref"} **get_shader**()

The `Shader<class_Shader>`{.interpreted-text role="ref"} program used to
render this material.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ShaderMaterial_method_get_shader_parameter}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_shader_parameter**(param:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShaderMaterial_method_get_shader_parameter>`{.interpreted-text
role="ref"}

Returns the current value set for this material of a uniform in the
shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShaderMaterial_method_set_shader_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_shader_parameter**(param:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_ShaderMaterial_method_set_shader_parameter>`{.interpreted-text
role="ref"}

Changes the value set for this material of a uniform in the shader.

\*\*Note:\*\* `param` is case-sensitive and must match the name of the
uniform in the code exactly (not the capitalized name in the inspector).

\*\*Note:\*\* Changes to the shader uniform will be effective on all
instances using this **ShaderMaterial**. To prevent this, use
per-instance uniforms with
`GeometryInstance3D.set_instance_shader_parameter()<class_GeometryInstance3D_method_set_instance_shader_parameter>`{.interpreted-text
role="ref"} or duplicate the **ShaderMaterial** resource using
`Resource.duplicate()<class_Resource_method_duplicate>`{.interpreted-text
role="ref"}. Per-instance uniforms allow for better shader reuse and are
therefore faster, so they should be preferred over duplicating the
**ShaderMaterial** when possible.
