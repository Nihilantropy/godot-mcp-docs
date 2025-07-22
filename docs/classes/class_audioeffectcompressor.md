github_url
:   hide

# AudioEffectCompressor {#class_AudioEffectCompressor}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a compressor audio effect to an audio bus.

Reduces sounds that exceed a certain threshold level, smooths out the
dynamics and increases the overall volume.

::: rst-class
classref-introduction-group
:::

## Description

Dynamic range compressor reduces the level of the sound when the
amplitude goes over a certain threshold in Decibels. One of the main
uses of a compressor is to increase the dynamic range by clipping as
little as possible (when sound goes over 0dB).

Compressor has many uses in the mix:

- In the Master bus to compress the whole output (although an
  `AudioEffectHardLimiter<class_AudioEffectHardLimiter>`{.interpreted-text
  role="ref"} is probably better).
- In voice channels to ensure they sound as balanced as possible.
- Sidechained. This can reduce the sound level sidechained with another
  audio bus for threshold detection. This technique is common in video
  game mixing to the level of music and SFX while voices are being
  heard.
- Accentuates transients by using a wider attack, making effects sound
  more punchy.

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

:::: {#class_AudioEffectCompressor_property_attack_us}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **attack_us** =
`20.0`
`🔗<class_AudioEffectCompressor_property_attack_us>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attack_us**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_attack_us**()

Compressor\'s reaction time when the signal exceeds the threshold, in
microseconds. Value can range from 20 to 2000.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCompressor_property_gain}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **gain** = `0.0`
`🔗<class_AudioEffectCompressor_property_gain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gain**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_gain**()

Gain applied to the output signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCompressor_property_mix}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mix** = `1.0`
`🔗<class_AudioEffectCompressor_property_mix>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mix**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_mix**()

Balance between original signal and effect signal. Value can range from
0 (totally dry) to 1 (totally wet).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCompressor_property_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ratio** = `4.0`
`🔗<class_AudioEffectCompressor_property_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_ratio**()

Amount of compression applied to the audio once it passes the threshold
level. The higher the ratio, the more the loud parts of the audio will
be compressed. Value can range from 1 to 48.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCompressor_property_release_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **release_ms** =
`250.0`
`🔗<class_AudioEffectCompressor_property_release_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_release_ms**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_release_ms**()

Compressor\'s delay time to stop reducing the signal after the signal
level falls below the threshold, in milliseconds. Value can range from
20 to 2000.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCompressor_property_sidechain}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**sidechain** = `&""`
`🔗<class_AudioEffectCompressor_property_sidechain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sidechain**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_sidechain**()

Reduce the sound level using another audio bus for threshold detection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCompressor_property_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **threshold** = `0.0`
`🔗<class_AudioEffectCompressor_property_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_threshold**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_threshold**()

The level above which compression is applied to the audio. Value can
range from -60 to 0.
