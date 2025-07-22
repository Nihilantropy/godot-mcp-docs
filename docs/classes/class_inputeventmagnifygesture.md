github_url
:   hide

# InputEventMagnifyGesture {#class_InputEventMagnifyGesture}

**Inherits:**
`InputEventGesture<class_InputEventGesture>`{.interpreted-text
role="ref"} **\<**
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"} **\<**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a magnifying touch gesture.

::: rst-class
classref-introduction-group
:::

## Description

Stores the factor of a magnifying touch gesture. This is usually
performed when the user pinches the touch screen and used for zooming
in/out.

\*\*Note:\*\* On Android, this requires the
`ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures<class_ProjectSettings_property_input_devices/pointing/android/enable_pan_and_scale_gestures>`{.interpreted-text
role="ref"} project setting to be enabled.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`{.interpreted-text
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

:::: {#class_InputEventMagnifyGesture_property_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **factor** = `1.0`
`🔗<class_InputEventMagnifyGesture_property_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_factor**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_factor**()

The amount (or delta) of the event. This value is closer to `1.0` the
slower the gesture is performed.
