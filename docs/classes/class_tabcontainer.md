github_url
:   hide

# TabContainer {#class_TabContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A container that creates a tab for each child control, displaying only
the active tab\'s control.

::: rst-class
classref-introduction-group
:::

## Description

Arranges child controls into a tabbed view, creating a tab for each one.
The active tab\'s corresponding control is made visible, while all other
child controls are hidden. Ignores non-control children.

\*\*Note:\*\* The drawing of the clickable tabs is handled by this node;
`TabBar<class_TabBar>`{.interpreted-text role="ref"} is not needed.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`{.interpreted-text
  role="doc"}

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

:::: {#class_TabContainer_signal_active_tab_rearranged}
::: rst-class
classref-signal
:::
::::

**active_tab_rearranged**(idx_to: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_signal_active_tab_rearranged>`{.interpreted-text
role="ref"}

Emitted when the active tab is rearranged via mouse drag. See
`drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_signal_pre_popup_pressed}
::: rst-class
classref-signal
:::
::::

**pre_popup_pressed**()
`🔗<class_TabContainer_signal_pre_popup_pressed>`{.interpreted-text
role="ref"}

Emitted when the **TabContainer**\'s
`Popup<class_Popup>`{.interpreted-text role="ref"} button is clicked.
See `set_popup()<class_TabContainer_method_set_popup>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_signal_tab_button_pressed}
::: rst-class
classref-signal
:::
::::

**tab_button_pressed**(tab: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_signal_tab_button_pressed>`{.interpreted-text
role="ref"}

Emitted when the user clicks on the button icon on this tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_signal_tab_changed}
::: rst-class
classref-signal
:::
::::

**tab_changed**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_signal_tab_changed>`{.interpreted-text
role="ref"}

Emitted when switching to another tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_signal_tab_clicked}
::: rst-class
classref-signal
:::
::::

**tab_clicked**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_signal_tab_clicked>`{.interpreted-text
role="ref"}

Emitted when a tab is clicked, even if it is the current tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_signal_tab_hovered}
::: rst-class
classref-signal
:::
::::

**tab_hovered**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_signal_tab_hovered>`{.interpreted-text
role="ref"}

Emitted when a tab is hovered by the mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_signal_tab_selected}
::: rst-class
classref-signal
:::
::::

**tab_selected**(tab: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_signal_tab_selected>`{.interpreted-text
role="ref"}

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

:::: {#enum_TabContainer_TabPosition}
::: rst-class
classref-enumeration
:::
::::

enum **TabPosition**:
`🔗<enum_TabContainer_TabPosition>`{.interpreted-text role="ref"}

:::: {#class_TabContainer_constant_POSITION_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
role="ref"} **POSITION_TOP** = `0`

Places the tab bar at the top.

:::: {#class_TabContainer_constant_POSITION_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
role="ref"} **POSITION_BOTTOM** = `1`

Places the tab bar at the bottom. The tab bar\'s
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} will be flipped
vertically.

:::: {#class_TabContainer_constant_POSITION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
role="ref"} **POSITION_MAX** = `2`

Represents the size of the
`TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TabContainer_property_all_tabs_in_front}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **all_tabs_in_front** =
`false`
`🔗<class_TabContainer_property_all_tabs_in_front>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_all_tabs_in_front**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_all_tabs_in_front**()

If `true`, all tabs are drawn in front of the panel. If `false`,
inactive tabs are drawn behind the panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_clip_tabs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **clip_tabs** = `true`
`🔗<class_TabContainer_property_clip_tabs>`{.interpreted-text
role="ref"}

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

:::: {#class_TabContainer_property_current_tab}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **current_tab** = `-1`
`🔗<class_TabContainer_property_current_tab>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_tab**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_current_tab**()

The current tab index. When set, this index\'s
`Control<class_Control>`{.interpreted-text role="ref"} node\'s `visible`
property is set to `true` and all others are set to `false`.

