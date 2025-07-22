github_url
:   hide

# BackBufferCopy {#class_BackBufferCopy}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that copies a region of the screen to a buffer for access in
shader code.

::: rst-class
classref-introduction-group
:::

## Description

Node for back-buffering the currently-displayed screen. The region
defined in the **BackBufferCopy** node is buffered with the content of
the screen it covers, or the entire screen according to the
`copy_mode<class_BackBufferCopy_property_copy_mode>`{.interpreted-text
role="ref"}. It can be accessed in shader scripts using the screen
texture (i.e. a uniform sampler with `hint_screen_texture`).

\*\*Note:\*\* Since this node inherits from
`Node2D<class_Node2D>`{.interpreted-text role="ref"} (and not
`Control<class_Control>`{.interpreted-text role="ref"}), anchors and
margins won\'t apply to child `Control<class_Control>`{.interpreted-text
role="ref"}-derived nodes. This can be problematic when resizing the
window. To avoid this, add `Control<class_Control>`{.interpreted-text
role="ref"}-derived nodes as *siblings* to the **BackBufferCopy** node
instead of adding them as children.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Screen-reading shaders <../tutorials/shaders/screen-reading_shaders>`{.interpreted-text
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

:::: {#enum_BackBufferCopy_CopyMode}
::: rst-class
classref-enumeration
:::
::::

enum **CopyMode**: `🔗<enum_BackBufferCopy_CopyMode>`{.interpreted-text
role="ref"}

:::: {#class_BackBufferCopy_constant_COPY_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CopyMode<enum_BackBufferCopy_CopyMode>`{.interpreted-text role="ref"}
**COPY_MODE_DISABLED** = `0`

Disables the buffering mode. This means the **BackBufferCopy** node will
directly use the portion of screen it covers.

:::: {#class_BackBufferCopy_constant_COPY_MODE_RECT}
::: rst-class
classref-enumeration-constant
:::
::::

`CopyMode<enum_BackBufferCopy_CopyMode>`{.interpreted-text role="ref"}
**COPY_MODE_RECT** = `1`

**BackBufferCopy** buffers a rectangular region.

:::: {#class_BackBufferCopy_constant_COPY_MODE_VIEWPORT}
::: rst-class
classref-enumeration-constant
:::
::::

`CopyMode<enum_BackBufferCopy_CopyMode>`{.interpreted-text role="ref"}
**COPY_MODE_VIEWPORT** = `2`

**BackBufferCopy** buffers the entire screen.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_BackBufferCopy_property_copy_mode}
::: rst-class
classref-property
:::
::::

`CopyMode<enum_BackBufferCopy_CopyMode>`{.interpreted-text role="ref"}
**copy_mode** = `1`
`🔗<class_BackBufferCopy_property_copy_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_copy_mode**(value:
  `CopyMode<enum_BackBufferCopy_CopyMode>`{.interpreted-text
  role="ref"})
- `CopyMode<enum_BackBufferCopy_CopyMode>`{.interpreted-text role="ref"}
  **get_copy_mode**()

Buffer mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BackBufferCopy_property_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **rect** =
`Rect2(-100, -100, 200, 200)`
`🔗<class_BackBufferCopy_property_rect>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_rect**()

The area covered by the **BackBufferCopy**. Only used if
`copy_mode<class_BackBufferCopy_property_copy_mode>`{.interpreted-text
role="ref"} is
`COPY_MODE_RECT<class_BackBufferCopy_constant_COPY_MODE_RECT>`{.interpreted-text
role="ref"}.
