github_url
:   hide

# RDPipelineMultisampleState {#class_RDPipelineMultisampleState}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Pipeline multisample state (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

**RDPipelineMultisampleState** is used to control how multisample or
supersample antialiasing is being performed when rendering using
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

:::: {#class_RDPipelineMultisampleState_property_enable_alpha_to_coverage}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**enable_alpha_to_coverage** = `false`
`🔗<class_RDPipelineMultisampleState_property_enable_alpha_to_coverage>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_alpha_to_coverage**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_alpha_to_coverage**()

If `true`, alpha to coverage is enabled. This generates a temporary
coverage value based on the alpha component of the fragment\'s first
color output. This allows alpha transparency to make use of multisample
antialiasing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineMultisampleState_property_enable_alpha_to_one}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_alpha_to_one**
= `false`
`🔗<class_RDPipelineMultisampleState_property_enable_alpha_to_one>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_alpha_to_one**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_alpha_to_one**()

If `true`, alpha is forced to either `0.0` or `1.0`. This allows
hardening the edges of antialiased alpha transparencies. Only relevant
if
`enable_alpha_to_coverage<class_RDPipelineMultisampleState_property_enable_alpha_to_coverage>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineMultisampleState_property_enable_sample_shading}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**enable_sample_shading** = `false`
`🔗<class_RDPipelineMultisampleState_property_enable_sample_shading>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_sample_shading**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_sample_shading**()

If `true`, enables per-sample shading which replaces MSAA by SSAA. This
provides higher quality antialiasing that works with transparent (alpha
scissor) edges. This has a very high performance cost. See also
`min_sample_shading<class_RDPipelineMultisampleState_property_min_sample_shading>`{.interpreted-text
role="ref"}. See the [per-sample shading Vulkan
documentation](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#primsrast-sampleshading)
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineMultisampleState_property_min_sample_shading}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**min_sample_shading** = `0.0`
`🔗<class_RDPipelineMultisampleState_property_min_sample_shading>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_sample_shading**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_min_sample_shading**()

The multiplier of
`sample_count<class_RDPipelineMultisampleState_property_sample_count>`{.interpreted-text
role="ref"} that determines how many samples are performed for each
fragment. Must be between `0.0` and `1.0` (inclusive). Only effective if
`enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>`{.interpreted-text
role="ref"} is `true`. If
`min_sample_shading<class_RDPipelineMultisampleState_property_min_sample_shading>`{.interpreted-text
role="ref"} is `1.0`, fragment invocation must only read from the
coverage index sample. Tile image access must not be used if
`enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>`{.interpreted-text
role="ref"} is *not* `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineMultisampleState_property_sample_count}
::: rst-class
classref-property
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **sample_count** = `0`
`🔗<class_RDPipelineMultisampleState_property_sample_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sample_count**(value:
  `TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
  role="ref"})
- `TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
  role="ref"} **get_sample_count**()

The number of MSAA samples (or SSAA samples if
`enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>`{.interpreted-text
role="ref"} is `true`) to perform. Higher values result in better
antialiasing, at the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineMultisampleState_property_sample_masks}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
**sample_masks** = `[]`
`🔗<class_RDPipelineMultisampleState_property_sample_masks>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sample_masks**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
  **get_sample_masks**()

The sample mask array. See the [sample mask Vulkan
documentation](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#fragops-samplemask)
for more details.
