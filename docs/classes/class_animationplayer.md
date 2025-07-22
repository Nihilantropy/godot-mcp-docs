github_url
:   hide

# AnimationPlayer {#class_AnimationPlayer}

**Inherits:** `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A node used for animation playback.

::: rst-class
classref-introduction-group
:::

## Description

An animation player is used for general-purpose playback of animations.
It contains a dictionary of
`AnimationLibrary<class_AnimationLibrary>`{.interpreted-text role="ref"}
resources and custom blend times between animation transitions.

Some methods and properties use a single key to reference an animation
directly. These keys are formatted as the key for the library, followed
by a forward slash, then the key for the animation within the library,
for example `"movement/run"`. If the library\'s key is an empty string
(known as the default library), the forward slash is omitted, being the
same key used by the library.

\*\*AnimationPlayer\*\* is better-suited than
`Tween<class_Tween>`{.interpreted-text role="ref"} for more complex
animations, for example ones with non-trivial timings. It can also be
used over `Tween<class_Tween>`{.interpreted-text role="ref"} if the
animation track editor is more convenient than doing it in code.

Updating the target properties of animations occurs at the process
frame.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D Sprite animation <../tutorials/2d/2d_sprite_animation>`{.interpreted-text
  role="doc"}
- `Animation documentation index <../tutorials/animation/index>`{.interpreted-text
  role="doc"}
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

## Signals

:::: {#class_AnimationPlayer_signal_animation_changed}
::: rst-class
classref-signal
:::
::::

**animation_changed**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, new_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationPlayer_signal_animation_changed>`{.interpreted-text
role="ref"}

Emitted when a queued animation plays after the previous animation
finished. See also
`queue()<class_AnimationPlayer_method_queue>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The signal is not emitted when the animation is changed
via `play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"} or by an
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_signal_current_animation_changed}
::: rst-class
classref-signal
:::
::::

**current_animation_changed**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_AnimationPlayer_signal_current_animation_changed>`{.interpreted-text
role="ref"}

Emitted when
`current_animation<class_AnimationPlayer_property_current_animation>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationPlayer_AnimationProcessCallback}
::: rst-class
classref-enumeration
:::
::::

enum **AnimationProcessCallback**:
`🔗<enum_AnimationPlayer_AnimationProcessCallback>`{.interpreted-text
role="ref"}

:::: {#class_AnimationPlayer_constant_ANIMATION_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationProcessCallback<enum_AnimationPlayer_AnimationProcessCallback>`{.interpreted-text
role="ref"} **ANIMATION_PROCESS_PHYSICS** = `0`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationPlayer_constant_ANIMATION_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationProcessCallback<enum_AnimationPlayer_AnimationProcessCallback>`{.interpreted-text
role="ref"} **ANIMATION_PROCESS_IDLE** = `1`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_IDLE>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationPlayer_constant_ANIMATION_PROCESS_MANUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationProcessCallback<enum_AnimationPlayer_AnimationProcessCallback>`{.interpreted-text
role="ref"} **ANIMATION_PROCESS_MANUAL** = `2`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_MANUAL>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AnimationPlayer_AnimationMethodCallMode}
::: rst-class
classref-enumeration
:::
::::

enum **AnimationMethodCallMode**:
`🔗<enum_AnimationPlayer_AnimationMethodCallMode>`{.interpreted-text
role="ref"}

:::: {#class_AnimationPlayer_constant_ANIMATION_METHOD_CALL_DEFERRED}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationMethodCallMode<enum_AnimationPlayer_AnimationMethodCallMode>`{.interpreted-text
role="ref"} **ANIMATION_METHOD_CALL_DEFERRED** = `0`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_METHOD_DEFERRED<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_METHOD_DEFERRED>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationPlayer_constant_ANIMATION_METHOD_CALL_IMMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationMethodCallMode<enum_AnimationPlayer_AnimationMethodCallMode>`{.interpreted-text
role="ref"} **ANIMATION_METHOD_CALL_IMMEDIATE** = `1`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationPlayer_property_assigned_animation}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**assigned_animation**
`🔗<class_AnimationPlayer_property_assigned_animation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_assigned_animation**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_assigned_animation**()

If playing, the current animation\'s key, otherwise, the animation last
played. When set, this changes the animation, but will not play it
unless already playing. See also
`current_animation<class_AnimationPlayer_property_current_animation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_autoplay}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **autoplay** = `""`
`🔗<class_AnimationPlayer_property_autoplay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoplay**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_autoplay**()

