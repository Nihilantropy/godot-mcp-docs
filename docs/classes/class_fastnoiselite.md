github_url
:   hide

# FastNoiseLite {#class_FastNoiseLite}

**Inherits:** `Noise<class_Noise>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Generates noise using the FastNoiseLite library.

::: rst-class
classref-introduction-group
:::

## Description

This class generates noise using the FastNoiseLite library, which is a
collection of several noise algorithms including Cellular, Perlin,
Value, and more.

Most generated noise values are in the range of `[-1, 1]`, but not
always. Some of the cellular noise algorithms return results above `1`.

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

:::: {#enum_FastNoiseLite_NoiseType}
::: rst-class
classref-enumeration
:::
::::

enum **NoiseType**: `🔗<enum_FastNoiseLite_NoiseType>`{.interpreted-text
role="ref"}

:::: {#class_FastNoiseLite_constant_TYPE_VALUE}
::: rst-class
classref-enumeration-constant
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**TYPE_VALUE** = `5`

A lattice of points are assigned random values then interpolated based
on neighboring values.

:::: {#class_FastNoiseLite_constant_TYPE_VALUE_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**TYPE_VALUE_CUBIC** = `4`

Similar to value noise
(`TYPE_VALUE<class_FastNoiseLite_constant_TYPE_VALUE>`{.interpreted-text
role="ref"}), but slower. Has more variance in peaks and valleys.

Cubic noise can be used to avoid certain artifacts when using value
noise to create a bumpmap. In general, you should always use this mode
if the value noise is being used for a heightmap or bumpmap.

:::: {#class_FastNoiseLite_constant_TYPE_PERLIN}
::: rst-class
classref-enumeration-constant
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**TYPE_PERLIN** = `3`

A lattice of random gradients. Their dot products are interpolated to
obtain values in between the lattices.

:::: {#class_FastNoiseLite_constant_TYPE_CELLULAR}
::: rst-class
classref-enumeration-constant
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**TYPE_CELLULAR** = `2`

Cellular includes both Worley noise and Voronoi diagrams which creates
various regions of the same value.

:::: {#class_FastNoiseLite_constant_TYPE_SIMPLEX}
::: rst-class
classref-enumeration-constant
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**TYPE_SIMPLEX** = `0`

As opposed to
`TYPE_PERLIN<class_FastNoiseLite_constant_TYPE_PERLIN>`{.interpreted-text
role="ref"}, gradients exist in a simplex lattice rather than a grid
lattice, avoiding directional artifacts. Internally uses
FastNoiseLite\'s OpenSimplex2 noise type.

:::: {#class_FastNoiseLite_constant_TYPE_SIMPLEX_SMOOTH}
::: rst-class
classref-enumeration-constant
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**TYPE_SIMPLEX_SMOOTH** = `1`

Modified, higher quality version of
`TYPE_SIMPLEX<class_FastNoiseLite_constant_TYPE_SIMPLEX>`{.interpreted-text
role="ref"}, but slower. Internally uses FastNoiseLite\'s OpenSimplex2S
noise type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FastNoiseLite_FractalType}
::: rst-class
classref-enumeration
:::
::::

enum **FractalType**:
`🔗<enum_FastNoiseLite_FractalType>`{.interpreted-text role="ref"}

:::: {#class_FastNoiseLite_constant_FRACTAL_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
role="ref"} **FRACTAL_NONE** = `0`

No fractal noise.

:::: {#class_FastNoiseLite_constant_FRACTAL_FBM}
::: rst-class
classref-enumeration-constant
:::
::::

`FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
role="ref"} **FRACTAL_FBM** = `1`

Method using Fractional Brownian Motion to combine octaves into a
fractal.

:::: {#class_FastNoiseLite_constant_FRACTAL_RIDGED}
::: rst-class
classref-enumeration-constant
:::
::::

`FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
role="ref"} **FRACTAL_RIDGED** = `2`

Method of combining octaves into a fractal resulting in a \"ridged\"
look.

:::: {#class_FastNoiseLite_constant_FRACTAL_PING_PONG}
::: rst-class
classref-enumeration-constant
:::
::::

`FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
role="ref"} **FRACTAL_PING_PONG** = `3`

