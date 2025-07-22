github_url
:   hide

# AudioEffectEQ {#class_AudioEffectEQ}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioEffectEQ10<class_AudioEffectEQ10>`{.interpreted-text role="ref"},
`AudioEffectEQ21<class_AudioEffectEQ21>`{.interpreted-text role="ref"},
`AudioEffectEQ6<class_AudioEffectEQ6>`{.interpreted-text role="ref"}

Base class for audio equalizers. Gives you control over frequencies.

Use it to create a custom equalizer if
`AudioEffectEQ6<class_AudioEffectEQ6>`{.interpreted-text role="ref"},
`AudioEffectEQ10<class_AudioEffectEQ10>`{.interpreted-text role="ref"}
or `AudioEffectEQ21<class_AudioEffectEQ21>`{.interpreted-text
role="ref"} don\'t fit your needs.

::: rst-class
classref-introduction-group
:::

## Description

AudioEffectEQ gives you control over frequencies. Use it to compensate
for existing deficiencies in audio. AudioEffectEQs are useful on the
Master bus to completely master a mix and give it more character. They
are also useful when a game is run on a mobile device, to adjust the mix
to that kind of speakers (it can be added but disabled when headphones
are plugged).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioEffectEQ_method_get_band_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_band_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectEQ_method_get_band_count>`{.interpreted-text
role="ref"}

Returns the number of bands of the equalizer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectEQ_method_get_band_gain_db}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_band_gain_db**(band_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectEQ_method_get_band_gain_db>`{.interpreted-text
role="ref"}

Returns the band\'s gain at the specified index, in dB.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectEQ_method_set_band_gain_db}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_band_gain_db**(band_idx: `int<class_int>`{.interpreted-text
role="ref"}, volume_db: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectEQ_method_set_band_gain_db>`{.interpreted-text
role="ref"}

Sets band\'s gain at the specified index, in dB.
