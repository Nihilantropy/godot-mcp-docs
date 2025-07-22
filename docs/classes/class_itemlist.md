github_url
:   hide

# ItemList {#class_ItemList}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A vertical list of selectable items with one or multiple columns.

::: rst-class
classref-introduction-group
:::

## Description

This control provides a vertical list of selectable items that may be in
a single or in multiple columns, with each item having options for text
and an icon. Tooltips are supported and may be different for every item
in the list.

Selectable items in the list may be selected or deselected and multiple
selection may be enabled. Selection with right mouse button may also be
enabled to allow use of popup context menus. Items may also be
\"activated\" by double-clicking them or by pressing
`Enter`{.interpreted-text role="kbd"}.

Item text only supports single-line strings. Newline characters (e.g.
`\n`) in the string won\'t produce a newline. Text wrapping is enabled
in
`ICON_MODE_TOP<class_ItemList_constant_ICON_MODE_TOP>`{.interpreted-text
role="ref"} mode, but the column\'s width is adjusted to fully fit its
content by default. You need to set
`fixed_column_width<class_ItemList_property_fixed_column_width>`{.interpreted-text
role="ref"} greater than zero to wrap the text.

All `set_*` methods allow negative item indices, i.e. `-1` to access the
last item, `-2` to select the second-to-last item, and so on.

\*\*Incremental search:\*\* Like
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"} and
`Tree<class_Tree>`{.interpreted-text role="ref"}, **ItemList** supports
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

