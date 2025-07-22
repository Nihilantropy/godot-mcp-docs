github_url
:   hide

# InputEventGesture {#class_InputEventGesture}

**Inherits:**
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"} **\<**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`InputEventMagnifyGesture<class_InputEventMagnifyGesture>`{.interpreted-text
role="ref"},
`InputEventPanGesture<class_InputEventPanGesture>`{.interpreted-text
role="ref"}

Abstract base class for touch gestures.

::: rst-class
classref-introduction-group
:::

## Description

InputEventGestures are sent when a user performs a supported gesture on
a touch screen. Gestures can\'t be emulated using mouse, because they
typically require multi-touch.

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

:::: {#class_InputEventGesture_property_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **position** =
`Vector2(0, 0)`
`🔗<class_InputEventGesture_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position**()

The local gesture position relative to the
`Viewport<class_Viewport>`{.interpreted-text role="ref"}. If used in
`Control._gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}, the position is relative to the current
`Control<class_Control>`{.interpreted-text role="ref"} that received
this gesture.
