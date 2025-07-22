github_url
:   hide

# PopupMenu {#class_PopupMenu}

**Inherits:** `Popup<class_Popup>`{.interpreted-text role="ref"} **\<**
`Window<class_Window>`{.interpreted-text role="ref"} **\<**
`Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A modal window used to display a list of options.

::: rst-class
classref-introduction-group
:::

## Description

**PopupMenu** is a modal window used to display a list of options.
Useful for toolbars and context menus.

The size of a **PopupMenu** can be limited by using
`Window.max_size<class_Window_property_max_size>`{.interpreted-text
role="ref"}. If the height of the list of items is larger than the
maximum height of the **PopupMenu**, a
`ScrollContainer<class_ScrollContainer>`{.interpreted-text role="ref"}
within the popup will allow the user to scroll the contents. If no
maximum size is set, or if it is set to `0`, the **PopupMenu** height
will be limited by its parent rect.

All `set_*` methods allow negative item indices, i.e. `-1` to access the
last item, `-2` to select the second-to-last item, and so on.

\*\*Incremental search:\*\* Like
`ItemList<class_ItemList>`{.interpreted-text role="ref"} and
`Tree<class_Tree>`{.interpreted-text role="ref"}, **PopupMenu** supports
searching within the list while the control is focused. Press a key that
matches the first letter of an item\'s name to select the first item
starting with the given letter. After that point, there are two ways to
perform incremental search: 1) Press the same key again before the
timeout duration to select the next item starting with the same letter.
2) Press letter keys that match the rest of the word before the timeout
duration to match to select the item in question directly. Both of these
actions will be reset to the beginning of the list if the timeout
duration has passed since the last keystroke was registered. You can
adjust the timeout duration by changing
`ProjectSettings.gui/timers/incremental_search_max_interval_msec<class_ProjectSettings_property_gui/timers/incremental_search_max_interval_msec>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The ID values used for items are limited to 32 bits, not
full 64 bits of `int<class_int>`{.interpreted-text role="ref"}. This has
a range of `-2^32` to `2^32 - 1`, i.e. `-2147483648` to `2147483647`.

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

:::: {#class_PopupMenu_signal_id_focused}
::: rst-class
classref-signal
:::
::::

**id_focused**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_signal_id_focused>`{.interpreted-text role="ref"}

Emitted when the user navigated to an item of some `id` using the
`ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>`{.interpreted-text
role="ref"} or
`ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>`{.interpreted-text
role="ref"} input action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_signal_id_pressed}
::: rst-class
classref-signal
:::
::::

**id_pressed**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_signal_id_pressed>`{.interpreted-text role="ref"}

Emitted when an item of some `id` is pressed or its accelerator is
activated.

\*\*Note:\*\* If `id` is negative (either explicitly or due to
overflow), this will return the corresponding index instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_signal_index_pressed}
::: rst-class
classref-signal
:::
::::

**index_pressed**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_signal_index_pressed>`{.interpreted-text role="ref"}

Emitted when an item of some `index` is pressed or its accelerator is
activated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_signal_menu_changed}
::: rst-class
classref-signal
:::
::::

**menu_changed**()
`🔗<class_PopupMenu_signal_menu_changed>`{.interpreted-text role="ref"}

Emitted when any item is added, modified or removed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PopupMenu_property_allow_search}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_search** =
`true` `🔗<class_PopupMenu_property_allow_search>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_search**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_search**()

If `true`, allows navigating **PopupMenu** with letter keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_property_hide_on_checkable_item_selection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**hide_on_checkable_item_selection** = `true`
`🔗<class_PopupMenu_property_hide_on_checkable_item_selection>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_on_checkable_item_selection**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hide_on_checkable_item_selection**()

If `true`, hides the **PopupMenu** when a checkbox or radio button is
selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_property_hide_on_item_selection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**hide_on_item_selection** = `true`
`🔗<class_PopupMenu_property_hide_on_item_selection>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_on_item_selection**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hide_on_item_selection**()

