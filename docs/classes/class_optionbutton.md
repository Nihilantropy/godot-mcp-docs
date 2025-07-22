github_url
:   hide

::: {.meta keywords="select"}
:::

# OptionButton {#class_OptionButton}

**Inherits:** `Button<class_Button>`{.interpreted-text role="ref"}
**\<** `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A button that brings up a dropdown with selectable options when pressed.

::: rst-class
classref-introduction-group
:::

## Description

**OptionButton** is a type of button that brings up a dropdown with
selectable items when pressed. The item selected becomes the \"current\"
item and is displayed as the button text.

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

\*\*Note:\*\* The IDs used for items are limited to signed 32-bit
integers, not the full 64 bits of `int<class_int>`{.interpreted-text
role="ref"}. These have a range of `-2^31` to `2^31 - 1`, that is,
`-2147483648` to `2147483647`.

\*\*Note:\*\* The
`Button.text<class_Button_property_text>`{.interpreted-text role="ref"}
and `Button.icon<class_Button_property_icon>`{.interpreted-text
role="ref"} properties are set automatically based on the selected item.
They shouldn\'t be changed manually.

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

:::: {#class_OptionButton_signal_item_focused}
::: rst-class
classref-signal
:::
::::

**item_focused**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_signal_item_focused>`{.interpreted-text
role="ref"}

Emitted when the user navigates to an item using the
`ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>`{.interpreted-text
role="ref"} or
`ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>`{.interpreted-text
role="ref"} input actions. The index of the item selected is passed as
argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_signal_item_selected}
::: rst-class
classref-signal
:::
::::

**item_selected**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_signal_item_selected>`{.interpreted-text
role="ref"}

Emitted when the current item has been changed by the user. The index of
the item selected is passed as argument.

`allow_reselect<class_OptionButton_property_allow_reselect>`{.interpreted-text
role="ref"} must be enabled to reselect an item.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OptionButton_property_allow_reselect}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_reselect** =
`false`
`🔗<class_OptionButton_property_allow_reselect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_reselect**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_reselect**()

If `true`, the currently selected item can be selected again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_property_fit_to_longest_item}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fit_to_longest_item**
= `true`
`🔗<class_OptionButton_property_fit_to_longest_item>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fit_to_longest_item**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_fit_to_longest_item**()

If `true`, minimum size will be determined by the longest item\'s text,
instead of the currently selected one\'s.

\*\*Note:\*\* For performance reasons, the minimum size doesn\'t update
immediately when adding, removing or modifying items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_property_item_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_count** = `0`
`🔗<class_OptionButton_property_item_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_item_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_item_count**()

The number of items to select from.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_property_selected}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **selected** = `-1`
`🔗<class_OptionButton_property_selected>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `int<class_int>`{.interpreted-text role="ref"} **get_selected**()

The index of the currently selected item, or `-1` if no item is
selected.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OptionButton_method_add_icon_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_item**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_OptionButton_method_add_icon_item>`{.interpreted-text
role="ref"}

