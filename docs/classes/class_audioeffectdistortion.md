github_url
:   hide

# AudioEffectDistortion {#class_AudioEffectDistortion}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a distortion audio effect to an Audio bus.

Modifies the sound to make it distorted.

::: rst-class
classref-introduction-group
:::

## Description

Different types are available: clip, tan, lo-fi (bit crushing),
overdrive, or waveshape.

By distorting the waveform the frequency content changes, which will
often make the sound \"crunchy\" or \"abrasive\". For games, it can
simulate sound coming from some saturated device or speaker very
efficiently.

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

:::: {#enum_AudioEffectDistortion_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**: `🔗<enum_AudioEffectDistortion_Mode>`{.interpreted-text
role="ref"}

:::: {#class_AudioEffectDistortion_constant_MODE_CLIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
**MODE_CLIP** = `0`

Digital distortion effect which cuts off peaks at the top and bottom of
the waveform.

:::: {#class_AudioEffectDistortion_constant_MODE_ATAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
**MODE_ATAN** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_AudioEffectDistortion_constant_MODE_LOFI}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
**MODE_LOFI** = `2`

Low-resolution digital distortion effect (bit depth reduction). You can
use it to emulate the sound of early digital audio devices.

:::: {#class_AudioEffectDistortion_constant_MODE_OVERDRIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
**MODE_OVERDRIVE** = `3`

Emulates the warm distortion produced by a field effect transistor,
which is commonly used in solid-state musical instrument amplifiers. The
`drive<class_AudioEffectDistortion_property_drive>`{.interpreted-text
role="ref"} property has no effect in this mode.

:::: {#class_AudioEffectDistortion_constant_MODE_WAVESHAPE}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
**MODE_WAVESHAPE** = `4`

Waveshaper distortions are used mainly by electronic musicians to
achieve an extra-abrasive sound.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioEffectDistortion_property_drive}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **drive** = `0.0`
`🔗<class_AudioEffectDistortion_property_drive>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drive**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_drive**()

Distortion power. Value can range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDistortion_property_keep_hf_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **keep_hf_hz** =
`16000.0`
`🔗<class_AudioEffectDistortion_property_keep_hf_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_hf_hz**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_keep_hf_hz**()

High-pass filter, in Hz. Frequencies higher than this value will not be
affected by the distortion. Value can range from 1 to 20000.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDistortion_property_mode}
::: rst-class
classref-property
:::
::::

`Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
**mode** = `0`
`🔗<class_AudioEffectDistortion_property_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode**(value:
  `Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"})
- `Mode<enum_AudioEffectDistortion_Mode>`{.interpreted-text role="ref"}
  **get_mode**()

Distortion type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDistortion_property_post_gain}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **post_gain** = `0.0`
`🔗<class_AudioEffectDistortion_property_post_gain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_post_gain**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_post_gain**()

Increases or decreases the volume after the effect, in decibels. Value
can range from -80 to 24.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDistortion_property_pre_gain}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pre_gain** = `0.0`
`🔗<class_AudioEffectDistortion_property_pre_gain>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pre_gain**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_pre_gain**()

Increases or decreases the volume before the effect, in decibels. Value
can range from -60 to 60.
