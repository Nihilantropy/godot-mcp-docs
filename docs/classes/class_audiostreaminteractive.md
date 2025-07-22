github_url
:   hide

# AudioStreamInteractive {#class_AudioStreamInteractive}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Audio stream that can playback music interactively, combining clips and
a transition table.

::: rst-class
classref-introduction-group
:::

## Description

This is an audio stream that can playback music interactively, combining
clips and a transition table. Clips must be added first, and then the
transition rules via the
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}. Additionally, this stream exports a property parameter to
control the playback via
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"},
`AudioStreamPlayer2D<class_AudioStreamPlayer2D>`{.interpreted-text
role="ref"}, or
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"}.

The way this is used is by filling a number of clips, then configuring
the transition table. From there, clips are selected for playback and
the music will smoothly go from the current to the new one while using
the corresponding transition rule defined in the transition table.

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

:::: {#enum_AudioStreamInteractive_TransitionFromTime}
::: rst-class
classref-enumeration
:::
::::

enum **TransitionFromTime**:
`🔗<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_IMMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"} **TRANSITION_FROM_TIME_IMMEDIATE** = `0`

Start transition as soon as possible, don\'t wait for any specific time
position.

:::: {#class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_NEXT_BEAT}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"} **TRANSITION_FROM_TIME_NEXT_BEAT** = `1`

Transition when the clip playback position reaches the next beat.

:::: {#class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_NEXT_BAR}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"} **TRANSITION_FROM_TIME_NEXT_BAR** = `2`

Transition when the clip playback position reaches the next bar.

:::: {#class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_END}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"} **TRANSITION_FROM_TIME_END** = `3`

Transition when the current clip finished playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AudioStreamInteractive_TransitionToTime}
::: rst-class
classref-enumeration
:::
::::

enum **TransitionToTime**:
`🔗<enum_AudioStreamInteractive_TransitionToTime>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamInteractive_constant_TRANSITION_TO_TIME_SAME_POSITION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>`{.interpreted-text
role="ref"} **TRANSITION_TO_TIME_SAME_POSITION** = `0`

Transition to the same position in the destination clip. This is useful
when both clips have exactly the same length and the music should fade
between them.

:::: {#class_AudioStreamInteractive_constant_TRANSITION_TO_TIME_START}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>`{.interpreted-text
role="ref"} **TRANSITION_TO_TIME_START** = `1`

Transition to the start of the destination clip.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AudioStreamInteractive_FadeMode}
::: rst-class
classref-enumeration
:::
::::

enum **FadeMode**:
`🔗<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text role="ref"}

:::: {#class_AudioStreamInteractive_constant_FADE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"} **FADE_DISABLED** = `0`

Do not use fade for the transition. This is useful when transitioning
from a clip-end to clip-beginning, and each clip has their begin/end.

:::: {#class_AudioStreamInteractive_constant_FADE_IN}
::: rst-class
classref-enumeration-constant
:::
::::

`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"} **FADE_IN** = `1`

Use a fade-in in the next clip, let the current clip finish.

