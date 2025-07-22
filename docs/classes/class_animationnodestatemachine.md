github_url
:   hide

# AnimationNodeStateMachine {#class_AnimationNodeStateMachine}

**Inherits:**
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A state machine with multiple
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s, used by
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Contains multiple
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s representing animation states, connected in a graph. State
transitions can be configured to happen automatically or via code, using
a shortest-path algorithm. Retrieve the
`AnimationNodeStateMachinePlayback<class_AnimationNodeStateMachinePlayback>`{.interpreted-text
role="ref"} object from the
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"} node
to control it programmatically.

::::: tabs
::: code-tab
gdscript

var state_machine = \$AnimationTree.get(\"parameters/playback\")
state_machine.travel(\"some_state\")
:::

::: code-tab
csharp

var stateMachine =
GetNode\<AnimationTree\>(\"AnimationTree\").Get(\"parameters/playback\")
as AnimationNodeStateMachinePlayback;
stateMachine.Travel(\"some_state\");
:::
:::::

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

## Enumerations

:::: {#enum_AnimationNodeStateMachine_StateMachineType}
::: rst-class
classref-enumeration
:::
::::

enum **StateMachineType**:
`🔗<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
role="ref"}

:::: {#class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_ROOT}
::: rst-class
classref-enumeration-constant
:::
::::

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
role="ref"} **STATE_MACHINE_TYPE_ROOT** = `0`

Seeking to the beginning is treated as playing from the start state.
Transition to the end state is treated as exiting the state machine.

:::: {#class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_NESTED}
::: rst-class
classref-enumeration-constant
:::
::::

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
role="ref"} **STATE_MACHINE_TYPE_NESTED** = `1`

Seeking to the beginning is treated as seeking to the beginning of the
animation in the current state. Transition to the end state, or the
absence of transitions in each state, is treated as exiting the state
machine.

:::: {#class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_GROUPED}
::: rst-class
classref-enumeration-constant
:::
::::

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
role="ref"} **STATE_MACHINE_TYPE_GROUPED** = `2`

This is a grouped state machine that can be controlled from a parent
state machine. It does not work independently. There must be a state
machine with
`state_machine_type<class_AnimationNodeStateMachine_property_state_machine_type>`{.interpreted-text
role="ref"} of
`STATE_MACHINE_TYPE_ROOT<class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_ROOT>`{.interpreted-text
role="ref"} or
`STATE_MACHINE_TYPE_NESTED<class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_NESTED>`{.interpreted-text
role="ref"} in the parent or ancestor.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeStateMachine_property_allow_transition_to_self}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_transition_to_self** = `false`
`🔗<class_AnimationNodeStateMachine_property_allow_transition_to_self>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_transition_to_self**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_allow_transition_to_self**()

If `true`, allows teleport to the self state with
`AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"}. When the reset option is enabled in
`AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"}, the animation is restarted. If `false`, nothing happens on
the teleportation to the self state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_property_reset_ends}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **reset_ends** =
`false`
`🔗<class_AnimationNodeStateMachine_property_reset_ends>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_reset_ends**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **are_ends_reset**()

If `true`, treat the cross-fade to the start and end nodes as a blend
with the RESET animation.

In most cases, when additional cross-fades are performed in the parent
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"} of
the state machine, setting this property to `false` and matching the
cross-fade time of the parent
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"} and
the state machine\'s start node and end node gives good results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_property_state_machine_type}
::: rst-class
classref-property
:::
::::

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
role="ref"} **state_machine_type** = `0`
`🔗<class_AnimationNodeStateMachine_property_state_machine_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_state_machine_type**(value:
  `StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
  role="ref"})
- `StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
  role="ref"} **get_state_machine_type**()

This property can define the process of transitions for different use
cases. See also
`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNodeStateMachine_method_add_node}
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
`🔗<class_AnimationNodeStateMachine_method_add_node>`{.interpreted-text
role="ref"}

Adds a new animation node to the graph. The `position` is used for
display in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_add_transition}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_transition**(from:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to:
`StringName<class_StringName>`{.interpreted-text role="ref"},
transition:
`AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeStateMachine_method_add_transition>`{.interpreted-text
role="ref"}

Adds a transition between the given animation nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_graph_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_graph_offset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_graph_offset>`{.interpreted-text
role="ref"}

Returns the draw offset of the graph. Used for display in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_node}
::: rst-class
classref-method
:::
::::

`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**get_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_node>`{.interpreted-text
role="ref"}

Returns the animation node with the given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_node_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_node_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_node_list>`{.interpreted-text
role="ref"}

Returns a list containing the names of all animation nodes in this state
machine.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_node_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_node_name**(node:
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_node_name>`{.interpreted-text
role="ref"}

Returns the given animation node\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_node_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_node_position**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_node_position>`{.interpreted-text
role="ref"}

Returns the given animation node\'s coordinates. Used for display in the
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_transition}
::: rst-class
classref-method
:::
::::

`AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>`{.interpreted-text
role="ref"} **get_transition**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_transition>`{.interpreted-text
role="ref"}

Returns the given transition.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_transition_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_transition_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_transition_count>`{.interpreted-text
role="ref"}

Returns the number of connections in the graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_transition_from}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_transition_from**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_transition_from>`{.interpreted-text
role="ref"}

Returns the given transition\'s start node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_get_transition_to}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_transition_to**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_get_transition_to>`{.interpreted-text
role="ref"}

Returns the given transition\'s end node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_has_node}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_node**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_has_node>`{.interpreted-text
role="ref"}

Returns `true` if the graph contains the given animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_has_transition}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_transition**(from:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachine_method_has_transition>`{.interpreted-text
role="ref"}

Returns `true` if there is a transition between the given animation
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_remove_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeStateMachine_method_remove_node>`{.interpreted-text
role="ref"}

Deletes the given animation node from the graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_remove_transition}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_transition**(from:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeStateMachine_method_remove_transition>`{.interpreted-text
role="ref"}

Deletes the transition between the two specified animation nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_remove_transition_by_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_transition_by_index**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeStateMachine_method_remove_transition_by_index>`{.interpreted-text
role="ref"}

Deletes the given transition by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_rename_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, new_name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeStateMachine_method_rename_node>`{.interpreted-text
role="ref"}

Renames the given animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_replace_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**replace_node**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, node:
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeStateMachine_method_replace_node>`{.interpreted-text
role="ref"}

Replaces the given animation node with a new animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_set_graph_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_graph_offset**(offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeStateMachine_method_set_graph_offset>`{.interpreted-text
role="ref"}

Sets the draw offset of the graph. Used for display in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachine_method_set_node_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_node_position**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeStateMachine_method_set_node_position>`{.interpreted-text
role="ref"}

Sets the animation node\'s coordinates. Used for display in the editor.
