github_url
:   hide

# Camera2D {#class_Camera2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Camera node for 2D scenes.

::: rst-class
classref-introduction-group
:::

## Description

Camera node for 2D scenes. It forces the screen (current layer) to
scroll following this node. This makes it easier (and faster) to program
scrollable scenes than manually changing the position of
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}-based
nodes.

Cameras register themselves in the nearest
`Viewport<class_Viewport>`{.interpreted-text role="ref"} node (when
ascending the tree). Only one camera can be active per viewport. If no
viewport is available ascending the tree, the camera will register in
the global viewport.

This node is intended to be a simple helper to get things going quickly,
but more functionality may be desired to change how the camera works. To
make your own custom camera node, inherit it from
`Node2D<class_Node2D>`{.interpreted-text role="ref"} and change the
transform of the canvas by setting
`Viewport.canvas_transform<class_Viewport_property_canvas_transform>`{.interpreted-text
role="ref"} in `Viewport<class_Viewport>`{.interpreted-text role="ref"}
(you can obtain the current `Viewport<class_Viewport>`{.interpreted-text
role="ref"} by using
`Node.get_viewport()<class_Node_method_get_viewport>`{.interpreted-text
role="ref"}).

Note that the **Camera2D** node\'s
`Node2D.global_position<class_Node2D_property_global_position>`{.interpreted-text
role="ref"} doesn\'t represent the actual position of the screen, which
may differ due to applied smoothing or limits. You can use
`get_screen_center_position()<class_Camera2D_method_get_screen_center_position>`{.interpreted-text
role="ref"} to get the real position. Same for the node\'s
`Node2D.global_rotation<class_Node2D_property_global_rotation>`{.interpreted-text
role="ref"} which may be different due to applied rotation smoothing.
You can use
`get_screen_rotation()<class_Camera2D_method_get_screen_rotation>`{.interpreted-text
role="ref"} to get the current rotation of the screen.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)
- [2D Isometric Demo](https://godotengine.org/asset-library/asset/2718)

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

:::: {#enum_Camera2D_AnchorMode}
::: rst-class
classref-enumeration
:::
::::

enum **AnchorMode**: `🔗<enum_Camera2D_AnchorMode>`{.interpreted-text
role="ref"}

:::: {#class_Camera2D_constant_ANCHOR_MODE_FIXED_TOP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`AnchorMode<enum_Camera2D_AnchorMode>`{.interpreted-text role="ref"}
**ANCHOR_MODE_FIXED_TOP_LEFT** = `0`

The camera\'s position is fixed so that the top-left corner is always at
the origin.

:::: {#class_Camera2D_constant_ANCHOR_MODE_DRAG_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`AnchorMode<enum_Camera2D_AnchorMode>`{.interpreted-text role="ref"}
**ANCHOR_MODE_DRAG_CENTER** = `1`

The camera\'s position takes into account vertical/horizontal offsets
and the screen size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Camera2D_Camera2DProcessCallback}
::: rst-class
classref-enumeration
:::
::::

enum **Camera2DProcessCallback**:
`🔗<enum_Camera2D_Camera2DProcessCallback>`{.interpreted-text
role="ref"}

:::: {#class_Camera2D_constant_CAMERA2D_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>`{.interpreted-text
role="ref"} **CAMERA2D_PROCESS_PHYSICS** = `0`

The camera updates during physics frames (see
`Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_Camera2D_constant_CAMERA2D_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>`{.interpreted-text
role="ref"} **CAMERA2D_PROCESS_IDLE** = `1`

The camera updates during process frames (see
`Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Camera2D_property_anchor_mode}
::: rst-class
classref-property
:::
::::

`AnchorMode<enum_Camera2D_AnchorMode>`{.interpreted-text role="ref"}
**anchor_mode** = `1`
`🔗<class_Camera2D_property_anchor_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_anchor_mode**(value:
  `AnchorMode<enum_Camera2D_AnchorMode>`{.interpreted-text role="ref"})
- `AnchorMode<enum_Camera2D_AnchorMode>`{.interpreted-text role="ref"}
  **get_anchor_mode**()

The Camera2D\'s anchor point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_custom_viewport}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **custom_viewport**
`🔗<class_Camera2D_property_custom_viewport>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_viewport**(value: `Node<class_Node>`{.interpreted-text
  role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"}
  **get_custom_viewport**()

The custom `Viewport<class_Viewport>`{.interpreted-text role="ref"} node
attached to the **Camera2D**. If `null` or not a
`Viewport<class_Viewport>`{.interpreted-text role="ref"}, uses the
default viewport instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_bottom_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**drag_bottom_margin** = `0.2`
`🔗<class_Camera2D_property_drag_bottom_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  drag_margin: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Bottom margin needed to drag the camera. A value of `1` makes the camera
move only when reaching the bottom edge of the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_horizontal_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_horizontal_enabled** = `false`
`🔗<class_Camera2D_property_drag_horizontal_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_horizontal_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drag_horizontal_enabled**()

If `true`, the camera only moves when reaching the horizontal (left and
right) drag margins. If `false`, the camera moves horizontally
regardless of margins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_horizontal_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**drag_horizontal_offset** = `0.0`
`🔗<class_Camera2D_property_drag_horizontal_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_horizontal_offset**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_horizontal_offset**()

The relative horizontal drag offset of the camera between the right
(`-1`) and left (`1`) drag margins.

\*\*Note:\*\* Used to set the initial horizontal drag offset; determine
the current offset; or force the current offset. It\'s not automatically
updated when
`drag_horizontal_enabled<class_Camera2D_property_drag_horizontal_enabled>`{.interpreted-text
role="ref"} is `true` or the drag margins are changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_left_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **drag_left_margin**
= `0.2` `🔗<class_Camera2D_property_drag_left_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  drag_margin: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Left margin needed to drag the camera. A value of `1` makes the camera
move only when reaching the left edge of the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_right_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **drag_right_margin**
= `0.2`
`🔗<class_Camera2D_property_drag_right_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  drag_margin: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Right margin needed to drag the camera. A value of `1` makes the camera
move only when reaching the right edge of the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_top_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **drag_top_margin** =
`0.2` `🔗<class_Camera2D_property_drag_top_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  drag_margin: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Top margin needed to drag the camera. A value of `1` makes the camera
move only when reaching the top edge of the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_vertical_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_vertical_enabled** = `false`
`🔗<class_Camera2D_property_drag_vertical_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_vertical_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drag_vertical_enabled**()

If `true`, the camera only moves when reaching the vertical (top and
bottom) drag margins. If `false`, the camera moves vertically regardless
of the drag margins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_drag_vertical_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**drag_vertical_offset** = `0.0`
`🔗<class_Camera2D_property_drag_vertical_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_vertical_offset**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_vertical_offset**()

The relative vertical drag offset of the camera between the bottom
(`-1`) and top (`1`) drag margins.

\*\*Note:\*\* Used to set the initial vertical drag offset; determine
the current offset; or force the current offset. It\'s not automatically
updated when
`drag_vertical_enabled<class_Camera2D_property_drag_vertical_enabled>`{.interpreted-text
role="ref"} is `true` or the drag margins are changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_editor_draw_drag_margin}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor_draw_drag_margin** = `false`
`🔗<class_Camera2D_property_editor_draw_drag_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin_drawing_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_margin_drawing_enabled**()

If `true`, draws the camera\'s drag margin rectangle in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_editor_draw_limits}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editor_draw_limits**
= `false`
`🔗<class_Camera2D_property_editor_draw_limits>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit_drawing_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_limit_drawing_enabled**()

If `true`, draws the camera\'s limits rectangle in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_editor_draw_screen}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editor_draw_screen**
= `true`
`🔗<class_Camera2D_property_editor_draw_screen>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_drawing_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_screen_drawing_enabled**()

If `true`, draws the camera\'s screen rectangle in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_Camera2D_property_enabled>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

Controls whether the camera can be active or not. If `true`, the
**Camera2D** will become the main camera when it enters the scene tree
and there is no active camera currently (see
`Viewport.get_camera_2d()<class_Viewport_method_get_camera_2d>`{.interpreted-text
role="ref"}).

When the camera is currently active and
`enabled<class_Camera2D_property_enabled>`{.interpreted-text role="ref"}
is set to `false`, the next enabled **Camera2D** in the scene tree will
become active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_ignore_rotation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ignore_rotation** =
`true` `🔗<class_Camera2D_property_ignore_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ignore_rotation**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_ignoring_rotation**()

If `true`, the camera\'s rendered view is not affected by its
`Node2D.rotation<class_Node2D_property_rotation>`{.interpreted-text
role="ref"} and
`Node2D.global_rotation<class_Node2D_property_global_rotation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_limit_bottom}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **limit_bottom** =
`10000000` `🔗<class_Camera2D_property_limit_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit**(margin: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, limit: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_limit**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Bottom scroll limit in pixels. The camera stops moving when reaching
this value, but
`offset<class_Camera2D_property_offset>`{.interpreted-text role="ref"}
can push the view past the limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_limit_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **limit_enabled** =
`true` `🔗<class_Camera2D_property_limit_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_limit_enabled**()

If `true`, the limits will be enabled. Disabling this will allow the
camera to focus anywhere, when the four `limit_*` properties will not
work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_limit_left}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **limit_left** =
`-10000000` `🔗<class_Camera2D_property_limit_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit**(margin: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, limit: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_limit**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Left scroll limit in pixels. The camera stops moving when reaching this
value, but `offset<class_Camera2D_property_offset>`{.interpreted-text
role="ref"} can push the view past the limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_limit_right}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **limit_right** =
`10000000` `🔗<class_Camera2D_property_limit_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit**(margin: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, limit: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_limit**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Right scroll limit in pixels. The camera stops moving when reaching this
value, but `offset<class_Camera2D_property_offset>`{.interpreted-text
role="ref"} can push the view past the limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_limit_smoothed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **limit_smoothed** =
`false` `🔗<class_Camera2D_property_limit_smoothed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit_smoothing_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_limit_smoothing_enabled**()

If `true`, the camera smoothly stops when reaches its limits.

This property has no effect if
`position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>`{.interpreted-text
role="ref"} is `false`.

\*\*Note:\*\* To immediately update the camera\'s position to be within
limits without smoothing, even with this setting enabled, invoke
`reset_smoothing()<class_Camera2D_method_reset_smoothing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_limit_top}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **limit_top** =
`-10000000` `🔗<class_Camera2D_property_limit_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit**(margin: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, limit: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_limit**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Top scroll limit in pixels. The camera stops moving when reaching this
value, but `offset<class_Camera2D_property_offset>`{.interpreted-text
role="ref"} can push the view past the limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)` `🔗<class_Camera2D_property_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The camera\'s relative offset. Useful for looking around or camera shake
animations. The offsetted camera can go past the limits defined in
`limit_top<class_Camera2D_property_limit_top>`{.interpreted-text
role="ref"},
`limit_bottom<class_Camera2D_property_limit_bottom>`{.interpreted-text
role="ref"},
`limit_left<class_Camera2D_property_limit_left>`{.interpreted-text
role="ref"} and
`limit_right<class_Camera2D_property_limit_right>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_position_smoothing_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**position_smoothing_enabled** = `false`
`🔗<class_Camera2D_property_position_smoothing_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position_smoothing_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_position_smoothing_enabled**()

If `true`, the camera\'s view smoothly moves towards its target position
at
`position_smoothing_speed<class_Camera2D_property_position_smoothing_speed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_position_smoothing_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**position_smoothing_speed** = `5.0`
`🔗<class_Camera2D_property_position_smoothing_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position_smoothing_speed**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_position_smoothing_speed**()

Speed in pixels per second of the camera\'s smoothing effect when
`position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_process_callback}
::: rst-class
classref-property
:::
::::

`Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>`{.interpreted-text
role="ref"} **process_callback** = `1`
`🔗<class_Camera2D_property_process_callback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_callback**(value:
  `Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>`{.interpreted-text
  role="ref"})
- `Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>`{.interpreted-text
  role="ref"} **get_process_callback**()

The camera\'s process callback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_rotation_smoothing_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rotation_smoothing_enabled** = `false`
`🔗<class_Camera2D_property_rotation_smoothing_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_smoothing_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_rotation_smoothing_enabled**()

If `true`, the camera\'s view smoothly rotates, via asymptotic
smoothing, to align with its target rotation at
`rotation_smoothing_speed<class_Camera2D_property_rotation_smoothing_speed>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property has no effect if
`ignore_rotation<class_Camera2D_property_ignore_rotation>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_rotation_smoothing_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rotation_smoothing_speed** = `5.0`
`🔗<class_Camera2D_property_rotation_smoothing_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_smoothing_speed**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_rotation_smoothing_speed**()

The angular, asymptotic speed of the camera\'s rotation smoothing effect
when
`rotation_smoothing_enabled<class_Camera2D_property_rotation_smoothing_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_property_zoom}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **zoom** =
`Vector2(1, 1)` `🔗<class_Camera2D_property_zoom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_zoom**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_zoom**()

The camera\'s zoom. Higher values are more zoomed in. For example, a
zoom of `Vector2(2.0, 2.0)` will be twice as zoomed in on each axis (the
view covers an area four times smaller). In contrast, a zoom of
`Vector2(0.5, 0.5)` will be twice as zoomed out on each axis (the view
covers an area four times larger). The X and Y components should
generally always be set to the same value, unless you wish to stretch
the camera view.

\*\*Note:\*\*
`FontFile.oversampling<class_FontFile_property_oversampling>`{.interpreted-text
role="ref"} does *not* take **Camera2D** zoom into account. This means
that zooming in/out will cause bitmap fonts and rasterized (non-MSDF)
dynamic fonts to appear blurry or pixelated unless the font is part of a
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"} that
makes it ignore camera zoom. To ensure text remains crisp regardless of
zoom, you can enable MSDF font rendering by enabling
`ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field<class_ProjectSettings_property_gui/theme/default_font_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} (applies to the default project font only), or enabling
**Multichannel Signed Distance Field** in the import options of a
DynamicFont for custom fonts. On system fonts,
`SystemFont.multichannel_signed_distance_field<class_SystemFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} can be enabled in the inspector.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Camera2D_method_align}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **align**()
`🔗<class_Camera2D_method_align>`{.interpreted-text role="ref"}

Aligns the camera to the tracked node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_force_update_scroll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_scroll**()
`🔗<class_Camera2D_method_force_update_scroll>`{.interpreted-text
role="ref"}

Forces the camera to update scroll immediately.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_get_drag_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_drag_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera2D_method_get_drag_margin>`{.interpreted-text
role="ref"}

