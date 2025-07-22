github_url
:   hide

# VisualShaderNodeParticleAccelerator {#class_VisualShaderNodeParticleAccelerator}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that accelerates particles.

::: rst-class
classref-introduction-group
:::

## Description

Particle accelerator can be used in \"process\" step of particle shader.
It will accelerate the particles. Connect it to the Velocity output
port.

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

:::: {#enum_VisualShaderNodeParticleAccelerator_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**:
`🔗<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeParticleAccelerator_constant_MODE_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"} **MODE_LINEAR** = `0`

The particles will be accelerated based on their velocity.

:::: {#class_VisualShaderNodeParticleAccelerator_constant_MODE_RADIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"} **MODE_RADIAL** = `1`

The particles will be accelerated towards or away from the center.

:::: {#class_VisualShaderNodeParticleAccelerator_constant_MODE_TANGENTIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"} **MODE_TANGENTIAL** = `2`

The particles will be accelerated tangentially to the radius vector from
center to their position.

:::: {#class_VisualShaderNodeParticleAccelerator_constant_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"} **MODE_MAX** = `3`

Represents the size of the
`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeParticleAccelerator_property_mode}
::: rst-class
classref-property
:::
::::

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
role="ref"} **mode** = `0`
`🔗<class_VisualShaderNodeParticleAccelerator_property_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode**(value:
  `Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
  role="ref"})
- `Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`{.interpreted-text
  role="ref"} **get_mode**()

Defines in what manner the particles will be accelerated.
