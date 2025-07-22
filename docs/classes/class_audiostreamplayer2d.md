github_url
:   hide

::: {.meta keywords="sound, sfx"}
:::

# AudioStreamPlayer2D {#class_AudioStreamPlayer2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Plays positional sound in 2D space.

::: rst-class
classref-introduction-group
:::

## Description

Plays audio that is attenuated with distance to the listener.

By default, audio is heard from the screen center. This can be changed
by adding an `AudioListener2D<class_AudioListener2D>`{.interpreted-text
role="ref"} node to the scene and enabling it by calling
`AudioListener2D.make_current()<class_AudioListener2D_method_make_current>`{.interpreted-text
role="ref"} on it.

See also `AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"} to play a sound non-positionally.

\*\*Note:\*\* Hiding an **AudioStreamPlayer2D** node does not disable
its audio output. To temporarily disable an **AudioStreamPlayer2D**\'s
audio output, set
`volume_db<class_AudioStreamPlayer2D_property_volume_db>`{.interpreted-text
role="ref"} to a very low value like `-100` (which isn\'t audible to
human hearing).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer2D_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_AudioStreamPlayer2D_signal_finished>`{.interpreted-text
role="ref"}

Emitted when the audio stops playing.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamPlayer2D_property_area_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **area_mask** = `1`
`🔗<class_AudioStreamPlayer2D_property_area_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_area_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_area_mask**()

Determines which `Area2D<class_Area2D>`{.interpreted-text role="ref"}
layers affect the sound for reverb and audio bus effects. Areas can be
used to redirect `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"}s so that they play in a certain audio bus. An example of how
you might use this is making a \"water\" area so that sounds played in
the water are redirected through an audio bus to make them sound like
they are being played underwater.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_attenuation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **attenuation** =
`1.0`
`🔗<class_AudioStreamPlayer2D_property_attenuation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attenuation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_attenuation**()

The volume is attenuated over distance with this as an exponent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_autoplay}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autoplay** = `false`
`🔗<class_AudioStreamPlayer2D_property_autoplay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoplay**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_autoplay_enabled**()

If `true`, audio plays when added to scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_bus}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **bus** =
`&"Master"`
`🔗<class_AudioStreamPlayer2D_property_bus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bus**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_bus**()

Bus on which this audio is playing.

\*\*Note:\*\* When setting this property, keep in mind that no
validation is performed to see if the given name matches an existing
bus. This is because audio bus layouts might be loaded after this
property is set. If this given name can\'t be resolved at runtime, it
will fall back to `"Master"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_distance** =
`2000.0`
`🔗<class_AudioStreamPlayer2D_property_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_max_distance**()

Maximum distance from which audio is still hearable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_max_polyphony}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_polyphony** = `1`
`🔗<class_AudioStreamPlayer2D_property_max_polyphony>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_polyphony**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_polyphony**()

The maximum number of sounds this node can play at the same time.
Playing additional sounds after this value is reached will cut off the
oldest sounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_panning_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **panning_strength**
= `1.0`
`🔗<class_AudioStreamPlayer2D_property_panning_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_panning_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_panning_strength**()

Scales the panning strength for this node by multiplying the base
`ProjectSettings.audio/general/2d_panning_strength<class_ProjectSettings_property_audio/general/2d_panning_strength>`{.interpreted-text
role="ref"} with this factor. Higher values will pan audio from left to
right more dramatically than lower values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_pitch_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pitch_scale** =
`1.0`
`🔗<class_AudioStreamPlayer2D_property_pitch_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pitch_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pitch_scale**()

The pitch and the tempo of the audio, as a multiplier of the audio
sample\'s sample rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_playback_type}
::: rst-class
classref-property
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **playback_type** = `0`
`🔗<class_AudioStreamPlayer2D_property_playback_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_playback_type**(value:
  `PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
  role="ref"})
- `PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
  role="ref"} **get_playback_type**()

**Experimental:** This property may be changed or removed in future
versions.

The playback type of the stream player. If set other than to the default
value, it will force that playback type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_playing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **playing** = `false`
`🔗<class_AudioStreamPlayer2D_property_playing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_playing**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()

If `true`, audio is playing or is queued to be played (see
`play()<class_AudioStreamPlayer2D_method_play>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_stream}
::: rst-class
classref-property
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**stream**
`🔗<class_AudioStreamPlayer2D_property_stream>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream**(value:
  `AudioStream<class_AudioStream>`{.interpreted-text role="ref"})
- `AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
  **get_stream**()

The `AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
object to be played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_stream_paused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **stream_paused** =
`false`
`🔗<class_AudioStreamPlayer2D_property_stream_paused>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream_paused**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_stream_paused**()

If `true`, the playback is paused. You can resume it by setting
`stream_paused<class_AudioStreamPlayer2D_property_stream_paused>`{.interpreted-text
role="ref"} to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_volume_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_db** = `0.0`
`🔗<class_AudioStreamPlayer2D_property_volume_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_volume_db**()

Base volume before attenuation, in decibels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_property_volume_linear}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_linear**
`🔗<class_AudioStreamPlayer2D_property_volume_linear>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_linear**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volume_linear**()

Base volume before attenuation, as a linear value.

\*\*Note:\*\* This member modifies
`volume_db<class_AudioStreamPlayer2D_property_volume_db>`{.interpreted-text
role="ref"} for convenience. The returned value is equivalent to the
result of
`@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"} on
`volume_db<class_AudioStreamPlayer2D_property_volume_db>`{.interpreted-text
role="ref"}. Setting this member is equivalent to setting
`volume_db<class_AudioStreamPlayer2D_property_volume_db>`{.interpreted-text
role="ref"} to the result of
`@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>`{.interpreted-text
role="ref"} on a value.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamPlayer2D_method_get_playback_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_playback_position**()
`🔗<class_AudioStreamPlayer2D_method_get_playback_position>`{.interpreted-text
role="ref"}

Returns the position in the
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_method_get_stream_playback}
::: rst-class
classref-method
:::
::::

`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **get_stream_playback**()
`🔗<class_AudioStreamPlayer2D_method_get_stream_playback>`{.interpreted-text
role="ref"}

Returns the
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} object associated with this **AudioStreamPlayer2D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_method_has_stream_playback}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_stream_playback**()
`🔗<class_AudioStreamPlayer2D_method_has_stream_playback>`{.interpreted-text
role="ref"}

Returns whether the
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"} can return the
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} object or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play**(from_position: `float<class_float>`{.interpreted-text
role="ref"} = 0.0)
`🔗<class_AudioStreamPlayer2D_method_play>`{.interpreted-text
role="ref"}

Queues the audio to play on the next physics frame, from the given
position `from_position`, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_method_seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek**(to_position: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamPlayer2D_method_seek>`{.interpreted-text
role="ref"}

Sets the position from which audio will be played, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer2D_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_AudioStreamPlayer2D_method_stop>`{.interpreted-text
role="ref"}

Stops the audio.
