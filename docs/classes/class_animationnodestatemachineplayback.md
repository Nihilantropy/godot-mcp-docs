github_url
:   hide

# AnimationNodeStateMachinePlayback {#class_AnimationNodeStateMachinePlayback}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides playback control for an
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Allows control of `AnimationTree<class_AnimationTree>`{.interpreted-text
role="ref"} state machines created with
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"}. Retrieve with `$AnimationTree.get("parameters/playback")`.

::::: tabs
::: code-tab
gdscript

var state_machine = \$AnimationTree.get(\"parameters/playback\")
state_machine.travel(\"some_state\")
:::

::: code-tab
csharp

var stateMachine =
GetNode\<AnimationTree\>(\"AnimationTree\").Get(\"parameters/playback\").As\<AnimationNodeStateMachinePlayback\>();
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

## Signals

:::: {#class_AnimationNodeStateMachinePlayback_signal_state_finished}
::: rst-class
classref-signal
:::
::::

**state_finished**(state:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeStateMachinePlayback_signal_state_finished>`{.interpreted-text
role="ref"}

Emitted when the `state` finishes playback. If `state` is a state
machine set to grouped mode, its signals are passed through with its
name prefixed.

If there is a crossfade, this will be fired when the influence of the
`get_fading_from_node()<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>`{.interpreted-text
role="ref"} animation is no longer present.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_signal_state_started}
::: rst-class
classref-signal
:::
::::

**state_started**(state:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeStateMachinePlayback_signal_state_started>`{.interpreted-text
role="ref"}

Emitted when the `state` starts playback. If `state` is a state machine
set to grouped mode, its signals are passed through with its name
prefixed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNodeStateMachinePlayback_method_get_current_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_current_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachinePlayback_method_get_current_length>`{.interpreted-text
role="ref"}

Returns the current state length.

\*\*Note:\*\* It is possible that any
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} can be nodes as well as animations. This means that there
can be multiple animations within a single state. Which animation length
has priority depends on the nodes connected inside it. Also, if a
transition does not reset, the remaining length at that point will be
returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_get_current_node}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_current_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachinePlayback_method_get_current_node>`{.interpreted-text
role="ref"}

Returns the currently playing animation state.

\*\*Note:\*\* When using a cross-fade, the current state changes to the
next state immediately after the cross-fade begins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_get_current_play_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_current_play_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachinePlayback_method_get_current_play_position>`{.interpreted-text
role="ref"}

Returns the playback position within the current animation state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_get_fading_from_node}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_fading_from_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>`{.interpreted-text
role="ref"}

Returns the starting state of currently fading animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_get_travel_path}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_travel_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachinePlayback_method_get_travel_path>`{.interpreted-text
role="ref"}

Returns the current travel path as computed internally by the A\*
algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeStateMachinePlayback_method_is_playing>`{.interpreted-text
role="ref"}

Returns `true` if an animation is playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_next}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **next**()
`🔗<class_AnimationNodeStateMachinePlayback_method_next>`{.interpreted-text
role="ref"}

If there is a next path by travel or auto advance, immediately
transitions from the current state to the next state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_start}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **start**(node:
`StringName<class_StringName>`{.interpreted-text role="ref"}, reset:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_AnimationNodeStateMachinePlayback_method_start>`{.interpreted-text
role="ref"}

Starts playing the given animation.

If `reset` is `true`, the animation is played from the beginning.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_AnimationNodeStateMachinePlayback_method_stop>`{.interpreted-text
role="ref"}

Stops the currently playing animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachinePlayback_method_travel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**travel**(to_node: `StringName<class_StringName>`{.interpreted-text
role="ref"}, reset_on_teleport: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"}

Transitions from the current state to another one, following the
shortest path.

If the path does not connect from the current state, the animation will
play after the state teleports.

If `reset_on_teleport` is `true`, the animation is played from the
beginning when the travel cause a teleportation.
