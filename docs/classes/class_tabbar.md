github_url
:   hide

# TabBar {#class_TabBar}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control that provides a horizontal bar with tabs.

::: rst-class
classref-introduction-group
:::

## Description

A control that provides a horizontal bar with tabs. Similar to
`TabContainer<class_TabContainer>`{.interpreted-text role="ref"} but is
only in charge of drawing tabs, not interacting with children.

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

:::: {#class_TabBar_signal_active_tab_rearranged}
::: rst-class
classref-signal
:::
::::

**active_tab_rearranged**(idx_to: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_signal_active_tab_rearranged>`{.interpreted-text
role="ref"}

Emitted when the active tab is rearranged via mouse drag. See
`drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_button_pressed}
::: rst-class
classref-signal
:::
::::

**tab_button_pressed**(tab: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_signal_tab_button_pressed>`{.interpreted-text
role="ref"}

Emitted when a tab\'s right button is pressed. See
`set_tab_button_icon()<class_TabBar_method_set_tab_button_icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_changed}
::: rst-class
classref-signal
:::
::::

**tab_changed**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_signal_tab_changed>`{.interpreted-text role="ref"}

Emitted when switching to another tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_clicked}
::: rst-class
classref-signal
:::
::::

**tab_clicked**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_signal_tab_clicked>`{.interpreted-text role="ref"}

Emitted when a tab is clicked, even if it is the current tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_close_pressed}
::: rst-class
classref-signal
:::
::::

**tab_close_pressed**(tab: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_signal_tab_close_pressed>`{.interpreted-text
role="ref"}

Emitted when a tab\'s close button is pressed or when middle-clicking on
a tab, if
`close_with_middle_mouse<class_TabBar_property_close_with_middle_mouse>`{.interpreted-text
role="ref"} is enabled.

\*\*Note:\*\* Tabs are not removed automatically once the close button
is pressed, this behavior needs to be programmed manually. For example:

::::: tabs
::: code-tab
gdscript

\$TabBar.tab_close_pressed.connect(\$TabBar.remove_tab)
:::

::: code-tab
csharp

GetNode\<TabBar\>(\"TabBar\").TabClosePressed +=
GetNode\<TabBar\>(\"TabBar\").RemoveTab;
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_hovered}
::: rst-class
classref-signal
:::
::::

**tab_hovered**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_signal_tab_hovered>`{.interpreted-text role="ref"}

Emitted when a tab is hovered by the mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_rmb_clicked}
::: rst-class
classref-signal
:::
::::

**tab_rmb_clicked**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_signal_tab_rmb_clicked>`{.interpreted-text role="ref"}

Emitted when a tab is right-clicked.
`select_with_rmb<class_TabBar_property_select_with_rmb>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_signal_tab_selected}
::: rst-class
classref-signal
:::
::::

**tab_selected**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_signal_tab_selected>`{.interpreted-text role="ref"}

Emitted when a tab is selected via click, directional input, or script,
even if it is the current tab.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_TabBar_AlignmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlignmentMode**:
`🔗<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}