The key of the animation to play when the scene loads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_current_animation}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**current_animation** = `""`
`🔗<class_AnimationPlayer_property_current_animation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_animation**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_animation**()

The key of the currently playing animation. If no animation is playing,
the property\'s value is an empty string. Changing this value does not
restart the animation. See
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"} for more information on playing animations.

\*\*Note:\*\* While this property appears in the Inspector, it\'s not
meant to be edited, and it\'s not saved in the scene. This property is
mainly used to get the currently playing animation, and internally for
animation playback tracks. For more information, see
`Animation<class_Animation>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_current_animation_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**current_animation_length**
`🔗<class_AnimationPlayer_property_current_animation_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_current_animation_length**()

The length (in seconds) of the currently playing animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_current_animation_position}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**current_animation_position**
`🔗<class_AnimationPlayer_property_current_animation_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_current_animation_position**()

The position (in seconds) of the currently playing animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_movie_quit_on_finish}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**movie_quit_on_finish** = `false`
`🔗<class_AnimationPlayer_property_movie_quit_on_finish>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_movie_quit_on_finish_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_movie_quit_on_finish_enabled**()

If `true` and the engine is running in Movie Maker mode (see
`MovieWriter<class_MovieWriter>`{.interpreted-text role="ref"}), exits
the engine with
`SceneTree.quit()<class_SceneTree_method_quit>`{.interpreted-text
role="ref"} as soon as an animation is done playing in this
**AnimationPlayer**. A message is printed when the engine quits for this
reason.

\*\*Note:\*\* This obeys the same logic as the
`AnimationMixer.animation_finished<class_AnimationMixer_signal_animation_finished>`{.interpreted-text
role="ref"} signal, so it will not quit the engine if the animation is
set to be looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_playback_auto_capture}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**playback_auto_capture** = `true`
`🔗<class_AnimationPlayer_property_playback_auto_capture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_capture**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_auto_capture**()

If `true`, performs
`AnimationMixer.capture()<class_AnimationMixer_method_capture>`{.interpreted-text
role="ref"} before playback automatically. This means just
`play_with_capture()<class_AnimationPlayer_method_play_with_capture>`{.interpreted-text
role="ref"} is executed with default arguments instead of
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Capture interpolation is only performed if the animation
contains a capture track. See also
`Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_playback_auto_capture_duration}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**playback_auto_capture_duration** = `-1.0`
`🔗<class_AnimationPlayer_property_playback_auto_capture_duration>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_capture_duration**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_capture_duration**()

See also
`play_with_capture()<class_AnimationPlayer_method_play_with_capture>`{.interpreted-text
role="ref"} and
`AnimationMixer.capture()<class_AnimationMixer_method_capture>`{.interpreted-text
role="ref"}.

If
`playback_auto_capture_duration<class_AnimationPlayer_property_playback_auto_capture_duration>`{.interpreted-text
role="ref"} is negative value, the duration is set to the interval
between the current position and the first key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_playback_auto_capture_ease_type}
::: rst-class
classref-property
:::
::::

`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
**playback_auto_capture_ease_type** = `0`
`🔗<class_AnimationPlayer_property_playback_auto_capture_ease_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_capture_ease_type**(value:
  `EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"})
- `EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
  **get_auto_capture_ease_type**()

The ease type of the capture interpolation. See also
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_playback_auto_capture_transition_type}
::: rst-class
classref-property
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **playback_auto_capture_transition_type** = `0`
`🔗<class_AnimationPlayer_property_playback_auto_capture_transition_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_capture_transition_type**(value:
  `TransitionType<enum_Tween_TransitionType>`{.interpreted-text
  role="ref"})
- `TransitionType<enum_Tween_TransitionType>`{.interpreted-text
  role="ref"} **get_auto_capture_transition_type**()

The transition type of the capture interpolation. See also
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_playback_default_blend_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**playback_default_blend_time** = `0.0`
`🔗<class_AnimationPlayer_property_playback_default_blend_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_blend_time**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_default_blend_time**()

The default time in which to blend animations. Ranges from 0 to 4096
with 0.01 precision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_property_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **speed_scale** =
`1.0` `🔗<class_AnimationPlayer_property_speed_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_speed_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_speed_scale**()

The speed scaling ratio. For example, if this value is `1`, then the
animation plays at normal speed. If it\'s `0.5`, then it plays at half
speed. If it\'s `2`, then it plays at double speed.

If set to a negative value, the animation is played in reverse. If set
to `0`, the animation will not advance.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationPlayer_method_animation_get_next}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**animation_get_next**(animation_from:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_animation_get_next>`{.interpreted-text
role="ref"}

