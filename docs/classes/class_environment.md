github_url
:   hide

# Environment {#class_Environment}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Resource for environment nodes (like
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}) that define multiple rendering options.

::: rst-class
classref-introduction-group
:::

## Description

Resource for environment nodes (like
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}) that define multiple environment operations (such as
background `Sky<class_Sky>`{.interpreted-text role="ref"} or
`Color<class_Color>`{.interpreted-text role="ref"}, ambient light, fog,
depth-of-field\...). These parameters affect the final render of the
scene. The order of these operations is:

- Depth of Field Blur
- Glow
- Tonemap (Auto Exposure)
- Adjustments

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Environment and post-processing <../tutorials/3d/environment_and_post_processing>`{.interpreted-text
  role="doc"}
- `High dynamic range lighting <../tutorials/3d/high_dynamic_range>`{.interpreted-text
  role="doc"}
- [3D Material Testers
  Demo](https://godotengine.org/asset-library/asset/2742)
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

:::: {#enum_Environment_BGMode}
::: rst-class
classref-enumeration
:::
::::

enum **BGMode**: `🔗<enum_Environment_BGMode>`{.interpreted-text
role="ref"}

:::: {#class_Environment_constant_BG_CLEAR_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_CLEAR_COLOR** = `0`

Clears the background using the clear color defined in
`ProjectSettings.rendering/environment/defaults/default_clear_color<class_ProjectSettings_property_rendering/environment/defaults/default_clear_color>`{.interpreted-text
role="ref"}.

:::: {#class_Environment_constant_BG_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_COLOR** = `1`

Clears the background using a custom clear color.

:::: {#class_Environment_constant_BG_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_SKY** = `2`

Displays a user-defined sky in the background.

:::: {#class_Environment_constant_BG_CANVAS}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_CANVAS** = `3`

Displays a `CanvasLayer<class_CanvasLayer>`{.interpreted-text
role="ref"} in the background.

:::: {#class_Environment_constant_BG_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_KEEP** = `4`

Keeps on screen every pixel drawn in the background. This is the fastest
background mode, but it can only be safely used in fully-interior scenes
(no visible sky or sky reflections). If enabled in a scene where the
background is visible, \"ghost trail\" artifacts will be visible when
moving the camera.

:::: {#class_Environment_constant_BG_CAMERA_FEED}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_CAMERA_FEED** = `5`

Displays a camera feed in the background.

:::: {#class_Environment_constant_BG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**BG_MAX** = `6`

Represents the size of the
`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Environment_AmbientSource}
::: rst-class
classref-enumeration
:::
::::

enum **AmbientSource**:
`🔗<enum_Environment_AmbientSource>`{.interpreted-text role="ref"}

:::: {#class_Environment_constant_AMBIENT_SOURCE_BG}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
role="ref"} **AMBIENT_SOURCE_BG** = `0`

Gather ambient light from whichever source is specified as the
background.

:::: {#class_Environment_constant_AMBIENT_SOURCE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
role="ref"} **AMBIENT_SOURCE_DISABLED** = `1`

Disable ambient light. This provides a slight performance boost over
`AMBIENT_SOURCE_SKY<class_Environment_constant_AMBIENT_SOURCE_SKY>`{.interpreted-text
role="ref"}.

:::: {#class_Environment_constant_AMBIENT_SOURCE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
role="ref"} **AMBIENT_SOURCE_COLOR** = `2`

Specify a specific `Color<class_Color>`{.interpreted-text role="ref"}
for ambient light. This provides a slight performance boost over
`AMBIENT_SOURCE_SKY<class_Environment_constant_AMBIENT_SOURCE_SKY>`{.interpreted-text
role="ref"}.

:::: {#class_Environment_constant_AMBIENT_SOURCE_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
role="ref"} **AMBIENT_SOURCE_SKY** = `3`

Gather ambient light from the `Sky<class_Sky>`{.interpreted-text
role="ref"} regardless of what the background is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Environment_ReflectionSource}
::: rst-class
classref-enumeration
:::
::::

enum **ReflectionSource**:
`🔗<enum_Environment_ReflectionSource>`{.interpreted-text role="ref"}

:::: {#class_Environment_constant_REFLECTION_SOURCE_BG}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionSource<enum_Environment_ReflectionSource>`{.interpreted-text
role="ref"} **REFLECTION_SOURCE_BG** = `0`

Use the background for reflections.

:::: {#class_Environment_constant_REFLECTION_SOURCE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionSource<enum_Environment_ReflectionSource>`{.interpreted-text
role="ref"} **REFLECTION_SOURCE_DISABLED** = `1`

Disable reflections. This provides a slight performance boost over other
options.

:::: {#class_Environment_constant_REFLECTION_SOURCE_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionSource<enum_Environment_ReflectionSource>`{.interpreted-text
role="ref"} **REFLECTION_SOURCE_SKY** = `2`

Use the `Sky<class_Sky>`{.interpreted-text role="ref"} for reflections
regardless of what the background is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Environment_ToneMapper}
::: rst-class
classref-enumeration
:::
::::

enum **ToneMapper**: `🔗<enum_Environment_ToneMapper>`{.interpreted-text
role="ref"}

