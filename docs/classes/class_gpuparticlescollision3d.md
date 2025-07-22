github_url
:   hide

# GPUParticlesCollision3D {#class_GPUParticlesCollision3D}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`GPUParticlesCollisionBox3D<class_GPUParticlesCollisionBox3D>`{.interpreted-text
role="ref"},
`GPUParticlesCollisionHeightField3D<class_GPUParticlesCollisionHeightField3D>`{.interpreted-text
role="ref"},
`GPUParticlesCollisionSDF3D<class_GPUParticlesCollisionSDF3D>`{.interpreted-text
role="ref"},
`GPUParticlesCollisionSphere3D<class_GPUParticlesCollisionSphere3D>`{.interpreted-text
role="ref"}

Abstract base class for 3D particle collision shapes affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

Particle collision shapes can be used to make particles stop or bounce
against them.

Particle collision shapes work in real-time and can be moved, rotated
and scaled during gameplay. Unlike attractors, non-uniform scaling of
collision shapes is *not* supported.

Particle collision shapes can be temporarily disabled by hiding them.

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

\*\*Note:\*\* Particles pushed by a collider that is being moved will
not be interpolated, which can result in visible stuttering. This can be
alleviated by setting
`GPUParticles3D.fixed_fps<class_GPUParticles3D_property_fixed_fps>`{.interpreted-text
role="ref"} to `0` or a value that matches or exceeds the target
framerate.

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

:::: {#class_GPUParticlesCollision3D_property_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **cull_mask** =
`4294967295`
`🔗<class_GPUParticlesCollision3D_property_cull_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_cull_mask**()

The particle rendering layers
(`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"}) that will be affected by the collision shape. By default,
all particles that have
`ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} set to
`ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`{.interpreted-text
role="ref"} or
`ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>`{.interpreted-text
role="ref"} will be affected by a collision shape.

After configuring particle nodes accordingly, specific layers can be
unchecked to prevent certain particles from being affected by colliders.
For example, this can be used if you\'re using a collider as part of a
spell effect but don\'t want the collider to affect unrelated weather
particles at the same position.

Particle collision can also be disabled on a per-process material basis
by setting
`ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} on the
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
node.
