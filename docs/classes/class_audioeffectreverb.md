github_url
:   hide

# AudioEffectReverb {#class_AudioEffectReverb}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a reverberation audio effect to an Audio bus.

::: rst-class
classref-introduction-group
:::

## Description

Simulates the sound of acoustic environments such as rooms, concert
halls, caverns, or an open spaces.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#class_AudioEffectReverb_property_damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping** = `0.5`
`🔗<class_AudioEffectReverb_property_damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_damping**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_damping**()

Defines how reflective the imaginary room\'s walls are. Value can range
from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_dry}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dry** = `1.0`
`🔗<class_AudioEffectReverb_property_dry>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dry**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_dry**()

Output percent of original sound. At 0, only modified sound is
outputted. Value can range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_hipass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **hipass** = `0.0`
`🔗<class_AudioEffectReverb_property_hipass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hpf**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_hpf**()

High-pass filter passes signals with a frequency higher than a certain
cutoff frequency and attenuates signals with frequencies lower than the
cutoff frequency. Value can range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_predelay_feedback}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **predelay_feedback**
= `0.4`
`🔗<class_AudioEffectReverb_property_predelay_feedback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_predelay_feedback**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_predelay_feedback**()

Output percent of predelay. Value can range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_predelay_msec}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **predelay_msec** =
`150.0`
`🔗<class_AudioEffectReverb_property_predelay_msec>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_predelay_msec**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_predelay_msec**()

Time between the original signal and the early reflections of the reverb
signal, in milliseconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_room_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **room_size** = `0.8`
`🔗<class_AudioEffectReverb_property_room_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_room_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_room_size**()

Dimensions of simulated room. Bigger means more echoes. Value can range
from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_spread}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spread** = `1.0`
`🔗<class_AudioEffectReverb_property_spread>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spread**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_spread**()

Widens or narrows the stereo image of the reverb tail. 1 means fully
widens. Value can range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectReverb_property_wet}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **wet** = `0.5`
`🔗<class_AudioEffectReverb_property_wet>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wet**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_wet**()

Output percent of modified sound. At 0, only original sound is
outputted. Value can range from 0 to 1.
