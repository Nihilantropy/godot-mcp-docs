github_url
:   hide

# AcceptDialog {#class_AcceptDialog}

**Inherits:** `Window<class_Window>`{.interpreted-text role="ref"}
**\<** `Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`ConfirmationDialog<class_ConfirmationDialog>`{.interpreted-text
role="ref"}

A base dialog used for user notification.

::: rst-class
classref-introduction-group
:::

## Description

The default use of **AcceptDialog** is to allow it to only be accepted
or closed, with the same result. However, the
`confirmed<class_AcceptDialog_signal_confirmed>`{.interpreted-text
role="ref"} and
`canceled<class_AcceptDialog_signal_canceled>`{.interpreted-text
role="ref"} signals allow to make the two actions different, and the
`add_button()<class_AcceptDialog_method_add_button>`{.interpreted-text
role="ref"} method allows to add custom buttons and actions.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_AcceptDialog_signal_canceled}
::: rst-class
classref-signal
:::
::::

**canceled**()
`🔗<class_AcceptDialog_signal_canceled>`{.interpreted-text role="ref"}

Emitted when the dialog is closed or the button created with
`add_cancel_button()<class_AcceptDialog_method_add_cancel_button>`{.interpreted-text
role="ref"} is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_signal_confirmed}
::: rst-class
classref-signal
:::
::::

**confirmed**()
`🔗<class_AcceptDialog_signal_confirmed>`{.interpreted-text role="ref"}

Emitted when the dialog is accepted, i.e. the OK button is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_signal_custom_action}
::: rst-class
classref-signal
:::
::::

**custom_action**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AcceptDialog_signal_custom_action>`{.interpreted-text
role="ref"}

Emitted when a custom button with an action is pressed. See
`add_button()<class_AcceptDialog_method_add_button>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AcceptDialog_property_dialog_autowrap}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **dialog_autowrap** =
`false`
`🔗<class_AcceptDialog_property_dialog_autowrap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_autowrap**()

Sets autowrapping for the text in the dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_property_dialog_close_on_escape}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**dialog_close_on_escape** = `true`
`🔗<class_AcceptDialog_property_dialog_close_on_escape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_close_on_escape**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_close_on_escape**()

If `true`, the dialog will be hidden when the `ui_cancel` action is
pressed (by default, this action is bound to
`@GlobalScope.KEY_ESCAPE<class_@GlobalScope_constant_KEY_ESCAPE>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_property_dialog_hide_on_ok}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **dialog_hide_on_ok** =
`true`
`🔗<class_AcceptDialog_property_dialog_hide_on_ok>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_on_ok**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_hide_on_ok**()

If `true`, the dialog is hidden when the OK button is pressed. You can
set it to `false` if you want to do e.g. input validation when receiving
the `confirmed<class_AcceptDialog_signal_confirmed>`{.interpreted-text
role="ref"} signal, and handle hiding the dialog in your own logic.

\*\*Note:\*\* Some nodes derived from this class can have a different
default value, and potentially their own built-in logic overriding this
setting. For example `FileDialog<class_FileDialog>`{.interpreted-text
role="ref"} defaults to `false`, and has its own input validation code
that is called when you press OK, which eventually hides the dialog if
the input is valid. As such, this property can\'t be used in
`FileDialog<class_FileDialog>`{.interpreted-text role="ref"} to disable
hiding the dialog when pressing OK.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_property_dialog_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **dialog_text** =
`""` `🔗<class_AcceptDialog_property_dialog_text>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

