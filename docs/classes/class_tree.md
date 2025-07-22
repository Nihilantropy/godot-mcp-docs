github_url
:   hide

# Tree {#class_Tree}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control used to show a set of internal
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}s in a
hierarchical structure.

::: rst-class
classref-introduction-group
:::

## Description

A control used to show a set of internal
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}s in a
hierarchical structure. The tree items can be selected, expanded and
collapsed. The tree can have multiple columns with custom controls like
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}s, buttons and
popups. It can be useful for structured displays and interactions.

Trees are built via code, using
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} objects to
create the structure. They have a single root, but multiple roots can be
simulated with
`hide_root<class_Tree_property_hide_root>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var tree = Tree.new() var root = tree.create_item() tree.hide_root =
    true var child1 = tree.create_item(root) var child2 =
    tree.create_item(root) var subchild1 = tree.create_item(child1)
    subchild1.set_text(0, \"Subchild1\")
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var tree = new Tree(); TreeItem
root = tree.CreateItem(); tree.HideRoot = true; TreeItem child1 =
tree.CreateItem(root); TreeItem child2 = tree.CreateItem(root); TreeItem
subchild1 = tree.CreateItem(child1); subchild1.SetText(0,
\"Subchild1\"); }
:::
:::::

To iterate over all the `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"} objects in a **Tree** object, use
`TreeItem.get_next()<class_TreeItem_method_get_next>`{.interpreted-text
role="ref"} and
`TreeItem.get_first_child()<class_TreeItem_method_get_first_child>`{.interpreted-text
role="ref"} after getting the root through
`get_root()<class_Tree_method_get_root>`{.interpreted-text role="ref"}.
You can use `Object.free()<class_Object_method_free>`{.interpreted-text
role="ref"} on a `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"} to remove it from the **Tree**.

\*\*Incremental search:\*\* Like
`ItemList<class_ItemList>`{.interpreted-text role="ref"} and
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}, **Tree**
supports searching within the list while the control is focused. Press a
key that matches the first letter of an item\'s name to select the first
item starting with the given letter. After that point, there are two
ways to perform incremental search: 1) Press the same key again before
the timeout duration to select the next item starting with the same
letter. 2) Press letter keys that match the rest of the word before the
timeout duration to match to select the item in question directly. Both
of these actions will be reset to the beginning of the list if the
timeout duration has passed since the last keystroke was registered. You
can adjust the timeout duration by changing
`ProjectSettings.gui/timers/incremental_search_max_interval_msec<class_ProjectSettings_property_gui/timers/incremental_search_max_interval_msec>`{.interpreted-text
role="ref"}.

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

:::: {#class_Tree_signal_button_clicked}
::: rst-class
classref-signal
:::
::::

**button_clicked**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"}, mouse_button_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_button_clicked>`{.interpreted-text role="ref"}

Emitted when a button on the tree was pressed (see
`TreeItem.add_button()<class_TreeItem_method_add_button>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_cell_selected}
::: rst-class
classref-signal
:::
::::

**cell_selected**()
`🔗<class_Tree_signal_cell_selected>`{.interpreted-text role="ref"}

Emitted when a cell is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_check_propagated_to_item}
::: rst-class
classref-signal
:::
::::

**check_propagated_to_item**(item:
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_check_propagated_to_item>`{.interpreted-text
role="ref"}

Emitted when
`TreeItem.propagate_check()<class_TreeItem_method_propagate_check>`{.interpreted-text
role="ref"} is called. Connect to this signal to process the items that
are affected when
`TreeItem.propagate_check()<class_TreeItem_method_propagate_check>`{.interpreted-text
role="ref"} is invoked. The order that the items affected will be
processed is as follows: the item that invoked the method, children of
that item, and finally parents of that item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_column_title_clicked}
::: rst-class
classref-signal
:::
::::

**column_title_clicked**(column: `int<class_int>`{.interpreted-text
role="ref"}, mouse_button_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Tree_signal_column_title_clicked>`{.interpreted-text
role="ref"}

Emitted when a column\'s title is clicked with either
`@GlobalScope.MOUSE_BUTTON_LEFT<class_@GlobalScope_constant_MOUSE_BUTTON_LEFT>`{.interpreted-text
role="ref"} or
`@GlobalScope.MOUSE_BUTTON_RIGHT<class_@GlobalScope_constant_MOUSE_BUTTON_RIGHT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_custom_item_clicked}
::: rst-class
classref-signal
:::
::::

**custom_item_clicked**(mouse_button_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_custom_item_clicked>`{.interpreted-text
role="ref"}

Emitted when an item with
`TreeItem.CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} is clicked with a mouse button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_custom_popup_edited}
::: rst-class
classref-signal
:::
::::