If `true`, hides the **PopupMenu** when an item is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_property_hide_on_state_item_selection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**hide_on_state_item_selection** = `false`
`🔗<class_PopupMenu_property_hide_on_state_item_selection>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_on_state_item_selection**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hide_on_state_item_selection**()

If `true`, hides the **PopupMenu** when a state item is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_property_item_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_count** = `0`
`🔗<class_PopupMenu_property_item_count>`{.interpreted-text role="ref"}

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

:::: {#class_PopupMenu_property_prefer_native_menu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **prefer_native_menu**
= `false`
`🔗<class_PopupMenu_property_prefer_native_menu>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_prefer_native_menu**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_prefer_native_menu**()

If `true`, `MenuBar<class_MenuBar>`{.interpreted-text role="ref"} will
use native menu when supported.

\*\*Note:\*\* If **PopupMenu** is linked to
`StatusIndicator<class_StatusIndicator>`{.interpreted-text role="ref"},
`MenuBar<class_MenuBar>`{.interpreted-text role="ref"}, or another
**PopupMenu** item it can use native menu regardless of this property,
use
`is_native_menu()<class_PopupMenu_method_is_native_menu>`{.interpreted-text
role="ref"} to check it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_property_submenu_popup_delay}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**submenu_popup_delay** = `0.3`
`🔗<class_PopupMenu_property_submenu_popup_delay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_submenu_popup_delay**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_submenu_popup_delay**()

Sets the delay time in seconds for the submenu item to popup on mouse
hovering. If the popup menu is added as a child of another (acting as a
submenu), it will inherit the delay time of the parent menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_property_system_menu_id}
::: rst-class
classref-property
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**system_menu_id** = `0`
`🔗<class_PopupMenu_property_system_menu_id>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_system_menu**(value:
  `SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text
  role="ref"})
- `SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text
  role="ref"} **get_system_menu**()

If set to one of the values of
`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text
role="ref"}, this **PopupMenu** is bound to the special system menu.
Only one **PopupMenu** can be bound to each special menu at a time.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PopupMenu_method_activate_item_by_event}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**activate_item_by_event**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"},
for_global_only: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_PopupMenu_method_activate_item_by_event>`{.interpreted-text
role="ref"}

Checks the provided `event` against the **PopupMenu**\'s shortcuts and
accelerators, and activates the first item with matching events. If
`for_global_only` is `true`, only shortcuts and accelerators with
`global` set to `true` will be called.

Returns `true` if an item was successfully activated.

\*\*Note:\*\* Certain `Control<class_Control>`{.interpreted-text
role="ref"}s, such as `MenuButton<class_MenuButton>`{.interpreted-text
role="ref"}, will call this method automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_check_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_check_item**(label: `String<class_String>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"} = -1,
accel: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_check_item>`{.interpreted-text
role="ref"}

Adds a new checkable item with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`).
If no `id` is provided, one will be created from the index. If no
`accel` is provided, then the default value of 0 (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}) will be assigned to the item (which means it won\'t have
any accelerator). See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.
See
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_check_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_check_shortcut**(shortcut:
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, global:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PopupMenu_method_add_check_shortcut>`{.interpreted-text
role="ref"}

Adds a new checkable item and assigns the specified
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} to it. Sets the
label of the checkbox to the
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}\'s name.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.
See
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_icon_check_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_check_item**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, accel:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_icon_check_item>`{.interpreted-text
role="ref"}

Adds a new checkable item with text `label` and icon `texture`.

An `id` can optionally be provided, as well as an accelerator (`accel`).
If no `id` is provided, one will be created from the index. If no
`accel` is provided, then the default value of 0 (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}) will be assigned to the item (which means it won\'t have
any accelerator). See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.
See
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_icon_check_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_check_shortcut**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, shortcut:
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, global:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PopupMenu_method_add_icon_check_shortcut>`{.interpreted-text
role="ref"}

