github_url
:   hide

# Path3D {#class_Path3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Contains a `Curve3D<class_Curve3D>`{.interpreted-text role="ref"} path
for `PathFollow3D<class_PathFollow3D>`{.interpreted-text role="ref"}
nodes to follow.

::: rst-class
classref-introduction-group
:::

## Description

Can have `PathFollow3D<class_PathFollow3D>`{.interpreted-text
role="ref"} child nodes moving along the
`Curve3D<class_Curve3D>`{.interpreted-text role="ref"}. See
`PathFollow3D<class_PathFollow3D>`{.interpreted-text role="ref"} for
more information on the usage.

Note that the path is considered as relative to the moved nodes
(children of `PathFollow3D<class_PathFollow3D>`{.interpreted-text
role="ref"}). As such, the curve should usually start with a zero vector
`(0, 0, 0)`.

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

## Signals

:::: {#class_Path3D_signal_curve_changed}
::: rst-class
classref-signal
:::
::::

**curve_changed**()
`🔗<class_Path3D_signal_curve_changed>`{.interpreted-text role="ref"}

Emitted when the `curve<class_Path3D_property_curve>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Path3D_signal_debug_color_changed}
::: rst-class
classref-signal
:::
::::

**debug_color_changed**()
`🔗<class_Path3D_signal_debug_color_changed>`{.interpreted-text
role="ref"}

Emitted when the
`debug_custom_color<class_Path3D_property_debug_custom_color>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Path3D_property_curve}
::: rst-class
classref-property
:::
::::

`Curve3D<class_Curve3D>`{.interpreted-text role="ref"} **curve**
`🔗<class_Path3D_property_curve>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve**(value: `Curve3D<class_Curve3D>`{.interpreted-text
  role="ref"})
- `Curve3D<class_Curve3D>`{.interpreted-text role="ref"} **get_curve**()

A `Curve3D<class_Curve3D>`{.interpreted-text role="ref"} describing the
path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Path3D_property_debug_custom_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug_custom_color** = `Color(0, 0, 0, 1)`
`🔗<class_Path3D_property_debug_custom_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_custom_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_debug_custom_color**()

The custom color to use to draw the shape in the editor.

If set to `Color(0.0, 0.0, 0.0)` (by default), the color set in
EditorSettings is used.
