github_url
:   hide

# GPUParticlesCollisionSDF3D {#class_GPUParticlesCollisionSDF3D}

**Inherits:**
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A baked signed distance field 3D particle collision shape affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

A baked signed distance field 3D particle collision shape affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

Signed distance fields (SDF) allow for efficiently representing
approximate collision shapes for convex and concave objects of any
shape. This is more flexible than
`GPUParticlesCollisionHeightField3D<class_GPUParticlesCollisionHeightField3D>`{.interpreted-text
role="ref"}, but it requires a baking step.

\*\*Baking:\*\* The signed distance field texture can be baked by
selecting the **GPUParticlesCollisionSDF3D** node in the editor, then
clicking **Bake SDF** at the top of the 3D viewport. Any *visible*
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}s
within the
`size<class_GPUParticlesCollisionSDF3D_property_size>`{.interpreted-text
role="ref"} will be taken into account for baking, regardless of their
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Baking a **GPUParticlesCollisionSDF3D**\'s
`texture<class_GPUParticlesCollisionSDF3D_property_texture>`{.interpreted-text
role="ref"} is only possible within the editor, as there is no bake
method exposed for use in exported projects. However, it\'s still
possible to load pre-baked
`Texture3D<class_Texture3D>`{.interpreted-text role="ref"}s into its
`texture<class_GPUParticlesCollisionSDF3D_property_texture>`{.interpreted-text
role="ref"} property in an exported project.

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
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_GPUParticlesCollisionSDF3D_Resolution}
::: rst-class
classref-enumeration
:::
::::

enum **Resolution**:
`🔗<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"}

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_16}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_16** = `0`

Bake a 16×16×16 signed distance field. This is the fastest option, but
also the least precise.

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_32}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_32** = `1`

Bake a 32×32×32 signed distance field.

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_64}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_64** = `2`

Bake a 64×64×64 signed distance field.

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_128}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_128** = `3`

Bake a 128×128×128 signed distance field.

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_256}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_256** = `4`

Bake a 256×256×256 signed distance field.

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_512}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_512** = `5`

Bake a 512×512×512 signed distance field. This is the slowest option,
but also the most precise.

:::: {#class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_MAX** = `6`

Represents the size of the
`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GPUParticlesCollisionSDF3D_property_bake_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bake_mask** =
`4294967295`
`🔗<class_GPUParticlesCollisionSDF3D_property_bake_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bake_mask**()

The visual layers to account for when baking the particle collision SDF.
Only `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"}s whose
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} match with this
`bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>`{.interpreted-text
role="ref"} will be included in the generated particle collision SDF. By
default, all objects are taken into account for the particle collision
SDF baking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionSDF3D_property_resolution}
::: rst-class
classref-property
:::
::::

`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
role="ref"} **resolution** = `2`
`🔗<class_GPUParticlesCollisionSDF3D_property_resolution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_resolution**(value:
  `Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
  role="ref"})
- `Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>`{.interpreted-text
  role="ref"} **get_resolution**()

The bake resolution to use for the signed distance field
`texture<class_GPUParticlesCollisionSDF3D_property_texture>`{.interpreted-text
role="ref"}. The texture must be baked again for changes to the
`resolution<class_GPUParticlesCollisionSDF3D_property_resolution>`{.interpreted-text
role="ref"} property to be effective. Higher resolutions have a greater
performance cost and take more time to bake. Higher resolutions also
result in larger baked textures, leading to increased VRAM and storage
space requirements. To improve performance and reduce bake times, use
the lowest resolution possible for the object you\'re representing the
collision of.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionSDF3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(2, 2, 2)`
`🔗<class_GPUParticlesCollisionSDF3D_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The collision SDF\'s size in 3D units. To improve SDF quality, the
`size<class_GPUParticlesCollisionSDF3D_property_size>`{.interpreted-text
role="ref"} should be set as small as possible while covering the parts
of the scene you need.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionSDF3D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture3D<class_Texture3D>`{.interpreted-text role="ref"} **texture**
`🔗<class_GPUParticlesCollisionSDF3D_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture3D<class_Texture3D>`{.interpreted-text
  role="ref"})
- `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
  **get_texture**()

The 3D texture representing the signed distance field.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionSDF3D_property_thickness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **thickness** = `1.0`
`🔗<class_GPUParticlesCollisionSDF3D_property_thickness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_thickness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_thickness**()

The collision shape\'s thickness. Unlike other particle colliders,
**GPUParticlesCollisionSDF3D** is actually hollow on the inside.
`thickness<class_GPUParticlesCollisionSDF3D_property_thickness>`{.interpreted-text
role="ref"} can be increased to prevent particles from tunneling through
the collision shape at high speeds, or when the
**GPUParticlesCollisionSDF3D** is moved.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_bake_mask_value**(layer_number: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bake_mask_value**(layer_number: `int<class_int>`{.interpreted-text
role="ref"}, value: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.
