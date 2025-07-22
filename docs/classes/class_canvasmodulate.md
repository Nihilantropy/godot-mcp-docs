github_url
:   hide

::: {.meta keywords="color"}
:::

# CanvasModulate {#class_CanvasModulate}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that applies a color tint to a canvas.

::: rst-class
classref-introduction-group
:::

## Description

**CanvasModulate** applies a color tint to all nodes on a canvas. Only
one can be used to tint a canvas, but
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}s can be
used to render things independently.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>`{.interpreted-text
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

:::: {#class_CanvasModulate_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)`
`🔗<class_CanvasModulate_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The tint color to apply.
