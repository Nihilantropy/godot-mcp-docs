github_url
:   hide

# AudioEffectSpectrumAnalyzer {#class_AudioEffectSpectrumAnalyzer}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Audio effect that can be used for real-time audio visualizations.

::: rst-class
classref-introduction-group
:::

## Description

This audio effect does not affect sound output, but can be used for
real-time audio visualizations.

This resource configures an
`AudioEffectSpectrumAnalyzerInstance<class_AudioEffectSpectrumAnalyzerInstance>`{.interpreted-text
role="ref"}, which performs the actual analysis at runtime. An instance
can be obtained with
`AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>`{.interpreted-text
role="ref"}.

See also
`AudioStreamGenerator<class_AudioStreamGenerator>`{.interpreted-text
role="ref"} for procedurally generating sounds.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Audio Spectrum Visualizer
  Demo](https://godotengine.org/asset-library/asset/2762)

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

:::: {#enum_AudioEffectSpectrumAnalyzer_FFTSize}
::: rst-class
classref-enumeration
:::
::::

enum **FFTSize**:
`🔗<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"}

:::: {#class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_256}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest
latency, but least stable over time.

:::: {#class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_512}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency,
but less stable over time.

:::: {#class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_1024}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a
compromise between latency and stability over time.

:::: {#class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_2048}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High
latency, but stable over time.

:::: {#class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_4096}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest
latency, but most stable over time.

:::: {#class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **FFT_SIZE_MAX** = `5`

Represents the size of the
`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioEffectSpectrumAnalyzer_property_buffer_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **buffer_length** =
`2.0`
`🔗<class_AudioEffectSpectrumAnalyzer_property_buffer_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffer_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_buffer_length**()

The length of the buffer to keep (in seconds). Higher values keep data
around for longer, but require more memory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectSpectrumAnalyzer_property_fft_size}
::: rst-class
classref-property
:::
::::

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
role="ref"} **fft_size** = `2`
`🔗<class_AudioEffectSpectrumAnalyzer_property_fft_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fft_size**(value:
  `FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
  role="ref"})
- `FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`{.interpreted-text
  role="ref"} **get_fft_size**()

The size of the [Fast Fourier
transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer.
Higher values smooth out the spectrum analysis over time, but have
greater latency. The effects of this higher latency are especially
noticeable with sudden amplitude changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectSpectrumAnalyzer_property_tap_back_pos}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap_back_pos** =
`0.01`
`🔗<class_AudioEffectSpectrumAnalyzer_property_tap_back_pos>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap_back_pos**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tap_back_pos**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