:::: {#class_AudioStreamInteractive_constant_FADE_OUT}
::: rst-class
classref-enumeration-constant
:::
::::

`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"} **FADE_OUT** = `2`

Use a fade-out in the current clip, the next clip will start by itself.

:::: {#class_AudioStreamInteractive_constant_FADE_CROSS}
::: rst-class
classref-enumeration-constant
:::
::::

`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"} **FADE_CROSS** = `3`

Use a cross-fade between clips.

:::: {#class_AudioStreamInteractive_constant_FADE_AUTOMATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"} **FADE_AUTOMATIC** = `4`

Use automatic fade logic depending on the transition from/to. It is
recommended to use this by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AudioStreamInteractive_AutoAdvanceMode}
::: rst-class
classref-enumeration
:::
::::

enum **AutoAdvanceMode**:
`🔗<enum_AudioStreamInteractive_AutoAdvanceMode>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamInteractive_constant_AUTO_ADVANCE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`{.interpreted-text
role="ref"} **AUTO_ADVANCE_DISABLED** = `0`

Disable auto-advance (default).

:::: {#class_AudioStreamInteractive_constant_AUTO_ADVANCE_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`{.interpreted-text
role="ref"} **AUTO_ADVANCE_ENABLED** = `1`

Enable auto-advance, a clip must be specified.

:::: {#class_AudioStreamInteractive_constant_AUTO_ADVANCE_RETURN_TO_HOLD}
::: rst-class
classref-enumeration-constant
:::
::::

`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`{.interpreted-text
role="ref"} **AUTO_ADVANCE_RETURN_TO_HOLD** = `2`

Enable auto-advance, but instead of specifying a clip, the playback will
return to hold (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_AudioStreamInteractive_constant_CLIP_ANY}
::: rst-class
classref-constant
:::
::::

**CLIP_ANY** = `-1`
`🔗<class_AudioStreamInteractive_constant_CLIP_ANY>`{.interpreted-text
role="ref"}

This constant describes that any clip is valid for a specific transition
as either source or destination.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamInteractive_property_clip_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **clip_count** = `0`
`🔗<class_AudioStreamInteractive_property_clip_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clip_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_clip_count**()

Amount of clips contained in this interactive player.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_property_initial_clip}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **initial_clip** = `0`
`🔗<class_AudioStreamInteractive_property_initial_clip>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_initial_clip**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_initial_clip**()

Index of the initial clip, which will be played first when this stream
is played.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamInteractive_method_add_transition}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_transition**(from_clip: `int<class_int>`{.interpreted-text
role="ref"}, to_clip: `int<class_int>`{.interpreted-text role="ref"},
from_time:
`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"}, to_time:
`TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>`{.interpreted-text
role="ref"}, fade_mode:
`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"}, fade_beats: `float<class_float>`{.interpreted-text
role="ref"}, use_filler_clip: `bool<class_bool>`{.interpreted-text
role="ref"} = false, filler_clip: `int<class_int>`{.interpreted-text
role="ref"} = -1, hold_previous: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}

Add a transition between two clips. Provide the indices of the source
and destination clips, or use the
`CLIP_ANY<class_AudioStreamInteractive_constant_CLIP_ANY>`{.interpreted-text
role="ref"} constant to indicate that transition happens to/from any
clip to this one.

\* `from_time` indicates the moment in the current clip the transition
will begin after triggered.

\* `to_time` indicates the time in the next clip that the playback will
start from.

\* `fade_mode` indicates how the fade will happen between clips. If
unsure, just use
`FADE_AUTOMATIC<class_AudioStreamInteractive_constant_FADE_AUTOMATIC>`{.interpreted-text
role="ref"} which uses the most common type of fade for each situation.

\* `fade_beats` indicates how many beats the fade will take. Using
decimals is allowed.

\* `use_filler_clip` indicates that there will be a filler clip used
between the source and destination clips.

\* `filler_clip` the index of the filler clip.

