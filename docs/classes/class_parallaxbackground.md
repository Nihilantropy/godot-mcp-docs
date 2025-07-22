github_url
:   hide

# ParallaxBackground {#class_ParallaxBackground}

**Deprecated:** Use the `Parallax2D<class_Parallax2D>`{.interpreted-text
role="ref"} node instead.

**Inherits:** `CanvasLayer<class_CanvasLayer>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A node used to create a parallax scrolling background.

::: rst-class
classref-introduction-group
:::

## Description

A ParallaxBackground uses one or more
`ParallaxLayer<class_ParallaxLayer>`{.interpreted-text role="ref"} child
nodes to create a parallax effect. Each
`ParallaxLayer<class_ParallaxLayer>`{.interpreted-text role="ref"} can
move at a different speed using
`ParallaxLayer.motion_offset<class_ParallaxLayer_property_motion_offset>`{.interpreted-text
role="ref"}. This creates an illusion of depth in a 2D game. If not used
with a `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}, you
must manually calculate the
`scroll_offset<class_ParallaxBackground_property_scroll_offset>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Each **ParallaxBackground** is drawn on one specific
`Viewport<class_Viewport>`{.interpreted-text role="ref"} and cannot be
shared between multiple `Viewport<class_Viewport>`{.interpreted-text
role="ref"}s, see
`CanvasLayer.custom_viewport<class_CanvasLayer_property_custom_viewport>`{.interpreted-text
role="ref"}. When using multiple
`Viewport<class_Viewport>`{.interpreted-text role="ref"}s, for example
in a split-screen game, you need create an individual
**ParallaxBackground** for each
`Viewport<class_Viewport>`{.interpreted-text role="ref"} you want it to
be drawn on.

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

:::: {#class_ParallaxBackground_property_scroll_base_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**scroll_base_offset** = `Vector2(0, 0)`
`🔗<class_ParallaxBackground_property_scroll_base_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_base_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_scroll_base_offset**()

The base position offset for all
`ParallaxLayer<class_ParallaxLayer>`{.interpreted-text role="ref"}
children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxBackground_property_scroll_base_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**scroll_base_scale** = `Vector2(1, 1)`
`🔗<class_ParallaxBackground_property_scroll_base_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_base_scale**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_scroll_base_scale**()

The base motion scale for all
`ParallaxLayer<class_ParallaxLayer>`{.interpreted-text role="ref"}
children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxBackground_property_scroll_ignore_camera_zoom}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_ignore_camera_zoom** = `false`
`🔗<class_ParallaxBackground_property_scroll_ignore_camera_zoom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ignore_camera_zoom**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_ignore_camera_zoom**()

If `true`, elements in
`ParallaxLayer<class_ParallaxLayer>`{.interpreted-text role="ref"} child
aren\'t affected by the zoom level of the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxBackground_property_scroll_limit_begin}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**scroll_limit_begin** = `Vector2(0, 0)`
`🔗<class_ParallaxBackground_property_scroll_limit_begin>`{.interpreted-text
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
limit, the background will stop scrolling. Must be lower than
`scroll_limit_end<class_ParallaxBackground_property_scroll_limit_end>`{.interpreted-text
role="ref"} to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxBackground_property_scroll_limit_end}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**scroll_limit_end** = `Vector2(0, 0)`
`🔗<class_ParallaxBackground_property_scroll_limit_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_limit_end**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_limit_end**()

Bottom-right limits for scrolling to end. If the camera is outside of
this limit, the background will stop scrolling. Must be higher than
`scroll_limit_begin<class_ParallaxBackground_property_scroll_limit_begin>`{.interpreted-text
role="ref"} to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxBackground_property_scroll_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scroll_offset**
= `Vector2(0, 0)`
`🔗<class_ParallaxBackground_property_scroll_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_scroll_offset**()

The ParallaxBackground\'s scroll value. Calculated automatically when
using a `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}, but
can be used to manually manage scrolling when no camera is present.