Returns the specified `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}\'s margin. See also
`drag_bottom_margin<class_Camera2D_property_drag_bottom_margin>`{.interpreted-text
role="ref"},
`drag_top_margin<class_Camera2D_property_drag_top_margin>`{.interpreted-text
role="ref"},
`drag_left_margin<class_Camera2D_property_drag_left_margin>`{.interpreted-text
role="ref"}, and
`drag_right_margin<class_Camera2D_property_drag_right_margin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_get_limit}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_limit**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Camera2D_method_get_limit>`{.interpreted-text
role="ref"}

Returns the camera limit for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}. See also
`limit_bottom<class_Camera2D_property_limit_bottom>`{.interpreted-text
role="ref"},
`limit_top<class_Camera2D_property_limit_top>`{.interpreted-text
role="ref"},
`limit_left<class_Camera2D_property_limit_left>`{.interpreted-text
role="ref"}, and
`limit_right<class_Camera2D_property_limit_right>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_get_screen_center_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_screen_center_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera2D_method_get_screen_center_position>`{.interpreted-text
role="ref"}

Returns the center of the screen from this camera\'s point of view, in
global coordinates.

\*\*Note:\*\* The exact targeted position of the camera may be
different. See
`get_target_position()<class_Camera2D_method_get_target_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_get_screen_rotation}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_screen_rotation**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera2D_method_get_screen_rotation>`{.interpreted-text
role="ref"}

Returns the current screen rotation from this camera\'s point of view.

\*\*Note:\*\* The screen rotation can be different from
`Node2D.global_rotation<class_Node2D_property_global_rotation>`{.interpreted-text
role="ref"} if the camera is rotating smoothly due to
`rotation_smoothing_enabled<class_Camera2D_property_rotation_smoothing_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_get_target_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_target_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera2D_method_get_target_position>`{.interpreted-text
role="ref"}

Returns this camera\'s target position, in global coordinates.

\*\*Note:\*\* The returned value is not the same as
`Node2D.global_position<class_Node2D_property_global_position>`{.interpreted-text
role="ref"}, as it is affected by the drag properties. It is also not
the same as the current position if
`position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>`{.interpreted-text
role="ref"} is `true` (see
`get_screen_center_position()<class_Camera2D_method_get_screen_center_position>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_is_current}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_current**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Camera2D_method_is_current>`{.interpreted-text
role="ref"}

Returns `true` if this **Camera2D** is the active camera (see
`Viewport.get_camera_2d()<class_Viewport_method_get_camera_2d>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_make_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_current**()
`🔗<class_Camera2D_method_make_current>`{.interpreted-text role="ref"}

