github_url
:   hide

# MenuButton {#class_MenuButton}

**Inherits:** `Button<class_Button>`{.interpreted-text role="ref"}
**\<** `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A button that brings up a `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} when clicked.

::: rst-class
classref-introduction-group
:::

## Description

A button that brings up a `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} when clicked. To create new items inside this
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}, use
`get_popup().add_item("My Item Name")`. You can also create them
directly from Godot editor\'s inspector.

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

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

:::: {#class_MenuButton_signal_about_to_popup}
::: rst-class
classref-signal
:::
::::

**about_to_popup**()
`🔗<class_MenuButton_signal_about_to_popup>`{.interpreted-text
role="ref"}

Emitted when the `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} of this MenuButton is about to show.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MenuButton_property_item_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_count** = `0`
`🔗<class_MenuButton_property_item_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_item_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_item_count**()

The number of items currently in the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuButton_property_switch_on_hover}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **switch_on_hover** =
`false`
`🔗<class_MenuButton_property_switch_on_hover>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_switch_on_hover**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_switch_on_hover**()

If `true`, when the cursor hovers above another **MenuButton** within
the same parent which also has
`switch_on_hover<class_MenuButton_property_switch_on_hover>`{.interpreted-text
role="ref"} enabled, it will close the current **MenuButton** and open
the other one.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MenuButton_method_get_popup}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_popup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MenuButton_method_get_popup>`{.interpreted-text
role="ref"}

Returns the `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
contained in this button.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their `Window.visible<class_Window_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuButton_method_set_disable_shortcuts}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_shortcuts**(disabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_MenuButton_method_set_disable_shortcuts>`{.interpreted-text
role="ref"}

If `true`, shortcuts are disabled and cannot be used to trigger the
button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuButton_method_show_popup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**show_popup**()
`🔗<class_MenuButton_method_show_popup>`{.interpreted-text role="ref"}

Adjusts popup position and sizing for the **MenuButton**, then shows the
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}. Prefer this
over using `get_popup().popup()`.