:::: {#class_ItemList_signal_empty_clicked}
::: rst-class
classref-signal
:::
::::

**empty_clicked**(at_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
mouse_button_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ItemList_signal_empty_clicked>`{.interpreted-text role="ref"}

Emitted when any mouse click is issued within the rect of the list but
on empty space.

`at_position` is the click position in this control\'s local coordinate
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_signal_item_activated}
::: rst-class
classref-signal
:::
::::

**item_activated**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_signal_item_activated>`{.interpreted-text role="ref"}

Emitted when specified list item is activated via double-clicking or by
pressing `Enter`{.interpreted-text role="kbd"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_signal_item_clicked}
::: rst-class
classref-signal
:::
::::

**item_clicked**(index: `int<class_int>`{.interpreted-text role="ref"},
at_position: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
mouse_button_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ItemList_signal_item_clicked>`{.interpreted-text role="ref"}

Emitted when specified list item has been clicked with any mouse button.

`at_position` is the click position in this control\'s local coordinate
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_signal_item_selected}
::: rst-class
classref-signal
:::
::::

**item_selected**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ItemList_signal_item_selected>`{.interpreted-text role="ref"}

Emitted when specified item has been selected. Only applicable in single
selection mode.

`allow_reselect<class_ItemList_property_allow_reselect>`{.interpreted-text
role="ref"} must be enabled to reselect an item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_signal_multi_selected}
::: rst-class
classref-signal
:::
::::

**multi_selected**(index: `int<class_int>`{.interpreted-text
role="ref"}, selected: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ItemList_signal_multi_selected>`{.interpreted-text role="ref"}

Emitted when a multiple selection is altered on a list allowing multiple
selection.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ItemList_IconMode}
::: rst-class
classref-enumeration
:::
::::

enum **IconMode**: `🔗<enum_ItemList_IconMode>`{.interpreted-text
role="ref"}

:::: {#class_ItemList_constant_ICON_MODE_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`IconMode<enum_ItemList_IconMode>`{.interpreted-text role="ref"}
**ICON_MODE_TOP** = `0`

Icon is drawn above the text.

:::: {#class_ItemList_constant_ICON_MODE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`IconMode<enum_ItemList_IconMode>`{.interpreted-text role="ref"}
**ICON_MODE_LEFT** = `1`

Icon is drawn to the left of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ItemList_SelectMode}
::: rst-class
classref-enumeration
:::
::::

enum **SelectMode**: `🔗<enum_ItemList_SelectMode>`{.interpreted-text
role="ref"}

:::: {#class_ItemList_constant_SELECT_SINGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"}
**SELECT_SINGLE** = `0`

Only allow selecting a single item.

:::: {#class_ItemList_constant_SELECT_MULTI}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"}
**SELECT_MULTI** = `1`

Allows selecting multiple items by holding `Ctrl`{.interpreted-text
role="kbd"} or `Shift`{.interpreted-text role="kbd"}.

:::: {#class_ItemList_constant_SELECT_TOGGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"}
**SELECT_TOGGLE** = `2`

Allows selecting multiple items by toggling them on and off.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ItemList_property_allow_reselect}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_reselect** =
`false` `🔗<class_ItemList_property_allow_reselect>`{.interpreted-text
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

:::: {#class_ItemList_property_allow_rmb_select}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_rmb_select** =
`false` `🔗<class_ItemList_property_allow_rmb_select>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_rmb_select**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_rmb_select**()

If `true`, right mouse button click can select items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_allow_search}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_search** =
`true` `🔗<class_ItemList_property_allow_search>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_search**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_search**()

If `true`, allows navigating the **ItemList** with letter keys through
incremental search.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_auto_height}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_height** =
`false` `🔗<class_ItemList_property_auto_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_height**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_auto_height**()

If `true`, the control will automatically resize the height to fit its
content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_auto_width}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_width** =
`false` `🔗<class_ItemList_property_auto_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_width**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_auto_width**()

If `true`, the control will automatically resize the width to fit its
content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_fixed_column_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fixed_column_width** =
`0` `🔗<class_ItemList_property_fixed_column_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fixed_column_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_fixed_column_width**()

The width all columns will be adjusted to.

A value of zero disables the adjustment, each item will have a width
equal to the width of its content and the columns will have an uneven
width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_fixed_icon_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**fixed_icon_size** = `Vector2i(0, 0)`
`🔗<class_ItemList_property_fixed_icon_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fixed_icon_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_fixed_icon_size**()

The size all icons will be adjusted to.

If either X or Y component is not greater than zero, icon size won\'t be
affected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_icon_mode}
::: rst-class
classref-property
:::
::::

`IconMode<enum_ItemList_IconMode>`{.interpreted-text role="ref"}
**icon_mode** = `1`
`🔗<class_ItemList_property_icon_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_icon_mode**(value:
  `IconMode<enum_ItemList_IconMode>`{.interpreted-text role="ref"})
- `IconMode<enum_ItemList_IconMode>`{.interpreted-text role="ref"}
  **get_icon_mode**()

The icon position, whether above or to the left of the text. See the
`IconMode<enum_ItemList_IconMode>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_icon_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **icon_scale** =
`1.0` `🔗<class_ItemList_property_icon_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_icon_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_icon_scale**()

The scale of icon applied after
`fixed_icon_size<class_ItemList_property_fixed_icon_size>`{.interpreted-text
role="ref"} and transposing takes effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_item_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **item_count** = `0`
`🔗<class_ItemList_property_item_count>`{.interpreted-text role="ref"}

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

:::: {#class_ItemList_property_max_columns}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_columns** = `1`
`🔗<class_ItemList_property_max_columns>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_columns**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_columns**()

Maximum columns the list will have.

If greater than zero, the content will be split among the specified
columns.

A value of zero means unlimited columns, i.e. all items will be put in
the same row.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_max_text_lines}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_text_lines** = `1`
`🔗<class_ItemList_property_max_text_lines>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_text_lines**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_text_lines**()

Maximum lines of text allowed in each item. Space will be reserved even
when there is not enough lines of text to display.

\*\*Note:\*\* This property takes effect only when
`icon_mode<class_ItemList_property_icon_mode>`{.interpreted-text
role="ref"} is
`ICON_MODE_TOP<class_ItemList_constant_ICON_MODE_TOP>`{.interpreted-text
role="ref"}. To make the text wrap,
`fixed_column_width<class_ItemList_property_fixed_column_width>`{.interpreted-text
role="ref"} should be greater than zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_same_column_width}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **same_column_width** =
`false`
`🔗<class_ItemList_property_same_column_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_same_column_width**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_same_column_width**()

Whether all columns will have the same width.

If `true`, the width is equal to the largest column width of all
columns.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_select_mode}
::: rst-class
classref-property
:::
::::

`SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"}
**select_mode** = `0`
`🔗<class_ItemList_property_select_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_select_mode**(value:
  `SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"})
- `SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"}
  **get_select_mode**()

Allows single or multiple item selection. See the
`SelectMode<enum_ItemList_SelectMode>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_text_overrun_behavior}
::: rst-class
classref-property
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **text_overrun_behavior** = `3`
`🔗<class_ItemList_property_text_overrun_behavior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_overrun_behavior**(value:
  `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"})
