github_url
:   hide

::: {.meta keywords="sound, sfx"}
:::

# AudioStreamPlayer3D {#class_AudioStreamPlayer3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Plays positional sound in 3D space.

::: rst-class
classref-introduction-group
:::

## Description

Plays audio with positional sound effects, based on the relative
position of the audio listener. Positional effects include distance
attenuation, directionality, and the Doppler effect. For greater
realism, a low-pass filter is applied to distant sounds. This can be
disabled by setting
`attenuation_filter_cutoff_hz<class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz>`{.interpreted-text
role="ref"} to `20500`.

By default, audio is heard from the camera position. This can be changed
by adding an `AudioListener3D<class_AudioListener3D>`{.interpreted-text
role="ref"} node to the scene and enabling it by calling
`AudioListener3D.make_current()<class_AudioListener3D_method_make_current>`{.interpreted-text
role="ref"} on it.

See also `AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"} to play a sound non-positionally.

\*\*Note:\*\* Hiding an **AudioStreamPlayer3D** node does not disable
its audio output. To temporarily disable an **AudioStreamPlayer3D**\'s
audio output, set
`volume_db<class_AudioStreamPlayer3D_property_volume_db>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer3D_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_AudioStreamPlayer3D_signal_finished>`{.interpreted-text
role="ref"}

Emitted when the audio stops playing.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AudioStreamPlayer3D_AttenuationModel}
::: rst-class
classref-enumeration
:::
::::

enum **AttenuationModel**:
`🔗<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamPlayer3D_constant_ATTENUATION_INVERSE_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
role="ref"} **ATTENUATION_INVERSE_DISTANCE** = `0`

Attenuation of loudness according to linear distance.

:::: {#class_AudioStreamPlayer3D_constant_ATTENUATION_INVERSE_SQUARE_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
role="ref"} **ATTENUATION_INVERSE_SQUARE_DISTANCE** = `1`

Attenuation of loudness according to squared distance.

:::: {#class_AudioStreamPlayer3D_constant_ATTENUATION_LOGARITHMIC}
::: rst-class
classref-enumeration-constant
:::
::::

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
role="ref"} **ATTENUATION_LOGARITHMIC** = `2`

Attenuation of loudness according to logarithmic distance.

:::: {#class_AudioStreamPlayer3D_constant_ATTENUATION_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
role="ref"} **ATTENUATION_DISABLED** = `3`

No attenuation of loudness according to distance. The sound will still
be heard positionally, unlike an
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"}.
`ATTENUATION_DISABLED<class_AudioStreamPlayer3D_constant_ATTENUATION_DISABLED>`{.interpreted-text
role="ref"} can be combined with a
`max_distance<class_AudioStreamPlayer3D_property_max_distance>`{.interpreted-text
role="ref"} value greater than `0.0` to achieve linear attenuation
clamped to a sphere of a defined size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AudioStreamPlayer3D_DopplerTracking}
::: rst-class
classref-enumeration
:::
::::

enum **DopplerTracking**:
`🔗<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
role="ref"} **DOPPLER_TRACKING_DISABLED** = `0`

Disables doppler tracking.

:::: {#class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_IDLE_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
role="ref"} **DOPPLER_TRACKING_IDLE_STEP** = `1`

Executes doppler tracking during process frames (see
`Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_PHYSICS_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
role="ref"} **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Executes doppler tracking during physics frames (see
`Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamPlayer3D_property_area_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **area_mask** = `1`
`🔗<class_AudioStreamPlayer3D_property_area_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_area_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_area_mask**()

Determines which `Area3D<class_Area3D>`{.interpreted-text role="ref"}
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

:::: {#class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**attenuation_filter_cutoff_hz** = `5000.0`
`🔗<class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attenuation_filter_cutoff_hz**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_attenuation_filter_cutoff_hz**()

The cutoff frequency of the attenuation low-pass filter, in Hz. A sound
above this frequency is attenuated more than a sound below this
frequency. To disable this effect, set this to `20500` as this frequency
is above the human hearing limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_attenuation_filter_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**attenuation_filter_db** = `-24.0`
`🔗<class_AudioStreamPlayer3D_property_attenuation_filter_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attenuation_filter_db**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_attenuation_filter_db**()

Amount how much the filter affects the loudness, in decibels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_attenuation_model}
::: rst-class
classref-property
:::
::::

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
role="ref"} **attenuation_model** = `0`
`🔗<class_AudioStreamPlayer3D_property_attenuation_model>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attenuation_model**(value:
  `AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
  role="ref"})
