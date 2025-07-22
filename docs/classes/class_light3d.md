github_url
:   hide

# Light3D {#class_Light3D}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}, `OmniLight3D<class_OmniLight3D>`{.interpreted-text
role="ref"}, `SpotLight3D<class_SpotLight3D>`{.interpreted-text
role="ref"}

Provides a base class for different kinds of light nodes.

::: rst-class
classref-introduction-group
:::

## Description

Light3D is the *abstract* base class for light nodes. As it can\'t be
instantiated, it shouldn\'t be used directly. Other types of light nodes
inherit from it. Light3D contains the common variables and parameters
used for lighting.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D lights and shadows <../tutorials/3d/lights_and_shadows>`{.interpreted-text
  role="doc"}
- `Faking global illumination <../tutorials/3d/global_illumination/faking_global_illumination>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#enum_Light3D_Param}
::: rst-class
classref-enumeration
:::
::::

enum **Param**: `🔗<enum_Light3D_Param>`{.interpreted-text role="ref"}

:::: {#class_Light3D_constant_PARAM_ENERGY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_ENERGY** = `0`

Constant for accessing
`light_energy<class_Light3D_property_light_energy>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_INDIRECT_ENERGY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_INDIRECT_ENERGY** = `1`

Constant for accessing
`light_indirect_energy<class_Light3D_property_light_indirect_energy>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_VOLUMETRIC_FOG_ENERGY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_VOLUMETRIC_FOG_ENERGY** = `2`

Constant for accessing
`light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SPECULAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SPECULAR** = `3`

Constant for accessing
`light_specular<class_Light3D_property_light_specular>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_RANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_RANGE** = `4`

Constant for accessing
`OmniLight3D.omni_range<class_OmniLight3D_property_omni_range>`{.interpreted-text
role="ref"} or
`SpotLight3D.spot_range<class_SpotLight3D_property_spot_range>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"} **PARAM_SIZE**
= `5`

Constant for accessing
`light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_ATTENUATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_ATTENUATION** = `6`

Constant for accessing
`OmniLight3D.omni_attenuation<class_OmniLight3D_property_omni_attenuation>`{.interpreted-text
role="ref"} or
`SpotLight3D.spot_attenuation<class_SpotLight3D_property_spot_attenuation>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SPOT_ANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SPOT_ANGLE** = `7`

Constant for accessing
`SpotLight3D.spot_angle<class_SpotLight3D_property_spot_angle>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SPOT_ATTENUATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SPOT_ATTENUATION** = `8`

Constant for accessing
`SpotLight3D.spot_angle_attenuation<class_SpotLight3D_property_spot_angle_attenuation>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_MAX_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_MAX_DISTANCE** = `9`

Constant for accessing
`DirectionalLight3D.directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_SPLIT_1_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_SPLIT_1_OFFSET** = `10`

Constant for accessing
`DirectionalLight3D.directional_shadow_split_1<class_DirectionalLight3D_property_directional_shadow_split_1>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_SPLIT_2_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_SPLIT_2_OFFSET** = `11`

Constant for accessing
`DirectionalLight3D.directional_shadow_split_2<class_DirectionalLight3D_property_directional_shadow_split_2>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_SPLIT_3_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_SPLIT_3_OFFSET** = `12`

Constant for accessing
`DirectionalLight3D.directional_shadow_split_3<class_DirectionalLight3D_property_directional_shadow_split_3>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_FADE_START}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_FADE_START** = `13`

Constant for accessing
`DirectionalLight3D.directional_shadow_fade_start<class_DirectionalLight3D_property_directional_shadow_fade_start>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_NORMAL_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_NORMAL_BIAS** = `14`

Constant for accessing
`shadow_normal_bias<class_Light3D_property_shadow_normal_bias>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_BIAS** = `15`

Constant for accessing
`shadow_bias<class_Light3D_property_shadow_bias>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_PANCAKE_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_PANCAKE_SIZE** = `16`

Constant for accessing
`DirectionalLight3D.directional_shadow_pancake_size<class_DirectionalLight3D_property_directional_shadow_pancake_size>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_OPACITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_OPACITY** = `17`

Constant for accessing
`shadow_opacity<class_Light3D_property_shadow_opacity>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_SHADOW_BLUR}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_SHADOW_BLUR** = `18`

