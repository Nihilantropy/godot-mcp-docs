github_url
:   hide

# AnimationNodeStateMachineTransition {#class_AnimationNodeStateMachineTransition}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A transition within an
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"} connecting two
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

The path generated when using
`AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"} is limited to the nodes connected by
**AnimationNodeStateMachineTransition**.

You can set the timing and conditions of the transition in detail.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_AnimationNodeStateMachineTransition_signal_advance_condition_changed}
::: rst-class
classref-signal
:::
::::

**advance_condition_changed**()
`🔗<class_AnimationNodeStateMachineTransition_signal_advance_condition_changed>`{.interpreted-text
role="ref"}

Emitted when
`advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>`{.interpreted-text
role="ref"} is changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationNodeStateMachineTransition_SwitchMode}
::: rst-class
classref-enumeration
:::
::::

enum **SwitchMode**:
`🔗<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
role="ref"}

:::: {#class_AnimationNodeStateMachineTransition_constant_SWITCH_MODE_IMMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
role="ref"} **SWITCH_MODE_IMMEDIATE** = `0`

Switch to the next state immediately. The current state will end and
blend into the beginning of the new one.

:::: {#class_AnimationNodeStateMachineTransition_constant_SWITCH_MODE_SYNC}
::: rst-class
classref-enumeration-constant
:::
::::

`SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
role="ref"} **SWITCH_MODE_SYNC** = `1`

Switch to the next state immediately, but will seek the new state to the
playback position of the old state.

:::: {#class_AnimationNodeStateMachineTransition_constant_SWITCH_MODE_AT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
role="ref"} **SWITCH_MODE_AT_END** = `2`

Wait for the current state playback to end, then switch to the beginning
of the next state animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AnimationNodeStateMachineTransition_AdvanceMode}
::: rst-class
classref-enumeration
:::
::::

enum **AdvanceMode**:
`🔗<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
role="ref"}

:::: {#class_AnimationNodeStateMachineTransition_constant_ADVANCE_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
role="ref"} **ADVANCE_MODE_DISABLED** = `0`

Don\'t use this transition.

:::: {#class_AnimationNodeStateMachineTransition_constant_ADVANCE_MODE_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
role="ref"} **ADVANCE_MODE_ENABLED** = `1`

Only use this transition during
`AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationNodeStateMachineTransition_constant_ADVANCE_MODE_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
role="ref"} **ADVANCE_MODE_AUTO** = `2`

Automatically use this transition if the
`advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>`{.interpreted-text
role="ref"} and
`advance_expression<class_AnimationNodeStateMachineTransition_property_advance_expression>`{.interpreted-text
role="ref"} checks are `true` (if assigned).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeStateMachineTransition_property_advance_condition}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**advance_condition** = `&""`
`🔗<class_AnimationNodeStateMachineTransition_property_advance_condition>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_advance_condition**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_advance_condition**()

Turn on auto advance when this condition is set. The provided name will
become a boolean parameter on the
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"} that
can be controlled from code (see [Using
AnimationTree](../tutorials/animation/animation_tree.html#controlling-from-code)).
For example, if
`AnimationTree.tree_root<class_AnimationTree_property_tree_root>`{.interpreted-text
role="ref"} is an
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"} and
`advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>`{.interpreted-text
role="ref"} is set to `"idle"`:

::::: tabs
::: code-tab
gdscript

\$animation_tree.set(\"parameters/conditions/idle\", is_on_floor and
(linear_velocity.x == 0))
:::

::: code-tab
csharp

GetNode\<AnimationTree\>(\"animation_tree\").Set(\"parameters/conditions/idle\",
IsOnFloor && (LinearVelocity.X == 0));
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_advance_expression}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**advance_expression** = `""`
`🔗<class_AnimationNodeStateMachineTransition_property_advance_expression>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_advance_expression**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_advance_expression**()

Use an expression as a condition for state machine transitions. It is
possible to create complex animation advance conditions for switching
between states and gives much greater flexibility for creating complex
state machines by directly interfacing with the script code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_advance_mode}
::: rst-class
classref-property
:::
::::

`AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
role="ref"} **advance_mode** = `1`
`🔗<class_AnimationNodeStateMachineTransition_property_advance_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_advance_mode**(value:
  `AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
  role="ref"})
- `AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>`{.interpreted-text
  role="ref"} **get_advance_mode**()

Determines whether the transition should be disabled, enabled when using
`AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"}, or traversed automatically if the
`advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>`{.interpreted-text
role="ref"} and
`advance_expression<class_AnimationNodeStateMachineTransition_property_advance_expression>`{.interpreted-text
role="ref"} checks are `true` (if assigned).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_break_loop_at_end}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **break_loop_at_end** =
`false`
`🔗<class_AnimationNodeStateMachineTransition_property_break_loop_at_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_break_loop_at_end**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_loop_broken_at_end**()

If `true`, breaks the loop at the end of the loop cycle for transition,
even if the animation is looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **priority** = `1`
`🔗<class_AnimationNodeStateMachineTransition_property_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_priority**()

Lower priority transitions are preferred when travelling through the
tree via
`AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`{.interpreted-text
role="ref"} or
`advance_mode<class_AnimationNodeStateMachineTransition_property_advance_mode>`{.interpreted-text
role="ref"} is set to
`ADVANCE_MODE_AUTO<class_AnimationNodeStateMachineTransition_constant_ADVANCE_MODE_AUTO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_reset}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **reset** = `true`
`🔗<class_AnimationNodeStateMachineTransition_property_reset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_reset**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_reset**()

If `true`, the destination animation is played back from the beginning
when switched.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_switch_mode}
::: rst-class
classref-property
:::
::::

`SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
role="ref"} **switch_mode** = `0`
`🔗<class_AnimationNodeStateMachineTransition_property_switch_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_switch_mode**(value:
  `SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
  role="ref"})
- `SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`{.interpreted-text
  role="ref"} **get_switch_mode**()

The transition type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_xfade_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **xfade_curve**
`🔗<class_AnimationNodeStateMachineTransition_property_xfade_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_xfade_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_xfade_curve**()

Ease curve for better control over cross-fade between this state and the
next. Should be a unit `Curve<class_Curve>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeStateMachineTransition_property_xfade_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **xfade_time** =
`0.0`
`🔗<class_AnimationNodeStateMachineTransition_property_xfade_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_xfade_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_xfade_time**()

The time to cross-fade between this state and the next.

\*\*Note:\*\*
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"} transitions the current state immediately after the start of
the fading. The precise remaining time can only be inferred from the
main animation. When
`AnimationNodeOutput<class_AnimationNodeOutput>`{.interpreted-text
role="ref"} is considered as the most upstream, so the
`xfade_time<class_AnimationNodeStateMachineTransition_property_xfade_time>`{.interpreted-text
role="ref"} is not scaled depending on the downstream delta. See also
`AnimationNodeOneShot.fadeout_time<class_AnimationNodeOneShot_property_fadeout_time>`{.interpreted-text
role="ref"}.
