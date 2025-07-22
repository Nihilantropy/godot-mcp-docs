github_url
:   hide

# GraphEdit {#class_GraphEdit}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An editor for graph-like structures, using
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

**GraphEdit** provides tools for creation, manipulation, and display of
various graphs. Its main purpose in the engine is to power the visual
programming systems, such as visual shaders, but it is also available
for use in user projects.

\*\*GraphEdit\*\* by itself is only an empty container, representing an
infinite grid where `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"}s can be placed. Each
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} represents a
node in the graph, a single unit of data in the connected scheme.
**GraphEdit**, in turn, helps to control various interactions with nodes
and between nodes. When the user attempts to connect, disconnect, or
delete a `GraphNode<class_GraphNode>`{.interpreted-text role="ref"}, a
signal is emitted in the **GraphEdit**, but no action is taken by
default. It is the responsibility of the programmer utilizing this
control to implement the necessary logic to determine how each request
should be handled.

\*\*Performance:\*\* It is greatly advised to enable low-processor usage
mode (see
`OS.low_processor_usage_mode<class_OS_property_low_processor_usage_mode>`{.interpreted-text
role="ref"}) when using GraphEdits.

\*\*Note:\*\* Keep in mind that
`Node.get_children()<class_Node_method_get_children>`{.interpreted-text
role="ref"} will also return the connection layer node named
`_connection_layer` due to technical limitations. This behavior may
change in future releases.

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

:::: {#class_GraphEdit_signal_begin_node_move}
::: rst-class
classref-signal
:::
::::

**begin_node_move**()
`🔗<class_GraphEdit_signal_begin_node_move>`{.interpreted-text
role="ref"}

Emitted at the beginning of a
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}\'s
movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_connection_drag_ended}
::: rst-class
classref-signal
:::
::::

**connection_drag_ended**()
`🔗<class_GraphEdit_signal_connection_drag_ended>`{.interpreted-text
role="ref"}

Emitted at the end of a connection drag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_connection_drag_started}
::: rst-class
classref-signal
:::
::::

**connection_drag_started**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, is_output:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_connection_drag_started>`{.interpreted-text
role="ref"}

Emitted at the beginning of a connection drag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_connection_from_empty}
::: rst-class
classref-signal
:::
::::

**connection_from_empty**(to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"}, release_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_connection_from_empty>`{.interpreted-text
role="ref"}

Emitted when user drags a connection from an input port into the empty
space of the graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_connection_request}
::: rst-class
classref-signal
:::
::::

**connection_request**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_connection_request>`{.interpreted-text
role="ref"}

Emitted to the GraphEdit when the connection between the `from_port` of
the `from_node` `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"} and the `to_port` of the `to_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} is attempted
to be created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_connection_to_empty}
::: rst-class
classref-signal
:::
::::

**connection_to_empty**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, release_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_connection_to_empty>`{.interpreted-text
role="ref"}

Emitted when user drags a connection from an output port into the empty
space of the graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_copy_nodes_request}
::: rst-class
classref-signal
:::
::::

**copy_nodes_request**()
`🔗<class_GraphEdit_signal_copy_nodes_request>`{.interpreted-text
role="ref"}

Emitted when this **GraphEdit** captures a `ui_copy` action
(`Ctrl + C`{.interpreted-text role="kbd"} by default). In general, this
signal indicates that the selected
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s should
be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_cut_nodes_request}
::: rst-class
classref-signal
:::
::::

**cut_nodes_request**()
`🔗<class_GraphEdit_signal_cut_nodes_request>`{.interpreted-text
role="ref"}

Emitted when this **GraphEdit** captures a `ui_cut` action
(`Ctrl + X`{.interpreted-text role="kbd"} by default). In general, this
signal indicates that the selected
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s should
be cut.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_delete_nodes_request}
::: rst-class
classref-signal
:::
::::

**delete_nodes_request**(nodes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\])
`🔗<class_GraphEdit_signal_delete_nodes_request>`{.interpreted-text
role="ref"}

Emitted when this **GraphEdit** captures a `ui_graph_delete` action
(`Delete`{.interpreted-text role="kbd"} by default).

`nodes` is an array of node names that should be removed. These usually
include all selected nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_disconnection_request}
::: rst-class
classref-signal
:::
::::

**disconnection_request**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_disconnection_request>`{.interpreted-text
role="ref"}