:::: {#class_TabBar_constant_ALIGNMENT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
**ALIGNMENT_LEFT** = `0`

Places tabs to the left.

:::: {#class_TabBar_constant_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
**ALIGNMENT_CENTER** = `1`

Places tabs in the middle.

:::: {#class_TabBar_constant_ALIGNMENT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
**ALIGNMENT_RIGHT** = `2`

Places tabs to the right.

:::: {#class_TabBar_constant_ALIGNMENT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
**ALIGNMENT_MAX** = `3`

Represents the size of the
`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TabBar_CloseButtonDisplayPolicy}
::: rst-class
classref-enumeration
:::
::::

enum **CloseButtonDisplayPolicy**:
`🔗<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text role="ref"}

:::: {#class_TabBar_constant_CLOSE_BUTTON_SHOW_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
role="ref"} **CLOSE_BUTTON_SHOW_NEVER** = `0`

Never show the close buttons.

:::: {#class_TabBar_constant_CLOSE_BUTTON_SHOW_ACTIVE_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
role="ref"} **CLOSE_BUTTON_SHOW_ACTIVE_ONLY** = `1`

Only show the close button on the currently active tab.

:::: {#class_TabBar_constant_CLOSE_BUTTON_SHOW_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
role="ref"} **CLOSE_BUTTON_SHOW_ALWAYS** = `2`

Show the close button on all tabs.

:::: {#class_TabBar_constant_CLOSE_BUTTON_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
role="ref"} **CLOSE_BUTTON_MAX** = `3`

Represents the size of the
`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TabBar_property_clip_tabs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **clip_tabs** = `true`
`🔗<class_TabBar_property_clip_tabs>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clip_tabs**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_clip_tabs**()

If `true`, tabs overflowing this node\'s width will be hidden,
displaying two navigation buttons instead. Otherwise, this node\'s
minimum size is updated so that all tabs are visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_close_with_middle_mouse}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**close_with_middle_mouse** = `true`
`🔗<class_TabBar_property_close_with_middle_mouse>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_close_with_middle_mouse**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_close_with_middle_mouse**()

If `true`, middle clicking on the mouse will fire the
`tab_close_pressed<class_TabBar_signal_tab_close_pressed>`{.interpreted-text
role="ref"} signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_current_tab}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **current_tab** = `-1`
`🔗<class_TabBar_property_current_tab>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_tab**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_current_tab**()

The index of the current selected tab. A value of `-1` means that no tab
is selected and can only be set when
`deselect_enabled<class_TabBar_property_deselect_enabled>`{.interpreted-text
role="ref"} is `true` or if all tabs are hidden or disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_deselect_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **deselect_enabled** =
`false` `🔗<class_TabBar_property_deselect_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_deselect_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_deselect_enabled**()

If `true`, all tabs can be deselected so that no tab is selected. Click
on the current tab to deselect it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_drag_to_rearrange_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_to_rearrange_enabled** = `false`
`🔗<class_TabBar_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_to_rearrange_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_drag_to_rearrange_enabled**()

If `true`, tabs can be rearranged with mouse drag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_max_tab_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_tab_width** = `0`
`🔗<class_TabBar_property_max_tab_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_tab_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_tab_width**()

Sets the maximum width which all tabs should be limited to. Unlimited if
set to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_scroll_to_selected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **scroll_to_selected**
= `true`
`🔗<class_TabBar_property_scroll_to_selected>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_to_selected**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_scroll_to_selected**()

If `true`, the tab offset will be changed to keep the currently selected
tab visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_scrolling_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **scrolling_enabled** =
`true` `🔗<class_TabBar_property_scrolling_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scrolling_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_scrolling_enabled**()

if `true`, the mouse\'s scroll wheel can be used to navigate the scroll
view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_select_with_rmb}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **select_with_rmb** =
`false` `🔗<class_TabBar_property_select_with_rmb>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_select_with_rmb**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_select_with_rmb**()

If `true`, enables selecting a tab with the right mouse button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_tab_alignment}
::: rst-class
classref-property
:::
::::

`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
**tab_alignment** = `0`
`🔗<class_TabBar_property_tab_alignment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_alignment**(value:
  `AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text
  role="ref"})
- `AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text
  role="ref"} **get_tab_alignment**()

The position at which tabs will be placed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_tab_close_display_policy}
::: rst-class
classref-property
:::
::::

`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
role="ref"} **tab_close_display_policy** = `0`
`🔗<class_TabBar_property_tab_close_display_policy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_close_display_policy**(value:
  `CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
  role="ref"})
- `CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>`{.interpreted-text
  role="ref"} **get_tab_close_display_policy**()

When the close button will appear on the tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_tab_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tab_count** = `0`
`🔗<class_TabBar_property_tab_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_tab_count**()

The number of tabs currently in the bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_property_tabs_rearrange_group}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tabs_rearrange_group**
= `-1`
`🔗<class_TabBar_property_tabs_rearrange_group>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tabs_rearrange_group**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_tabs_rearrange_group**()

**TabBar**s with the same rearrange group ID will allow dragging the
tabs between them. Enable drag with
`drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}.

Setting this to `-1` will disable rearranging between **TabBar**s.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TabBar_method_add_tab}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_tab**(title: `String<class_String>`{.interpreted-text role="ref"}
= \"\", icon: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
= null) `🔗<class_TabBar_method_add_tab>`{.interpreted-text role="ref"}

Adds a new tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_clear_tabs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_tabs**() `🔗<class_TabBar_method_clear_tabs>`{.interpreted-text
role="ref"}

Clears all tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_ensure_tab_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**ensure_tab_visible**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_method_ensure_tab_visible>`{.interpreted-text
role="ref"}

Moves the scroll view to make the tab visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_offset_buttons_visible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_offset_buttons_visible**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_offset_buttons_visible>`{.interpreted-text
role="ref"}

Returns `true` if the offset buttons (the ones that appear when there\'s
not enough space for all tabs) are visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_previous_tab}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_previous_tab**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_previous_tab>`{.interpreted-text role="ref"}

Returns the previously active tab index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_button_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_tab_button_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_tab_button_icon>`{.interpreted-text
role="ref"}

Returns the icon for the right button of the tab at index `tab_idx` or
`null` if the right button has no icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_tab_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_get_tab_icon>`{.interpreted-text
role="ref"}

Returns the icon for the tab at index `tab_idx` or `null` if the tab has
no icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_icon_max_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tab_icon_max_width**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_tab_icon_max_width>`{.interpreted-text
role="ref"}

