github_url
:   hide

# LightmapGI {#class_LightmapGI}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Computes and stores baked lightmaps for fast global illumination.

::: rst-class
classref-introduction-group
:::

## Description

The **LightmapGI** node is used to compute and store baked lightmaps.
Lightmaps are used to provide high-quality indirect lighting with very
little light leaking. **LightmapGI** can also provide rough reflections
using spherical harmonics if
`directional<class_LightmapGI_property_directional>`{.interpreted-text
role="ref"} is enabled. Dynamic objects can receive indirect lighting
thanks to *light probes*, which can be automatically placed by setting
`generate_probes_subdiv<class_LightmapGI_property_generate_probes_subdiv>`{.interpreted-text
role="ref"} to a value other than
`GENERATE_PROBES_DISABLED<class_LightmapGI_constant_GENERATE_PROBES_DISABLED>`{.interpreted-text
role="ref"}. Additional lightmap probes can also be added by creating
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}
nodes. The downside is that lightmaps are fully static and cannot be
baked in an exported project. Baking a **LightmapGI** node is also
slower compared to `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"}.

\*\*Procedural generation:\*\* Lightmap baking functionality is only
available in the editor. This means **LightmapGI** is not suited to
procedurally generated or user-built levels. For procedurally generated
or user-built levels, use `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} or SDFGI instead (see
`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}).

\*\*Performance:\*\* **LightmapGI** provides the best possible run-time
performance for global illumination. It is suitable for low-end hardware
including integrated graphics and mobile devices.

\*\*Note:\*\* Due to how lightmaps work, most properties only have a
visible effect once lightmaps are baked again.

\*\*Note:\*\* Lightmap baking on
`CSGShape3D<class_CSGShape3D>`{.interpreted-text role="ref"}s and
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}es is
not supported, as these cannot store UV2 data required for baking.

\*\*Note:\*\* If no custom lightmappers are installed, **LightmapGI**
can only be baked from devices that support the Forward+ or Mobile
renderers.

\*\*Note:\*\* The **LightmapGI** node only bakes light data for child
nodes of its parent. Nodes further up the hierarchy of the scene will
not be baked.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Lightmap global illumination <../tutorials/3d/global_illumination/using_lightmap_gi>`{.interpreted-text
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

:::: {#enum_LightmapGI_BakeQuality}
::: rst-class
classref-enumeration
:::
::::

enum **BakeQuality**:
`🔗<enum_LightmapGI_BakeQuality>`{.interpreted-text role="ref"}

:::: {#class_LightmapGI_constant_BAKE_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text role="ref"}
**BAKE_QUALITY_LOW** = `0`

Low bake quality (fastest bake times). The quality of this preset can be
adjusted by changing
`ProjectSettings.rendering/lightmapping/bake_quality/low_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_ray_count>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/lightmapping/bake_quality/low_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_probe_ray_count>`{.interpreted-text
role="ref"}.

:::: {#class_LightmapGI_constant_BAKE_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text role="ref"}
**BAKE_QUALITY_MEDIUM** = `1`

Medium bake quality (fast bake times). The quality of this preset can be
adjusted by changing
`ProjectSettings.rendering/lightmapping/bake_quality/medium_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_ray_count>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/lightmapping/bake_quality/medium_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_probe_ray_count>`{.interpreted-text
role="ref"}.

:::: {#class_LightmapGI_constant_BAKE_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text role="ref"}
**BAKE_QUALITY_HIGH** = `2`

High bake quality (slow bake times). The quality of this preset can be
adjusted by changing
`ProjectSettings.rendering/lightmapping/bake_quality/high_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_ray_count>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/lightmapping/bake_quality/high_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_probe_ray_count>`{.interpreted-text
role="ref"}.

:::: {#class_LightmapGI_constant_BAKE_QUALITY_ULTRA}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text role="ref"}
**BAKE_QUALITY_ULTRA** = `3`

Highest bake quality (slowest bake times). The quality of this preset
can be adjusted by changing
`ProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_ray_count>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_LightmapGI_GenerateProbes}
::: rst-class
classref-enumeration
:::
::::

enum **GenerateProbes**:
`🔗<enum_LightmapGI_GenerateProbes>`{.interpreted-text role="ref"}

:::: {#class_LightmapGI_constant_GENERATE_PROBES_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
role="ref"} **GENERATE_PROBES_DISABLED** = `0`

Don\'t generate lightmap probes for lighting dynamic objects.

:::: {#class_LightmapGI_constant_GENERATE_PROBES_SUBDIV_4}
::: rst-class
classref-enumeration-constant
:::
::::

`GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
role="ref"} **GENERATE_PROBES_SUBDIV_4** = `1`

Lowest level of subdivision (fastest bake times, smallest file sizes).

:::: {#class_LightmapGI_constant_GENERATE_PROBES_SUBDIV_8}
::: rst-class
classref-enumeration-constant
:::
::::

`GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
role="ref"} **GENERATE_PROBES_SUBDIV_8** = `2`

Low level of subdivision (fast bake times, small file sizes).

:::: {#class_LightmapGI_constant_GENERATE_PROBES_SUBDIV_16}
::: rst-class
classref-enumeration-constant
:::
::::

`GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
role="ref"} **GENERATE_PROBES_SUBDIV_16** = `3`

High level of subdivision (slow bake times, large file sizes).

:::: {#class_LightmapGI_constant_GENERATE_PROBES_SUBDIV_32}
::: rst-class
classref-enumeration-constant
:::
::::

`GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
role="ref"} **GENERATE_PROBES_SUBDIV_32** = `4`

Highest level of subdivision (slowest bake times, largest file sizes).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_LightmapGI_BakeError}
::: rst-class
classref-enumeration
:::
::::

enum **BakeError**: `🔗<enum_LightmapGI_BakeError>`{.interpreted-text
role="ref"}

:::: {#class_LightmapGI_constant_BAKE_ERROR_OK}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_OK** = `0`

Lightmap baking was successful.

:::: {#class_LightmapGI_constant_BAKE_ERROR_NO_SCENE_ROOT}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_NO_SCENE_ROOT** = `1`

Lightmap baking failed because the root node for the edited scene could
not be accessed.

:::: {#class_LightmapGI_constant_BAKE_ERROR_FOREIGN_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_FOREIGN_DATA** = `2`

Lightmap baking failed as the lightmap data resource is embedded in a
foreign resource.

:::: {#class_LightmapGI_constant_BAKE_ERROR_NO_LIGHTMAPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_NO_LIGHTMAPPER** = `3`

Lightmap baking failed as there is no lightmapper available in this
Godot build.

:::: {#class_LightmapGI_constant_BAKE_ERROR_NO_SAVE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_NO_SAVE_PATH** = `4`

Lightmap baking failed as the
`LightmapGIData<class_LightmapGIData>`{.interpreted-text role="ref"}
save path isn\'t configured in the resource.

:::: {#class_LightmapGI_constant_BAKE_ERROR_NO_MESHES}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_NO_MESHES** = `5`

Lightmap baking failed as there are no meshes whose
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"} is
`GeometryInstance3D.GI_MODE_STATIC<class_GeometryInstance3D_constant_GI_MODE_STATIC>`{.interpreted-text
role="ref"} and with valid UV2 mapping in the current scene. You may
need to select 3D scenes in the Import dock and change their global
illumination mode accordingly.

:::: {#class_LightmapGI_constant_BAKE_ERROR_MESHES_INVALID}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_MESHES_INVALID** = `6`

Lightmap baking failed as the lightmapper failed to analyze some of the
meshes marked as static for baking.

:::: {#class_LightmapGI_constant_BAKE_ERROR_CANT_CREATE_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_CANT_CREATE_IMAGE** = `7`

Lightmap baking failed as the resulting image couldn\'t be saved or
imported by Godot after it was saved.

:::: {#class_LightmapGI_constant_BAKE_ERROR_USER_ABORTED}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_USER_ABORTED** = `8`

The user aborted the lightmap baking operation (typically by clicking
the **Cancel** button in the progress dialog).

:::: {#class_LightmapGI_constant_BAKE_ERROR_TEXTURE_SIZE_TOO_SMALL}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_TEXTURE_SIZE_TOO_SMALL** = `9`

Lightmap baking failed as the maximum texture size is too small to fit
some of the meshes marked for baking.

:::: {#class_LightmapGI_constant_BAKE_ERROR_LIGHTMAP_TOO_SMALL}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_LIGHTMAP_TOO_SMALL** = `10`

Lightmap baking failed as the lightmap is too small.

:::: {#class_LightmapGI_constant_BAKE_ERROR_ATLAS_TOO_SMALL}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeError<enum_LightmapGI_BakeError>`{.interpreted-text role="ref"}
**BAKE_ERROR_ATLAS_TOO_SMALL** = `11`

Lightmap baking failed as the lightmap was unable to fit into an atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_LightmapGI_EnvironmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentMode**:
`🔗<enum_LightmapGI_EnvironmentMode>`{.interpreted-text role="ref"}

:::: {#class_LightmapGI_constant_ENVIRONMENT_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
role="ref"} **ENVIRONMENT_MODE_DISABLED** = `0`

Ignore environment lighting when baking lightmaps.

:::: {#class_LightmapGI_constant_ENVIRONMENT_MODE_SCENE}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
role="ref"} **ENVIRONMENT_MODE_SCENE** = `1`

Use the scene\'s environment lighting when baking lightmaps.

\*\*Note:\*\* If baking lightmaps in a scene with no
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text role="ref"}
node, this will act like
`ENVIRONMENT_MODE_DISABLED<class_LightmapGI_constant_ENVIRONMENT_MODE_DISABLED>`{.interpreted-text
role="ref"}. The editor\'s preview sky and sun is *not* taken into
account by **LightmapGI** when baking lightmaps.

:::: {#class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
role="ref"} **ENVIRONMENT_MODE_CUSTOM_SKY** = `2`

Use
`environment_custom_sky<class_LightmapGI_property_environment_custom_sky>`{.interpreted-text
role="ref"} as a source of environment lighting when baking lightmaps.

:::: {#class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
role="ref"} **ENVIRONMENT_MODE_CUSTOM_COLOR** = `3`

Use
`environment_custom_color<class_LightmapGI_property_environment_custom_color>`{.interpreted-text
role="ref"} multiplied by
`environment_custom_energy<class_LightmapGI_property_environment_custom_energy>`{.interpreted-text
role="ref"} as a constant source of environment lighting when baking
lightmaps.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_LightmapGI_property_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bias** = `0.0005`
`🔗<class_LightmapGI_property_bias>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bias**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bias**()

The bias to use when computing shadows. Increasing
`bias<class_LightmapGI_property_bias>`{.interpreted-text role="ref"} can
fix shadow acne on the resulting baked lightmap, but can introduce
peter-panning (shadows not connecting to their casters). Real-time
`Light3D<class_Light3D>`{.interpreted-text role="ref"} shadows are not
affected by this
`bias<class_LightmapGI_property_bias>`{.interpreted-text role="ref"}
property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_bounce_indirect_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**bounce_indirect_energy** = `1.0`
`🔗<class_LightmapGI_property_bounce_indirect_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bounce_indirect_energy**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bounce_indirect_energy**()

The energy multiplier for each bounce. Higher values will make indirect
lighting brighter. A value of `1.0` represents physically accurate
behavior, but higher values can be used to make indirect lighting
propagate more visibly when using a low number of bounces. This can be
used to speed up bake times by lowering the number of
`bounces<class_LightmapGI_property_bounces>`{.interpreted-text
role="ref"} then increasing
`bounce_indirect_energy<class_LightmapGI_property_bounce_indirect_energy>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`bounce_indirect_energy<class_LightmapGI_property_bounce_indirect_energy>`{.interpreted-text
role="ref"} only has an effect if
`bounces<class_LightmapGI_property_bounces>`{.interpreted-text
role="ref"} is set to a value greater than or equal to `1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_bounces}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bounces** = `3`
`🔗<class_LightmapGI_property_bounces>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bounces**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bounces**()

Number of light bounces that are taken into account during baking.
Higher values result in brighter, more realistic lighting, at the cost
of longer bake times. If set to `0`, only environment lighting, direct
light and emissive lighting is baked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_camera_attributes}
::: rst-class
classref-property
:::
::::

`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**camera_attributes**
`🔗<class_LightmapGI_property_camera_attributes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_attributes**(value:
  `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"})
- `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"} **get_camera_attributes**()

The `CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"} resource that specifies exposure levels to bake at.
Auto-exposure and non exposure properties will be ignored. Exposure
settings should be used to reduce the dynamic range present when baking.
If exposure is too high, the **LightmapGI** will have banding artifacts
or may have over-exposure artifacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_denoiser_range}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **denoiser_range** = `10`
`🔗<class_LightmapGI_property_denoiser_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_denoiser_range**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_denoiser_range**()

The distance in pixels from which the denoiser samples. Lower values
preserve more details, but may give blotchy results if the lightmap
quality is not high enough. Only effective if
`use_denoiser<class_LightmapGI_property_use_denoiser>`{.interpreted-text
role="ref"} is `true` and
`ProjectSettings.rendering/lightmapping/denoising/denoiser<class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser>`{.interpreted-text
role="ref"} is set to JNLM.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_denoiser_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **denoiser_strength**
= `0.1`
`🔗<class_LightmapGI_property_denoiser_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_denoiser_strength**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_denoiser_strength**()

The strength of denoising step applied to the generated lightmaps. Only
effective if
`use_denoiser<class_LightmapGI_property_use_denoiser>`{.interpreted-text
role="ref"} is `true` and
`ProjectSettings.rendering/lightmapping/denoising/denoiser<class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser>`{.interpreted-text
role="ref"} is set to JNLM.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_directional}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **directional** =
`false` `🔗<class_LightmapGI_property_directional>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_directional**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_directional**()

If `true`, bakes lightmaps to contain directional information as
spherical harmonics. This results in more realistic lighting appearance,
especially with normal mapped materials and for lights that have their
direct light baked
(`Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>`{.interpreted-text
role="ref"} set to
`Light3D.BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>`{.interpreted-text
role="ref"} and with
`Light3D.editor_only<class_Light3D_property_editor_only>`{.interpreted-text
role="ref"} set to `false`). The directional information is also used to
provide rough reflections for static and dynamic objects. This has a
small run-time performance cost as the shader has to perform more work
to interpret the direction information from the lightmap. Directional
lightmaps also take longer to bake and result in larger file sizes.

\*\*Note:\*\* The property\'s name has no relationship with
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}.
`directional<class_LightmapGI_property_directional>`{.interpreted-text
role="ref"} works with all light types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_environment_custom_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**environment_custom_color** = `Color(1, 1, 1, 1)`
`🔗<class_LightmapGI_property_environment_custom_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment_custom_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_environment_custom_color**()

The color to use for environment lighting. Only effective if
`environment_mode<class_LightmapGI_property_environment_mode>`{.interpreted-text
role="ref"} is
`ENVIRONMENT_MODE_CUSTOM_COLOR<class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_COLOR>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_environment_custom_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**environment_custom_energy** = `1.0`
`🔗<class_LightmapGI_property_environment_custom_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment_custom_energy**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_environment_custom_energy**()

The color multiplier to use for environment lighting. Only effective if
`environment_mode<class_LightmapGI_property_environment_mode>`{.interpreted-text
role="ref"} is
`ENVIRONMENT_MODE_CUSTOM_COLOR<class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_COLOR>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_environment_custom_sky}
::: rst-class
classref-property
:::
::::

`Sky<class_Sky>`{.interpreted-text role="ref"}
**environment_custom_sky**
`🔗<class_LightmapGI_property_environment_custom_sky>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment_custom_sky**(value:
  `Sky<class_Sky>`{.interpreted-text role="ref"})
- `Sky<class_Sky>`{.interpreted-text role="ref"}
  **get_environment_custom_sky**()

The sky to use as a source of environment lighting. Only effective if
`environment_mode<class_LightmapGI_property_environment_mode>`{.interpreted-text
role="ref"} is
`ENVIRONMENT_MODE_CUSTOM_SKY<class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_SKY>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_environment_mode}
::: rst-class
classref-property
:::
::::

`EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
role="ref"} **environment_mode** = `1`
`🔗<class_LightmapGI_property_environment_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment_mode**(value:
  `EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
  role="ref"})
