github_url
:   hide

# TreeItem {#class_TreeItem}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

An internal control for a single item inside
`Tree<class_Tree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A single item of a `Tree<class_Tree>`{.interpreted-text role="ref"}
control. It can contain other **TreeItem**s as children, which allows it
to create a hierarchy. It can also contain text and buttons.
**TreeItem** is not a `Node<class_Node>`{.interpreted-text role="ref"},
it is internal to the `Tree<class_Tree>`{.interpreted-text role="ref"}.

To create a **TreeItem**, use
`Tree.create_item()<class_Tree_method_create_item>`{.interpreted-text
role="ref"} or
`create_child()<class_TreeItem_method_create_child>`{.interpreted-text
role="ref"}. To remove a **TreeItem**, use
`Object.free()<class_Object_method_free>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The ID values used for buttons are 32-bit, unlike
`int<class_int>`{.interpreted-text role="ref"} which is always 64-bit.
They go from `-2147483648` to `2147483647`.

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

## Enumerations

:::: {#enum_TreeItem_TreeCellMode}
::: rst-class
classref-enumeration
:::
::::

enum **TreeCellMode**:
`🔗<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}

:::: {#class_TreeItem_constant_CELL_MODE_STRING}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}
**CELL_MODE_STRING** = `0`

Cell shows a string label, optionally with an icon. When editable, the
text can be edited using a `LineEdit<class_LineEdit>`{.interpreted-text
role="ref"}, or a `TextEdit<class_TextEdit>`{.interpreted-text
role="ref"} popup if
`set_edit_multiline()<class_TreeItem_method_set_edit_multiline>`{.interpreted-text
role="ref"} is used.

:::: {#class_TreeItem_constant_CELL_MODE_CHECK}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}
**CELL_MODE_CHECK** = `1`

Cell shows a checkbox, optionally with text and an icon. The checkbox
can be pressed, released, or indeterminate (via
`set_indeterminate()<class_TreeItem_method_set_indeterminate>`{.interpreted-text
role="ref"}). The checkbox can\'t be clicked unless the cell is
editable.

:::: {#class_TreeItem_constant_CELL_MODE_RANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}
**CELL_MODE_RANGE** = `2`

Cell shows a numeric range. When editable, it can be edited using a
range slider. Use
`set_range()<class_TreeItem_method_set_range>`{.interpreted-text
role="ref"} to set the value and
`set_range_config()<class_TreeItem_method_set_range_config>`{.interpreted-text
role="ref"} to configure the range.

This cell can also be used in a text dropdown mode when you assign a
text with `set_text()<class_TreeItem_method_set_text>`{.interpreted-text
role="ref"}. Separate options with a comma, e.g.
`"Option1,Option2,Option3"`.

:::: {#class_TreeItem_constant_CELL_MODE_ICON}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}
**CELL_MODE_ICON** = `3`

Cell shows an icon. It can\'t be edited nor display text. The icon is
always centered within the cell.

:::: {#class_TreeItem_constant_CELL_MODE_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}
**CELL_MODE_CUSTOM** = `4`

Cell shows as a clickable button. It will display an arrow similar to
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"}, but
doesn\'t feature a dropdown (for that you can use
`CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"}). Clicking the button emits the
`Tree.item_edited<class_Tree_signal_item_edited>`{.interpreted-text
role="ref"} signal. The button is flat by default, you can use
`set_custom_as_button()<class_TreeItem_method_set_custom_as_button>`{.interpreted-text
role="ref"} to display it with a
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}.

This mode also supports custom drawing using
`set_custom_draw_callback()<class_TreeItem_method_set_custom_draw_callback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TreeItem_property_collapsed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collapsed**
`🔗<class_TreeItem_property_collapsed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collapsed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_collapsed**()

If `true`, the TreeItem is collapsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_property_custom_minimum_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **custom_minimum_height**
`🔗<class_TreeItem_property_custom_minimum_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_minimum_height**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_custom_minimum_height**()

The custom minimum height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_property_disable_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disable_folding**
`🔗<class_TreeItem_property_disable_folding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_folding**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_folding_disabled**()