Emitted to the GraphEdit when the connection between `from_port` of
`from_node` `GraphNode<class_GraphNode>`{.interpreted-text role="ref"}
and `to_port` of `to_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} is attempted
to be removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_duplicate_nodes_request}
::: rst-class
classref-signal
:::
::::

**duplicate_nodes_request**()
`🔗<class_GraphEdit_signal_duplicate_nodes_request>`{.interpreted-text
role="ref"}

Emitted when this **GraphEdit** captures a `ui_graph_duplicate` action
(`Ctrl + D`{.interpreted-text role="kbd"} by default). In general, this
signal indicates that the selected
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s should
be duplicated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_end_node_move}
::: rst-class
classref-signal
:::
::::

**end_node_move**()
`🔗<class_GraphEdit_signal_end_node_move>`{.interpreted-text role="ref"}

Emitted at the end of a
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}\'s
movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_frame_rect_changed}
::: rst-class
classref-signal
:::
::::

**frame_rect_changed**(frame:
`GraphFrame<class_GraphFrame>`{.interpreted-text role="ref"}, new_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_frame_rect_changed>`{.interpreted-text
role="ref"}

Emitted when the `GraphFrame<class_GraphFrame>`{.interpreted-text
role="ref"} `frame` is resized to `new_rect`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_graph_elements_linked_to_frame_request}
::: rst-class
classref-signal
:::
::::

**graph_elements_linked_to_frame_request**(elements:
`Array<class_Array>`{.interpreted-text role="ref"}, frame:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_graph_elements_linked_to_frame_request>`{.interpreted-text
role="ref"}

Emitted when one or more
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s are
dropped onto the `GraphFrame<class_GraphFrame>`{.interpreted-text
role="ref"} named `frame`, when they were not previously attached to any
other one.

`elements` is an array of
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s to be
attached.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_node_deselected}
::: rst-class
classref-signal
:::
::::

**node_deselected**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_GraphEdit_signal_node_deselected>`{.interpreted-text
role="ref"}

Emitted when the given
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"} node is
deselected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_node_selected}
::: rst-class
classref-signal
:::
::::

**node_selected**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_GraphEdit_signal_node_selected>`{.interpreted-text role="ref"}

Emitted when the given
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"} node is
selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_paste_nodes_request}
::: rst-class
classref-signal
:::
::::

**paste_nodes_request**()
`🔗<class_GraphEdit_signal_paste_nodes_request>`{.interpreted-text
role="ref"}

Emitted when this **GraphEdit** captures a `ui_paste` action
(`Ctrl + V`{.interpreted-text role="kbd"} by default). In general, this
signal indicates that previously copied
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s should
be pasted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_popup_request}
::: rst-class
classref-signal
:::
::::

**popup_request**(at_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_popup_request>`{.interpreted-text role="ref"}

Emitted when a popup is requested. Happens on right-clicking in the
GraphEdit. `at_position` is the position of the mouse pointer when the
signal is sent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_signal_scroll_offset_changed}
::: rst-class
classref-signal
:::
::::

