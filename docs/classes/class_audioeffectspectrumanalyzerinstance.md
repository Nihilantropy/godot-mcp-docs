github_url
:   hide

# AudioEffectSpectrumAnalyzerInstance {#class_AudioEffectSpectrumAnalyzerInstance}

**Inherits:**
`AudioEffectInstance<class_AudioEffectInstance>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Queryable instance of an
`AudioEffectSpectrumAnalyzer<class_AudioEffectSpectrumAnalyzer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

The runtime part of an
`AudioEffectSpectrumAnalyzer<class_AudioEffectSpectrumAnalyzer>`{.interpreted-text
role="ref"}, which can be used to query the magnitude of a frequency
range on its host bus.

An instance of this class can be obtained with
`AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Audio Spectrum Visualizer
  Demo](https://godotengine.org/asset-library/asset/2762)

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

## Enumerations

:::: {#enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode}
::: rst-class
classref-enumeration
:::
::::

enum **MagnitudeMode**:
`🔗<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>`{.interpreted-text
role="ref"}

:::: {#class_AudioEffectSpectrumAnalyzerInstance_constant_MAGNITUDE_AVERAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>`{.interpreted-text
role="ref"} **MAGNITUDE_AVERAGE** = `0`

Use the average value across the frequency range as magnitude.

:::: {#class_AudioEffectSpectrumAnalyzerInstance_constant_MAGNITUDE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>`{.interpreted-text
role="ref"} **MAGNITUDE_MAX** = `1`

Use the maximum value of the frequency range as magnitude.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_magnitude_for_frequency_range**(from_hz:
`float<class_float>`{.interpreted-text role="ref"}, to_hz:
`float<class_float>`{.interpreted-text role="ref"}, mode:
`MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>`{.interpreted-text
role="ref"} = 1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range>`{.interpreted-text
role="ref"}

Returns the magnitude of the frequencies from `from_hz` to `to_hz` in
linear energy as a Vector2. The `x` component of the return value
represents the left stereo channel, and `y` represents the right
channel.

`mode` determines how the frequency range will be processed.