:::: {#class_Environment_constant_TONE_MAPPER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text role="ref"}
**TONE_MAPPER_LINEAR** = `0`

Does not modify color data, resulting in a linear tonemapping curve
which unnaturally clips bright values, causing bright lighting to look
blown out. The simplest and fastest tonemapper.

:::: {#class_Environment_constant_TONE_MAPPER_REINHARDT}
::: rst-class
classref-enumeration-constant
:::
::::

`ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text role="ref"}
**TONE_MAPPER_REINHARDT** = `1`

A simple tonemapping curve that rolls off bright values to prevent
clipping. This results in an image that can appear dull and low
contrast. Slower than
`TONE_MAPPER_LINEAR<class_Environment_constant_TONE_MAPPER_LINEAR>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When
`tonemap_white<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"} is left at the default value of `1.0`,
`TONE_MAPPER_REINHARDT<class_Environment_constant_TONE_MAPPER_REINHARDT>`{.interpreted-text
role="ref"} produces an identical image to
`TONE_MAPPER_LINEAR<class_Environment_constant_TONE_MAPPER_LINEAR>`{.interpreted-text
role="ref"}.

:::: {#class_Environment_constant_TONE_MAPPER_FILMIC}
::: rst-class
classref-enumeration-constant
:::
::::

`ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text role="ref"}
**TONE_MAPPER_FILMIC** = `2`

Uses a film-like tonemapping curve to prevent clipping of bright values
and provide better contrast than
`TONE_MAPPER_REINHARDT<class_Environment_constant_TONE_MAPPER_REINHARDT>`{.interpreted-text
role="ref"}. Slightly slower than
`TONE_MAPPER_REINHARDT<class_Environment_constant_TONE_MAPPER_REINHARDT>`{.interpreted-text
role="ref"}.

:::: {#class_Environment_constant_TONE_MAPPER_ACES}
::: rst-class
classref-enumeration-constant
:::
::::

`ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text role="ref"}
**TONE_MAPPER_ACES** = `3`

Uses a high-contrast film-like tonemapping curve and desaturates bright
values for a more realistic appearance. Slightly slower than
`TONE_MAPPER_FILMIC<class_Environment_constant_TONE_MAPPER_FILMIC>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This tonemapping operator is called \"ACES Fitted\" in
Godot 3.x.

:::: {#class_Environment_constant_TONE_MAPPER_AGX}
::: rst-class
classref-enumeration-constant
:::
::::

`ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text role="ref"}
**TONE_MAPPER_AGX** = `4`

Uses a film-like tonemapping curve and desaturates bright values for a
more realistic appearance. Better than other tonemappers at maintaining
the hue of colors as they become brighter. The slowest tonemapping
option.

\*\*Note:\*\*
`tonemap_white<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"} is fixed at a value of `16.29`, which makes
`TONE_MAPPER_AGX<class_Environment_constant_TONE_MAPPER_AGX>`{.interpreted-text
role="ref"} unsuitable for use with the Mobile rendering method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Environment_GlowBlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **GlowBlendMode**:
`🔗<enum_Environment_GlowBlendMode>`{.interpreted-text role="ref"}

:::: {#class_Environment_constant_GLOW_BLEND_MODE_ADDITIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
role="ref"} **GLOW_BLEND_MODE_ADDITIVE** = `0`

Additive glow blending mode. Mostly used for particles, glows (bloom),
lens flare, bright sources.

:::: {#class_Environment_constant_GLOW_BLEND_MODE_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
role="ref"} **GLOW_BLEND_MODE_SCREEN** = `1`

Screen glow blending mode. Increases brightness, used frequently with
bloom.

:::: {#class_Environment_constant_GLOW_BLEND_MODE_SOFTLIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
role="ref"} **GLOW_BLEND_MODE_SOFTLIGHT** = `2`

Soft light glow blending mode. Modifies contrast, exposes shadows and
highlights (vivid bloom).

:::: {#class_Environment_constant_GLOW_BLEND_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
role="ref"} **GLOW_BLEND_MODE_REPLACE** = `3`

Replace glow blending mode. Replaces all pixels\' color by the glow
value. This can be used to simulate a full-screen blur effect by
tweaking the glow parameters to match the original image\'s brightness.

:::: {#class_Environment_constant_GLOW_BLEND_MODE_MIX}
::: rst-class
classref-enumeration-constant
:::
::::

`GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
role="ref"} **GLOW_BLEND_MODE_MIX** = `4`

Mixes the glow with the underlying color to avoid increasing brightness
as much while still maintaining a glow effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Environment_FogMode}
::: rst-class
classref-enumeration
:::
::::

enum **FogMode**: `🔗<enum_Environment_FogMode>`{.interpreted-text
role="ref"}

:::: {#class_Environment_constant_FOG_MODE_EXPONENTIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`FogMode<enum_Environment_FogMode>`{.interpreted-text role="ref"}
**FOG_MODE_EXPONENTIAL** = `0`

Use a physically-based fog model defined primarily by fog density.

:::: {#class_Environment_constant_FOG_MODE_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`FogMode<enum_Environment_FogMode>`{.interpreted-text role="ref"}
**FOG_MODE_DEPTH** = `1`

Use a simple fog model defined by start and end positions and a custom
curve. While not physically accurate, this model can be useful when you
need more artistic control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Environment_SDFGIYScale}
::: rst-class
classref-enumeration
:::
::::

enum **SDFGIYScale**:
`🔗<enum_Environment_SDFGIYScale>`{.interpreted-text role="ref"}

:::: {#class_Environment_constant_SDFGI_Y_SCALE_50_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFGIYScale<enum_Environment_SDFGIYScale>`{.interpreted-text
role="ref"} **SDFGI_Y_SCALE_50_PERCENT** = `0`

Use 50% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be
twice as short as they are wide. This allows providing increased GI
detail and reduced light leaking with thin floors and ceilings. This is
usually the best choice for scenes that don\'t feature much verticality.

:::: {#class_Environment_constant_SDFGI_Y_SCALE_75_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFGIYScale<enum_Environment_SDFGIYScale>`{.interpreted-text
role="ref"} **SDFGI_Y_SCALE_75_PERCENT** = `1`

Use 75% scale for SDFGI on the Y (vertical) axis. This is a balance
between the 50% and 100% SDFGI Y scales.

:::: {#class_Environment_constant_SDFGI_Y_SCALE_100_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFGIYScale<enum_Environment_SDFGIYScale>`{.interpreted-text
role="ref"} **SDFGI_Y_SCALE_100_PERCENT** = `2`

Use 100% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be
as tall as they are wide. This is usually the best choice for highly
vertical scenes. The downside is that light leaking may become more
noticeable with thin floors and ceilings.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Environment_property_adjustment_brightness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**adjustment_brightness** = `1.0`
`🔗<class_Environment_property_adjustment_brightness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_adjustment_brightness**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_adjustment_brightness**()

The global brightness value of the rendered scene. Effective only if
`adjustment_enabled<class_Environment_property_adjustment_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_adjustment_color_correction}
::: rst-class
classref-property
:::
::::

`Texture<class_Texture>`{.interpreted-text role="ref"}
**adjustment_color_correction**
`🔗<class_Environment_property_adjustment_color_correction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_adjustment_color_correction**(value:
  `Texture<class_Texture>`{.interpreted-text role="ref"})
- `Texture<class_Texture>`{.interpreted-text role="ref"}
  **get_adjustment_color_correction**()

The `Texture2D<class_Texture2D>`{.interpreted-text role="ref"} or
`Texture3D<class_Texture3D>`{.interpreted-text role="ref"} lookup table
(LUT) to use for the built-in post-process color grading. Can use a
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"} for a 1-dimensional LUT, or a
`Texture3D<class_Texture3D>`{.interpreted-text role="ref"} for a more
complex LUT. Effective only if
`adjustment_enabled<class_Environment_property_adjustment_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_adjustment_contrast}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**adjustment_contrast** = `1.0`
`🔗<class_Environment_property_adjustment_contrast>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_adjustment_contrast**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_adjustment_contrast**()

The global contrast value of the rendered scene (default value is 1).
Effective only if
`adjustment_enabled<class_Environment_property_adjustment_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_adjustment_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **adjustment_enabled**
= `false`
`🔗<class_Environment_property_adjustment_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_adjustment_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_adjustment_enabled**()

If `true`, enables the `adjustment_*` properties provided by this
resource. If `false`, modifications to the `adjustment_*` properties
will have no effect on the rendered scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_adjustment_saturation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**adjustment_saturation** = `1.0`
`🔗<class_Environment_property_adjustment_saturation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_adjustment_saturation**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_adjustment_saturation**()

The global color saturation value of the rendered scene (default value
is 1). Effective only if
`adjustment_enabled<class_Environment_property_adjustment_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ambient_light_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**ambient_light_color** = `Color(0, 0, 0, 1)`
`🔗<class_Environment_property_ambient_light_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_light_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_ambient_light_color**()

The ambient light\'s `Color<class_Color>`{.interpreted-text role="ref"}.
Only effective if
`ambient_light_sky_contribution<class_Environment_property_ambient_light_sky_contribution>`{.interpreted-text
role="ref"} is lower than `1.0` (exclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ambient_light_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ambient_light_energy** = `1.0`
`🔗<class_Environment_property_ambient_light_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_light_energy**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ambient_light_energy**()

The ambient light\'s energy. The higher the value, the stronger the
light. Only effective if
`ambient_light_sky_contribution<class_Environment_property_ambient_light_sky_contribution>`{.interpreted-text
role="ref"} is lower than `1.0` (exclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ambient_light_sky_contribution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ambient_light_sky_contribution** = `1.0`
`🔗<class_Environment_property_ambient_light_sky_contribution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_light_sky_contribution**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ambient_light_sky_contribution**()

Defines the amount of light that the sky brings on the scene. A value of
`0.0` means that the sky\'s light emission has no effect on the scene
illumination, thus all ambient illumination is provided by the ambient
light. On the contrary, a value of `1.0` means that *all* the light that
affects the scene is provided by the sky, thus the ambient light
parameter has no effect on the scene.

\*\*Note:\*\*
`ambient_light_sky_contribution<class_Environment_property_ambient_light_sky_contribution>`{.interpreted-text
role="ref"} is internally clamped between `0.0` and `1.0` (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ambient_light_source}
::: rst-class
classref-property
:::
::::

`AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
role="ref"} **ambient_light_source** = `0`
`🔗<class_Environment_property_ambient_light_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_source**(value:
  `AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
  role="ref"})
- `AmbientSource<enum_Environment_AmbientSource>`{.interpreted-text
  role="ref"} **get_ambient_source**()

The ambient light source to use for rendering materials and global
illumination.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_background_camera_feed_id}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**background_camera_feed_id** = `1`
`🔗<class_Environment_property_background_camera_feed_id>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_feed_id**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_camera_feed_id**()

The ID of the camera feed to show in the background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_background_canvas_max_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**background_canvas_max_layer** = `0`
`🔗<class_Environment_property_background_canvas_max_layer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_canvas_max_layer**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_canvas_max_layer**()

The maximum layer ID to display. Only effective when using the
`BG_CANVAS<class_Environment_constant_BG_CANVAS>`{.interpreted-text
role="ref"} background mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_background_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **background_color**
= `Color(0, 0, 0, 1)`
`🔗<class_Environment_property_background_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bg_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_bg_color**()

The `Color<class_Color>`{.interpreted-text role="ref"} displayed for
clear areas of the scene. Only effective when using the
`BG_COLOR<class_Environment_constant_BG_COLOR>`{.interpreted-text
role="ref"} background mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_background_energy_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**background_energy_multiplier** = `1.0`
`🔗<class_Environment_property_background_energy_multiplier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bg_energy_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bg_energy_multiplier**()

Multiplier for background energy. Increase to make background brighter,
decrease to make background dimmer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_background_intensity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**background_intensity** = `30000.0`
`🔗<class_Environment_property_background_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bg_intensity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bg_intensity**()

Luminance of background measured in nits (candela per square meter).
Only used when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is enabled. The default value is roughly equivalent to the
sky at midday.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_background_mode}
::: rst-class
classref-property
:::
::::

`BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
**background_mode** = `0`
`🔗<class_Environment_property_background_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_background**(value:
  `BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"})
- `BGMode<enum_Environment_BGMode>`{.interpreted-text role="ref"}
  **get_background**()

The background mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_aerial_perspective}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**fog_aerial_perspective** = `0.0`
`🔗<class_Environment_property_fog_aerial_perspective>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_aerial_perspective**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_aerial_perspective**()

If set above `0.0` (exclusive), blends between the fog\'s color and the
color of the background `Sky<class_Sky>`{.interpreted-text role="ref"},
as read from the radiance cubemap. This has a small performance cost
when set above `0.0`. Must have
`background_mode<class_Environment_property_background_mode>`{.interpreted-text
role="ref"} set to
`BG_SKY<class_Environment_constant_BG_SKY>`{.interpreted-text
role="ref"}.

This is useful to simulate [aerial
perspective](https://en.wikipedia.org/wiki/Aerial_perspective) in large
scenes with low density fog. However, it is not very useful for
high-density fog, as the sky will shine through. When set to `1.0`, the
fog color comes completely from the `Sky<class_Sky>`{.interpreted-text
role="ref"}. If set to `0.0`, aerial perspective is disabled.

Notice that this does not sample the `Sky<class_Sky>`{.interpreted-text
role="ref"} directly, but rather the radiance cubemap. The cubemap is
sampled at a mipmap level depending on the depth of the rendered pixel;
the farther away, the higher the resolution of the sampled mipmap. This
results in the actual color being a blurred version of the sky, with
more blur closer to the camera. The highest mipmap resolution is used at
a depth of `Camera3D.far<class_Camera3D_property_far>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_density}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_density** =
`0.01` `🔗<class_Environment_property_fog_density>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_density**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_density**()

The fog density to be used. This is demonstrated in different ways
depending on the
`fog_mode<class_Environment_property_fog_mode>`{.interpreted-text
role="ref"} mode chosen:

\*\*Exponential Fog Mode:\*\* Higher values result in denser fog. The
fog rendering is exponential like in real life.

\*\*Depth Fog mode:\*\* The maximum intensity of the deep fog, effect
will appear in the distance (relative to the camera). At `1.0` the fog
will fully obscure the scene, at `0.0` the fog will not be visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_depth_begin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_depth_begin** =
`10.0`
`🔗<class_Environment_property_fog_depth_begin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_depth_begin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_depth_begin**()

The fog\'s depth starting distance from the camera. Only available when
`fog_mode<class_Environment_property_fog_mode>`{.interpreted-text
role="ref"} is set to
`FOG_MODE_DEPTH<class_Environment_constant_FOG_MODE_DEPTH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_depth_curve}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_depth_curve** =
`1.0` `🔗<class_Environment_property_fog_depth_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_depth_curve**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_depth_curve**()

The fog depth\'s intensity curve. A number of presets are available in
the Inspector by right-clicking the curve. Only available when
`fog_mode<class_Environment_property_fog_mode>`{.interpreted-text
role="ref"} is set to
`FOG_MODE_DEPTH<class_Environment_constant_FOG_MODE_DEPTH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_depth_end}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_depth_end** =
`100.0` `🔗<class_Environment_property_fog_depth_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_depth_end**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_depth_end**()

The fog\'s depth end distance from the camera. If this value is set to
`0`, it will be equal to the current camera\'s
`Camera3D.far<class_Camera3D_property_far>`{.interpreted-text
role="ref"} value. Only available when
`fog_mode<class_Environment_property_fog_mode>`{.interpreted-text
role="ref"} is set to
`FOG_MODE_DEPTH<class_Environment_constant_FOG_MODE_DEPTH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fog_enabled** =
`false` `🔗<class_Environment_property_fog_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_fog_enabled**()

If `true`, fog effects are enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_height** =
`0.0` `🔗<class_Environment_property_fog_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_height**()

The height at which the height fog effect begins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_height_density}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**fog_height_density** = `0.0`
`🔗<class_Environment_property_fog_height_density>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_height_density**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_height_density**()

The density used to increase fog as height decreases. To make fog
increase as height increases, use a negative value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_light_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **fog_light_color** =
`Color(0.518, 0.553, 0.608, 1)`
`🔗<class_Environment_property_fog_light_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_light_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_fog_light_color**()

The fog\'s color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_light_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_light_energy**
= `1.0`
`🔗<class_Environment_property_fog_light_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_light_energy**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_light_energy**()

The fog\'s brightness. Higher values result in brighter fog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_mode}
::: rst-class
classref-property
:::
::::

`FogMode<enum_Environment_FogMode>`{.interpreted-text role="ref"}
**fog_mode** = `0`
`🔗<class_Environment_property_fog_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_mode**(value:
  `FogMode<enum_Environment_FogMode>`{.interpreted-text role="ref"})
- `FogMode<enum_Environment_FogMode>`{.interpreted-text role="ref"}
  **get_fog_mode**()

The fog mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_sky_affect}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_sky_affect** =
`1.0` `🔗<class_Environment_property_fog_sky_affect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_sky_affect**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_sky_affect**()

The factor to use when affecting the sky with non-volumetric fog. `1.0`
means that fog can fully obscure the sky. Lower values reduce the impact
of fog on sky rendering, with `0.0` not affecting sky rendering at all.

\*\*Note:\*\*
`fog_sky_affect<class_Environment_property_fog_sky_affect>`{.interpreted-text
role="ref"} has no visual effect if
`fog_aerial_perspective<class_Environment_property_fog_aerial_perspective>`{.interpreted-text
role="ref"} is `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_fog_sun_scatter}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fog_sun_scatter** =
`0.0` `🔗<class_Environment_property_fog_sun_scatter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fog_sun_scatter**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fog_sun_scatter**()

If set above `0.0`, renders the scene\'s directional light(s) in the fog
color depending on the view angle. This can be used to give the
impression that the sun is \"piercing\" through the fog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_blend_mode}
::: rst-class
classref-property
:::
::::

`GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
role="ref"} **glow_blend_mode** = `2`
`🔗<class_Environment_property_glow_blend_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_blend_mode**(value:
  `GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
  role="ref"})
