github_url
:   hide

::: {.meta keywords="expandable, collapsible, collapse"}
:::

# FoldableContainer {#class_FoldableContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A container that can be expanded/collapsed.

::: rst-class
classref-introduction-group
:::

## Description

A container that can be expanded/collapsed, with a title that can be
filled with controls, such as buttons.

The title can be positioned at the top or bottom of the container.

The container can be expanded or collapsed by clicking the title or by
pressing `ui_accept` when focused.

Child control nodes are hidden when the container is collapsed. Ignores
non-control children.

Can allow grouping with other FoldableContainers, check
`foldable_group<class_FoldableContainer_property_foldable_group>`{.interpreted-text
role="ref"} and `FoldableGroup<class_FoldableGroup>`{.interpreted-text
role="ref"}.

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

:::: {#class_FoldableContainer_signal_folding_changed}
::: rst-class
classref-signal
:::
::::

**folding_changed**(is_folded: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_FoldableContainer_signal_folding_changed>`{.interpreted-text
role="ref"}

Emitted when the container is folded/expanded.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_FoldableContainer_TitlePosition}
::: rst-class
classref-enumeration
:::
::::

enum **TitlePosition**:
`🔗<enum_FoldableContainer_TitlePosition>`{.interpreted-text role="ref"}

:::: {#class_FoldableContainer_constant_POSITION_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`TitlePosition<enum_FoldableContainer_TitlePosition>`{.interpreted-text
role="ref"} **POSITION_TOP** = `0`

Makes the title appear at the top of the container.

:::: {#class_FoldableContainer_constant_POSITION_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`TitlePosition<enum_FoldableContainer_TitlePosition>`{.interpreted-text
role="ref"} **POSITION_BOTTOM** = `1`

Makes the title appear at the bottom of the container. Also makes all
StyleBoxes flipped vertically.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_FoldableContainer_property_foldable_group}
::: rst-class
classref-property
:::
::::

`FoldableGroup<class_FoldableGroup>`{.interpreted-text role="ref"}
**foldable_group**
`🔗<class_FoldableContainer_property_foldable_group>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_foldable_group**(value:
  `FoldableGroup<class_FoldableGroup>`{.interpreted-text role="ref"})
- `FoldableGroup<class_FoldableGroup>`{.interpreted-text role="ref"}
  **get_foldable_group**()

The `FoldableGroup<class_FoldableGroup>`{.interpreted-text role="ref"}
associated with the container. When multiple **FoldableContainer** nodes
share the same group, only one of them is allowed to be unfolded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_folded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **folded** = `false`
`🔗<class_FoldableContainer_property_folded>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_folded**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_folded**()

If `true`, the container will becomes folded and will hide all its
children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_FoldableContainer_property_language>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_language**()

Language code used for text shaping algorithms. If left empty, current
locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_title}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **title** = `""`
`🔗<class_FoldableContainer_property_title>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_title**()

The container\'s title text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_title_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **title_alignment** = `0`
`🔗<class_FoldableContainer_property_title_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_title_alignment**()

Title\'s horizontal text alignment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_title_position}
::: rst-class
classref-property
:::
::::

`TitlePosition<enum_FoldableContainer_TitlePosition>`{.interpreted-text
role="ref"} **title_position** = `0`
`🔗<class_FoldableContainer_property_title_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title_position**(value:
  `TitlePosition<enum_FoldableContainer_TitlePosition>`{.interpreted-text
  role="ref"})
- `TitlePosition<enum_FoldableContainer_TitlePosition>`{.interpreted-text
  role="ref"} **get_title_position**()

Title\'s position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_title_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **title_text_direction** = `0`
`🔗<class_FoldableContainer_property_title_text_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title_text_direction**(value:
  `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"})
- `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"} **get_title_text_direction**()

Title text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_property_title_text_overrun_behavior}
::: rst-class
classref-property
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **title_text_overrun_behavior** = `0`
`🔗<class_FoldableContainer_property_title_text_overrun_behavior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title_text_overrun_behavior**(value:
  `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"})
- `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"} **get_title_text_overrun_behavior**()

Defines the behavior of the title when the text is longer than the
available space.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FoldableContainer_method_add_title_bar_control}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_title_bar_control**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_FoldableContainer_method_add_title_bar_control>`{.interpreted-text
role="ref"}

Adds a `Control<class_Control>`{.interpreted-text role="ref"} that will
be placed next to the container\'s title, obscuring the clickable area.
Prime usage is adding `Button<class_Button>`{.interpreted-text
role="ref"} nodes, but it can be any
`Control<class_Control>`{.interpreted-text role="ref"}.

The control will be added as a child of this container and removed from
previous parent if necessary. The controls will be placed aligned to the
right, with the first added control being the leftmost one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_method_expand}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **expand**()
`🔗<class_FoldableContainer_method_expand>`{.interpreted-text
role="ref"}

Expands the container and emits
`folding_changed<class_FoldableContainer_signal_folding_changed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_method_fold}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fold**()
`🔗<class_FoldableContainer_method_fold>`{.interpreted-text role="ref"}

Folds the container and emits
`folding_changed<class_FoldableContainer_signal_folding_changed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_method_remove_title_bar_control}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_title_bar_control**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_FoldableContainer_method_remove_title_bar_control>`{.interpreted-text
role="ref"}

Removes a `Control<class_Control>`{.interpreted-text role="ref"} added
with
`add_title_bar_control()<class_FoldableContainer_method_add_title_bar_control>`{.interpreted-text
role="ref"}. The node is not freed automatically, you need to use
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_FoldableContainer_theme_color_collapsed_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**collapsed_font_color** = `Color(1, 1, 1, 1)`
`🔗<class_FoldableContainer_theme_color_collapsed_font_color>`{.interpreted-text
role="ref"}

The title\'s font color when collapsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_FoldableContainer_theme_color_font_color>`{.interpreted-text
role="ref"}

