github_url
:   hide

# AudioEffectPitchShift {#class_AudioEffectPitchShift}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a pitch-shifting audio effect to an audio bus.

Raises or lowers the pitch of original sound.

::: rst-class
classref-introduction-group
:::

## Description

Allows modulation of pitch independently of tempo. All frequencies can
be increased/decreased with minimal effect on transients.

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

:::: {#enum_AudioEffectPitchShift_FFTSize}
::: rst-class
classref-enumeration
:::
::::

enum **FFTSize**:
`🔗<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text role="ref"}

:::: {#class_AudioEffectPitchShift_constant_FFT_SIZE_256}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest
latency, but least stable over time.

:::: {#class_AudioEffectPitchShift_constant_FFT_SIZE_512}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency,
but less stable over time.

:::: {#class_AudioEffectPitchShift_constant_FFT_SIZE_1024}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a
compromise between latency and stability over time.

:::: {#class_AudioEffectPitchShift_constant_FFT_SIZE_2048}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High
latency, but stable over time.

:::: {#class_AudioEffectPitchShift_constant_FFT_SIZE_4096}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest
latency, but most stable over time.

:::: {#class_AudioEffectPitchShift_constant_FFT_SIZE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_MAX** = `5`

Represents the size of the
`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioEffectPitchShift_property_fft_size}
::: rst-class
classref-property
:::
::::

`FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
role="ref"} **fft_size** = `3`
`🔗<class_AudioEffectPitchShift_property_fft_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fft_size**(value:
  `FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
  role="ref"})
- `FFTSize<enum_AudioEffectPitchShift_FFTSize>`{.interpreted-text
  role="ref"} **get_fft_size**()

The size of the [Fast Fourier
transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer.
Higher values smooth out the effect over time, but have greater latency.
The effects of this higher latency are especially noticeable on sounds
that have sudden amplitude changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectPitchShift_property_oversampling}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **oversampling** = `4`
`🔗<class_AudioEffectPitchShift_property_oversampling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_oversampling**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_oversampling**()

The oversampling factor to use. Higher values result in better quality,
but are more demanding on the CPU and may cause audio cracking if the
CPU can\'t keep up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectPitchShift_property_pitch_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pitch_scale** =
`1.0`
`🔗<class_AudioEffectPitchShift_property_pitch_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pitch_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pitch_scale**()

The pitch scale to use. `1.0` is the default pitch and plays sounds
unaffected.
`pitch_scale<class_AudioEffectPitchShift_property_pitch_scale>`{.interpreted-text
role="ref"} can range from `0.0` (infinitely low pitch, inaudible) to
`16` (16 times higher than the initial pitch).