If `true`, folding is disabled for this TreeItem.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible**
`🔗<class_TreeItem_property_visible>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, the **TreeItem** is visible (default).

Note that if a **TreeItem** is set to not be visible, none of its
children will be visible either.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TreeItem_method_add_button}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_button**(column: `int<class_int>`{.interpreted-text role="ref"},
button: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"} = -1, disabled:
`bool<class_bool>`{.interpreted-text role="ref"} = false, tooltip_text:
`String<class_String>`{.interpreted-text role="ref"} = \"\",
description: `String<class_String>`{.interpreted-text role="ref"} =
\"\") `🔗<class_TreeItem_method_add_button>`{.interpreted-text
role="ref"}

Adds a button with `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} `button` to the end of the cell at column `column`. The `id`
is used to identify the button in the according
`Tree.button_clicked<class_Tree_signal_button_clicked>`{.interpreted-text
role="ref"} signal and can be different from the buttons index. If not
specified, the next available index is used, which may be retrieved by
calling
`get_button_count()<class_TreeItem_method_get_button_count>`{.interpreted-text
role="ref"} immediately before this method. Optionally, the button can
be `disabled` and have a `tooltip_text`. `description` is used as the
button description for assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_add_child}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_child**(child: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}) `🔗<class_TreeItem_method_add_child>`{.interpreted-text
role="ref"}

Adds a previously unparented **TreeItem** as a direct child of this one.
The `child` item must not be a part of any
`Tree<class_Tree>`{.interpreted-text role="ref"} or parented to any
**TreeItem**. See also
`remove_child()<class_TreeItem_method_remove_child>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_call_recursive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**call_recursive**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_call_recursive>`{.interpreted-text role="ref"}

Calls the `method` on the actual TreeItem and its children recursively.
Pass parameters as a comma separated list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_clear_buttons}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_buttons**()
`🔗<class_TreeItem_method_clear_buttons>`{.interpreted-text role="ref"}

Removes all buttons from all columns of this item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_clear_custom_bg_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_custom_bg_color**(column: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_clear_custom_bg_color>`{.interpreted-text
role="ref"}

Resets the background color for the given column to default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_clear_custom_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_custom_color**(column: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_clear_custom_color>`{.interpreted-text
role="ref"}

Resets the color for the given column to default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_create_child}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**create_child**(index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_TreeItem_method_create_child>`{.interpreted-text
role="ref"}

Creates an item and adds it as a child.

The new item will be inserted as position `index` (the default value
`-1` means the last position), or it will be the last child if `index`
is higher than the child count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_deselect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**deselect**(column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_deselect>`{.interpreted-text role="ref"}

Deselects the given column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_erase_button}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_button**(column: `int<class_int>`{.interpreted-text role="ref"},
button_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_erase_button>`{.interpreted-text role="ref"}

Removes the button at index `button_index` in column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **get_auto_translate_mode**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_auto_translate_mode>`{.interpreted-text
role="ref"}

Returns the column\'s auto translate mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_autowrap_mode}
::: rst-class
classref-method
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **get_autowrap_mode**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_autowrap_mode>`{.interpreted-text
role="ref"}

Returns the text autowrap mode in the given `column`. By default it is
`TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_button}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_button**(column: `int<class_int>`{.interpreted-text role="ref"},
button_index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_button>`{.interpreted-text
role="ref"}

Returns the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
of the button at index `button_index` in column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_button_by_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_button_by_id**(column: `int<class_int>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_button_by_id>`{.interpreted-text
role="ref"}

Returns the button index if there is a button with ID `id` in column
`column`, otherwise returns -1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_button_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_button_color**(column: `int<class_int>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_button_color>`{.interpreted-text
role="ref"}

Returns the color of the button with ID `id` in column `column`. If the
specified button does not exist, returns
`Color.BLACK<class_Color_constant_BLACK>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_button_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_button_count**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_button_count>`{.interpreted-text
role="ref"}

Returns the number of buttons in column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_button_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_button_id**(column:
`int<class_int>`{.interpreted-text role="ref"}, button_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_button_id>`{.interpreted-text
role="ref"}

Returns the ID for the button at index `button_index` in column
`column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_button_tooltip_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_button_tooltip_text**(column: `int<class_int>`{.interpreted-text
role="ref"}, button_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_button_tooltip_text>`{.interpreted-text
role="ref"}

Returns the tooltip text for the button at index `button_index` in
column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_cell_mode}
::: rst-class
classref-method
:::
::::

`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text role="ref"}
**get_cell_mode**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_cell_mode>`{.interpreted-text
role="ref"}

Returns the column\'s cell mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_child}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_child**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_get_child>`{.interpreted-text role="ref"}

