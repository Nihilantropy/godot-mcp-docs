github_url
:   hide

::: {.meta keywords="click, press"}
:::

# InputEventMouseButton {#class_InputEventMouseButton}

**Inherits:** `InputEventMouse<class_InputEventMouse>`{.interpreted-text
role="ref"} **\<**
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"} **\<**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a mouse button being pressed or released.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about mouse click events. See
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On Wear OS devices, rotary input is mapped to
`@GlobalScope.MOUSE_BUTTON_WHEEL_UP<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_UP>`{.interpreted-text
role="ref"} and
`@GlobalScope.MOUSE_BUTTON_WHEEL_DOWN<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_DOWN>`{.interpreted-text
role="ref"}. This can be changed to
`@GlobalScope.MOUSE_BUTTON_WHEEL_LEFT<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_LEFT>`{.interpreted-text
role="ref"} and
`@GlobalScope.MOUSE_BUTTON_WHEEL_RIGHT<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_RIGHT>`{.interpreted-text
role="ref"} with the
`ProjectSettings.input_devices/pointing/android/rotary_input_scroll_axis<class_ProjectSettings_property_input_devices/pointing/android/rotary_input_scroll_axis>`{.interpreted-text
role="ref"} setting.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`{.interpreted-text
  role="doc"}
- `Mouse and input coordinates <../tutorials/inputs/mouse_and_input_coordinates>`{.interpreted-text
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

:::: {#class_InputEventMouseButton_property_button_index}
::: rst-class
classref-property
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **button_index** = `0`
`🔗<class_InputEventMouseButton_property_button_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_button_index**(value:
  `MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
  role="ref"})
- `MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
  role="ref"} **get_button_index**()

The mouse button identifier, one of the
`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} button or button wheel constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseButton_property_canceled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **canceled** = `false`
`🔗<class_InputEventMouseButton_property_canceled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_canceled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_canceled**()

If `true`, the mouse button event has been canceled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseButton_property_double_click}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **double_click** =
`false`
`🔗<class_InputEventMouseButton_property_double_click>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_double_click**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_double_click**()

If `true`, the mouse button\'s state is a double-click.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseButton_property_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **factor** = `1.0`
`🔗<class_InputEventMouseButton_property_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_factor**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_factor**()

The amount (or delta) of the event. When used for high-precision scroll
events, this indicates the scroll amount (vertical or horizontal). This
is only supported on some platforms; the reported sensitivity varies
depending on the platform. May be `0` if not supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseButton_property_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pressed** = `false`
`🔗<class_InputEventMouseButton_property_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()

If `true`, the mouse button\'s state is pressed. If `false`, the mouse
button\'s state is released.
