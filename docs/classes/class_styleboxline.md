github_url
:   hide

# StyleBoxLine {#class_StyleBoxLine}

**Inherits:** `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that displays
a single line of a given color and thickness.

::: rst-class
classref-introduction-group
:::

## Description

A `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that displays
a single line of a given color and thickness. The line can be either
horizontal or vertical. Useful for separators.

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

:::: {#class_StyleBoxLine_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(0, 0, 0, 1)`
`🔗<class_StyleBoxLine_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The line\'s color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxLine_property_grow_begin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **grow_begin** =
`1.0` `🔗<class_StyleBoxLine_property_grow_begin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_grow_begin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_grow_begin**()

The number of pixels the line will extend before the **StyleBoxLine**\'s
bounds. If set to a negative value, the line will begin inside the
**StyleBoxLine**\'s bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxLine_property_grow_end}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **grow_end** = `1.0`
`🔗<class_StyleBoxLine_property_grow_end>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_grow_end**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_grow_end**()

The number of pixels the line will extend past the **StyleBoxLine**\'s
bounds. If set to a negative value, the line will end inside the
**StyleBoxLine**\'s bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxLine_property_thickness}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **thickness** = `1`
`🔗<class_StyleBoxLine_property_thickness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_thickness**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_thickness**()

The line\'s thickness in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBoxLine_property_vertical}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **vertical** = `false`
`🔗<class_StyleBoxLine_property_vertical>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_vertical**()

If `true`, the line will be vertical. If `false`, the line will be
horizontal.