Returns a child item by its `index` (see
`get_child_count()<class_TreeItem_method_get_child_count>`{.interpreted-text
role="ref"}). This method is often used for iterating all children of an
item.

Negative indices access the children from the last one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_child_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_child_count**()
`🔗<class_TreeItem_method_get_child_count>`{.interpreted-text
role="ref"}

Returns the number of child items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_children}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}\]
**get_children**()
`🔗<class_TreeItem_method_get_children>`{.interpreted-text role="ref"}

Returns an array of references to the item\'s children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_custom_bg_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_custom_bg_color**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_custom_bg_color>`{.interpreted-text
role="ref"}

Returns the custom background color of column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_custom_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_custom_color**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_custom_color>`{.interpreted-text
role="ref"}

Returns the custom color of column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_custom_draw_callback}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**get_custom_draw_callback**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_custom_draw_callback>`{.interpreted-text
role="ref"}

Returns the custom callback of column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_custom_font}
::: rst-class
classref-method
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"}
**get_custom_font**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_custom_font>`{.interpreted-text
role="ref"}

Returns custom font used to draw text in the column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_custom_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_custom_font_size**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_custom_font_size>`{.interpreted-text
role="ref"}

Returns custom font size used to draw text in the column `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_description}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_description**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_description>`{.interpreted-text
role="ref"}

Returns the given column\'s description for assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_expand_right}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_expand_right**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_expand_right>`{.interpreted-text
role="ref"}

Returns `true` if `expand_right` is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_first_child}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_first_child**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_first_child>`{.interpreted-text
role="ref"}

Returns the TreeItem\'s first child.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_icon**(column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_icon>`{.interpreted-text
role="ref"}

Returns the given column\'s icon
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}. Error if no
icon is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_icon_max_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_icon_max_width**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_icon_max_width>`{.interpreted-text
role="ref"}

Returns the maximum allowed width of the icon in the given `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_icon_modulate}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_icon_modulate**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_icon_modulate>`{.interpreted-text
role="ref"}

Returns the `Color<class_Color>`{.interpreted-text role="ref"}
modulating the column\'s icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_icon_overlay}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_icon_overlay**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_icon_overlay>`{.interpreted-text
role="ref"}

Returns the given column\'s icon overlay
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_icon_region}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_icon_region**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_icon_region>`{.interpreted-text
role="ref"}

Returns the icon `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} region as `Rect2<class_Rect2>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_index**()
`🔗<class_TreeItem_method_get_index>`{.interpreted-text role="ref"}

Returns the node\'s order in the tree. For example, if called on the
first child item the position is `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_language**(column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_language>`{.interpreted-text
role="ref"}

Returns item\'s text language code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_metadata**(column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_metadata>`{.interpreted-text
role="ref"}

Returns the metadata value that was set for the given column using
`set_metadata()<class_TreeItem_method_set_metadata>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_next}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} **get_next**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_next>`{.interpreted-text
role="ref"}

Returns the next sibling TreeItem in the tree or a `null` object if
there is none.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_next_in_tree}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_next_in_tree**(wrap: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_TreeItem_method_get_next_in_tree>`{.interpreted-text
role="ref"}

Returns the next TreeItem in the tree (in the context of a depth-first
search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first element
in the tree when called on the last element, otherwise it returns
`null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_next_visible}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_next_visible**(wrap: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_TreeItem_method_get_next_visible>`{.interpreted-text
role="ref"}

Returns the next visible TreeItem in the tree (in the context of a
depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first visible
element in the tree when called on the last visible element, otherwise
it returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_parent}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_parent**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_parent>`{.interpreted-text
role="ref"}

Returns the parent TreeItem or a `null` object if there is none.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_prev}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"} **get_prev**()
`🔗<class_TreeItem_method_get_prev>`{.interpreted-text role="ref"}

Returns the previous sibling TreeItem in the tree or a `null` object if
there is none.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_prev_in_tree}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_prev_in_tree**(wrap: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_TreeItem_method_get_prev_in_tree>`{.interpreted-text
role="ref"}

Returns the previous TreeItem in the tree (in the context of a
depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last element in
the tree when called on the first visible element, otherwise it returns
`null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_prev_visible}
::: rst-class
classref-method
:::
::::