**custom_popup_edited**(arrow_clicked:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_custom_popup_edited>`{.interpreted-text
role="ref"}

Emitted when a cell with the
`TreeItem.CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} is clicked to be edited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_empty_clicked}
::: rst-class
classref-signal
:::
::::

**empty_clicked**(click_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
mouse_button_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_empty_clicked>`{.interpreted-text role="ref"}

Emitted when a mouse button is clicked in the empty space of the tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_item_activated}
::: rst-class
classref-signal
:::
::::

**item_activated**()
`🔗<class_Tree_signal_item_activated>`{.interpreted-text role="ref"}

Emitted when an item is double-clicked, or selected with a `ui_accept`
input event (e.g. using `Enter`{.interpreted-text role="kbd"} or
`Space`{.interpreted-text role="kbd"} on the keyboard).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_item_collapsed}
::: rst-class
classref-signal
:::
::::

**item_collapsed**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}) `🔗<class_Tree_signal_item_collapsed>`{.interpreted-text
role="ref"}

Emitted when an item is collapsed by a click on the folding arrow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_item_edited}
::: rst-class
classref-signal
:::
::::

**item_edited**() `🔗<class_Tree_signal_item_edited>`{.interpreted-text
role="ref"}

Emitted when an item is edited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_item_icon_double_clicked}
::: rst-class
classref-signal
:::
::::

**item_icon_double_clicked**()
`🔗<class_Tree_signal_item_icon_double_clicked>`{.interpreted-text
role="ref"}

Emitted when an item\'s icon is double-clicked. For a signal that emits
when any part of the item is double-clicked, see
`item_activated<class_Tree_signal_item_activated>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_item_mouse_selected}
::: rst-class
classref-signal
:::
::::

**item_mouse_selected**(mouse_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
mouse_button_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_item_mouse_selected>`{.interpreted-text
role="ref"}

Emitted when an item is selected with a mouse button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_item_selected}
::: rst-class
classref-signal
:::
::::

**item_selected**()
`🔗<class_Tree_signal_item_selected>`{.interpreted-text role="ref"}

Emitted when an item is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_multi_selected}
::: rst-class
classref-signal
:::
::::

**multi_selected**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"},
selected: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Tree_signal_multi_selected>`{.interpreted-text role="ref"}

Emitted instead of
`item_selected<class_Tree_signal_item_selected>`{.interpreted-text
role="ref"} if
`select_mode<class_Tree_property_select_mode>`{.interpreted-text
role="ref"} is set to
`SELECT_MULTI<class_Tree_constant_SELECT_MULTI>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_signal_nothing_selected}
::: rst-class
classref-signal
:::
::::

**nothing_selected**()
`🔗<class_Tree_signal_nothing_selected>`{.interpreted-text role="ref"}

Emitted when a left mouse button click does not select any item.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Tree_SelectMode}
::: rst-class
classref-enumeration
:::
::::

enum **SelectMode**: `🔗<enum_Tree_SelectMode>`{.interpreted-text
role="ref"}

:::: {#class_Tree_constant_SELECT_SINGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"}
**SELECT_SINGLE** = `0`

Allows selection of a single cell at a time. From the perspective of
items, only a single item is allowed to be selected. And there is only
one column selected in the selected item.

The focus cursor is always hidden in this mode, but it is positioned at
the current selection, making the currently selected item the currently
focused item.

:::: {#class_Tree_constant_SELECT_ROW}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"}
**SELECT_ROW** = `1`

Allows selection of a single row at a time. From the perspective of
items, only a single items is allowed to be selected. And all the
columns are selected in the selected item.

The focus cursor is always hidden in this mode, but it is positioned at
the first column of the current selection, making the currently selected
item the currently focused item.

:::: {#class_Tree_constant_SELECT_MULTI}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"}
**SELECT_MULTI** = `2`

Allows selection of multiple cells at the same time. From the
perspective of items, multiple items are allowed to be selected. And
there can be multiple columns selected in each selected item.

The focus cursor is visible in this mode, the item or column under the
cursor is not necessarily selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Tree_DropModeFlags}
::: rst-class
classref-enumeration
:::
::::

enum **DropModeFlags**: `🔗<enum_Tree_DropModeFlags>`{.interpreted-text
role="ref"}

:::: {#class_Tree_constant_DROP_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DropModeFlags<enum_Tree_DropModeFlags>`{.interpreted-text role="ref"}
**DROP_MODE_DISABLED** = `0`

Disables all drop sections, but still allows to detect the \"on item\"
drop section by
`get_drop_section_at_position()<class_Tree_method_get_drop_section_at_position>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This is the default flag, it has no effect when combined
with other flags.

:::: {#class_Tree_constant_DROP_MODE_ON_ITEM}
::: rst-class
classref-enumeration-constant
:::
::::

`DropModeFlags<enum_Tree_DropModeFlags>`{.interpreted-text role="ref"}
**DROP_MODE_ON_ITEM** = `1`

Enables the \"on item\" drop section. This drop section covers the
entire item.

When combined with
`DROP_MODE_INBETWEEN<class_Tree_constant_DROP_MODE_INBETWEEN>`{.interpreted-text
role="ref"}, this drop section halves the height and stays centered
vertically.

:::: {#class_Tree_constant_DROP_MODE_INBETWEEN}
::: rst-class
classref-enumeration-constant
:::
::::

`DropModeFlags<enum_Tree_DropModeFlags>`{.interpreted-text role="ref"}
**DROP_MODE_INBETWEEN** = `2`

Enables \"above item\" and \"below item\" drop sections. The \"above
item\" drop section covers the top half of the item, and the \"below
item\" drop section covers the bottom half.

When combined with
`DROP_MODE_ON_ITEM<class_Tree_constant_DROP_MODE_ON_ITEM>`{.interpreted-text
role="ref"}, these drop sections halves the height and stays on top /
bottom accordingly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Tree_property_allow_reselect}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_reselect** =
`false` `🔗<class_Tree_property_allow_reselect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_reselect**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_reselect**()

If `true`, the currently selected cell may be selected again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_allow_rmb_select}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_rmb_select** =
`false` `🔗<class_Tree_property_allow_rmb_select>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_rmb_select**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_rmb_select**()

If `true`, a right mouse button click can select items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_allow_search}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_search** =
`true` `🔗<class_Tree_property_allow_search>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_search**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_search**()

