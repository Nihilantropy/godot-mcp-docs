github_url
:   hide

# AnimationNodeBlendTree {#class_AnimationNodeBlendTree}

**Inherits:**
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A sub-tree of many type
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}s used
for complex animations. Used by
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This animation node may contain a sub-tree of any other type animation
nodes, such as
`AnimationNodeTransition<class_AnimationNodeTransition>`{.interpreted-text
role="ref"},
`AnimationNodeBlend2<class_AnimationNodeBlend2>`{.interpreted-text
role="ref"},
`AnimationNodeBlend3<class_AnimationNodeBlend3>`{.interpreted-text
role="ref"},
`AnimationNodeOneShot<class_AnimationNodeOneShot>`{.interpreted-text
role="ref"}, etc. This is one of the most commonly used animation node
roots.

An `AnimationNodeOutput<class_AnimationNodeOutput>`{.interpreted-text
role="ref"} node named `output` is created by default.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
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

:::: {#class_AnimationNodeBlendTree_signal_node_changed}
::: rst-class
classref-signal
:::
::::

**node_changed**(node_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeBlendTree_signal_node_changed>`{.interpreted-text
role="ref"}

Emitted when the input port information is changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_AnimationNodeBlendTree_constant_CONNECTION_OK}
::: rst-class
classref-constant
:::
::::

**CONNECTION_OK** = `0`
`🔗<class_AnimationNodeBlendTree_constant_CONNECTION_OK>`{.interpreted-text
role="ref"}

The connection was successful.

:::: {#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT}
::: rst-class
classref-constant
:::
::::

**CONNECTION_ERROR_NO_INPUT** = `1`
`🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT>`{.interpreted-text
role="ref"}

The input node is `null`.

:::: {#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT_INDEX}
::: rst-class
classref-constant
:::
::::

**CONNECTION_ERROR_NO_INPUT_INDEX** = `2`
`🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT_INDEX>`{.interpreted-text
role="ref"}

The specified input port is out of range.

:::: {#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_OUTPUT}
::: rst-class
classref-constant
:::
::::

**CONNECTION_ERROR_NO_OUTPUT** = `3`
`🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_OUTPUT>`{.interpreted-text
role="ref"}

The output node is `null`.

:::: {#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_SAME_NODE}
::: rst-class
classref-constant
:::
::::

**CONNECTION_ERROR_SAME_NODE** = `4`
`🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_SAME_NODE>`{.interpreted-text
role="ref"}

Input and output nodes are the same.

:::: {#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_CONNECTION_EXISTS}
::: rst-class
classref-constant
:::
::::

**CONNECTION_ERROR_CONNECTION_EXISTS** = `5`
`🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_CONNECTION_EXISTS>`{.interpreted-text
role="ref"}

The specified connection already exists.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeBlendTree_property_graph_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **graph_offset**
= `Vector2(0, 0)`
`🔗<class_AnimationNodeBlendTree_property_graph_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_graph_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_graph_offset**()

The global offset of all sub animation nodes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNodeBlendTree_method_add_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, node:
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"},
position: `Vector2<class_Vector2>`{.interpreted-text role="ref"} =
Vector2(0, 0))
`🔗<class_AnimationNodeBlendTree_method_add_node>`{.interpreted-text
role="ref"}

Adds an `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} at the given `position`. The `name` is used to identify the
created sub animation node later.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_connect_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**connect_node**(input_node:
`StringName<class_StringName>`{.interpreted-text role="ref"},
input_index: `int<class_int>`{.interpreted-text role="ref"},
output_node: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendTree_method_connect_node>`{.interpreted-text
role="ref"}

Connects the output of an
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"} as
input for another `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"}, at the input port specified by `input_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_disconnect_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_node**(input_node:
`StringName<class_StringName>`{.interpreted-text role="ref"},
input_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeBlendTree_method_disconnect_node>`{.interpreted-text
role="ref"}

Disconnects the animation node connected to the specified input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_get_node}
::: rst-class
classref-method
:::
::::

`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**get_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendTree_method_get_node>`{.interpreted-text
role="ref"}

Returns the sub animation node with the specified `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_get_node_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_node_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendTree_method_get_node_list>`{.interpreted-text
role="ref"}

Returns a list containing the names of all sub animation nodes in this
blend tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_get_node_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_node_position**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendTree_method_get_node_position>`{.interpreted-text
role="ref"}

Returns the position of the sub animation node with the specified
`name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_has_node}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_node**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendTree_method_has_node>`{.interpreted-text
role="ref"}

Returns `true` if a sub animation node with specified `name` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_remove_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendTree_method_remove_node>`{.interpreted-text
role="ref"}

Removes a sub animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_rename_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, new_name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendTree_method_rename_node>`{.interpreted-text
role="ref"}

Changes the name of a sub animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendTree_method_set_node_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_node_position**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeBlendTree_method_set_node_position>`{.interpreted-text
role="ref"}

Modifies the position of a sub animation node.