- `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"} **get_text_overrun_behavior**()

The clipping behavior when the text exceeds an item\'s bounding
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_property_wraparound_items}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **wraparound_items** =
`true` `🔗<class_ItemList_property_wraparound_items>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wraparound_items**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **has_wraparound_items**()

If `true`, the control will automatically move items into a new row to
fit its content. See also
`HFlowContainer<class_HFlowContainer>`{.interpreted-text role="ref"} for
this behavior.

If `false`, the control will add a horizontal scrollbar to make all
items visible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ItemList_method_add_icon_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_icon_item**(icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, selectable:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_ItemList_method_add_icon_item>`{.interpreted-text role="ref"}

Adds an item to the item list with no text, only an icon. Returns the
index of an added item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_add_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_item**(text:
`String<class_String>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} = null,
selectable: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_ItemList_method_add_item>`{.interpreted-text role="ref"}

Adds an item to the item list with specified text. Returns the index of
an added item.

Specify an `icon`, or use `null` as the `icon` for a list item with no
icon.

If `selectable` is `true`, the list item will be selectable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_ItemList_method_clear>`{.interpreted-text role="ref"}

Removes all items from the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_deselect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**deselect**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_deselect>`{.interpreted-text role="ref"}

Ensures the item associated with the specified index is not selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_deselect_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**deselect_all**()
`🔗<class_ItemList_method_deselect_all>`{.interpreted-text role="ref"}

Ensures there are no items selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_ensure_current_is_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**ensure_current_is_visible**()
`🔗<class_ItemList_method_ensure_current_is_visible>`{.interpreted-text
role="ref"}

Ensure current selection is visible, adjusting the scroll position as
necessary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_force_update_list_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_list_size**()
`🔗<class_ItemList_method_force_update_list_size>`{.interpreted-text
role="ref"}

Forces an update to the list size based on its items. This happens
automatically whenever size of the items, or other relevant settings
like
`auto_height<class_ItemList_property_auto_height>`{.interpreted-text
role="ref"}, change. The method can be used to trigger the update ahead
of next drawing pass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_h_scroll_bar}
::: rst-class
classref-method
:::
::::

`HScrollBar<class_HScrollBar>`{.interpreted-text role="ref"}
**get_h_scroll_bar**()
`🔗<class_ItemList_method_get_h_scroll_bar>`{.interpreted-text
role="ref"}

Returns the horizontal scrollbar.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_at_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_item_at_position**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, exact:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_at_position>`{.interpreted-text
role="ref"}

Returns the item index at the given `position`.

When there is no item at that point, -1 will be returned if `exact` is
`true`, and the closest item index will be returned otherwise.

\*\*Note:\*\* The returned value is unreliable if called right after
modifying the **ItemList**, before it redraws in the next frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **get_item_auto_translate_mode**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_auto_translate_mode>`{.interpreted-text
role="ref"}

Returns item\'s auto translate mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_custom_bg_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_item_custom_bg_color**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_custom_bg_color>`{.interpreted-text
role="ref"}

Returns the custom background color of the item specified by `idx`
index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_custom_fg_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_item_custom_fg_color**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_custom_fg_color>`{.interpreted-text
role="ref"}

Returns the custom foreground color of the item specified by `idx`
index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_item_icon**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ItemList_method_get_item_icon>`{.interpreted-text
role="ref"}

Returns the icon associated with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_icon_modulate}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_item_icon_modulate**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_icon_modulate>`{.interpreted-text
role="ref"}

Returns a `Color<class_Color>`{.interpreted-text role="ref"} modulating
item\'s icon at the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_icon_region}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_item_icon_region**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_icon_region>`{.interpreted-text
role="ref"}

Returns the region of item\'s icon used. The whole icon will be used if
the region has no area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_language**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_language>`{.interpreted-text
role="ref"}

Returns item\'s text language code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_item_metadata**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_metadata>`{.interpreted-text
role="ref"}

