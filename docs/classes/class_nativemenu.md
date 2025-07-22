github_url
:   hide

# NativeMenu {#class_NativeMenu}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A server interface for OS native menus.

::: rst-class
classref-introduction-group
:::

## Description

**NativeMenu** handles low-level access to the OS native global menu bar
and popup menus.

\*\*Note:\*\* This is low-level API, consider using
`MenuBar<class_MenuBar>`{.interpreted-text role="ref"} with
`MenuBar.prefer_global_menu<class_MenuBar_property_prefer_global_menu>`{.interpreted-text
role="ref"} set to `true`, and
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"} with
`PopupMenu.prefer_native_menu<class_PopupMenu_property_prefer_native_menu>`{.interpreted-text
role="ref"} set to `true`.

To create a menu, use
`create_menu()<class_NativeMenu_method_create_menu>`{.interpreted-text
role="ref"}, add menu items using `add_*_item` methods. To remove a
menu, use
`free_menu()<class_NativeMenu_method_free_menu>`{.interpreted-text
role="ref"}.

    var menu

    func _menu_callback(item_id):
        if item_id == "ITEM_CUT":
            cut()
        elif item_id == "ITEM_COPY":
            copy()
        elif item_id == "ITEM_PASTE":
            paste()

    func _enter_tree():
        # Create new menu and add items:
        menu = NativeMenu.create_menu()
        NativeMenu.add_item(menu, "Cut", _menu_callback, Callable(), "ITEM_CUT")
        NativeMenu.add_item(menu, "Copy", _menu_callback, Callable(), "ITEM_COPY")
        NativeMenu.add_separator(menu)
        NativeMenu.add_item(menu, "Paste", _menu_callback, Callable(), "ITEM_PASTE")

    func _on_button_pressed():
        # Show popup menu at mouse position:
        NativeMenu.popup(menu, DisplayServer.mouse_get_position())

    func _exit_tree():
        # Remove menu when it's no longer needed:
        NativeMenu.free_menu(menu)

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

## Enumerations