**scroll_offset_changed**(offset:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_signal_scroll_offset_changed>`{.interpreted-text
role="ref"}

Emitted when the scroll offset is changed by the user. It will not be
emitted when changed in code.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_GraphEdit_PanningScheme}
::: rst-class
classref-enumeration
:::
::::

enum **PanningScheme**:
`🔗<enum_GraphEdit_PanningScheme>`{.interpreted-text role="ref"}

:::: {#class_GraphEdit_constant_SCROLL_ZOOMS}
::: rst-class
classref-enumeration-constant
:::
::::

`PanningScheme<enum_GraphEdit_PanningScheme>`{.interpreted-text
role="ref"} **SCROLL_ZOOMS** = `0`

`Mouse Wheel`{.interpreted-text role="kbd"} will zoom,
`Ctrl + Mouse Wheel`{.interpreted-text role="kbd"} will move the view.

:::: {#class_GraphEdit_constant_SCROLL_PANS}
::: rst-class
classref-enumeration-constant
:::
::::

`PanningScheme<enum_GraphEdit_PanningScheme>`{.interpreted-text
role="ref"} **SCROLL_PANS** = `1`

`Mouse Wheel`{.interpreted-text role="kbd"} will move the view,
`Ctrl + Mouse Wheel`{.interpreted-text role="kbd"} will zoom.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_GraphEdit_GridPattern}
::: rst-class
classref-enumeration
:::
::::

enum **GridPattern**: `🔗<enum_GraphEdit_GridPattern>`{.interpreted-text
role="ref"}

:::: {#class_GraphEdit_constant_GRID_PATTERN_LINES}
::: rst-class
classref-enumeration-constant
:::
::::

`GridPattern<enum_GraphEdit_GridPattern>`{.interpreted-text role="ref"}
**GRID_PATTERN_LINES** = `0`

Draw the grid using solid lines.

:::: {#class_GraphEdit_constant_GRID_PATTERN_DOTS}
::: rst-class
classref-enumeration-constant
:::
::::

`GridPattern<enum_GraphEdit_GridPattern>`{.interpreted-text role="ref"}
**GRID_PATTERN_DOTS** = `1`

Draw the grid using dots.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GraphEdit_property_connection_lines_antialiased}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**connection_lines_antialiased** = `true`
`🔗<class_GraphEdit_property_connection_lines_antialiased>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_connection_lines_antialiased**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_connection_lines_antialiased**()

If `true`, the lines between nodes will use antialiasing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_connection_lines_curvature}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**connection_lines_curvature** = `0.5`
`🔗<class_GraphEdit_property_connection_lines_curvature>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_connection_lines_curvature**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_connection_lines_curvature**()

The curvature of the lines between the nodes. 0 results in straight
lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_connection_lines_thickness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**connection_lines_thickness** = `4.0`
`🔗<class_GraphEdit_property_connection_lines_thickness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_connection_lines_thickness**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_connection_lines_thickness**()

The thickness of the lines between the nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_connections}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **connections** = `[]`
`🔗<class_GraphEdit_property_connections>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_connections**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
  role="ref"}\] **get_connection_list**()

The connections between `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"}s.

A connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} in the form
of:

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

Connections with `keep_alive` set to `false` may be deleted
automatically if invalid during a redraw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_grid_pattern}
::: rst-class
classref-property
:::
::::

`GridPattern<enum_GraphEdit_GridPattern>`{.interpreted-text role="ref"}
**grid_pattern** = `0`
`🔗<class_GraphEdit_property_grid_pattern>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_grid_pattern**(value:
  `GridPattern<enum_GraphEdit_GridPattern>`{.interpreted-text
  role="ref"})
- `GridPattern<enum_GraphEdit_GridPattern>`{.interpreted-text
  role="ref"} **get_grid_pattern**()

The pattern used for drawing the grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_minimap_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **minimap_enabled** =
`true` `🔗<class_GraphEdit_property_minimap_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_minimap_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_minimap_enabled**()

If `true`, the minimap is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_minimap_opacity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **minimap_opacity** =
`0.65` `🔗<class_GraphEdit_property_minimap_opacity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_minimap_opacity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_minimap_opacity**()

The opacity of the minimap rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_minimap_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **minimap_size**
= `Vector2(240, 160)`
`🔗<class_GraphEdit_property_minimap_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_minimap_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_minimap_size**()

The size of the minimap rectangle. The map itself is based on the size
of the grid area and is scaled to fit this rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_panning_scheme}
::: rst-class
classref-property
:::
::::

`PanningScheme<enum_GraphEdit_PanningScheme>`{.interpreted-text
role="ref"} **panning_scheme** = `0`
`🔗<class_GraphEdit_property_panning_scheme>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_panning_scheme**(value:
  `PanningScheme<enum_GraphEdit_PanningScheme>`{.interpreted-text
  role="ref"})
- `PanningScheme<enum_GraphEdit_PanningScheme>`{.interpreted-text
  role="ref"} **get_panning_scheme**()

Defines the control scheme for panning with mouse wheel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_right_disconnects}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **right_disconnects** =
`false`
`🔗<class_GraphEdit_property_right_disconnects>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_right_disconnects**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_right_disconnects_enabled**()

