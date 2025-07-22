github_url
:   hide

# GraphNode {#class_GraphNode}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `GraphElement<class_GraphElement>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A container with connection ports, representing a node in a
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**GraphNode** allows to create nodes for a
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} graph with
customizable content based on its child controls. **GraphNode** is
derived from `Container<class_Container>`{.interpreted-text role="ref"}
and it is responsible for placing its children on screen. This works
similar to `VBoxContainer<class_VBoxContainer>`{.interpreted-text
role="ref"}. Children, in turn, provide **GraphNode** with so-called
slots, each of which can have a connection port on either side.

Each **GraphNode** slot is defined by its index and can provide the node
with up to two ports: one on the left, and one on the right. By
convention the left port is also referred to as the **input port** and
the right port is referred to as the **output port**. Each port can be
enabled and configured individually, using different type and color. The
type is an arbitrary value that you can define using your own
considerations. The parent
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} will receive
this information on each connect and disconnect request.

Slots can be configured in the Inspector dock once you add at least one
child `Control<class_Control>`{.interpreted-text role="ref"}. The
properties are grouped by each slot\'s index in the \"Slot\" section.

\*\*Note:\*\* While GraphNode is set up using slots and slot indices,
connections are made between the ports which are enabled. Because of
that `GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} uses the
port\'s index and not the slot\'s index. You can use
`get_input_port_slot()<class_GraphNode_method_get_input_port_slot>`{.interpreted-text
role="ref"} and
`get_output_port_slot()<class_GraphNode_method_get_output_port_slot>`{.interpreted-text
role="ref"} to get the slot index from the port index.

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

:::: {#class_GraphNode_signal_slot_sizes_changed}
::: rst-class
classref-signal
:::
::::

**slot_sizes_changed**()
`🔗<class_GraphNode_signal_slot_sizes_changed>`{.interpreted-text
role="ref"}

Emitted when any slot\'s size might have changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_signal_slot_updated}
::: rst-class
classref-signal
:::
::::

**slot_updated**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_GraphNode_signal_slot_updated>`{.interpreted-text
role="ref"}

Emitted when any GraphNode\'s slot is updated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GraphNode_property_ignore_invalid_connection_type}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**ignore_invalid_connection_type** = `false`
`🔗<class_GraphNode_property_ignore_invalid_connection_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ignore_invalid_connection_type**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_ignoring_valid_connection_type**()

If `true`, you can connect ports with different types, even if the
connection was not explicitly allowed in the parent
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_property_slots_focus_mode}
::: rst-class
classref-property
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**slots_focus_mode** = `3`
`🔗<class_GraphNode_property_slots_focus_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_slots_focus_mode**(value:
  `FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"})
- `FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
  **get_slots_focus_mode**()

Determines how connection slots can be focused.

- If set to
  `Control.FOCUS_CLICK<class_Control_constant_FOCUS_CLICK>`{.interpreted-text
  role="ref"}, connections can only be made with the mouse.
- If set to
  `Control.FOCUS_ALL<class_Control_constant_FOCUS_ALL>`{.interpreted-text
  role="ref"}, slots can also be focused using the
  `ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>`{.interpreted-text
  role="ref"} and
  `ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>`{.interpreted-text
  role="ref"} and connected using
  `ProjectSettings.input/ui_left<class_ProjectSettings_property_input/ui_left>`{.interpreted-text
  role="ref"} and
  `ProjectSettings.input/ui_right<class_ProjectSettings_property_input/ui_right>`{.interpreted-text
  role="ref"} input actions.
- If set to
  `Control.FOCUS_ACCESSIBILITY<class_Control_constant_FOCUS_ACCESSIBILITY>`{.interpreted-text
  role="ref"}, slot input actions are only enabled when the screen
  reader is active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_property_title}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **title** = `""`
`🔗<class_GraphNode_property_title>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_title**()

The text displayed in the GraphNode\'s title bar.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GraphNode_private_method__draw_port}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw_port**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, left: `bool<class_bool>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_private_method__draw_port>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_clear_all_slots}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_all_slots**()
`🔗<class_GraphNode_method_clear_all_slots>`{.interpreted-text
role="ref"}

Disables all slots of the GraphNode. This will remove all input/output
ports from the GraphNode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_clear_slot}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_slot**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_GraphNode_method_clear_slot>`{.interpreted-text
role="ref"}

Disables the slot with the given `slot_index`. This will remove the
corresponding input and output port from the GraphNode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_input_port_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_input_port_color**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_input_port_color>`{.interpreted-text
role="ref"}

Returns the `Color<class_Color>`{.interpreted-text role="ref"} of the
input port with the given `port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_input_port_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_input_port_count**()
`🔗<class_GraphNode_method_get_input_port_count>`{.interpreted-text
role="ref"}

Returns the number of slots with an enabled input port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_input_port_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_input_port_position**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_input_port_position>`{.interpreted-text
role="ref"}