Forces this **Camera2D** to become the current active one.
`enabled<class_Camera2D_property_enabled>`{.interpreted-text role="ref"}
must be `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_reset_smoothing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_smoothing**()
`🔗<class_Camera2D_method_reset_smoothing>`{.interpreted-text
role="ref"}

Sets the camera\'s position immediately to its current smoothing
destination.

This method has no effect if
`position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_set_drag_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_drag_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
drag_margin: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Camera2D_method_set_drag_margin>`{.interpreted-text
role="ref"}

Sets the specified `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}\'s margin. See also
`drag_bottom_margin<class_Camera2D_property_drag_bottom_margin>`{.interpreted-text
role="ref"},
`drag_top_margin<class_Camera2D_property_drag_top_margin>`{.interpreted-text
role="ref"},
`drag_left_margin<class_Camera2D_property_drag_left_margin>`{.interpreted-text
role="ref"}, and
`drag_right_margin<class_Camera2D_property_drag_right_margin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera2D_method_set_limit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_limit**(margin: `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}, limit: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Camera2D_method_set_limit>`{.interpreted-text role="ref"}

Sets the camera limit for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}. See also
`limit_bottom<class_Camera2D_property_limit_bottom>`{.interpreted-text
role="ref"},
`limit_top<class_Camera2D_property_limit_top>`{.interpreted-text
role="ref"},
`limit_left<class_Camera2D_property_limit_left>`{.interpreted-text
role="ref"}, and
`limit_right<class_Camera2D_property_limit_right>`{.interpreted-text
role="ref"}.