Adds an item, with a `texture` icon, text `label` and (optionally) `id`.
If no `id` is passed, the item index will be used as the item\'s ID. New
items are appended at the end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_add_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_item**(label: `String<class_String>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_OptionButton_method_add_item>`{.interpreted-text role="ref"}

Adds an item, with text `label` and (optionally) `id`. If no `id` is
passed, the item index will be used as the item\'s ID. New items are
appended at the end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_add_separator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_separator**(text: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`🔗<class_OptionButton_method_add_separator>`{.interpreted-text
role="ref"}

Adds a separator to the list of items. Separators help to group items,
and can optionally be given a `text` header. A separator also gets an
index assigned, and is appended at the end of the item list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_OptionButton_method_clear>`{.interpreted-text role="ref"}

Clears all the items in the **OptionButton**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **get_item_auto_translate_mode**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_auto_translate_mode>`{.interpreted-text
role="ref"}

Returns the auto translate mode of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_item_icon**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_icon>`{.interpreted-text
role="ref"}

Returns the icon of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_item_id**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_id>`{.interpreted-text
role="ref"}

Returns the ID of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_item_index**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_index>`{.interpreted-text
role="ref"}

Returns the index of the item with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_item_metadata**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_metadata>`{.interpreted-text
role="ref"}

Retrieves the metadata of an item. Metadata may be any type and can be
used to store extra information about an item, such as an external
string ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_text**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_text>`{.interpreted-text
role="ref"}

Returns the text of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_item_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_tooltip**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_item_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_popup}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_popup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OptionButton_method_get_popup>`{.interpreted-text
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

:::: {#class_OptionButton_method_get_selectable_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selectable_item**(from_last: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_selectable_item>`{.interpreted-text
role="ref"}

Returns the index of the first item which is not disabled, or marked as
a separator. If `from_last` is `true`, the items will be searched in
reverse order.

Returns `-1` if no item is found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_selected_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_selected_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_selected_id>`{.interpreted-text
role="ref"}

Returns the ID of the selected item, or `-1` if no item is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_get_selected_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_selected_metadata**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_get_selected_metadata>`{.interpreted-text
role="ref"}

Gets the metadata of the selected item. Metadata for items can be set
using
`set_item_metadata()<class_OptionButton_method_set_item_metadata>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_has_selectable_items}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_selectable_items**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_has_selectable_items>`{.interpreted-text
role="ref"}

Returns `true` if this button contains at least one item which is not
disabled, or marked as a separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_is_item_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_disabled**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_is_item_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_is_item_separator}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_separator**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OptionButton_method_is_item_separator>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` is marked as a separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_remove_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_item**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_method_remove_item>`{.interpreted-text
role="ref"}

Removes the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_select}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **select**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_method_select>`{.interpreted-text role="ref"}

Selects an item by index and makes it the current item. This will work
even if the item is disabled.

Passing `-1` as the index deselects any currently selected item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_disable_shortcuts}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_shortcuts**(disabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_OptionButton_method_set_disable_shortcuts>`{.interpreted-text
role="ref"}

If `true`, shortcuts are disabled and cannot be used to trigger the
button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_auto_translate_mode**(idx: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"})
`🔗<class_OptionButton_method_set_item_auto_translate_mode>`{.interpreted-text
role="ref"}

Sets the auto translate mode of the item at index `idx`.

Items use
`Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>`{.interpreted-text
role="ref"} by default, which uses the same auto translate mode as the
**OptionButton** itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_disabled**(idx: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_method_set_item_disabled>`{.interpreted-text
role="ref"}

Sets whether the item at index `idx` is disabled.

Disabled items are drawn differently in the dropdown and are not
selectable by the user. If the current selected item is set as disabled,
it will remain selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon**(idx: `int<class_int>`{.interpreted-text role="ref"},
texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_method_set_item_icon>`{.interpreted-text
role="ref"}

Sets the icon of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_id**(idx: `int<class_int>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_method_set_item_id>`{.interpreted-text
role="ref"}

Sets the ID of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_metadata**(idx: `int<class_int>`{.interpreted-text
role="ref"}, metadata: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_OptionButton_method_set_item_metadata>`{.interpreted-text
role="ref"}

Sets the metadata of an item. Metadata may be of any type and can be
used to store extra information about an item, such as an external
string ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_text**(idx: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OptionButton_method_set_item_text>`{.interpreted-text
role="ref"}

Sets the text of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_set_item_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_tooltip**(idx: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_OptionButton_method_set_item_tooltip>`{.interpreted-text
role="ref"}

Sets the tooltip of the item at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_method_show_popup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**show_popup**()
`🔗<class_OptionButton_method_show_popup>`{.interpreted-text role="ref"}

Adjusts popup position and sizing for the **OptionButton**, then shows
the `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}. Prefer
this over using `get_popup().popup()`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_OptionButton_theme_constant_arrow_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **arrow_margin** = `4`
`🔗<class_OptionButton_theme_constant_arrow_margin>`{.interpreted-text
role="ref"}

The horizontal space between the arrow icon and the right edge of the
button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_theme_constant_modulate_arrow}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **modulate_arrow** = `0`
`🔗<class_OptionButton_theme_constant_modulate_arrow>`{.interpreted-text
role="ref"}

If different than `0`, the arrow icon will be modulated to the font
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OptionButton_theme_icon_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **arrow**
`🔗<class_OptionButton_theme_icon_arrow>`{.interpreted-text role="ref"}

The arrow icon to be drawn on the right end of the button.
