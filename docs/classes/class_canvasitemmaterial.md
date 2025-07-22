github_url
:   hide

# CanvasItemMaterial {#class_CanvasItemMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A material for `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

**CanvasItemMaterial**s provide a means of modifying the textures
associated with a CanvasItem. They specialize in describing blend and
lighting behaviors for textures. Use a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"} to
more fully customize a material\'s interactions with a
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}.

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

:::: {#enum_CanvasItemMaterial_BlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **BlendMode**:
`🔗<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text role="ref"}

:::: {#class_CanvasItemMaterial_constant_BLEND_MODE_MIX}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha
(opacity) value.

:::: {#class_CanvasItemMaterial_constant_BLEND_MODE_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_ADD** = `1`

Additive blending mode.

:::: {#class_CanvasItemMaterial_constant_BLEND_MODE_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

:::: {#class_CanvasItemMaterial_constant_BLEND_MODE_MUL}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

:::: {#class_CanvasItemMaterial_constant_BLEND_MODE_PREMULT_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_PREMULT_ALPHA** = `4`

Mix blending mode. Colors are assumed to be premultiplied by the alpha
(opacity) value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CanvasItemMaterial_LightMode}
::: rst-class
classref-enumeration
:::
::::

enum **LightMode**:
`🔗<enum_CanvasItemMaterial_LightMode>`{.interpreted-text role="ref"}

:::: {#class_CanvasItemMaterial_constant_LIGHT_MODE_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`LightMode<enum_CanvasItemMaterial_LightMode>`{.interpreted-text
role="ref"} **LIGHT_MODE_NORMAL** = `0`

Render the material using both light and non-light sensitive material
properties.

:::: {#class_CanvasItemMaterial_constant_LIGHT_MODE_UNSHADED}
::: rst-class
classref-enumeration-constant
:::
::::

`LightMode<enum_CanvasItemMaterial_LightMode>`{.interpreted-text
role="ref"} **LIGHT_MODE_UNSHADED** = `1`

Render the material as if there were no light.

:::: {#class_CanvasItemMaterial_constant_LIGHT_MODE_LIGHT_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightMode<enum_CanvasItemMaterial_LightMode>`{.interpreted-text
role="ref"} **LIGHT_MODE_LIGHT_ONLY** = `2`

Render the material as if there were only light.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CanvasItemMaterial_property_blend_mode}
::: rst-class
classref-property
:::
::::

`BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
role="ref"} **blend_mode** = `0`
`🔗<class_CanvasItemMaterial_property_blend_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_mode**(value:
  `BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
  role="ref"})
- `BlendMode<enum_CanvasItemMaterial_BlendMode>`{.interpreted-text
  role="ref"} **get_blend_mode**()

The manner in which a material\'s rendering is applied to underlying
textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItemMaterial_property_light_mode}
::: rst-class
classref-property
:::
::::

`LightMode<enum_CanvasItemMaterial_LightMode>`{.interpreted-text
role="ref"} **light_mode** = `0`
`🔗<class_CanvasItemMaterial_property_light_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_light_mode**(value:
  `LightMode<enum_CanvasItemMaterial_LightMode>`{.interpreted-text
  role="ref"})
- `LightMode<enum_CanvasItemMaterial_LightMode>`{.interpreted-text
  role="ref"} **get_light_mode**()

The manner in which material reacts to lighting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItemMaterial_property_particles_anim_h_frames}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**particles_anim_h_frames**
`🔗<class_CanvasItemMaterial_property_particles_anim_h_frames>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particles_anim_h_frames**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_particles_anim_h_frames**()

The number of columns in the spritesheet assigned as
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} for a
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} or
`CPUParticles2D<class_CPUParticles2D>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This property is only used and visible in the editor if
`particles_animation<class_CanvasItemMaterial_property_particles_animation>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItemMaterial_property_particles_anim_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **particles_anim_loop**
`🔗<class_CanvasItemMaterial_property_particles_anim_loop>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particles_anim_loop**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particles_anim_loop**()

If `true`, the particles animation will loop.

\*\*Note:\*\* This property is only used and visible in the editor if
`particles_animation<class_CanvasItemMaterial_property_particles_animation>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItemMaterial_property_particles_anim_v_frames}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**particles_anim_v_frames**
`🔗<class_CanvasItemMaterial_property_particles_anim_v_frames>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particles_anim_v_frames**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_particles_anim_v_frames**()

The number of rows in the spritesheet assigned as
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} for a
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} or
`CPUParticles2D<class_CPUParticles2D>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This property is only used and visible in the editor if
`particles_animation<class_CanvasItemMaterial_property_particles_animation>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItemMaterial_property_particles_animation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **particles_animation**
= `false`
`🔗<class_CanvasItemMaterial_property_particles_animation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particles_animation**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particles_animation**()

If `true`, enable spritesheet-based animation features when assigned to
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} and
`CPUParticles2D<class_CPUParticles2D>`{.interpreted-text role="ref"}
nodes. The
`ParticleProcessMaterial.anim_speed_max<class_ParticleProcessMaterial_property_anim_speed_max>`{.interpreted-text
role="ref"} or
`CPUParticles2D.anim_speed_max<class_CPUParticles2D_property_anim_speed_max>`{.interpreted-text
role="ref"} should also be set to a positive value for the animation to
play.

This property (and other `particles_anim_*` properties that depend on
it) has no effect on other types of nodes.
