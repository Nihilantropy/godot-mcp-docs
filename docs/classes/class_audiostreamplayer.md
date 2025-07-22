github_url
:   hide

::: {.meta keywords="sound, music, song"}
:::

# AudioStreamPlayer {#class_AudioStreamPlayer}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node for audio playback.

::: rst-class
classref-introduction-group
:::

## Description

The **AudioStreamPlayer** node plays an audio stream non-positionally.
It is ideal for user interfaces, menus, or background music.

To use this node,
`stream<class_AudioStreamPlayer_property_stream>`{.interpreted-text
role="ref"} needs to be set to a valid
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"} resource.
Playing more than one sound at the same time is also supported, see
`max_polyphony<class_AudioStreamPlayer_property_max_polyphony>`{.interpreted-text
role="ref"}.

If you need to play audio at a specific position, use
`AudioStreamPlayer2D<class_AudioStreamPlayer2D>`{.interpreted-text
role="ref"} or
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`{.interpreted-text
  role="doc"}
- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)
- [Audio Device Changer
  Demo](https://godotengine.org/asset-library/asset/2758)
- [Audio Generator
  Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record
  Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer
  Demo](https://godotengine.org/asset-library/asset/2762)

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

:::: {#class_AudioStreamPlayer_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_AudioStreamPlayer_signal_finished>`{.interpreted-text
role="ref"}

Emitted when a sound finishes playing without interruptions. This signal
is *not* emitted when calling
`stop()<class_AudioStreamPlayer_method_stop>`{.interpreted-text
role="ref"}, or when exiting the tree while sounds are playing.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AudioStreamPlayer_MixTarget}
::: rst-class
classref-enumeration
:::
::::

enum **MixTarget**:
`🔗<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text role="ref"}

:::: {#class_AudioStreamPlayer_constant_MIX_TARGET_STEREO}
::: rst-class
classref-enumeration-constant
:::
::::

`MixTarget<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text
role="ref"} **MIX_TARGET_STEREO** = `0`

The audio will be played only on the first channel. This is the default.

:::: {#class_AudioStreamPlayer_constant_MIX_TARGET_SURROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`MixTarget<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text
role="ref"} **MIX_TARGET_SURROUND** = `1`

The audio will be played on all surround channels.

:::: {#class_AudioStreamPlayer_constant_MIX_TARGET_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`MixTarget<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text
role="ref"} **MIX_TARGET_CENTER** = `2`

The audio will be played on the second channel, which is usually the
center.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamPlayer_property_autoplay}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autoplay** = `false`
`🔗<class_AudioStreamPlayer_property_autoplay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoplay**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_autoplay_enabled**()

If `true`, this node calls
`play()<class_AudioStreamPlayer_method_play>`{.interpreted-text
role="ref"} when entering the tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_bus}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **bus** =
`&"Master"` `🔗<class_AudioStreamPlayer_property_bus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bus**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_bus**()

The target bus name. All sounds from this node will be playing on this
bus.

\*\*Note:\*\* At runtime, if no bus with the given name exists, all
sounds will fall back on `"Master"`. See also
`AudioServer.get_bus_name()<class_AudioServer_method_get_bus_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_max_polyphony}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_polyphony** = `1`
`🔗<class_AudioStreamPlayer_property_max_polyphony>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_polyphony**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_polyphony**()

The maximum number of sounds this node can play at the same time.
Calling `play()<class_AudioStreamPlayer_method_play>`{.interpreted-text
role="ref"} after this value is reached will cut off the oldest sounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_mix_target}
::: rst-class
classref-property
:::
::::