Returns the maximum allowed width of the icon for the tab at index
`tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_idx_at_point}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tab_idx_at_point**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_tab_idx_at_point>`{.interpreted-text
role="ref"}

Returns the index of the tab at local coordinates `point`. Returns `-1`
if the point is outside the control boundaries or if there\'s no tab at
the queried position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tab_language**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_tab_language>`{.interpreted-text role="ref"}

Returns tab title language code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_tab_metadata**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_tab_metadata>`{.interpreted-text role="ref"}

Returns the metadata value set to the tab at index `tab_idx` using
`set_tab_metadata()<class_TabBar_method_set_tab_metadata>`{.interpreted-text
role="ref"}. If no metadata was previously set, returns `null` by
default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_offset}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_tab_offset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_get_tab_offset>`{.interpreted-text
role="ref"}

Returns the number of hidden tabs offsetted to the left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_tab_rect**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_get_tab_rect>`{.interpreted-text
role="ref"}

Returns tab `Rect2<class_Rect2>`{.interpreted-text role="ref"} with
local position and size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_text_direction}
::: rst-class
classref-method
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **get_tab_text_direction**(tab_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabBar_method_get_tab_text_direction>`{.interpreted-text
role="ref"}

Returns tab title text base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_title}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tab_title**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_get_tab_title>`{.interpreted-text
role="ref"}

Returns the title of the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_get_tab_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tab_tooltip**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_get_tab_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip text of the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_is_tab_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_tab_disabled**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_is_tab_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the tab at index `tab_idx` is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_is_tab_hidden}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_tab_hidden**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabBar_method_is_tab_hidden>`{.interpreted-text
role="ref"}

Returns `true` if the tab at index `tab_idx` is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_move_tab}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_tab**(from: `int<class_int>`{.interpreted-text role="ref"}, to:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_method_move_tab>`{.interpreted-text role="ref"}

Moves a tab from `from` to `to`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_remove_tab}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_tab**(tab_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_method_remove_tab>`{.interpreted-text role="ref"}

Removes the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_select_next_available}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**select_next_available**()
`🔗<class_TabBar_method_select_next_available>`{.interpreted-text
role="ref"}

Selects the first available tab with greater index than the currently
selected. Returns `true` if tab selection changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_select_previous_available}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**select_previous_available**()
`🔗<class_TabBar_method_select_previous_available>`{.interpreted-text
role="ref"}

Selects the first available tab with lower index than the currently
selected. Returns `true` if tab selection changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_button_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_button_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_method_set_tab_button_icon>`{.interpreted-text
role="ref"}

Sets an `icon` for the button of the tab at index `tab_idx` (located to
the right, before the close button), making it visible and clickable
(See
`tab_button_pressed<class_TabBar_signal_tab_button_pressed>`{.interpreted-text
role="ref"}). Giving it a `null` value will hide the button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_disabled**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TabBar_method_set_tab_disabled>`{.interpreted-text role="ref"}

If `disabled` is `true`, disables the tab at index `tab_idx`, making it
non-interactable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_hidden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_hidden**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, hidden: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TabBar_method_set_tab_hidden>`{.interpreted-text role="ref"}

If `hidden` is `true`, hides the tab at index `tab_idx`, making it
disappear from the tab area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}) `🔗<class_TabBar_method_set_tab_icon>`{.interpreted-text
role="ref"}

Sets an `icon` for the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_icon_max_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_icon_max_width**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabBar_method_set_tab_icon_max_width>`{.interpreted-text
role="ref"}

Sets the maximum allowed width of the icon for the tab at index
`tab_idx`. This limit is applied on top of the default size of the icon
and on top of
`icon_max_width<class_TabBar_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_language}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_language**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_method_set_tab_language>`{.interpreted-text role="ref"}

Sets language code of tab title used for line-breaking and text shaping
algorithms, if left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_metadata**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, metadata: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_method_set_tab_metadata>`{.interpreted-text role="ref"}

Sets the metadata value for the tab at index `tab_idx`, which can be
retrieved later using
`get_tab_metadata()<class_TabBar_method_get_tab_metadata>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_text_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_text_direction**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, direction:
`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"})
`🔗<class_TabBar_method_set_tab_text_direction>`{.interpreted-text
role="ref"}

Sets tab title base writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_title}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_title**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, title: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_TabBar_method_set_tab_title>`{.interpreted-text
role="ref"}

Sets a `title` for the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_method_set_tab_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_tooltip**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_TabBar_method_set_tab_tooltip>`{.interpreted-text
role="ref"}

Sets a `tooltip` for tab at index `tab_idx`.

\*\*Note:\*\* By default, if the `tooltip` is empty and the tab text is
truncated (not all characters fit into the tab), the title will be
displayed as a tooltip. To hide the tooltip, assign `" "` as the
`tooltip` text.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_TabBar_theme_color_drop_mark_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **drop_mark_color** =
`Color(1, 1, 1, 1)`
`🔗<class_TabBar_theme_color_drop_mark_color>`{.interpreted-text
role="ref"}