If `true`, allows navigating the **Tree** with letter keys through
incremental search.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_auto_tooltip}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_tooltip** =
`true` `🔗<class_Tree_property_auto_tooltip>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_tooltip**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_tooltip_enabled**()

If `true`, tree items with no tooltip assigned display their text as
their tooltip. See also
`TreeItem.get_tooltip_text()<class_TreeItem_method_get_tooltip_text>`{.interpreted-text
role="ref"} and
`TreeItem.get_button_tooltip_text()<class_TreeItem_method_get_button_tooltip_text>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_column_titles_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**column_titles_visible** = `false`
`🔗<class_Tree_property_column_titles_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_column_titles_visible**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_column_titles_visible**()

If `true`, column titles are visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_columns}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **columns** = `1`
`🔗<class_Tree_property_columns>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_columns**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_columns**()

The number of columns.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_drop_mode_flags}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **drop_mode_flags** = `0`
`🔗<class_Tree_property_drop_mode_flags>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drop_mode_flags**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_drop_mode_flags**()

The drop mode as an OR combination of flags. See
`DropModeFlags<enum_Tree_DropModeFlags>`{.interpreted-text role="ref"}
constants. Once dropping is done, reverts to
`DROP_MODE_DISABLED<class_Tree_constant_DROP_MODE_DISABLED>`{.interpreted-text
role="ref"}. Setting this during
`Control._can_drop_data()<class_Control_private_method__can_drop_data>`{.interpreted-text
role="ref"} is recommended.

This controls the drop sections, i.e. the decision and drawing of
possible drop locations based on the mouse position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_enable_recursive_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**enable_recursive_folding** = `true`
`🔗<class_Tree_property_enable_recursive_folding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_recursive_folding**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_recursive_folding_enabled**()

If `true`, recursive folding is enabled for this **Tree**. Holding down
`Shift`{.interpreted-text role="kbd"} while clicking the fold arrow or
using `ui_right`/`ui_left` shortcuts collapses or uncollapses the
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} and all its
descendants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_hide_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hide_folding** =
`false` `🔗<class_Tree_property_hide_folding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_folding**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_folding_hidden**()

If `true`, the folding arrow is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_hide_root}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hide_root** = `false`
`🔗<class_Tree_property_hide_root>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_root**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_root_hidden**()

If `true`, the tree\'s root is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_scroll_horizontal_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_horizontal_enabled** = `true`
`🔗<class_Tree_property_scroll_horizontal_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_scroll_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_h_scroll_enabled**()

If `true`, enables horizontal scrolling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_scroll_vertical_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_vertical_enabled** = `true`
`🔗<class_Tree_property_scroll_vertical_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_scroll_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_v_scroll_enabled**()

If `true`, enables vertical scrolling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_property_select_mode}
::: rst-class
classref-property
:::
::::

`SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"}
**select_mode** = `0`
`🔗<class_Tree_property_select_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_select_mode**(value:
  `SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"})
- `SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"}
  **get_select_mode**()

Allows single or multiple selection. See the
`SelectMode<enum_Tree_SelectMode>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Tree_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_Tree_method_clear>`{.interpreted-text role="ref"}

Clears the tree. This removes all items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_create_item}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**create_item**(parent: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"} = null, index: `int<class_int>`{.interpreted-text
role="ref"} = -1) `🔗<class_Tree_method_create_item>`{.interpreted-text
role="ref"}

