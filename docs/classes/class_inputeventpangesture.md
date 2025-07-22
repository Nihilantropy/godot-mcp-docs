github_url
:   hide

# InputEventPanGesture {#class_InputEventPanGesture}

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

Represents a panning touch gesture.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about pan gestures. A pan gesture is performed when
the user swipes the touch screen with two fingers. It\'s typically used
for panning/scrolling.

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

:::: {#class_InputEventPanGesture_property_delta}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **delta** =
`Vector2(0, 0)`
`🔗<class_InputEventPanGesture_property_delta>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_delta**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_delta**()

Panning amount since last pan event.