Method of combining octaves into a fractal with a ping pong effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FastNoiseLite_CellularDistanceFunction}
::: rst-class
classref-enumeration
:::
::::

enum **CellularDistanceFunction**:
`🔗<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
role="ref"}

:::: {#class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
role="ref"} **DISTANCE_EUCLIDEAN** = `0`

Euclidean distance to the nearest point.

:::: {#class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN_SQUARED}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
role="ref"} **DISTANCE_EUCLIDEAN_SQUARED** = `1`

Squared Euclidean distance to the nearest point.

:::: {#class_FastNoiseLite_constant_DISTANCE_MANHATTAN}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
role="ref"} **DISTANCE_MANHATTAN** = `2`

Manhattan distance (taxicab metric) to the nearest point.

:::: {#class_FastNoiseLite_constant_DISTANCE_HYBRID}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
role="ref"} **DISTANCE_HYBRID** = `3`

Blend of
`DISTANCE_EUCLIDEAN<class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN>`{.interpreted-text
role="ref"} and
`DISTANCE_MANHATTAN<class_FastNoiseLite_constant_DISTANCE_MANHATTAN>`{.interpreted-text
role="ref"} to give curved cell boundaries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FastNoiseLite_CellularReturnType}
::: rst-class
classref-enumeration
:::
::::

enum **CellularReturnType**:
`🔗<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"}

