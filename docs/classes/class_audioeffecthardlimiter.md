github_url
:   hide

# AudioEffectHardLimiter {#class_AudioEffectHardLimiter}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a hard limiter audio effect to an Audio bus.

::: rst-class
classref-introduction-group
:::

## Description

A limiter is an effect designed to disallow sound from going over a
given dB threshold. Hard limiters predict volume peaks, and will
smoothly apply gain reduction when a peak crosses the ceiling threshold
to prevent clipping and distortion. It preserves the waveform and
prevents it from crossing the ceiling threshold. Adding one in the
Master bus is recommended as a safety measure to prevent sudden volume
peaks from occurring, and to prevent distortion caused by clipping.

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

:::: {#class_AudioEffectHardLimiter_property_ceiling_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ceiling_db** =
`-0.3`
`🔗<class_AudioEffectHardLimiter_property_ceiling_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ceiling_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ceiling_db**()

The waveform\'s maximum allowed value, in decibels. This value can range
from `-24.0` to `0.0`.

The default value of `-0.3` prevents potential inter-sample peaks (ISP)
from crossing over 0 dB, which can cause slight distortion on some older
hardware.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectHardLimiter_property_pre_gain_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pre_gain_db** =
`0.0`
`🔗<class_AudioEffectHardLimiter_property_pre_gain_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pre_gain_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pre_gain_db**()

Gain to apply before limiting, in decibels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectHardLimiter_property_release}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **release** = `0.1`
`🔗<class_AudioEffectHardLimiter_property_release>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_release**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_release**()

Time it takes in seconds for the gain reduction to fully release.
