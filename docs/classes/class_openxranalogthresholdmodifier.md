github_url
:   hide

# OpenXRAnalogThresholdModifier {#class_OpenXRAnalogThresholdModifier}

**Inherits:**
`OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>`{.interpreted-text
role="ref"} **\<**
`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

The analog threshold binding modifier can modify a float input to a
boolean input with specified thresholds.

::: rst-class
classref-introduction-group
:::

## Description

The analog threshold binding modifier can modify a float input to a
boolean input with specified thresholds.

See
[XR_VALVE_analog_threshold](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VALVE_analog_threshold)
for in-depth details.

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

:::: {#class_OpenXRAnalogThresholdModifier_property_off_haptic}
::: rst-class
classref-property
:::
::::

`OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text role="ref"}
**off_haptic**
`🔗<class_OpenXRAnalogThresholdModifier_property_off_haptic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_off_haptic**(value:
  `OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text
  role="ref"})
- `OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text
  role="ref"} **get_off_haptic**()

Haptic pulse to emit when the user releases the input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAnalogThresholdModifier_property_off_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **off_threshold** =
`0.4`
`🔗<class_OpenXRAnalogThresholdModifier_property_off_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_off_threshold**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_off_threshold**()

When our input value falls below this, our output becomes `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAnalogThresholdModifier_property_on_haptic}
::: rst-class
classref-property
:::
::::

`OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text role="ref"}
**on_haptic**
`🔗<class_OpenXRAnalogThresholdModifier_property_on_haptic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_on_haptic**(value:
  `OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text
  role="ref"})
- `OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text
  role="ref"} **get_on_haptic**()

Haptic pulse to emit when the user presses the input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAnalogThresholdModifier_property_on_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **on_threshold** =
`0.6`
`🔗<class_OpenXRAnalogThresholdModifier_property_on_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_on_threshold**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_on_threshold**()

When our input value is equal or larger than this value, our output
becomes `true`. It stays `true` until it falls under the
`off_threshold<class_OpenXRAnalogThresholdModifier_property_off_threshold>`{.interpreted-text
role="ref"} value.