- `GlowBlendMode<enum_Environment_GlowBlendMode>`{.interpreted-text
  role="ref"} **get_glow_blend_mode**()

The glow blending mode.

\*\*Note:\*\*
`glow_blend_mode<class_Environment_property_glow_blend_mode>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_bloom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_bloom** =
`0.0` `🔗<class_Environment_property_glow_bloom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_bloom**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_bloom**()

The bloom\'s intensity. If set to a value higher than `0`, this will
make glow visible in areas darker than the
`glow_hdr_threshold<class_Environment_property_glow_hdr_threshold>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **glow_enabled** =
`false` `🔗<class_Environment_property_glow_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_glow_enabled**()

If `true`, the glow effect is enabled. This simulates real world
eye/camera behavior where bright pixels bleed onto surrounding pixels.

\*\*Note:\*\* When using the Mobile rendering method, glow looks
different due to the lower dynamic range available in the Mobile
rendering method.

\*\*Note:\*\* When using the Compatibility rendering method, glow uses a
different implementation with some properties being unavailable and
hidden from the inspector: `glow_levels/*`,
`glow_normalized<class_Environment_property_glow_normalized>`{.interpreted-text
role="ref"},
`glow_strength<class_Environment_property_glow_strength>`{.interpreted-text
role="ref"},
`glow_blend_mode<class_Environment_property_glow_blend_mode>`{.interpreted-text
role="ref"},
`glow_mix<class_Environment_property_glow_mix>`{.interpreted-text
role="ref"},
`glow_map<class_Environment_property_glow_map>`{.interpreted-text
role="ref"}, and
`glow_map_strength<class_Environment_property_glow_map_strength>`{.interpreted-text
role="ref"}. This implementation is optimized to run on low-end devices
and is less flexible as a result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_hdr_luminance_cap}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**glow_hdr_luminance_cap** = `12.0`
`🔗<class_Environment_property_glow_hdr_luminance_cap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_hdr_luminance_cap**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_hdr_luminance_cap**()

The higher threshold of the HDR glow. Areas brighter than this threshold
will be clamped for the purposes of the glow effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_hdr_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_hdr_scale** =
`2.0` `🔗<class_Environment_property_glow_hdr_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_hdr_bleed_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_hdr_bleed_scale**()