Constant for accessing
`shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_TRANSMITTANCE_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_TRANSMITTANCE_BIAS** = `19`

Constant for accessing
`shadow_transmittance_bias<class_Light3D_property_shadow_transmittance_bias>`{.interpreted-text
role="ref"}.

:::: {#class_Light3D_constant_PARAM_INTENSITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"}
**PARAM_INTENSITY** = `20`

Constant for accessing
`light_intensity_lumens<class_Light3D_property_light_intensity_lumens>`{.interpreted-text
role="ref"} and
`light_intensity_lux<class_Light3D_property_light_intensity_lux>`{.interpreted-text
role="ref"}. Only used when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is `true`.

:::: {#class_Light3D_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Light3D_Param>`{.interpreted-text role="ref"} **PARAM_MAX**
= `21`

Represents the size of the `Param<enum_Light3D_Param>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Light3D_BakeMode}
::: rst-class
classref-enumeration
:::
::::

enum **BakeMode**: `🔗<enum_Light3D_BakeMode>`{.interpreted-text
role="ref"}

:::: {#class_Light3D_constant_BAKE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeMode<enum_Light3D_BakeMode>`{.interpreted-text role="ref"}
**BAKE_DISABLED** = `0`

Light is ignored when baking. This is the fastest mode, but the light
will not be taken into account when baking global illumination. This
mode should generally be used for dynamic lights that change quickly, as
the effect of global illumination is less noticeable on those lights.

\*\*Note:\*\* Hiding a light does *not* affect baking
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. Hiding a
light will still affect baking
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} and SDFGI (see
`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}).

:::: {#class_Light3D_constant_BAKE_STATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeMode<enum_Light3D_BakeMode>`{.interpreted-text role="ref"}
**BAKE_STATIC** = `1`

Light is taken into account in static baking
(`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"},
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}, SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"})). The light can be moved around or modified, but its global
illumination will not update in real-time. This is suitable for subtle
changes (such as flickering torches), but generally not large changes
such as toggling a light on and off.

\*\*Note:\*\* The light is not baked in
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} if
`editor_only<class_Light3D_property_editor_only>`{.interpreted-text
role="ref"} is `true`.

:::: {#class_Light3D_constant_BAKE_DYNAMIC}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeMode<enum_Light3D_BakeMode>`{.interpreted-text role="ref"}
**BAKE_DYNAMIC** = `2`

Light is taken into account in dynamic baking
(`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} and SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) only). The light can be moved around or modified with
global illumination updating in real-time. The light\'s global
illumination appearance will be slightly different compared to
`BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>`{.interpreted-text
role="ref"}. This has a greater performance cost compared to
`BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>`{.interpreted-text
role="ref"}. When using SDFGI, the update speed of dynamic lights is
affected by
`ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Light3D_property_distance_fade_begin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_fade_begin** = `40.0`
`🔗<class_Light3D_property_distance_fade_begin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distance_fade_begin**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_distance_fade_begin**()

The distance from the camera at which the light begins to fade away (in
3D units).

\*\*Note:\*\* Only effective for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_distance_fade_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**distance_fade_enabled** = `false`
`🔗<class_Light3D_property_distance_fade_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_distance_fade**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_distance_fade_enabled**()

If `true`, the light will smoothly fade away when far from the active
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} starting at
`distance_fade_begin<class_Light3D_property_distance_fade_begin>`{.interpreted-text
role="ref"}. This acts as a form of level of detail (LOD). The light
will fade out over
`distance_fade_begin<class_Light3D_property_distance_fade_begin>`{.interpreted-text
role="ref"} +
`distance_fade_length<class_Light3D_property_distance_fade_length>`{.interpreted-text
role="ref"}, after which it will be culled and not sent to the shader at
all. Use this to reduce the number of active lights in a scene and thus
improve performance.

\*\*Note:\*\* Only effective for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_distance_fade_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_fade_length** = `10.0`
`🔗<class_Light3D_property_distance_fade_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distance_fade_length**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_distance_fade_length**()

Distance over which the light and its shadow fades. The light\'s energy
and shadow\'s opacity is progressively reduced over this distance and is
completely invisible at the end.

\*\*Note:\*\* Only effective for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_distance_fade_shadow}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_fade_shadow** = `50.0`
`🔗<class_Light3D_property_distance_fade_shadow>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distance_fade_shadow**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_distance_fade_shadow**()

The distance from the camera at which the light\'s shadow cuts off (in
3D units). Set this to a value lower than
`distance_fade_begin<class_Light3D_property_distance_fade_begin>`{.interpreted-text
role="ref"} +
`distance_fade_length<class_Light3D_property_distance_fade_length>`{.interpreted-text
role="ref"} to further improve performance, as shadow rendering is often
more expensive than light rendering itself.

\*\*Note:\*\* Only effective for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}, and only
when
`shadow_enabled<class_Light3D_property_shadow_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_editor_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editor_only** =
`false` `🔗<class_Light3D_property_editor_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editor_only**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_editor_only**()

