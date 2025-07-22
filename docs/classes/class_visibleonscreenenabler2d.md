github_url
:   hide

# VisibleOnScreenEnabler2D {#class_VisibleOnScreenEnabler2D}

**Inherits:**
`VisibleOnScreenNotifier2D<class_VisibleOnScreenNotifier2D>`{.interpreted-text
role="ref"} **\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A rectangular region of 2D space that, when visible on screen, enables a
target node.

::: rst-class
classref-introduction-group
:::

## Description

**VisibleOnScreenEnabler2D** contains a rectangular region of 2D space
and a target node. The target node will be automatically enabled (via
its
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} property) when any part of this region becomes visible on
the screen, and automatically disabled otherwise. This can for example
be used to activate enemies only when the player approaches them.

See
`VisibleOnScreenNotifier2D<class_VisibleOnScreenNotifier2D>`{.interpreted-text
role="ref"} if you only want to be notified when the region is visible
on screen.

\*\*Note:\*\* **VisibleOnScreenEnabler2D** uses the render culling code
to determine whether it\'s visible on screen, so it won\'t function
unless
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} is set to `true`.

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

:::: {#enum_VisibleOnScreenEnabler2D_EnableMode}
::: rst-class
classref-enumeration
:::
::::

enum **EnableMode**:
`🔗<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
role="ref"}

:::: {#class_VisibleOnScreenEnabler2D_constant_ENABLE_MODE_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`EnableMode<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
role="ref"} **ENABLE_MODE_INHERIT** = `0`

Corresponds to
`Node.PROCESS_MODE_INHERIT<class_Node_constant_PROCESS_MODE_INHERIT>`{.interpreted-text
role="ref"}.

:::: {#class_VisibleOnScreenEnabler2D_constant_ENABLE_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`EnableMode<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
role="ref"} **ENABLE_MODE_ALWAYS** = `1`

Corresponds to
`Node.PROCESS_MODE_ALWAYS<class_Node_constant_PROCESS_MODE_ALWAYS>`{.interpreted-text
role="ref"}.

:::: {#class_VisibleOnScreenEnabler2D_constant_ENABLE_MODE_WHEN_PAUSED}
::: rst-class
classref-enumeration-constant
:::
::::

`EnableMode<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
role="ref"} **ENABLE_MODE_WHEN_PAUSED** = `2`

Corresponds to
`Node.PROCESS_MODE_WHEN_PAUSED<class_Node_constant_PROCESS_MODE_WHEN_PAUSED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisibleOnScreenEnabler2D_property_enable_mode}
::: rst-class
classref-property
:::
::::

`EnableMode<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
role="ref"} **enable_mode** = `0`
`🔗<class_VisibleOnScreenEnabler2D_property_enable_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_mode**(value:
  `EnableMode<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
  role="ref"})
- `EnableMode<enum_VisibleOnScreenEnabler2D_EnableMode>`{.interpreted-text
  role="ref"} **get_enable_mode**()

Determines how the target node is enabled. Corresponds to
`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}. When
the node is disabled, it always uses
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisibleOnScreenEnabler2D_property_enable_node_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**enable_node_path** = `NodePath("..")`
`🔗<class_VisibleOnScreenEnabler2D_property_enable_node_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_node_path**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_enable_node_path**()

The path to the target node, relative to the
**VisibleOnScreenEnabler2D**. The target node is cached; it\'s only
assigned when setting this property (if the **VisibleOnScreenEnabler2D**
is inside the scene tree) and every time the
**VisibleOnScreenEnabler2D** enters the scene tree. If the path is
empty, no node will be affected. If the path is invalid, an error is
also generated.