Adds a new checkable item and assigns the specified
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} and icon
`texture` to it. Sets the label of the checkbox to the
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}\'s name.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.
See
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_icon_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_item**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, accel:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_icon_item>`{.interpreted-text role="ref"}

Adds a new item with text `label` and icon `texture`.

An `id` can optionally be provided, as well as an accelerator (`accel`).
If no `id` is provided, one will be created from the index. If no
`accel` is provided, then the default value of 0 (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}) will be assigned to the item (which means it won\'t have
any accelerator). See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_icon_radio_check_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_radio_check_item**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, accel:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_icon_radio_check_item>`{.interpreted-text
role="ref"}

Same as
`add_icon_check_item()<class_PopupMenu_method_add_icon_check_item>`{.interpreted-text
role="ref"}, but uses a radio check button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_icon_radio_check_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_radio_check_shortcut**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, shortcut:
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, global:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PopupMenu_method_add_icon_radio_check_shortcut>`{.interpreted-text
role="ref"}

Same as
`add_icon_check_shortcut()<class_PopupMenu_method_add_icon_check_shortcut>`{.interpreted-text
role="ref"}, but uses a radio check button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_icon_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_icon_shortcut**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, shortcut:
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, global:
`bool<class_bool>`{.interpreted-text role="ref"} = false, allow_echo:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PopupMenu_method_add_icon_shortcut>`{.interpreted-text
role="ref"}

Adds a new item and assigns the specified
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} and icon
`texture` to it. Sets the label of the checkbox to the
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}\'s name.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

If `allow_echo` is `true`, the shortcut can be activated with echo
events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_item**(label: `String<class_String>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"} = -1,
accel: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_item>`{.interpreted-text role="ref"}

Adds a new item with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`).
If no `id` is provided, one will be created from the index. If no
`accel` is provided, then the default value of 0 (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}) will be assigned to the item (which means it won\'t have
any accelerator). See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

\*\*Note:\*\* The provided `id` is used only in
`id_pressed<class_PopupMenu_signal_id_pressed>`{.interpreted-text
role="ref"} and
`id_focused<class_PopupMenu_signal_id_focused>`{.interpreted-text
role="ref"} signals. It\'s not related to the `index` arguments in e.g.
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_multistate_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_multistate_item**(label: `String<class_String>`{.interpreted-text
role="ref"}, max_states: `int<class_int>`{.interpreted-text role="ref"},
default_state: `int<class_int>`{.interpreted-text role="ref"} = 0, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, accel:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_multistate_item>`{.interpreted-text
role="ref"}

Adds a new multistate item with text `label`.

Contrarily to normal binary items, multistate items can have more than
two states, as defined by `max_states`. The default value is defined by
`default_state`.

An `id` can optionally be provided, as well as an accelerator (`accel`).
If no `id` is provided, one will be created from the index. If no
`accel` is provided, then the default value of 0 (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}) will be assigned to the item (which means it won\'t have
any accelerator). See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

    func _ready():
        add_multistate_item("Item", 3, 0)

        index_pressed.connect(func(index: int):
                toggle_item_multistate(index)
                match get_item_multistate(index):
                    0:
                        print("First state")
                    1:
                        print("Second state")
                    2:
                        print("Third state")
            )

\*\*Note:\*\* Multistate items don\'t update their state automatically
and must be done manually. See
`toggle_item_multistate()<class_PopupMenu_method_toggle_item_multistate>`{.interpreted-text
role="ref"},
`set_item_multistate()<class_PopupMenu_method_set_item_multistate>`{.interpreted-text
role="ref"} and
`get_item_multistate()<class_PopupMenu_method_get_item_multistate>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_radio_check_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_radio_check_item**(label: `String<class_String>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"} = -1,
accel: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} = 0)
`🔗<class_PopupMenu_method_add_radio_check_item>`{.interpreted-text
role="ref"}

Adds a new radio check button with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`).
If no `id` is provided, one will be created from the index. If no
`accel` is provided, then the default value of 0 (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}) will be assigned to the item (which means it won\'t have
any accelerator). See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.
See
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_radio_check_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_radio_check_shortcut**(shortcut:
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, global:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PopupMenu_method_add_radio_check_shortcut>`{.interpreted-text
role="ref"}