A value of `-1` means that no tab is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_deselect_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **deselect_enabled** =
`false`
`🔗<class_TabContainer_property_deselect_enabled>`{.interpreted-text
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
on the
`current_tab<class_TabContainer_property_current_tab>`{.interpreted-text
role="ref"} to deselect it.

Only the tab header will be shown if no tabs are selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_drag_to_rearrange_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_to_rearrange_enabled** = `false`
`🔗<class_TabContainer_property_drag_to_rearrange_enabled>`{.interpreted-text
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

:::: {#class_TabContainer_property_tab_alignment}
::: rst-class
classref-property
:::
::::

`AlignmentMode<enum_TabBar_AlignmentMode>`{.interpreted-text role="ref"}
**tab_alignment** = `0`
`🔗<class_TabContainer_property_tab_alignment>`{.interpreted-text
role="ref"}

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

:::: {#class_TabContainer_property_tab_focus_mode}
::: rst-class
classref-property
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**tab_focus_mode** = `2`
`🔗<class_TabContainer_property_tab_focus_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_focus_mode**(value:
  `FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"})
- `FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
  **get_tab_focus_mode**()

The focus access mode for the internal
`TabBar<class_TabBar>`{.interpreted-text role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_tabs_position}
::: rst-class
classref-property
:::
::::

`TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
role="ref"} **tabs_position** = `0`
`🔗<class_TabContainer_property_tabs_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tabs_position**(value:
  `TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
  role="ref"})
- `TabPosition<enum_TabContainer_TabPosition>`{.interpreted-text
  role="ref"} **get_tabs_position**()

The position of the tab bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_tabs_rearrange_group}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tabs_rearrange_group**
= `-1`
`🔗<class_TabContainer_property_tabs_rearrange_group>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tabs_rearrange_group**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_tabs_rearrange_group**()

**TabContainer**s with the same rearrange group ID will allow dragging
the tabs between them. Enable drag with
`drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}.

Setting this to `-1` will disable rearranging between **TabContainer**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_tabs_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tabs_visible** =
`true` `🔗<class_TabContainer_property_tabs_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tabs_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_tabs_visible**()

If `true`, tabs are visible. If `false`, tabs\' content and titles are
hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_property_use_hidden_tabs_for_min_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_hidden_tabs_for_min_size** = `false`
`🔗<class_TabContainer_property_use_hidden_tabs_for_min_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_hidden_tabs_for_min_size**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_hidden_tabs_for_min_size**()

If `true`, child `Control<class_Control>`{.interpreted-text role="ref"}
nodes that are hidden have their minimum size take into account in the
total, instead of only the currently visible one.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TabContainer_method_get_current_tab_control}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**get_current_tab_control**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_current_tab_control>`{.interpreted-text
role="ref"}

Returns the child `Control<class_Control>`{.interpreted-text role="ref"}
node located at the active tab index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_popup}
::: rst-class
classref-method
:::
::::

`Popup<class_Popup>`{.interpreted-text role="ref"} **get_popup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TabContainer_method_get_popup>`{.interpreted-text
role="ref"}

Returns the `Popup<class_Popup>`{.interpreted-text role="ref"} node
instance if one has been set already with
`set_popup()<class_TabContainer_method_set_popup>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their `Window.visible<class_Window_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_previous_tab}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_previous_tab**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_previous_tab>`{.interpreted-text
role="ref"}

Returns the previously active tab index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_bar}
::: rst-class
classref-method
:::
::::

`TabBar<class_TabBar>`{.interpreted-text role="ref"} **get_tab_bar**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_bar>`{.interpreted-text
role="ref"}

Returns the `TabBar<class_TabBar>`{.interpreted-text role="ref"}
contained in this container.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it or editing its tabs may cause a crash. If you wish to edit the tabs,
use the methods provided in **TabContainer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_button_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_tab_button_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_button_icon>`{.interpreted-text
role="ref"}

Returns the button icon from the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_control}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**get_tab_control**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_control>`{.interpreted-text
role="ref"}

Returns the `Control<class_Control>`{.interpreted-text role="ref"} node
from the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_tab_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_count>`{.interpreted-text
role="ref"}

Returns the number of tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_tab_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_icon>`{.interpreted-text
role="ref"}

Returns the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
for the tab at index `tab_idx` or `null` if the tab has no
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_icon_max_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tab_icon_max_width**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_icon_max_width>`{.interpreted-text
role="ref"}

Returns the maximum allowed width of the icon for the tab at index
`tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_idx_at_point}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tab_idx_at_point**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_idx_at_point>`{.interpreted-text
role="ref"}

Returns the index of the tab at local coordinates `point`. Returns `-1`
if the point is outside the control boundaries or if there\'s no tab at
the queried position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_idx_from_control}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tab_idx_from_control**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_idx_from_control>`{.interpreted-text
role="ref"}

Returns the index of the tab tied to the given `control`. The control
must be a child of the **TabContainer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_tab_metadata**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_metadata>`{.interpreted-text
role="ref"}

Returns the metadata value set to the tab at index `tab_idx` using
`set_tab_metadata()<class_TabContainer_method_set_tab_metadata>`{.interpreted-text
role="ref"}. If no metadata was previously set, returns `null` by
default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_title}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tab_title**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_title>`{.interpreted-text
role="ref"}