- `EnvironmentMode<enum_LightmapGI_EnvironmentMode>`{.interpreted-text
  role="ref"} **get_environment_mode**()

The environment mode to use when baking lightmaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_generate_probes_subdiv}
::: rst-class
classref-property
:::
::::

`GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
role="ref"} **generate_probes_subdiv** = `2`
`🔗<class_LightmapGI_property_generate_probes_subdiv>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_generate_probes**(value:
  `GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
  role="ref"})
- `GenerateProbes<enum_LightmapGI_GenerateProbes>`{.interpreted-text
  role="ref"} **get_generate_probes**()

The level of subdivision to use when automatically generating
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s for
dynamic object lighting. Higher values result in more accurate indirect
lighting on dynamic objects, at the cost of longer bake times and larger
file sizes.

\*\*Note:\*\* Automatically generated
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s are
not visible as nodes in the Scene tree dock, and cannot be modified this
way after they are generated.

\*\*Note:\*\* Regardless of
`generate_probes_subdiv<class_LightmapGI_property_generate_probes_subdiv>`{.interpreted-text
role="ref"}, direct lighting on dynamic objects is always applied using
`Light3D<class_Light3D>`{.interpreted-text role="ref"} nodes in
real-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_interior}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **interior** = `false`
`🔗<class_LightmapGI_property_interior>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interior**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_interior**()

If `true`, ignore environment lighting when baking lightmaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_light_data}
::: rst-class
classref-property
:::
::::