`TreeItem<class_TreeItem>`{.interpreted-text role="ref"}
**get_prev_visible**(wrap: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_TreeItem_method_get_prev_visible>`{.interpreted-text
role="ref"}

Returns the previous visible sibling TreeItem in the tree (in the
context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last visible
element in the tree when called on the first visible element, otherwise
it returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_range}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_range**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_range>`{.interpreted-text
role="ref"}

Returns the value of a
`CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"} column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_range_config}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_range_config**(column: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_get_range_config>`{.interpreted-text
role="ref"}

Returns a dictionary containing the range parameters for a given column.
The keys are \"min\", \"max\", \"step\", and \"expr\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_structured_text_bidi_override}
::: rst-class
classref-method
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **get_structured_text_bidi_override**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_structured_text_bidi_override>`{.interpreted-text
role="ref"}

Returns the BiDi algorithm override set for this cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_structured_text_bidi_override_options}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_structured_text_bidi_override_options**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_structured_text_bidi_override_options>`{.interpreted-text
role="ref"}

Returns the additional BiDi options set for this cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_suffix}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_suffix**(column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_suffix>`{.interpreted-text
role="ref"}

Gets the suffix string shown after the column value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_text**(column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_text>`{.interpreted-text
role="ref"}

Returns the given column\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_text_alignment}
::: rst-class
classref-method
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **get_text_alignment**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_text_alignment>`{.interpreted-text
role="ref"}

Returns the given column\'s text alignment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_text_direction}
::: rst-class
classref-method
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **get_text_direction**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_text_direction>`{.interpreted-text
role="ref"}

Returns item\'s text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_text_overrun_behavior}
::: rst-class
classref-method
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **get_text_overrun_behavior**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_text_overrun_behavior>`{.interpreted-text
role="ref"}

Returns the clipping behavior when the text exceeds the item\'s bounding
rectangle in the given `column`. By default it is
`TextServer.OVERRUN_TRIM_ELLIPSIS<class_TextServer_constant_OVERRUN_TRIM_ELLIPSIS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_tooltip_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tooltip_text**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_get_tooltip_text>`{.interpreted-text
role="ref"}

Returns the given column\'s tooltip text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_get_tree}
::: rst-class
classref-method
:::
::::

`Tree<class_Tree>`{.interpreted-text role="ref"} **get_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_get_tree>`{.interpreted-text
role="ref"}

Returns the `Tree<class_Tree>`{.interpreted-text role="ref"} that owns
this TreeItem.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_any_collapsed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_any_collapsed**(only_visible: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_TreeItem_method_is_any_collapsed>`{.interpreted-text
role="ref"}

Returns `true` if this **TreeItem**, or any of its descendants, is
collapsed.

If `only_visible` is `true` it ignores non-visible **TreeItem**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_button_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_button_disabled**(column: `int<class_int>`{.interpreted-text
role="ref"}, button_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_is_button_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the button at index `button_index` for the given
`column` is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_checked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_checked**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_is_checked>`{.interpreted-text
role="ref"}

Returns `true` if the given `column` is checked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_custom_set_as_button}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_custom_set_as_button**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_is_custom_set_as_button>`{.interpreted-text
role="ref"}

Returns `true` if the cell was made into a button with
`set_custom_as_button()<class_TreeItem_method_set_custom_as_button>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_edit_multiline}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_edit_multiline**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_is_edit_multiline>`{.interpreted-text
role="ref"}

Returns `true` if the given `column` is multiline editable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_editable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_editable**(column:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_is_editable>`{.interpreted-text role="ref"}

Returns `true` if the given `column` is editable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_indeterminate}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_indeterminate**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_is_indeterminate>`{.interpreted-text
role="ref"}

Returns `true` if the given `column` is indeterminate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_selectable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_selectable**(column: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TreeItem_method_is_selectable>`{.interpreted-text
role="ref"}

Returns `true` if the given `column` is selectable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_selected**(column:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_is_selected>`{.interpreted-text role="ref"}

Returns `true` if the given `column` is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_is_visible_in_tree}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_visible_in_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TreeItem_method_is_visible_in_tree>`{.interpreted-text
role="ref"}

Returns `true` if
`visible<class_TreeItem_property_visible>`{.interpreted-text role="ref"}
is `true` and all its ancestors are also visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_move_after}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_after**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}) `🔗<class_TreeItem_method_move_after>`{.interpreted-text
role="ref"}

Moves this TreeItem right after the given `item`.

