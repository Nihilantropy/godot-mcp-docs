github_url
:   hide

# LabelSettings {#class_LabelSettings}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides common settings to customize the text in a
`Label<class_Label>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**LabelSettings** is a resource that provides common settings to
customize the text in a `Label<class_Label>`{.interpreted-text
role="ref"}. It will take priority over the properties defined in
`Control.theme<class_Control_property_theme>`{.interpreted-text
role="ref"}. The resource can be shared between multiple labels and
changed on the fly, so it\'s convenient and flexible way to setup text
style.

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

## Property Descriptions

:::: {#class_LabelSettings_property_font}
::: rst-class
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_LabelSettings_property_font>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font**(value: `Font<class_Font>`{.interpreted-text role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"} **get_font**()

`Font<class_Font>`{.interpreted-text role="ref"} used for the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_font_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(1, 1, 1, 1)`
`🔗<class_LabelSettings_property_font_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_font_color**()

Color of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size** = `16`
`🔗<class_LabelSettings_property_font_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_size**()

Size of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_line_spacing}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **line_spacing** =
`3.0` `🔗<class_LabelSettings_property_line_spacing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_spacing**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_outline_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **outline_color** =
`Color(1, 1, 1, 1)`
`🔗<class_LabelSettings_property_outline_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_outline_color**()

The color of the outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_outline_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_LabelSettings_property_outline_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_outline_size**()

Text outline size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_paragraph_spacing}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **paragraph_spacing**
= `0.0`
`🔗<class_LabelSettings_property_paragraph_spacing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_paragraph_spacing**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_paragraph_spacing**()

Vertical space between paragraphs. Added on top of
`line_spacing<class_LabelSettings_property_line_spacing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_shadow_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **shadow_color** =
`Color(0, 0, 0, 0)`
`🔗<class_LabelSettings_property_shadow_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_shadow_color**()

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_shadow_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **shadow_offset**
= `Vector2(1, 1)`
`🔗<class_LabelSettings_property_shadow_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_shadow_offset**()

Offset of the shadow effect, in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_shadow_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_size** = `1`
`🔗<class_LabelSettings_property_shadow_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_shadow_size**()

Size of the shadow effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_stacked_outline_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stacked_outline_count**
= `0`
`🔗<class_LabelSettings_property_stacked_outline_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stacked_outline_count**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stacked_outline_count**()

The number of stacked outlines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_stacked_shadow_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stacked_shadow_count**
= `0`
`🔗<class_LabelSettings_property_stacked_shadow_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stacked_shadow_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stacked_shadow_count**()

The number of stacked shadows.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_LabelSettings_method_add_stacked_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_stacked_outline**(index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_LabelSettings_method_add_stacked_outline>`{.interpreted-text
role="ref"}

Adds a new stacked outline to the label at the given `index`. If `index`
is `-1`, the new stacked outline will be added at the end of the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_add_stacked_shadow}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_stacked_shadow**(index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_LabelSettings_method_add_stacked_shadow>`{.interpreted-text
role="ref"}

Adds a new stacked shadow to the label at the given `index`. If `index`
is `-1`, the new stacked shadow will be added at the end of the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_get_stacked_outline_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_stacked_outline_color**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LabelSettings_method_get_stacked_outline_color>`{.interpreted-text
role="ref"}

Returns the color of the stacked outline at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_get_stacked_outline_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_stacked_outline_size**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LabelSettings_method_get_stacked_outline_size>`{.interpreted-text
role="ref"}

Returns the size of the stacked outline at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_get_stacked_shadow_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_stacked_shadow_color**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LabelSettings_method_get_stacked_shadow_color>`{.interpreted-text
role="ref"}

Returns the color of the stacked shadow at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_get_stacked_shadow_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_stacked_shadow_offset**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LabelSettings_method_get_stacked_shadow_offset>`{.interpreted-text
role="ref"}

Returns the offset of the stacked shadow at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_get_stacked_shadow_outline_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_stacked_shadow_outline_size**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LabelSettings_method_get_stacked_shadow_outline_size>`{.interpreted-text
role="ref"}

Returns the outline size of the stacked shadow at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_move_stacked_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_stacked_outline**(from_index: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_LabelSettings_method_move_stacked_outline>`{.interpreted-text
role="ref"}

Moves the stacked outline at index `from_index` to the given position
`to_position` in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_move_stacked_shadow}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_stacked_shadow**(from_index: `int<class_int>`{.interpreted-text
role="ref"}, to_position: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_LabelSettings_method_move_stacked_shadow>`{.interpreted-text
role="ref"}

Moves the stacked shadow at index `from_index` to the given position
`to_position` in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_remove_stacked_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_stacked_outline**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_LabelSettings_method_remove_stacked_outline>`{.interpreted-text
role="ref"}

Removes the stacked outline at index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_remove_stacked_shadow}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_stacked_shadow**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_LabelSettings_method_remove_stacked_shadow>`{.interpreted-text
role="ref"}

Removes the stacked shadow at index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_set_stacked_outline_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stacked_outline_color**(index: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_LabelSettings_method_set_stacked_outline_color>`{.interpreted-text
role="ref"}

Sets the color of the stacked outline identified by the given `index` to
`color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_set_stacked_outline_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stacked_outline_size**(index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_LabelSettings_method_set_stacked_outline_size>`{.interpreted-text
role="ref"}

Sets the size of the stacked outline identified by the given `index` to
`size`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_set_stacked_shadow_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stacked_shadow_color**(index: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_LabelSettings_method_set_stacked_shadow_color>`{.interpreted-text
role="ref"}

Sets the color of the stacked shadow identified by the given `index` to
`color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_set_stacked_shadow_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stacked_shadow_offset**(index: `int<class_int>`{.interpreted-text
role="ref"}, offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_LabelSettings_method_set_stacked_shadow_offset>`{.interpreted-text
role="ref"}

Sets the offset of the stacked shadow identified by the given `index` to
`offset`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_method_set_stacked_shadow_outline_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stacked_shadow_outline_size**(index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_LabelSettings_method_set_stacked_shadow_outline_size>`{.interpreted-text
role="ref"}

Sets the outline size of the stacked shadow identified by the given
`index` to `size`.