Returns the position of the input port with the given `port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_input_port_slot}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_input_port_slot**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_input_port_slot>`{.interpreted-text
role="ref"}

Returns the corresponding slot index of the input port with the given
`port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_input_port_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_input_port_type**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_input_port_type>`{.interpreted-text
role="ref"}

Returns the type of the input port with the given `port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_output_port_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_output_port_color**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_output_port_color>`{.interpreted-text
role="ref"}

Returns the `Color<class_Color>`{.interpreted-text role="ref"} of the
output port with the given `port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_output_port_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_output_port_count**()
`🔗<class_GraphNode_method_get_output_port_count>`{.interpreted-text
role="ref"}

Returns the number of slots with an enabled output port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_output_port_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_output_port_position**(port_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_get_output_port_position>`{.interpreted-text
role="ref"}

Returns the position of the output port with the given `port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_output_port_slot}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_output_port_slot**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_output_port_slot>`{.interpreted-text
role="ref"}

Returns the corresponding slot index of the output port with the given
`port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_output_port_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_output_port_type**(port_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GraphNode_method_get_output_port_type>`{.interpreted-text
role="ref"}

Returns the type of the output port with the given `port_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_slot_color_left}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_slot_color_left**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_get_slot_color_left>`{.interpreted-text
role="ref"}

Returns the left (input) `Color<class_Color>`{.interpreted-text
role="ref"} of the slot with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_slot_color_right}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_slot_color_right**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_get_slot_color_right>`{.interpreted-text
role="ref"}

Returns the right (output) `Color<class_Color>`{.interpreted-text
role="ref"} of the slot with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_slot_custom_icon_left}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_slot_custom_icon_left**(slot_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_get_slot_custom_icon_left>`{.interpreted-text
role="ref"}

Returns the left (input) custom
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} of the slot
with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_slot_custom_icon_right}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_slot_custom_icon_right**(slot_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_get_slot_custom_icon_right>`{.interpreted-text
role="ref"}

Returns the right (output) custom
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} of the slot
with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_slot_type_left}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_slot_type_left**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_get_slot_type_left>`{.interpreted-text
role="ref"}

Returns the left (input) type of the slot with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_slot_type_right}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_slot_type_right**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_get_slot_type_right>`{.interpreted-text
role="ref"}

Returns the right (output) type of the slot with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_get_titlebar_hbox}
::: rst-class
classref-method
:::
::::

`HBoxContainer<class_HBoxContainer>`{.interpreted-text role="ref"}
**get_titlebar_hbox**()
`🔗<class_GraphNode_method_get_titlebar_hbox>`{.interpreted-text
role="ref"}

Returns the `HBoxContainer<class_HBoxContainer>`{.interpreted-text
role="ref"} used for the title bar, only containing a
`Label<class_Label>`{.interpreted-text role="ref"} for displaying the
title by default. This can be used to add custom controls to the title
bar such as option or close buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_is_slot_draw_stylebox}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_slot_draw_stylebox**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_is_slot_draw_stylebox>`{.interpreted-text
role="ref"}

Returns `true` if the background
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} of the slot
with the given `slot_index` is drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_is_slot_enabled_left}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_slot_enabled_left**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_is_slot_enabled_left>`{.interpreted-text
role="ref"}

Returns `true` if left (input) side of the slot with the given
`slot_index` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_is_slot_enabled_right}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_slot_enabled_right**(slot_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphNode_method_is_slot_enabled_right>`{.interpreted-text
role="ref"}

Returns `true` if right (output) side of the slot with the given
`slot_index` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot**(slot_index: `int<class_int>`{.interpreted-text role="ref"},
enable_left_port: `bool<class_bool>`{.interpreted-text role="ref"},
type_left: `int<class_int>`{.interpreted-text role="ref"}, color_left:
`Color<class_Color>`{.interpreted-text role="ref"}, enable_right_port:
`bool<class_bool>`{.interpreted-text role="ref"}, type_right:
`int<class_int>`{.interpreted-text role="ref"}, color_right:
`Color<class_Color>`{.interpreted-text role="ref"}, custom_icon_left:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} = null,
custom_icon_right: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} = null, draw_stylebox: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_GraphNode_method_set_slot>`{.interpreted-text role="ref"}

Sets properties of the slot with the given `slot_index`.

If `enable_left_port`/`enable_right_port` is `true`, a port will appear
and the slot will be able to be connected from this side.

With `type_left`/`type_right` an arbitrary type can be assigned to each
port. Two ports can be connected if they share the same type, or if the
connection between their types is allowed in the parent
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} (see
`GraphEdit.add_valid_connection_type()<class_GraphEdit_method_add_valid_connection_type>`{.interpreted-text
role="ref"}). Keep in mind that the
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} has the final
say in accepting the connection. Type compatibility simply allows the
`GraphEdit.connection_request<class_GraphEdit_signal_connection_request>`{.interpreted-text
role="ref"} signal to be emitted.

Ports can be further customized using `color_left`/`color_right` and
`custom_icon_left`/`custom_icon_right`. The color parameter adds a tint
to the icon. The custom icon can be used to override the default port
dot.

Additionally, `draw_stylebox` can be used to enable or disable drawing
of the background stylebox for each slot. See
`slot<class_GraphNode_theme_style_slot>`{.interpreted-text role="ref"}.

Individual properties can also be set using one of the `set_slot_*`
methods.

\*\*Note:\*\* This method only sets properties of the slot. To create
the slot itself, add a `Control<class_Control>`{.interpreted-text
role="ref"}-derived child to the GraphNode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_color_left}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_color_left**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_color_left>`{.interpreted-text
role="ref"}

