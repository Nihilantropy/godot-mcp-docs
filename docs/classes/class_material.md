github_url
:   hide

# Material {#class_Material}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`CanvasItemMaterial<class_CanvasItemMaterial>`{.interpreted-text
role="ref"}, `FogMaterial<class_FogMaterial>`{.interpreted-text
role="ref"},
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"},
`ParticleProcessMaterial<class_ParticleProcessMaterial>`{.interpreted-text
role="ref"},
`PhysicalSkyMaterial<class_PhysicalSkyMaterial>`{.interpreted-text
role="ref"},
`PlaceholderMaterial<class_PlaceholderMaterial>`{.interpreted-text
role="ref"},
`ProceduralSkyMaterial<class_ProceduralSkyMaterial>`{.interpreted-text
role="ref"}, `ShaderMaterial<class_ShaderMaterial>`{.interpreted-text
role="ref"}

Virtual base class for applying visual properties to an object, such as
color and roughness.

::: rst-class
classref-introduction-group
:::

## Description

**Material** is a base resource used for coloring and shading geometry.
All materials inherit from it and almost all
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
derived nodes carry a **Material**. A few flags and parameters are
shared between all material types and are configured here.

Importantly, you can inherit from **Material** to create your own custom
material type in script or in GDExtension.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Material Testers
  Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

## Constants

:::: {#class_Material_constant_RENDER_PRIORITY_MAX}
::: rst-class
classref-constant
:::
::::

**RENDER_PRIORITY_MAX** = `127`
`🔗<class_Material_constant_RENDER_PRIORITY_MAX>`{.interpreted-text
role="ref"}

Maximum value for the
`render_priority<class_Material_property_render_priority>`{.interpreted-text
role="ref"} parameter.

:::: {#class_Material_constant_RENDER_PRIORITY_MIN}
::: rst-class
classref-constant
:::
::::

**RENDER_PRIORITY_MIN** = `-128`
`🔗<class_Material_constant_RENDER_PRIORITY_MIN>`{.interpreted-text
role="ref"}

Minimum value for the
`render_priority<class_Material_property_render_priority>`{.interpreted-text
role="ref"} parameter.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Material_property_next_pass}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **next_pass**
`🔗<class_Material_property_next_pass>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_next_pass**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_next_pass**()

Sets the **Material** to be used for the next pass. This renders the
object again using a different material.

\*\*Note:\*\*
`next_pass<class_Material_property_next_pass>`{.interpreted-text
role="ref"} materials are not necessarily drawn immediately after the
source **Material**. Draw order is determined by material properties,
`render_priority<class_Material_property_render_priority>`{.interpreted-text
role="ref"}, and distance to camera.

\*\*Note:\*\* This only applies to
`StandardMaterial3D<class_StandardMaterial3D>`{.interpreted-text
role="ref"}s and
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}s
with type \"Spatial\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Material_property_render_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **render_priority**
`🔗<class_Material_property_render_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_render_priority**()

Sets the render priority for objects in 3D scenes. Higher priority
objects will be sorted in front of lower priority objects. In other
words, all objects with
`render_priority<class_Material_property_render_priority>`{.interpreted-text
role="ref"} `1` will render on top of all objects with
`render_priority<class_Material_property_render_priority>`{.interpreted-text
role="ref"} `0`.

\*\*Note:\*\* This only applies to
`StandardMaterial3D<class_StandardMaterial3D>`{.interpreted-text
role="ref"}s and
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}s
with type \"Spatial\".

\*\*Note:\*\* This will not impact how transparent objects are sorted
relative to opaque objects or how dynamic meshes will be sorted relative
to other opaque meshes. This is because all transparent objects are
drawn after all opaque objects and all dynamic opaque meshes are drawn
before other opaque meshes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Material_private_method__can_do_next_pass}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_do_next_pass**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Material_private_method__can_do_next_pass>`{.interpreted-text
role="ref"}

Only exposed for the purpose of overriding. You cannot call this
function directly. Used internally to determine if
`next_pass<class_Material_property_next_pass>`{.interpreted-text
role="ref"} should be shown in the editor or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Material_private_method__can_use_render_priority}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_use_render_priority**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Material_private_method__can_use_render_priority>`{.interpreted-text
role="ref"}

Only exposed for the purpose of overriding. You cannot call this
function directly. Used internally to determine if
`render_priority<class_Material_property_render_priority>`{.interpreted-text
role="ref"} should be shown in the editor or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Material_private_method__get_shader_mode}
::: rst-class
classref-method
:::
::::

`Mode<enum_Shader_Mode>`{.interpreted-text role="ref"}
**\_get_shader_mode**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Material_private_method__get_shader_mode>`{.interpreted-text
role="ref"}

Only exposed for the purpose of overriding. You cannot call this
function directly. Used internally by various editor tools.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Material_private_method__get_shader_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_get_shader_rid**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Material_private_method__get_shader_rid>`{.interpreted-text
role="ref"}

Only exposed for the purpose of overriding. You cannot call this
function directly. Used internally by various editor tools. Used to
access the RID of the **Material**\'s
`Shader<class_Shader>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Material_method_create_placeholder}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Material_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderMaterial<class_PlaceholderMaterial>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Material_method_inspect_native_shader_code}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**inspect_native_shader_code**()
`🔗<class_Material_method_inspect_native_shader_code>`{.interpreted-text
role="ref"}

Only available when running in the editor. Opens a popup that visualizes
the generated shader code, including all variants and internal shader
code. See also
`Shader.inspect_native_shader_code()<class_Shader_method_inspect_native_shader_code>`{.interpreted-text
role="ref"}.