Adds a new radio check button and assigns a
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} to it. Sets the
label of the checkbox to the
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}\'s name.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.
See
`set_item_checked()<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_separator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_separator**(label: `String<class_String>`{.interpreted-text
role="ref"} = \"\", id: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_PopupMenu_method_add_separator>`{.interpreted-text
role="ref"}

Adds a separator between items. Separators also occupy an index, which
you can set by using the `id` parameter.

A `label` can optionally be provided, which will appear at the center of
the separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_shortcut**(shortcut: `Shortcut<class_Shortcut>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"} = -1,
global: `bool<class_bool>`{.interpreted-text role="ref"} = false,
allow_echo: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PopupMenu_method_add_shortcut>`{.interpreted-text role="ref"}

Adds a `Shortcut<class_Shortcut>`{.interpreted-text role="ref"}.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

If `allow_echo` is `true`, the shortcut can be activated with echo
events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_submenu_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_submenu_item**(label: `String<class_String>`{.interpreted-text
role="ref"}, submenu: `String<class_String>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_PopupMenu_method_add_submenu_item>`{.interpreted-text
role="ref"}

**Deprecated:** Prefer using
`add_submenu_node_item()<class_PopupMenu_method_add_submenu_node_item>`{.interpreted-text
role="ref"} instead.

Adds an item that will act as a submenu of the parent **PopupMenu** node
when clicked. The `submenu` argument must be the name of an existing
**PopupMenu** that has been added as a child to this node. This submenu
will be shown when the item is clicked, hovered for long enough, or
activated using the `ui_select` or `ui_right` input actions.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_add_submenu_node_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_submenu_node_item**(label:
`String<class_String>`{.interpreted-text role="ref"}, submenu:
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_PopupMenu_method_add_submenu_node_item>`{.interpreted-text
role="ref"}

Adds an item that will act as a submenu of the parent **PopupMenu** node
when clicked. This submenu will be shown when the item is clicked,
hovered for long enough, or activated using the `ui_select` or
`ui_right` input actions.

`submenu` must be either child of this **PopupMenu** or has no parent
node (in which case it will be automatically added as a child). If the
`submenu` popup has another parent, this method will fail.

An `id` can optionally be provided. If no `id` is provided, one will be
created from the index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear**(free_submenus: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_PopupMenu_method_clear>`{.interpreted-text role="ref"}

Removes all items from the **PopupMenu**. If `free_submenus` is `true`,
the submenu nodes are automatically freed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_focused_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_focused_item**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_focused_item>`{.interpreted-text
role="ref"}

Returns the index of the currently focused item. Returns `-1` if no item
is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_accelerator}
::: rst-class
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**get_item_accelerator**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"}

Returns the accelerator of the item at the given `index`. An accelerator
is a keyboard shortcut that can be pressed to trigger the menu button
even if it\'s not currently open. The return value is an integer which
is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}). If no accelerator is defined
for the specified `index`,
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} returns `0` (corresponding to
`@GlobalScope.KEY_NONE<class_@GlobalScope_constant_KEY_NONE>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **get_item_auto_translate_mode**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_auto_translate_mode>`{.interpreted-text
role="ref"}

Returns the auto translate mode of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_item_icon**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_icon>`{.interpreted-text role="ref"}

Returns the icon of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_icon_max_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_icon_max_width**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_icon_max_width>`{.interpreted-text
role="ref"}

Returns the maximum allowed width of the icon for the item at the given
`index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_icon_modulate}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_item_icon_modulate**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_icon_modulate>`{.interpreted-text
role="ref"}

Returns a `Color<class_Color>`{.interpreted-text role="ref"} modulating
the item\'s icon at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_item_id**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PopupMenu_method_get_item_id>`{.interpreted-text
role="ref"}

Returns the ID of the item at the given `index`. `id` can be manually
assigned, while index can not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_indent}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_indent**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_indent>`{.interpreted-text
role="ref"}

Returns the horizontal offset of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_item_index**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_index>`{.interpreted-text
role="ref"}

Returns the index of the item containing the specified `id`. Index is
automatically assigned to each item by the engine and can not be set
manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_language**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_language>`{.interpreted-text
role="ref"}

Returns item\'s text language code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_item_metadata**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_metadata>`{.interpreted-text
role="ref"}

Returns the metadata of the specified item, which might be of any type.
You can set it with
`set_item_metadata()<class_PopupMenu_method_set_item_metadata>`{.interpreted-text
role="ref"}, which provides a simple way of assigning context data to
items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_multistate}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_multistate**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_multistate>`{.interpreted-text
role="ref"}

Returns the state of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_multistate_max}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_multistate_max**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_multistate_max>`{.interpreted-text
role="ref"}