Returns the title of the tab at index `tab_idx`. Tab titles default to
the name of the indexed child node, but this can be overridden with
`set_tab_title()<class_TabContainer_method_set_tab_title>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_get_tab_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tab_tooltip**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_get_tab_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip text of the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_is_tab_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_tab_disabled**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_is_tab_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the tab at index `tab_idx` is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_is_tab_hidden}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_tab_hidden**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TabContainer_method_is_tab_hidden>`{.interpreted-text
role="ref"}

Returns `true` if the tab at index `tab_idx` is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_select_next_available}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**select_next_available**()
`🔗<class_TabContainer_method_select_next_available>`{.interpreted-text
role="ref"}

Selects the first available tab with greater index than the currently
selected. Returns `true` if tab selection changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_select_previous_available}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**select_previous_available**()
`🔗<class_TabContainer_method_select_previous_available>`{.interpreted-text
role="ref"}

Selects the first available tab with lower index than the currently
selected. Returns `true` if tab selection changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_popup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_popup**(popup: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_method_set_popup>`{.interpreted-text role="ref"}

If set on a `Popup<class_Popup>`{.interpreted-text role="ref"} node
instance, a popup menu icon appears in the top-right corner of the
**TabContainer** (setting it to `null` will make it go away). Clicking
it will expand the `Popup<class_Popup>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_button_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_button_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_method_set_tab_button_icon>`{.interpreted-text
role="ref"}

Sets the button icon from the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_disabled**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_method_set_tab_disabled>`{.interpreted-text
role="ref"}

If `disabled` is `true`, disables the tab at index `tab_idx`, making it
non-interactable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_hidden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_hidden**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, hidden: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_method_set_tab_hidden>`{.interpreted-text
role="ref"}

If `hidden` is `true`, hides the tab at index `tab_idx`, making it
disappear from the tab area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_icon**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_method_set_tab_icon>`{.interpreted-text
role="ref"}

Sets an icon for the tab at index `tab_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_icon_max_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_icon_max_width**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TabContainer_method_set_tab_icon_max_width>`{.interpreted-text
role="ref"}

Sets the maximum allowed width of the icon for the tab at index
`tab_idx`. This limit is applied on top of the default size of the icon
and on top of
`icon_max_width<class_TabContainer_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_metadata**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, metadata: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_method_set_tab_metadata>`{.interpreted-text
role="ref"}

Sets the metadata value for the tab at index `tab_idx`, which can be
retrieved later using
`get_tab_metadata()<class_TabContainer_method_get_tab_metadata>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_title}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_title**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, title: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_method_set_tab_title>`{.interpreted-text
role="ref"}

Sets a custom title for the tab at index `tab_idx` (tab titles default
to the name of the indexed child node). Set it back to the child\'s name
to make the tab default to it again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_method_set_tab_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_tooltip**(tab_idx: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TabContainer_method_set_tab_tooltip>`{.interpreted-text
role="ref"}

Sets a custom tooltip text for tab at index `tab_idx`.

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

:::: {#class_TabContainer_theme_color_drop_mark_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **drop_mark_color** =
`Color(1, 1, 1, 1)`
`🔗<class_TabContainer_theme_color_drop_mark_color>`{.interpreted-text
role="ref"}

Modulation color for the
`drop_mark<class_TabContainer_theme_icon_drop_mark>`{.interpreted-text
role="ref"} icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_TabContainer_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

Font color of disabled tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_color_font_hovered_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_TabContainer_theme_color_font_hovered_color>`{.interpreted-text
role="ref"}

Font color of the currently hovered tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_TabContainer_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the tab name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_TabContainer_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

Font color of the currently selected tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_color_font_unselected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)`
`🔗<class_TabContainer_theme_color_font_unselected_color>`{.interpreted-text
role="ref"}

Font color of the other, unselected tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_constant_icon_max_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_max_width** = `0`
`🔗<class_TabContainer_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}

The maximum allowed width of the tab\'s icon. This limit is applied on
top of the default size of the icon, but before the value set with
`TabBar.set_tab_icon_max_width()<class_TabBar_method_set_tab_icon_max_width>`{.interpreted-text
role="ref"}. The height is adjusted according to the icon\'s ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_constant_icon_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_separation** = `4`
`🔗<class_TabContainer_theme_constant_icon_separation>`{.interpreted-text
role="ref"}

Space between tab\'s name and its icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_TabContainer_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the tab text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_TabContainer_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_constant_side_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **side_margin** = `8`
`🔗<class_TabContainer_theme_constant_side_margin>`{.interpreted-text
role="ref"}