Creates an item in the tree and adds it as a child of `parent`, which
can be either a valid `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"} or `null`.

If `parent` is `null`, the root item will be the parent, or the new item
will be the root itself if the tree is empty.

The new item will be the `index`-th child of parent, or it will be the
last child if there are not enough siblings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_deselect_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**deselect_all**()
`🔗<class_Tree_method_deselect_all>`{.interpreted-text role="ref"}

Deselects all tree items (rows and columns). In
`SELECT_MULTI<class_Tree_constant_SELECT_MULTI>`{.interpreted-text
role="ref"} mode also removes selection cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_edit_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**edit_selected**(force_edit: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Tree_method_edit_selected>`{.interpreted-text role="ref"}

Edits the selected tree item as if it was clicked.

Either the item must be set editable with
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"} or `force_edit` must be `true`.

Returns `true` if the item could be edited. Fails if no item is
selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_ensure_cursor_is_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**ensure_cursor_is_visible**()
`🔗<class_Tree_method_ensure_cursor_is_visible>`{.interpreted-text
role="ref"}

Makes the currently focused cell visible.

This will scroll the tree if necessary. In
`SELECT_ROW<class_Tree_constant_SELECT_ROW>`{.interpreted-text
role="ref"} mode, this will not do horizontal scrolling, as all the
cells in the selected row is focused logically.

\*\*Note:\*\* Despite the name of this method, the focus cursor itself
is only visible in
`SELECT_MULTI<class_Tree_constant_SELECT_MULTI>`{.interpreted-text
role="ref"} mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_button_id_at_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_button_id_at_position**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_button_id_at_position>`{.interpreted-text
role="ref"}

Returns the button ID at `position`, or -1 if no button is there.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_at_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_column_at_position**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_column_at_position>`{.interpreted-text
role="ref"}

Returns the column index at `position`, or -1 if no item is there.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_expand_ratio}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_column_expand_ratio**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_column_expand_ratio>`{.interpreted-text
role="ref"}

Returns the expand ratio assigned to the column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_title}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_column_title**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_column_title>`{.interpreted-text
role="ref"}

Returns the column\'s title.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_title_alignment}
::: rst-class
classref-method
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **get_column_title_alignment**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_column_title_alignment>`{.interpreted-text
role="ref"}

Returns the column title alignment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_title_direction}
::: rst-class
classref-method
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **get_column_title_direction**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_column_title_direction>`{.interpreted-text
role="ref"}

Returns column title base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_title_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_column_title_language**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_column_title_language>`{.interpreted-text
role="ref"}

Returns column title language code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_column_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_column_width**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_column_width>`{.interpreted-text
role="ref"}

Returns the column\'s width in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_custom_popup_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_custom_popup_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_custom_popup_rect>`{.interpreted-text
role="ref"}

Returns the rectangle for custom popups. Helper to create custom cell
controls that display a popup. See
`TreeItem.set_cell_mode()<class_TreeItem_method_set_cell_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_drop_section_at_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_drop_section_at_position**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_drop_section_at_position>`{.interpreted-text
role="ref"}

Returns the drop section at `position`, or -100 if no item is there.

Values -1, 0, or 1 will be returned for the \"above item\", \"on item\",
and \"below item\" drop sections, respectively. See
`DropModeFlags<enum_Tree_DropModeFlags>`{.interpreted-text role="ref"}
for a description of each drop section.

To get the item which the returned drop section is relative to, use
`get_item_at_position()<class_Tree_method_get_item_at_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_edited}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_edited**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_edited>`{.interpreted-text
role="ref"}

Returns the currently edited item. Can be used with
`item_edited<class_Tree_signal_item_edited>`{.interpreted-text
role="ref"} to get the item that was modified.

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   \$Tree.item_edited.connect(on_Tree_item_edited)

func on_Tree_item_edited():

:   print(\$Tree.get_edited()) \# This item just got edited (e.g.
    checked).
:::

::: code-tab
csharp

