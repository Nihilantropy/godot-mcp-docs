github_url
:   hide

# AudioEffectAmplify {#class_AudioEffectAmplify}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds an amplifying audio effect to an audio bus.

::: rst-class
classref-introduction-group
:::

## Description

Increases or decreases the volume being routed through the audio bus.

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

:::: {#class_AudioEffectAmplify_property_volume_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_db** = `0.0`
`🔗<class_AudioEffectAmplify_property_volume_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_volume_db**()

Amount of amplification in decibels. Positive values make the sound
louder, negative values make it quieter. Value can range from -80 to 24.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectAmplify_property_volume_linear}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_linear**
`🔗<class_AudioEffectAmplify_property_volume_linear>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_linear**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volume_linear**()

Amount of amplification as a linear value.

\*\*Note:\*\* This member modifies
`volume_db<class_AudioEffectAmplify_property_volume_db>`{.interpreted-text
role="ref"} for convenience. The returned value is equivalent to the
result of
`@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"} on
`volume_db<class_AudioEffectAmplify_property_volume_db>`{.interpreted-text
role="ref"}. Setting this member is equivalent to setting
`volume_db<class_AudioEffectAmplify_property_volume_db>`{.interpreted-text
role="ref"} to the result of
`@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>`{.interpreted-text
role="ref"} on a value.
