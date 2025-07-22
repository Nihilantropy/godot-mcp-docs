github_url
:   hide

# OpenXRDpadBindingModifier {#class_OpenXRDpadBindingModifier}

**Inherits:**
`OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>`{.interpreted-text
role="ref"} **\<**
`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

The DPad binding modifier converts an axis input to a dpad output.

::: rst-class
classref-introduction-group
:::

## Description

The DPad binding modifier converts an axis input to a dpad output,
emulating a DPad. New input paths for each dpad direction will be added
to the interaction profile. When bound to actions the DPad emulation
will be activated. You should **not** combine dpad inputs with normal
inputs in the same action set for the same control, this will result in
an error being returned when suggested bindings are submitted to OpenXR.

See
[XR_EXT_dpad_binding](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding)
for in-depth details.

\*\*Note:\*\* If the DPad binding modifier extension is enabled, all
dpad binding paths will be available in the action map. Adding the
modifier to an interaction profile allows you to further customize the
behavior.

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

:::: {#class_OpenXRDpadBindingModifier_property_action_set}
::: rst-class
classref-property
:::
::::

`OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text role="ref"}
**action_set**
`🔗<class_OpenXRDpadBindingModifier_property_action_set>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action_set**(value:
  `OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text
  role="ref"})
- `OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text role="ref"}
  **get_action_set**()

Action set for which this dpad binding modifier is active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRDpadBindingModifier_property_center_region}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **center_region** =
`0.1`
`🔗<class_OpenXRDpadBindingModifier_property_center_region>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_region**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_center_region**()

Center region in which our center position of our dpad return `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRDpadBindingModifier_property_input_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **input_path** =
`""`
`🔗<class_OpenXRDpadBindingModifier_property_input_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_input_path**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_input_path**()

Input path for this dpad binding modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRDpadBindingModifier_property_is_sticky}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_sticky** = `false`
`🔗<class_OpenXRDpadBindingModifier_property_is_sticky>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_is_sticky**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_is_sticky**()

If `false`, when the joystick enters a new dpad zone this becomes
`true`.

If `true`, when the joystick remains in active dpad zone, this remains
`true` even if we overlap with another zone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRDpadBindingModifier_property_off_haptic}
::: rst-class
classref-property
:::
::::

`OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text role="ref"}
**off_haptic**
`🔗<class_OpenXRDpadBindingModifier_property_off_haptic>`{.interpreted-text
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

:::: {#class_OpenXRDpadBindingModifier_property_on_haptic}
::: rst-class
classref-property
:::
::::

`OpenXRHapticBase<class_OpenXRHapticBase>`{.interpreted-text role="ref"}
**on_haptic**
`🔗<class_OpenXRDpadBindingModifier_property_on_haptic>`{.interpreted-text
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

:::: {#class_OpenXRDpadBindingModifier_property_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **threshold** = `0.6`
`🔗<class_OpenXRDpadBindingModifier_property_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_threshold**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_threshold**()

When our input value is equal or larger than this value, our dpad in
that direction becomes `true`. It stays `true` until it falls under the
`threshold_released<class_OpenXRDpadBindingModifier_property_threshold_released>`{.interpreted-text
role="ref"} value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRDpadBindingModifier_property_threshold_released}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**threshold_released** = `0.4`
`🔗<class_OpenXRDpadBindingModifier_property_threshold_released>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_threshold_released**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_threshold_released**()

When our input value falls below this, our output becomes `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRDpadBindingModifier_property_wedge_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **wedge_angle** =
`1.5707964`
`🔗<class_OpenXRDpadBindingModifier_property_wedge_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wedge_angle**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_wedge_angle**()

The angle of each wedge that identifies the 4 directions of the emulated
dpad.