If `true`, enables disconnection of existing connections in the
GraphEdit by dragging the right end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_scroll_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scroll_offset**
= `Vector2(0, 0)`
`🔗<class_GraphEdit_property_scroll_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_scroll_offset**()

The scroll offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_arrange_button}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_arrange_button**
= `true`
`🔗<class_GraphEdit_property_show_arrange_button>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_arrange_button**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_arrange_button**()

If `true`, the button to automatically arrange graph nodes is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_grid}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_grid** = `true`
`🔗<class_GraphEdit_property_show_grid>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_grid**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_showing_grid**()

If `true`, the grid is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_grid_buttons}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_grid_buttons** =
`true`
`🔗<class_GraphEdit_property_show_grid_buttons>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_grid_buttons**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_grid_buttons**()

If `true`, buttons that allow to configure grid and snapping options are
visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_menu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_menu** = `true`
`🔗<class_GraphEdit_property_show_menu>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_menu**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_showing_menu**()

If `true`, the menu toolbar is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_minimap_button}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_minimap_button**
= `true`
`🔗<class_GraphEdit_property_show_minimap_button>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_minimap_button**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_minimap_button**()

If `true`, the button to toggle the minimap is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_zoom_buttons}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_zoom_buttons** =
`true`
`🔗<class_GraphEdit_property_show_zoom_buttons>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_zoom_buttons**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_zoom_buttons**()

If `true`, buttons that allow to change and reset the zoom level are
visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_show_zoom_label}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_zoom_label** =
`false` `🔗<class_GraphEdit_property_show_zoom_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_zoom_label**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_zoom_label**()

If `true`, the label with the current zoom level is visible. The zoom
level is displayed in percents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_snapping_distance}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **snapping_distance** =
`20` `🔗<class_GraphEdit_property_snapping_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snapping_distance**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_snapping_distance**()

The snapping distance in pixels, also determines the grid line distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_snapping_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **snapping_enabled** =
`true` `🔗<class_GraphEdit_property_snapping_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snapping_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_snapping_enabled**()

If `true`, enables snapping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_type_names}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**type_names** = `{}`
`🔗<class_GraphEdit_property_type_names>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_type_names**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_type_names**()

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} of human
readable port type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_zoom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **zoom** = `1.0`
`🔗<class_GraphEdit_property_zoom>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_zoom**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_zoom**()

The current zoom value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_zoom_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **zoom_max** =
`2.0736003` `🔗<class_GraphEdit_property_zoom_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_zoom_max**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_zoom_max**()

The upper zoom limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_zoom_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **zoom_min** =
`0.23256795` `🔗<class_GraphEdit_property_zoom_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_zoom_min**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_zoom_min**()

The lower zoom limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_property_zoom_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **zoom_step** = `1.2`
`🔗<class_GraphEdit_property_zoom_step>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_zoom_step**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_zoom_step**()

The step of each zoom level.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GraphEdit_private_method__get_connection_line}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **\_get_connection_line**(from_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, to_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_private_method__get_connection_line>`{.interpreted-text
role="ref"}