The title\'s font color when expanded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(1, 1, 1, 1)`
`🔗<class_FoldableContainer_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The title\'s font outline color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_color_hover_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **hover_font_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_FoldableContainer_theme_color_hover_font_color>`{.interpreted-text
role="ref"}

The title\'s font hover color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `2`
`🔗<class_FoldableContainer_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal separation between the title\'s icon and text, and
between title bar controls.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_FoldableContainer_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The title\'s font outline size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_FoldableContainer_theme_font_font>`{.interpreted-text
role="ref"}

The title\'s font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_FoldableContainer_theme_font_size_font_size>`{.interpreted-text
role="ref"}

The title\'s font size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_icon_expanded_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**expanded_arrow**
`🔗<class_FoldableContainer_theme_icon_expanded_arrow>`{.interpreted-text
role="ref"}

The title\'s icon used when expanded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_icon_expanded_arrow_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**expanded_arrow_mirrored**
`🔗<class_FoldableContainer_theme_icon_expanded_arrow_mirrored>`{.interpreted-text
role="ref"}

The title\'s icon used when expanded (for bottom title).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_icon_folded_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**folded_arrow**
`🔗<class_FoldableContainer_theme_icon_folded_arrow>`{.interpreted-text
role="ref"}

The title\'s icon used when folded (for left-to-right layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_icon_folded_arrow_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**folded_arrow_mirrored**
`🔗<class_FoldableContainer_theme_icon_folded_arrow_mirrored>`{.interpreted-text
role="ref"}

The title\'s icon used when collapsed (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_FoldableContainer_theme_style_focus>`{.interpreted-text
role="ref"}

Background used when **FoldableContainer** has GUI focus. The
`focus<class_FoldableContainer_theme_style_focus>`{.interpreted-text
role="ref"} `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} is
displayed *over* the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} remains visible. A
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that represents
an outline or an underline works well for this purpose. To disable the
focus visual effect, assign a
`StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text role="ref"}
resource. Note that disabling the focus visual effect will harm
keyboard/controller navigation usability, so this is not recommended for
accessibility reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_FoldableContainer_theme_style_panel>`{.interpreted-text
role="ref"}

Default background for the **FoldableContainer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_style_title_collapsed_hover_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**title_collapsed_hover_panel**
`🔗<class_FoldableContainer_theme_style_title_collapsed_hover_panel>`{.interpreted-text
role="ref"}

Background used when the mouse cursor enters the title\'s area when
collapsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_style_title_collapsed_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**title_collapsed_panel**
`🔗<class_FoldableContainer_theme_style_title_collapsed_panel>`{.interpreted-text
role="ref"}

Default background for the **FoldableContainer**\'s title when
collapsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_style_title_hover_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**title_hover_panel**
`🔗<class_FoldableContainer_theme_style_title_hover_panel>`{.interpreted-text
role="ref"}

Background used when the mouse cursor enters the title\'s area when
expanded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableContainer_theme_style_title_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **title_panel**
`🔗<class_FoldableContainer_theme_style_title_panel>`{.interpreted-text
role="ref"}

Default background for the **FoldableContainer**\'s title when expanded.
