github_url
:   hide

# InputEventMouse {#class_InputEventMouse}

**Inherits:**
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"} **\<**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"},
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"}

Base input event type for mouse events.

::: rst-class
classref-introduction-group
:::

## Description

Stores general information about mouse events.

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

:::: {#class_InputEventMouse_property_button_mask}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"}\] **button_mask** = `0`
`🔗<class_InputEventMouse_property_button_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_button_mask**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
  role="ref"}\] **get_button_mask**()

The mouse button mask identifier, one of or a bitwise combination of the
`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} button masks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouse_property_global_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**global_position** = `Vector2(0, 0)`
`🔗<class_InputEventMouse_property_global_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_position**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_global_position**()

When received in
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} or
`Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}, returns the mouse\'s position in the root
`Viewport<class_Viewport>`{.interpreted-text role="ref"} using the
coordinate system of the root
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

When received in
`Control._gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}, returns the mouse\'s position in the
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"} that the
`Control<class_Control>`{.interpreted-text role="ref"} is in using the
coordinate system of the
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouse_property_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **position** =
`Vector2(0, 0)`
`🔗<class_InputEventMouse_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position**()

When received in
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} or
`Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}, returns the mouse\'s position in the
`Viewport<class_Viewport>`{.interpreted-text role="ref"} this
`Node<class_Node>`{.interpreted-text role="ref"} is in using the
coordinate system of this `Viewport<class_Viewport>`{.interpreted-text
role="ref"}.

When received in
`Control._gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}, returns the mouse\'s position in the
`Control<class_Control>`{.interpreted-text role="ref"} using the local
coordinate system of the `Control<class_Control>`{.interpreted-text
role="ref"}.
