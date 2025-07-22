github_url
:   hide

# VisibleOnScreenNotifier2D {#class_VisibleOnScreenNotifier2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisibleOnScreenEnabler2D<class_VisibleOnScreenEnabler2D>`{.interpreted-text
role="ref"}

A rectangular region of 2D space that detects whether it is visible on
screen.

::: rst-class
classref-introduction-group
:::

## Description

**VisibleOnScreenNotifier2D** represents a rectangular region of 2D
space. When any part of this region becomes visible on screen or in a
viewport, it will emit a
`screen_entered<class_VisibleOnScreenNotifier2D_signal_screen_entered>`{.interpreted-text
role="ref"} signal, and likewise it will emit a
`screen_exited<class_VisibleOnScreenNotifier2D_signal_screen_exited>`{.interpreted-text
role="ref"} signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is
visible on screen, use
`VisibleOnScreenEnabler2D<class_VisibleOnScreenEnabler2D>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* **VisibleOnScreenNotifier2D** uses the render culling code
to determine whether it\'s visible on screen, so it won\'t function
unless
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} is set to `true`.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)

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

## Signals

:::: {#class_VisibleOnScreenNotifier2D_signal_screen_entered}
::: rst-class
classref-signal
:::
::::

**screen_entered**()
`🔗<class_VisibleOnScreenNotifier2D_signal_screen_entered>`{.interpreted-text
role="ref"}

Emitted when the VisibleOnScreenNotifier2D enters the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisibleOnScreenNotifier2D_signal_screen_exited}
::: rst-class
classref-signal
:::
::::

**screen_exited**()
`🔗<class_VisibleOnScreenNotifier2D_signal_screen_exited>`{.interpreted-text
role="ref"}

Emitted when the VisibleOnScreenNotifier2D exits the screen.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisibleOnScreenNotifier2D_property_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **rect** =
`Rect2(-10, -10, 20, 20)`
`🔗<class_VisibleOnScreenNotifier2D_property_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_rect**()

The VisibleOnScreenNotifier2D\'s bounding rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisibleOnScreenNotifier2D_property_show_rect}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_rect** = `true`
`🔗<class_VisibleOnScreenNotifier2D_property_show_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_rect**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_showing_rect**()

If `true`, shows the rectangle area of
`rect<class_VisibleOnScreenNotifier2D_property_rect>`{.interpreted-text
role="ref"} in the editor with a translucent magenta fill. Unlike
changing the visibility of the VisibleOnScreenNotifier2D, this does not
affect the screen culling detection.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VisibleOnScreenNotifier2D_method_is_on_screen}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_screen**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisibleOnScreenNotifier2D_method_is_on_screen>`{.interpreted-text
role="ref"}

If `true`, the bounding rectangle is on the screen.

\*\*Note:\*\* It takes one frame for the
**VisibleOnScreenNotifier2D**\'s visibility to be determined once added
to the scene tree, so this method will always return `false` right after
it is instantiated, before the draw pass.