The bleed scale of the HDR glow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_hdr_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**glow_hdr_threshold** = `1.0`
`🔗<class_Environment_property_glow_hdr_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_hdr_bleed_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_hdr_bleed_threshold**()

The lower threshold of the HDR glow. When using the Mobile rendering
method (which only supports a lower dynamic range up to `2.0`), this may
need to be below `1.0` for glow to be visible. A value of `0.9` works
well in this case. This value also needs to be decreased below `1.0`
when using glow in 2D, as 2D rendering is performed in SDR.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_intensity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_intensity** =
`0.8` `🔗<class_Environment_property_glow_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_intensity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_intensity**()

The overall brightness multiplier of the glow effect. When using the
Mobile rendering method (which only supports a lower dynamic range up to
`2.0`), this should be increased to `1.5` to compensate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/1}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/1** =
`0.0` `🔗<class_Environment_property_glow_levels/1>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 1st level of glow. This is the most \"local\" level
(least blurry).

\*\*Note:\*\*
`glow_levels/1<class_Environment_property_glow_levels/1>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/2}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/2** =
`0.0` `🔗<class_Environment_property_glow_levels/2>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 2nd level of glow.

\*\*Note:\*\*
`glow_levels/2<class_Environment_property_glow_levels/2>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/3}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/3** =
`1.0` `🔗<class_Environment_property_glow_levels/3>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 3rd level of glow.

\*\*Note:\*\*
`glow_levels/3<class_Environment_property_glow_levels/3>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/4}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/4** =
`0.0` `🔗<class_Environment_property_glow_levels/4>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 4th level of glow.

\*\*Note:\*\*
`glow_levels/4<class_Environment_property_glow_levels/4>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/5}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/5** =
`1.0` `🔗<class_Environment_property_glow_levels/5>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 5th level of glow.

\*\*Note:\*\*
`glow_levels/5<class_Environment_property_glow_levels/5>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/6}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/6** =
`0.0` `🔗<class_Environment_property_glow_levels/6>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 6th level of glow.

\*\*Note:\*\*
`glow_levels/6<class_Environment_property_glow_levels/6>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_levels/7}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_levels/7** =
`0.0` `🔗<class_Environment_property_glow_levels/7>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"}, intensity: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_level**(idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The intensity of the 7th level of glow. This is the most \"global\"
level (blurriest).

\*\*Note:\*\*
`glow_levels/7<class_Environment_property_glow_levels/7>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_map}
::: rst-class
classref-property
:::
::::