If `true`, the light only appears in the editor and will not be visible
at runtime. If `true`, the light will never be baked in
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} regardless
of its
`light_bake_mode<class_Light3D_property_light_bake_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_angular_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**light_angular_distance** = `0.0`
`🔗<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The light\'s angular size in degrees. Increasing this will make shadows
softer at greater distances (also called percentage-closer soft shadows,
or PCSS). Only available for
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s. For reference, the Sun from the Earth is approximately
`0.5`. Increasing this value above `0.0` for lights with shadows enabled
will have a noticeable performance cost due to PCSS.

\*\*Note:\*\*
`light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"} is not affected by
`Node3D.scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"} (the light\'s scale or its parent\'s scale).

\*\*Note:\*\* PCSS for directional lights is only supported in the
Forward+ rendering method, not Mobile or Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_bake_mode}
::: rst-class
classref-property
:::
::::

`BakeMode<enum_Light3D_BakeMode>`{.interpreted-text role="ref"}
**light_bake_mode** = `2`
`🔗<class_Light3D_property_light_bake_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_mode**(value:
  `BakeMode<enum_Light3D_BakeMode>`{.interpreted-text role="ref"})
- `BakeMode<enum_Light3D_BakeMode>`{.interpreted-text role="ref"}
  **get_bake_mode**()

The light\'s bake mode. This will affect the global illumination
techniques that have an effect on the light\'s rendering.

\*\*Note:\*\* Meshes\' global illumination mode will also affect the
global illumination rendering. See
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **light_color** =
`Color(1, 1, 1, 1)`
`🔗<class_Light3D_property_light_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The light\'s color in the nonlinear sRGB color space. An *overbright*
color can be used to achieve a result equivalent to increasing the
light\'s
`light_energy<class_Light3D_property_light_energy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **light_cull_mask** =
`4294967295`
`🔗<class_Light3D_property_light_cull_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_cull_mask**()

The light will affect objects in the selected layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **light_energy** =
`1.0` `🔗<class_Light3D_property_light_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The light\'s strength multiplier (this is not a physical unit). For
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}, changing
this value will only change the light color\'s intensity, not the
light\'s radius.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_indirect_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**light_indirect_energy** = `1.0`
`🔗<class_Light3D_property_light_indirect_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Secondary multiplier used with indirect light (light bounces). Used with
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} and SDFGI (see
`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* This property is ignored if
`light_energy<class_Light3D_property_light_energy>`{.interpreted-text
role="ref"} is equal to `0.0`, as the light won\'t be present at all in
the GI shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_intensity_lumens}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**light_intensity_lumens**
`🔗<class_Light3D_property_light_intensity_lumens>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Used by positional lights
(`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}) when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is `true`. Sets the intensity of the light source measured
in Lumens. Lumens are a measure of luminous flux, which is the total
amount of visible light emitted by a light source per unit of time.

For `SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}s, we
assume that the area outside the visible cone is surrounded by a perfect
light absorbing material. Accordingly, the apparent brightness of the
cone area does not change as the cone increases and decreases in size.

A typical household lightbulb can range from around 600 lumens to 1,200
lumens, a candle is about 13 lumens, while a streetlight can be
approximately 60,000 lumens.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_intensity_lux}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**light_intensity_lux**
`🔗<class_Light3D_property_light_intensity_lux>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Used by `DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is `true`. Sets the intensity of the light source measured
in Lux. Lux is a measure of luminous flux per unit area, it is equal to
one lumen per square meter. Lux is the measure of how much light hits a
surface at a given time.