The space at the left or right edges of the tab bar, accordingly with
the current
`tab_alignment<class_TabContainer_property_tab_alignment>`{.interpreted-text
role="ref"}.

The margin is ignored with
`TabBar.ALIGNMENT_RIGHT<class_TabBar_constant_ALIGNMENT_RIGHT>`{.interpreted-text
role="ref"} if the tabs are clipped (see
`clip_tabs<class_TabContainer_property_clip_tabs>`{.interpreted-text
role="ref"}) or a popup has been set (see
`set_popup()<class_TabContainer_method_set_popup>`{.interpreted-text
role="ref"}). The margin is always ignored with
`TabBar.ALIGNMENT_CENTER<class_TabBar_constant_ALIGNMENT_CENTER>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_constant_tab_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tab_separation** = `0`
`🔗<class_TabContainer_theme_constant_tab_separation>`{.interpreted-text
role="ref"}

The space between tabs in the tab bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_TabContainer_theme_font_font>`{.interpreted-text role="ref"}

The font used to draw tab names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_TabContainer_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the tab names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_decrement}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **decrement**
`🔗<class_TabContainer_theme_icon_decrement>`{.interpreted-text
role="ref"}

Icon for the left arrow button that appears when there are too many tabs
to fit in the container width. When the button is disabled (i.e. the
first tab is visible), it appears semi-transparent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_decrement_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**decrement_highlight**
`🔗<class_TabContainer_theme_icon_decrement_highlight>`{.interpreted-text
role="ref"}

Icon for the left arrow button that appears when there are too many tabs
to fit in the container width. Used when the button is being hovered
with the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_drop_mark}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **drop_mark**
`🔗<class_TabContainer_theme_icon_drop_mark>`{.interpreted-text
role="ref"}

Icon shown to indicate where a dragged tab is gonna be dropped (see
`drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_increment}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **increment**
`🔗<class_TabContainer_theme_icon_increment>`{.interpreted-text
role="ref"}

Icon for the right arrow button that appears when there are too many
tabs to fit in the container width. When the button is disabled (i.e.
the last tab is visible) it appears semi-transparent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_increment_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**increment_highlight**
`🔗<class_TabContainer_theme_icon_increment_highlight>`{.interpreted-text
role="ref"}

Icon for the right arrow button that appears when there are too many
tabs to fit in the container width. Used when the button is being
hovered with the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_menu}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **menu**
`🔗<class_TabContainer_theme_icon_menu>`{.interpreted-text role="ref"}

The icon for the menu button (see
`set_popup()<class_TabContainer_method_set_popup>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_icon_menu_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**menu_highlight**
`🔗<class_TabContainer_theme_icon_menu_highlight>`{.interpreted-text
role="ref"}

The icon for the menu button (see
`set_popup()<class_TabContainer_method_set_popup>`{.interpreted-text
role="ref"}) when it\'s being hovered with the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_TabContainer_theme_style_panel>`{.interpreted-text role="ref"}

The style for the background fill.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_style_tab_disabled}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tab_disabled**
`🔗<class_TabContainer_theme_style_tab_disabled>`{.interpreted-text
role="ref"}

The style of disabled tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_style_tab_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **tab_focus**
`🔗<class_TabContainer_theme_style_tab_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
`TabBar<class_TabBar>`{.interpreted-text role="ref"} is focused. The
`tab_focus<class_TabContainer_theme_style_tab_focus>`{.interpreted-text
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

:::: {#class_TabContainer_theme_style_tab_hovered}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **tab_hovered**
`🔗<class_TabContainer_theme_style_tab_hovered>`{.interpreted-text
role="ref"}

The style of the currently hovered tab.

\*\*Note:\*\* This style will be drawn with the same width as
`tab_unselected<class_TabContainer_theme_style_tab_unselected>`{.interpreted-text
role="ref"} at minimum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_style_tab_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tab_selected**
`🔗<class_TabContainer_theme_style_tab_selected>`{.interpreted-text
role="ref"}

The style of the currently selected tab.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_style_tab_unselected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tab_unselected**
`🔗<class_TabContainer_theme_style_tab_unselected>`{.interpreted-text
role="ref"}

The style of the other, unselected tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TabContainer_theme_style_tabbar_background}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**tabbar_background**
`🔗<class_TabContainer_theme_style_tabbar_background>`{.interpreted-text
role="ref"}

The style for the background fill of the
`TabBar<class_TabBar>`{.interpreted-text role="ref"} area.
