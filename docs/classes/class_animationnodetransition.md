github_url
:   hide

# AnimationNodeTransition {#class_AnimationNodeTransition}

**Inherits:**
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A transition within an
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}
connecting two `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

Simple state machine for cases which don\'t require a more advanced
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"}. Animations can be connected to the inputs and transition
times can be specified.

After setting the request and changing the animation playback, the
transition node automatically clears the request on the next process
frame by setting its `transition_request` value to empty.

\*\*Note:\*\* When using a cross-fade, `current_state` and
`current_index` change to the next state immediately after the
cross-fade begins.

::::: tabs
::: code-tab
gdscript

\# Play child animation connected to \"state_2\" port.
animation_tree.set(\"parameters/Transition/transition_request\",
\"state_2\") \# Alternative syntax (same result as above).
animation_tree\[\"parameters/Transition/transition_request\"\] =
\"state_2\"

\# Get current state name (read-only).
animation_tree.get(\"parameters/Transition/current_state\") \#
Alternative syntax (same result as above).
animation_tree\[\"parameters/Transition/current_state\"\]

\# Get current state index (read-only).
animation_tree.get(\"parameters/Transition/current_index\") \#
Alternative syntax (same result as above).
animation_tree\[\"parameters/Transition/current_index\"\]
:::

::: code-tab
csharp

// Play child animation connected to \"state_2\" port.
animationTree.Set(\"parameters/Transition/transition_request\",
\"state_2\");

// Get current state name (read-only).
animationTree.Get(\"parameters/Transition/current_state\");

// Get current state index (read-only).
animationTree.Get(\"parameters/Transition/current_index\");
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#class_AnimationNodeTransition_property_allow_transition_to_self}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_transition_to_self** = `false`
`🔗<class_AnimationNodeTransition_property_allow_transition_to_self>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_transition_to_self**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_allow_transition_to_self**()

If `true`, allows transition to the self state. When the reset option is
enabled in input, the animation is restarted. If `false`, nothing
happens on the transition to the self state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_property_input_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **input_count** = `0`
`🔗<class_AnimationNodeTransition_property_input_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_input_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_input_count**()

The number of enabled input ports for this animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_property_xfade_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **xfade_curve**
`🔗<class_AnimationNodeTransition_property_xfade_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_xfade_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_xfade_curve**()

Determines how cross-fading between animations is eased. If empty, the
transition will be linear. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_property_xfade_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **xfade_time** =
`0.0`
`🔗<class_AnimationNodeTransition_property_xfade_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_xfade_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_xfade_time**()

Cross-fading time (in seconds) between each animation connected to the
inputs.

\*\*Note:\*\* **AnimationNodeTransition** transitions the current state
immediately after the start of the fading. The precise remaining time
can only be inferred from the main animation. When
`AnimationNodeOutput<class_AnimationNodeOutput>`{.interpreted-text
role="ref"} is considered as the most upstream, so the
`xfade_time<class_AnimationNodeTransition_property_xfade_time>`{.interpreted-text
role="ref"} is not scaled depending on the downstream delta. See also
`AnimationNodeOneShot.fadeout_time<class_AnimationNodeOneShot_property_fadeout_time>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNodeTransition_method_is_input_loop_broken_at_end}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_input_loop_broken_at_end**(input:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeTransition_method_is_input_loop_broken_at_end>`{.interpreted-text
role="ref"}

Returns whether the animation breaks the loop at the end of the loop
cycle for transition.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_method_is_input_reset}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_input_reset**(input: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeTransition_method_is_input_reset>`{.interpreted-text
role="ref"}

Returns whether the animation restarts when the animation transitions
from the other animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_method_is_input_set_as_auto_advance}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_input_set_as_auto_advance**(input:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeTransition_method_is_input_set_as_auto_advance>`{.interpreted-text
role="ref"}

Returns `true` if auto-advance is enabled for the given `input` index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_method_set_input_as_auto_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_as_auto_advance**(input: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeTransition_method_set_input_as_auto_advance>`{.interpreted-text
role="ref"}

Enables or disables auto-advance for the given `input` index. If
enabled, state changes to the next input after playing the animation
once. If enabled for the last input state, it loops to the first.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_method_set_input_break_loop_at_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_break_loop_at_end**(input:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeTransition_method_set_input_break_loop_at_end>`{.interpreted-text
role="ref"}

If `true`, breaks the loop at the end of the loop cycle for transition,
even if the animation is looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeTransition_method_set_input_reset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_reset**(input: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeTransition_method_set_input_reset>`{.interpreted-text
role="ref"}

If `true`, the destination animation is restarted when the animation
transitions.
