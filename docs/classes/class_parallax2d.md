github_url
:   hide

# Parallax2D {#class_Parallax2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node used to create a parallax scrolling background.

::: rst-class
classref-introduction-group
:::

## Description

A **Parallax2D** is used to create a parallax effect. It can move at a
different speed relative to the camera movement using
`scroll_scale<class_Parallax2D_property_scroll_scale>`{.interpreted-text
role="ref"}. This creates an illusion of depth in a 2D game. If manual
scrolling is desired, the `Camera2D<class_Camera2D>`{.interpreted-text
role="ref"} position can be ignored with
`ignore_camera_scroll<class_Parallax2D_property_ignore_camera_scroll>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Any changes to this node\'s position made after it enters
the scene tree will be overridden if
`ignore_camera_scroll<class_Parallax2D_property_ignore_camera_scroll>`{.interpreted-text
role="ref"} is `false` or
`screen_offset<class_Parallax2D_property_screen_offset>`{.interpreted-text
role="ref"} is modified.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D Parallax <../tutorials/2d/2d_parallax>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Parallax2D_property_autoscroll}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **autoscroll** =
`Vector2(0, 0)`
`🔗<class_Parallax2D_property_autoscroll>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoscroll**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_autoscroll**()

Velocity at which the offset scrolls automatically, in pixels per
second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_follow_viewport}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **follow_viewport** =
`true` `🔗<class_Parallax2D_property_follow_viewport>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_follow_viewport**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_follow_viewport**()

If `true`, this **Parallax2D** is offset by the current camera\'s
position. If the **Parallax2D** is in a
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"} separate
from the current camera, it may be desired to match the value with
`CanvasLayer.follow_viewport_enabled<class_CanvasLayer_property_follow_viewport_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_ignore_camera_scroll}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**ignore_camera_scroll** = `false`
`🔗<class_Parallax2D_property_ignore_camera_scroll>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ignore_camera_scroll**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_ignore_camera_scroll**()

If `true`, **Parallax2D**\'s position is not affected by the position of
the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_limit_begin}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **limit_begin** =
`Vector2(-10000000, -10000000)`
`🔗<class_Parallax2D_property_limit_begin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit_begin**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_limit_begin**()

Top-left limits for scrolling to begin. If the camera is outside of this
limit, the **Parallax2D** stops scrolling. Must be lower than
`limit_end<class_Parallax2D_property_limit_end>`{.interpreted-text
role="ref"} minus the viewport size to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_limit_end}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **limit_end** =
`Vector2(10000000, 10000000)`
`🔗<class_Parallax2D_property_limit_end>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit_end**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_limit_end**()

Bottom-right limits for scrolling to end. If the camera is outside of
this limit, the **Parallax2D** will stop scrolling. Must be higher than
`limit_begin<class_Parallax2D_property_limit_begin>`{.interpreted-text
role="ref"} and the viewport size combined to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_repeat_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **repeat_size** =
`Vector2(0, 0)`
`🔗<class_Parallax2D_property_repeat_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_repeat_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_repeat_size**()

Repeats the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
of each of this node\'s children and offsets them by this value. When
scrolling, the node\'s position loops, giving the illusion of an
infinite scrolling background if the values are larger than the screen
size. If an axis is set to `0`, the
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} will not be
repeated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_repeat_times}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **repeat_times** = `1`
`🔗<class_Parallax2D_property_repeat_times>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_repeat_times**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_repeat_times**()

Overrides the amount of times the texture repeats. Each texture copy
spreads evenly from the original by
`repeat_size<class_Parallax2D_property_repeat_size>`{.interpreted-text
role="ref"}. Useful for when zooming out with a camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_screen_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **screen_offset**
= `Vector2(0, 0)`
`🔗<class_Parallax2D_property_screen_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_screen_offset**()

Offset used to scroll this **Parallax2D**. This value is updated
automatically unless
`ignore_camera_scroll<class_Parallax2D_property_ignore_camera_scroll>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_scroll_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scroll_offset**
= `Vector2(0, 0)`
`🔗<class_Parallax2D_property_scroll_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_scroll_offset**()

The **Parallax2D**\'s offset. Similar to
`screen_offset<class_Parallax2D_property_screen_offset>`{.interpreted-text
role="ref"} and
`Node2D.position<class_Node2D_property_position>`{.interpreted-text
role="ref"}, but will not be overridden.

\*\*Note:\*\* Values will loop if
`repeat_size<class_Parallax2D_property_repeat_size>`{.interpreted-text
role="ref"} is set higher than `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Parallax2D_property_scroll_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scroll_scale**
= `Vector2(1, 1)`
`🔗<class_Parallax2D_property_scroll_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_scale**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_scroll_scale**()

Multiplier to the final **Parallax2D**\'s offset. Can be used to
simulate distance from the camera.

For example, a value of `1` scrolls at the same speed as the camera. A
value greater than `1` scrolls faster, making objects appear closer.
Less than `1` scrolls slower, making objects appear further, and a value
of `0` stops the objects completely.