public override void [Ready]{#ready}() {
GetNode\<Tree\>(\"Tree\").ItemEdited += OnTreeItemEdited; }

public void OnTreeItemEdited() {
GD.Print(GetNode\<Tree\>(\"Tree\").GetEdited()); // This item just got
edited (e.g. checked). }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_edited_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_edited_column**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_edited_column>`{.interpreted-text
role="ref"}

Returns the column for the currently edited item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_item_area_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_item_area_rect**(item:
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"} = -1, button_index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_item_area_rect>`{.interpreted-text role="ref"}

Returns the rectangle area for the specified
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}. If `column` is
specified, only get the position and size of that column, otherwise get
the rectangle containing all columns. If a button index is specified,
the rectangle of that button will be returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_item_at_position}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_item_at_position**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_item_at_position>`{.interpreted-text
role="ref"}

Returns the tree item at the specified position (relative to the tree
origin position).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_next_selected}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_next_selected**(from: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}) `🔗<class_Tree_method_get_next_selected>`{.interpreted-text
role="ref"}

Returns the next selected `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"} after the given one, or `null` if the end is reached.

If `from` is `null`, this returns the first selected item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_pressed_button}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_pressed_button**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_pressed_button>`{.interpreted-text role="ref"}

Returns the last pressed button\'s index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_root}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} **get_root**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_root>`{.interpreted-text
role="ref"}

Returns the tree\'s root item, or `null` if the tree is empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_scroll}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_scroll**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_scroll>`{.interpreted-text
role="ref"}

Returns the current scrolling position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_selected}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_selected**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tree_method_get_selected>`{.interpreted-text
role="ref"}

Returns the currently focused item, or `null` if no item is focused.

In `SELECT_ROW<class_Tree_constant_SELECT_ROW>`{.interpreted-text
role="ref"} and
`SELECT_SINGLE<class_Tree_constant_SELECT_SINGLE>`{.interpreted-text
role="ref"} modes, the focused item is same as the selected item. In
`SELECT_MULTI<class_Tree_constant_SELECT_MULTI>`{.interpreted-text
role="ref"} mode, the focused item is the item under the focus cursor,
not necessarily selected.

To get the currently selected item(s), use
`get_next_selected()<class_Tree_method_get_next_selected>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_get_selected_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_selected_column**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_get_selected_column>`{.interpreted-text
role="ref"}

Returns the currently focused column, or -1 if no column is focused.

In `SELECT_SINGLE<class_Tree_constant_SELECT_SINGLE>`{.interpreted-text
role="ref"} mode, the focused column is the selected column. In
`SELECT_ROW<class_Tree_constant_SELECT_ROW>`{.interpreted-text
role="ref"} mode, the focused column is always 0 if any item is
selected. In
`SELECT_MULTI<class_Tree_constant_SELECT_MULTI>`{.interpreted-text
role="ref"} mode, the focused column is the column under the focus
cursor, and there are not necessarily any column selected.

To tell whether a column of an item is selected, use
`TreeItem.is_selected()<class_TreeItem_method_is_selected>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_is_column_clipping_content}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_column_clipping_content**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_is_column_clipping_content>`{.interpreted-text
role="ref"}

Returns `true` if the column has enabled clipping (see
`set_column_clip_content()<class_Tree_method_set_column_clip_content>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_is_column_expanding}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_column_expanding**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tree_method_is_column_expanding>`{.interpreted-text
role="ref"}

Returns `true` if the column has enabled expanding (see
`set_column_expand()<class_Tree_method_set_column_expand>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_scroll_to_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scroll_to_item**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}, center_on_item: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Tree_method_scroll_to_item>`{.interpreted-text role="ref"}

Causes the **Tree** to jump to the specified
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_clip_content}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_clip_content**(column: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Tree_method_set_column_clip_content>`{.interpreted-text
role="ref"}

