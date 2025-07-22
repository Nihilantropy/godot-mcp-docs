github_url
:   hide

# AudioEffectDelay {#class_AudioEffectDelay}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a delay audio effect to an audio bus. Plays input signal back after
a period of time.

Two tap delay and feedback options.

::: rst-class
classref-introduction-group
:::

## Description

Plays input signal back after a period of time. The delayed signal may
be played back multiple times to create the sound of a repeating,
decaying echo. Delay effects range from a subtle echo effect to a
pronounced blending of previous sounds with new sounds.

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

:::: {#class_AudioEffectDelay_property_dry}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dry** = `1.0`
`🔗<class_AudioEffectDelay_property_dry>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dry**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_dry**()

Output percent of original sound. At 0, only delayed sounds are output.
Value can range from 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_feedback_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **feedback_active** =
`false`
`🔗<class_AudioEffectDelay_property_feedback_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_feedback_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_feedback_active**()

If `true`, feedback is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_feedback_delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **feedback_delay_ms**
= `340.0`
`🔗<class_AudioEffectDelay_property_feedback_delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_feedback_delay_ms**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_feedback_delay_ms**()

Feedback delay time in milliseconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_feedback_level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **feedback_level_db**
= `-6.0`
`🔗<class_AudioEffectDelay_property_feedback_level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_feedback_level_db**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_feedback_level_db**()

Sound level for feedback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_feedback_lowpass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **feedback_lowpass**
= `16000.0`
`🔗<class_AudioEffectDelay_property_feedback_lowpass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_feedback_lowpass**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_feedback_lowpass**()

Low-pass filter for feedback, in Hz. Frequencies below this value are
filtered out of the source signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap1_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tap1_active** =
`true`
`🔗<class_AudioEffectDelay_property_tap1_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap1_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_tap1_active**()

If `true`, the first tap will be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap1_delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap1_delay_ms** =
`250.0`
`🔗<class_AudioEffectDelay_property_tap1_delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap1_delay_ms**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tap1_delay_ms**()

First tap delay time in milliseconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap1_level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap1_level_db** =
`-6.0`
`🔗<class_AudioEffectDelay_property_tap1_level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap1_level_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tap1_level_db**()

Sound level for the first tap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap1_pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap1_pan** = `0.2`
`🔗<class_AudioEffectDelay_property_tap1_pan>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap1_pan**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_tap1_pan**()

Pan position for the first tap. Value can range from -1 (fully left) to
1 (fully right).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap2_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tap2_active** =
`true`
`🔗<class_AudioEffectDelay_property_tap2_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap2_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_tap2_active**()

If `true`, the second tap will be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap2_delay_ms}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap2_delay_ms** =
`500.0`
`🔗<class_AudioEffectDelay_property_tap2_delay_ms>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap2_delay_ms**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tap2_delay_ms**()

Second tap delay time in milliseconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap2_level_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap2_level_db** =
`-12.0`
`🔗<class_AudioEffectDelay_property_tap2_level_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap2_level_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_tap2_level_db**()

Sound level for the second tap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectDelay_property_tap2_pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tap2_pan** = `-0.4`
`🔗<class_AudioEffectDelay_property_tap2_pan>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tap2_pan**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_tap2_pan**()

Pan position for the second tap. Value can range from -1 (fully left) to
1 (fully right).
