github_url
:   hide

# AudioEffectPanner {#class_AudioEffectPanner}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Adds a panner audio effect to an audio bus. Pans sound left or right.

::: rst-class
classref-introduction-group
:::

## Description

Determines how much of an audio signal is sent to the left and right
buses.

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

:::: {#class_AudioEffectPanner_property_pan}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pan** = `0.0`
`🔗<class_AudioEffectPanner_property_pan>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pan**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_pan**()

Pan position. Value can range from -1 (fully left) to 1 (fully right).
