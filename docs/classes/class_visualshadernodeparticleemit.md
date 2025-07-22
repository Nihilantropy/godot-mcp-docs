github_url
:   hide

# VisualShaderNodeParticleEmit {#class_VisualShaderNodeParticleEmit}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that forces to emit a particle from a sub-emitter.

::: rst-class
classref-introduction-group
:::

## Description

This node internally calls `emit_subparticle` shader method. It will
emit a particle from the configured sub-emitter and also allows to
customize how its emitted. Requires a sub-emitter assigned to the
particles node with this shader.

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

## Enumerations

:::: {#enum_VisualShaderNodeParticleEmit_EmitFlags}
::: rst-class
classref-enumeration
:::
::::

enum **EmitFlags**:
`🔗<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_POSITION}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"} **EMIT_FLAG_POSITION** = `1`

If enabled, the particle starts with the position defined by this node.

:::: {#class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_ROT_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"} **EMIT_FLAG_ROT_SCALE** = `2`

If enabled, the particle starts with the rotation and scale defined by
this node.

:::: {#class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"} **EMIT_FLAG_VELOCITY** = `4`

If enabled,the particle starts with the velocity defined by this node.

:::: {#class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"} **EMIT_FLAG_COLOR** = `8`

If enabled, the particle starts with the color defined by this node.

:::: {#class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"} **EMIT_FLAG_CUSTOM** = `16`

If enabled, the particle starts with the `CUSTOM` data defined by this
node.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeParticleEmit_property_flags}
::: rst-class
classref-property
:::
::::

`EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
role="ref"} **flags** = `31`
`🔗<class_VisualShaderNodeParticleEmit_property_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flags**(value:
  `EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
  role="ref"})
- `EmitFlags<enum_VisualShaderNodeParticleEmit_EmitFlags>`{.interpreted-text
  role="ref"} **get_flags**()

Flags used to override the properties defined in the sub-emitter\'s
process material.
