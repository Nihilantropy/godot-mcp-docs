github_url
:   hide

# AudioEffectChorus {#class_AudioEffectChorus}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a chorus audio effect.

::: rst-class
classref-introduction-group
:::

## Description

Adds a chorus audio effect. The effect applies a filter with voices to
duplicate the audio source and manipulate it through the filter.

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

## Property Descriptions

:::: {#class_AudioEffectChorus_property_dry}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dry** = `1.0`
`🔗<class_AudioEffectChorus_property_dry>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dry**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_dry**()

The effect\'s raw signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/1/cutoff_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/1/cutoff_hz**
= `8000.0`
`🔗<class_AudioEffectChorus_property_voice/1/cutoff_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, cutoff_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s cutoff frequency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/1/delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/1/delay_ms**
= `15.0`
`🔗<class_AudioEffectChorus_property_voice/1/delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, delay_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s signal delay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/1/depth_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/1/depth_ms**
= `2.0`
`🔗<class_AudioEffectChorus_property_voice/1/depth_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, depth_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice filter\'s depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/1/level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/1/level_db**
= `0.0`
`🔗<class_AudioEffectChorus_property_voice/1/level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, level_db: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s volume.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/1/pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/1/pan** =
`-0.5`
`🔗<class_AudioEffectChorus_property_voice/1/pan>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, pan: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s pan level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/1/rate_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/1/rate_hz** =
`0.8`
`🔗<class_AudioEffectChorus_property_voice/1/rate_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, rate_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s filter rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/2/cutoff_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/2/cutoff_hz**
= `8000.0`
`🔗<class_AudioEffectChorus_property_voice/2/cutoff_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, cutoff_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s cutoff frequency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/2/delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/2/delay_ms**
= `20.0`
`🔗<class_AudioEffectChorus_property_voice/2/delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, delay_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s signal delay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/2/depth_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/2/depth_ms**
= `3.0`
`🔗<class_AudioEffectChorus_property_voice/2/depth_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, depth_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice filter\'s depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/2/level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/2/level_db**
= `0.0`
`🔗<class_AudioEffectChorus_property_voice/2/level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, level_db: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s volume.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/2/pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/2/pan** =
`0.5`
`🔗<class_AudioEffectChorus_property_voice/2/pan>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, pan: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s pan level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/2/rate_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/2/rate_hz** =
`1.2`
`🔗<class_AudioEffectChorus_property_voice/2/rate_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, rate_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s filter rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/3/cutoff_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/3/cutoff_hz**
`🔗<class_AudioEffectChorus_property_voice/3/cutoff_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, cutoff_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s cutoff frequency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/3/delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/3/delay_ms**
`🔗<class_AudioEffectChorus_property_voice/3/delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, delay_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s signal delay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/3/depth_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/3/depth_ms**
`🔗<class_AudioEffectChorus_property_voice/3/depth_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, depth_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice filter\'s depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/3/level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/3/level_db**
`🔗<class_AudioEffectChorus_property_voice/3/level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, level_db: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s volume.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/3/pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/3/pan**
`🔗<class_AudioEffectChorus_property_voice/3/pan>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, pan: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s pan level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/3/rate_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/3/rate_hz**
`🔗<class_AudioEffectChorus_property_voice/3/rate_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, rate_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s filter rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/4/cutoff_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/4/cutoff_hz**
`🔗<class_AudioEffectChorus_property_voice/4/cutoff_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, cutoff_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s cutoff frequency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/4/delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/4/delay_ms**
`🔗<class_AudioEffectChorus_property_voice/4/delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, delay_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s signal delay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/4/depth_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/4/depth_ms**
`🔗<class_AudioEffectChorus_property_voice/4/depth_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, depth_ms: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice filter\'s depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/4/level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/4/level_db**
`🔗<class_AudioEffectChorus_property_voice/4/level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, level_db: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s volume.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/4/pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/4/pan**
`🔗<class_AudioEffectChorus_property_voice/4/pan>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, pan: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s pan level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice/4/rate_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **voice/4/rate_hz**
`🔗<class_AudioEffectChorus_property_voice/4/rate_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"}, rate_hz: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The voice\'s filter rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_voice_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **voice_count** = `2`
`🔗<class_AudioEffectChorus_property_voice_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_voice_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_voice_count**()

The number of voices in the effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_property_wet}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **wet** = `0.5`
`🔗<class_AudioEffectChorus_property_wet>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wet**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_wet**()

The effect\'s processed signal.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioEffectChorus_method_get_voice_cutoff_hz}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectChorus_method_get_voice_cutoff_hz>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_get_voice_delay_ms}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectChorus_method_get_voice_delay_ms>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_get_voice_depth_ms}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectChorus_method_get_voice_depth_ms>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_get_voice_level_db}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectChorus_method_get_voice_level_db>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_get_voice_pan}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectChorus_method_get_voice_pan>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_get_voice_rate_hz}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectChorus_method_get_voice_rate_hz>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_set_voice_cutoff_hz}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_voice_cutoff_hz**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"}, cutoff_hz: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectChorus_method_set_voice_cutoff_hz>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_set_voice_delay_ms}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_voice_delay_ms**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"}, delay_ms: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectChorus_method_set_voice_delay_ms>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_set_voice_depth_ms}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_voice_depth_ms**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"}, depth_ms: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectChorus_method_set_voice_depth_ms>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_set_voice_level_db}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_voice_level_db**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"}, level_db: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectChorus_method_set_voice_level_db>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_set_voice_pan}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_voice_pan**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"}, pan: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AudioEffectChorus_method_set_voice_pan>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectChorus_method_set_voice_rate_hz}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_voice_rate_hz**(voice_idx: `int<class_int>`{.interpreted-text
role="ref"}, rate_hz: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectChorus_method_set_voice_rate_hz>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
