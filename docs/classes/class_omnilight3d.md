github_url
:   hide

::: {.meta keywords="point"}
:::

# OmniLight3D {#class_OmniLight3D}

**Inherits:** `Light3D<class_Light3D>`{.interpreted-text role="ref"}
**\<** `VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Omnidirectional light, such as a light bulb or a candle.

::: rst-class
classref-introduction-group
:::

## Description

An Omnidirectional light is a type of
`Light3D<class_Light3D>`{.interpreted-text role="ref"} that emits light
in all directions. The light is attenuated by distance and this
attenuation can be configured by changing its energy, radius, and
attenuation parameters.

\*\*Note:\*\* When using the Mobile rendering method, only 8 omni lights
can be displayed on each mesh resource. Attempting to display more than
8 omni lights on a single mesh resource will result in omni lights
flickering in and out as the camera moves. When using the Compatibility
rendering method, only 8 omni lights can be displayed on each mesh
resource by default, but this can be increased by adjusting
`ProjectSettings.rendering/limits/opengl/max_lights_per_object<class_ProjectSettings_property_rendering/limits/opengl/max_lights_per_object>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When using the Mobile or Compatibility rendering methods,
omni lights will only correctly affect meshes whose visibility AABB
intersects with the light\'s AABB. If using a shader to deform the mesh
in a way that makes it go outside its AABB,
`GeometryInstance3D.extra_cull_margin<class_GeometryInstance3D_property_extra_cull_margin>`{.interpreted-text
role="ref"} must be increased on the mesh. Otherwise, the light may not
be visible on the mesh.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D lights and shadows <../tutorials/3d/lights_and_shadows>`{.interpreted-text
  role="doc"}
- `Faking global illumination <../tutorials/3d/global_illumination/faking_global_illumination>`{.interpreted-text
  role="doc"}

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

:::: {#enum_OmniLight3D_ShadowMode}
::: rst-class
classref-enumeration
:::
::::

enum **ShadowMode**: `🔗<enum_OmniLight3D_ShadowMode>`{.interpreted-text
role="ref"}

:::: {#class_OmniLight3D_constant_SHADOW_DUAL_PARABOLOID}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowMode<enum_OmniLight3D_ShadowMode>`{.interpreted-text role="ref"}
**SHADOW_DUAL_PARABOLOID** = `0`

Shadows are rendered to a dual-paraboloid texture. Faster than
`SHADOW_CUBE<class_OmniLight3D_constant_SHADOW_CUBE>`{.interpreted-text
role="ref"}, but lower-quality.

:::: {#class_OmniLight3D_constant_SHADOW_CUBE}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowMode<enum_OmniLight3D_ShadowMode>`{.interpreted-text role="ref"}
**SHADOW_CUBE** = `1`

Shadows are rendered to a cubemap. Slower than
`SHADOW_DUAL_PARABOLOID<class_OmniLight3D_constant_SHADOW_DUAL_PARABOLOID>`{.interpreted-text
role="ref"}, but higher-quality.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OmniLight3D_property_omni_attenuation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **omni_attenuation**
= `1.0`
`🔗<class_OmniLight3D_property_omni_attenuation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

Controls the distance attenuation function for omnilights.

A value of `0.0` will maintain a constant brightness through most of the
range, but smoothly attenuate the light at the edge of the range. Use a
value of `2.0` for physically accurate lights as it results in the
proper inverse square attenutation.

\*\*Note:\*\* Setting attenuation to `2.0` or higher may result in
distant objects receiving minimal light, even within range. For example,
with a range of `4096`, an object at `100` units is attenuated by a
factor of `0.0001`. With a default brightness of `1`, the light would
not be visible at that distance.

\*\*Note:\*\* Using negative or values higher than `10.0` may lead to
unexpected results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OmniLight3D_property_omni_range}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **omni_range** =
`5.0` `🔗<class_OmniLight3D_property_omni_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The light\'s radius. Note that the effectively lit area may appear to be
smaller depending on the
`omni_attenuation<class_OmniLight3D_property_omni_attenuation>`{.interpreted-text
role="ref"} in use. No matter the
`omni_attenuation<class_OmniLight3D_property_omni_attenuation>`{.interpreted-text
role="ref"} in use, the light will never reach anything outside this
radius.

\*\*Note:\*\*
`omni_range<class_OmniLight3D_property_omni_range>`{.interpreted-text
role="ref"} is not affected by
`Node3D.scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"} (the light\'s scale or its parent\'s scale).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OmniLight3D_property_omni_shadow_mode}
::: rst-class
classref-property
:::
::::

`ShadowMode<enum_OmniLight3D_ShadowMode>`{.interpreted-text role="ref"}
**omni_shadow_mode** = `1`
`🔗<class_OmniLight3D_property_omni_shadow_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_mode**(value:
  `ShadowMode<enum_OmniLight3D_ShadowMode>`{.interpreted-text
  role="ref"})
- `ShadowMode<enum_OmniLight3D_ShadowMode>`{.interpreted-text
  role="ref"} **get_shadow_mode**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