Virtual method which can be overridden to customize how connections are
drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_private_method__is_in_input_hotzone}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_in_input_hotzone**(in_node:
`Object<class_Object>`{.interpreted-text role="ref"}, in_port:
`int<class_int>`{.interpreted-text role="ref"}, mouse_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_private_method__is_in_input_hotzone>`{.interpreted-text
role="ref"}

Returns whether the `mouse_position` is in the input hot zone.

By default, a hot zone is a `Rect2<class_Rect2>`{.interpreted-text
role="ref"} positioned such that its center is at
`in_node`.`GraphNode.get_input_port_position()<class_GraphNode_method_get_input_port_position>`{.interpreted-text
role="ref"}(`in_port`) (For output\'s case, call
`GraphNode.get_output_port_position()<class_GraphNode_method_get_output_port_position>`{.interpreted-text
role="ref"} instead). The hot zone\'s width is twice the Theme Property
`port_grab_distance_horizontal`, and its height is twice the
`port_grab_distance_vertical`.

Below is a sample code to help get started:

    func _is_in_input_hotzone(in_node, in_port, mouse_position):
        var port_size = Vector2(get_theme_constant("port_grab_distance_horizontal"), get_theme_constant("port_grab_distance_vertical"))
        var port_pos = in_node.get_position() + in_node.get_input_port_position(in_port) - port_size / 2
        var rect = Rect2(port_pos, port_size)

        return rect.has_point(mouse_position)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_private_method__is_in_output_hotzone}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_in_output_hotzone**(in_node:
`Object<class_Object>`{.interpreted-text role="ref"}, in_port:
`int<class_int>`{.interpreted-text role="ref"}, mouse_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_private_method__is_in_output_hotzone>`{.interpreted-text
role="ref"}

Returns whether the `mouse_position` is in the output hot zone. For more
information on hot zones, see
`_is_in_input_hotzone()<class_GraphEdit_private_method__is_in_input_hotzone>`{.interpreted-text
role="ref"}.

Below is a sample code to help get started:

    func _is_in_output_hotzone(in_node, in_port, mouse_position):
        var port_size = Vector2(get_theme_constant("port_grab_distance_horizontal"), get_theme_constant("port_grab_distance_vertical"))
        var port_pos = in_node.get_position() + in_node.get_output_port_position(in_port) - port_size / 2
        var rect = Rect2(port_pos, port_size)

        return rect.has_point(mouse_position)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_private_method__is_node_hover_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_node_hover_valid**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_private_method__is_node_hover_valid>`{.interpreted-text
role="ref"}

This virtual method can be used to insert additional error detection
while the user is dragging a connection over a valid port.

Return `true` if the connection is indeed valid or return `false` if the
connection is impossible. If the connection is impossible, no snapping
to the port and thus no connection request to that port will happen.

In this example a connection to same node is suppressed:

::::: tabs
::: code-tab
gdscript

func [is_node_hover_valid]{#is_node_hover_valid}(from, from_port, to, to_port):

:   return from != to
:::

::: code-tab
csharp

public override bool [IsNodeHoverValid]{#isnodehovervalid}(StringName
fromNode, int fromPort, StringName toNode, int toPort) { return fromNode
!= toNode; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_add_valid_connection_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_valid_connection_type**(from_type:
`int<class_int>`{.interpreted-text role="ref"}, to_type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_add_valid_connection_type>`{.interpreted-text
role="ref"}

Allows the connection between two different port types. The port type is
defined individually for the left and the right port of each slot with
the
`GraphNode.set_slot()<class_GraphNode_method_set_slot>`{.interpreted-text
role="ref"} method.

See also
`is_valid_connection_type()<class_GraphEdit_method_is_valid_connection_type>`{.interpreted-text
role="ref"} and
`remove_valid_connection_type()<class_GraphEdit_method_remove_valid_connection_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_add_valid_left_disconnect_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_valid_left_disconnect_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_add_valid_left_disconnect_type>`{.interpreted-text
role="ref"}

Allows to disconnect nodes when dragging from the left port of the
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}\'s slot if it
has the specified type. See also
`remove_valid_left_disconnect_type()<class_GraphEdit_method_remove_valid_left_disconnect_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_add_valid_right_disconnect_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_valid_right_disconnect_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_add_valid_right_disconnect_type>`{.interpreted-text
role="ref"}

Allows to disconnect nodes when dragging from the right port of the
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}\'s slot if it
has the specified type. See also
`remove_valid_right_disconnect_type()<class_GraphEdit_method_remove_valid_right_disconnect_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_arrange_nodes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**arrange_nodes**()
`🔗<class_GraphEdit_method_arrange_nodes>`{.interpreted-text role="ref"}

Rearranges selected nodes in a layout with minimum crossings between
connections and uniform horizontal and vertical gap between nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_attach_graph_element_to_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**attach_graph_element_to_frame**(element:
`StringName<class_StringName>`{.interpreted-text role="ref"}, frame:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_attach_graph_element_to_frame>`{.interpreted-text
role="ref"}

