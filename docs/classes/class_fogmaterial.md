github_url
:   hide

# FogMaterial {#class_FogMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A material that controls how volumetric fog is rendered, to be assigned
to a `FogVolume<class_FogVolume>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A `Material<class_Material>`{.interpreted-text role="ref"} resource that
can be used by `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}s to draw volumetric effects.

If you need more advanced effects, use a custom
`fog shader <../tutorials/shaders/shader_reference/fog_shader>`{.interpreted-text
role="doc"}.

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

:::: {#class_FogMaterial_property_albedo}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **albedo** =
`Color(1, 1, 1, 1)`
`🔗<class_FogMaterial_property_albedo>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_albedo**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_albedo**()

The single-scattering `Color<class_Color>`{.interpreted-text role="ref"}
of the `FogVolume<class_FogVolume>`{.interpreted-text role="ref"}.
Internally,
`albedo<class_FogMaterial_property_albedo>`{.interpreted-text
role="ref"} is converted into single-scattering, which is additively
blended with other `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}s and the
`Environment.volumetric_fog_albedo<class_Environment_property_volumetric_fog_albedo>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogMaterial_property_density}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **density** = `1.0`
`🔗<class_FogMaterial_property_density>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_density**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_density**()

The density of the `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}. Denser objects are more opaque, but may suffer from
under-sampling artifacts that look like stripes. Negative values can be
used to subtract fog from other
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}s or global
volumetric fog.

\*\*Note:\*\* Due to limited precision,
`density<class_FogMaterial_property_density>`{.interpreted-text
role="ref"} values between `-0.001` and `0.001` (exclusive) act like
`0.0`. This does not apply to
`Environment.volumetric_fog_density<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogMaterial_property_density_texture}
::: rst-class
classref-property
:::
::::

`Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
**density_texture**
`🔗<class_FogMaterial_property_density_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_density_texture**(value:
  `Texture3D<class_Texture3D>`{.interpreted-text role="ref"})
- `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
  **get_density_texture**()

The 3D texture that is used to scale the
`density<class_FogMaterial_property_density>`{.interpreted-text
role="ref"} of the `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}. This can be used to vary fog density within the
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} with any kind
of static pattern. For animated effects, consider using a custom
`fog shader <../tutorials/shaders/shader_reference/fog_shader>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogMaterial_property_edge_fade}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **edge_fade** = `0.1`
`🔗<class_FogMaterial_property_edge_fade>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edge_fade**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_edge_fade**()

The hardness of the edges of the
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}. A higher
value will result in softer edges, while a lower value will result in
harder edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogMaterial_property_emission}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **emission** =
`Color(0, 0, 0, 1)`
`🔗<class_FogMaterial_property_emission>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_emission**()

The `Color<class_Color>`{.interpreted-text role="ref"} of the light
emitted by the `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}. Emitted light will not cast light or shadows on other
objects, but can be useful for modulating the
`Color<class_Color>`{.interpreted-text role="ref"} of the
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} independently
from light sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogMaterial_property_height_falloff}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height_falloff** =
`0.0` `🔗<class_FogMaterial_property_height_falloff>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height_falloff**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_height_falloff**()

The rate by which the height-based fog decreases in density as height
increases in world space. A high falloff will result in a sharp
transition, while a low falloff will result in a smoother transition. A
value of `0.0` results in uniform-density fog. The height threshold is
determined by the height of the associated
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}.