Returns the metadata value of the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_item_rect**(idx: `int<class_int>`{.interpreted-text role="ref"},
expand: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ItemList_method_get_item_rect>`{.interpreted-text
role="ref"}

Returns the position and size of the item with the specified index, in
the coordinate system of the **ItemList** node. If `expand` is `true`
the last column expands to fill the rest of the row.

\*\*Note:\*\* The returned value is unreliable if called right after
modifying the **ItemList**, before it redraws in the next frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_text**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ItemList_method_get_item_text>`{.interpreted-text
role="ref"}

Returns the text associated with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_text_direction}
::: rst-class
classref-method
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **get_item_text_direction**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_text_direction>`{.interpreted-text
role="ref"}

Returns item\'s text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_item_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_item_tooltip**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_get_item_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip hint associated with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_selected_items}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_selected_items**()
`🔗<class_ItemList_method_get_selected_items>`{.interpreted-text
role="ref"}

Returns an array with the indexes of the selected items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_get_v_scroll_bar}
::: rst-class
classref-method
:::
::::

`VScrollBar<class_VScrollBar>`{.interpreted-text role="ref"}
**get_v_scroll_bar**()
`🔗<class_ItemList_method_get_v_scroll_bar>`{.interpreted-text
role="ref"}

Returns the vertical scrollbar.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_is_anything_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_anything_selected**()
`🔗<class_ItemList_method_is_anything_selected>`{.interpreted-text
role="ref"}

Returns `true` if one or more items are selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_is_item_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_disabled**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_is_item_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the item at the specified index is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_is_item_icon_transposed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_icon_transposed**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_is_item_icon_transposed>`{.interpreted-text
role="ref"}

Returns `true` if the item icon will be drawn transposed, i.e. the X and
Y axes are swapped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_is_item_selectable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_selectable**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_is_item_selectable>`{.interpreted-text
role="ref"}

Returns `true` if the item at the specified index is selectable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_is_item_tooltip_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_item_tooltip_enabled**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ItemList_method_is_item_tooltip_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the tooltip is enabled for specified item index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_is_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_selected**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ItemList_method_is_selected>`{.interpreted-text
role="ref"}