Modulation color for the
`drop_mark<class_TabBar_theme_icon_drop_mark>`{.interpreted-text
role="ref"} icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_TabBar_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

Font color of disabled tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_color_font_hovered_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_TabBar_theme_color_font_hovered_color>`{.interpreted-text
role="ref"}

Font color of the currently hovered tab. Does not apply to the selected
tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_TabBar_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the tab name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_TabBar_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

Font color of the currently selected tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_color_font_unselected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)`
`🔗<class_TabBar_theme_color_font_unselected_color>`{.interpreted-text
role="ref"}

Font color of the other, unselected tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_TabBar_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal separation between the elements inside tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_constant_icon_max_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_max_width** = `0`
`🔗<class_TabBar_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}

The maximum allowed width of the tab\'s icon. This limit is applied on
top of the default size of the icon, but before the value set with
`set_tab_icon_max_width()<class_TabBar_method_set_tab_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_TabBar_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the tab text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_TabBar_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_constant_tab_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tab_separation** = `0`
`🔗<class_TabBar_theme_constant_tab_separation>`{.interpreted-text
role="ref"}

The space between tabs in the tab bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_TabBar_theme_font_font>`{.interpreted-text role="ref"}

The font used to draw tab names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_TabBar_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the tab names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_icon_close}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **close**
`🔗<class_TabBar_theme_icon_close>`{.interpreted-text role="ref"}

The icon for the close button (see
`tab_close_display_policy<class_TabBar_property_tab_close_display_policy>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_icon_decrement}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **decrement**
`🔗<class_TabBar_theme_icon_decrement>`{.interpreted-text role="ref"}

Icon for the left arrow button that appears when there are too many tabs
to fit in the container width. When the button is disabled (i.e. the
first tab is visible), it appears semi-transparent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_icon_decrement_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**decrement_highlight**
`🔗<class_TabBar_theme_icon_decrement_highlight>`{.interpreted-text
role="ref"}

Icon for the left arrow button that appears when there are too many tabs
to fit in the container width. Used when the button is being hovered
with the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_icon_drop_mark}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **drop_mark**
`🔗<class_TabBar_theme_icon_drop_mark>`{.interpreted-text role="ref"}

Icon shown to indicate where a dragged tab is gonna be dropped (see
`drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_icon_increment}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **increment**
`🔗<class_TabBar_theme_icon_increment>`{.interpreted-text role="ref"}

Icon for the right arrow button that appears when there are too many
tabs to fit in the container width. When the button is disabled (i.e.
the last tab is visible) it appears semi-transparent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_icon_increment_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**increment_highlight**
`🔗<class_TabBar_theme_icon_increment_highlight>`{.interpreted-text
role="ref"}

Icon for the right arrow button that appears when there are too many
tabs to fit in the container width. Used when the button is being
hovered with the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_button_highlight}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**button_highlight**
`🔗<class_TabBar_theme_style_button_highlight>`{.interpreted-text
role="ref"}

Background of the tab and close buttons when they\'re being hovered with
the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_button_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**button_pressed**
`🔗<class_TabBar_theme_style_button_pressed>`{.interpreted-text
role="ref"}

Background of the tab and close buttons when it\'s being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_tab_disabled}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tab_disabled**
`🔗<class_TabBar_theme_style_tab_disabled>`{.interpreted-text
role="ref"}

The style of disabled tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_tab_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **tab_focus**
`🔗<class_TabBar_theme_style_tab_focus>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**TabBar** is focused. The
`tab_focus<class_TabBar_theme_style_tab_focus>`{.interpreted-text
role="ref"} `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} is
displayed *over* the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} of the selected tab, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} remains visible. A
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that represents
an outline or an underline works well for this purpose. To disable the
focus visual effect, assign a
`StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text role="ref"}
resource. Note that disabling the focus visual effect will harm
keyboard/controller navigation usability, so this is not recommended for
accessibility reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_tab_hovered}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **tab_hovered**
`🔗<class_TabBar_theme_style_tab_hovered>`{.interpreted-text role="ref"}

The style of the currently hovered tab. Does not apply to the selected
tab.

\*\*Note:\*\* This style will be drawn with the same width as
`tab_unselected<class_TabBar_theme_style_tab_unselected>`{.interpreted-text
role="ref"} at minimum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_tab_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tab_selected**
`🔗<class_TabBar_theme_style_tab_selected>`{.interpreted-text
role="ref"}

The style of the currently selected tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabBar_theme_style_tab_unselected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tab_unselected**
`🔗<class_TabBar_theme_style_tab_unselected>`{.interpreted-text
role="ref"}

The style of the other, unselected tabs.
