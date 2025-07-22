github_url
:   hide

# InputEventWithModifiers {#class_InputEventWithModifiers}

**Inherits:**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`InputEventGesture<class_InputEventGesture>`{.interpreted-text
role="ref"}, `InputEventKey<class_InputEventKey>`{.interpreted-text
role="ref"}, `InputEventMouse<class_InputEventMouse>`{.interpreted-text
role="ref"}

Abstract base class for input events affected by modifier keys like
`Shift`{.interpreted-text role="kbd"} and `Alt`{.interpreted-text
role="kbd"}.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about mouse, keyboard, and touch gesture input
events. This includes information about which modifier keys are pressed,
such as `Shift`{.interpreted-text role="kbd"} or `Alt`{.interpreted-text
role="kbd"}. See
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Modifier keys are considered modifiers only when used in
combination with another key. As a result, their corresponding member
variables, such as
`ctrl_pressed<class_InputEventWithModifiers_property_ctrl_pressed>`{.interpreted-text
role="ref"}, will return `false` if the key is pressed on its own.

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
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_InputEventWithModifiers_property_alt_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **alt_pressed** =
`false`
`🔗<class_InputEventWithModifiers_property_alt_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alt_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_alt_pressed**()

State of the `Alt`{.interpreted-text role="kbd"} modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventWithModifiers_property_command_or_control_autoremap}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**command_or_control_autoremap** = `false`
`🔗<class_InputEventWithModifiers_property_command_or_control_autoremap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_command_or_control_autoremap**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_command_or_control_autoremap**()

Automatically use `Meta`{.interpreted-text role="kbd"}
(`Cmd`{.interpreted-text role="kbd"}) on macOS and
`Ctrl`{.interpreted-text role="kbd"} on other platforms. If `true`,
`ctrl_pressed<class_InputEventWithModifiers_property_ctrl_pressed>`{.interpreted-text
role="ref"} and
`meta_pressed<class_InputEventWithModifiers_property_meta_pressed>`{.interpreted-text
role="ref"} cannot be set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventWithModifiers_property_ctrl_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ctrl_pressed** =
`false`
`🔗<class_InputEventWithModifiers_property_ctrl_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ctrl_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ctrl_pressed**()

State of the `Ctrl`{.interpreted-text role="kbd"} modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventWithModifiers_property_meta_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **meta_pressed** =
`false`
`🔗<class_InputEventWithModifiers_property_meta_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_meta_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_meta_pressed**()

State of the `Meta`{.interpreted-text role="kbd"} modifier. On Windows
and Linux, this represents the Windows key (sometimes called \"meta\" or
\"super\" on Linux). On macOS, this represents the Command key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventWithModifiers_property_shift_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shift_pressed** =
`false`
`🔗<class_InputEventWithModifiers_property_shift_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shift_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shift_pressed**()

State of the `Shift`{.interpreted-text role="kbd"} modifier.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_InputEventWithModifiers_method_get_modifiers_mask}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}\] **get_modifiers_mask**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventWithModifiers_method_get_modifiers_mask>`{.interpreted-text
role="ref"}

Returns the keycode combination of modifier keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventWithModifiers_method_is_command_or_control_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_command_or_control_pressed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventWithModifiers_method_is_command_or_control_pressed>`{.interpreted-text
role="ref"}

On macOS, returns `true` if `Meta`{.interpreted-text role="kbd"}
(`Cmd`{.interpreted-text role="kbd"}) is pressed.

On other platforms, returns `true` if `Ctrl`{.interpreted-text
role="kbd"} is pressed.
