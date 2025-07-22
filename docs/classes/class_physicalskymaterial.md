github_url
:   hide

# PhysicalSkyMaterial {#class_PhysicalSkyMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A material that defines a sky for a `Sky<class_Sky>`{.interpreted-text
role="ref"} resource by a set of physical properties.

::: rst-class
classref-introduction-group
:::

## Description

The **PhysicalSkyMaterial** uses the Preetham analytic daylight model to
draw a sky based on physical properties. This results in a substantially
more realistic sky than the
`ProceduralSkyMaterial<class_ProceduralSkyMaterial>`{.interpreted-text
role="ref"}, but it is slightly slower and less flexible.

The **PhysicalSkyMaterial** only supports one sun. The color, energy,
and direction of the sun are taken from the first
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"} in the scene tree.

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

:::: {#class_PhysicalSkyMaterial_property_energy_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **energy_multiplier**
= `1.0`
`🔗<class_PhysicalSkyMaterial_property_energy_multiplier>`{.interpreted-text
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

:::: {#class_PhysicalSkyMaterial_property_ground_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **ground_color** =
`Color(0.1, 0.07, 0.034, 1)`
`🔗<class_PhysicalSkyMaterial_property_ground_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ground_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_ground_color**()

Modulates the `Color<class_Color>`{.interpreted-text role="ref"} on the
bottom half of the sky to represent the ground.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_mie_coefficient}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mie_coefficient** =
`0.005`
`🔗<class_PhysicalSkyMaterial_property_mie_coefficient>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mie_coefficient**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_mie_coefficient**()

Controls the strength of [Mie
scattering](https://en.wikipedia.org/wiki/Mie_scattering) for the sky.
Mie scattering results from light colliding with larger particles (like
water). On earth, Mie scattering results in a whitish color around the
sun and horizon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_mie_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **mie_color** =
`Color(0.69, 0.729, 0.812, 1)`
`🔗<class_PhysicalSkyMaterial_property_mie_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mie_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_mie_color**()

Controls the `Color<class_Color>`{.interpreted-text role="ref"} of the
[Mie scattering](https://en.wikipedia.org/wiki/Mie_scattering) effect.
While not physically accurate, this allows for the creation of
alien-looking planets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_mie_eccentricity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mie_eccentricity**
= `0.8`
`🔗<class_PhysicalSkyMaterial_property_mie_eccentricity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mie_eccentricity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_mie_eccentricity**()

Controls the direction of the [Mie
scattering](https://en.wikipedia.org/wiki/Mie_scattering). A value of
`1` means that when light hits a particle it\'s passing through straight
forward. A value of `-1` means that all light is scatter backwards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_night_sky}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **night_sky**
`🔗<class_PhysicalSkyMaterial_property_night_sky>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_night_sky**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_night_sky**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} for the night
sky. This is added to the sky, so if it is bright enough, it may be
visible during the day.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_rayleigh_coefficient}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rayleigh_coefficient** = `2.0`
`🔗<class_PhysicalSkyMaterial_property_rayleigh_coefficient>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rayleigh_coefficient**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_rayleigh_coefficient**()

Controls the strength of the [Rayleigh
scattering](https://en.wikipedia.org/wiki/Rayleigh_scattering). Rayleigh
scattering results from light colliding with small particles. It is
responsible for the blue color of the sky.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_rayleigh_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **rayleigh_color** =
`Color(0.3, 0.405, 0.6, 1)`
`🔗<class_PhysicalSkyMaterial_property_rayleigh_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rayleigh_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_rayleigh_color**()

Controls the `Color<class_Color>`{.interpreted-text role="ref"} of the
[Rayleigh
scattering](https://en.wikipedia.org/wiki/Rayleigh_scattering). While
not physically accurate, this allows for the creation of alien-looking
planets. For example, setting this to a red
`Color<class_Color>`{.interpreted-text role="ref"} results in a
Mars-looking atmosphere with a corresponding blue sunset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_sun_disk_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sun_disk_scale** =
`1.0`
`🔗<class_PhysicalSkyMaterial_property_sun_disk_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sun_disk_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sun_disk_scale**()

Sets the size of the sun disk. Default value is based on Sol\'s
perceived size from Earth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_turbidity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **turbidity** =
`10.0`
`🔗<class_PhysicalSkyMaterial_property_turbidity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_turbidity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_turbidity**()

Sets the thickness of the atmosphere. High turbidity creates a
foggy-looking atmosphere, while a low turbidity results in a clearer
atmosphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalSkyMaterial_property_use_debanding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_debanding** =
`true`
`🔗<class_PhysicalSkyMaterial_property_use_debanding>`{.interpreted-text
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