Returns the max states of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_shortcut}
::: rst-class
classref-method
:::
::::

`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}
**get_item_shortcut**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_shortcut>`{.interpreted-text
role="ref"}

Returns the `Shortcut<class_Shortcut>`{.interpreted-text role="ref"}
associated with the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_submenu}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_submenu**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_submenu>`{.interpreted-text
role="ref"}

**Deprecated:** Prefer using
`get_item_submenu_node()<class_PopupMenu_method_get_item_submenu_node>`{.interpreted-text
role="ref"} instead.

Returns the submenu name of the item at the given `index`. See
`add_submenu_item()<class_PopupMenu_method_add_submenu_item>`{.interpreted-text
role="ref"} for more info on how to add a submenu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_submenu_node}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_item_submenu_node**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_submenu_node>`{.interpreted-text
role="ref"}

Returns the submenu of the item at the given `index`, or `null` if no
submenu was added. See
`add_submenu_node_item()<class_PopupMenu_method_add_submenu_node_item>`{.interpreted-text
role="ref"} for more info on how to add a submenu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_text**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_text>`{.interpreted-text role="ref"}

Returns the text of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_text_direction}
::: rst-class
classref-method
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **get_item_text_direction**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_text_direction>`{.interpreted-text
role="ref"}

Returns item\'s text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_get_item_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_tooltip**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_get_item_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip associated with the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_item_checkable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_checkable**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_item_checkable>`{.interpreted-text
role="ref"}

Returns `true` if the item at the given `index` is checkable in some
way, i.e. if it has a checkbox or radio button.

\*\*Note:\*\* Checkable items just display a checkmark or radio button,
but don\'t have any built-in checking behavior and must be
checked/unchecked manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_item_checked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_checked**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_item_checked>`{.interpreted-text
role="ref"}

Returns `true` if the item at the given `index` is checked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_item_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_disabled**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_item_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the item at the given `index` is disabled. When it is
disabled it can\'t be selected, or its action invoked.

See
`set_item_disabled()<class_PopupMenu_method_set_item_disabled>`{.interpreted-text
role="ref"} for more info on how to disable an item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_item_radio_checkable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_radio_checkable**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_item_radio_checkable>`{.interpreted-text
role="ref"}

Returns `true` if the item at the given `index` has radio button-style
checkability.

\*\*Note:\*\* This is purely cosmetic; you must add the logic for
checking/unchecking items in radio groups.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_item_separator}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_separator**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_item_separator>`{.interpreted-text
role="ref"}

Returns `true` if the item is a separator. If it is, it will be
displayed as a line. See
`add_separator()<class_PopupMenu_method_add_separator>`{.interpreted-text
role="ref"} for more info on how to add a separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_item_shortcut_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_shortcut_disabled**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_item_shortcut_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the specified item\'s shortcut is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_native_menu}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_native_menu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_native_menu>`{.interpreted-text
role="ref"}

Returns `true` if the system native menu is supported and currently used
by this **PopupMenu**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_is_system_menu}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_system_menu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PopupMenu_method_is_system_menu>`{.interpreted-text
role="ref"}

Returns `true` if the menu is bound to the special system menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_remove_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_item**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_remove_item>`{.interpreted-text role="ref"}

Removes the item at the given `index` from the menu.

\*\*Note:\*\* The indices of items after the removed item will be
shifted by one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_scroll_to_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scroll_to_item**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_scroll_to_item>`{.interpreted-text
role="ref"}

Moves the scroll view to make the item at the given `index` visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_focused_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_focused_item**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_focused_item>`{.interpreted-text
role="ref"}