`Texture<class_Texture>`{.interpreted-text role="ref"} **glow_map**
`🔗<class_Environment_property_glow_map>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_map**(value: `Texture<class_Texture>`{.interpreted-text
  role="ref"})
- `Texture<class_Texture>`{.interpreted-text role="ref"}
  **get_glow_map**()

The texture that should be used as a glow map to *multiply* the
resulting glow color according to
`glow_map_strength<class_Environment_property_glow_map_strength>`{.interpreted-text
role="ref"}. This can be used to create a \"lens dirt\" effect. The
texture\'s RGB color channels are used for modulation, but the alpha
channel is ignored.

\*\*Note:\*\* The texture will be stretched to fit the screen.
Therefore, it\'s recommended to use a texture with an aspect ratio that
matches your project\'s base aspect ratio (typically 16:9).

\*\*Note:\*\*
`glow_map<class_Environment_property_glow_map>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_map_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_map_strength**
= `0.8`
`🔗<class_Environment_property_glow_map_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_map_strength**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_map_strength**()

How strong of an influence the
`glow_map<class_Environment_property_glow_map>`{.interpreted-text
role="ref"} should have on the overall glow effect. A strength of `0.0`
means the glow map has no influence, while a strength of `1.0` means the
glow map has full influence.

\*\*Note:\*\* If the glow map has black areas, a value of `1.0` can also
turn off the glow effect entirely in specific areas of the screen.

\*\*Note:\*\*
`glow_map_strength<class_Environment_property_glow_map_strength>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_mix}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_mix** = `0.05`
`🔗<class_Environment_property_glow_mix>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_mix**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_glow_mix**()

When using the
`GLOW_BLEND_MODE_MIX<class_Environment_constant_GLOW_BLEND_MODE_MIX>`{.interpreted-text
role="ref"}
`glow_blend_mode<class_Environment_property_glow_blend_mode>`{.interpreted-text
role="ref"}, this controls how much the source image is blended with the
glow layer. A value of `0.0` makes the glow rendering invisible, while a
value of `1.0` is equivalent to
`GLOW_BLEND_MODE_REPLACE<class_Environment_constant_GLOW_BLEND_MODE_REPLACE>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`glow_mix<class_Environment_property_glow_mix>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_normalized}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **glow_normalized** =
`false`
`🔗<class_Environment_property_glow_normalized>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_normalized**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_glow_normalized**()

If `true`, glow levels will be normalized so that summed together their
intensities equal `1.0`.

\*\*Note:\*\*
`glow_normalized<class_Environment_property_glow_normalized>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_glow_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **glow_strength** =
`1.0` `🔗<class_Environment_property_glow_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glow_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_glow_strength**()

The strength of the glow effect. This applies as the glow is blurred
across the screen and increases the distance and intensity of the blur.
When using the Mobile rendering method, this should be increased to
compensate for the lower dynamic range.

\*\*Note:\*\*
`glow_strength<class_Environment_property_glow_strength>`{.interpreted-text
role="ref"} has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation
optimized for low-end devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_reflected_light_source}
::: rst-class
classref-property
:::
::::

`ReflectionSource<enum_Environment_ReflectionSource>`{.interpreted-text
role="ref"} **reflected_light_source** = `0`
`🔗<class_Environment_property_reflected_light_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_reflection_source**(value:
  `ReflectionSource<enum_Environment_ReflectionSource>`{.interpreted-text
  role="ref"})
- `ReflectionSource<enum_Environment_ReflectionSource>`{.interpreted-text
  role="ref"} **get_reflection_source**()

The reflected (specular) light source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_bounce_feedback}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sdfgi_bounce_feedback** = `0.5`
`🔗<class_Environment_property_sdfgi_bounce_feedback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_bounce_feedback**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_bounce_feedback**()

The energy multiplier applied to light every time it bounces from a
surface when using SDFGI. Values greater than `0.0` will simulate
multiple bounces, resulting in a more realistic appearance. Increasing
`sdfgi_bounce_feedback<class_Environment_property_sdfgi_bounce_feedback>`{.interpreted-text
role="ref"} generally has no performance impact. See also
`sdfgi_energy<class_Environment_property_sdfgi_energy>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Values greater than `0.5` can cause infinite feedback
loops and should be avoided in scenes with bright materials.

\*\*Note:\*\* If
`sdfgi_bounce_feedback<class_Environment_property_sdfgi_bounce_feedback>`{.interpreted-text
role="ref"} is `0.0`, indirect lighting will not be represented in
reflections as light will only bounce one time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_cascade0_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sdfgi_cascade0_distance** = `12.8`
`🔗<class_Environment_property_sdfgi_cascade0_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_cascade0_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_cascade0_distance**()

**Note:** This property is linked to
`sdfgi_min_cell_size<class_Environment_property_sdfgi_min_cell_size>`{.interpreted-text
role="ref"} and
`sdfgi_max_distance<class_Environment_property_sdfgi_max_distance>`{.interpreted-text
role="ref"}. Changing its value will automatically change those
properties as well.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_cascades}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sdfgi_cascades** = `4`
`🔗<class_Environment_property_sdfgi_cascades>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_cascades**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sdfgi_cascades**()

The number of cascades to use for SDFGI (between 1 and 8). A higher
number of cascades allows displaying SDFGI further away while preserving
detail up close, at the cost of performance. When using SDFGI on
small-scale levels,
`sdfgi_cascades<class_Environment_property_sdfgi_cascades>`{.interpreted-text
role="ref"} can often be decreased between `1` and `4` to improve
performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sdfgi_enabled** =
`false` `🔗<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_sdfgi_enabled**()

If `true`, enables signed distance field global illumination for meshes
that have their
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"} set to
`GeometryInstance3D.GI_MODE_STATIC<class_GeometryInstance3D_constant_GI_MODE_STATIC>`{.interpreted-text
role="ref"}. SDFGI is a real-time global illumination technique that
works well with procedurally generated and user-built levels, including
in situations where geometry is created during gameplay. The signed
distance field is automatically generated around the camera as it moves.
Dynamic lights are supported, but dynamic occluders and emissive
surfaces are not.

\*\*Note:\*\* SDFGI is only supported in the Forward+ rendering method,
not Mobile or Compatibility.

\*\*Performance:\*\* SDFGI is relatively demanding on the GPU and is not
suited to low-end hardware such as integrated graphics (consider
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} instead).
To improve SDFGI performance, enable
`ProjectSettings.rendering/global_illumination/gi/use_half_resolution<class_ProjectSettings_property_rendering/global_illumination/gi/use_half_resolution>`{.interpreted-text
role="ref"} in the Project Settings.

\*\*Note:\*\* Meshes should have sufficiently thick walls to avoid light
leaks (avoid one-sided walls). For interior levels, enclose your level
geometry in a sufficiently large box and bridge the loops to close the
mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sdfgi_energy** =
`1.0` `🔗<class_Environment_property_sdfgi_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_energy**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_energy**()

The energy multiplier to use for SDFGI. Higher values will result in
brighter indirect lighting and reflections. See also
`sdfgi_bounce_feedback<class_Environment_property_sdfgi_bounce_feedback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sdfgi_max_distance** = `204.8`
`🔗<class_Environment_property_sdfgi_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_max_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_max_distance**()

The maximum distance at which SDFGI is visible. Beyond this distance,
environment lighting or other sources of GI such as
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}
will be used as a fallback.

\*\*Note:\*\* This property is linked to
`sdfgi_min_cell_size<class_Environment_property_sdfgi_min_cell_size>`{.interpreted-text
role="ref"} and
`sdfgi_cascade0_distance<class_Environment_property_sdfgi_cascade0_distance>`{.interpreted-text
role="ref"}. Changing its value will automatically change those
properties as well.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_min_cell_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sdfgi_min_cell_size** = `0.2`
`🔗<class_Environment_property_sdfgi_min_cell_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_min_cell_size**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_min_cell_size**()