Returns the key of the animation which is queued to play after the
`animation_from` animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_animation_set_next}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**animation_set_next**(animation_from:
`StringName<class_StringName>`{.interpreted-text role="ref"},
animation_to: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AnimationPlayer_method_animation_set_next>`{.interpreted-text
role="ref"}

Triggers the `animation_to` animation when the `animation_from`
animation completes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_clear_queue}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_queue**()
`🔗<class_AnimationPlayer_method_clear_queue>`{.interpreted-text
role="ref"}

Clears all queued, unplayed animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_blend_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_blend_time**(animation_from:
`StringName<class_StringName>`{.interpreted-text role="ref"},
animation_to: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_blend_time>`{.interpreted-text
role="ref"}

Returns the blend time (in seconds) between two animations, referenced
by their keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_method_call_mode}
::: rst-class
classref-method
:::
::::

`AnimationMethodCallMode<enum_AnimationPlayer_AnimationMethodCallMode>`{.interpreted-text
role="ref"} **get_method_call_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_method_call_mode>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.callback_mode_method<class_AnimationMixer_property_callback_mode_method>`{.interpreted-text
role="ref"} instead.

Returns the call mode used for \"Call Method\" tracks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_playing_speed}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_playing_speed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_playing_speed>`{.interpreted-text
role="ref"}

Returns the actual playing speed of current animation or `0` if not
playing. This speed is the
`speed_scale<class_AnimationPlayer_property_speed_scale>`{.interpreted-text
role="ref"} property multiplied by `custom_speed` argument specified
when calling the
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"} method.

Returns a negative value if the current animation is playing backwards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_process_callback}
::: rst-class
classref-method
:::
::::

`AnimationProcessCallback<enum_AnimationPlayer_AnimationProcessCallback>`{.interpreted-text
role="ref"} **get_process_callback**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_process_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"} instead.

Returns the process notification in which to update animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_queue}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_queue**()
`🔗<class_AnimationPlayer_method_get_queue>`{.interpreted-text
role="ref"}

Returns a list of the animation keys that are currently queued to play.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_root}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **get_root**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_root>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.root_node<class_AnimationMixer_property_root_node>`{.interpreted-text
role="ref"} instead.

Returns the node which node path references will travel from.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_section_end_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_section_end_time**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_section_end_time>`{.interpreted-text
role="ref"}

Returns the end time of the section currently being played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_get_section_start_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_section_start_time**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_get_section_start_time>`{.interpreted-text
role="ref"}

Returns the start time of the section currently being played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_has_section}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_section**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_has_section>`{.interpreted-text
role="ref"}

Returns `true` if an animation is currently playing with a section.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationPlayer_method_is_playing>`{.interpreted-text
role="ref"}

Returns `true` if an animation is currently playing (even if
`speed_scale<class_AnimationPlayer_property_speed_scale>`{.interpreted-text
role="ref"} and/or `custom_speed` are `0`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_pause}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **pause**()
`🔗<class_AnimationPlayer_method_pause>`{.interpreted-text role="ref"}

Pauses the currently playing animation. The
`current_animation_position<class_AnimationPlayer_property_current_animation_position>`{.interpreted-text
role="ref"} will be kept and calling
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"} or
`play_backwards()<class_AnimationPlayer_method_play_backwards>`{.interpreted-text
role="ref"} without arguments or with the same animation name as
`assigned_animation<class_AnimationPlayer_property_assigned_animation>`{.interpreted-text
role="ref"} will resume the animation.

See also `stop()<class_AnimationPlayer_method_stop>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **play**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
custom_blend: `float<class_float>`{.interpreted-text role="ref"} = -1,
custom_speed: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
from_end: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_AnimationPlayer_method_play>`{.interpreted-text role="ref"}

Plays the animation with key `name`. Custom blend times and speed can be
set.

The `from_end` option only affects when switching to a new animation
track, or if the same track but at the start or end. It does not affect
resuming playback that was paused in the middle of an animation. If
`custom_speed` is negative and `from_end` is `true`, the animation will
play backwards (which is equivalent to calling
`play_backwards()<class_AnimationPlayer_method_play_backwards>`{.interpreted-text
role="ref"}).

The **AnimationPlayer** keeps track of its current or last played
animation with
`assigned_animation<class_AnimationPlayer_property_assigned_animation>`{.interpreted-text
role="ref"}. If this method is called with that same animation `name`,
or with no `name` parameter, the assigned animation will resume playing
if it was paused.

\*\*Note:\*\* The animation will be updated the next time the
**AnimationPlayer** is processed. If other variables are updated at the
same time this is called, they may be updated too early. To perform the
update immediately, call `advance(0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play_backwards}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_backwards**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
custom_blend: `float<class_float>`{.interpreted-text role="ref"} = -1)
`🔗<class_AnimationPlayer_method_play_backwards>`{.interpreted-text
role="ref"}

