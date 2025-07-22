github_url
:   hide

# AudioEffectLimiter {#class_AudioEffectLimiter}

**Deprecated:** Use
`AudioEffectHardLimiter<class_AudioEffectHardLimiter>`{.interpreted-text
role="ref"} instead.

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a soft-clip limiter audio effect to an Audio bus.

::: rst-class
classref-introduction-group
:::

## Description

A limiter is similar to a compressor, but it\'s less flexible and
designed to disallow sound going over a given dB threshold. Adding one
in the Master bus is always recommended to reduce the effects of
clipping.

Soft clipping starts to reduce the peaks a little below the threshold
level and progressively increases its effect as the input level
increases such that the threshold is never exceeded.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
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

## Property Descriptions

:::: {#class_AudioEffectLimiter_property_ceiling_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ceiling_db** =
`-0.1`
`🔗<class_AudioEffectLimiter_property_ceiling_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ceiling_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ceiling_db**()

The waveform\'s maximum allowed value, in decibels. Value can range from
-20 to -0.1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectLimiter_property_soft_clip_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **soft_clip_db** =
`2.0`
`🔗<class_AudioEffectLimiter_property_soft_clip_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_soft_clip_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_soft_clip_db**()

Applies a gain to the limited waves, in decibels. Value can range from 0
to 6.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectLimiter_property_soft_clip_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **soft_clip_ratio** =
`10.0`
`🔗<class_AudioEffectLimiter_property_soft_clip_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_soft_clip_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_soft_clip_ratio**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectLimiter_property_threshold_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **threshold_db** =
`0.0`
`🔗<class_AudioEffectLimiter_property_threshold_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_threshold_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_threshold_db**()

Threshold from which the limiter begins to be active, in decibels. Value
can range from -30 to 0.
