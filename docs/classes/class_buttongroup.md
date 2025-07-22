github_url
:   hide

# ButtonGroup {#class_ButtonGroup}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A group of buttons that doesn\'t allow more than one button to be
pressed at a time.

::: rst-class
classref-introduction-group
:::

## Description

A group of `BaseButton<class_BaseButton>`{.interpreted-text
role="ref"}-derived buttons. The buttons in a **ButtonGroup** are
treated like radio buttons: No more than one button can be pressed at a
time. Some types of buttons (such as
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"}) may have a
special appearance in this state.

Every member of a **ButtonGroup** should have
`BaseButton.toggle_mode<class_BaseButton_property_toggle_mode>`{.interpreted-text
role="ref"} set to `true`.

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

:::: {#class_ButtonGroup_signal_pressed}
::: rst-class
classref-signal
:::
::::

**pressed**(button: `BaseButton<class_BaseButton>`{.interpreted-text
role="ref"}) `🔗<class_ButtonGroup_signal_pressed>`{.interpreted-text
role="ref"}

Emitted when one of the buttons of the group is pressed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ButtonGroup_property_allow_unpress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_unpress** =
`false` `🔗<class_ButtonGroup_property_allow_unpress>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_unpress**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_allow_unpress**()

If `true`, it is possible to unpress all buttons in this
**ButtonGroup**.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ButtonGroup_method_get_buttons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`BaseButton<class_BaseButton>`{.interpreted-text
role="ref"}\] **get_buttons**()
`🔗<class_ButtonGroup_method_get_buttons>`{.interpreted-text role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Button<class_Button>`{.interpreted-text role="ref"}s who have this as
their **ButtonGroup** (see
`BaseButton.button_group<class_BaseButton_property_button_group>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ButtonGroup_method_get_pressed_button}
::: rst-class
classref-method
:::
::::

`BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
**get_pressed_button**()
`🔗<class_ButtonGroup_method_get_pressed_button>`{.interpreted-text
role="ref"}

Returns the current pressed button.