The cell size to use for the closest SDFGI cascade (in 3D units). Lower
values allow SDFGI to be more precise up close, at the cost of making
SDFGI updates more demanding. This can cause stuttering when the camera
moves fast. Higher values allow SDFGI to cover more ground, while also
reducing the performance impact of SDFGI updates.

\*\*Note:\*\* This property is linked to
`sdfgi_max_distance<class_Environment_property_sdfgi_max_distance>`{.interpreted-text
role="ref"} and
`sdfgi_cascade0_distance<class_Environment_property_sdfgi_cascade0_distance>`{.interpreted-text
role="ref"}. Changing its value will automatically change those
properties as well.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_normal_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sdfgi_normal_bias**
= `1.1`
`🔗<class_Environment_property_sdfgi_normal_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_normal_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_normal_bias**()

The normal bias to use for SDFGI probes. Increasing this value can
reduce visible streaking artifacts on sloped surfaces, at the cost of
increased light leaking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_probe_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sdfgi_probe_bias**
= `1.1`
`🔗<class_Environment_property_sdfgi_probe_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_probe_bias**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sdfgi_probe_bias**()

The constant bias to use for SDFGI probes. Increasing this value can
reduce visible streaking artifacts on sloped surfaces, at the cost of
increased light leaking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_read_sky_light}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**sdfgi_read_sky_light** = `true`
`🔗<class_Environment_property_sdfgi_read_sky_light>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_read_sky_light**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_sdfgi_reading_sky_light**()

If `true`, SDFGI takes the environment lighting into account. This
should be set to `false` for interior scenes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_use_occlusion}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sdfgi_use_occlusion**
= `false`
`🔗<class_Environment_property_sdfgi_use_occlusion>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_use_occlusion**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_sdfgi_using_occlusion**()

If `true`, SDFGI uses an occlusion detection approach to reduce light
leaking. Occlusion may however introduce dark blotches in certain spots,
which may be undesired in mostly outdoor scenes.
`sdfgi_use_occlusion<class_Environment_property_sdfgi_use_occlusion>`{.interpreted-text
role="ref"} has a performance impact and should only be enabled when
needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sdfgi_y_scale}
::: rst-class
classref-property
:::
::::

`SDFGIYScale<enum_Environment_SDFGIYScale>`{.interpreted-text
role="ref"} **sdfgi_y_scale** = `1`
`🔗<class_Environment_property_sdfgi_y_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdfgi_y_scale**(value:
  `SDFGIYScale<enum_Environment_SDFGIYScale>`{.interpreted-text
  role="ref"})
- `SDFGIYScale<enum_Environment_SDFGIYScale>`{.interpreted-text
  role="ref"} **get_sdfgi_y_scale**()

The Y scale to use for SDFGI cells. Lower values will result in SDFGI
cells being packed together more closely on the Y axis. This is used to
balance between quality and covering a lot of vertical ground.
`sdfgi_y_scale<class_Environment_property_sdfgi_y_scale>`{.interpreted-text
role="ref"} should be set depending on how vertical your scene is (and
how fast your camera may move on the Y axis).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sky}
::: rst-class
classref-property
:::
::::

`Sky<class_Sky>`{.interpreted-text role="ref"} **sky**
`🔗<class_Environment_property_sky>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky**(value: `Sky<class_Sky>`{.interpreted-text role="ref"})
- `Sky<class_Sky>`{.interpreted-text role="ref"} **get_sky**()

The `Sky<class_Sky>`{.interpreted-text role="ref"} resource used for
this **Environment**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sky_custom_fov}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sky_custom_fov** =
`0.0` `🔗<class_Environment_property_sky_custom_fov>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_custom_fov**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sky_custom_fov**()

If set to a value greater than `0.0`, overrides the field of view to use
for sky rendering. If set to `0.0`, the same FOV as the current
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} is used for sky
rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_sky_rotation}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **sky_rotation**
= `Vector3(0, 0, 0)`
`🔗<class_Environment_property_sky_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_rotation**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_sky_rotation**()

The rotation to use for sky rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_ao_channel_affect}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ssao_ao_channel_affect** = `0.0`
`🔗<class_Environment_property_ssao_ao_channel_affect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_ao_channel_affect**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_ao_channel_affect**()

The screen-space ambient occlusion intensity on materials that have an
AO texture defined. Values higher than `0` will make the SSAO effect
visible in areas darkened by AO textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_detail}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_detail** =
`0.5` `🔗<class_Environment_property_ssao_detail>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_detail**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_detail**()

Sets the strength of the additional level of detail for the screen-space
ambient occlusion effect. A high value makes the detail pass more
prominent, but it may contribute to aliasing in your final image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ssao_enabled** =
`false` `🔗<class_Environment_property_ssao_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ssao_enabled**()

If `true`, the screen-space ambient occlusion effect is enabled. This
darkens objects\' corners and cavities to simulate ambient light not
reaching the entire object as in real life. This works well for small,
dynamic objects, but baked lighting or ambient occlusion textures will
do a better job at displaying ambient occlusion on large static objects.
Godot uses a form of SSAO called Adaptive Screen Space Ambient Occlusion
which is itself a form of Horizon Based Ambient Occlusion.

\*\*Note:\*\* SSAO is only supported in the Forward+ rendering method,
not Mobile or Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_horizon}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_horizon** =
`0.06` `🔗<class_Environment_property_ssao_horizon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_horizon**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_horizon**()

The threshold for considering whether a given point on a surface is
occluded or not represented as an angle from the horizon mapped into the
`0.0-1.0` range. A value of `1.0` results in no occlusion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_intensity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_intensity** =
`2.0` `🔗<class_Environment_property_ssao_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_intensity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_intensity**()

The primary screen-space ambient occlusion intensity. Acts as a
multiplier for the screen-space ambient occlusion effect. A higher value
results in darker occlusion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_light_affect}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_light_affect**
= `0.0`
`🔗<class_Environment_property_ssao_light_affect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_direct_light_affect**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_direct_light_affect**()

The screen-space ambient occlusion intensity in direct light. In real
life, ambient occlusion only applies to indirect light, which means its
effects can\'t be seen in direct light. Values higher than `0` will make
the SSAO effect visible in direct light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_power}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_power** =
`1.5` `🔗<class_Environment_property_ssao_power>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_power**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_power**()

The distribution of occlusion. A higher value results in darker
occlusion, similar to
`ssao_intensity<class_Environment_property_ssao_intensity>`{.interpreted-text
role="ref"}, but with a sharper falloff.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_radius** =
`1.0` `🔗<class_Environment_property_ssao_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_radius**()

The distance at which objects can occlude each other when calculating
screen-space ambient occlusion. Higher values will result in occlusion
over a greater distance at the cost of performance and quality.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssao_sharpness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssao_sharpness** =
`0.98` `🔗<class_Environment_property_ssao_sharpness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssao_sharpness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssao_sharpness**()

The amount that the screen-space ambient occlusion effect is allowed to
blur over the edges of objects. Setting too high will result in aliasing
around the edges of objects. Setting too low will make object edges
appear blurry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssil_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ssil_enabled** =
`false` `🔗<class_Environment_property_ssil_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssil_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ssil_enabled**()