\*\*Note:\*\* You can\'t move to the root or move the root.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_move_before}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_before**(item: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}) `🔗<class_TreeItem_method_move_before>`{.interpreted-text
role="ref"}

Moves this TreeItem right before the given `item`.

\*\*Note:\*\* You can\'t move to the root or move the root.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_propagate_check}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**propagate_check**(column: `int<class_int>`{.interpreted-text
role="ref"}, emit_signal: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_TreeItem_method_propagate_check>`{.interpreted-text
role="ref"}

Propagates this item\'s checked status to its children and parents for
the given `column`. It is possible to process the items affected by this
method call by connecting to
`Tree.check_propagated_to_item<class_Tree_signal_check_propagated_to_item>`{.interpreted-text
role="ref"}. The order that the items affected will be processed is as
follows: the item invoking this method, children of that item, and
finally parents of that item. If `emit_signal` is `false`, then
`Tree.check_propagated_to_item<class_Tree_signal_check_propagated_to_item>`{.interpreted-text
role="ref"} will not be emitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_remove_child}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_child**(child: `TreeItem<class_TreeItem>`{.interpreted-text
role="ref"}) `🔗<class_TreeItem_method_remove_child>`{.interpreted-text
role="ref"}

Removes the given child **TreeItem** and all its children from the
`Tree<class_Tree>`{.interpreted-text role="ref"}. Note that it doesn\'t
free the item from memory, so it can be reused later (see
`add_child()<class_TreeItem_method_add_child>`{.interpreted-text
role="ref"}). To completely remove a **TreeItem** use
`Object.free()<class_Object_method_free>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If you want to move a child from one
`Tree<class_Tree>`{.interpreted-text role="ref"} to another, then
instead of removing and adding it manually you can use
`move_before()<class_TreeItem_method_move_before>`{.interpreted-text
role="ref"} or
`move_after()<class_TreeItem_method_move_after>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_select}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select**(column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_select>`{.interpreted-text role="ref"}

Selects the given `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_auto_translate_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_auto_translate_mode**(column: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_auto_translate_mode>`{.interpreted-text
role="ref"}

Sets the given column\'s auto translate mode to `mode`.

