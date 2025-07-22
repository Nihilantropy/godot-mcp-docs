github_url
:   hide

# GraphFrame {#class_GraphFrame}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `GraphElement<class_GraphElement>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

GraphFrame is a special
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"} that
can be used to organize other
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s inside
a `GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

GraphFrame is a special
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"} to
which other `GraphElement<class_GraphElement>`{.interpreted-text
role="ref"}s can be attached. It can be configured to automatically
resize to enclose all attached
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s. If
the frame is moved, all the attached
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s inside
it will be moved as well.

A GraphFrame is always kept behind the connection layer and other
`GraphElement<class_GraphElement>`{.interpreted-text role="ref"}s inside
a `GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

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

## Signals

:::: {#class_GraphFrame_signal_autoshrink_changed}
::: rst-class
classref-signal
:::
::::

**autoshrink_changed**()
`🔗<class_GraphFrame_signal_autoshrink_changed>`{.interpreted-text
role="ref"}

Emitted when
`autoshrink_enabled<class_GraphFrame_property_autoshrink_enabled>`{.interpreted-text
role="ref"} or
`autoshrink_margin<class_GraphFrame_property_autoshrink_margin>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GraphFrame_property_autoshrink_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autoshrink_enabled**
= `true`
`🔗<class_GraphFrame_property_autoshrink_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoshrink_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_autoshrink_enabled**()

If `true`, the frame\'s rect will be adjusted automatically to enclose
all attached `GraphElement<class_GraphElement>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_property_autoshrink_margin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **autoshrink_margin** =
`40` `🔗<class_GraphFrame_property_autoshrink_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoshrink_margin**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_autoshrink_margin**()

The margin around the attached nodes that is used to calculate the size
of the frame when
`autoshrink_enabled<class_GraphFrame_property_autoshrink_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_property_drag_margin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **drag_margin** = `16`
`🔗<class_GraphFrame_property_drag_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_margin**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_drag_margin**()

The margin inside the frame that can be used to drag the frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_property_tint_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **tint_color** =
`Color(0.3, 0.3, 0.3, 0.75)`
`🔗<class_GraphFrame_property_tint_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_tint_color**()

The color of the frame when
`tint_color_enabled<class_GraphFrame_property_tint_color_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_property_tint_color_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tint_color_enabled**
= `false`
`🔗<class_GraphFrame_property_tint_color_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_color_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_tint_color_enabled**()

If `true`, the tint color will be used to tint the frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_property_title}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **title** = `""`
`🔗<class_GraphFrame_property_title>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_title**()

Title of the frame.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GraphFrame_method_get_titlebar_hbox}
::: rst-class
classref-method
:::
::::

`HBoxContainer<class_HBoxContainer>`{.interpreted-text role="ref"}
**get_titlebar_hbox**()
`🔗<class_GraphFrame_method_get_titlebar_hbox>`{.interpreted-text
role="ref"}

Returns the `HBoxContainer<class_HBoxContainer>`{.interpreted-text
role="ref"} used for the title bar, only containing a
`Label<class_Label>`{.interpreted-text role="ref"} for displaying the
title by default.

This can be used to add custom controls to the title bar such as option
or close buttons.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_GraphFrame_theme_color_resizer_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **resizer_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_GraphFrame_theme_color_resizer_color>`{.interpreted-text
role="ref"}

The color modulation applied to the resizer icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_GraphFrame_theme_style_panel>`{.interpreted-text role="ref"}

The default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
used for the background of the **GraphFrame**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_theme_style_panel_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**panel_selected**
`🔗<class_GraphFrame_theme_style_panel_selected>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the background of the **GraphFrame** when it is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_theme_style_titlebar}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **titlebar**
`🔗<class_GraphFrame_theme_style_titlebar>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the title bar of the **GraphFrame**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphFrame_theme_style_titlebar_selected}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**titlebar_selected**
`🔗<class_GraphFrame_theme_style_titlebar_selected>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the title bar of the **GraphFrame** when it is selected.
