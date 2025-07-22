github_url
:   hide

# GPUParticlesCollisionSphere3D {#class_GPUParticlesCollisionSphere3D}

**Inherits:**
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A sphere-shaped 3D particle collision shape affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

A sphere-shaped 3D particle collision shape affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

Particle collision shapes work in real-time and can be moved, rotated
and scaled during gameplay. Unlike attractors, non-uniform scaling of
collision shapes is *not* supported.

\*\*Note:\*\*
`ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} must be
`ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`{.interpreted-text
role="ref"} or
`ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>`{.interpreted-text
role="ref"} on the
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}\'s
process material for collision to work.

\*\*Note:\*\* Particle collision only affects
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

:::: {#class_GPUParticlesCollisionSphere3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `1.0`
`🔗<class_GPUParticlesCollisionSphere3D_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The collision sphere\'s radius in 3D units.