All columns use
`Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>`{.interpreted-text
role="ref"} by default, which uses the same auto translate mode as the
`Tree<class_Tree>`{.interpreted-text role="ref"} itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_autowrap_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_autowrap_mode**(column: `int<class_int>`{.interpreted-text
role="ref"}, autowrap_mode:
`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_autowrap_mode>`{.interpreted-text
role="ref"}

Sets the autowrap mode in the given `column`. If set to something other
than
`TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`{.interpreted-text
role="ref"}, the text gets wrapped inside the cell\'s bounding
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_button}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_button**(column: `int<class_int>`{.interpreted-text role="ref"},
button_index: `int<class_int>`{.interpreted-text role="ref"}, button:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_button>`{.interpreted-text role="ref"}

Sets the given column\'s button
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} at index
`button_index` to `button`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_button_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_button_color**(column: `int<class_int>`{.interpreted-text
role="ref"}, button_index: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_button_color>`{.interpreted-text
role="ref"}

Sets the given column\'s button color at index `button_index` to
`color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_button_description}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_button_description**(column: `int<class_int>`{.interpreted-text
role="ref"}, button_index: `int<class_int>`{.interpreted-text
role="ref"}, description: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_button_description>`{.interpreted-text
role="ref"}

Sets the given column\'s button description at index `button_index` for
assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_button_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_button_disabled**(column: `int<class_int>`{.interpreted-text
role="ref"}, button_index: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_button_disabled>`{.interpreted-text
role="ref"}

If `true`, disables the button at index `button_index` in the given
`column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_button_tooltip_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_button_tooltip_text**(column: `int<class_int>`{.interpreted-text
role="ref"}, button_index: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_button_tooltip_text>`{.interpreted-text
role="ref"}

Sets the tooltip text for the button at index `button_index` in the
given `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_cell_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell_mode**(column: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`TreeCellMode<enum_TreeItem_TreeCellMode>`{.interpreted-text
role="ref"}) `🔗<class_TreeItem_method_set_cell_mode>`{.interpreted-text
role="ref"}

Sets the given column\'s cell mode to `mode`. This determines how the
cell is displayed and edited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_checked}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_checked**(column: `int<class_int>`{.interpreted-text role="ref"},
checked: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_checked>`{.interpreted-text role="ref"}

If `checked` is `true`, the given `column` is checked. Clears column\'s
indeterminate status.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_collapsed_recursive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collapsed_recursive**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_collapsed_recursive>`{.interpreted-text
role="ref"}

Collapses or uncollapses this **TreeItem** and all the descendants of
this item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_as_button}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_as_button**(column: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_custom_as_button>`{.interpreted-text
role="ref"}

Makes a cell with
`CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} display as a non-flat button with a
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_bg_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_bg_color**(column: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
just_outline: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_TreeItem_method_set_custom_bg_color>`{.interpreted-text
role="ref"}

Sets the given column\'s custom background color and whether to just use
it as an outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_color**(column: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_custom_color>`{.interpreted-text
role="ref"}

Sets the given column\'s custom color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_draw**(column: `int<class_int>`{.interpreted-text
role="ref"}, object: `Object<class_Object>`{.interpreted-text
role="ref"}, callback: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_custom_draw>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`set_custom_draw_callback()<class_TreeItem_method_set_custom_draw_callback>`{.interpreted-text
role="ref"} instead.

Sets the given column\'s custom draw callback to the `callback` method
on `object`.

The method named `callback` should accept two arguments: the
**TreeItem** that is drawn and its position and size as a
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_draw_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_draw_callback**(column: `int<class_int>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_custom_draw_callback>`{.interpreted-text
role="ref"}

Sets the given column\'s custom draw callback. Use an empty
`Callable<class_Callable>`{.interpreted-text role="ref"} (`Callable()`)
to clear the custom callback. The cell has to be in
`CELL_MODE_CUSTOM<class_TreeItem_constant_CELL_MODE_CUSTOM>`{.interpreted-text
role="ref"} to use this feature.

The `callback` should accept two arguments: the **TreeItem** that is
drawn and its position and size as a
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_font**(column: `int<class_int>`{.interpreted-text
role="ref"}, font: `Font<class_Font>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_custom_font>`{.interpreted-text
role="ref"}

Sets custom font used to draw text in the given `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_custom_font_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_font_size**(column: `int<class_int>`{.interpreted-text
role="ref"}, font_size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_custom_font_size>`{.interpreted-text
role="ref"}

Sets custom font size used to draw text in the given `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_description}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_description**(column: `int<class_int>`{.interpreted-text
role="ref"}, description: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_description>`{.interpreted-text
role="ref"}

Sets the given column\'s description for assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_edit_multiline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_edit_multiline**(column: `int<class_int>`{.interpreted-text
role="ref"}, multiline: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_edit_multiline>`{.interpreted-text
role="ref"}

If `multiline` is `true`, the given `column` is multiline editable.

\*\*Note:\*\* This option only affects the type of control
(`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} or
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}) that appears
when editing the column. You can set multiline values with
`set_text()<class_TreeItem_method_set_text>`{.interpreted-text
role="ref"} even if the column is not multiline editable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_editable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_editable**(column: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_editable>`{.interpreted-text role="ref"}

If `enabled` is `true`, the given `column` is editable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_expand_right}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_expand_right**(column: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_expand_right>`{.interpreted-text
role="ref"}

If `enable` is `true`, the given `column` is expanded to the right.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon**(column: `int<class_int>`{.interpreted-text role="ref"},
texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_icon>`{.interpreted-text role="ref"}

Sets the given cell\'s icon
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}. If the cell
is in
`CELL_MODE_ICON<class_TreeItem_constant_CELL_MODE_ICON>`{.interpreted-text
role="ref"} mode, the icon is displayed in the center of the cell.
Otherwise, the icon is displayed before the cell\'s text.
`CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"} does not display an icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_icon_max_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon_max_width**(column: `int<class_int>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_icon_max_width>`{.interpreted-text
role="ref"}

Sets the maximum allowed width of the icon in the given `column`. This
limit is applied on top of the default size of the icon and on top of
`Tree.icon_max_width<class_Tree_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_icon_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon_modulate**(column: `int<class_int>`{.interpreted-text
role="ref"}, modulate: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_icon_modulate>`{.interpreted-text
role="ref"}

Modulates the given column\'s icon with `modulate`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_icon_overlay}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon_overlay**(column: `int<class_int>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_icon_overlay>`{.interpreted-text
role="ref"}

