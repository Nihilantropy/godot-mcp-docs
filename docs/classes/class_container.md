github_url
:   hide

# Container {#class_Container}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AspectRatioContainer<class_AspectRatioContainer>`{.interpreted-text
role="ref"}, `BoxContainer<class_BoxContainer>`{.interpreted-text
role="ref"}, `CenterContainer<class_CenterContainer>`{.interpreted-text
role="ref"}, `EditorProperty<class_EditorProperty>`{.interpreted-text
role="ref"}, `FlowContainer<class_FlowContainer>`{.interpreted-text
role="ref"},
`FoldableContainer<class_FoldableContainer>`{.interpreted-text
role="ref"}, `GraphElement<class_GraphElement>`{.interpreted-text
role="ref"}, `GridContainer<class_GridContainer>`{.interpreted-text
role="ref"}, `MarginContainer<class_MarginContainer>`{.interpreted-text
role="ref"}, `PanelContainer<class_PanelContainer>`{.interpreted-text
role="ref"}, `ScrollContainer<class_ScrollContainer>`{.interpreted-text
role="ref"}, `SplitContainer<class_SplitContainer>`{.interpreted-text
role="ref"},
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"}, `TabContainer<class_TabContainer>`{.interpreted-text
role="ref"}

Base class for all GUI containers.

::: rst-class
classref-introduction-group
:::

## Description

Base class for all GUI containers. A **Container** automatically
arranges its child controls in a certain way. This class can be
inherited to make custom container types.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_Container_signal_pre_sort_children}
::: rst-class
classref-signal
:::
::::

**pre_sort_children**()
`🔗<class_Container_signal_pre_sort_children>`{.interpreted-text
role="ref"}

Emitted when children are going to be sorted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Container_signal_sort_children}
::: rst-class
classref-signal
:::
::::

**sort_children**()
`🔗<class_Container_signal_sort_children>`{.interpreted-text role="ref"}

Emitted when sorting the children is needed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Container_constant_NOTIFICATION_PRE_SORT_CHILDREN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PRE_SORT_CHILDREN** = `50`
`🔗<class_Container_constant_NOTIFICATION_PRE_SORT_CHILDREN>`{.interpreted-text
role="ref"}

Notification just before children are going to be sorted, in case
there\'s something to process beforehand.

:::: {#class_Container_constant_NOTIFICATION_SORT_CHILDREN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_SORT_CHILDREN** = `51`
`🔗<class_Container_constant_NOTIFICATION_SORT_CHILDREN>`{.interpreted-text
role="ref"}

Notification for when sorting the children, it must be obeyed
immediately.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Container_private_method__get_allowed_size_flags_horizontal}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_get_allowed_size_flags_horizontal**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Container_private_method__get_allowed_size_flags_horizontal>`{.interpreted-text
role="ref"}

Implement to return a list of allowed horizontal
`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"} for
child nodes. This doesn\'t technically prevent the usages of any other
size flags, if your implementation requires that. This only limits the
options available to the user in the Inspector dock.

\*\*Note:\*\* Having no size flags is equal to having
`Control.SIZE_SHRINK_BEGIN<class_Control_constant_SIZE_SHRINK_BEGIN>`{.interpreted-text
role="ref"}. As such, this value is always implicitly allowed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Container_private_method__get_allowed_size_flags_vertical}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_get_allowed_size_flags_vertical**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Container_private_method__get_allowed_size_flags_vertical>`{.interpreted-text
role="ref"}

Implement to return a list of allowed vertical
`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"} for
child nodes. This doesn\'t technically prevent the usages of any other
size flags, if your implementation requires that. This only limits the
options available to the user in the Inspector dock.

\*\*Note:\*\* Having no size flags is equal to having
`Control.SIZE_SHRINK_BEGIN<class_Control_constant_SIZE_SHRINK_BEGIN>`{.interpreted-text
role="ref"}. As such, this value is always implicitly allowed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Container_method_fit_child_in_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fit_child_in_rect**(child: `Control<class_Control>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_Container_method_fit_child_in_rect>`{.interpreted-text
role="ref"}

Fit a child control in a given rect. This is mainly a helper for
creating custom container classes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Container_method_queue_sort}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_sort**()
`🔗<class_Container_method_queue_sort>`{.interpreted-text role="ref"}

Queue resort of the contained children. This is called automatically
anyway, but can be called upon request.
