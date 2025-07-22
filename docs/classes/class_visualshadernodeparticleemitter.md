github_url
:   hide

# VisualShaderNodeParticleEmitter {#class_VisualShaderNodeParticleEmitter}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeParticleBoxEmitter<class_VisualShaderNodeParticleBoxEmitter>`{.interpreted-text
role="ref"},
`VisualShaderNodeParticleMeshEmitter<class_VisualShaderNodeParticleMeshEmitter>`{.interpreted-text
role="ref"},
`VisualShaderNodeParticleRingEmitter<class_VisualShaderNodeParticleRingEmitter>`{.interpreted-text
role="ref"},
`VisualShaderNodeParticleSphereEmitter<class_VisualShaderNodeParticleSphereEmitter>`{.interpreted-text
role="ref"}

A base class for particle emitters.

::: rst-class
classref-introduction-group
:::

## Description

Particle emitter nodes can be used in \"start\" step of particle shaders
and they define the starting position of the particles. Connect them to
the Position output port.

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

:::: {#class_VisualShaderNodeParticleEmitter_property_mode_2d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **mode_2d** = `false`
`🔗<class_VisualShaderNodeParticleEmitter_property_mode_2d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode_2d**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_mode_2d**()

If `true`, the result of this emitter is projected to 2D space. By
default it is `false` and meant for use in 3D space.