:::: {#enum_NativeMenu_Feature}
::: rst-class
classref-enumeration
:::
::::

enum **Feature**: `🔗<enum_NativeMenu_Feature>`{.interpreted-text
role="ref"}

:::: {#class_NativeMenu_constant_FEATURE_GLOBAL_MENU}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_NativeMenu_Feature>`{.interpreted-text role="ref"}
**FEATURE_GLOBAL_MENU** = `0`

**NativeMenu** supports native global main menu.

:::: {#class_NativeMenu_constant_FEATURE_POPUP_MENU}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_NativeMenu_Feature>`{.interpreted-text role="ref"}
**FEATURE_POPUP_MENU** = `1`

**NativeMenu** supports native popup menus.

:::: {#class_NativeMenu_constant_FEATURE_OPEN_CLOSE_CALLBACK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_NativeMenu_Feature>`{.interpreted-text role="ref"}
**FEATURE_OPEN_CLOSE_CALLBACK** = `2`

**NativeMenu** supports menu open and close callbacks.

:::: {#class_NativeMenu_constant_FEATURE_HOVER_CALLBACK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_NativeMenu_Feature>`{.interpreted-text role="ref"}
**FEATURE_HOVER_CALLBACK** = `3`

**NativeMenu** supports menu item hover callback.

:::: {#class_NativeMenu_constant_FEATURE_KEY_CALLBACK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_NativeMenu_Feature>`{.interpreted-text role="ref"}
**FEATURE_KEY_CALLBACK** = `4`

**NativeMenu** supports menu item accelerator/key callback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NativeMenu_SystemMenus}
::: rst-class
classref-enumeration
:::
::::

enum **SystemMenus**:
`🔗<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}

:::: {#class_NativeMenu_constant_INVALID_MENU_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**INVALID_MENU_ID** = `0`

Invalid special system menu ID.

:::: {#class_NativeMenu_constant_MAIN_MENU_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**MAIN_MENU_ID** = `1`

Global main menu ID.

:::: {#class_NativeMenu_constant_APPLICATION_MENU_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**APPLICATION_MENU_ID** = `2`

Application (first menu after \"Apple\" menu on macOS) menu ID.

:::: {#class_NativeMenu_constant_WINDOW_MENU_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**WINDOW_MENU_ID** = `3`

\"Window\" menu ID (on macOS this menu includes standard window control
items and a list of open windows).

:::: {#class_NativeMenu_constant_HELP_MENU_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**HELP_MENU_ID** = `4`

\"Help\" menu ID (on macOS this menu includes help search bar).

:::: {#class_NativeMenu_constant_DOCK_MENU_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text role="ref"}
**DOCK_MENU_ID** = `5`

Dock icon right-click menu ID (on macOS this menu include standard
application control items and a list of open windows).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NativeMenu_method_add_check_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_check_item**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_NativeMenu_method_add_check_item>`{.interpreted-text
role="ref"}

Adds a new checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_icon_check_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**add_icon_check_item**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, label: `String<class_String>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable(), key_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
tag: `Variant<class_Variant>`{.interpreted-text role="ref"} = null,
accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
= 0, index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_NativeMenu_method_add_icon_check_item>`{.interpreted-text
role="ref"}

Adds a new checkable item with text `label` and icon `icon` to the
global menu `rid`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_icon_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_icon_item**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_NativeMenu_method_add_icon_item>`{.interpreted-text
role="ref"}

Adds a new item with text `label` and icon `icon` to the global menu
`rid`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_icon_radio_check_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**add_icon_radio_check_item**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, label: `String<class_String>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable(), key_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
tag: `Variant<class_Variant>`{.interpreted-text role="ref"} = null,
accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
= 0, index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_NativeMenu_method_add_icon_radio_check_item>`{.interpreted-text
role="ref"}

Adds a new radio-checkable item with text `label` and icon `icon` to the
global menu `rid`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* Radio-checkable items just display a checkmark, but don\'t
have any built-in checking behavior and must be checked/unchecked
manually. See
`set_item_checked()<class_NativeMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_item**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_NativeMenu_method_add_item>`{.interpreted-text role="ref"}

Adds a new item with text `label` to the global menu `rid`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_multistate_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**add_multistate_item**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, label: `String<class_String>`{.interpreted-text
role="ref"}, max_states: `int<class_int>`{.interpreted-text role="ref"},
default_state: `int<class_int>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_NativeMenu_method_add_multistate_item>`{.interpreted-text
role="ref"}

Adds a new item with text `label` to the global menu `rid`.

Contrarily to normal binary items, multistate items can have more than
two states, as defined by `max_states`. Each press or activate of the
item will increase the state by one. The default value is defined by
`default_state`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* By default, there\'s no indication of the current item
state, it should be changed manually.

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_radio_check_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**add_radio_check_item**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, label: `String<class_String>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable(), key_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
tag: `Variant<class_Variant>`{.interpreted-text role="ref"} = null,
accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
= 0, index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_NativeMenu_method_add_radio_check_item>`{.interpreted-text
role="ref"}

Adds a new radio-checkable item with text `label` to the global menu
`rid`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* Radio-checkable items just display a checkmark, but don\'t
have any built-in checking behavior and must be checked/unchecked
manually. See
`set_item_checked()<class_NativeMenu_method_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* On Windows, `accelerator` and `key_callback` are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_separator}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_separator**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_NativeMenu_method_add_separator>`{.interpreted-text
role="ref"}

Adds a separator between items to the global menu `rid`. Separators also
occupy an index.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_add_submenu_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_submenu_item**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, submenu_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, tag:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null, index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_NativeMenu_method_add_submenu_item>`{.interpreted-text
role="ref"}

Adds an item that will act as a submenu of the global menu `rid`. The
`submenu_rid` argument is the RID of the global menu that will be shown
when the item is clicked.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_clear>`{.interpreted-text role="ref"}

Removes all items from the global menu `rid`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_create_menu}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **create_menu**()
`🔗<class_NativeMenu_method_create_menu>`{.interpreted-text role="ref"}

Creates a new global menu object.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_find_item_index_with_submenu}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**find_item_index_with_submenu**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, submenu_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_find_item_index_with_submenu>`{.interpreted-text
role="ref"}

Returns the index of the item with the submenu specified by
`submenu_rid`. Indices are automatically assigned to each item by the
engine, and cannot be set manually.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_find_item_index_with_tag}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**find_item_index_with_tag**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, tag: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_find_item_index_with_tag>`{.interpreted-text
role="ref"}

Returns the index of the item with the specified `tag`. Indices are
automatically assigned to each item by the engine, and cannot be set
manually.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_find_item_index_with_text}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**find_item_index_with_text**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_find_item_index_with_text>`{.interpreted-text
role="ref"}

Returns the index of the item with the specified `text`. Indices are
automatically assigned to each item by the engine, and cannot be set
manually.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_free_menu}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_menu**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_free_menu>`{.interpreted-text role="ref"}

Frees a global menu object created by this **NativeMenu**.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_accelerator}
::: rst-class
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**get_item_accelerator**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_accelerator>`{.interpreted-text
role="ref"}

Returns the accelerator of the item at index `idx`. Accelerators are
special combinations of keys that activate the item, no matter which
control is focused.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_callback}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**get_item_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_callback>`{.interpreted-text
role="ref"}

Returns the callback of the item at index `idx`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_item_count**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_count>`{.interpreted-text
role="ref"}

Returns number of items in the global menu `rid`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_item_icon**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_icon>`{.interpreted-text
role="ref"}

Returns the icon of the item at index `idx`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_indentation_level}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_indentation_level**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_indentation_level>`{.interpreted-text
role="ref"}

Returns the horizontal offset of the item at the given `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_key_callback}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**get_item_key_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_key_callback>`{.interpreted-text
role="ref"}

Returns the callback of the item accelerator at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_max_states}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_max_states**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_max_states>`{.interpreted-text
role="ref"}

Returns number of states of a multistate item. See
`add_multistate_item()<class_NativeMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_state}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_item_state**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_state>`{.interpreted-text
role="ref"}

Returns the state of a multistate item. See
`add_multistate_item()<class_NativeMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_submenu}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_item_submenu**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_submenu>`{.interpreted-text
role="ref"}

Returns the submenu ID of the item at index `idx`. See
`add_submenu_item()<class_NativeMenu_method_add_submenu_item>`{.interpreted-text
role="ref"} for more info on how to add a submenu.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_tag}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_item_tag**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_tag>`{.interpreted-text role="ref"}