If `true`, the screen-space indirect lighting effect is enabled. Screen
space indirect lighting is a form of indirect lighting that allows
diffuse light to bounce between nearby objects. Screen-space indirect
lighting works very similarly to screen-space ambient occlusion, in that
it only affects a limited range. It is intended to be used along with a
form of proper global illumination like SDFGI or
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}. Screen-space
indirect lighting is not affected by individual light\'s
`Light3D.light_indirect_energy<class_Light3D_property_light_indirect_energy>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* SSIL is only supported in the Forward+ rendering method,
not Mobile or Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssil_intensity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssil_intensity** =
`1.0` `🔗<class_Environment_property_ssil_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssil_intensity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssil_intensity**()

The brightness multiplier for the screen-space indirect lighting effect.
A higher value will result in brighter light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssil_normal_rejection}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ssil_normal_rejection** = `1.0`
`🔗<class_Environment_property_ssil_normal_rejection>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssil_normal_rejection**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssil_normal_rejection**()

Amount of normal rejection used when calculating screen-space indirect
lighting. Normal rejection uses the normal of a given sample point to
reject samples that are facing away from the current pixel. Normal
rejection is necessary to avoid light leaking when only one side of an
object is illuminated. However, normal rejection can be disabled if
light leaking is desirable, such as when the scene mostly contains
emissive objects that emit light from faces that cannot be seen from the
camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssil_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssil_radius** =
`5.0` `🔗<class_Environment_property_ssil_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssil_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssil_radius**()

The distance that bounced lighting can travel when using the screen
space indirect lighting effect. A larger value will result in light
bouncing further in a scene, but may result in under-sampling artifacts
which look like long spikes surrounding light sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssil_sharpness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssil_sharpness** =
`0.98` `🔗<class_Environment_property_ssil_sharpness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssil_sharpness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssil_sharpness**()

The amount that the screen-space indirect lighting effect is allowed to
blur over the edges of objects. Setting too high will result in aliasing
around the edges of objects. Setting too low will make object edges
appear blurry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssr_depth_tolerance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ssr_depth_tolerance** = `0.2`
`🔗<class_Environment_property_ssr_depth_tolerance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssr_depth_tolerance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssr_depth_tolerance**()

The depth tolerance for screen-space reflections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssr_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ssr_enabled** =
`false` `🔗<class_Environment_property_ssr_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssr_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ssr_enabled**()

If `true`, screen-space reflections are enabled. Screen-space
reflections are more accurate than reflections from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s or
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}s,
but are slower and can\'t reflect surfaces occluded by others.

\*\*Note:\*\* SSR is only supported in the Forward+ rendering method,
not Mobile or Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssr_fade_in}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssr_fade_in** =
`0.15` `🔗<class_Environment_property_ssr_fade_in>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssr_fade_in**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssr_fade_in**()

The fade-in distance for screen-space reflections. Affects the area from
the reflected material to the screen-space reflection. Only positive
values are valid (negative values will be clamped to `0.0`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssr_fade_out}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ssr_fade_out** =
`2.0` `🔗<class_Environment_property_ssr_fade_out>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssr_fade_out**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ssr_fade_out**()

The fade-out distance for screen-space reflections. Affects the area
from the screen-space reflection to the \"global\" reflection. Only
positive values are valid (negative values will be clamped to `0.0`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_ssr_max_steps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **ssr_max_steps** = `64`
`🔗<class_Environment_property_ssr_max_steps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ssr_max_steps**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_ssr_max_steps**()

The maximum number of steps for screen-space reflections. Higher values
are slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_tonemap_exposure}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tonemap_exposure**
= `1.0`
`🔗<class_Environment_property_tonemap_exposure>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tonemap_exposure**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tonemap_exposure**()

Adjusts the brightness of values before they are provided to the
tonemapper. Higher
`tonemap_exposure<class_Environment_property_tonemap_exposure>`{.interpreted-text
role="ref"} values result in a brighter image. See also
`tonemap_white<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Values provided to the tonemapper will also be multiplied
by `2.0` and `1.8` for
`TONE_MAPPER_FILMIC<class_Environment_constant_TONE_MAPPER_FILMIC>`{.interpreted-text
role="ref"} and
`TONE_MAPPER_ACES<class_Environment_constant_TONE_MAPPER_ACES>`{.interpreted-text
role="ref"} respectively to produce a similar apparent brightness as
`TONE_MAPPER_LINEAR<class_Environment_constant_TONE_MAPPER_LINEAR>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_tonemap_mode}
::: rst-class
classref-property
:::
::::

`ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text role="ref"}
**tonemap_mode** = `0`
`🔗<class_Environment_property_tonemap_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tonemapper**(value:
  `ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text
  role="ref"})
- `ToneMapper<enum_Environment_ToneMapper>`{.interpreted-text
  role="ref"} **get_tonemapper**()

The tonemapping mode to use. Tonemapping is the process that
\"converts\" HDR values to be suitable for rendering on an LDR display.
(Godot doesn\'t support rendering on HDR displays yet.)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_tonemap_white}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tonemap_white** =
`1.0` `🔗<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tonemap_white**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tonemap_white**()

The white reference value for tonemapping, which indicates where bright
white is located in the scale of values provided to the tonemapper. For
photorealistic lighting, recommended values are between `6.0` and `8.0`.
Higher values result in less blown out highlights, but may make the
scene appear lower contrast. See also
`tonemap_exposure<class_Environment_property_tonemap_exposure>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`tonemap_white<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"} is ignored when using
`TONE_MAPPER_LINEAR<class_Environment_constant_TONE_MAPPER_LINEAR>`{.interpreted-text
role="ref"} or
`TONE_MAPPER_AGX<class_Environment_constant_TONE_MAPPER_AGX>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_albedo}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**volumetric_fog_albedo** = `Color(1, 1, 1, 1)`
`🔗<class_Environment_property_volumetric_fog_albedo>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_albedo**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_volumetric_fog_albedo**()

The `Color<class_Color>`{.interpreted-text role="ref"} of the volumetric
fog when interacting with lights. Mist and fog have an albedo close to
`Color(1, 1, 1, 1)` while smoke has a darker albedo.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_ambient_inject}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_ambient_inject** = `0.0`
`🔗<class_Environment_property_volumetric_fog_ambient_inject>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_ambient_inject**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_ambient_inject**()

Scales the strength of ambient light used in the volumetric fog. A value
of `0.0` means that ambient light will not impact the volumetric fog.
`volumetric_fog_ambient_inject<class_Environment_property_volumetric_fog_ambient_inject>`{.interpreted-text
role="ref"} has a small performance cost when set above `0.0`.

\*\*Note:\*\* This has no visible effect if
`volumetric_fog_density<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"} is `0.0` or if
`volumetric_fog_albedo<class_Environment_property_volumetric_fog_albedo>`{.interpreted-text
role="ref"} is a fully black color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_anisotropy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_anisotropy** = `0.2`
`🔗<class_Environment_property_volumetric_fog_anisotropy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_anisotropy**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_anisotropy**()

