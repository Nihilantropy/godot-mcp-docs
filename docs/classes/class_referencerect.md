github_url
:   hide

# ReferenceRect {#class_ReferenceRect}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A rectangular box for designing UIs.

::: rst-class
classref-introduction-group
:::

## Description

A rectangular box that displays only a colored border around its
rectangle (see
`Control.get_rect()<class_Control_method_get_rect>`{.interpreted-text
role="ref"}). It can be used to visualize the extents of a
`Control<class_Control>`{.interpreted-text role="ref"} node, for testing
purposes.

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

:::: {#class_ReferenceRect_property_border_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **border_color** =
`Color(1, 0, 0, 1)`
`🔗<class_ReferenceRect_property_border_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_border_color**()

Sets the border color of the **ReferenceRect**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReferenceRect_property_border_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **border_width** =
`1.0` `🔗<class_ReferenceRect_property_border_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_border_width**()

Sets the border width of the **ReferenceRect**. The border grows both
inwards and outwards with respect to the rectangle box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReferenceRect_property_editor_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editor_only** =
`true` `🔗<class_ReferenceRect_property_editor_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editor_only**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_editor_only**()

If `true`, the **ReferenceRect** will only be visible while in editor.
Otherwise, **ReferenceRect** will be visible in the running project.
