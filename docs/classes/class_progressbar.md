github_url
:   hide

# ProgressBar {#class_ProgressBar}

**Inherits:** `Range<class_Range>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control used for visual representation of a percentage.

::: rst-class
classref-introduction-group
:::

## Description

A control used for visual representation of a percentage. Shows the fill
percentage in the center. Can also be used to show indeterminate
progress. For more fill modes, use
`TextureProgressBar<class_TextureProgressBar>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ProgressBar_FillMode}
::: rst-class
classref-enumeration
:::
::::

enum **FillMode**: `🔗<enum_ProgressBar_FillMode>`{.interpreted-text
role="ref"}

:::: {#class_ProgressBar_constant_FILL_BEGIN_TO_END}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_ProgressBar_FillMode>`{.interpreted-text role="ref"}
**FILL_BEGIN_TO_END** = `0`

The progress bar fills from begin to end horizontally, according to the
language direction. If
`Control.is_layout_rtl()<class_Control_method_is_layout_rtl>`{.interpreted-text
role="ref"} returns `false`, it fills from left to right, and if it
returns `true`, it fills from right to left.

:::: {#class_ProgressBar_constant_FILL_END_TO_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_ProgressBar_FillMode>`{.interpreted-text role="ref"}
**FILL_END_TO_BEGIN** = `1`

The progress bar fills from end to begin horizontally, according to the
language direction. If
`Control.is_layout_rtl()<class_Control_method_is_layout_rtl>`{.interpreted-text
role="ref"} returns `false`, it fills from right to left, and if it
returns `true`, it fills from left to right.

:::: {#class_ProgressBar_constant_FILL_TOP_TO_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_ProgressBar_FillMode>`{.interpreted-text role="ref"}
**FILL_TOP_TO_BOTTOM** = `2`

The progress fills from top to bottom.

:::: {#class_ProgressBar_constant_FILL_BOTTOM_TO_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`FillMode<enum_ProgressBar_FillMode>`{.interpreted-text role="ref"}
**FILL_BOTTOM_TO_TOP** = `3`

The progress fills from bottom to top.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ProgressBar_property_editor_preview_indeterminate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor_preview_indeterminate**
`🔗<class_ProgressBar_property_editor_preview_indeterminate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editor_preview_indeterminate**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editor_preview_indeterminate_enabled**()

If `false`, the
`indeterminate<class_ProgressBar_property_indeterminate>`{.interpreted-text
role="ref"} animation will be paused in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_property_fill_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fill_mode** = `0`
`🔗<class_ProgressBar_property_fill_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fill_mode**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_fill_mode**()

The fill direction. See
`FillMode<enum_ProgressBar_FillMode>`{.interpreted-text role="ref"} for
possible values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_property_indeterminate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **indeterminate** =
`false` `🔗<class_ProgressBar_property_indeterminate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_indeterminate**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_indeterminate**()

When set to `true`, the progress bar indicates that something is
happening with an animation, but does not show the fill percentage or
value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_property_show_percentage}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_percentage** =
`true`
`🔗<class_ProgressBar_property_show_percentage>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_percentage**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_percentage_shown**()

If `true`, the fill percentage is displayed on the bar.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_ProgressBar_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.95, 0.95, 0.95, 1)`
`🔗<class_ProgressBar_theme_color_font_color>`{.interpreted-text
role="ref"}

The color of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_ProgressBar_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the **ProgressBar**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_ProgressBar_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_ProgressBar_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_ProgressBar_theme_font_font>`{.interpreted-text role="ref"}

Font used to draw the fill percentage if
`show_percentage<class_ProgressBar_property_show_percentage>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_ProgressBar_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size used to draw the fill percentage if
`show_percentage<class_ProgressBar_property_show_percentage>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_theme_style_background}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **background**
`🔗<class_ProgressBar_theme_style_background>`{.interpreted-text
role="ref"}

The style of the background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProgressBar_theme_style_fill}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **fill**
`🔗<class_ProgressBar_theme_style_fill>`{.interpreted-text role="ref"}

The style of the progress (i.e. the part that fills the bar).