:::: {#class_FastNoiseLite_constant_RETURN_CELL_VALUE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_CELL_VALUE** = `0`

The cellular distance function will return the same value for all points
within a cell.

:::: {#class_FastNoiseLite_constant_RETURN_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_DISTANCE** = `1`

The cellular distance function will return a value determined by the
distance to the nearest point.

:::: {#class_FastNoiseLite_constant_RETURN_DISTANCE2}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_DISTANCE2** = `2`

The cellular distance function returns the distance to the
second-nearest point.

:::: {#class_FastNoiseLite_constant_RETURN_DISTANCE2_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_DISTANCE2_ADD** = `3`

The distance to the nearest point is added to the distance to the
second-nearest point.

:::: {#class_FastNoiseLite_constant_RETURN_DISTANCE2_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_DISTANCE2_SUB** = `4`

The distance to the nearest point is subtracted from the distance to the
second-nearest point.

:::: {#class_FastNoiseLite_constant_RETURN_DISTANCE2_MUL}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_DISTANCE2_MUL** = `5`

The distance to the nearest point is multiplied with the distance to the
second-nearest point.

:::: {#class_FastNoiseLite_constant_RETURN_DISTANCE2_DIV}
::: rst-class
classref-enumeration-constant
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **RETURN_DISTANCE2_DIV** = `6`

The distance to the nearest point is divided by the distance to the
second-nearest point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FastNoiseLite_DomainWarpType}
::: rst-class
classref-enumeration
:::
::::

enum **DomainWarpType**:
`🔗<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text role="ref"}

:::: {#class_FastNoiseLite_constant_DOMAIN_WARP_SIMPLEX}
::: rst-class
classref-enumeration-constant
:::
::::

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text
role="ref"} **DOMAIN_WARP_SIMPLEX** = `0`

The domain is warped using the simplex noise algorithm.

:::: {#class_FastNoiseLite_constant_DOMAIN_WARP_SIMPLEX_REDUCED}
::: rst-class
classref-enumeration-constant
:::
::::

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text
role="ref"} **DOMAIN_WARP_SIMPLEX_REDUCED** = `1`

The domain is warped using a simplified version of the simplex noise
algorithm.

:::: {#class_FastNoiseLite_constant_DOMAIN_WARP_BASIC_GRID}
::: rst-class
classref-enumeration-constant
:::
::::

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text
role="ref"} **DOMAIN_WARP_BASIC_GRID** = `2`

The domain is warped using a simple noise grid (not as smooth as the
other methods, but more performant).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FastNoiseLite_DomainWarpFractalType}
::: rst-class
classref-enumeration
:::
::::

enum **DomainWarpFractalType**:
`🔗<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
role="ref"}

:::: {#class_FastNoiseLite_constant_DOMAIN_WARP_FRACTAL_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
role="ref"} **DOMAIN_WARP_FRACTAL_NONE** = `0`

No fractal noise for warping the space.

:::: {#class_FastNoiseLite_constant_DOMAIN_WARP_FRACTAL_PROGRESSIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
role="ref"} **DOMAIN_WARP_FRACTAL_PROGRESSIVE** = `1`

Warping the space progressively, octave for octave, resulting in a more
\"liquified\" distortion.

:::: {#class_FastNoiseLite_constant_DOMAIN_WARP_FRACTAL_INDEPENDENT}
::: rst-class
classref-enumeration-constant
:::
::::

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
role="ref"} **DOMAIN_WARP_FRACTAL_INDEPENDENT** = `2`

Warping the space independently for each octave, resulting in a more
chaotic distortion.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_FastNoiseLite_property_cellular_distance_function}
::: rst-class
classref-property
:::
::::

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
role="ref"} **cellular_distance_function** = `0`
`🔗<class_FastNoiseLite_property_cellular_distance_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cellular_distance_function**(value:
  `CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
  role="ref"})
- `CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`{.interpreted-text
  role="ref"} **get_cellular_distance_function**()

Determines how the distance to the nearest/second-nearest point is
computed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_cellular_jitter}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cellular_jitter** =
`1.0`
`🔗<class_FastNoiseLite_property_cellular_jitter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cellular_jitter**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_cellular_jitter**()

Maximum distance a point can move off of its grid position. Set to `0`
for an even grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_cellular_return_type}
::: rst-class
classref-property
:::
::::

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
role="ref"} **cellular_return_type** = `1`
`🔗<class_FastNoiseLite_property_cellular_return_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cellular_return_type**(value:
  `CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
  role="ref"})
- `CellularReturnType<enum_FastNoiseLite_CellularReturnType>`{.interpreted-text
  role="ref"} **get_cellular_return_type**()

Return type from cellular noise calculations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_amplitude}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**domain_warp_amplitude** = `30.0`
`🔗<class_FastNoiseLite_property_domain_warp_amplitude>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_amplitude**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_domain_warp_amplitude**()

Sets the maximum warp distance from the origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **domain_warp_enabled**
= `false`
`🔗<class_FastNoiseLite_property_domain_warp_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_domain_warp_enabled**()

If enabled, another FastNoiseLite instance is used to warp the space,
resulting in a distortion of the noise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_fractal_gain}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**domain_warp_fractal_gain** = `0.5`
`🔗<class_FastNoiseLite_property_domain_warp_fractal_gain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_fractal_gain**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_domain_warp_fractal_gain**()

Determines the strength of each subsequent layer of the noise which is
used to warp the space.

A low value places more emphasis on the lower frequency base layers,
while a high value puts more emphasis on the higher frequency layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_fractal_lacunarity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**domain_warp_fractal_lacunarity** = `6.0`
`🔗<class_FastNoiseLite_property_domain_warp_fractal_lacunarity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_fractal_lacunarity**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_domain_warp_fractal_lacunarity**()

The change in frequency between octaves, also known as \"lacunarity\",
of the fractal noise which warps the space. Increasing this value
results in higher octaves, producing noise with finer details and a
rougher appearance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_fractal_octaves}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**domain_warp_fractal_octaves** = `5`
`🔗<class_FastNoiseLite_property_domain_warp_fractal_octaves>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_fractal_octaves**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_domain_warp_fractal_octaves**()

The number of noise layers that are sampled to get the final value for
the fractal noise which warps the space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_fractal_type}
::: rst-class
classref-property
:::
::::

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
role="ref"} **domain_warp_fractal_type** = `1`
`🔗<class_FastNoiseLite_property_domain_warp_fractal_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_fractal_type**(value:
  `DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
  role="ref"})
