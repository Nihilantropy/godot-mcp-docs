github_url
:   hide

# AudioEffectStereoEnhance {#class_AudioEffectStereoEnhance}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An audio effect that can be used to adjust the intensity of stereo
panning.

::: rst-class
classref-introduction-group
:::

## Description

An audio effect that can be used to adjust the intensity of stereo
panning.

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

:::: {#class_AudioEffectStereoEnhance_property_pan_pullout}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pan_pullout** =
`1.0`
`🔗<class_AudioEffectStereoEnhance_property_pan_pullout>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pan_pullout**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pan_pullout**()

Amplifies the difference between stereo channels, increasing or
decreasing existing panning. A value of 0.0 will downmix stereo to mono.
Does not affect a mono signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectStereoEnhance_property_surround}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **surround** = `0.0`
`🔗<class_AudioEffectStereoEnhance_property_surround>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_surround**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_surround**()

Widens sound stage through phase shifting in conjunction with
`time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>`{.interpreted-text
role="ref"}. Just pans sound to the left channel if
`time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>`{.interpreted-text
role="ref"} is 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectStereoEnhance_property_time_pullout_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **time_pullout_ms** =
`0.0`
`🔗<class_AudioEffectStereoEnhance_property_time_pullout_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_time_pullout**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_time_pullout**()

Widens sound stage through phase shifting in conjunction with
`surround<class_AudioEffectStereoEnhance_property_surround>`{.interpreted-text
role="ref"}. Just delays the right channel if
`surround<class_AudioEffectStereoEnhance_property_surround>`{.interpreted-text
role="ref"} is 0.