Attaches the `element`
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"} to the
`frame` `GraphFrame<class_GraphFrame>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_clear_connections}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_connections**()
`🔗<class_GraphEdit_method_clear_connections>`{.interpreted-text
role="ref"}

Removes all connections between nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_connect_node}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_node**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"}, keep_alive:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_GraphEdit_method_connect_node>`{.interpreted-text role="ref"}

Create a connection between the `from_port` of the `from_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} and the
`to_port` of the `to_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}. If the
connection already exists, no connection is created.

Connections with `keep_alive` set to `false` may be deleted
automatically if invalid during a redraw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_detach_graph_element_from_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**detach_graph_element_from_frame**(element:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_detach_graph_element_from_frame>`{.interpreted-text
role="ref"}

Detaches the `element`
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"} from
the `GraphFrame<class_GraphFrame>`{.interpreted-text role="ref"} it is
currently attached to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_disconnect_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_node**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_disconnect_node>`{.interpreted-text
role="ref"}

Removes the connection between the `from_port` of the `from_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} and the
`to_port` of the `to_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}. If the
connection does not exist, no connection is removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_force_connection_drag_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_connection_drag_end**()
`🔗<class_GraphEdit_method_force_connection_drag_end>`{.interpreted-text
role="ref"}

Ends the creation of the current connection. In other words, if you are
dragging a connection you can use this method to abort the process and
remove the line that followed your cursor.

This is best used together with
`connection_drag_started<class_GraphEdit_signal_connection_drag_started>`{.interpreted-text
role="ref"} and
`connection_drag_ended<class_GraphEdit_signal_connection_drag_ended>`{.interpreted-text
role="ref"} to add custom behavior like node addition through shortcuts.

\*\*Note:\*\* This method suppresses any other connection request
signals apart from
`connection_drag_ended<class_GraphEdit_signal_connection_drag_ended>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_attached_nodes_of_frame}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_attached_nodes_of_frame**(frame:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_get_attached_nodes_of_frame>`{.interpreted-text
role="ref"}

Returns an array of node names that are attached to the
`GraphFrame<class_GraphFrame>`{.interpreted-text role="ref"} with the
given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_closest_connection_at_point}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_closest_connection_at_point**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, max_distance:
`float<class_float>`{.interpreted-text role="ref"} = 4.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_method_get_closest_connection_at_point>`{.interpreted-text
role="ref"}

Returns the closest connection to the given point in screen space. If no
connection is found within `max_distance` pixels, an empty
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} is
returned.

A connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} in the form
of:

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

For example, getting a connection at a given mouse position can be
achieved like this:

:::: tabs
::: code-tab
gdscript

var connection =
get_closest_connection_at_point(mouse_event.get_position())
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_connection_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_connection_count**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_get_connection_count>`{.interpreted-text
role="ref"}

Returns the number of connections from `from_port` of `from_node`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_connection_line}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_connection_line**(from_node:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, to_node:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_method_get_connection_line>`{.interpreted-text
role="ref"}

Returns the points which would make up a connection between `from_node`
and `to_node`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_connection_list_from_node}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_connection_list_from_node**(node:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_method_get_connection_list_from_node>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} containing
a list of all connections for `node`.

A connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} in the form
of:

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

\*\*Example:\*\* Get all connections on a specific port:

    func get_connection_list_from_port(node, port):
        var connections = get_connection_list_from_node(node)
        var result = []
        for connection in connections:
            var dict = {}
            if connection["from_node"] == node and connection["from_port"] == port:
                dict["node"] = connection["to_node"]
                dict["port"] = connection["to_port"]
                dict["type"] = "left"
                result.push_back(dict)
            elif connection["to_node"] == node and connection["to_port"] == port:
                dict["node"] = connection["from_node"]
                dict["port"] = connection["from_port"]
                dict["type"] = "right"
                result.push_back(dict)
        return result

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_connections_intersecting_with_rect}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_connections_intersecting_with_rect**(rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_method_get_connections_intersecting_with_rect>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} containing
the list of connections that intersect with the given
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

A connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} in the form
of:

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_element_frame}
::: rst-class
classref-method
:::
::::

`GraphFrame<class_GraphFrame>`{.interpreted-text role="ref"}
**get_element_frame**(element:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_get_element_frame>`{.interpreted-text
role="ref"}

Returns the `GraphFrame<class_GraphFrame>`{.interpreted-text role="ref"}
that contains the `GraphElement<class_GraphElement>`{.interpreted-text
role="ref"} with the given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_get_menu_hbox}
::: rst-class
classref-method
:::
::::