Returns `true` if the item at the specified index is currently selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_move_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_item**(from_idx: `int<class_int>`{.interpreted-text role="ref"},
to_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_move_item>`{.interpreted-text role="ref"}

Moves item from index `from_idx` to `to_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_remove_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_item**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_remove_item>`{.interpreted-text role="ref"}

Removes the item specified by `idx` index from the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_select}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **select**(idx:
`int<class_int>`{.interpreted-text role="ref"}, single:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_ItemList_method_select>`{.interpreted-text role="ref"}

Select the item at the specified index.

\*\*Note:\*\* This method does not trigger the item selection signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_auto_translate_mode**(idx: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_auto_translate_mode>`{.interpreted-text
role="ref"}

Sets the auto translate mode of the item associated with the specified
index.

Items use
`Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>`{.interpreted-text
role="ref"} by default, which uses the same auto translate mode as the
**ItemList** itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_custom_bg_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_custom_bg_color**(idx: `int<class_int>`{.interpreted-text
role="ref"}, custom_bg_color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_custom_bg_color>`{.interpreted-text
role="ref"}

Sets the background color of the item specified by `idx` index to the
specified `Color<class_Color>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_custom_fg_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_custom_fg_color**(idx: `int<class_int>`{.interpreted-text
role="ref"}, custom_fg_color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_custom_fg_color>`{.interpreted-text
role="ref"}

Sets the foreground color of the item specified by `idx` index to the
specified `Color<class_Color>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_disabled**(idx: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_set_item_disabled>`{.interpreted-text
role="ref"}

Disables (or enables) the item at the specified index.

Disabled items cannot be selected and do not trigger activation signals
(when double-clicking or pressing `Enter`{.interpreted-text
role="kbd"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon**(idx: `int<class_int>`{.interpreted-text role="ref"},
icon: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_set_item_icon>`{.interpreted-text role="ref"}

Sets (or replaces) the icon\'s
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} associated
with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_icon_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon_modulate**(idx: `int<class_int>`{.interpreted-text
role="ref"}, modulate: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_icon_modulate>`{.interpreted-text
role="ref"}

Sets a modulating `Color<class_Color>`{.interpreted-text role="ref"} of
the item associated with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_icon_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon_region**(idx: `int<class_int>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_set_item_icon_region>`{.interpreted-text
role="ref"}

Sets the region of item\'s icon used. The whole icon will be used if the
region has no area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_icon_transposed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_icon_transposed**(idx: `int<class_int>`{.interpreted-text
role="ref"}, transposed: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_icon_transposed>`{.interpreted-text
role="ref"}

Sets whether the item icon will be drawn transposed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_language}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_language**(idx: `int<class_int>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_language>`{.interpreted-text
role="ref"}

Sets language code of item\'s text used for line-breaking and text
shaping algorithms, if left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_metadata**(idx: `int<class_int>`{.interpreted-text
role="ref"}, metadata: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_metadata>`{.interpreted-text
role="ref"}

Sets a value (of any type) to be stored with the item associated with
the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_selectable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_selectable**(idx: `int<class_int>`{.interpreted-text
role="ref"}, selectable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_selectable>`{.interpreted-text
role="ref"}

Allows or disallows selection of the item associated with the specified
index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_text**(idx: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_set_item_text>`{.interpreted-text role="ref"}

Sets text of the item associated with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_text_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_text_direction**(idx: `int<class_int>`{.interpreted-text
role="ref"}, direction:
`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_text_direction>`{.interpreted-text
role="ref"}

Sets item\'s text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_tooltip**(idx: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ItemList_method_set_item_tooltip>`{.interpreted-text
role="ref"}

Sets the tooltip hint for the item associated with the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_set_item_tooltip_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_item_tooltip_enabled**(idx: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ItemList_method_set_item_tooltip_enabled>`{.interpreted-text
role="ref"}

Sets whether the tooltip hint is enabled for specified item index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_method_sort_items_by_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sort_items_by_text**()
`🔗<class_ItemList_method_sort_items_by_text>`{.interpreted-text
role="ref"}

Sorts items in the list by their text.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_ItemList_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.65, 0.65, 0.65, 1)`
`🔗<class_ItemList_theme_color_font_color>`{.interpreted-text
role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_color_font_hovered_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_ItemList_theme_color_font_hovered_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is hovered and not selected yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_color_font_hovered_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_selected_color** = `Color(1, 1, 1, 1)`
`🔗<class_ItemList_theme_color_font_hovered_selected_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is hovered and selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_ItemList_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(1, 1, 1, 1)`
`🔗<class_ItemList_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
item is selected, but not hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_color_guide_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **guide_color** =
`Color(0.7, 0.7, 0.7, 0.25)`
`🔗<class_ItemList_theme_color_guide_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the guideline. The
guideline is a line drawn between each row of items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_ItemList_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal spacing between items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_constant_icon_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_margin** = `4`
`🔗<class_ItemList_theme_constant_icon_margin>`{.interpreted-text
role="ref"}

The spacing between item\'s icon and text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_constant_line_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **line_separation** = `2`
`🔗<class_ItemList_theme_constant_line_separation>`{.interpreted-text
role="ref"}

The vertical spacing between each line of text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_ItemList_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the item text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_ItemList_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_constant_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **v_separation** = `4`
`🔗<class_ItemList_theme_constant_v_separation>`{.interpreted-text
role="ref"}

The vertical spacing between items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_ItemList_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} of the item\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_ItemList_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the item\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_cursor}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **cursor**
`🔗<class_ItemList_theme_style_cursor>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for the
cursor, when the **ItemList** is being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_cursor_unfocused}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**cursor_unfocused**
`🔗<class_ItemList_theme_style_cursor_unfocused>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for the
cursor, when the **ItemList** is not being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_ItemList_theme_style_focus>`{.interpreted-text role="ref"}

The focused style for the **ItemList**, drawn on top of the background,
but below everything else.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_hovered}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **hovered**
`🔗<class_ItemList_theme_style_hovered>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
hovered, but not selected items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_hovered_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hovered_selected**
`🔗<class_ItemList_theme_style_hovered_selected>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the hovered
and selected items, used when the **ItemList** is not being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_hovered_selected_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hovered_selected_focus**
`🔗<class_ItemList_theme_style_hovered_selected_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the hovered
and selected items, used when the **ItemList** is being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_ItemList_theme_style_panel>`{.interpreted-text role="ref"}

The background style for the **ItemList**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **selected**
`🔗<class_ItemList_theme_style_selected>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
selected items, used when the **ItemList** is not being focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ItemList_theme_style_selected_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**selected_focus**
`🔗<class_ItemList_theme_style_selected_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
selected items, used when the **ItemList** is being focused.
