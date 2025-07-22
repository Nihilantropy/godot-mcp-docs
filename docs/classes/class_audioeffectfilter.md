github_url
:   hide

# AudioEffectFilter {#class_AudioEffectFilter}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioEffectBandLimitFilter<class_AudioEffectBandLimitFilter>`{.interpreted-text
role="ref"},
`AudioEffectBandPassFilter<class_AudioEffectBandPassFilter>`{.interpreted-text
role="ref"},
`AudioEffectHighPassFilter<class_AudioEffectHighPassFilter>`{.interpreted-text
role="ref"},
`AudioEffectHighShelfFilter<class_AudioEffectHighShelfFilter>`{.interpreted-text
role="ref"},
`AudioEffectLowPassFilter<class_AudioEffectLowPassFilter>`{.interpreted-text
role="ref"},
`AudioEffectLowShelfFilter<class_AudioEffectLowShelfFilter>`{.interpreted-text
role="ref"},
`AudioEffectNotchFilter<class_AudioEffectNotchFilter>`{.interpreted-text
role="ref"}

Adds a filter to the audio bus.

::: rst-class
classref-introduction-group
:::

## Description

Allows frequencies other than the
`cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`{.interpreted-text
role="ref"} to pass.

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

## Enumerations

:::: {#enum_AudioEffectFilter_FilterDB}
::: rst-class
classref-enumeration
:::
::::

enum **FilterDB**:
`🔗<enum_AudioEffectFilter_FilterDB>`{.interpreted-text role="ref"}

:::: {#class_AudioEffectFilter_constant_FILTER_6DB}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
role="ref"} **FILTER_6DB** = `0`

Cutting off at 6dB per octave.

:::: {#class_AudioEffectFilter_constant_FILTER_12DB}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
role="ref"} **FILTER_12DB** = `1`

Cutting off at 12dB per octave.

:::: {#class_AudioEffectFilter_constant_FILTER_18DB}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
role="ref"} **FILTER_18DB** = `2`

Cutting off at 18dB per octave.

:::: {#class_AudioEffectFilter_constant_FILTER_24DB}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
role="ref"} **FILTER_24DB** = `3`

Cutting off at 24dB per octave.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioEffectFilter_property_cutoff_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cutoff_hz** =
`2000.0`
`🔗<class_AudioEffectFilter_property_cutoff_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cutoff**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_cutoff**()

Threshold frequency for the filter, in Hz.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectFilter_property_db}
::: rst-class
classref-property
:::
::::

`FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
role="ref"} **db** = `0`
`🔗<class_AudioEffectFilter_property_db>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_db**(value:
  `FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
  role="ref"})
- `FilterDB<enum_AudioEffectFilter_FilterDB>`{.interpreted-text
  role="ref"} **get_db**()

Steepness of the cutoff curve in dB per octave, also known as the order
of the filter. Higher orders have a more aggressive cutoff.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectFilter_property_gain}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **gain** = `1.0`
`🔗<class_AudioEffectFilter_property_gain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gain**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_gain**()

Gain amount of the frequencies after the filter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectFilter_property_resonance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **resonance** = `0.5`
`🔗<class_AudioEffectFilter_property_resonance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_resonance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_resonance**()

Amount of boost in the frequency range near the cutoff frequency.