- `DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`{.interpreted-text
  role="ref"} **get_domain_warp_fractal_type**()

The method for combining octaves into a fractal which is used to warp
the space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_frequency}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**domain_warp_frequency** = `0.05`
`🔗<class_FastNoiseLite_property_domain_warp_frequency>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_frequency**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_domain_warp_frequency**()

Frequency of the noise which warps the space. Low frequency results in
smooth noise while high frequency results in rougher, more granular
noise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_domain_warp_type}
::: rst-class
classref-property
:::
::::

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text
role="ref"} **domain_warp_type** = `0`
`🔗<class_FastNoiseLite_property_domain_warp_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_domain_warp_type**(value:
  `DomainWarpType<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text
  role="ref"})
- `DomainWarpType<enum_FastNoiseLite_DomainWarpType>`{.interpreted-text
  role="ref"} **get_domain_warp_type**()

The warp algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_fractal_gain}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fractal_gain** =
`0.5` `🔗<class_FastNoiseLite_property_fractal_gain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractal_gain**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fractal_gain**()

Determines the strength of each subsequent layer of noise in fractal
noise.

A low value places more emphasis on the lower frequency base layers,
while a high value puts more emphasis on the higher frequency layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_fractal_lacunarity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**fractal_lacunarity** = `2.0`
`🔗<class_FastNoiseLite_property_fractal_lacunarity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractal_lacunarity**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fractal_lacunarity**()

Frequency multiplier between subsequent octaves. Increasing this value
results in higher octaves producing noise with finer details and a
rougher appearance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_fractal_octaves}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fractal_octaves** = `5`
`🔗<class_FastNoiseLite_property_fractal_octaves>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractal_octaves**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_fractal_octaves**()

The number of noise layers that are sampled to get the final value for
fractal noise types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_fractal_ping_pong_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**fractal_ping_pong_strength** = `2.0`
`🔗<class_FastNoiseLite_property_fractal_ping_pong_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractal_ping_pong_strength**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fractal_ping_pong_strength**()

Sets the strength of the fractal ping pong type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_fractal_type}
::: rst-class
classref-property
:::
::::

`FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
role="ref"} **fractal_type** = `1`
`🔗<class_FastNoiseLite_property_fractal_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractal_type**(value:
  `FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
  role="ref"})
- `FractalType<enum_FastNoiseLite_FractalType>`{.interpreted-text
  role="ref"} **get_fractal_type**()

The method for combining octaves into a fractal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_fractal_weighted_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**fractal_weighted_strength** = `0.0`
`🔗<class_FastNoiseLite_property_fractal_weighted_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractal_weighted_strength**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fractal_weighted_strength**()

Higher weighting means higher octaves have less impact if lower octaves
have a large impact.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_frequency}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **frequency** =
`0.01` `🔗<class_FastNoiseLite_property_frequency>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frequency**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_frequency**()

The frequency for all noise types. Low frequency results in smooth noise
while high frequency results in rougher, more granular noise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_noise_type}
::: rst-class
classref-property
:::
::::

`NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text role="ref"}
**noise_type** = `1`
`🔗<class_FastNoiseLite_property_noise_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_noise_type**(value:
  `NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text
  role="ref"})
- `NoiseType<enum_FastNoiseLite_NoiseType>`{.interpreted-text
  role="ref"} **get_noise_type**()

The noise algorithm used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **offset** =
`Vector3(0, 0, 0)`
`🔗<class_FastNoiseLite_property_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_offset**()

Translate the noise input coordinates by the given
`Vector3<class_Vector3>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FastNoiseLite_property_seed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **seed** = `0`
`🔗<class_FastNoiseLite_property_seed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_seed**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_seed**()

The random number seed for all noise types.
