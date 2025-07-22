github_url
:   hide

# VisualShaderNodeParticleMeshEmitter {#class_VisualShaderNodeParticleMeshEmitter}

**Inherits:**
`VisualShaderNodeParticleEmitter<class_VisualShaderNodeParticleEmitter>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that makes particles emitted in a shape defined by
a `Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

`VisualShaderNodeParticleEmitter<class_VisualShaderNodeParticleEmitter>`{.interpreted-text
role="ref"} that makes the particles emitted in a shape of the assigned
`mesh<class_VisualShaderNodeParticleMeshEmitter_property_mesh>`{.interpreted-text
role="ref"}. It will emit from the mesh\'s surfaces, either all or only
the specified one.

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

:::: {#class_VisualShaderNodeParticleMeshEmitter_property_mesh}
::: rst-class
classref-property
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **mesh**
`🔗<class_VisualShaderNodeParticleMeshEmitter_property_mesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
- `Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_mesh**()

The `Mesh<class_Mesh>`{.interpreted-text role="ref"} that defines
emission shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeParticleMeshEmitter_property_surface_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **surface_index** = `0`
`🔗<class_VisualShaderNodeParticleMeshEmitter_property_surface_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_surface_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_surface_index**()

Index of the surface that emits particles.
`use_all_surfaces<class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces>`{.interpreted-text
role="ref"} must be `false` for this to take effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_all_surfaces** =
`true`
`🔗<class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_all_surfaces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_use_all_surfaces**()

If `true`, the particles will emit from all surfaces of the mesh.
