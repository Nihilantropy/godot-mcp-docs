github_url
:   hide

# GPUParticlesAttractorBox3D {#class_GPUParticlesAttractorBox3D}

**Inherits:**
`GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A box-shaped attractor that influences particles from
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

A box-shaped attractor that influences particles from
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes. Can be used to attract particles towards its origin, or to push
them away from its origin.

Particle attractors work in real-time and can be moved, rotated and
scaled during gameplay. Unlike collision shapes, non-uniform scaling of
attractors is also supported.

\*\*Note:\*\* Particle attractors only affect
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"},
not `CPUParticles3D<class_CPUParticles3D>`{.interpreted-text
role="ref"}.

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

:::: {#class_GPUParticlesAttractorBox3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(2, 2, 2)`
`🔗<class_GPUParticlesAttractorBox3D_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The attractor box\'s size in 3D units.
