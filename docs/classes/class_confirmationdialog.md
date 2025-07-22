github_url
:   hide

# ConfirmationDialog {#class_ConfirmationDialog}

**Inherits:** `AcceptDialog<class_AcceptDialog>`{.interpreted-text
role="ref"} **\<** `Window<class_Window>`{.interpreted-text role="ref"}
**\<** `Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorCommandPalette<class_EditorCommandPalette>`{.interpreted-text
role="ref"},
`EditorFileDialog<class_EditorFileDialog>`{.interpreted-text
role="ref"}, `FileDialog<class_FileDialog>`{.interpreted-text
role="ref"},
`ScriptCreateDialog<class_ScriptCreateDialog>`{.interpreted-text
role="ref"}

A dialog used for confirmation of actions.

::: rst-class
classref-introduction-group
:::

## Description

A dialog used for confirmation of actions. This window is similar to
`AcceptDialog<class_AcceptDialog>`{.interpreted-text role="ref"}, but
pressing its Cancel button can have a different outcome from pressing
the OK button. The order of the two buttons varies depending on the host
OS.

To get cancel action, you can use:

::::: tabs
::: code-tab
gdscript

get_cancel_button().pressed.connect([on_canceled]{#on_canceled})
:::

::: code-tab
csharp

GetCancelButton().Pressed += OnCanceled;
:::
:::::

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

:::: {#class_ConfirmationDialog_property_cancel_button_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**cancel_button_text** = `"Cancel"`
`🔗<class_ConfirmationDialog_property_cancel_button_text>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cancel_button_text**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_cancel_button_text**()

The text displayed by the cancel button (see
`get_cancel_button()<class_ConfirmationDialog_method_get_cancel_button>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ConfirmationDialog_method_get_cancel_button}
::: rst-class
classref-method
:::
::::

`Button<class_Button>`{.interpreted-text role="ref"}
**get_cancel_button**()
`🔗<class_ConfirmationDialog_method_get_cancel_button>`{.interpreted-text
role="ref"}

Returns the cancel button.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.
