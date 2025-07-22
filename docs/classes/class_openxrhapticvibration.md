github_url
:   hide

# OpenXRHapticVibration {#class_OpenXRHapticVibration}

**Inherits:**
`OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Vibration haptic feedback.

::: rst-class
classref-introduction-group
:::

## Description

This haptic feedback resource makes it possible to define a vibration
based haptic feedback pulse that can be triggered through actions in the
OpenXR action map.

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

:::: {#class_OpenXRHapticVibration_property_amplitude}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **amplitude** = `1.0`
`🔗<class_OpenXRHapticVibration_property_amplitude>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_amplitude**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_amplitude**()

The amplitude of the pulse between `0.0` and `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRHapticVibration_property_duration}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **duration** = `-1`
`🔗<class_OpenXRHapticVibration_property_duration>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_duration**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_duration**()

The duration of the pulse in nanoseconds. Use `-1` for a minimum
duration pulse for the current XR runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRHapticVibration_property_frequency}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **frequency** = `0.0`
`🔗<class_OpenXRHapticVibration_property_frequency>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frequency**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_frequency**()

The frequency of the pulse in Hz. `0.0` will let the XR runtime chose an
optimal frequency for the device used.