Allows to enable clipping for column\'s content, making the content size
ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_custom_minimum_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_custom_minimum_width**(column:
`int<class_int>`{.interpreted-text role="ref"}, min_width:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_method_set_column_custom_minimum_width>`{.interpreted-text
role="ref"}

Overrides the calculated minimum width of a column. It can be set to `0`
to restore the default behavior. Columns that have the \"Expand\" flag
will use their \"min_width\" in a similar fashion to
`Control.size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_expand}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_expand**(column: `int<class_int>`{.interpreted-text
role="ref"}, expand: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Tree_method_set_column_expand>`{.interpreted-text role="ref"}

If `true`, the column will have the \"Expand\" flag of
`Control<class_Control>`{.interpreted-text role="ref"}. Columns that
have the \"Expand\" flag will use their expand ratio in a similar
fashion to
`Control.size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>`{.interpreted-text
role="ref"} (see
`set_column_expand_ratio()<class_Tree_method_set_column_expand_ratio>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_expand_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_expand_ratio**(column: `int<class_int>`{.interpreted-text
role="ref"}, ratio: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_method_set_column_expand_ratio>`{.interpreted-text
role="ref"}

Sets the relative expand ratio for a column. See
`set_column_expand()<class_Tree_method_set_column_expand>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_title}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_title**(column: `int<class_int>`{.interpreted-text
role="ref"}, title: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_Tree_method_set_column_title>`{.interpreted-text
role="ref"}

Sets the title of a column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_title_alignment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_title_alignment**(column:
`int<class_int>`{.interpreted-text role="ref"}, title_alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"})
`🔗<class_Tree_method_set_column_title_alignment>`{.interpreted-text
role="ref"}

Sets the column title alignment. Note that
`@GlobalScope.HORIZONTAL_ALIGNMENT_FILL<class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_FILL>`{.interpreted-text
role="ref"} is not supported for column titles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_title_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_title_direction**(column:
`int<class_int>`{.interpreted-text role="ref"}, direction:
`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"})
`🔗<class_Tree_method_set_column_title_direction>`{.interpreted-text
role="ref"}

Sets column title base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_column_title_language}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_column_title_language**(column: `int<class_int>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_Tree_method_set_column_title_language>`{.interpreted-text
role="ref"}

Sets language code of column title used for line-breaking and text
shaping algorithms, if left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_method_set_selected}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selected**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tree_method_set_selected>`{.interpreted-text role="ref"}

Selects the specified `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"} and column.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_Tree_theme_color_children_hl_line_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**children_hl_line_color** = `Color(0.27, 0.27, 0.27, 1)`
`🔗<class_Tree_theme_color_children_hl_line_color>`{.interpreted-text
role="ref"}

The `Color<class_Color>`{.interpreted-text role="ref"} of the
relationship lines between the selected
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} and its
children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_custom_button_font_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**custom_button_font_highlight** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_Tree_theme_color_custom_button_font_highlight>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} for a
`TreeItem.CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} mode cell when it\'s hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_drop_position_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**drop_position_color** = `Color(1, 1, 1, 1)`
`🔗<class_Tree_theme_color_drop_position_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} used to draw possible
drop locations. See
`DropModeFlags<enum_Tree_DropModeFlags>`{.interpreted-text role="ref"}
constants for further description of drop locations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.7, 0.7, 0.7, 1)`
`🔗<class_Tree_theme_color_font_color>`{.interpreted-text role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_Tree_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} for a
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell when it\'s non-editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_hovered_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_Tree_theme_color_font_hovered_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is hovered and not selected yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_hovered_dimmed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_dimmed_color** = `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_Tree_theme_color_font_hovered_dimmed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is hovered, while a button of the same item is hovered as the same
time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_hovered_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_selected_color** = `Color(1, 1, 1, 1)`
`🔗<class_Tree_theme_color_font_hovered_selected_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is hovered and selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_Tree_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(1, 1, 1, 1)`
`🔗<class_Tree_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_guide_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **guide_color** =
`Color(0.7, 0.7, 0.7, 0.25)`
`🔗<class_Tree_theme_color_guide_color>`{.interpreted-text role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the guideline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_parent_hl_line_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**parent_hl_line_color** = `Color(0.27, 0.27, 0.27, 1)`
`🔗<class_Tree_theme_color_parent_hl_line_color>`{.interpreted-text
role="ref"}

The `Color<class_Color>`{.interpreted-text role="ref"} of the
relationship lines between the selected
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} and its
parents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_relationship_line_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**relationship_line_color** = `Color(0.27, 0.27, 0.27, 1)`
`🔗<class_Tree_theme_color_relationship_line_color>`{.interpreted-text
role="ref"}

The default `Color<class_Color>`{.interpreted-text role="ref"} of the
relationship lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_color_title_button_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**title_button_color** = `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_Tree_theme_color_title_button_color>`{.interpreted-text
role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
title button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_button_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **button_margin** = `4`
`🔗<class_Tree_theme_constant_button_margin>`{.interpreted-text
role="ref"}

The horizontal space between each button in a cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_children_hl_line_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**children_hl_line_width** = `1`
`🔗<class_Tree_theme_constant_children_hl_line_width>`{.interpreted-text
role="ref"}

The width of the relationship lines between the selected
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} and its
children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_draw_guides}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **draw_guides** = `1`
`🔗<class_Tree_theme_constant_draw_guides>`{.interpreted-text
role="ref"}

Draws the guidelines if not zero, this acts as a boolean. The guideline
is a horizontal line drawn at the bottom of each item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_draw_relationship_lines}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**draw_relationship_lines** = `0`
`🔗<class_Tree_theme_constant_draw_relationship_lines>`{.interpreted-text
role="ref"}

Draws the relationship lines if not zero, this acts as a boolean.
Relationship lines are drawn at the start of child items to show
hierarchy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_Tree_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal space between item cells. This is also used as the margin
at the start of an item when folding is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_icon_max_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_max_width** = `0`
`🔗<class_Tree_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}