Sets the currently focused item as the given `index`.

Passing `-1` as the index makes so that no item is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_accelerator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_accelerator**(index: `int<class_int>`{.interpreted-text
role="ref"}, accel: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_accelerator>`{.interpreted-text
role="ref"}

Sets the accelerator of the item at the given `index`. An accelerator is
a keyboard shortcut that can be pressed to trigger the menu button even
if it\'s not currently open. `accel` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_as_checkable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_as_checkable**(index: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_as_checkable>`{.interpreted-text
role="ref"}

Sets whether the item at the given `index` has a checkbox. If `false`,
sets the type of the item to plain text.

\*\*Note:\*\* Checkable items just display a checkmark, but don\'t have
any built-in checking behavior and must be checked/unchecked manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_as_radio_checkable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_as_radio_checkable**(index:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_as_radio_checkable>`{.interpreted-text
role="ref"}

Sets the type of the item at the given `index` to radio button. If
`false`, sets the type of the item to plain text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_as_separator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_as_separator**(index: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_as_separator>`{.interpreted-text
role="ref"}

Mark the item at the given `index` as a separator, which means that it
would be displayed as a line. If `false`, sets the type of the item to
plain text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_auto_translate_mode**(index:
`int<class_int>`{.interpreted-text role="ref"}, mode:
`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_auto_translate_mode>`{.interpreted-text
role="ref"}

Sets the auto translate mode of the item at the given `index`.

Items use
`Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>`{.interpreted-text
role="ref"} by default, which uses the same auto translate mode as the
**PopupMenu** itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_checked}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_checked**(index: `int<class_int>`{.interpreted-text
role="ref"}, checked: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_checked>`{.interpreted-text
role="ref"}

Sets the checkstate status of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_disabled**(index: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_disabled>`{.interpreted-text
role="ref"}

Enables/disables the item at the given `index`. When it is disabled, it
can\'t be selected and its action can\'t be invoked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon**(index: `int<class_int>`{.interpreted-text role="ref"},
icon: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_icon>`{.interpreted-text role="ref"}

Replaces the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
icon of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_icon_max_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon_max_width**(index: `int<class_int>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_icon_max_width>`{.interpreted-text
role="ref"}

Sets the maximum allowed width of the icon for the item at the given
`index`. This limit is applied on top of the default size of the icon
and on top of
`icon_max_width<class_PopupMenu_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_icon_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon_modulate**(index: `int<class_int>`{.interpreted-text
role="ref"}, modulate: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_icon_modulate>`{.interpreted-text
role="ref"}

Sets a modulating `Color<class_Color>`{.interpreted-text role="ref"} of
the item\'s icon at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_id**(index: `int<class_int>`{.interpreted-text role="ref"},
id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_id>`{.interpreted-text role="ref"}

Sets the `id` of the item at the given `index`.

The `id` is used in
`id_pressed<class_PopupMenu_signal_id_pressed>`{.interpreted-text
role="ref"} and
`id_focused<class_PopupMenu_signal_id_focused>`{.interpreted-text
role="ref"} signals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_indent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_indent**(index: `int<class_int>`{.interpreted-text
role="ref"}, indent: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_indent>`{.interpreted-text
role="ref"}

Sets the horizontal offset of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_language}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_language**(index: `int<class_int>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_language>`{.interpreted-text
role="ref"}

Sets language code of item\'s text used for line-breaking and text
shaping algorithms, if left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_metadata**(index: `int<class_int>`{.interpreted-text
role="ref"}, metadata: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_metadata>`{.interpreted-text
role="ref"}

Sets the metadata of an item, which may be of any type. You can later
get it with
`get_item_metadata()<class_PopupMenu_method_get_item_metadata>`{.interpreted-text
role="ref"}, which provides a simple way of assigning context data to
items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_multistate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_multistate**(index: `int<class_int>`{.interpreted-text
role="ref"}, state: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_multistate>`{.interpreted-text
role="ref"}

Sets the state of a multistate item. See
`add_multistate_item()<class_PopupMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_multistate_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_multistate_max**(index: `int<class_int>`{.interpreted-text
role="ref"}, max_states: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_multistate_max>`{.interpreted-text
role="ref"}

Sets the max states of a multistate item. See
`add_multistate_item()<class_PopupMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_shortcut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_shortcut**(index: `int<class_int>`{.interpreted-text
role="ref"}, shortcut: `Shortcut<class_Shortcut>`{.interpreted-text
role="ref"}, global: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_PopupMenu_method_set_item_shortcut>`{.interpreted-text
role="ref"}

Sets a `Shortcut<class_Shortcut>`{.interpreted-text role="ref"} for the
item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_shortcut_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_shortcut_disabled**(index: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_shortcut_disabled>`{.interpreted-text
role="ref"}

Disables the `Shortcut<class_Shortcut>`{.interpreted-text role="ref"} of
the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_submenu}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_submenu**(index: `int<class_int>`{.interpreted-text
role="ref"}, submenu: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_submenu>`{.interpreted-text
role="ref"}

**Deprecated:** Prefer using
`set_item_submenu_node()<class_PopupMenu_method_set_item_submenu_node>`{.interpreted-text
role="ref"} instead.

Sets the submenu of the item at the given `index`. The submenu is the
name of a child **PopupMenu** node that would be shown when the item is
clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_submenu_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_submenu_node**(index: `int<class_int>`{.interpreted-text
role="ref"}, submenu: `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_submenu_node>`{.interpreted-text
role="ref"}

Sets the submenu of the item at the given `index`. The submenu is a
**PopupMenu** node that would be shown when the item is clicked. It must
either be a child of this **PopupMenu** or has no parent (in which case
it will be automatically added as a child). If the `submenu` popup has
another parent, this method will fail.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_text**(index: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PopupMenu_method_set_item_text>`{.interpreted-text role="ref"}

Sets the text of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_text_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_text_direction**(index: `int<class_int>`{.interpreted-text
role="ref"}, direction:
`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_text_direction>`{.interpreted-text
role="ref"}

Sets item\'s text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_set_item_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_tooltip**(index: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_set_item_tooltip>`{.interpreted-text
role="ref"}

Sets the `String<class_String>`{.interpreted-text role="ref"} tooltip of
the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_toggle_item_checked}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**toggle_item_checked**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_toggle_item_checked>`{.interpreted-text
role="ref"}

Toggles the check state of the item at the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_method_toggle_item_multistate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**toggle_item_multistate**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_PopupMenu_method_toggle_item_multistate>`{.interpreted-text
role="ref"}

Cycle to the next state of a multistate item. See
`add_multistate_item()<class_PopupMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_PopupMenu_theme_color_font_accelerator_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_accelerator_color** = `Color(0.7, 0.7, 0.7, 0.8)`
`🔗<class_PopupMenu_theme_color_font_accelerator_color>`{.interpreted-text
role="ref"}

The text `Color<class_Color>`{.interpreted-text role="ref"} used for
shortcuts and accelerators that show next to the menu item name when
defined. See
`get_item_accelerator()<class_PopupMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"} for more info on accelerators.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_PopupMenu_theme_color_font_color>`{.interpreted-text
role="ref"}

The default text `Color<class_Color>`{.interpreted-text role="ref"} for
menu items\' names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0.4, 0.4, 0.4, 0.8)`
`🔗<class_PopupMenu_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} used for disabled
menu items\' text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_color_font_hover_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_hover_color**
= `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_PopupMenu_theme_color_font_hover_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} used for the hovered
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_PopupMenu_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_color_font_separator_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_separator_color** = `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_PopupMenu_theme_color_font_separator_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} used for labeled
separators\' text. See
`add_separator()<class_PopupMenu_method_add_separator>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_color_font_separator_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_separator_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_PopupMenu_theme_color_font_separator_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the labeled separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_PopupMenu_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal space between the item\'s elements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_icon_max_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_max_width** = `0`
`🔗<class_PopupMenu_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}

The maximum allowed width of the item\'s icon. This limit is applied on
top of the default size of the icon, but before the value set with
`set_item_icon_max_width()<class_PopupMenu_method_set_item_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_indent}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **indent** = `10`
`🔗<class_PopupMenu_theme_constant_indent>`{.interpreted-text
role="ref"}

Width of the single indentation level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_item_end_padding}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_end_padding** =
`2`
`🔗<class_PopupMenu_theme_constant_item_end_padding>`{.interpreted-text
role="ref"}

Horizontal padding to the right of the items (or left, in RTL layout).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_item_start_padding}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_start_padding** =
`2`
`🔗<class_PopupMenu_theme_constant_item_start_padding>`{.interpreted-text
role="ref"}

Horizontal padding to the left of the items (or right, in RTL layout).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_PopupMenu_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the item text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_PopupMenu_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_separator_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**separator_outline_size** = `0`
`🔗<class_PopupMenu_theme_constant_separator_outline_size>`{.interpreted-text
role="ref"}

The size of the labeled separator text outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_constant_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **v_separation** = `4`
`🔗<class_PopupMenu_theme_constant_v_separation>`{.interpreted-text
role="ref"}

The vertical space between each menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_PopupMenu_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} used for the menu
items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_font_font_separator}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font_separator**
`🔗<class_PopupMenu_theme_font_font_separator>`{.interpreted-text
role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} used for the labeled
separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_font_size_font_separator_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_separator_size**
`🔗<class_PopupMenu_theme_font_size_font_separator_size>`{.interpreted-text
role="ref"}