`LightmapGIData<class_LightmapGIData>`{.interpreted-text role="ref"}
**light_data**
`🔗<class_LightmapGI_property_light_data>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_light_data**(value:
  `LightmapGIData<class_LightmapGIData>`{.interpreted-text role="ref"})
- `LightmapGIData<class_LightmapGIData>`{.interpreted-text role="ref"}
  **get_light_data**()

The `LightmapGIData<class_LightmapGIData>`{.interpreted-text role="ref"}
associated to this **LightmapGI** node. This resource is automatically
created after baking, and is not meant to be created manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_max_texture_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_texture_size** =
`16384`
`🔗<class_LightmapGI_property_max_texture_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_texture_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_texture_size**()

The maximum texture size for the generated texture atlas. Higher values
will result in fewer slices being generated, but may not work on all
hardware as a result of hardware limitations on texture sizes. Leave
`max_texture_size<class_LightmapGI_property_max_texture_size>`{.interpreted-text
role="ref"} at its default value of `16384` if unsure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_quality}
::: rst-class
classref-property
:::
::::

`BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text role="ref"}
**quality** = `1`
`🔗<class_LightmapGI_property_quality>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_quality**(value:
  `BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text
  role="ref"})
- `BakeQuality<enum_LightmapGI_BakeQuality>`{.interpreted-text
  role="ref"} **get_bake_quality**()

The quality preset to use when baking lightmaps. This affects bake
times, but output file sizes remain mostly identical across quality
levels.

To further speed up bake times, decrease
`bounces<class_LightmapGI_property_bounces>`{.interpreted-text
role="ref"}, disable
`use_denoiser<class_LightmapGI_property_use_denoiser>`{.interpreted-text
role="ref"} and/or decrease
`texel_scale<class_LightmapGI_property_texel_scale>`{.interpreted-text
role="ref"}.

To further increase quality, enable
`supersampling<class_LightmapGI_property_supersampling>`{.interpreted-text
role="ref"} and/or increase
`texel_scale<class_LightmapGI_property_texel_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_shadowmask_mode}
::: rst-class
classref-property
:::
::::

`ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>`{.interpreted-text
role="ref"} **shadowmask_mode** = `0`
`🔗<class_LightmapGI_property_shadowmask_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadowmask_mode**(value:
  `ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>`{.interpreted-text
  role="ref"})
- `ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>`{.interpreted-text
  role="ref"} **get_shadowmask_mode**()

**Experimental:** This property may be changed or removed in future
versions.

The shadowmasking policy to use for directional shadows on static
objects that are baked with this **LightmapGI** instance.

Shadowmasking allows
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"} nodes to cast shadows even outside the range defined by
their
`DirectionalLight3D.directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"} property. This is done by baking a texture that contains a
shadowmap for the directional light, then using this texture according
to the current shadowmask mode.

\*\*Note:\*\* The shadowmask texture is only created if
`shadowmask_mode<class_LightmapGI_property_shadowmask_mode>`{.interpreted-text
role="ref"} is not
`LightmapGIData.SHADOWMASK_MODE_NONE<class_LightmapGIData_constant_SHADOWMASK_MODE_NONE>`{.interpreted-text
role="ref"}. To see a difference, you need to bake lightmaps again after
switching from
`LightmapGIData.SHADOWMASK_MODE_NONE<class_LightmapGIData_constant_SHADOWMASK_MODE_NONE>`{.interpreted-text
role="ref"} to any other mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_supersampling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **supersampling** =
`false` `🔗<class_LightmapGI_property_supersampling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_supersampling_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_supersampling_enabled**()

If `true`, lightmaps are baked with the texel scale multiplied with
`supersampling_factor<class_LightmapGI_property_supersampling_factor>`{.interpreted-text
role="ref"} and downsampled before saving the lightmap (so the effective
texel density is identical to having supersampling disabled).

Supersampling provides increased lightmap quality with less noise,
smoother shadows and better shadowing of small-scale features in
objects. However, it may result in significantly increased bake times
and memory usage while baking lightmaps. Padding is automatically
adjusted to avoid increasing light leaking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_supersampling_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**supersampling_factor** = `2.0`
`🔗<class_LightmapGI_property_supersampling_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_supersampling_factor**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_supersampling_factor**()

