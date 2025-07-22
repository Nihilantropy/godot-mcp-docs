github_url
:   hide

# GPUParticlesAttractorVectorField3D {#class_GPUParticlesAttractorVectorField3D}

**Inherits:**
`GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A box-shaped attractor with varying directions and strengths defined in
it that influences particles from
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

A box-shaped attractor with varying directions and strengths defined in
it that influences particles from
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

Unlike
`GPUParticlesAttractorBox3D<class_GPUParticlesAttractorBox3D>`{.interpreted-text
role="ref"}, **GPUParticlesAttractorVectorField3D** uses a
`texture<class_GPUParticlesAttractorVectorField3D_property_texture>`{.interpreted-text
role="ref"} to affect attraction strength within the box. This can be
used to create complex attraction scenarios where particles travel in
different directions depending on their location. This can be useful for
weather effects such as sandstorms.

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

:::: {#class_GPUParticlesAttractorVectorField3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(2, 2, 2)`
`🔗<class_GPUParticlesAttractorVectorField3D_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The size of the vector field box in 3D units.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesAttractorVectorField3D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture3D<class_Texture3D>`{.interpreted-text role="ref"} **texture**
`🔗<class_GPUParticlesAttractorVectorField3D_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture3D<class_Texture3D>`{.interpreted-text
  role="ref"})
- `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
  **get_texture**()

The 3D texture to be used. Values are linearly interpolated between the
texture\'s pixels.

\*\*Note:\*\* To get better performance, the 3D texture\'s resolution
should reflect the
`size<class_GPUParticlesAttractorVectorField3D_property_size>`{.interpreted-text
role="ref"} of the attractor. Since particle attraction is usually
low-frequency data, the texture can be kept at a low resolution such as
64×64×64.