On a clear sunny day a surface in direct sunlight may be approximately
100,000 lux, a typical room in a home may be approximately 50 lux, while
the moonlit ground may be approximately 0.1 lux.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_negative}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **light_negative** =
`false` `🔗<class_Light3D_property_light_negative>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_negative**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_negative**()

If `true`, the light\'s effect is reversed, darkening areas and casting
bright shadows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_projector}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**light_projector**
`🔗<class_Light3D_property_light_projector>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_projector**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_projector**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} projected by
light.
`shadow_enabled<class_Light3D_property_shadow_enabled>`{.interpreted-text
role="ref"} must be on for the projector to work. Light projectors make
the light appear as if it is shining through a colored but transparent
object, almost like light shining through stained-glass.

\*\*Note:\*\* Unlike
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
whose filter mode can be adjusted on a per-material basis, the filter
mode for light projector textures is set globally with
`ProjectSettings.rendering/textures/light_projectors/filter<class_ProjectSettings_property_rendering/textures/light_projectors/filter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Light projector textures are only supported in the
Forward+ and Mobile rendering methods, not Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **light_size** =
`0.0` `🔗<class_Light3D_property_light_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The size of the light in Godot units. Only available for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"}s and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}s.
Increasing this value will make the light fade out slower and shadows
appear blurrier (also called percentage-closer soft shadows, or PCSS).
This can be used to simulate area lights to an extent. Increasing this
value above `0.0` for lights with shadows enabled will have a noticeable
performance cost due to PCSS.

\*\*Note:\*\*
`light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"} is not affected by
`Node3D.scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"} (the light\'s scale or its parent\'s scale).

\*\*Note:\*\* PCSS for positional lights is only supported in the
Forward+ and Mobile rendering methods, not Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_specular}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **light_specular** =
`1.0` `🔗<class_Light3D_property_light_specular>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the specular blob in objects affected by the light. At
`0`, the light becomes a pure diffuse light. When not baking emission,
this can be used to avoid unrealistic reflections when placing lights
above an emissive surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_temperature}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **light_temperature**
`🔗<class_Light3D_property_light_temperature>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_temperature**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_temperature**()

Sets the color temperature of the light source, measured in Kelvin. This
is used to calculate a correlated color temperature which tints the
`light_color<class_Light3D_property_light_color>`{.interpreted-text
role="ref"}.

