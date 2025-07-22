github_url
:   hide

# FlowContainer {#class_FlowContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`HFlowContainer<class_HFlowContainer>`{.interpreted-text role="ref"},
`VFlowContainer<class_VFlowContainer>`{.interpreted-text role="ref"}

A container that arranges its child controls horizontally or vertically
and wraps them around at the borders.

::: rst-class
classref-introduction-group
:::

## Description

A container that arranges its child controls horizontally or vertically
and wraps them around at the borders. This is similar to how text in a
book wraps around when no more words can fit on a line.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_FlowContainer_AlignmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlignmentMode**:
`🔗<enum_FlowContainer_AlignmentMode>`{.interpreted-text role="ref"}

:::: {#class_FlowContainer_constant_ALIGNMENT_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_FlowContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container,
i.e. top if orientation is vertical, left if orientation is horizontal
(right for RTL layout).

:::: {#class_FlowContainer_constant_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_FlowContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

:::: {#class_FlowContainer_constant_ALIGNMENT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_FlowContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e.
bottom if orientation is vertical, right if orientation is horizontal
(left for RTL layout).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FlowContainer_LastWrapAlignmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **LastWrapAlignmentMode**:
`🔗<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
role="ref"}

:::: {#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
role="ref"} **LAST_WRAP_ALIGNMENT_INHERIT** = `0`

The last partially filled row or column will wrap aligned to the
previous row or column in accordance with
`alignment<class_FlowContainer_property_alignment>`{.interpreted-text
role="ref"}.

:::: {#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
role="ref"} **LAST_WRAP_ALIGNMENT_BEGIN** = `1`

The last partially filled row or column will wrap aligned to the
beginning of the previous row or column.

:::: {#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
role="ref"} **LAST_WRAP_ALIGNMENT_CENTER** = `2`

The last partially filled row or column will wrap aligned to the center
of the previous row or column.

:::: {#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
role="ref"} **LAST_WRAP_ALIGNMENT_END** = `3`

The last partially filled row or column will wrap aligned to the end of
the previous row or column.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_FlowContainer_property_alignment}
::: rst-class
classref-property
:::
::::

`AlignmentMode<enum_FlowContainer_AlignmentMode>`{.interpreted-text
role="ref"} **alignment** = `0`
`🔗<class_FlowContainer_property_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alignment**(value:
  `AlignmentMode<enum_FlowContainer_AlignmentMode>`{.interpreted-text
  role="ref"})
- `AlignmentMode<enum_FlowContainer_AlignmentMode>`{.interpreted-text
  role="ref"} **get_alignment**()

The alignment of the container\'s children (must be one of
`ALIGNMENT_BEGIN<class_FlowContainer_constant_ALIGNMENT_BEGIN>`{.interpreted-text
role="ref"},
`ALIGNMENT_CENTER<class_FlowContainer_constant_ALIGNMENT_CENTER>`{.interpreted-text
role="ref"}, or
`ALIGNMENT_END<class_FlowContainer_constant_ALIGNMENT_END>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FlowContainer_property_last_wrap_alignment}
::: rst-class
classref-property
:::
::::

`LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
role="ref"} **last_wrap_alignment** = `0`
`🔗<class_FlowContainer_property_last_wrap_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_last_wrap_alignment**(value:
  `LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
  role="ref"})
- `LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>`{.interpreted-text
  role="ref"} **get_last_wrap_alignment**()

The wrap behavior of the last, partially filled row or column (must be
one of
`LAST_WRAP_ALIGNMENT_INHERIT<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_INHERIT>`{.interpreted-text
role="ref"},
`LAST_WRAP_ALIGNMENT_BEGIN<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_BEGIN>`{.interpreted-text
role="ref"},
`LAST_WRAP_ALIGNMENT_CENTER<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_CENTER>`{.interpreted-text
role="ref"}, or
`LAST_WRAP_ALIGNMENT_END<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_END>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FlowContainer_property_reverse_fill}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **reverse_fill** =
`false`
`🔗<class_FlowContainer_property_reverse_fill>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_reverse_fill**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_reverse_fill**()

If `true`, reverses fill direction. Horizontal **FlowContainer**s will
fill rows bottom to top, vertical **FlowContainer**s will fill columns
right to left.

When using a vertical **FlowContainer** with a right to left
`Control.layout_direction<class_Control_property_layout_direction>`{.interpreted-text
role="ref"}, columns will fill left to right instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FlowContainer_property_vertical}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **vertical** = `false`
`🔗<class_FlowContainer_property_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_vertical**()

If `true`, the **FlowContainer** will arrange its children vertically,
rather than horizontally.

Can\'t be changed when using
`HFlowContainer<class_HFlowContainer>`{.interpreted-text role="ref"} and
`VFlowContainer<class_VFlowContainer>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FlowContainer_method_get_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FlowContainer_method_get_line_count>`{.interpreted-text
role="ref"}

Returns the current line count.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_FlowContainer_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_FlowContainer_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal separation of child nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FlowContainer_theme_constant_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **v_separation** = `4`
`🔗<class_FlowContainer_theme_constant_v_separation>`{.interpreted-text
role="ref"}

The vertical separation of child nodes.
