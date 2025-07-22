github_url
:   hide

# BaseButton {#class_BaseButton}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `Button<class_Button>`{.interpreted-text role="ref"},
`LinkButton<class_LinkButton>`{.interpreted-text role="ref"},
`TextureButton<class_TextureButton>`{.interpreted-text role="ref"}

Abstract base class for GUI buttons.

::: rst-class
classref-introduction-group
:::

## Description

**BaseButton** is an abstract base class for GUI buttons. It doesn\'t
display anything by itself.

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

## Signals

:::: {#class_BaseButton_signal_button_down}
::: rst-class
classref-signal
:::
::::

**button_down**()
`🔗<class_BaseButton_signal_button_down>`{.interpreted-text role="ref"}

Emitted when the button starts being held down.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_signal_button_up}
::: rst-class
classref-signal
:::
::::

**button_up**()
`🔗<class_BaseButton_signal_button_up>`{.interpreted-text role="ref"}

Emitted when the button stops being held down.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_signal_pressed}
::: rst-class
classref-signal
:::
::::

**pressed**() `🔗<class_BaseButton_signal_pressed>`{.interpreted-text
role="ref"}

Emitted when the button is toggled or pressed. This is on
`button_down<class_BaseButton_signal_button_down>`{.interpreted-text
role="ref"} if
`action_mode<class_BaseButton_property_action_mode>`{.interpreted-text
role="ref"} is
`ACTION_MODE_BUTTON_PRESS<class_BaseButton_constant_ACTION_MODE_BUTTON_PRESS>`{.interpreted-text
role="ref"} and on
`button_up<class_BaseButton_signal_button_up>`{.interpreted-text
role="ref"} otherwise.

If you need to know the button\'s pressed state (and
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is active), use
`toggled<class_BaseButton_signal_toggled>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_signal_toggled}
::: rst-class
classref-signal
:::
::::

**toggled**(toggled_on: `bool<class_bool>`{.interpreted-text
role="ref"}) `🔗<class_BaseButton_signal_toggled>`{.interpreted-text
role="ref"}

Emitted when the button was just toggled between pressed and normal
states (only if
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is active). The new state is contained in the `toggled_on`
argument.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_BaseButton_DrawMode}
::: rst-class
classref-enumeration
:::
::::

enum **DrawMode**: `🔗<enum_BaseButton_DrawMode>`{.interpreted-text
role="ref"}

:::: {#class_BaseButton_constant_DRAW_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"}
**DRAW_NORMAL** = `0`

The normal state (i.e. not pressed, not hovered, not toggled and
enabled) of buttons.

:::: {#class_BaseButton_constant_DRAW_PRESSED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"}
**DRAW_PRESSED** = `1`

The state of buttons are pressed.

:::: {#class_BaseButton_constant_DRAW_HOVER}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"}
**DRAW_HOVER** = `2`

The state of buttons are hovered.

:::: {#class_BaseButton_constant_DRAW_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"}
**DRAW_DISABLED** = `3`

The state of buttons are disabled.

:::: {#class_BaseButton_constant_DRAW_HOVER_PRESSED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"}
**DRAW_HOVER_PRESSED** = `4`

The state of buttons are both hovered and pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_BaseButton_ActionMode}
::: rst-class
classref-enumeration
:::
::::

enum **ActionMode**: `🔗<enum_BaseButton_ActionMode>`{.interpreted-text
role="ref"}

:::: {#class_BaseButton_constant_ACTION_MODE_BUTTON_PRESS}
::: rst-class
classref-enumeration-constant
:::
::::

`ActionMode<enum_BaseButton_ActionMode>`{.interpreted-text role="ref"}
**ACTION_MODE_BUTTON_PRESS** = `0`

Require just a press to consider the button clicked.

:::: {#class_BaseButton_constant_ACTION_MODE_BUTTON_RELEASE}
::: rst-class
classref-enumeration-constant
:::
::::

`ActionMode<enum_BaseButton_ActionMode>`{.interpreted-text role="ref"}
**ACTION_MODE_BUTTON_RELEASE** = `1`

Require a press and a subsequent release before considering the button
clicked.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_BaseButton_property_action_mode}
::: rst-class
classref-property
:::
::::

`ActionMode<enum_BaseButton_ActionMode>`{.interpreted-text role="ref"}
**action_mode** = `1`
`🔗<class_BaseButton_property_action_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action_mode**(value:
  `ActionMode<enum_BaseButton_ActionMode>`{.interpreted-text
  role="ref"})
- `ActionMode<enum_BaseButton_ActionMode>`{.interpreted-text role="ref"}
  **get_action_mode**()

Determines when the button is considered clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_button_group}
::: rst-class
classref-property
:::
::::

`ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"}
**button_group**
`🔗<class_BaseButton_property_button_group>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_button_group**(value:
  `ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"})
- `ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"}
  **get_button_group**()

The `ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"}
associated with the button. Not to be confused with node groups.

\*\*Note:\*\* The button will be configured as a radio button if a
`ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"} is
assigned to it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_button_mask}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"}\] **button_mask** = `1`
`🔗<class_BaseButton_property_button_mask>`{.interpreted-text
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

Binary mask to choose which mouse buttons this button will respond to.

To allow both left-click and right-click, use
`MOUSE_BUTTON_MASK_LEFT | MOUSE_BUTTON_MASK_RIGHT`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_button_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **button_pressed** =
`false` `🔗<class_BaseButton_property_button_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()

If `true`, the button\'s state is pressed. Means the button is pressed
down or toggled (if
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is active). Only works if
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* Changing the value of
`button_pressed<class_BaseButton_property_button_pressed>`{.interpreted-text
role="ref"} will result in
`toggled<class_BaseButton_signal_toggled>`{.interpreted-text role="ref"}
to be emitted. If you want to change the pressed state without emitting
that signal, use
`set_pressed_no_signal()<class_BaseButton_method_set_pressed_no_signal>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disabled** = `false`
`🔗<class_BaseButton_property_disabled>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_disabled**()

If `true`, the button is in disabled state and can\'t be clicked or
toggled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_keep_pressed_outside}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**keep_pressed_outside** = `false`
`🔗<class_BaseButton_property_keep_pressed_outside>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_pressed_outside**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_keep_pressed_outside**()

If `true`, the button stays pressed when moving the cursor outside the
button while pressing it.

\*\*Note:\*\* This property only affects the button\'s visual
appearance. Signals will be emitted at the same moment regardless of
this property\'s value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_shortcut}
::: rst-class
classref-property
:::
::::

`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} **shortcut**
`🔗<class_BaseButton_property_shortcut>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shortcut**(value: `Shortcut<class_Shortcut>`{.interpreted-text
  role="ref"})
- `Shortcut<class_Shortcut>`{.interpreted-text role="ref"}
  **get_shortcut**()

`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} associated to
the button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_shortcut_feedback}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shortcut_feedback** =
`true`
`🔗<class_BaseButton_property_shortcut_feedback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shortcut_feedback**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shortcut_feedback**()

If `true`, the button will highlight for a short amount of time when its
shortcut is activated. If `false` and
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is `false`, the shortcut will activate without any visual
feedback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_shortcut_in_tooltip}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shortcut_in_tooltip**
= `true`
`🔗<class_BaseButton_property_shortcut_in_tooltip>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shortcut_in_tooltip**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shortcut_in_tooltip_enabled**()

If `true`, the button will add information about its shortcut in the
tooltip.

\*\*Note:\*\* This property does nothing when the tooltip control is
customized using
`Control._make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_property_toggle_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **toggle_mode** =
`false` `🔗<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_toggle_mode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_toggle_mode**()

If `true`, the button is in toggle mode. Makes the button flip state
between pressed and unpressed each time its area is clicked.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_BaseButton_private_method__pressed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_pressed**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_BaseButton_private_method__pressed>`{.interpreted-text
role="ref"}

Called when the button is pressed. If you need to know the button\'s
pressed state (and
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is active), use
`_toggled()<class_BaseButton_private_method__toggled>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_private_method__toggled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_toggled**(toggled_on: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_BaseButton_private_method__toggled>`{.interpreted-text
role="ref"}

Called when the button is toggled (only if
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is active).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_method_get_draw_mode}
::: rst-class
classref-method
:::
::::

`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"}
**get_draw_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BaseButton_method_get_draw_mode>`{.interpreted-text
role="ref"}

Returns the visual state used to draw the button. This is useful mainly
when implementing your own draw code by either overriding
[draw]{#draw}() or connecting to \"draw\" signal. The visual state of
the button is defined by the
`DrawMode<enum_BaseButton_DrawMode>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_method_is_hovered}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_hovered**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_BaseButton_method_is_hovered>`{.interpreted-text
role="ref"}

Returns `true` if the mouse has entered the button and has not left it
yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BaseButton_method_set_pressed_no_signal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_pressed_no_signal**(pressed: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_BaseButton_method_set_pressed_no_signal>`{.interpreted-text
role="ref"}

Changes the
`button_pressed<class_BaseButton_property_button_pressed>`{.interpreted-text
role="ref"} state of the button, without emitting
`toggled<class_BaseButton_signal_toggled>`{.interpreted-text
role="ref"}. Use when you just want to change the state of the button
without sending the pressed event (e.g. when initializing scene). Only
works if
`toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* This method doesn\'t unpress other buttons in
`button_group<class_BaseButton_property_button_group>`{.interpreted-text
role="ref"}.