\* If `hold_previous` is used, then this clip will be remembered. This
can be used together with
`AUTO_ADVANCE_RETURN_TO_HOLD<class_AudioStreamInteractive_constant_AUTO_ADVANCE_RETURN_TO_HOLD>`{.interpreted-text
role="ref"} to return to this clip after another is done playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_erase_transition}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_transition**(from_clip: `int<class_int>`{.interpreted-text
role="ref"}, to_clip: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamInteractive_method_erase_transition>`{.interpreted-text
role="ref"}

Erase a transition by providing `from_clip` and `to_clip` clip indices.
`CLIP_ANY<class_AudioStreamInteractive_constant_CLIP_ANY>`{.interpreted-text
role="ref"} can be used for either argument or both.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_clip_auto_advance}
::: rst-class
classref-method
:::
::::

`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`{.interpreted-text
role="ref"} **get_clip_auto_advance**(clip_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_clip_auto_advance>`{.interpreted-text
role="ref"}

Return whether a clip has auto-advance enabled. See
`set_clip_auto_advance()<class_AudioStreamInteractive_method_set_clip_auto_advance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_clip_auto_advance_next_clip**(clip_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip>`{.interpreted-text
role="ref"}

Return the clip towards which the clip referenced by `clip_index` will
auto-advance to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_clip_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_clip_name**(clip_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_clip_name>`{.interpreted-text
role="ref"}

Return the name of a clip.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_clip_stream}
::: rst-class
classref-method
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**get_clip_stream**(clip_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_clip_stream>`{.interpreted-text
role="ref"}

Return the `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} associated with a clip.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_transition_fade_beats}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_transition_fade_beats**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_transition_fade_beats>`{.interpreted-text
role="ref"}

Return the time (in beats) for a transition (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_transition_fade_mode}
::: rst-class
classref-method
:::
::::

`FadeMode<enum_AudioStreamInteractive_FadeMode>`{.interpreted-text
role="ref"} **get_transition_fade_mode**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_transition_fade_mode>`{.interpreted-text
role="ref"}

Return the mode for a transition (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_transition_filler_clip}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_transition_filler_clip**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_transition_filler_clip>`{.interpreted-text
role="ref"}

Return the filler clip for a transition (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_transition_from_time}
::: rst-class
classref-method
:::
::::

`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`{.interpreted-text
role="ref"} **get_transition_from_time**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_transition_from_time>`{.interpreted-text
role="ref"}

Return the source time position for a transition (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_transition_list}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_transition_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_transition_list>`{.interpreted-text
role="ref"}

Return the list of transitions (from, to interleaved).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_get_transition_to_time}
::: rst-class
classref-method
:::
::::

`TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>`{.interpreted-text
role="ref"} **get_transition_to_time**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_get_transition_to_time>`{.interpreted-text
role="ref"}

Return the destination time position for a transition (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_has_transition}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_transition**(from_clip: `int<class_int>`{.interpreted-text
role="ref"}, to_clip: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_has_transition>`{.interpreted-text
role="ref"}

Returns `true` if a given transition exists (was added via
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_is_transition_holding_previous}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_transition_holding_previous**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_is_transition_holding_previous>`{.interpreted-text
role="ref"}

Return whether a transition uses the *hold previous* functionality (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_is_transition_using_filler_clip}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_transition_using_filler_clip**(from_clip:
`int<class_int>`{.interpreted-text role="ref"}, to_clip:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamInteractive_method_is_transition_using_filler_clip>`{.interpreted-text
role="ref"}

Return whether a transition uses the *filler clip* functionality (see
`add_transition()<class_AudioStreamInteractive_method_add_transition>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_set_clip_auto_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_clip_auto_advance**(clip_index: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamInteractive_method_set_clip_auto_advance>`{.interpreted-text
role="ref"}

Set whether a clip will auto-advance by changing the auto-advance mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_clip_auto_advance_next_clip**(clip_index:
`int<class_int>`{.interpreted-text role="ref"}, auto_advance_next_clip:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip>`{.interpreted-text
role="ref"}

Set the index of the next clip towards which this clip will auto advance
to when finished. If the clip being played loops, then auto-advance will
be ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_set_clip_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_clip_name**(clip_index: `int<class_int>`{.interpreted-text
role="ref"}, name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamInteractive_method_set_clip_name>`{.interpreted-text
role="ref"}

Set the name of the current clip (for easier identification).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamInteractive_method_set_clip_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_clip_stream**(clip_index: `int<class_int>`{.interpreted-text
role="ref"}, stream: `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamInteractive_method_set_clip_stream>`{.interpreted-text
role="ref"}

Set the `AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
associated with the current clip.