The direction of scattered light as it goes through the volumetric fog.
A value close to `1.0` means almost all light is scattered forward. A
value close to `0.0` means light is scattered equally in all directions.
A value close to `-1.0` means light is scattered mostly backward. Fog
and mist scatter light slightly forward, while smoke scatters light
equally in all directions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_density}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_density** = `0.05`
`🔗<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_density**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_density**()

The base *exponential* density of the volumetric fog. Set this to the
lowest density you want to have globally.
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}s can be used
to add to or subtract from this density in specific areas. Fog rendering
is exponential as in real life.

A value of `0.0` disables global volumetric fog while allowing
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}s to display
volumetric fog in specific areas.

To make volumetric fog work as a volumetric *lighting* solution, set
`volumetric_fog_density<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"} to the lowest non-zero value (`0.0001`) then increase
lights\'
`Light3D.light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>`{.interpreted-text
role="ref"} to values between `10000` and `100000` to compensate for the
very low density.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_detail_spread}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_detail_spread** = `2.0`
`🔗<class_Environment_property_volumetric_fog_detail_spread>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_detail_spread**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_detail_spread**()

The distribution of size down the length of the froxel buffer. A higher
value compresses the froxels closer to the camera and places more detail
closer to the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_emission}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**volumetric_fog_emission** = `Color(0, 0, 0, 1)`
`🔗<class_Environment_property_volumetric_fog_emission>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_emission**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_volumetric_fog_emission**()

The emitted light from the volumetric fog. Even with emission,
volumetric fog will not cast light onto other surfaces. Emission is
useful to establish an ambient color. As the volumetric fog effect uses
single-scattering only, fog tends to need a little bit of emission to
soften the harsh shadows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_emission_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_emission_energy** = `1.0`
`🔗<class_Environment_property_volumetric_fog_emission_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_emission_energy**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_emission_energy**()

The brightness of the emitted light from the volumetric fog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**volumetric_fog_enabled** = `false`
`🔗<class_Environment_property_volumetric_fog_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_volumetric_fog_enabled**()

Enables the volumetric fog effect. Volumetric fog uses a screen-aligned
froxel buffer to calculate accurate volumetric scattering in the short
to medium range. Volumetric fog interacts with
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}s and lights
to calculate localized and global fog. Volumetric fog uses a PBR
single-scattering model based on extinction, scattering, and emission
which it exposes to users as density, albedo, and emission.

\*\*Note:\*\* Volumetric fog is only supported in the Forward+ rendering
method, not Mobile or Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_gi_inject}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_gi_inject** = `1.0`
`🔗<class_Environment_property_volumetric_fog_gi_inject>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_gi_inject**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_gi_inject**()

Scales the strength of Global Illumination used in the volumetric fog\'s
albedo color. A value of `0.0` means that Global Illumination will not
impact the volumetric fog.
`volumetric_fog_gi_inject<class_Environment_property_volumetric_fog_gi_inject>`{.interpreted-text
role="ref"} has a small performance cost when set above `0.0`.

\*\*Note:\*\* This has no visible effect if
`volumetric_fog_density<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"} is `0.0` or if
`volumetric_fog_albedo<class_Environment_property_volumetric_fog_albedo>`{.interpreted-text
role="ref"} is a fully black color.

\*\*Note:\*\* Only `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} and SDFGI
(`sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) are taken into account when using
`volumetric_fog_gi_inject<class_Environment_property_volumetric_fog_gi_inject>`{.interpreted-text
role="ref"}. Global illumination from
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"},
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}
and SSIL (see
`ssil_enabled<class_Environment_property_ssil_enabled>`{.interpreted-text
role="ref"}) will be ignored by volumetric fog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_length** = `64.0`
`🔗<class_Environment_property_volumetric_fog_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_length**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_length**()

The distance over which the volumetric fog is computed. Increase to
compute fog over a greater range, decrease to add more detail when a
long range is not needed. For best quality fog, keep this as low as
possible. See also
`ProjectSettings.rendering/environment/volumetric_fog/volume_depth<class_ProjectSettings_property_rendering/environment/volumetric_fog/volume_depth>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_sky_affect}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_sky_affect** = `1.0`
`🔗<class_Environment_property_volumetric_fog_sky_affect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_sky_affect**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_sky_affect**()

The factor to use when affecting the sky with volumetric fog. `1.0`
means that volumetric fog can fully obscure the sky. Lower values reduce
the impact of volumetric fog on sky rendering, with `0.0` not affecting
sky rendering at all.

\*\*Note:\*\*
`volumetric_fog_sky_affect<class_Environment_property_volumetric_fog_sky_affect>`{.interpreted-text
role="ref"} also affects `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}s, even if
`volumetric_fog_density<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"} is `0.0`. If you notice
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}s are
disappearing when looking towards the sky, set
`volumetric_fog_sky_affect<class_Environment_property_volumetric_fog_sky_affect>`{.interpreted-text
role="ref"} to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_temporal_reprojection_amount}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**volumetric_fog_temporal_reprojection_amount** = `0.9`
`🔗<class_Environment_property_volumetric_fog_temporal_reprojection_amount>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_temporal_reprojection_amount**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volumetric_fog_temporal_reprojection_amount**()

The amount by which to blend the last frame with the current frame. A
higher number results in smoother volumetric fog, but makes \"ghosting\"
much worse. A lower value reduces ghosting but can result in the
per-frame temporal jitter becoming visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_property_volumetric_fog_temporal_reprojection_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**volumetric_fog_temporal_reprojection_enabled** = `true`
`🔗<class_Environment_property_volumetric_fog_temporal_reprojection_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volumetric_fog_temporal_reprojection_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_volumetric_fog_temporal_reprojection_enabled**()

Enables temporal reprojection in the volumetric fog. Temporal
reprojection blends the current frame\'s volumetric fog with the last
frame\'s volumetric fog to smooth out jagged edges. The performance cost
is minimal; however, it leads to moving
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}s and
`Light3D<class_Light3D>`{.interpreted-text role="ref"}s \"ghosting\" and
leaving a trail behind them. When temporal reprojection is enabled, try
to avoid moving `FogVolume<class_FogVolume>`{.interpreted-text
role="ref"}s or `Light3D<class_Light3D>`{.interpreted-text role="ref"}s
too fast. Short-lived dynamic lighting effects should have
`Light3D.light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>`{.interpreted-text
role="ref"} set to `0.0` to avoid ghosting.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Environment_method_get_glow_level}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_glow_level**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Environment_method_get_glow_level>`{.interpreted-text
role="ref"}

Returns the intensity of the glow level `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Environment_method_set_glow_level}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_glow_level**(idx: `int<class_int>`{.interpreted-text role="ref"},
intensity: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Environment_method_set_glow_level>`{.interpreted-text
role="ref"}

Sets the intensity of the glow level `idx`. A value above `0.0` enables
the level. Each level relies on the previous level. This means that
enabling higher glow levels will slow down the glow effect rendering,
even if previous levels aren\'t enabled.