Returns the metadata of the specified item, which might be of any type.
You can set it with
`set_item_tag()<class_NativeMenu_method_set_item_tag>`{.interpreted-text
role="ref"}, which provides a simple way of assigning context data to
items.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_text**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_text>`{.interpreted-text
role="ref"}

Returns the text of the item at index `idx`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_item_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_tooltip**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_item_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip associated with the specified index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_minimum_width}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_minimum_width**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_minimum_width>`{.interpreted-text
role="ref"}

Returns global menu minimum width.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_popup_close_callback}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**get_popup_close_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_popup_close_callback>`{.interpreted-text
role="ref"}

Returns global menu close callback.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_popup_open_callback}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**get_popup_open_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_popup_open_callback>`{.interpreted-text
role="ref"}

Returns global menu open callback.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NativeMenu_method_get_size>`{.interpreted-text
role="ref"}

Returns global menu size.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_system_menu}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_system_menu**(menu_id:
`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_system_menu>`{.interpreted-text
role="ref"}

Returns RID of a special system menu.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_get_system_menu_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_system_menu_name**(menu_id:
`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_get_system_menu_name>`{.interpreted-text
role="ref"}

Returns readable name of a special system menu.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_has_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_feature**(feature:
`Feature<enum_NativeMenu_Feature>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NativeMenu_method_has_feature>`{.interpreted-text
role="ref"}

Returns `true` if the specified `feature` is supported by the current
**NativeMenu**, `false` otherwise.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_has_menu}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_menu**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NativeMenu_method_has_menu>`{.interpreted-text
role="ref"}

Returns `true` if `rid` is valid global menu.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_has_system_menu}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_system_menu**(menu_id:
`SystemMenus<enum_NativeMenu_SystemMenus>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_has_system_menu>`{.interpreted-text
role="ref"}

Returns `true` if a special system menu is supported.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_item_checkable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_checkable**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_is_item_checkable>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` is checkable in some way, i.e.
if it has a checkbox or radio button.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_item_checked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_checked**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_is_item_checked>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` is checked.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_item_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_disabled**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_is_item_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` is disabled. When it is
disabled it can\'t be selected, or its action invoked.

See
`set_item_disabled()<class_NativeMenu_method_set_item_disabled>`{.interpreted-text
role="ref"} for more info on how to disable an item.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_item_hidden}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_item_hidden**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_is_item_hidden>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` is hidden.

See
`set_item_hidden()<class_NativeMenu_method_set_item_hidden>`{.interpreted-text
role="ref"} for more info on how to hide an item.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_item_radio_checkable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_radio_checkable**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_is_item_radio_checkable>`{.interpreted-text
role="ref"}

Returns `true` if the item at index `idx` has radio button-style
checkability.

\*\*Note:\*\* This is purely cosmetic; you must add the logic for
checking/unchecking items in radio groups.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_opened}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_opened**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NativeMenu_method_is_opened>`{.interpreted-text
role="ref"}

Returns `true` if the menu is currently opened.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_is_system_menu}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_system_menu**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NativeMenu_method_is_system_menu>`{.interpreted-text
role="ref"}

Return `true` is global menu is a special system menu.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_popup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **popup**(rid:
`RID<class_RID>`{.interpreted-text role="ref"}, position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_popup>`{.interpreted-text role="ref"}

Shows the global menu at `position` in the screen coordinates.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_remove_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_item**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_remove_item>`{.interpreted-text role="ref"}

Removes the item at index `idx` from the global menu `rid`.

\*\*Note:\*\* The indices of items after the removed item will be
shifted by one.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_interface_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_interface_direction**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, is_rtl: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_interface_direction>`{.interpreted-text
role="ref"}

Sets the menu text layout direction from right-to-left if `is_rtl` is
`true`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_accelerator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_accelerator**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
keycode: `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_accelerator>`{.interpreted-text
role="ref"}