`HBoxContainer<class_HBoxContainer>`{.interpreted-text role="ref"}
**get_menu_hbox**()
`🔗<class_GraphEdit_method_get_menu_hbox>`{.interpreted-text role="ref"}

Gets the `HBoxContainer<class_HBoxContainer>`{.interpreted-text
role="ref"} that contains the zooming and grid snap controls in the top
left of the graph. You can use this method to reposition the toolbar or
to add your own custom controls to it.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_is_node_connected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_node_connected**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_is_node_connected>`{.interpreted-text
role="ref"}

Returns `true` if the `from_port` of the `from_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} is connected
to the `to_port` of the `to_node`
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_is_valid_connection_type}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_connection_type**(from_type:
`int<class_int>`{.interpreted-text role="ref"}, to_type:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GraphEdit_method_is_valid_connection_type>`{.interpreted-text
role="ref"}

Returns whether it\'s possible to make a connection between two
different port types. The port type is defined individually for the left
and the right port of each slot with the
`GraphNode.set_slot()<class_GraphNode_method_set_slot>`{.interpreted-text
role="ref"} method.

See also
`add_valid_connection_type()<class_GraphEdit_method_add_valid_connection_type>`{.interpreted-text
role="ref"} and
`remove_valid_connection_type()<class_GraphEdit_method_remove_valid_connection_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_remove_valid_connection_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_valid_connection_type**(from_type:
`int<class_int>`{.interpreted-text role="ref"}, to_type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_remove_valid_connection_type>`{.interpreted-text
role="ref"}

Disallows the connection between two different port types previously
allowed by
`add_valid_connection_type()<class_GraphEdit_method_add_valid_connection_type>`{.interpreted-text
role="ref"}. The port type is defined individually for the left and the
right port of each slot with the
`GraphNode.set_slot()<class_GraphNode_method_set_slot>`{.interpreted-text
role="ref"} method.

See also
`is_valid_connection_type()<class_GraphEdit_method_is_valid_connection_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_remove_valid_left_disconnect_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_valid_left_disconnect_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_remove_valid_left_disconnect_type>`{.interpreted-text
role="ref"}

Disallows to disconnect nodes when dragging from the left port of the
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}\'s slot if it
has the specified type. Use this to disable disconnection previously
allowed with
`add_valid_left_disconnect_type()<class_GraphEdit_method_add_valid_left_disconnect_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_remove_valid_right_disconnect_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_valid_right_disconnect_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_remove_valid_right_disconnect_type>`{.interpreted-text
role="ref"}

Disallows to disconnect nodes when dragging from the right port of the
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"}\'s slot if it
has the specified type. Use this to disable disconnection previously
allowed with
`add_valid_right_disconnect_type()<class_GraphEdit_method_add_valid_right_disconnect_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_set_connection_activity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_connection_activity**(from_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_set_connection_activity>`{.interpreted-text
role="ref"}

Sets the coloration of the connection between `from_node`\'s `from_port`
and `to_node`\'s `to_port` with the color provided in the
`activity<class_GraphEdit_theme_color_activity>`{.interpreted-text
role="ref"} theme property. The color is linearly interpolated between
the connection color and the activity color using `amount` as weight.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_method_set_selected}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selected**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_GraphEdit_method_set_selected>`{.interpreted-text role="ref"}

Sets the specified `node` as the one selected.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_GraphEdit_theme_color_activity}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **activity** =
`Color(1, 1, 1, 1)`
`🔗<class_GraphEdit_theme_color_activity>`{.interpreted-text role="ref"}

Color the connection line is interpolated to based on the activity value
of a connection (see
`set_connection_activity()<class_GraphEdit_method_set_connection_activity>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_connection_hover_tint_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**connection_hover_tint_color** = `Color(0, 0, 0, 0.3)`
`🔗<class_GraphEdit_theme_color_connection_hover_tint_color>`{.interpreted-text
role="ref"}

Color which is blended with the connection line when the mouse is
hovering over it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_connection_rim_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**connection_rim_color** = `Color(0.1, 0.1, 0.1, 0.6)`
`🔗<class_GraphEdit_theme_color_connection_rim_color>`{.interpreted-text
role="ref"}

Color of the rim around each connection line used for making
intersecting lines more distinguishable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_connection_valid_target_tint_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**connection_valid_target_tint_color** = `Color(1, 1, 1, 0.4)`
`🔗<class_GraphEdit_theme_color_connection_valid_target_tint_color>`{.interpreted-text
role="ref"}

Color which is blended with the connection line when the currently
dragged connection is hovering over a valid target port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_grid_major}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **grid_major** =
`Color(1, 1, 1, 0.2)`
`🔗<class_GraphEdit_theme_color_grid_major>`{.interpreted-text
role="ref"}

Color of major grid lines/dots.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_grid_minor}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **grid_minor** =
`Color(1, 1, 1, 0.05)`
`🔗<class_GraphEdit_theme_color_grid_minor>`{.interpreted-text
role="ref"}

Color of minor grid lines/dots.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_selection_fill}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **selection_fill** =
`Color(1, 1, 1, 0.3)`
`🔗<class_GraphEdit_theme_color_selection_fill>`{.interpreted-text
role="ref"}

The fill color of the selection rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_color_selection_stroke}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **selection_stroke**
= `Color(1, 1, 1, 0.8)`
`🔗<class_GraphEdit_theme_color_selection_stroke>`{.interpreted-text
role="ref"}

The outline color of the selection rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_constant_connection_hover_thickness}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**connection_hover_thickness** = `0`
`🔗<class_GraphEdit_theme_constant_connection_hover_thickness>`{.interpreted-text
role="ref"}

Widen the line of the connection when the mouse is hovering over it by a
percentage factor. A value of `0` disables the highlight. A value of
`100` doubles the line width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_constant_port_hotzone_inner_extent}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**port_hotzone_inner_extent** = `22`
`🔗<class_GraphEdit_theme_constant_port_hotzone_inner_extent>`{.interpreted-text
role="ref"}

The horizontal range within which a port can be grabbed (inner side).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_constant_port_hotzone_outer_extent}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**port_hotzone_outer_extent** = `26`
`🔗<class_GraphEdit_theme_constant_port_hotzone_outer_extent>`{.interpreted-text
role="ref"}

The horizontal range within which a port can be grabbed (outer side).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_grid_toggle}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**grid_toggle**
`🔗<class_GraphEdit_theme_icon_grid_toggle>`{.interpreted-text
role="ref"}

The icon for the grid toggle button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_layout}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **layout**
`🔗<class_GraphEdit_theme_icon_layout>`{.interpreted-text role="ref"}

The icon for the layout button for auto-arranging the graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_minimap_toggle}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**minimap_toggle**
`🔗<class_GraphEdit_theme_icon_minimap_toggle>`{.interpreted-text
role="ref"}

The icon for the minimap toggle button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_snapping_toggle}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**snapping_toggle**
`🔗<class_GraphEdit_theme_icon_snapping_toggle>`{.interpreted-text
role="ref"}

The icon for the snapping toggle button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_zoom_in}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **zoom_in**
`🔗<class_GraphEdit_theme_icon_zoom_in>`{.interpreted-text role="ref"}

The icon for the zoom in button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_zoom_out}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **zoom_out**
`🔗<class_GraphEdit_theme_icon_zoom_out>`{.interpreted-text role="ref"}

The icon for the zoom out button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_icon_zoom_reset}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**zoom_reset**
`🔗<class_GraphEdit_theme_icon_zoom_reset>`{.interpreted-text
role="ref"}

The icon for the zoom reset button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_style_menu_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **menu_panel**
`🔗<class_GraphEdit_theme_style_menu_panel>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this theme property. Please help
us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_GraphEdit_theme_style_panel>`{.interpreted-text role="ref"}

The background drawn under the grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphEdit_theme_style_panel_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel_focus**
`🔗<class_GraphEdit_theme_style_panel_focus>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**GraphEdit** is focused (when used with assistive apps).
