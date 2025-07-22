github_url
:   hide

# BoxContainer {#class_BoxContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `HBoxContainer<class_HBoxContainer>`{.interpreted-text
role="ref"}, `VBoxContainer<class_VBoxContainer>`{.interpreted-text
role="ref"}

A container that arranges its child controls horizontally or vertically.

::: rst-class
classref-introduction-group
:::

## Description

A container that arranges its child controls horizontally or vertically,
rearranging them automatically when their minimum size changes.

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

:::: {#enum_BoxContainer_AlignmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlignmentMode**:
`🔗<enum_BoxContainer_AlignmentMode>`{.interpreted-text role="ref"}

:::: {#class_BoxContainer_constant_ALIGNMENT_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_BoxContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container,
i.e. top if orientation is vertical, left if orientation is horizontal
(right for RTL layout).

:::: {#class_BoxContainer_constant_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_BoxContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

:::: {#class_BoxContainer_constant_ALIGNMENT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_BoxContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e.
bottom if orientation is vertical, right if orientation is horizontal
(left for RTL layout).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_BoxContainer_property_alignment}
::: rst-class
classref-property
:::
::::

`AlignmentMode<enum_BoxContainer_AlignmentMode>`{.interpreted-text
role="ref"} **alignment** = `0`
`🔗<class_BoxContainer_property_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alignment**(value:
  `AlignmentMode<enum_BoxContainer_AlignmentMode>`{.interpreted-text
  role="ref"})
- `AlignmentMode<enum_BoxContainer_AlignmentMode>`{.interpreted-text
  role="ref"} **get_alignment**()

The alignment of the container\'s children (must be one of
`ALIGNMENT_BEGIN<class_BoxContainer_constant_ALIGNMENT_BEGIN>`{.interpreted-text
role="ref"},
`ALIGNMENT_CENTER<class_BoxContainer_constant_ALIGNMENT_CENTER>`{.interpreted-text
role="ref"}, or
`ALIGNMENT_END<class_BoxContainer_constant_ALIGNMENT_END>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoxContainer_property_vertical}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **vertical** = `false`
`🔗<class_BoxContainer_property_vertical>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_vertical**()

If `true`, the **BoxContainer** will arrange its children vertically,
rather than horizontally.

Can\'t be changed when using
`HBoxContainer<class_HBoxContainer>`{.interpreted-text role="ref"} and
`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_BoxContainer_method_add_spacer}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**add_spacer**(begin: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_BoxContainer_method_add_spacer>`{.interpreted-text role="ref"}

Adds a `Control<class_Control>`{.interpreted-text role="ref"} node to
the box as a spacer. If `begin` is `true`, it will insert the
`Control<class_Control>`{.interpreted-text role="ref"} node in front of
all other children.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_BoxContainer_theme_constant_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **separation** = `4`
`🔗<class_BoxContainer_theme_constant_separation>`{.interpreted-text
role="ref"}

The space between the **BoxContainer**\'s elements, in pixels.
