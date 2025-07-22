github_url
:   hide

# VisualShaderNodeParticleMultiplyByAxisAngle {#class_VisualShaderNodeParticleMultiplyByAxisAngle}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader helper node for multiplying position and rotation of
particles.

::: rst-class
classref-introduction-group
:::

## Description

This node helps to multiply a position input vector by rotation using
specific axis. Intended to work with emitters.

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

:::: {#class_VisualShaderNodeParticleMultiplyByAxisAngle_property_degrees_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **degrees_mode** =
`true`
`🔗<class_VisualShaderNodeParticleMultiplyByAxisAngle_property_degrees_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_degrees_mode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_degrees_mode**()

If `true`, the angle will be interpreted in degrees instead of radians.
