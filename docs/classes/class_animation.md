github_url
:   hide

# Animation {#class_Animation}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds data that can be used to animate anything in the engine.

::: rst-class
classref-introduction-group
:::

## Description

This resource holds data that can be used to animate anything in the
engine. Animations are divided into tracks and each track must be linked
to a node. The state of that node can be changed through time, by adding
timed keys (events) to the track.

::::: tabs
::: code-tab
gdscript

\# This creates an animation that makes the node \"Enemy\" move to the
right by \# 100 pixels in 2.0 seconds. var animation = Animation.new()
var track_index = animation.add_track(Animation.TYPE_VALUE)
animation.track_set_path(track_index, \"Enemy:position:x\")
animation.track_insert_key(track_index, 0.0, 0)
animation.track_insert_key(track_index, 2.0, 100) animation.length = 2.0
:::

::: code-tab
csharp

// This creates an animation that makes the node \"Enemy\" move to the
right by // 100 pixels in 2.0 seconds. var animation = new Animation();
int trackIndex = animation.AddTrack(Animation.TrackType.Value);
animation.TrackSetPath(trackIndex, \"Enemy:position:x\");
animation.TrackInsertKey(trackIndex, 0.0f, 0);
animation.TrackInsertKey(trackIndex, 2.0f, 100); animation.Length =
2.0f;
:::
:::::

Animations are just data containers, and must be added to nodes such as
an `AnimationPlayer<class_AnimationPlayer>`{.interpreted-text
role="ref"} to be played back. Animation tracks have different types,
each with its own set of dedicated methods. Check
`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"} to
see available types.

\*\*Note:\*\* For 3D position/rotation/scale, using the dedicated
`TYPE_POSITION_3D<class_Animation_constant_TYPE_POSITION_3D>`{.interpreted-text
role="ref"},
`TYPE_ROTATION_3D<class_Animation_constant_TYPE_ROTATION_3D>`{.interpreted-text
role="ref"} and
`TYPE_SCALE_3D<class_Animation_constant_TYPE_SCALE_3D>`{.interpreted-text
role="ref"} track types instead of
`TYPE_VALUE<class_Animation_constant_TYPE_VALUE>`{.interpreted-text
role="ref"} is recommended for performance reasons.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Animation documentation index <../tutorials/animation/index>`{.interpreted-text
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

:::: {#enum_Animation_TrackType}
::: rst-class
classref-enumeration
:::
::::

enum **TrackType**: `🔗<enum_Animation_TrackType>`{.interpreted-text
role="ref"}

:::: {#class_Animation_constant_TYPE_VALUE}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_VALUE** = `0`

Value tracks set values in node properties, but only those which can be
interpolated. For 3D position/rotation/scale, using the dedicated
`TYPE_POSITION_3D<class_Animation_constant_TYPE_POSITION_3D>`{.interpreted-text
role="ref"},
`TYPE_ROTATION_3D<class_Animation_constant_TYPE_ROTATION_3D>`{.interpreted-text
role="ref"} and
`TYPE_SCALE_3D<class_Animation_constant_TYPE_SCALE_3D>`{.interpreted-text
role="ref"} track types instead of
`TYPE_VALUE<class_Animation_constant_TYPE_VALUE>`{.interpreted-text
role="ref"} is recommended for performance reasons.

:::: {#class_Animation_constant_TYPE_POSITION_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_POSITION_3D** = `1`

3D position track (values are stored in
`Vector3<class_Vector3>`{.interpreted-text role="ref"}s).

:::: {#class_Animation_constant_TYPE_ROTATION_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_ROTATION_3D** = `2`

3D rotation track (values are stored in
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}s).

:::: {#class_Animation_constant_TYPE_SCALE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_SCALE_3D** = `3`

3D scale track (values are stored in
`Vector3<class_Vector3>`{.interpreted-text role="ref"}s).

:::: {#class_Animation_constant_TYPE_BLEND_SHAPE}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_BLEND_SHAPE** = `4`

Blend shape track.

:::: {#class_Animation_constant_TYPE_METHOD}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_METHOD** = `5`

Method tracks call functions with given arguments per key.

:::: {#class_Animation_constant_TYPE_BEZIER}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_BEZIER** = `6`

Bezier tracks are used to interpolate a value using custom curves. They
can also be used to animate sub-properties of vectors and colors (e.g.
alpha value of a `Color<class_Color>`{.interpreted-text role="ref"}).

:::: {#class_Animation_constant_TYPE_AUDIO}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_AUDIO** = `7`

Audio tracks are used to play an audio stream with either type of
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"}. The stream can be trimmed and previewed in the animation.

:::: {#class_Animation_constant_TYPE_ANIMATION}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**TYPE_ANIMATION** = `8`

Animation tracks play animations in other
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Animation_InterpolationType}
::: rst-class
classref-enumeration
:::
::::

enum **InterpolationType**:
`🔗<enum_Animation_InterpolationType>`{.interpreted-text role="ref"}

:::: {#class_Animation_constant_INTERPOLATION_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"} **INTERPOLATION_NEAREST** = `0`

No interpolation (nearest value).

:::: {#class_Animation_constant_INTERPOLATION_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"} **INTERPOLATION_LINEAR** = `1`

Linear interpolation.

:::: {#class_Animation_constant_INTERPOLATION_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"} **INTERPOLATION_CUBIC** = `2`

Cubic interpolation. This looks smoother than linear interpolation, but
is more expensive to interpolate. Stick to
`INTERPOLATION_LINEAR<class_Animation_constant_INTERPOLATION_LINEAR>`{.interpreted-text
role="ref"} for complex 3D animations imported from external software,
even if it requires using a higher animation framerate in return.

:::: {#class_Animation_constant_INTERPOLATION_LINEAR_ANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"} **INTERPOLATION_LINEAR_ANGLE** = `3`

Linear interpolation with shortest path rotation.

\*\*Note:\*\* The result value is always normalized and may not match
the key value.

:::: {#class_Animation_constant_INTERPOLATION_CUBIC_ANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"} **INTERPOLATION_CUBIC_ANGLE** = `4`

Cubic interpolation with shortest path rotation.

\*\*Note:\*\* The result value is always normalized and may not match
the key value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Animation_UpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **UpdateMode**: `🔗<enum_Animation_UpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_Animation_constant_UPDATE_CONTINUOUS}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_Animation_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_CONTINUOUS** = `0`

Update between keyframes and hold the value.

:::: {#class_Animation_constant_UPDATE_DISCRETE}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_Animation_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_DISCRETE** = `1`

Update at the keyframes.

:::: {#class_Animation_constant_UPDATE_CAPTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_Animation_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_CAPTURE** = `2`

Same as
`UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>`{.interpreted-text
role="ref"} but works as a flag to capture the value of the current
object and perform interpolation in some methods. See also
`AnimationMixer.capture()<class_AnimationMixer_method_capture>`{.interpreted-text
role="ref"},
`AnimationPlayer.playback_auto_capture<class_AnimationPlayer_property_playback_auto_capture>`{.interpreted-text
role="ref"}, and
`AnimationPlayer.play_with_capture()<class_AnimationPlayer_method_play_with_capture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Animation_LoopMode}
::: rst-class
classref-enumeration
:::
::::

enum **LoopMode**: `🔗<enum_Animation_LoopMode>`{.interpreted-text
role="ref"}

:::: {#class_Animation_constant_LOOP_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
**LOOP_NONE** = `0`

At both ends of the animation, the animation will stop playing.

:::: {#class_Animation_constant_LOOP_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
**LOOP_LINEAR** = `1`

At both ends of the animation, the animation will be repeated without
changing the playback direction.

:::: {#class_Animation_constant_LOOP_PINGPONG}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
**LOOP_PINGPONG** = `2`

Repeats playback and reverse playback at both ends of the animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Animation_LoopedFlag}
::: rst-class
classref-enumeration
:::
::::

enum **LoopedFlag**: `🔗<enum_Animation_LoopedFlag>`{.interpreted-text
role="ref"}

:::: {#class_Animation_constant_LOOPED_FLAG_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopedFlag<enum_Animation_LoopedFlag>`{.interpreted-text role="ref"}
**LOOPED_FLAG_NONE** = `0`

This flag indicates that the animation proceeds without any looping.

:::: {#class_Animation_constant_LOOPED_FLAG_END}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopedFlag<enum_Animation_LoopedFlag>`{.interpreted-text role="ref"}
**LOOPED_FLAG_END** = `1`

This flag indicates that the animation has reached the end of the
animation and just after loop processed.

:::: {#class_Animation_constant_LOOPED_FLAG_START}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopedFlag<enum_Animation_LoopedFlag>`{.interpreted-text role="ref"}
**LOOPED_FLAG_START** = `2`

This flag indicates that the animation has reached the start of the
animation and just after loop processed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Animation_FindMode}
::: rst-class
classref-enumeration
:::
::::

enum **FindMode**: `🔗<enum_Animation_FindMode>`{.interpreted-text
role="ref"}

:::: {#class_Animation_constant_FIND_MODE_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`FindMode<enum_Animation_FindMode>`{.interpreted-text role="ref"}
**FIND_MODE_NEAREST** = `0`

Finds the nearest time key.

:::: {#class_Animation_constant_FIND_MODE_APPROX}
::: rst-class
classref-enumeration-constant
:::
::::

`FindMode<enum_Animation_FindMode>`{.interpreted-text role="ref"}
**FIND_MODE_APPROX** = `1`

Finds only the key with approximating the time.

:::: {#class_Animation_constant_FIND_MODE_EXACT}
::: rst-class
classref-enumeration-constant
:::
::::

`FindMode<enum_Animation_FindMode>`{.interpreted-text role="ref"}
**FIND_MODE_EXACT** = `2`

Finds only the key with matching the time.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Animation_property_capture_included}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **capture_included** =
`false`
`🔗<class_Animation_property_capture_included>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_capture_included**()

Returns `true` if the capture track is included. This is a cached
readonly value for performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_property_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length** = `1.0`
`🔗<class_Animation_property_length>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_length**()

The total length of the animation (in seconds).

\*\*Note:\*\* Length is not delimited by the last key, as this one may
be before or after the end to ensure correct interpolation and looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_property_loop_mode}
::: rst-class
classref-property
:::
::::

`LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
**loop_mode** = `0`
`🔗<class_Animation_property_loop_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_mode**(value:
  `LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"})
- `LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
  **get_loop_mode**()

Determines the behavior of both ends of the animation timeline during
animation playback. This indicates whether and how the animation should
be restarted, and is also used to correctly interpolate animation
cycles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_property_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **step** =
`0.033333335` `🔗<class_Animation_property_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_step**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_step**()

The animation step value.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Animation_method_add_marker}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_marker**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, time: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_add_marker>`{.interpreted-text role="ref"}

Adds a marker to this Animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_add_track}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_track**(type:
`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"},
at_position: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_Animation_method_add_track>`{.interpreted-text role="ref"}

Adds a track to the Animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_animation_track_get_key_animation}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**animation_track_get_key_animation**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_animation_track_get_key_animation>`{.interpreted-text
role="ref"}

Returns the animation name at the key identified by `key_idx`. The
`track_idx` must be the index of an Animation Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_animation_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**animation_track_insert_key**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"}, animation:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_animation_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a key with value `animation` at the given `time` (in seconds).
The `track_idx` must be the index of an Animation Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_animation_track_set_key_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**animation_track_set_key_animation**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, animation:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_animation_track_set_key_animation>`{.interpreted-text
role="ref"}

Sets the key identified by `key_idx` to value `animation`. The
`track_idx` must be the index of an Animation Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_get_key_end_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**audio_track_get_key_end_offset**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_audio_track_get_key_end_offset>`{.interpreted-text
role="ref"}

Returns the end offset of the key identified by `key_idx`. The
`track_idx` must be the index of an Audio Track.

End offset is the number of seconds cut off at the ending of the audio
stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_get_key_start_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**audio_track_get_key_start_offset**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_audio_track_get_key_start_offset>`{.interpreted-text
role="ref"}

Returns the start offset of the key identified by `key_idx`. The
`track_idx` must be the index of an Audio Track.

Start offset is the number of seconds cut off at the beginning of the
audio stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_get_key_stream}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**audio_track_get_key_stream**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_audio_track_get_key_stream>`{.interpreted-text
role="ref"}

Returns the audio stream of the key identified by `key_idx`. The
`track_idx` must be the index of an Audio Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio_track_insert_key**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, time: `float<class_float>`{.interpreted-text role="ref"},
stream: `Resource<class_Resource>`{.interpreted-text role="ref"},
start_offset: `float<class_float>`{.interpreted-text role="ref"} = 0,
end_offset: `float<class_float>`{.interpreted-text role="ref"} = 0)
`🔗<class_Animation_method_audio_track_insert_key>`{.interpreted-text
role="ref"}

Inserts an Audio Track key at the given `time` in seconds. The
`track_idx` must be the index of an Audio Track.

`stream` is the `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} resource to play. `start_offset` is the number of seconds
cut off at the beginning of the audio stream, while `end_offset` is at
the ending.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_is_use_blend}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**audio_track_is_use_blend**(track_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_audio_track_is_use_blend>`{.interpreted-text
role="ref"}

Returns `true` if the track at `track_idx` will be blended with other
animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_set_key_end_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**audio_track_set_key_end_offset**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_audio_track_set_key_end_offset>`{.interpreted-text
role="ref"}

Sets the end offset of the key identified by `key_idx` to value
`offset`. The `track_idx` must be the index of an Audio Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_set_key_start_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**audio_track_set_key_start_offset**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_audio_track_set_key_start_offset>`{.interpreted-text
role="ref"}

Sets the start offset of the key identified by `key_idx` to value
`offset`. The `track_idx` must be the index of an Audio Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_set_key_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**audio_track_set_key_stream**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, stream:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_audio_track_set_key_stream>`{.interpreted-text
role="ref"}

Sets the stream of the key identified by `key_idx` to value `stream`.
The `track_idx` must be the index of an Audio Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_audio_track_set_use_blend}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**audio_track_set_use_blend**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_audio_track_set_use_blend>`{.interpreted-text
role="ref"}

Sets whether the track will be blended with other animations. If `true`,
the audio playback volume changes depending on the blend value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_get_key_in_handle}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**bezier_track_get_key_in_handle**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_bezier_track_get_key_in_handle>`{.interpreted-text
role="ref"}

Returns the in handle of the key identified by `key_idx`. The
`track_idx` must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_get_key_out_handle}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**bezier_track_get_key_out_handle**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_bezier_track_get_key_out_handle>`{.interpreted-text
role="ref"}

Returns the out handle of the key identified by `key_idx`. The
`track_idx` must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_get_key_value}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**bezier_track_get_key_value**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_bezier_track_get_key_value>`{.interpreted-text
role="ref"}

Returns the value of the key identified by `key_idx`. The `track_idx`
must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**bezier_track_insert_key**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"}, value:
`float<class_float>`{.interpreted-text role="ref"}, in_handle:
`Vector2<class_Vector2>`{.interpreted-text role="ref"} = Vector2(0, 0),
out_handle: `Vector2<class_Vector2>`{.interpreted-text role="ref"} =
Vector2(0, 0))
`🔗<class_Animation_method_bezier_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a Bezier Track key at the given `time` in seconds. The
`track_idx` must be the index of a Bezier Track.

`in_handle` is the left-side weight of the added Bezier curve point,
`out_handle` is the right-side one, while `value` is the actual value at
this point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_interpolate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**bezier_track_interpolate**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_bezier_track_interpolate>`{.interpreted-text
role="ref"}

Returns the interpolated value at the given `time` (in seconds). The
`track_idx` must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_set_key_in_handle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bezier_track_set_key_in_handle**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, in_handle:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
balanced_value_time_ratio: `float<class_float>`{.interpreted-text
role="ref"} = 1.0)
`🔗<class_Animation_method_bezier_track_set_key_in_handle>`{.interpreted-text
role="ref"}

Sets the in handle of the key identified by `key_idx` to value
`in_handle`. The `track_idx` must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_set_key_out_handle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bezier_track_set_key_out_handle**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, out_handle:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
balanced_value_time_ratio: `float<class_float>`{.interpreted-text
role="ref"} = 1.0)
`🔗<class_Animation_method_bezier_track_set_key_out_handle>`{.interpreted-text
role="ref"}

Sets the out handle of the key identified by `key_idx` to value
`out_handle`. The `track_idx` must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_bezier_track_set_key_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bezier_track_set_key_value**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_bezier_track_set_key_value>`{.interpreted-text
role="ref"}

Sets the value of the key identified by `key_idx` to the given value.
The `track_idx` must be the index of a Bezier Track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_blend_shape_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**blend_shape_track_insert_key**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_blend_shape_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a key in a given blend shape track. Returns the key index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_blend_shape_track_interpolate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**blend_shape_track_interpolate**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time_sec:
`float<class_float>`{.interpreted-text role="ref"}, backward:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_blend_shape_track_interpolate>`{.interpreted-text
role="ref"}

Returns the interpolated blend shape value at the given time (in
seconds). The `track_idx` must be the index of a blend shape track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_Animation_method_clear>`{.interpreted-text role="ref"}

Clear the animation (clear all tracks and reset all).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_compress}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compress**(page_size: `int<class_int>`{.interpreted-text role="ref"} =
8192, fps: `int<class_int>`{.interpreted-text role="ref"} = 120,
split_tolerance: `float<class_float>`{.interpreted-text role="ref"} =
4.0) `🔗<class_Animation_method_compress>`{.interpreted-text role="ref"}

Compress the animation and all its tracks in-place. This will make
`track_is_compressed()<class_Animation_method_track_is_compressed>`{.interpreted-text
role="ref"} return `true` once called on this **Animation**. Compressed
tracks require less memory to be played, and are designed to be used for
complex 3D animations (such as cutscenes) imported from external 3D
software. Compression is lossy, but the difference is usually not
noticeable in real world conditions.

\*\*Note:\*\* Compressed tracks have various limitations (such as not
being editable from the editor), so only use compressed animations if
you actually need them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_copy_track}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**copy_track**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, to_animation:
`Animation<class_Animation>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_copy_track>`{.interpreted-text role="ref"}

Adds a new track to `to_animation` that is a copy of the given track
from this animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_find_track}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_track**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, type:
`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Animation_method_find_track>`{.interpreted-text
role="ref"}

Returns the index of the specified track. If the track is not found,
return -1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_marker_at_time}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_marker_at_time**(time: `float<class_float>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_marker_at_time>`{.interpreted-text
role="ref"}

Returns the name of the marker located at the given time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_marker_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_marker_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_marker_color>`{.interpreted-text
role="ref"}

Returns the given marker\'s color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_marker_names}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_marker_names**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_marker_names>`{.interpreted-text
role="ref"}

Returns every marker in this Animation, sorted ascending by time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_marker_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_marker_time**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_marker_time>`{.interpreted-text
role="ref"}

Returns the given marker\'s time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_next_marker}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_next_marker**(time: `float<class_float>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_next_marker>`{.interpreted-text
role="ref"}

Returns the closest marker that comes after the given time. If no such
marker exists, an empty string is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_prev_marker}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_prev_marker**(time: `float<class_float>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_prev_marker>`{.interpreted-text
role="ref"}

Returns the closest marker that comes before the given time. If no such
marker exists, an empty string is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_get_track_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_track_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_get_track_count>`{.interpreted-text
role="ref"}

Returns the amount of tracks in the animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_has_marker}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_marker**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Animation_method_has_marker>`{.interpreted-text
role="ref"}

Returns `true` if this Animation contains a marker with the given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_method_track_get_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**method_track_get_name**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, key_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_method_track_get_name>`{.interpreted-text
role="ref"}

Returns the method name of a method track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_method_track_get_params}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**method_track_get_params**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_method_track_get_params>`{.interpreted-text
role="ref"}

Returns the arguments values to be called on a method track for a given
key in a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_optimize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**optimize**(allowed_velocity_err:
`float<class_float>`{.interpreted-text role="ref"} = 0.01,
allowed_angular_err: `float<class_float>`{.interpreted-text role="ref"}
= 0.01, precision: `int<class_int>`{.interpreted-text role="ref"} = 3)
`🔗<class_Animation_method_optimize>`{.interpreted-text role="ref"}

Optimize the animation and all its tracks in-place. This will preserve
only as many keys as are necessary to keep the animation within the
specified bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_position_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**position_track_insert_key**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"}, position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_position_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a key in a given 3D position track. Returns the key index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_position_track_interpolate}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**position_track_interpolate**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time_sec:
`float<class_float>`{.interpreted-text role="ref"}, backward:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_position_track_interpolate>`{.interpreted-text
role="ref"}

Returns the interpolated position value at the given time (in seconds).
The `track_idx` must be the index of a 3D position track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_remove_marker}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_marker**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_Animation_method_remove_marker>`{.interpreted-text role="ref"}

Removes the marker with the given name from this Animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_remove_track}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_track**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_Animation_method_remove_track>`{.interpreted-text
role="ref"}

Removes a track by specifying the track index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_rotation_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rotation_track_insert_key**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"}, rotation:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_rotation_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a key in a given 3D rotation track. Returns the key index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_rotation_track_interpolate}
::: rst-class
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**rotation_track_interpolate**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time_sec:
`float<class_float>`{.interpreted-text role="ref"}, backward:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_rotation_track_interpolate>`{.interpreted-text
role="ref"}

Returns the interpolated rotation value at the given time (in seconds).
The `track_idx` must be the index of a 3D rotation track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_scale_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**scale_track_insert_key**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, time: `float<class_float>`{.interpreted-text role="ref"},
scale: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_scale_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a key in a given 3D scale track. Returns the key index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_scale_track_interpolate}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**scale_track_interpolate**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time_sec:
`float<class_float>`{.interpreted-text role="ref"}, backward:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_scale_track_interpolate>`{.interpreted-text
role="ref"}

Returns the interpolated scale value at the given time (in seconds). The
`track_idx` must be the index of a 3D scale track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_set_marker_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_marker_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_set_marker_color>`{.interpreted-text
role="ref"}

Sets the given marker\'s color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_find_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**track_find_key**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, time: `float<class_float>`{.interpreted-text role="ref"},
find_mode: `FindMode<enum_Animation_FindMode>`{.interpreted-text
role="ref"} = 0, limit: `bool<class_bool>`{.interpreted-text role="ref"}
= false, backward: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_find_key>`{.interpreted-text
role="ref"}

Finds the key index by time in a given track. Optionally, only find it
if the approx/exact time is given.

If `limit` is `true`, it does not return keys outside the animation
range.

If `backward` is `true`, the direction is reversed in methods that rely
on one directional processing.

For example, in case `find_mode` is
`FIND_MODE_NEAREST<class_Animation_constant_FIND_MODE_NEAREST>`{.interpreted-text
role="ref"}, if there is no key in the current position just after
seeked, the first key found is retrieved by searching before the
position, but if `backward` is `true`, the first key found is retrieved
after the position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_interpolation_loop_wrap}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**track_get_interpolation_loop_wrap**(track_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_interpolation_loop_wrap>`{.interpreted-text
role="ref"}

Returns `true` if the track at `track_idx` wraps the interpolation loop.
New tracks wrap the interpolation loop by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_interpolation_type}
::: rst-class
classref-method
:::
::::

`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"} **track_get_interpolation_type**(track_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_interpolation_type>`{.interpreted-text
role="ref"}

Returns the interpolation type of a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_key_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**track_get_key_count**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_key_count>`{.interpreted-text
role="ref"}

Returns the number of keys in a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_key_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**track_get_key_time**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, key_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_key_time>`{.interpreted-text
role="ref"}

Returns the time at which the key is located.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_key_transition}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**track_get_key_transition**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_key_transition>`{.interpreted-text
role="ref"}

Returns the transition curve (easing) for a specific key (see the
built-in math function
`@GlobalScope.ease()<class_@GlobalScope_method_ease>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_key_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**track_get_key_value**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, key_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_key_value>`{.interpreted-text
role="ref"}

Returns the value of a given key in a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**track_get_path**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_path>`{.interpreted-text
role="ref"}

Gets the path of a track. For more information on the path format, see
`track_set_path()<class_Animation_method_track_set_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_get_type}
::: rst-class
classref-method
:::
::::

`TrackType<enum_Animation_TrackType>`{.interpreted-text role="ref"}
**track_get_type**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_get_type>`{.interpreted-text
role="ref"}

Gets the type of a track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_insert_key}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**track_insert_key**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, time: `float<class_float>`{.interpreted-text role="ref"},
key: `Variant<class_Variant>`{.interpreted-text role="ref"}, transition:
`float<class_float>`{.interpreted-text role="ref"} = 1)
`🔗<class_Animation_method_track_insert_key>`{.interpreted-text
role="ref"}

Inserts a generic key in a given track. Returns the key index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_is_compressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**track_is_compressed**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_is_compressed>`{.interpreted-text
role="ref"}

Returns `true` if the track is compressed, `false` otherwise. See also
`compress()<class_Animation_method_compress>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_is_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**track_is_enabled**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_is_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the track at index `track_idx` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_is_imported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**track_is_imported**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_track_is_imported>`{.interpreted-text
role="ref"}

Returns `true` if the given track is imported. Else, return `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_move_down}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_move_down**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Animation_method_track_move_down>`{.interpreted-text
role="ref"}

Moves a track down.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_move_to}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_move_to**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, to_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_move_to>`{.interpreted-text role="ref"}

Changes the index position of track `track_idx` to the one defined in
`to_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_move_up}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_move_up**(track_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Animation_method_track_move_up>`{.interpreted-text role="ref"}

Moves a track up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_remove_key}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_remove_key**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, key_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_remove_key>`{.interpreted-text
role="ref"}

Removes a key by index in a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_remove_key_at_time}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_remove_key_at_time**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_remove_key_at_time>`{.interpreted-text
role="ref"}

Removes a key at `time` in a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_enabled**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_set_enabled>`{.interpreted-text
role="ref"}

Enables/disables the given track. Tracks are enabled by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_imported}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_imported**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, imported: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_set_imported>`{.interpreted-text
role="ref"}

Sets the given track as imported or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_interpolation_loop_wrap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_interpolation_loop_wrap**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, interpolation:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_set_interpolation_loop_wrap>`{.interpreted-text
role="ref"}

If `true`, the track at `track_idx` wraps the interpolation loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_interpolation_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_interpolation_type**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, interpolation:
`InterpolationType<enum_Animation_InterpolationType>`{.interpreted-text
role="ref"})
`🔗<class_Animation_method_track_set_interpolation_type>`{.interpreted-text
role="ref"}

Sets the interpolation type of a given track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_key_time}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_key_time**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, key_idx: `int<class_int>`{.interpreted-text role="ref"},
time: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_set_key_time>`{.interpreted-text
role="ref"}

Sets the time of an existing key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_key_transition}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_key_transition**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, key_idx:
`int<class_int>`{.interpreted-text role="ref"}, transition:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_set_key_transition>`{.interpreted-text
role="ref"}

Sets the transition curve (easing) for a specific key (see the built-in
math function
`@GlobalScope.ease()<class_@GlobalScope_method_ease>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_key_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_key_value**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, key: `int<class_int>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_set_key_value>`{.interpreted-text
role="ref"}

Sets the value of an existing key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_set_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_set_path**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`🔗<class_Animation_method_track_set_path>`{.interpreted-text
role="ref"}

Sets the path of a track. Paths must be valid scene-tree paths to a node
and must be specified starting from the
`AnimationMixer.root_node<class_AnimationMixer_property_root_node>`{.interpreted-text
role="ref"} that will reproduce the animation. Tracks that control
properties or bones must append their name after the path, separated by
`":"`.

For example, `"character/skeleton:ankle"` or
`"character/mesh:transform/local"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_track_swap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**track_swap**(track_idx: `int<class_int>`{.interpreted-text
role="ref"}, with_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_track_swap>`{.interpreted-text role="ref"}

Swaps the track `track_idx`\'s index position with the track `with_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_value_track_get_update_mode}
::: rst-class
classref-method
:::
::::

`UpdateMode<enum_Animation_UpdateMode>`{.interpreted-text role="ref"}
**value_track_get_update_mode**(track_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_value_track_get_update_mode>`{.interpreted-text
role="ref"}

Returns the update mode of a value track.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_value_track_interpolate}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**value_track_interpolate**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, time_sec:
`float<class_float>`{.interpreted-text role="ref"}, backward:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Animation_method_value_track_interpolate>`{.interpreted-text
role="ref"}

Returns the interpolated value at the given time (in seconds). The
`track_idx` must be the index of a value track.

A `backward` mainly affects the direction of key retrieval of the track
with
`UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"} converted by
`AnimationMixer.ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS>`{.interpreted-text
role="ref"} to match the result with
`track_find_key()<class_Animation_method_track_find_key>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Animation_method_value_track_set_update_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**value_track_set_update_mode**(track_idx:
`int<class_int>`{.interpreted-text role="ref"}, mode:
`UpdateMode<enum_Animation_UpdateMode>`{.interpreted-text role="ref"})
`🔗<class_Animation_method_value_track_set_update_mode>`{.interpreted-text
role="ref"}

Sets the update mode of a value track.
