github_url
:   hide

# Path2D {#class_Path2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Contains a `Curve2D<class_Curve2D>`{.interpreted-text role="ref"} path
for `PathFollow2D<class_PathFollow2D>`{.interpreted-text role="ref"}
nodes to follow.

::: rst-class
classref-introduction-group
:::

## Description

Can have `PathFollow2D<class_PathFollow2D>`{.interpreted-text
role="ref"} child nodes moving along the
`Curve2D<class_Curve2D>`{.interpreted-text role="ref"}. See
`PathFollow2D<class_PathFollow2D>`{.interpreted-text role="ref"} for
more information on usage.

\*\*Note:\*\* The path is considered as relative to the moved nodes
(children of `PathFollow2D<class_PathFollow2D>`{.interpreted-text
role="ref"}). As such, the curve should usually start with a zero vector
(`(0, 0)`).

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

:::: {#class_Path2D_property_curve}
::: rst-class
classref-property
:::
::::

`Curve2D<class_Curve2D>`{.interpreted-text role="ref"} **curve**
`🔗<class_Path2D_property_curve>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve**(value: `Curve2D<class_Curve2D>`{.interpreted-text
  role="ref"})
- `Curve2D<class_Curve2D>`{.interpreted-text role="ref"} **get_curve**()

A `Curve2D<class_Curve2D>`{.interpreted-text role="ref"} describing the
path.
