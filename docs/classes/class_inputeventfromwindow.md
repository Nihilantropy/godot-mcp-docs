github_url
:   hide

# InputEventFromWindow {#class_InputEventFromWindow}

**Inherits:** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`InputEventScreenDrag<class_InputEventScreenDrag>`{.interpreted-text
role="ref"},
`InputEventScreenTouch<class_InputEventScreenTouch>`{.interpreted-text
role="ref"},
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"}

Abstract base class for `Viewport<class_Viewport>`{.interpreted-text
role="ref"}-based input events.

::: rst-class
classref-introduction-group
:::

## Description

InputEventFromWindow represents events specifically received by windows.
This includes mouse events, keyboard events in focused windows or touch
screen actions.

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

:::: {#class_InputEventFromWindow_property_window_id}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **window_id** = `0`
`🔗<class_InputEventFromWindow_property_window_id>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_window_id**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_window_id**()

The ID of a `Window<class_Window>`{.interpreted-text role="ref"} that
received this event.
