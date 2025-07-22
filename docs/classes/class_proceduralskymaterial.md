github_url
:   hide

# ProceduralSkyMaterial {#class_ProceduralSkyMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A material that defines a simple sky for a
`Sky<class_Sky>`{.interpreted-text role="ref"} resource.

::: rst-class
classref-introduction-group
:::

## Description

**ProceduralSkyMaterial** provides a way to create an effective
background quickly by defining procedural parameters for the sun, the
sky and the ground. The sky and ground are defined by a main color, a
color at the horizon, and an easing curve to interpolate between them.
Suns are described by a position in the sky, a color, and a max angle
from the sun at which the easing curve ends. The max angle therefore
defines the size of the sun in the sky.

\*\*ProceduralSkyMaterial\*\* supports up to 4 suns, using the color,
and energy, direction, and angular distance of the first four
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"} nodes in the scene. This means that the suns are defined
individually by the properties of their corresponding
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s and globally by
`sun_angle_max<class_ProceduralSkyMaterial_property_sun_angle_max>`{.interpreted-text
role="ref"} and
`sun_curve<class_ProceduralSkyMaterial_property_sun_curve>`{.interpreted-text
role="ref"}.

\*\*ProceduralSkyMaterial\*\* uses a lightweight shader to draw the sky
and is therefore suited for real-time updates. This makes it a great
option for a sky that is simple and computationally cheap, but
unrealistic. If you need a more realistic procedural option, use
`PhysicalSkyMaterial<class_PhysicalSkyMaterial>`{.interpreted-text
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

:::: {#class_ProceduralSkyMaterial_property_energy_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **energy_multiplier**
= `1.0`
`🔗<class_ProceduralSkyMaterial_property_energy_multiplier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_energy_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_energy_multiplier**()

The sky\'s overall brightness multiplier. Higher values result in a
brighter sky.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_ground_bottom_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**ground_bottom_color** = `Color(0.2, 0.169, 0.133, 1)`
`🔗<class_ProceduralSkyMaterial_property_ground_bottom_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ground_bottom_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_ground_bottom_color**()

Color of the ground at the bottom. Blends with
`ground_horizon_color<class_ProceduralSkyMaterial_property_ground_horizon_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_ground_curve}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ground_curve** =
`0.02`
`🔗<class_ProceduralSkyMaterial_property_ground_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ground_curve**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ground_curve**()

How quickly the
`ground_horizon_color<class_ProceduralSkyMaterial_property_ground_horizon_color>`{.interpreted-text
role="ref"} fades into the
`ground_bottom_color<class_ProceduralSkyMaterial_property_ground_bottom_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_ground_energy_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ground_energy_multiplier** = `1.0`
`🔗<class_ProceduralSkyMaterial_property_ground_energy_multiplier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ground_energy_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ground_energy_multiplier**()

Multiplier for ground color. A higher value will make the ground
brighter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_ground_horizon_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**ground_horizon_color** = `Color(0.6463, 0.6558, 0.6708, 1)`
`🔗<class_ProceduralSkyMaterial_property_ground_horizon_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ground_horizon_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_ground_horizon_color**()

Color of the ground at the horizon. Blends with
`ground_bottom_color<class_ProceduralSkyMaterial_property_ground_bottom_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sky_cover}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **sky_cover**
`🔗<class_ProceduralSkyMaterial_property_sky_cover>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_cover**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_sky_cover**()

The sky cover texture to use. This texture must use an equirectangular
projection (similar to
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"}). The texture\'s colors will be *added* to the existing sky
color, and will be multiplied by
`sky_energy_multiplier<class_ProceduralSkyMaterial_property_sky_energy_multiplier>`{.interpreted-text
role="ref"} and
`sky_cover_modulate<class_ProceduralSkyMaterial_property_sky_cover_modulate>`{.interpreted-text
role="ref"}. This is mainly suited to displaying stars at night, but it
can also be used to display clouds at day or night (with a
non-physically-accurate look).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sky_cover_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**sky_cover_modulate** = `Color(1, 1, 1, 1)`
`🔗<class_ProceduralSkyMaterial_property_sky_cover_modulate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_cover_modulate**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_sky_cover_modulate**()

The tint to apply to the
`sky_cover<class_ProceduralSkyMaterial_property_sky_cover>`{.interpreted-text
role="ref"} texture. This can be used to change the sky cover\'s colors
or opacity independently of the sky energy, which is useful for
day/night or weather transitions. Only effective if a texture is defined
in
`sky_cover<class_ProceduralSkyMaterial_property_sky_cover>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sky_curve}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sky_curve** =
`0.15`
`🔗<class_ProceduralSkyMaterial_property_sky_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_curve**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_sky_curve**()

How quickly the
`sky_horizon_color<class_ProceduralSkyMaterial_property_sky_horizon_color>`{.interpreted-text
role="ref"} fades into the
`sky_top_color<class_ProceduralSkyMaterial_property_sky_top_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sky_energy_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sky_energy_multiplier** = `1.0`
`🔗<class_ProceduralSkyMaterial_property_sky_energy_multiplier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_energy_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sky_energy_multiplier**()

Multiplier for sky color. A higher value will make the sky brighter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sky_horizon_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **sky_horizon_color**
= `Color(0.6463, 0.6558, 0.6708, 1)`
`🔗<class_ProceduralSkyMaterial_property_sky_horizon_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_horizon_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_sky_horizon_color**()

Color of the sky at the horizon. Blends with
`sky_top_color<class_ProceduralSkyMaterial_property_sky_top_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sky_top_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **sky_top_color** =
`Color(0.385, 0.454, 0.55, 1)`
`🔗<class_ProceduralSkyMaterial_property_sky_top_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_top_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_sky_top_color**()

Color of the sky at the top. Blends with
`sky_horizon_color<class_ProceduralSkyMaterial_property_sky_horizon_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sun_angle_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sun_angle_max** =
`30.0`
`🔗<class_ProceduralSkyMaterial_property_sun_angle_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sun_angle_max**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sun_angle_max**()

Distance from center of sun where it fades out completely.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_sun_curve}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sun_curve** =
`0.15`
`🔗<class_ProceduralSkyMaterial_property_sun_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sun_curve**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_sun_curve**()

How quickly the sun fades away between the edge of the sun disk and
`sun_angle_max<class_ProceduralSkyMaterial_property_sun_angle_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProceduralSkyMaterial_property_use_debanding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_debanding** =
`true`
`🔗<class_ProceduralSkyMaterial_property_use_debanding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_debanding**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_debanding**()

If `true`, enables debanding. Debanding adds a small amount of noise
which helps reduce banding that appears from the smooth changes in color
in the sky.
