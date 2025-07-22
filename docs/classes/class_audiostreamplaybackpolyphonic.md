github_url
:   hide

# AudioStreamPlaybackPolyphonic {#class_AudioStreamPlaybackPolyphonic}

**Inherits:**
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Playback instance for
`AudioStreamPolyphonic<class_AudioStreamPolyphonic>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Playback instance for
`AudioStreamPolyphonic<class_AudioStreamPolyphonic>`{.interpreted-text
role="ref"}. After setting the `stream` property of
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"},
`AudioStreamPlayer2D<class_AudioStreamPlayer2D>`{.interpreted-text
role="ref"}, or
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"}, the playback instance can be obtained by calling
`AudioStreamPlayer.get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>`{.interpreted-text
role="ref"},
`AudioStreamPlayer2D.get_stream_playback()<class_AudioStreamPlayer2D_method_get_stream_playback>`{.interpreted-text
role="ref"} or
`AudioStreamPlayer3D.get_stream_playback()<class_AudioStreamPlayer3D_method_get_stream_playback>`{.interpreted-text
role="ref"} methods.

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

## Constants

:::: {#class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID}
::: rst-class
classref-constant
:::
::::

**INVALID_ID** = `-1`
`🔗<class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID>`{.interpreted-text
role="ref"}

Returned by
`play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`{.interpreted-text
role="ref"} in case it could not allocate a stream for playback.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamPlaybackPolyphonic_method_is_stream_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_stream_playing**(stream: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlaybackPolyphonic_method_is_stream_playing>`{.interpreted-text
role="ref"}

Returns `true` if the stream associated with the given integer ID is
still playing. Check
`play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`{.interpreted-text
role="ref"} for information on when this ID becomes invalid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaybackPolyphonic_method_play_stream}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **play_stream**(stream:
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"},
from_offset: `float<class_float>`{.interpreted-text role="ref"} = 0,
volume_db: `float<class_float>`{.interpreted-text role="ref"} = 0,
pitch_scale: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
playback_type:
`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} = 0, bus: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"Master\")
`🔗<class_AudioStreamPlaybackPolyphonic_method_play_stream>`{.interpreted-text
role="ref"}

Play an `AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
at a given offset, volume, pitch scale, playback type, and bus. Playback
starts immediately.

The return value is a unique integer ID that is associated to this
playback stream and which can be used to control it.

This ID becomes invalid when the stream ends (if it does not loop), when
the **AudioStreamPlaybackPolyphonic** is stopped, or when
`stop_stream()<class_AudioStreamPlaybackPolyphonic_method_stop_stream>`{.interpreted-text
role="ref"} is called.

This function returns
`INVALID_ID<class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID>`{.interpreted-text
role="ref"} if the amount of streams currently playing equals
`AudioStreamPolyphonic.polyphony<class_AudioStreamPolyphonic_property_polyphony>`{.interpreted-text
role="ref"}. If you need a higher amount of maximum polyphony, raise
this value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaybackPolyphonic_method_set_stream_pitch_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stream_pitch_scale**(stream: `int<class_int>`{.interpreted-text
role="ref"}, pitch_scale: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamPlaybackPolyphonic_method_set_stream_pitch_scale>`{.interpreted-text
role="ref"}

Change the stream pitch scale. The `stream` argument is an integer ID
returned by
`play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaybackPolyphonic_method_set_stream_volume}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stream_volume**(stream: `int<class_int>`{.interpreted-text
role="ref"}, volume_db: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamPlaybackPolyphonic_method_set_stream_volume>`{.interpreted-text
role="ref"}

Change the stream volume (in db). The `stream` argument is an integer ID
returned by
`play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaybackPolyphonic_method_stop_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**stop_stream**(stream: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamPlaybackPolyphonic_method_stop_stream>`{.interpreted-text
role="ref"}

Stop a stream. The `stream` argument is an integer ID returned by
`play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`{.interpreted-text
role="ref"}, which becomes invalid after calling this function.
