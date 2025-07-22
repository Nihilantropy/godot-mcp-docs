github_url
:   hide

# AudioEffectPhaser {#class_AudioEffectPhaser}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a phaser audio effect to an audio bus.

Combines the original signal with a copy that is slightly out of phase
with the original.

::: rst-class
classref-introduction-group
:::

## Description

Combines phase-shifted signals with the original signal. The movement of
the phase-shifted signals is controlled using a low-frequency
oscillator.

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

:::: {#class_AudioEffectPhaser_property_depth}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth** = `1.0`
`🔗<class_AudioEffectPhaser_property_depth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_depth**()

Determines how high the filter frequencies sweep. Low value will
primarily affect bass frequencies. High value can sweep high into the
treble. Value can range from `0.1` to `4.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectPhaser_property_feedback}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **feedback** = `0.7`
`🔗<class_AudioEffectPhaser_property_feedback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_feedback**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_feedback**()

Output percent of modified sound. Value can range from 0.1 to 0.9.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectPhaser_property_range_max_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **range_max_hz** =
`1600.0`
`🔗<class_AudioEffectPhaser_property_range_max_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_range_max_hz**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_range_max_hz**()

Determines the maximum frequency affected by the LFO modulations, in Hz.
Value can range from 10 to 10000.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectPhaser_property_range_min_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **range_min_hz** =
`440.0`
`🔗<class_AudioEffectPhaser_property_range_min_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_range_min_hz**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_range_min_hz**()

Determines the minimum frequency affected by the LFO modulations, in Hz.
Value can range from 10 to 10000.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectPhaser_property_rate_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rate_hz** = `0.5`
`🔗<class_AudioEffectPhaser_property_rate_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rate_hz**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_rate_hz**()

Adjusts the rate in Hz at which the effect sweeps up and down across the
frequency range.