`MixTarget<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text
role="ref"} **mix_target** = `0`
`🔗<class_AudioStreamPlayer_property_mix_target>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mix_target**(value:
  `MixTarget<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text
  role="ref"})
- `MixTarget<enum_AudioStreamPlayer_MixTarget>`{.interpreted-text
  role="ref"} **get_mix_target**()

The mix target channels. Has no effect when two speakers or less are
detected (see
`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_pitch_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pitch_scale** =
`1.0`
`🔗<class_AudioStreamPlayer_property_pitch_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pitch_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pitch_scale**()

The audio\'s pitch and tempo, as a multiplier of the
`stream<class_AudioStreamPlayer_property_stream>`{.interpreted-text
role="ref"}\'s sample rate. A value of `2.0` doubles the audio\'s pitch,
while a value of `0.5` halves the pitch.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_playback_type}
::: rst-class
classref-property
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **playback_type** = `0`
`🔗<class_AudioStreamPlayer_property_playback_type>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer_property_playing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **playing** = `false`
`🔗<class_AudioStreamPlayer_property_playing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_playing**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()

If `true`, this node is playing sounds. Setting this property has the
same effect as
`play()<class_AudioStreamPlayer_method_play>`{.interpreted-text
role="ref"} and
`stop()<class_AudioStreamPlayer_method_stop>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_stream}
::: rst-class
classref-property
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**stream**
`🔗<class_AudioStreamPlayer_property_stream>`{.interpreted-text
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
resource to be played. Setting this property stops all currently playing
sounds. If left empty, the **AudioStreamPlayer** does not work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_stream_paused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **stream_paused** =
`false`
`🔗<class_AudioStreamPlayer_property_stream_paused>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream_paused**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_stream_paused**()

If `true`, the sounds are paused. Setting
`stream_paused<class_AudioStreamPlayer_property_stream_paused>`{.interpreted-text
role="ref"} to `false` resumes all sounds.

\*\*Note:\*\* This property is automatically changed when exiting or
entering the tree, or this node is paused (see
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_volume_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_db** = `0.0`
`🔗<class_AudioStreamPlayer_property_volume_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_volume_db**()

Volume of sound, in decibels. This is an offset of the
`stream<class_AudioStreamPlayer_property_stream>`{.interpreted-text
role="ref"}\'s volume.

\*\*Note:\*\* To convert between decibel and linear energy (like most
volume sliders do), use
`volume_linear<class_AudioStreamPlayer_property_volume_linear>`{.interpreted-text
role="ref"}, or
`@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"} and
`@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_property_volume_linear}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_linear**
`🔗<class_AudioStreamPlayer_property_volume_linear>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_linear**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volume_linear**()

Volume of sound, as a linear value.

\*\*Note:\*\* This member modifies
`volume_db<class_AudioStreamPlayer_property_volume_db>`{.interpreted-text
role="ref"} for convenience. The returned value is equivalent to the
result of
`@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"} on
`volume_db<class_AudioStreamPlayer_property_volume_db>`{.interpreted-text
role="ref"}. Setting this member is equivalent to setting
`volume_db<class_AudioStreamPlayer_property_volume_db>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer_method_get_playback_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_playback_position**()
`🔗<class_AudioStreamPlayer_method_get_playback_position>`{.interpreted-text
role="ref"}

Returns the position in the
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"} of the
latest sound, in seconds. Returns `0.0` if no sounds are playing.

\*\*Note:\*\* The position is not always accurate, as the
`AudioServer<class_AudioServer>`{.interpreted-text role="ref"} does not
mix audio every processed frame. To get more accurate results, add
`AudioServer.get_time_since_last_mix()<class_AudioServer_method_get_time_since_last_mix>`{.interpreted-text
role="ref"} to the returned position.

\*\*Note:\*\* This method always returns `0.0` if the
`stream<class_AudioStreamPlayer_property_stream>`{.interpreted-text
role="ref"} is an
`AudioStreamInteractive<class_AudioStreamInteractive>`{.interpreted-text
role="ref"}, since it can have multiple clips playing at once.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_method_get_stream_playback}
::: rst-class
classref-method
:::
::::

`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **get_stream_playback**()
`🔗<class_AudioStreamPlayer_method_get_stream_playback>`{.interpreted-text
role="ref"}

Returns the latest
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} of this node, usually the most recently created by
`play()<class_AudioStreamPlayer_method_play>`{.interpreted-text
role="ref"}. If no sounds are playing, this method fails and returns an
empty playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_method_has_stream_playback}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_stream_playback**()
`🔗<class_AudioStreamPlayer_method_has_stream_playback>`{.interpreted-text
role="ref"}

Returns `true` if any sound is active, even if
`stream_paused<class_AudioStreamPlayer_property_stream_paused>`{.interpreted-text
role="ref"} is set to `true`. See also
`playing<class_AudioStreamPlayer_property_playing>`{.interpreted-text
role="ref"} and
`get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play**(from_position: `float<class_float>`{.interpreted-text
role="ref"} = 0.0)
`🔗<class_AudioStreamPlayer_method_play>`{.interpreted-text role="ref"}

Plays a sound from the beginning, or the given `from_position` in
seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_method_seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek**(to_position: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_AudioStreamPlayer_method_seek>`{.interpreted-text
role="ref"}

Restarts all sounds to be played from the given `to_position`, in
seconds. Does nothing if no sounds are playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_AudioStreamPlayer_method_stop>`{.interpreted-text role="ref"}

Stops all sounds from this node.