The sun on a cloudy day is approximately 6500 Kelvin, on a clear day it
is between 5500 to 6000 Kelvin, and on a clear day at sunrise or sunset
it ranges to around 1850 Kelvin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_light_volumetric_fog_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**light_volumetric_fog_energy** = `1.0`
`🔗<class_Light3D_property_light_volumetric_fog_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Secondary multiplier multiplied with
`light_energy<class_Light3D_property_light_energy>`{.interpreted-text
role="ref"} then used with the
`Environment<class_Environment>`{.interpreted-text role="ref"}\'s
volumetric fog (if enabled). If set to `0.0`, computing volumetric fog
will be skipped for this light, which can improve performance for large
amounts of lights when volumetric fog is enabled.

\*\*Note:\*\* To prevent short-lived dynamic light effects from poorly
interacting with volumetric fog, lights used in those effects should
have
`light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>`{.interpreted-text
role="ref"} set to `0.0` unless
`Environment.volumetric_fog_temporal_reprojection_enabled<class_Environment_property_volumetric_fog_temporal_reprojection_enabled>`{.interpreted-text
role="ref"} is disabled (or unless the reprojection amount is
significantly lowered).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **shadow_bias** =
`0.1` `🔗<class_Light3D_property_shadow_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Used to adjust shadow appearance. Too small a value results in
self-shadowing (\"shadow acne\"), while too large a value causes shadows
to separate from casters (\"peter-panning\"). Adjust as needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_blur}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **shadow_blur** =
`1.0` `🔗<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Blurs the edges of the shadow. Can be used to hide pixel artifacts in
low-resolution shadow maps. A high value can impact performance, make
shadows appear grainy and can cause other unwanted artifacts. Try to
keep as near default as possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_caster_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_caster_mask** =
`4294967295`
`🔗<class_Light3D_property_shadow_caster_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_caster_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_shadow_caster_mask**()

The light will only cast shadows using objects in the selected layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shadow_enabled** =
`false` `🔗<class_Light3D_property_shadow_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_shadow**()

If `true`, the light will cast real-time shadows. This has a significant
performance cost. Only enable shadow rendering when it makes a
noticeable difference in the scene\'s appearance, and consider using
`distance_fade_enabled<class_Light3D_property_distance_fade_enabled>`{.interpreted-text
role="ref"} to hide the light when far away from the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_normal_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shadow_normal_bias** = `2.0`
`🔗<class_Light3D_property_shadow_normal_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Offsets the lookup into the shadow map by the object\'s normal. This can
be used to reduce self-shadowing artifacts without using
`shadow_bias<class_Light3D_property_shadow_bias>`{.interpreted-text
role="ref"}. In practice, this value should be tweaked along with
`shadow_bias<class_Light3D_property_shadow_bias>`{.interpreted-text
role="ref"} to reduce artifacts as much as possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_opacity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **shadow_opacity** =
`1.0` `🔗<class_Light3D_property_shadow_opacity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The opacity to use when rendering the light\'s shadow map. Values lower
than `1.0` make the light appear through shadows. This can be used to
fake global illumination at a low performance cost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_reverse_cull_face}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shadow_reverse_cull_face** = `false`
`🔗<class_Light3D_property_shadow_reverse_cull_face>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_reverse_cull_face**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_shadow_reverse_cull_face**()

If `true`, reverses the backface culling of the mesh. This can be useful
when you have a flat mesh that has a light behind it. If you need to
cast a shadow on both sides of the mesh, set the mesh to use
double-sided shadows with
`GeometryInstance3D.SHADOW_CASTING_SETTING_DOUBLE_SIDED<class_GeometryInstance3D_constant_SHADOW_CASTING_SETTING_DOUBLE_SIDED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_property_shadow_transmittance_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shadow_transmittance_bias** = `0.05`
`🔗<class_Light3D_property_shadow_transmittance_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Light3D_method_get_correlated_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_correlated_color**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Light3D_method_get_correlated_color>`{.interpreted-text
role="ref"}

Returns the `Color<class_Color>`{.interpreted-text role="ref"} of an
idealized blackbody at the given
`light_temperature<class_Light3D_property_light_temperature>`{.interpreted-text
role="ref"}. This value is calculated internally based on the
`light_temperature<class_Light3D_property_light_temperature>`{.interpreted-text
role="ref"}. This `Color<class_Color>`{.interpreted-text role="ref"} is
multiplied by
`light_color<class_Light3D_property_light_color>`{.interpreted-text
role="ref"} before being sent to the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_method_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_param**(param:
`Param<enum_Light3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Light3D_method_get_param>`{.interpreted-text
role="ref"}

Returns the value of the specified
`Param<enum_Light3D_Param>`{.interpreted-text role="ref"} parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light3D_method_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param**(param: `Param<enum_Light3D_Param>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Light3D_method_set_param>`{.interpreted-text role="ref"}

Sets the value of the specified
`Param<enum_Light3D_Param>`{.interpreted-text role="ref"} parameter.