The text displayed by the dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_property_ok_button_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **ok_button_text**
= `""`
`🔗<class_AcceptDialog_property_ok_button_text>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ok_button_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_ok_button_text**()

The text displayed by the OK button (see
`get_ok_button()<class_AcceptDialog_method_get_ok_button>`{.interpreted-text
role="ref"}). If empty, a default text will be used.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AcceptDialog_method_add_button}
::: rst-class
classref-method
:::
::::

`Button<class_Button>`{.interpreted-text role="ref"}
**add_button**(text: `String<class_String>`{.interpreted-text
role="ref"}, right: `bool<class_bool>`{.interpreted-text role="ref"} =
false, action: `String<class_String>`{.interpreted-text role="ref"} =
\"\") `🔗<class_AcceptDialog_method_add_button>`{.interpreted-text
role="ref"}

Adds a button with label `text` and a custom `action` to the dialog and
returns the created button.

If `action` is not empty, pressing the button will emit the
`custom_action<class_AcceptDialog_signal_custom_action>`{.interpreted-text
role="ref"} signal with the specified action string.

If `true`, `right` will place the button to the right of any sibling
buttons.

You can use
`remove_button()<class_AcceptDialog_method_remove_button>`{.interpreted-text
role="ref"} method to remove a button created with this method from the
dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_method_add_cancel_button}
::: rst-class
classref-method
:::
::::

`Button<class_Button>`{.interpreted-text role="ref"}
**add_cancel_button**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_AcceptDialog_method_add_cancel_button>`{.interpreted-text
role="ref"}

Adds a button with label `name` and a cancel action to the dialog and
returns the created button.

You can use
`remove_button()<class_AcceptDialog_method_remove_button>`{.interpreted-text
role="ref"} method to remove a button created with this method from the
dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_method_get_label}
::: rst-class
classref-method
:::
::::

`Label<class_Label>`{.interpreted-text role="ref"} **get_label**()
`🔗<class_AcceptDialog_method_get_label>`{.interpreted-text role="ref"}

Returns the label used for built-in text.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_method_get_ok_button}
::: rst-class
classref-method
:::
::::

`Button<class_Button>`{.interpreted-text role="ref"} **get_ok_button**()
`🔗<class_AcceptDialog_method_get_ok_button>`{.interpreted-text
role="ref"}

Returns the OK `Button<class_Button>`{.interpreted-text role="ref"}
instance.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_method_register_text_enter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_text_enter**(line_edit:
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"})
`🔗<class_AcceptDialog_method_register_text_enter>`{.interpreted-text
role="ref"}

Registers a `LineEdit<class_LineEdit>`{.interpreted-text role="ref"} in
the dialog. When the enter key is pressed, the dialog will be accepted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_method_remove_button}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_button**(button: `Button<class_Button>`{.interpreted-text
role="ref"})
`🔗<class_AcceptDialog_method_remove_button>`{.interpreted-text
role="ref"}

Removes the `button` from the dialog. Does NOT free the `button`. The
`button` must be a `Button<class_Button>`{.interpreted-text role="ref"}
added with
`add_button()<class_AcceptDialog_method_add_button>`{.interpreted-text
role="ref"} or
`add_cancel_button()<class_AcceptDialog_method_add_cancel_button>`{.interpreted-text
role="ref"} method. After removal, pressing the `button` will no longer
emit this dialog\'s
`custom_action<class_AcceptDialog_signal_custom_action>`{.interpreted-text
role="ref"} or
`canceled<class_AcceptDialog_signal_canceled>`{.interpreted-text
role="ref"} signals.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_AcceptDialog_theme_constant_buttons_min_height}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buttons_min_height** =
`0`
`🔗<class_AcceptDialog_theme_constant_buttons_min_height>`{.interpreted-text
role="ref"}

The minimum height of each button in the bottom row (such as OK/Cancel)
in pixels. This can be increased to make buttons with short texts easier
to click/tap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_theme_constant_buttons_min_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buttons_min_width** =
`0`
`🔗<class_AcceptDialog_theme_constant_buttons_min_width>`{.interpreted-text
role="ref"}

The minimum width of each button in the bottom row (such as OK/Cancel)
in pixels. This can be increased to make buttons with short texts easier
to click/tap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_theme_constant_buttons_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buttons_separation** =
`10`
`🔗<class_AcceptDialog_theme_constant_buttons_separation>`{.interpreted-text
role="ref"}

The size of the vertical space between the dialog\'s content and the
button row.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AcceptDialog_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_AcceptDialog_theme_style_panel>`{.interpreted-text role="ref"}

The panel that fills the background of the window.
