github_url
:   hide

# ParallaxLayer {#class_ParallaxLayer}

**Deprecated:** Use the `Parallax2D<class_Parallax2D>`{.interpreted-text
role="ref"} node instead.

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A parallax scrolling layer to be used with
`ParallaxBackground<class_ParallaxBackground>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A ParallaxLayer must be the child of a
`ParallaxBackground<class_ParallaxBackground>`{.interpreted-text
role="ref"} node. Each ParallaxLayer can be set to move at different
speeds relative to the camera movement or the
`ParallaxBackground.scroll_offset<class_ParallaxBackground_property_scroll_offset>`{.interpreted-text
role="ref"} value.

This node\'s children will be affected by its scroll offset.

\*\*Note:\*\* Any changes to this node\'s position and scale made after
it enters the scene will be ignored.

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

:::: {#class_ParallaxLayer_property_motion_mirroring}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**motion_mirroring** = `Vector2(0, 0)`
`🔗<class_ParallaxLayer_property_motion_mirroring>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mirroring**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_mirroring**()

The interval, in pixels, at which the **ParallaxLayer** is drawn
repeatedly. Useful for creating an infinitely scrolling background. If
an axis is set to `0`, the **ParallaxLayer** will be drawn only once
along that direction.

\*\*Note:\*\* If you want the repetition to pixel-perfect match a
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} displayed by
a child node, you should account for any scale applied to the texture
when defining this interval. For example, if you use a child
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} scaled to `0.5`
to display a 600x600 texture, and want this sprite to be repeated
continuously horizontally, you should set the mirroring to
`Vector2(300, 0)`.

\*\*Note:\*\* If the length of the viewport axis is bigger than twice
the repeated axis size, it will not repeat infinitely, as the parallax
layer only draws 2 instances of the layer at any given time. The
visibility window is calculated from the parent
`ParallaxBackground<class_ParallaxBackground>`{.interpreted-text
role="ref"}\'s position, not the layer\'s own position. So, if you use
mirroring, **do not** change the **ParallaxLayer** position relative to
its parent. Instead, if you need to adjust the background\'s position,
set the
`CanvasLayer.offset<class_CanvasLayer_property_offset>`{.interpreted-text
role="ref"} property in the parent
`ParallaxBackground<class_ParallaxBackground>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Despite the name, the layer will not be mirrored, it will
only be repeated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxLayer_property_motion_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **motion_offset**
= `Vector2(0, 0)`
`🔗<class_ParallaxLayer_property_motion_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_motion_offset**()

The ParallaxLayer\'s offset relative to the parent ParallaxBackground\'s
`ParallaxBackground.scroll_offset<class_ParallaxBackground_property_scroll_offset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParallaxLayer_property_motion_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **motion_scale**
= `Vector2(1, 1)`
`🔗<class_ParallaxLayer_property_motion_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion_scale**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_motion_scale**()

Multiplies the ParallaxLayer\'s motion. If an axis is set to `0`, it
will not scroll.
