github_url
:   hide

# RDSamplerState {#class_RDSamplerState}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Sampler state (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

This object is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

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

:::: {#class_RDSamplerState_property_anisotropy_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anisotropy_max** =
`1.0`
`🔗<class_RDSamplerState_property_anisotropy_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_anisotropy_max**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_anisotropy_max**()

Maximum anisotropy that can be used when sampling. Only effective if
`use_anisotropy<class_RDSamplerState_property_use_anisotropy>`{.interpreted-text
role="ref"} is `true`. Higher values result in a sharper sampler at
oblique angles, at the cost of performance (due to memory bandwidth).
This value may be limited by the graphics hardware in use. Most graphics
hardware only supports values up to `16.0`.

If
`anisotropy_max<class_RDSamplerState_property_anisotropy_max>`{.interpreted-text
role="ref"} is `1.0`, forcibly disables anisotropy even if
`use_anisotropy<class_RDSamplerState_property_use_anisotropy>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_border_color}
::: rst-class
classref-property
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **border_color** = `2`
`🔗<class_RDSamplerState_property_border_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_color**(value:
  `SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
  role="ref"})
- `SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
  role="ref"} **get_border_color**()

The border color that will be returned when sampling outside the
sampler\'s bounds and the
`repeat_u<class_RDSamplerState_property_repeat_u>`{.interpreted-text
role="ref"},
`repeat_v<class_RDSamplerState_property_repeat_v>`{.interpreted-text
role="ref"} or
`repeat_w<class_RDSamplerState_property_repeat_w>`{.interpreted-text
role="ref"} modes have repeating disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_compare_op}
::: rst-class
classref-property
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **compare_op** = `7`
`🔗<class_RDSamplerState_property_compare_op>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_compare_op**(value:
  `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"})
- `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"} **get_compare_op**()

The compare operation to use. Only effective if
`enable_compare<class_RDSamplerState_property_enable_compare>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_enable_compare}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_compare** =
`false`
`🔗<class_RDSamplerState_property_enable_compare>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_compare**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_compare**()

If `true`, returned values will be based on the comparison operation
defined in
`compare_op<class_RDSamplerState_property_compare_op>`{.interpreted-text
role="ref"}. This is a hardware-based approach and is therefore faster
than performing this manually in a shader. For example, compare
operations are used for shadow map rendering by comparing depth values
from a shadow sampler.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_lod_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lod_bias** = `0.0`
`🔗<class_RDSamplerState_property_lod_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lod_bias**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_lod_bias**()

The mipmap LOD bias to use. Positive values will make the sampler
blurrier at a given distance, while negative values will make the
sampler sharper at a given distance (at the risk of looking grainy).
Recommended values are between `-0.5` and `0.0`. Only effective if the
sampler has mipmaps available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_mag_filter}
::: rst-class
classref-property
:::
::::

`SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
role="ref"} **mag_filter** = `0`
`🔗<class_RDSamplerState_property_mag_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mag_filter**(value:
  `SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
  role="ref"})
- `SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
  role="ref"} **get_mag_filter**()

The sampler\'s magnification filter. It is the filtering method used
when sampling texels that appear bigger than on-screen pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_max_lod}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_lod** = `1e+20`
`🔗<class_RDSamplerState_property_max_lod>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_lod**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max_lod**()

The maximum mipmap LOD bias to display (lowest resolution). Only
effective if the sampler has mipmaps available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_min_filter}
::: rst-class
classref-property
:::
::::

`SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
role="ref"} **min_filter** = `0`
`🔗<class_RDSamplerState_property_min_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_filter**(value:
  `SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
  role="ref"})
- `SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
  role="ref"} **get_min_filter**()

The sampler\'s minification filter. It is the filtering method used when
sampling texels that appear smaller than on-screen pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_min_lod}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **min_lod** = `0.0`
`🔗<class_RDSamplerState_property_min_lod>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_lod**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_min_lod**()

The minimum mipmap LOD bias to display (highest resolution). Only
effective if the sampler has mipmaps available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_mip_filter}
::: rst-class
classref-property
:::
::::

`SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
role="ref"} **mip_filter** = `0`
`🔗<class_RDSamplerState_property_mip_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mip_filter**(value:
  `SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
  role="ref"})
- `SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
  role="ref"} **get_mip_filter**()

The filtering method to use for mipmaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_repeat_u}
::: rst-class
classref-property
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **repeat_u** = `2`
`🔗<class_RDSamplerState_property_repeat_u>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_repeat_u**(value:
  `SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
  role="ref"})
- `SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
  role="ref"} **get_repeat_u**()

The repeat mode to use along the U axis of UV coordinates. This affects
the returned values if sampling outside the UV bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_repeat_v}
::: rst-class
classref-property
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **repeat_v** = `2`
`🔗<class_RDSamplerState_property_repeat_v>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_repeat_v**(value:
  `SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
  role="ref"})
- `SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
  role="ref"} **get_repeat_v**()

The repeat mode to use along the V axis of UV coordinates. This affects
the returned values if sampling outside the UV bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_repeat_w}
::: rst-class
classref-property
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **repeat_w** = `2`
`🔗<class_RDSamplerState_property_repeat_w>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_repeat_w**(value:
  `SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
  role="ref"})
- `SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
  role="ref"} **get_repeat_w**()

The repeat mode to use along the W axis of UV coordinates. This affects
the returned values if sampling outside the UV bounds. Only effective
for 3D samplers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_unnormalized_uvw}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **unnormalized_uvw** =
`false`
`🔗<class_RDSamplerState_property_unnormalized_uvw>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_unnormalized_uvw**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_unnormalized_uvw**()

If `true`, the texture will be sampled with coordinates ranging from 0
to the texture\'s resolution. Otherwise, the coordinates will be
normalized and range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDSamplerState_property_use_anisotropy}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_anisotropy** =
`false`
`🔗<class_RDSamplerState_property_use_anisotropy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_anisotropy**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_anisotropy**()

If `true`, perform anisotropic sampling. See
`anisotropy_max<class_RDSamplerState_property_anisotropy_max>`{.interpreted-text
role="ref"}.
