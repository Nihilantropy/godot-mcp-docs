github_url
:   hide

::: {.meta keywords="gamepad, controller"}
:::

# InputEventJoypadButton {#class_InputEventJoypadButton}

**Inherits:** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a gamepad button being pressed or released.

::: rst-class
classref-introduction-group
:::

## Description

Input event type for gamepad buttons. For gamepad analog sticks and
joysticks, see
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"}.

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

:::: {#class_InputEventJoypadButton_property_button_index}
::: rst-class
classref-property
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**button_index** = `0`
`🔗<class_InputEventJoypadButton_property_button_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_button_index**(value:
  `JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text
  role="ref"})
- `JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
  **get_button_index**()

Button identifier. One of the
`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
button constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventJoypadButton_property_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pressed** = `false`
`🔗<class_InputEventJoypadButton_property_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()

If `true`, the button\'s state is pressed. If `false`, the button\'s
state is released.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventJoypadButton_property_pressure}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pressure** = `0.0`
`🔗<class_InputEventJoypadButton_property_pressure>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressure**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_pressure**()

**Deprecated:** This property is never set by the engine and is always
`0`.