Plays the animation with key `name` in reverse.

This method is a shorthand for
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"} with `custom_speed = -1.0` and `from_end = true`, so see its
description for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play_section}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_section**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\", start_time: `float<class_float>`{.interpreted-text
role="ref"} = -1, end_time: `float<class_float>`{.interpreted-text
role="ref"} = -1, custom_blend: `float<class_float>`{.interpreted-text
role="ref"} = -1, custom_speed: `float<class_float>`{.interpreted-text
role="ref"} = 1.0, from_end: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_AnimationPlayer_method_play_section>`{.interpreted-text
role="ref"}

Plays the animation with key `name` and the section starting from
`start_time` and ending on `end_time`. See also
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"}.

Setting `start_time` to a value outside the range of the animation means
the start of the animation will be used instead, and setting `end_time`
to a value outside the range of the animation means the end of the
animation will be used instead. `start_time` cannot be equal to
`end_time`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play_section_backwards}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_section_backwards**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
start_time: `float<class_float>`{.interpreted-text role="ref"} = -1,
end_time: `float<class_float>`{.interpreted-text role="ref"} = -1,
custom_blend: `float<class_float>`{.interpreted-text role="ref"} = -1)
`🔗<class_AnimationPlayer_method_play_section_backwards>`{.interpreted-text
role="ref"}

Plays the animation with key `name` and the section starting from
`start_time` and ending on `end_time` in reverse.

This method is a shorthand for
`play_section()<class_AnimationPlayer_method_play_section>`{.interpreted-text
role="ref"} with `custom_speed = -1.0` and `from_end = true`, see its
description for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play_section_with_markers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_section_with_markers**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
start_marker: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\", end_marker:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
custom_blend: `float<class_float>`{.interpreted-text role="ref"} = -1,
custom_speed: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
from_end: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_AnimationPlayer_method_play_section_with_markers>`{.interpreted-text
role="ref"}

Plays the animation with key `name` and the section starting from
`start_marker` and ending on `end_marker`.

If the start marker is empty, the section starts from the beginning of
the animation. If the end marker is empty, the section ends on the end
of the animation. See also
`play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play_section_with_markers_backwards}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_section_with_markers_backwards**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
start_marker: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\", end_marker:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
custom_blend: `float<class_float>`{.interpreted-text role="ref"} = -1)
`🔗<class_AnimationPlayer_method_play_section_with_markers_backwards>`{.interpreted-text
role="ref"}

Plays the animation with key `name` and the section starting from
`start_marker` and ending on `end_marker` in reverse.

This method is a shorthand for
`play_section_with_markers()<class_AnimationPlayer_method_play_section_with_markers>`{.interpreted-text
role="ref"} with `custom_speed = -1.0` and `from_end = true`, see its
description for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_play_with_capture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_with_capture**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
duration: `float<class_float>`{.interpreted-text role="ref"} = -1.0,
custom_blend: `float<class_float>`{.interpreted-text role="ref"} = -1,
custom_speed: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
from_end: `bool<class_bool>`{.interpreted-text role="ref"} = false,
trans_type:
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} = 0, ease_type:
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"} = 0)
`🔗<class_AnimationPlayer_method_play_with_capture>`{.interpreted-text
role="ref"}

See also
`AnimationMixer.capture()<class_AnimationMixer_method_capture>`{.interpreted-text
role="ref"}.

You can use this method to use more detailed options for capture than
those performed by
`playback_auto_capture<class_AnimationPlayer_property_playback_auto_capture>`{.interpreted-text
role="ref"}. When
`playback_auto_capture<class_AnimationPlayer_property_playback_auto_capture>`{.interpreted-text
role="ref"} is `false`, this method is almost the same as the following:

    capture(name, duration, trans_type, ease_type)
    play(name, custom_blend, custom_speed, from_end)

If `name` is blank, it specifies
`assigned_animation<class_AnimationPlayer_property_assigned_animation>`{.interpreted-text
role="ref"}.

If `duration` is a negative value, the duration is set to the interval
between the current position and the first key, when `from_end` is
`true`, uses the interval between the current position and the last key
instead.

\*\*Note:\*\* The `duration` takes
`speed_scale<class_AnimationPlayer_property_speed_scale>`{.interpreted-text
role="ref"} into account, but `custom_speed` does not, because the
capture cache is interpolated with the blend result and the result may
contain multiple animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_queue}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **queue**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationPlayer_method_queue>`{.interpreted-text role="ref"}

