github_url
:   hide

# Sky {#class_Sky}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Defines a 3D environment\'s background by using a
`Material<class_Material>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

The **Sky** class uses a `Material<class_Material>`{.interpreted-text
role="ref"} to render a 3D environment\'s background and the light it
emits by updating the reflection/radiance cubemaps.

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

:::: {#enum_Sky_RadianceSize}
::: rst-class
classref-enumeration
:::
::::

enum **RadianceSize**: `🔗<enum_Sky_RadianceSize>`{.interpreted-text
role="ref"}

:::: {#class_Sky_constant_RADIANCE_SIZE_32}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_32** = `0`

Radiance texture size is 32×32 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_64}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_64** = `1`

Radiance texture size is 64×64 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_128}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_128** = `2`

Radiance texture size is 128×128 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_256}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_256** = `3`

Radiance texture size is 256×256 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_512}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_512** = `4`

Radiance texture size is 512×512 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_1024}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_1024** = `5`

Radiance texture size is 1024×1024 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_2048}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_2048** = `6`

Radiance texture size is 2048×2048 pixels.

:::: {#class_Sky_constant_RADIANCE_SIZE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**RADIANCE_SIZE_MAX** = `7`

Represents the size of the
`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Sky_ProcessMode}
::: rst-class
classref-enumeration
:::
::::

enum **ProcessMode**: `🔗<enum_Sky_ProcessMode>`{.interpreted-text
role="ref"}

:::: {#class_Sky_constant_PROCESS_MODE_AUTOMATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky
shader. If your shader uses `TIME` or `POSITION`, this will use
`PROCESS_MODE_REALTIME<class_Sky_constant_PROCESS_MODE_REALTIME>`{.interpreted-text
role="ref"}. If your shader uses any of the `LIGHT_*` variables or any
custom uniforms, this uses
`PROCESS_MODE_INCREMENTAL<class_Sky_constant_PROCESS_MODE_INCREMENTAL>`{.interpreted-text
role="ref"}. Otherwise, this defaults to
`PROCESS_MODE_QUALITY<class_Sky_constant_PROCESS_MODE_QUALITY>`{.interpreted-text
role="ref"}.

:::: {#class_Sky_constant_PROCESS_MODE_QUALITY}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In
general, this results in much higher quality than
`PROCESS_MODE_REALTIME<class_Sky_constant_PROCESS_MODE_REALTIME>`{.interpreted-text
role="ref"} but takes much longer to generate. This should not be used
if you plan on changing the sky at runtime. If you are finding that the
reflection is not blurry enough and is showing sparkles or fireflies,
try increasing
`ProjectSettings.rendering/reflections/sky_reflections/ggx_samples<class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples>`{.interpreted-text
role="ref"}.

:::: {#class_Sky_constant_PROCESS_MODE_INCREMENTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance
map as
`PROCESS_MODE_QUALITY<class_Sky_constant_PROCESS_MODE_QUALITY>`{.interpreted-text
role="ref"}, but updates over several frames. The number of frames is
determined by
`ProjectSettings.rendering/reflections/sky_reflections/roughness_layers<class_ProjectSettings_property_rendering/reflections/sky_reflections/roughness_layers>`{.interpreted-text
role="ref"}. Use this when you need highest quality radiance maps, but
have a sky that updates slowly.

:::: {#class_Sky_constant_PROCESS_MODE_REALTIME}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In
general this results in lower quality, but substantially faster run
times. If you need better quality, but still need to update the sky
every frame, consider turning on
`ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality<class_ProjectSettings_property_rendering/reflections/sky_reflections/fast_filter_high_quality>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The fast filtering algorithm is limited to 256×256
cubemaps, so
`radiance_size<class_Sky_property_radiance_size>`{.interpreted-text
role="ref"} must be set to
`RADIANCE_SIZE_256<class_Sky_constant_RADIANCE_SIZE_256>`{.interpreted-text
role="ref"}. Otherwise, a warning is printed and the overridden radiance
size is ignored.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Sky_property_process_mode}
::: rst-class
classref-property
:::
::::

`ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"}
**process_mode** = `0`
`🔗<class_Sky_property_process_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_mode**(value:
  `ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"})
- `ProcessMode<enum_Sky_ProcessMode>`{.interpreted-text role="ref"}
  **get_process_mode**()

The method for generating the radiance map from the sky. The radiance
map is a cubemap with increasingly blurry versions of the sky
corresponding to different levels of roughness. Radiance maps can be
expensive to calculate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sky_property_radiance_size}
::: rst-class
classref-property
:::
::::

`RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
**radiance_size** = `3`
`🔗<class_Sky_property_radiance_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radiance_size**(value:
  `RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"})
- `RadianceSize<enum_Sky_RadianceSize>`{.interpreted-text role="ref"}
  **get_radiance_size**()

The **Sky**\'s radiance map size. The higher the radiance map size, the
more detailed the lighting from the **Sky** will be.

\*\*Note:\*\* Some hardware will have trouble with higher radiance
sizes, especially
`RADIANCE_SIZE_512<class_Sky_constant_RADIANCE_SIZE_512>`{.interpreted-text
role="ref"} and above. Only use such high values on high-end hardware.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sky_property_sky_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**sky_material** `🔗<class_Sky_property_sky_material>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

`Material<class_Material>`{.interpreted-text role="ref"} used to draw
the background. Can be
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"},
`ProceduralSkyMaterial<class_ProceduralSkyMaterial>`{.interpreted-text
role="ref"},
`PhysicalSkyMaterial<class_PhysicalSkyMaterial>`{.interpreted-text
role="ref"}, or even a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"} if
you want to use your own custom shader.