Sets the accelerator of the item at index `idx`. `keycode` can be a
single `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}, or a
combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
callback: `Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_callback>`{.interpreted-text
role="ref"}

Sets the callback of the item at index `idx`. Callback is emitted when
an item is pressed.

\*\*Note:\*\* The `callback` Callable needs to accept exactly one
Variant parameter, the parameter passed to the Callable will be the
value passed to the `tag` parameter when the menu item was created.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_checkable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_checkable**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
checkable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_checkable>`{.interpreted-text
role="ref"}

Sets whether the item at index `idx` has a checkbox. If `false`, sets
the type of the item to plain text.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_checked}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_checked**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
checked: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_checked>`{.interpreted-text
role="ref"}

Sets the checkstate status of the item at index `idx`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_disabled**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_disabled>`{.interpreted-text
role="ref"}

Enables/disables the item at index `idx`. When it is disabled, it can\'t
be selected and its action can\'t be invoked.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_hidden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_hidden**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"}, hidden:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_hidden>`{.interpreted-text
role="ref"}

Hides/shows the item at index `idx`. When it is hidden, an item does not
appear in a menu and its action cannot be invoked.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_hover_callbacks}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_hover_callbacks**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
callback: `Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_hover_callbacks>`{.interpreted-text
role="ref"}

Sets the callback of the item at index `idx`. The callback is emitted
when an item is hovered.

\*\*Note:\*\* The `callback` Callable needs to accept exactly one
Variant parameter, the parameter passed to the Callable will be the
value passed to the `tag` parameter when the menu item was created.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_icon>`{.interpreted-text
role="ref"}

Replaces the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
icon of the specified `idx`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

\*\*Note:\*\* This method is not supported by macOS Dock menu items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_indentation_level}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_indentation_level**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"}, level:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_indentation_level>`{.interpreted-text
role="ref"}

Sets the horizontal offset of the item at the given `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_key_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_key_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_key_callback>`{.interpreted-text
role="ref"}

Sets the callback of the item at index `idx`. Callback is emitted when
its accelerator is activated.

\*\*Note:\*\* The `key_callback` Callable needs to accept exactly one
Variant parameter, the parameter passed to the Callable will be the
value passed to the `tag` parameter when the menu item was created.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_max_states}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_max_states**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
max_states: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_max_states>`{.interpreted-text
role="ref"}

Sets number of state of a multistate item. See
`add_multistate_item()<class_NativeMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_radio_checkable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_radio_checkable**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
checkable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_radio_checkable>`{.interpreted-text
role="ref"}

Sets the type of the item at the specified index `idx` to radio button.
If `false`, sets the type of the item to plain text.

\*\*Note:\*\* This is purely cosmetic; you must add the logic for
checking/unchecking items in radio groups.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_state**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"}, state:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_state>`{.interpreted-text
role="ref"}

Sets the state of a multistate item. See
`add_multistate_item()<class_NativeMenu_method_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_submenu}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_submenu**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
submenu_rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_submenu>`{.interpreted-text
role="ref"}

Sets the submenu RID of the item at index `idx`. The submenu is a global
menu that would be shown when the item is clicked.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_tag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_tag**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"}, tag:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_tag>`{.interpreted-text role="ref"}

Sets the metadata of an item, which may be of any type. You can later
get it with
`get_item_tag()<class_NativeMenu_method_get_item_tag>`{.interpreted-text
role="ref"}, which provides a simple way of assigning context data to
items.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_text**(rid: `RID<class_RID>`{.interpreted-text role="ref"},
idx: `int<class_int>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_text>`{.interpreted-text
role="ref"}

Sets the text of the item at index `idx`.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_item_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_tooltip**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
tooltip: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_item_tooltip>`{.interpreted-text
role="ref"}

Sets the `String<class_String>`{.interpreted-text role="ref"} tooltip of
the item at the specified index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_minimum_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_minimum_width**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, width: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NativeMenu_method_set_minimum_width>`{.interpreted-text
role="ref"}

Sets the minimum width of the global menu.

\*\*Note:\*\* This method is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_popup_close_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_popup_close_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_NativeMenu_method_set_popup_close_callback>`{.interpreted-text
role="ref"}

Registers callable to emit when the menu is about to show.

\*\*Note:\*\* The OS can simulate menu opening to track menu item
changes and global shortcuts, in which case the corresponding close
callback is not triggered. Use
`is_opened()<class_NativeMenu_method_is_opened>`{.interpreted-text
role="ref"} to check if the menu is currently opened.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NativeMenu_method_set_popup_open_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_popup_open_callback**(rid: `RID<class_RID>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_NativeMenu_method_set_popup_open_callback>`{.interpreted-text
role="ref"}

Registers callable to emit after the menu is closed.

\*\*Note:\*\* This method is implemented only on macOS.