- `AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`{.interpreted-text
  role="ref"} **get_attenuation_model**()

Decides if audio should get quieter with distance linearly,
quadratically, logarithmically, or not be affected by distance,
effectively disabling attenuation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_autoplay}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autoplay** = `false`
`🔗<class_AudioStreamPlayer3D_property_autoplay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoplay**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_autoplay_enabled**()

If `true`, audio plays when the AudioStreamPlayer3D node is added to
scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_bus}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **bus** =
`&"Master"`
`🔗<class_AudioStreamPlayer3D_property_bus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bus**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_bus**()

The bus on which this audio is playing.

\*\*Note:\*\* When setting this property, keep in mind that no
validation is performed to see if the given name matches an existing
bus. This is because audio bus layouts might be loaded after this
property is set. If this given name can\'t be resolved at runtime, it
will fall back to `"Master"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_doppler_tracking}
::: rst-class
classref-property
:::
::::

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
role="ref"} **doppler_tracking** = `0`
`🔗<class_AudioStreamPlayer3D_property_doppler_tracking>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_doppler_tracking**(value:
  `DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
  role="ref"})
- `DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`{.interpreted-text
  role="ref"} **get_doppler_tracking**()

Decides in which step the Doppler effect should be calculated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_emission_angle_degrees}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_angle_degrees** = `45.0`
`🔗<class_AudioStreamPlayer3D_property_emission_angle_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_angle**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_angle**()

The angle in which the audio reaches a listener unattenuated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_emission_angle_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**emission_angle_enabled** = `false`
`🔗<class_AudioStreamPlayer3D_property_emission_angle_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_angle_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_emission_angle_enabled**()

If `true`, the audio should be attenuated according to the direction of
the sound.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_emission_angle_filter_attenuation_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_angle_filter_attenuation_db** = `-12.0`
`🔗<class_AudioStreamPlayer3D_property_emission_angle_filter_attenuation_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_angle_filter_attenuation_db**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_angle_filter_attenuation_db**()

Attenuation factor used if listener is outside of
`emission_angle_degrees<class_AudioStreamPlayer3D_property_emission_angle_degrees>`{.interpreted-text
role="ref"} and
`emission_angle_enabled<class_AudioStreamPlayer3D_property_emission_angle_enabled>`{.interpreted-text
role="ref"} is set, in decibels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_max_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_db** = `3.0`
`🔗<class_AudioStreamPlayer3D_property_max_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max_db**()

Sets the absolute maximum of the sound level, in decibels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_distance** =
`0.0`
`🔗<class_AudioStreamPlayer3D_property_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_max_distance**()

The distance past which the sound can no longer be heard at all. Only
has an effect if set to a value greater than `0.0`.
`max_distance<class_AudioStreamPlayer3D_property_max_distance>`{.interpreted-text
role="ref"} works in tandem with
`unit_size<class_AudioStreamPlayer3D_property_unit_size>`{.interpreted-text
role="ref"}. However, unlike
`unit_size<class_AudioStreamPlayer3D_property_unit_size>`{.interpreted-text
role="ref"} whose behavior depends on the
`attenuation_model<class_AudioStreamPlayer3D_property_attenuation_model>`{.interpreted-text
role="ref"},
`max_distance<class_AudioStreamPlayer3D_property_max_distance>`{.interpreted-text
role="ref"} always works in a linear fashion. This can be used to
prevent the **AudioStreamPlayer3D** from requiring audio mixing when the
listener is far away, which saves CPU resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_max_polyphony}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_polyphony** = `1`
`🔗<class_AudioStreamPlayer3D_property_max_polyphony>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer3D_property_panning_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **panning_strength**
= `1.0`
`🔗<class_AudioStreamPlayer3D_property_panning_strength>`{.interpreted-text
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
`ProjectSettings.audio/general/3d_panning_strength<class_ProjectSettings_property_audio/general/3d_panning_strength>`{.interpreted-text
role="ref"} by this factor. If the product is `0.0` then stereo panning
is disabled and the volume is the same for all channels. If the product
is `1.0` then one of the channels will be muted when the sound is
located exactly to the left (or right) of the listener.

Two speaker stereo arrangements implement the [WebAudio standard for
StereoPannerNode
Panning](https://webaudio.github.io/web-audio-api/#stereopanner-algorithm)
where the volume is cosine of half the azimuth angle to the ear.

For other speaker arrangements such as the 5.1 and 7.1 the SPCAP
(Speaker-Placement Correction Amplitude) algorithm is implemented.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_pitch_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pitch_scale** =
`1.0`
`🔗<class_AudioStreamPlayer3D_property_pitch_scale>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer3D_property_playback_type}
::: rst-class
classref-property
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **playback_type** = `0`
`🔗<class_AudioStreamPlayer3D_property_playback_type>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer3D_property_playing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **playing** = `false`
`🔗<class_AudioStreamPlayer3D_property_playing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_playing**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()