Font size of the labeled separator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_PopupMenu_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the menu items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_checked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **checked**
`🔗<class_PopupMenu_theme_icon_checked>`{.interpreted-text role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
checked checkbox items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_checked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**checked_disabled**
`🔗<class_PopupMenu_theme_icon_checked_disabled>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
checked checkbox items when they are disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_radio_checked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_checked**
`🔗<class_PopupMenu_theme_icon_radio_checked>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
checked radio button items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_radio_checked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_checked_disabled**
`🔗<class_PopupMenu_theme_icon_radio_checked_disabled>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
checked radio button items when they are disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_radio_unchecked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_unchecked**
`🔗<class_PopupMenu_theme_icon_radio_unchecked>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
unchecked radio button items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_radio_unchecked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_unchecked_disabled**
`🔗<class_PopupMenu_theme_icon_radio_unchecked_disabled>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
unchecked radio button items when they are disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_submenu}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **submenu**
`🔗<class_PopupMenu_theme_icon_submenu>`{.interpreted-text role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
submenu arrow (for left-to-right layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_submenu_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**submenu_mirrored**
`🔗<class_PopupMenu_theme_icon_submenu_mirrored>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
submenu arrow (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_unchecked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **unchecked**
`🔗<class_PopupMenu_theme_icon_unchecked>`{.interpreted-text role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
unchecked checkbox items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_icon_unchecked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**unchecked_disabled**
`🔗<class_PopupMenu_theme_icon_unchecked_disabled>`{.interpreted-text
role="ref"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} icon for the
unchecked checkbox items when they are disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_style_hover}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **hover**
`🔗<class_PopupMenu_theme_style_hover>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} displayed when
the **PopupMenu** item is hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_style_labeled_separator_left}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**labeled_separator_left**
`🔗<class_PopupMenu_theme_style_labeled_separator_left>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the left
side of labeled separator. See
`add_separator()<class_PopupMenu_method_add_separator>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_style_labeled_separator_right}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**labeled_separator_right**
`🔗<class_PopupMenu_theme_style_labeled_separator_right>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the right
side of labeled separator. See
`add_separator()<class_PopupMenu_method_add_separator>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_PopupMenu_theme_style_panel>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
background panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PopupMenu_theme_style_separator}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **separator**
`🔗<class_PopupMenu_theme_style_separator>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for the
separators. See
`add_separator()<class_PopupMenu_method_add_separator>`{.interpreted-text
role="ref"}.
