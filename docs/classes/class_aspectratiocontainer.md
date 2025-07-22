github_url
:   hide

# AspectRatioContainer {#class_AspectRatioContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A container that preserves the proportions of its child controls.

::: rst-class
classref-introduction-group
:::

## Description

A container type that arranges its child controls in a way that
preserves their proportions automatically when the container is resized.
Useful when a container has a dynamic size and the child nodes must
adjust their sizes accordingly without losing their aspect ratios.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AspectRatioContainer_StretchMode}
::: rst-class
classref-enumeration
:::
::::

enum **StretchMode**:
`🔗<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
role="ref"}

:::: {#class_AspectRatioContainer_constant_STRETCH_WIDTH_CONTROLS_HEIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_WIDTH_CONTROLS_HEIGHT** = `0`

The height of child controls is automatically adjusted based on the
width of the container.

:::: {#class_AspectRatioContainer_constant_STRETCH_HEIGHT_CONTROLS_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_HEIGHT_CONTROLS_WIDTH** = `1`

The width of child controls is automatically adjusted based on the
height of the container.

:::: {#class_AspectRatioContainer_constant_STRETCH_FIT}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_FIT** = `2`

The bounding rectangle of child controls is automatically adjusted to
fit inside the container while keeping the aspect ratio.

:::: {#class_AspectRatioContainer_constant_STRETCH_COVER}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_COVER** = `3`

The width and height of child controls is automatically adjusted to make
their bounding rectangle cover the entire area of the container while
keeping the aspect ratio.

When the bounding rectangle of child controls exceed the container\'s
size and
`Control.clip_contents<class_Control_property_clip_contents>`{.interpreted-text
role="ref"} is enabled, this allows to show only the container\'s area
restricted by its own bounding rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AspectRatioContainer_AlignmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlignmentMode**:
`🔗<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
role="ref"}

:::: {#class_AspectRatioContainer_constant_ALIGNMENT_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_BEGIN** = `0`

Aligns child controls with the beginning (left or top) of the container.

:::: {#class_AspectRatioContainer_constant_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_CENTER** = `1`

Aligns child controls with the center of the container.

:::: {#class_AspectRatioContainer_constant_ALIGNMENT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
role="ref"} **ALIGNMENT_END** = `2`

Aligns child controls with the end (right or bottom) of the container.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AspectRatioContainer_property_alignment_horizontal}
::: rst-class
classref-property
:::
::::

`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
role="ref"} **alignment_horizontal** = `1`
`🔗<class_AspectRatioContainer_property_alignment_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alignment_horizontal**(value:
  `AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
  role="ref"})
- `AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
  role="ref"} **get_alignment_horizontal**()

Specifies the horizontal relative position of child controls.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AspectRatioContainer_property_alignment_vertical}
::: rst-class
classref-property
:::
::::

`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
role="ref"} **alignment_vertical** = `1`
`🔗<class_AspectRatioContainer_property_alignment_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alignment_vertical**(value:
  `AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
  role="ref"})
- `AlignmentMode<enum_AspectRatioContainer_AlignmentMode>`{.interpreted-text
  role="ref"} **get_alignment_vertical**()

Specifies the vertical relative position of child controls.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AspectRatioContainer_property_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ratio** = `1.0`
`🔗<class_AspectRatioContainer_property_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_ratio**()

The aspect ratio to enforce on child controls. This is the width divided
by the height. The ratio depends on the
`stretch_mode<class_AspectRatioContainer_property_stretch_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AspectRatioContainer_property_stretch_mode}
::: rst-class
classref-property
:::
::::

`StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
role="ref"} **stretch_mode** = `2`
`🔗<class_AspectRatioContainer_property_stretch_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_mode**(value:
  `StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
  role="ref"})
- `StretchMode<enum_AspectRatioContainer_StretchMode>`{.interpreted-text
  role="ref"} **get_stretch_mode**()

The stretch mode used to align child controls.