The factor by which the texel density is multiplied for supersampling.
For best results, use an integer value. While fractional values are
allowed, they can result in increased light leaking and a blurry
lightmap.

Higher values may result in better quality, but also increase bake times
and memory usage while baking.

See
`supersampling<class_LightmapGI_property_supersampling>`{.interpreted-text
role="ref"} for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_texel_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **texel_scale** =
`1.0` `🔗<class_LightmapGI_property_texel_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texel_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texel_scale**()

Scales the lightmap texel density of all meshes for the current bake.
This is a multiplier that builds upon the existing lightmap texel size
defined in each imported 3D scene, along with the per-mesh density
multiplier (which is designed to be used when the same mesh is used at
different scales). Lower values will result in faster bake times.

For example, doubling
`texel_scale<class_LightmapGI_property_texel_scale>`{.interpreted-text
role="ref"} doubles the lightmap texture resolution for all objects *on
each axis*, so it will *quadruple* the texel count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_use_denoiser}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_denoiser** =
`true` `🔗<class_LightmapGI_property_use_denoiser>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_denoiser**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_denoiser**()

If `true`, uses a GPU-based denoising algorithm on the generated
lightmap. This eliminates most noise within the generated lightmap at
the cost of longer bake times. File sizes are generally not impacted
significantly by the use of a denoiser, although lossless compression
may do a better job at compressing a denoised image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGI_property_use_texture_for_bounces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_texture_for_bounces** = `true`
`🔗<class_LightmapGI_property_use_texture_for_bounces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_texture_for_bounces**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_texture_for_bounces**()

If `true`, a texture with the lighting information will be generated to
speed up the generation of indirect lighting at the cost of some
accuracy. The geometry might exhibit extra light leak artifacts when
using low resolution lightmaps or UVs that stretch the lightmap
significantly across surfaces. Leave
`use_texture_for_bounces<class_LightmapGI_property_use_texture_for_bounces>`{.interpreted-text
role="ref"} at its default value of `true` if unsure.

\*\*Note:\*\*
`use_texture_for_bounces<class_LightmapGI_property_use_texture_for_bounces>`{.interpreted-text
role="ref"} only has an effect if
`bounces<class_LightmapGI_property_bounces>`{.interpreted-text
role="ref"} is set to a value greater than or equal to `1`.