The maximum allowed width of the icon in item\'s cells. This limit is
applied on top of the default size of the icon, but before the value set
with
`TreeItem.set_icon_max_width()<class_TreeItem_method_set_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_inner_item_margin_bottom}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**inner_item_margin_bottom** = `0`
`🔗<class_Tree_theme_constant_inner_item_margin_bottom>`{.interpreted-text
role="ref"}

The inner bottom margin of a cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_inner_item_margin_left}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**inner_item_margin_left** = `0`
`🔗<class_Tree_theme_constant_inner_item_margin_left>`{.interpreted-text
role="ref"}

The inner left margin of a cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_inner_item_margin_right}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**inner_item_margin_right** = `0`
`🔗<class_Tree_theme_constant_inner_item_margin_right>`{.interpreted-text
role="ref"}

The inner right margin of a cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_inner_item_margin_top}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **inner_item_margin_top**
= `0`
`🔗<class_Tree_theme_constant_inner_item_margin_top>`{.interpreted-text
role="ref"}

The inner top margin of a cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_item_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_margin** = `16`
`🔗<class_Tree_theme_constant_item_margin>`{.interpreted-text
role="ref"}

The horizontal margin at the start of an item. This is used when folding
is enabled for the item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_Tree_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_Tree_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_parent_hl_line_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **parent_hl_line_margin**
= `0`
`🔗<class_Tree_theme_constant_parent_hl_line_margin>`{.interpreted-text
role="ref"}

The space between the parent relationship lines for the selected
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} and the
relationship lines to its siblings that are not selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_parent_hl_line_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **parent_hl_line_width**
= `1`
`🔗<class_Tree_theme_constant_parent_hl_line_width>`{.interpreted-text
role="ref"}

The width of the relationship lines between the selected
`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} and its
parents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_relationship_line_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**relationship_line_width** = `1`
`🔗<class_Tree_theme_constant_relationship_line_width>`{.interpreted-text
role="ref"}

The default width of the relationship lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scroll_border}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scroll_border** = `4`
`🔗<class_Tree_theme_constant_scroll_border>`{.interpreted-text
role="ref"}

The maximum distance between the mouse cursor and the control\'s border
to trigger border scrolling when dragging.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scroll_speed}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scroll_speed** = `12`
`🔗<class_Tree_theme_constant_scroll_speed>`{.interpreted-text
role="ref"}

The speed of border scrolling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scrollbar_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**scrollbar_h_separation** = `4`
`🔗<class_Tree_theme_constant_scrollbar_h_separation>`{.interpreted-text
role="ref"}

The horizontal separation of tree content and scrollbar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scrollbar_margin_bottom}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**scrollbar_margin_bottom** = `-1`
`🔗<class_Tree_theme_constant_scrollbar_margin_bottom>`{.interpreted-text
role="ref"}

The bottom margin of the scrollbars. When negative, uses
`panel<class_Tree_theme_style_panel>`{.interpreted-text role="ref"}
bottom margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scrollbar_margin_left}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scrollbar_margin_left**
= `-1`
`🔗<class_Tree_theme_constant_scrollbar_margin_left>`{.interpreted-text
role="ref"}

The left margin of the horizontal scrollbar. When negative, uses
`panel<class_Tree_theme_style_panel>`{.interpreted-text role="ref"} left
margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scrollbar_margin_right}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**scrollbar_margin_right** = `-1`
`🔗<class_Tree_theme_constant_scrollbar_margin_right>`{.interpreted-text
role="ref"}

The right margin of the scrollbars. When negative, uses
`panel<class_Tree_theme_style_panel>`{.interpreted-text role="ref"}
right margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scrollbar_margin_top}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scrollbar_margin_top**
= `-1`
`🔗<class_Tree_theme_constant_scrollbar_margin_top>`{.interpreted-text
role="ref"}

The top margin of the vertical scrollbar. When negative, uses
`panel<class_Tree_theme_style_panel>`{.interpreted-text role="ref"} top
margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_scrollbar_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**scrollbar_v_separation** = `4`
`🔗<class_Tree_theme_constant_scrollbar_v_separation>`{.interpreted-text
role="ref"}

The vertical separation of tree content and scrollbar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_constant_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **v_separation** = `4`
`🔗<class_Tree_theme_constant_v_separation>`{.interpreted-text
role="ref"}

