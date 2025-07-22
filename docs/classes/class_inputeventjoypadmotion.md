github_url
:   hide

::: {.meta keywords="gamepad, controller"}
:::

# InputEventJoypadMotion {#class_InputEventJoypadMotion}

**Inherits:** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents axis motions (such as joystick or analog triggers) from a
gamepad.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about joystick motions. One
**InputEventJoypadMotion** represents one axis at a time. For gamepad
buttons, see
`InputEventJoypadButton<class_InputEventJoypadButton>`{.interpreted-text
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

:::: {#class_InputEventJoypadMotion_property_axis}
::: rst-class
classref-property
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**axis** = `0`
`🔗<class_InputEventJoypadMotion_property_axis>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis**(value:
  `JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"})
- `JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
  **get_axis**()

Axis identifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventJoypadMotion_property_axis_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **axis_value** =
`0.0`
`🔗<class_InputEventJoypadMotion_property_axis_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_value**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_axis_value**()

Current position of the joystick on the given axis. The value ranges
from `-1.0` to `1.0`. A value of `0` means the axis is in its resting
position.
