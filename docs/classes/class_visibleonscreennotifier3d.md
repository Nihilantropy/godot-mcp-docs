github_url
:   hide

# VisibleOnScreenNotifier3D {#class_VisibleOnScreenNotifier3D}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisibleOnScreenEnabler3D<class_VisibleOnScreenEnabler3D>`{.interpreted-text
role="ref"}

A box-shaped region of 3D space that detects whether it is visible on
screen.

::: rst-class
classref-introduction-group
:::

## Description

**VisibleOnScreenNotifier3D** represents a box-shaped region of 3D
space. When any part of this region becomes visible on screen or in a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}\'s view, it
will emit a
`screen_entered<class_VisibleOnScreenNotifier3D_signal_screen_entered>`{.interpreted-text
role="ref"} signal, and likewise it will emit a
`screen_exited<class_VisibleOnScreenNotifier3D_signal_screen_exited>`{.interpreted-text
role="ref"} signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is
visible on screen, use
`VisibleOnScreenEnabler3D<class_VisibleOnScreenEnabler3D>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* **VisibleOnScreenNotifier3D** uses an approximate
heuristic that doesn\'t take walls and other occlusion into account,
unless occlusion culling is used. It also won\'t function unless
`Node3D.visible<class_Node3D_property_visible>`{.interpreted-text
role="ref"} is set to `true`.

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

:::: {#class_VisibleOnScreenNotifier3D_signal_screen_entered}
::: rst-class
classref-signal
:::
::::

**screen_entered**()
`🔗<class_VisibleOnScreenNotifier3D_signal_screen_entered>`{.interpreted-text
role="ref"}

Emitted when the **VisibleOnScreenNotifier3D** enters the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisibleOnScreenNotifier3D_signal_screen_exited}
::: rst-class
classref-signal
:::
::::

**screen_exited**()
`🔗<class_VisibleOnScreenNotifier3D_signal_screen_exited>`{.interpreted-text
role="ref"}

Emitted when the **VisibleOnScreenNotifier3D** exits the screen.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisibleOnScreenNotifier3D_property_aabb}
::: rst-class
classref-property
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **aabb** =
`AABB(-1, -1, -1, 2, 2, 2)`
`🔗<class_VisibleOnScreenNotifier3D_property_aabb>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_aabb**(value: `AABB<class_AABB>`{.interpreted-text role="ref"})
- `AABB<class_AABB>`{.interpreted-text role="ref"} **get_aabb**()

The **VisibleOnScreenNotifier3D**\'s bounding box.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VisibleOnScreenNotifier3D_method_is_on_screen}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_screen**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisibleOnScreenNotifier3D_method_is_on_screen>`{.interpreted-text
role="ref"}

Returns `true` if the bounding box is on the screen.

\*\*Note:\*\* It takes one frame for the
**VisibleOnScreenNotifier3D**\'s visibility to be assessed once added to
the scene tree, so this method will always return `false` right after it
is instantiated.
