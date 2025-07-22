github_url
:   hide

# GPUParticlesAttractor3D {#class_GPUParticlesAttractor3D}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`GPUParticlesAttractorBox3D<class_GPUParticlesAttractorBox3D>`{.interpreted-text
role="ref"},
`GPUParticlesAttractorSphere3D<class_GPUParticlesAttractorSphere3D>`{.interpreted-text
role="ref"},
`GPUParticlesAttractorVectorField3D<class_GPUParticlesAttractorVectorField3D>`{.interpreted-text
role="ref"}

Abstract base class for 3D particle attractors.

::: rst-class
classref-introduction-group
:::

## Description

Particle attractors can be used to attract particles towards the
attractor\'s origin, or to push them away from the attractor\'s origin.

Particle attractors work in real-time and can be moved, rotated and
scaled during gameplay. Unlike collision shapes, non-uniform scaling of
attractors is also supported.

Attractors can be temporarily disabled by hiding them, or by setting
their
`strength<class_GPUParticlesAttractor3D_property_strength>`{.interpreted-text
role="ref"} to `0.0`.

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

:::: {#class_GPUParticlesAttractor3D_property_attenuation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **attenuation** =
`1.0`
`🔗<class_GPUParticlesAttractor3D_property_attenuation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attenuation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_attenuation**()

The particle attractor\'s attenuation. Higher values result in more
gradual pushing of particles as they come closer to the attractor\'s
origin. Zero or negative values will cause particles to be pushed very
fast as soon as the touch the attractor\'s edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesAttractor3D_property_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **cull_mask** =
`4294967295`
`🔗<class_GPUParticlesAttractor3D_property_cull_mask>`{.interpreted-text
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
role="ref"}) that will be affected by the attractor. By default, all
particles are affected by an attractor.

After configuring particle nodes accordingly, specific layers can be
unchecked to prevent certain particles from being affected by
attractors. For example, this can be used if you\'re using an attractor
as part of a spell effect but don\'t want the attractor to affect
unrelated weather particles at the same position.

Particle attraction can also be disabled on a per-process material basis
by setting
`ParticleProcessMaterial.attractor_interaction_enabled<class_ParticleProcessMaterial_property_attractor_interaction_enabled>`{.interpreted-text
role="ref"} on the
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesAttractor3D_property_directionality}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **directionality** =
`0.0`
`🔗<class_GPUParticlesAttractor3D_property_directionality>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_directionality**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_directionality**()

Adjusts how directional the attractor is. At `0.0`, the attractor is not
directional at all: it will attract particles towards its center. At
`1.0`, the attractor is fully directional: particles will always be
pushed towards local -Z (or +Z if
`strength<class_GPUParticlesAttractor3D_property_strength>`{.interpreted-text
role="ref"} is negative).

\*\*Note:\*\* If
`directionality<class_GPUParticlesAttractor3D_property_directionality>`{.interpreted-text
role="ref"} is greater than `0.0`, the direction in which particles are
pushed can be changed by rotating the **GPUParticlesAttractor3D** node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesAttractor3D_property_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **strength** = `1.0`
`🔗<class_GPUParticlesAttractor3D_property_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_strength**()

Adjusts the strength of the attractor. If
`strength<class_GPUParticlesAttractor3D_property_strength>`{.interpreted-text
role="ref"} is negative, particles will be pushed in the opposite
direction. Particles will be pushed *away* from the attractor\'s origin
if
`directionality<class_GPUParticlesAttractor3D_property_directionality>`{.interpreted-text
role="ref"} is `0.0`, or towards local +Z if
`directionality<class_GPUParticlesAttractor3D_property_directionality>`{.interpreted-text
role="ref"} is greater than `0.0`.
