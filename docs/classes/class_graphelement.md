github_url
:   hide

# GraphElement {#class_GraphElement}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `GraphFrame<class_GraphFrame>`{.interpreted-text
role="ref"}, `GraphNode<class_GraphNode>`{.interpreted-text role="ref"}

A container that represents a basic element that can be placed inside a
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} control.

::: rst-class
classref-introduction-group
:::

## Description

**GraphElement** allows to create custom elements for a
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"} graph. By
default such elements can be selected, resized, and repositioned, but
they cannot be connected. For a graph element that allows for
connections see `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"}.

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

## Signals

:::: {#class_GraphElement_signal_delete_request}
::: rst-class
classref-signal
:::
::::

**delete_request**()
`🔗<class_GraphElement_signal_delete_request>`{.interpreted-text
role="ref"}

Emitted when removing the GraphElement is requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_dragged}
::: rst-class
classref-signal
:::
::::

**dragged**(from: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, to: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_GraphElement_signal_dragged>`{.interpreted-text role="ref"}

Emitted when the GraphElement is dragged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_node_deselected}
::: rst-class
classref-signal
:::
::::

**node_deselected**()
`🔗<class_GraphElement_signal_node_deselected>`{.interpreted-text
role="ref"}

Emitted when the GraphElement is deselected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_node_selected}
::: rst-class
classref-signal
:::
::::

**node_selected**()
`🔗<class_GraphElement_signal_node_selected>`{.interpreted-text
role="ref"}

Emitted when the GraphElement is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_position_offset_changed}
::: rst-class
classref-signal
:::
::::

**position_offset_changed**()
`🔗<class_GraphElement_signal_position_offset_changed>`{.interpreted-text
role="ref"}

Emitted when the GraphElement is moved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_raise_request}
::: rst-class
classref-signal
:::
::::

**raise_request**()
`🔗<class_GraphElement_signal_raise_request>`{.interpreted-text
role="ref"}

Emitted when displaying the GraphElement over other ones is requested.
Happens on focusing (clicking into) the GraphElement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_resize_end}
::: rst-class
classref-signal
:::
::::

**resize_end**(new_size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_GraphElement_signal_resize_end>`{.interpreted-text role="ref"}

Emitted when releasing the mouse button after dragging the resizer
handle (see
`resizable<class_GraphElement_property_resizable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_signal_resize_request}
::: rst-class
classref-signal
:::
::::

**resize_request**(new_size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_GraphElement_signal_resize_request>`{.interpreted-text
role="ref"}

Emitted when resizing the GraphElement is requested. Happens on dragging
the resizer handle (see
`resizable<class_GraphElement_property_resizable>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GraphElement_property_draggable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draggable** = `true`
`🔗<class_GraphElement_property_draggable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draggable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_draggable**()

If `true`, the user can drag the GraphElement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_property_position_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**position_offset** = `Vector2(0, 0)`
`🔗<class_GraphElement_property_position_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position_offset**()

The offset of the GraphElement, relative to the scroll offset of the
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_property_resizable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **resizable** = `false`
`🔗<class_GraphElement_property_resizable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_resizable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_resizable**()

If `true`, the user can resize the GraphElement.

\*\*Note:\*\* Dragging the handle will only emit the
`resize_request<class_GraphElement_signal_resize_request>`{.interpreted-text
role="ref"} and
`resize_end<class_GraphElement_signal_resize_end>`{.interpreted-text
role="ref"} signals, the GraphElement needs to be resized manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_property_selectable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **selectable** = `true`
`🔗<class_GraphElement_property_selectable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_selectable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_selectable**()

If `true`, the user can select the GraphElement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GraphElement_property_selected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **selected** = `false`
`🔗<class_GraphElement_property_selected>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_selected**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_selected**()

If `true`, the GraphElement is selected.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_GraphElement_theme_icon_resizer}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **resizer**
`🔗<class_GraphElement_theme_icon_resizer>`{.interpreted-text
role="ref"}

The icon used for the resizer, visible when
`resizable<class_GraphElement_property_resizable>`{.interpreted-text
role="ref"} is enabled.