Sets the `Color<class_Color>`{.interpreted-text role="ref"} of the left
(input) side of the slot with the given `slot_index` to `color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_color_right}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_color_right**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_color_right>`{.interpreted-text
role="ref"}

Sets the `Color<class_Color>`{.interpreted-text role="ref"} of the right
(output) side of the slot with the given `slot_index` to `color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_custom_icon_left}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_custom_icon_left**(slot_index:
`int<class_int>`{.interpreted-text role="ref"}, custom_icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_custom_icon_left>`{.interpreted-text
role="ref"}

Sets the custom `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} of the left (input) side of the slot with the given
`slot_index` to `custom_icon`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_custom_icon_right}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_custom_icon_right**(slot_index:
`int<class_int>`{.interpreted-text role="ref"}, custom_icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_custom_icon_right>`{.interpreted-text
role="ref"}

Sets the custom `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} of the right (output) side of the slot with the given
`slot_index` to `custom_icon`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_draw_stylebox}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_draw_stylebox**(slot_index:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_draw_stylebox>`{.interpreted-text
role="ref"}

Toggles the background `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} of the slot with the given `slot_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_enabled_left}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_enabled_left**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_enabled_left>`{.interpreted-text
role="ref"}

Toggles the left (input) side of the slot with the given `slot_index`.
If `enable` is `true`, a port will appear on the left side and the slot
will be able to be connected from this side.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_enabled_right}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_enabled_right**(slot_index:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_enabled_right>`{.interpreted-text
role="ref"}

Toggles the right (output) side of the slot with the given `slot_index`.
If `enable` is `true`, a port will appear on the right side and the slot
will be able to be connected from this side.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_type_left}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_type_left**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}, type: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_type_left>`{.interpreted-text
role="ref"}

Sets the left (input) type of the slot with the given `slot_index` to
`type`. If the value is negative, all connections will be disallowed to
be created via user inputs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_method_set_slot_type_right}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_slot_type_right**(slot_index: `int<class_int>`{.interpreted-text
role="ref"}, type: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphNode_method_set_slot_type_right>`{.interpreted-text
role="ref"}

Sets the right (output) type of the slot with the given `slot_index` to
`type`. If the value is negative, all connections will be disallowed to
be created via user inputs.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_GraphNode_theme_color_resizer_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **resizer_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_GraphNode_theme_color_resizer_color>`{.interpreted-text
role="ref"}

The color modulation applied to the resizer icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_constant_port_h_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **port_h_offset** = `0`
`🔗<class_GraphNode_theme_constant_port_h_offset>`{.interpreted-text
role="ref"}

Horizontal offset for the ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_constant_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **separation** = `2`
`🔗<class_GraphNode_theme_constant_separation>`{.interpreted-text
role="ref"}

The vertical distance between ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_icon_port}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **port**
`🔗<class_GraphNode_theme_icon_port>`{.interpreted-text role="ref"}

The icon used for representing ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_GraphNode_theme_style_panel>`{.interpreted-text role="ref"}

The default background for the slot area of the **GraphNode**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_panel_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel_focus**
`🔗<class_GraphNode_theme_style_panel_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**GraphNode** is focused (when used with assistive apps).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_panel_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**panel_selected**
`🔗<class_GraphNode_theme_style_panel_selected>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the slot area when selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_slot}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **slot**
`🔗<class_GraphNode_theme_style_slot>`{.interpreted-text role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
each slot of the **GraphNode**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_slot_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**slot_selected**
`🔗<class_GraphNode_theme_style_slot_selected>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
slot is focused (when used with assistive apps).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_titlebar}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **titlebar**
`🔗<class_GraphNode_theme_style_titlebar>`{.interpreted-text role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the title bar of the **GraphNode**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphNode_theme_style_titlebar_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**titlebar_selected**
`🔗<class_GraphNode_theme_style_titlebar_selected>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the title bar of the **GraphNode** when it is selected.