Queues an animation for playback once the current animation and all
previously queued animations are done.

\*\*Note:\*\* If a looped animation is currently playing, the queued
animation will never play unless the looped animation is stopped
somehow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_reset_section}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_section**()
`🔗<class_AnimationPlayer_method_reset_section>`{.interpreted-text
role="ref"}

Resets the current section. Does nothing if a section has not been set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek**(seconds: `float<class_float>`{.interpreted-text role="ref"},
update: `bool<class_bool>`{.interpreted-text role="ref"} = false,
update_only: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_AnimationPlayer_method_seek>`{.interpreted-text role="ref"}

Seeks the animation to the `seconds` point in time (in seconds). If
`update` is `true`, the animation updates too, otherwise it updates at
process time. Events between the current frame and `seconds` are
skipped.

If `update_only` is `true`, the method / audio / animation playback
tracks will not be processed.

\*\*Note:\*\* Seeking to the end of the animation doesn\'t emit
`AnimationMixer.animation_finished<class_AnimationMixer_signal_animation_finished>`{.interpreted-text
role="ref"}. If you want to skip animation and emit the signal, use
`AnimationMixer.advance()<class_AnimationMixer_method_advance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_set_blend_time}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_time**(animation_from:
`StringName<class_StringName>`{.interpreted-text role="ref"},
animation_to: `StringName<class_StringName>`{.interpreted-text
role="ref"}, sec: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AnimationPlayer_method_set_blend_time>`{.interpreted-text
role="ref"}

Specifies a blend time (in seconds) between two animations, referenced
by their keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_set_method_call_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_method_call_mode**(mode:
`AnimationMethodCallMode<enum_AnimationPlayer_AnimationMethodCallMode>`{.interpreted-text
role="ref"})
`🔗<class_AnimationPlayer_method_set_method_call_mode>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.callback_mode_method<class_AnimationMixer_property_callback_mode_method>`{.interpreted-text
role="ref"} instead.

Sets the call mode used for \"Call Method\" tracks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_set_process_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_callback**(mode:
`AnimationProcessCallback<enum_AnimationPlayer_AnimationProcessCallback>`{.interpreted-text
role="ref"})
`🔗<class_AnimationPlayer_method_set_process_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"} instead.

Sets the process notification in which to update animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_set_root}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_root**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`🔗<class_AnimationPlayer_method_set_root>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.root_node<class_AnimationMixer_property_root_node>`{.interpreted-text
role="ref"} instead.

Sets the node which node path references will travel from.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_set_section}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_section**(start_time: `float<class_float>`{.interpreted-text
role="ref"} = -1, end_time: `float<class_float>`{.interpreted-text
role="ref"} = -1)
`🔗<class_AnimationPlayer_method_set_section>`{.interpreted-text
role="ref"}

Changes the start and end times of the section being played. The current
playback position will be clamped within the new section. See also
`play_section()<class_AnimationPlayer_method_play_section>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_set_section_with_markers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_section_with_markers**(start_marker:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
end_marker: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`🔗<class_AnimationPlayer_method_set_section_with_markers>`{.interpreted-text
role="ref"}

Changes the start and end markers of the section being played. The
current playback position will be clamped within the new section. See
also
`play_section_with_markers()<class_AnimationPlayer_method_play_section_with_markers>`{.interpreted-text
role="ref"}.

If the argument is empty, the section uses the beginning or end of the
animation. If both are empty, it means that the section is not set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationPlayer_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**stop**(keep_state: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_AnimationPlayer_method_stop>`{.interpreted-text
role="ref"}

Stops the currently playing animation. The animation position is reset
to `0` and the `custom_speed` is reset to `1.0`. See also
`pause()<class_AnimationPlayer_method_pause>`{.interpreted-text
role="ref"}.

If `keep_state` is `true`, the animation state is not updated visually.

\*\*Note:\*\* The method / audio / animation playback tracks will not be
processed by this method.