Sets the given cell\'s icon overlay
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}. The cell has
to be in
`CELL_MODE_ICON<class_TreeItem_constant_CELL_MODE_ICON>`{.interpreted-text
role="ref"} mode, and icon has to be set. Overlay is drawn on top of
icon, in the bottom left corner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_icon_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon_region**(column: `int<class_int>`{.interpreted-text
role="ref"}, region: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_icon_region>`{.interpreted-text
role="ref"}

Sets the given column\'s icon\'s texture region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_indeterminate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_indeterminate**(column: `int<class_int>`{.interpreted-text
role="ref"}, indeterminate: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_indeterminate>`{.interpreted-text
role="ref"}

If `indeterminate` is `true`, the given `column` is marked
indeterminate.

\*\*Note:\*\* If set `true` from `false`, then column is cleared of
checked status.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_language}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_language**(column: `int<class_int>`{.interpreted-text role="ref"},
language: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_language>`{.interpreted-text role="ref"}

Sets language code of item\'s text used for line-breaking and text
shaping algorithms, if left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_metadata**(column: `int<class_int>`{.interpreted-text role="ref"},
meta: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_metadata>`{.interpreted-text role="ref"}

Sets the metadata value for the given column, which can be retrieved
later using
`get_metadata()<class_TreeItem_method_get_metadata>`{.interpreted-text
role="ref"}. This can be used, for example, to store a reference to the
original data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_range**(column: `int<class_int>`{.interpreted-text role="ref"},
value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_range>`{.interpreted-text role="ref"}

Sets the value of a
`CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"} column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_range_config}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_range_config**(column: `int<class_int>`{.interpreted-text
role="ref"}, min: `float<class_float>`{.interpreted-text role="ref"},
max: `float<class_float>`{.interpreted-text role="ref"}, step:
`float<class_float>`{.interpreted-text role="ref"}, expr:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_TreeItem_method_set_range_config>`{.interpreted-text
role="ref"}

Sets the range of accepted values for a column. The column must be in
the
`CELL_MODE_RANGE<class_TreeItem_constant_CELL_MODE_RANGE>`{.interpreted-text
role="ref"} mode.

If `expr` is `true`, the edit mode slider will use an exponential scale
as with
`Range.exp_edit<class_Range_property_exp_edit>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_selectable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selectable**(column: `int<class_int>`{.interpreted-text
role="ref"}, selectable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_selectable>`{.interpreted-text role="ref"}

If `selectable` is `true`, the given `column` is selectable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_structured_text_bidi_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_structured_text_bidi_override**(column:
`int<class_int>`{.interpreted-text role="ref"}, parser:
`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_structured_text_bidi_override>`{.interpreted-text
role="ref"}

Set BiDi algorithm override for the structured text. Has effect for
cells that display text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_structured_text_bidi_override_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_structured_text_bidi_override_options**(column:
`int<class_int>`{.interpreted-text role="ref"}, args:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_structured_text_bidi_override_options>`{.interpreted-text
role="ref"}

Set additional options for BiDi override. Has effect for cells that
display text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_suffix}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_suffix**(column: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_suffix>`{.interpreted-text role="ref"}

Sets a string to be shown after a column\'s value (for example, a unit
abbreviation).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_text**(column: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TreeItem_method_set_text>`{.interpreted-text role="ref"}

Sets the given column\'s text value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_text_alignment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_text_alignment**(column: `int<class_int>`{.interpreted-text
role="ref"}, text_alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_text_alignment>`{.interpreted-text
role="ref"}

Sets the given column\'s text alignment to `text_alignment`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_text_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_text_direction**(column: `int<class_int>`{.interpreted-text
role="ref"}, direction:
`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_text_direction>`{.interpreted-text
role="ref"}

Sets item\'s text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_text_overrun_behavior}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_text_overrun_behavior**(column: `int<class_int>`{.interpreted-text
role="ref"}, overrun_behavior:
`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_text_overrun_behavior>`{.interpreted-text
role="ref"}

Sets the clipping behavior when the text exceeds the item\'s bounding
rectangle in the given `column`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_set_tooltip_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tooltip_text**(column: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TreeItem_method_set_tooltip_text>`{.interpreted-text
role="ref"}

Sets the given column\'s tooltip text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TreeItem_method_uncollapse_tree}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**uncollapse_tree**()
`🔗<class_TreeItem_method_uncollapse_tree>`{.interpreted-text
role="ref"}

Uncollapses all **TreeItem**s necessary to reveal this **TreeItem**,
i.e. all ancestor **TreeItem**s.