The vertical padding inside each item, i.e. the distance between the
item\'s content and top/bottom border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_Tree_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} of the item\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_font_title_button_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **title_button_font**
`🔗<class_Tree_theme_font_title_button_font>`{.interpreted-text
role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} of the title button\'s
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_Tree_theme_font_size_font_size>`{.interpreted-text role="ref"}

Font size of the item\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_font_size_title_button_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**title_button_font_size**
`🔗<class_Tree_theme_font_size_title_button_font_size>`{.interpreted-text
role="ref"}

Font size of the title button\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **arrow**
`🔗<class_Tree_theme_icon_arrow>`{.interpreted-text role="ref"}

The arrow icon used when a foldable item is not collapsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_arrow_collapsed}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**arrow_collapsed**
`🔗<class_Tree_theme_icon_arrow_collapsed>`{.interpreted-text
role="ref"}

The arrow icon used when a foldable item is collapsed (for left-to-right
layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_arrow_collapsed_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**arrow_collapsed_mirrored**
`🔗<class_Tree_theme_icon_arrow_collapsed_mirrored>`{.interpreted-text
role="ref"}

The arrow icon used when a foldable item is collapsed (for right-to-left
layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_checked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **checked**
`🔗<class_Tree_theme_icon_checked>`{.interpreted-text role="ref"}

The check icon to display when the
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell is checked and editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_checked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**checked_disabled**
`🔗<class_Tree_theme_icon_checked_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell is checked and non-editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_indeterminate}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**indeterminate**
`🔗<class_Tree_theme_icon_indeterminate>`{.interpreted-text role="ref"}

The check icon to display when the
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell is indeterminate and editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_indeterminate_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**indeterminate_disabled**
`🔗<class_Tree_theme_icon_indeterminate_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell is indeterminate and non-editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_select_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**select_arrow**
`🔗<class_Tree_theme_icon_select_arrow>`{.interpreted-text role="ref"}

The arrow icon to display for the
`TreeItem.CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"} mode cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_unchecked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **unchecked**
`🔗<class_Tree_theme_icon_unchecked>`{.interpreted-text role="ref"}

The check icon to display when the
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell is unchecked and editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_unchecked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**unchecked_disabled**
`🔗<class_Tree_theme_icon_unchecked_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the
`TreeItem.CELL_MODE_CHECK<class_TreeItem_constant_CELL_MODE_CHECK>`{.interpreted-text
role="ref"} mode cell is unchecked and non-editable (see
`TreeItem.set_editable()<class_TreeItem_method_set_editable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_icon_updown}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **updown**
`🔗<class_Tree_theme_icon_updown>`{.interpreted-text role="ref"}

The updown arrow icon to display for the
`TreeItem.CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"} mode cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_button_hover}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**button_hover**
`🔗<class_Tree_theme_style_button_hover>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when a
button in the tree is hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_button_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**button_pressed**
`🔗<class_Tree_theme_style_button_pressed>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when a
button in the tree is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_cursor}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **cursor**
`🔗<class_Tree_theme_style_cursor>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for the
cursor, when the **Tree** is being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_cursor_unfocused}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**cursor_unfocused**
`🔗<class_Tree_theme_style_cursor_unfocused>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for the
cursor, when the **Tree** is not being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_custom_button}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**custom_button**
`🔗<class_Tree_theme_style_custom_button>`{.interpreted-text role="ref"}

Default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for a
`TreeItem.CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} mode cell when button is enabled with
`TreeItem.set_custom_as_button()<class_TreeItem_method_set_custom_as_button>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_custom_button_hover}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**custom_button_hover**
`🔗<class_Tree_theme_style_custom_button_hover>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for a
`TreeItem.CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} mode button cell when it\'s hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_custom_button_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**custom_button_pressed**
`🔗<class_Tree_theme_style_custom_button_pressed>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for a
`TreeItem.CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} mode button cell when it\'s pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_Tree_theme_style_focus>`{.interpreted-text role="ref"}

The focused style for the **Tree**, drawn on top of everything.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_hovered}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **hovered**
`🔗<class_Tree_theme_style_hovered>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the item
being hovered, but not selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_hovered_dimmed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hovered_dimmed**
`🔗<class_Tree_theme_style_hovered_dimmed>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the item
being hovered, while a button of the same item is hovered as the same
time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_hovered_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hovered_selected**
`🔗<class_Tree_theme_style_hovered_selected>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the hovered
and selected items, used when the **Tree** is not being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_hovered_selected_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hovered_selected_focus**
`🔗<class_Tree_theme_style_hovered_selected_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the hovered
and selected items, used when the **Tree** is being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_Tree_theme_style_panel>`{.interpreted-text role="ref"}

The background style for the **Tree**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **selected**
`🔗<class_Tree_theme_style_selected>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
selected items, used when the **Tree** is not being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_selected_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**selected_focus**
`🔗<class_Tree_theme_style_selected_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
selected items, used when the **Tree** is being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_title_button_hover}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**title_button_hover**
`🔗<class_Tree_theme_style_title_button_hover>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
title button is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_title_button_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**title_button_normal**
`🔗<class_Tree_theme_style_title_button_normal>`{.interpreted-text
role="ref"}

Default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
title button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tree_theme_style_title_button_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**title_button_pressed**
`🔗<class_Tree_theme_style_title_button_pressed>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
title button is being pressed.
