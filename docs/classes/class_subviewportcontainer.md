github_url
:   hide

# SubViewportContainer {#class_SubViewportContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A container used for displaying the contents of a
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A container that displays the contents of underlying
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"} child
nodes. It uses the combined size of the
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}s as
minimum size, unless
`stretch<class_SubViewportContainer_property_stretch>`{.interpreted-text
role="ref"} is enabled.

\*\*Note:\*\* Changing a **SubViewportContainer**\'s
`Control.scale<class_Control_property_scale>`{.interpreted-text
role="ref"} will cause its contents to appear distorted. To change its
visual size without causing distortion, adjust the node\'s margins
instead (if it\'s not already in a container).

\*\*Note:\*\* The **SubViewportContainer** forwards mouse-enter and
mouse-exit notifications to its sub-viewports.

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

:::: {#class_SubViewportContainer_property_mouse_target}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **mouse_target** =
`false`
`🔗<class_SubViewportContainer_property_mouse_target>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mouse_target**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_mouse_target_enabled**()

Configure, if either the **SubViewportContainer** or alternatively the
`Control<class_Control>`{.interpreted-text role="ref"} nodes of its
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"} children
should be available as targets of mouse-related functionalities, like
identifying the drop target in drag-and-drop operations or cursor shape
of hovered `Control<class_Control>`{.interpreted-text role="ref"} node.

If `false`, the `Control<class_Control>`{.interpreted-text role="ref"}
nodes inside its `SubViewport<class_SubViewport>`{.interpreted-text
role="ref"} children are considered as targets.

If `true`, the **SubViewportContainer** itself will be considered as a
target.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SubViewportContainer_property_stretch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **stretch** = `false`
`🔗<class_SubViewportContainer_property_stretch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_stretch_enabled**()

If `true`, the sub-viewport will be automatically resized to the
control\'s size.

\*\*Note:\*\* If `true`, this will prohibit changing
`SubViewport.size<class_SubViewport_property_size>`{.interpreted-text
role="ref"} of its children manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SubViewportContainer_property_stretch_shrink}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stretch_shrink** = `1`
`🔗<class_SubViewportContainer_property_stretch_shrink>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_shrink**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_stretch_shrink**()

Divides the sub-viewport\'s effective resolution by this value while
preserving its scale. This can be used to speed up rendering.

For example, a 1280×720 sub-viewport with
`stretch_shrink<class_SubViewportContainer_property_stretch_shrink>`{.interpreted-text
role="ref"} set to `2` will be rendered at 640×360 while occupying the
same size in the container.

\*\*Note:\*\*
`stretch<class_SubViewportContainer_property_stretch>`{.interpreted-text
role="ref"} must be `true` for this property to work.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SubViewportContainer_private_method__propagate_input_event}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_propagate_input_event**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SubViewportContainer_private_method__propagate_input_event>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Virtual method to be implemented by the user. If it returns `true`, the
`event` is propagated to
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"} children.
Propagation doesn\'t happen if it returns `false`. If the function is
not implemented, all events are propagated to SubViewports.