If `true`, audio is playing or is queued to be played (see
`play()<class_AudioStreamPlayer3D_method_play>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_stream}
::: rst-class
classref-property
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**stream**
`🔗<class_AudioStreamPlayer3D_property_stream>`{.interpreted-text
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
resource to be played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_stream_paused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **stream_paused** =
`false`
`🔗<class_AudioStreamPlayer3D_property_stream_paused>`{.interpreted-text
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
`stream_paused<class_AudioStreamPlayer3D_property_stream_paused>`{.interpreted-text
role="ref"} to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_unit_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **unit_size** =
`10.0`
`🔗<class_AudioStreamPlayer3D_property_unit_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_unit_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_unit_size**()

The factor for the attenuation effect. Higher values make the sound
audible over a larger distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_volume_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_db** = `0.0`
`🔗<class_AudioStreamPlayer3D_property_volume_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_volume_db**()

The base sound level before attenuation, in decibels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_property_volume_linear}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_linear**
`🔗<class_AudioStreamPlayer3D_property_volume_linear>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_linear**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_volume_linear**()

The base sound level before attenuation, as a linear value.

\*\*Note:\*\* This member modifies
`volume_db<class_AudioStreamPlayer3D_property_volume_db>`{.interpreted-text
role="ref"} for convenience. The returned value is equivalent to the
result of
`@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"} on
`volume_db<class_AudioStreamPlayer3D_property_volume_db>`{.interpreted-text
role="ref"}. Setting this member is equivalent to setting
`volume_db<class_AudioStreamPlayer3D_property_volume_db>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer3D_method_get_playback_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_playback_position**()
`🔗<class_AudioStreamPlayer3D_method_get_playback_position>`{.interpreted-text
role="ref"}

Returns the position in the
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_method_get_stream_playback}
::: rst-class
classref-method
:::
::::

`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **get_stream_playback**()
`🔗<class_AudioStreamPlayer3D_method_get_stream_playback>`{.interpreted-text
role="ref"}

Returns the
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} object associated with this **AudioStreamPlayer3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_method_has_stream_playback}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_stream_playback**()
`🔗<class_AudioStreamPlayer3D_method_has_stream_playback>`{.interpreted-text
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

:::: {#class_AudioStreamPlayer3D_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play**(from_position: `float<class_float>`{.interpreted-text
role="ref"} = 0.0)
`🔗<class_AudioStreamPlayer3D_method_play>`{.interpreted-text
role="ref"}

Queues the audio to play on the next physics frame, from the given
position `from_position`, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_method_seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek**(to_position: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamPlayer3D_method_seek>`{.interpreted-text
role="ref"}

Sets the position from which audio will be played, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayer3D_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_AudioStreamPlayer3D_method_stop>`{.interpreted-text
role="ref"}

Stops the audio.
