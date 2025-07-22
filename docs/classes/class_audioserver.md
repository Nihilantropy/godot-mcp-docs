github_url
:   hide

# AudioServer {#class_AudioServer}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Server interface for low-level audio access.

::: rst-class
classref-introduction-group
:::

## Description

**AudioServer** is a low-level server interface for audio access. It is
in charge of creating sample data (playable audio) as well as its
playback via a voice interface.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
  role="doc"}
- [Audio Device Changer
  Demo](https://godotengine.org/asset-library/asset/2758)
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

:::: {#class_AudioServer_signal_bus_layout_changed}
::: rst-class
classref-signal
:::
::::

**bus_layout_changed**()
`🔗<class_AudioServer_signal_bus_layout_changed>`{.interpreted-text
role="ref"}

Emitted when an audio bus is added, deleted, or moved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_signal_bus_renamed}
::: rst-class
classref-signal
:::
::::

**bus_renamed**(bus_index: `int<class_int>`{.interpreted-text
role="ref"}, old_name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, new_name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AudioServer_signal_bus_renamed>`{.interpreted-text role="ref"}

Emitted when the audio bus at `bus_index` is renamed from `old_name` to
`new_name`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AudioServer_SpeakerMode}
::: rst-class
classref-enumeration
:::
::::

enum **SpeakerMode**:
`🔗<enum_AudioServer_SpeakerMode>`{.interpreted-text role="ref"}

:::: {#class_AudioServer_constant_SPEAKER_MODE_STEREO}
::: rst-class
classref-enumeration-constant
:::
::::

`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} **SPEAKER_MODE_STEREO** = `0`

Two or fewer speakers were detected.

:::: {#class_AudioServer_constant_SPEAKER_SURROUND_31}
::: rst-class
classref-enumeration-constant
:::
::::

`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} **SPEAKER_SURROUND_31** = `1`

A 3.1 channel surround setup was detected.

:::: {#class_AudioServer_constant_SPEAKER_SURROUND_51}
::: rst-class
classref-enumeration-constant
:::
::::

`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} **SPEAKER_SURROUND_51** = `2`

A 5.1 channel surround setup was detected.

:::: {#class_AudioServer_constant_SPEAKER_SURROUND_71}
::: rst-class
classref-enumeration-constant
:::
::::

`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} **SPEAKER_SURROUND_71** = `3`

A 7.1 channel surround setup was detected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AudioServer_PlaybackType}
::: rst-class
classref-enumeration
:::
::::

enum **PlaybackType**:
`🔗<enum_AudioServer_PlaybackType>`{.interpreted-text role="ref"}

:::: {#class_AudioServer_constant_PLAYBACK_TYPE_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **PLAYBACK_TYPE_DEFAULT** = `0`

**Experimental:** This constant may be changed or removed in future
versions.

The playback will be considered of the type declared at
`ProjectSettings.audio/general/default_playback_type<class_ProjectSettings_property_audio/general/default_playback_type>`{.interpreted-text
role="ref"}.

:::: {#class_AudioServer_constant_PLAYBACK_TYPE_STREAM}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **PLAYBACK_TYPE_STREAM** = `1`

**Experimental:** This constant may be changed or removed in future
versions.

Force the playback to be considered as a stream.

:::: {#class_AudioServer_constant_PLAYBACK_TYPE_SAMPLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **PLAYBACK_TYPE_SAMPLE** = `2`

**Experimental:** This constant may be changed or removed in future
versions.

Force the playback to be considered as a sample. This can provide lower
latency and more stable playback (with less risk of audio crackling), at
the cost of having less flexibility.

\*\*Note:\*\* Only currently supported on the web platform.

\*\*Note:\*\* `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"}s are not supported when playback is considered as a sample.

:::: {#class_AudioServer_constant_PLAYBACK_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} **PLAYBACK_TYPE_MAX** = `3`

**Experimental:** This constant may be changed or removed in future
versions.

Represents the size of the
`PlaybackType<enum_AudioServer_PlaybackType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioServer_property_bus_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bus_count** = `1`
`🔗<class_AudioServer_property_bus_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bus_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bus_count**()

Number of available audio buses.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_property_input_device}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **input_device** =
`"Default"`
`🔗<class_AudioServer_property_input_device>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_input_device**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_input_device**()

Name of the current device for audio input (see
`get_input_device_list()<class_AudioServer_method_get_input_device_list>`{.interpreted-text
role="ref"}). On systems with multiple audio inputs (such as analog, USB
and HDMI audio), this can be used to select the audio input device. The
value `"Default"` will record audio on the system-wide default audio
input. If an invalid device name is set, the value will be reverted back
to `"Default"`.

\*\*Note:\*\*
`ProjectSettings.audio/driver/enable_input<class_ProjectSettings_property_audio/driver/enable_input>`{.interpreted-text
role="ref"} must be `true` for audio input to work. See also that
setting\'s description for caveats related to permissions and operating
system privacy settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_property_output_device}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **output_device** =
`"Default"`
`🔗<class_AudioServer_property_output_device>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_output_device**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_output_device**()

Name of the current device for audio output (see
`get_output_device_list()<class_AudioServer_method_get_output_device_list>`{.interpreted-text
role="ref"}). On systems with multiple audio outputs (such as analog,
USB and HDMI audio), this can be used to select the audio output device.
The value `"Default"` will play audio on the system-wide default audio
output. If an invalid device name is set, the value will be reverted
back to `"Default"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_property_playback_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**playback_speed_scale** = `1.0`
`🔗<class_AudioServer_property_playback_speed_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_playback_speed_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_playback_speed_scale**()

Scales the rate at which audio is played (i.e. setting it to `0.5` will
make the audio be played at half its speed). See also
`Engine.time_scale<class_Engine_property_time_scale>`{.interpreted-text
role="ref"} to affect the general simulation speed, which is independent
from
`playback_speed_scale<class_AudioServer_property_playback_speed_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioServer_method_add_bus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_bus**(at_position: `int<class_int>`{.interpreted-text role="ref"}
= -1) `🔗<class_AudioServer_method_add_bus>`{.interpreted-text
role="ref"}

Adds a bus at `at_position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_add_bus_effect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_bus_effect**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, effect: `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"}, at_position: `int<class_int>`{.interpreted-text role="ref"}
= -1) `🔗<class_AudioServer_method_add_bus_effect>`{.interpreted-text
role="ref"}

Adds an `AudioEffect<class_AudioEffect>`{.interpreted-text role="ref"}
effect to the bus `bus_idx` at `at_position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_generate_bus_layout}
::: rst-class
classref-method
:::
::::

`AudioBusLayout<class_AudioBusLayout>`{.interpreted-text role="ref"}
**generate_bus_layout**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_generate_bus_layout>`{.interpreted-text
role="ref"}

Generates an `AudioBusLayout<class_AudioBusLayout>`{.interpreted-text
role="ref"} using the available buses and effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_channels}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_bus_channels**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_channels>`{.interpreted-text
role="ref"}

Returns the number of channels of the bus at index `bus_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_effect}
::: rst-class
classref-method
:::
::::

`AudioEffect<class_AudioEffect>`{.interpreted-text role="ref"}
**get_bus_effect**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, effect_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_get_bus_effect>`{.interpreted-text
role="ref"}

Returns the `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} at position `effect_idx` in bus `bus_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_effect_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_bus_effect_count**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AudioServer_method_get_bus_effect_count>`{.interpreted-text
role="ref"}

Returns the number of effects on the bus at `bus_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_effect_instance}
::: rst-class
classref-method
:::
::::

`AudioEffectInstance<class_AudioEffectInstance>`{.interpreted-text
role="ref"} **get_bus_effect_instance**(bus_idx:
`int<class_int>`{.interpreted-text role="ref"}, effect_idx:
`int<class_int>`{.interpreted-text role="ref"}, channel:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_AudioServer_method_get_bus_effect_instance>`{.interpreted-text
role="ref"}

Returns the
`AudioEffectInstance<class_AudioEffectInstance>`{.interpreted-text
role="ref"} assigned to the given bus and effect indices (and optionally
channel).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_bus_index**(bus_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_index>`{.interpreted-text
role="ref"}

Returns the index of the bus with the name `bus_name`. Returns `-1` if
no bus with the specified name exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_bus_name**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_name>`{.interpreted-text
role="ref"}

Returns the name of the bus with the index `bus_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_peak_volume_left_db}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_bus_peak_volume_left_db**(bus_idx:
`int<class_int>`{.interpreted-text role="ref"}, channel:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_peak_volume_left_db>`{.interpreted-text
role="ref"}

Returns the peak volume of the left speaker at bus index `bus_idx` and
channel index `channel`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_peak_volume_right_db}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_bus_peak_volume_right_db**(bus_idx:
`int<class_int>`{.interpreted-text role="ref"}, channel:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_peak_volume_right_db>`{.interpreted-text
role="ref"}

Returns the peak volume of the right speaker at bus index `bus_idx` and
channel index `channel`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_send}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_bus_send**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_send>`{.interpreted-text
role="ref"}

Returns the name of the bus that the bus at index `bus_idx` sends to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_volume_db}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_bus_volume_db**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_volume_db>`{.interpreted-text
role="ref"}

Returns the volume of the bus at index `bus_idx` in dB.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_bus_volume_linear}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_bus_volume_linear**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_bus_volume_linear>`{.interpreted-text
role="ref"}

Returns the volume of the bus at index `bus_idx` as a linear value.

\*\*Note:\*\* The returned value is equivalent to the result of
`@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"} on the result of
`get_bus_volume_db()<class_AudioServer_method_get_bus_volume_db>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_driver_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_driver_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_driver_name>`{.interpreted-text
role="ref"}

Returns the name of the current audio driver. The default usually
depends on the operating system, but may be overridden via the
`--audio-driver`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}. `--headless` also automatically sets the audio driver to
`Dummy`. See also
`ProjectSettings.audio/driver/driver<class_ProjectSettings_property_audio/driver/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_input_device_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_input_device_list**()
`🔗<class_AudioServer_method_get_input_device_list>`{.interpreted-text
role="ref"}

Returns the names of all audio input devices detected on the system.

\*\*Note:\*\*
`ProjectSettings.audio/driver/enable_input<class_ProjectSettings_property_audio/driver/enable_input>`{.interpreted-text
role="ref"} must be `true` for audio input to work. See also that
setting\'s description for caveats related to permissions and operating
system privacy settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_input_mix_rate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_input_mix_rate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_input_mix_rate>`{.interpreted-text
role="ref"}

Returns the sample rate at the input of the **AudioServer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_mix_rate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_mix_rate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_mix_rate>`{.interpreted-text
role="ref"}

Returns the sample rate at the output of the **AudioServer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_output_device_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_output_device_list**()
`🔗<class_AudioServer_method_get_output_device_list>`{.interpreted-text
role="ref"}

Returns the names of all audio output devices detected on the system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_output_latency}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_output_latency**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_output_latency>`{.interpreted-text
role="ref"}

Returns the audio driver\'s effective output latency. This is based on
`ProjectSettings.audio/driver/output_latency<class_ProjectSettings_property_audio/driver/output_latency>`{.interpreted-text
role="ref"}, but the exact returned value will differ depending on the
operating system and audio driver.

\*\*Note:\*\* This can be expensive; it is not recommended to call
`get_output_latency()<class_AudioServer_method_get_output_latency>`{.interpreted-text
role="ref"} every frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_speaker_mode}
::: rst-class
classref-method
:::
::::

`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} **get_speaker_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_speaker_mode>`{.interpreted-text
role="ref"}

Returns the speaker configuration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_time_since_last_mix}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_time_since_last_mix**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_time_since_last_mix>`{.interpreted-text
role="ref"}

Returns the relative time since the last mix occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_get_time_to_next_mix}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_time_to_next_mix**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_get_time_to_next_mix>`{.interpreted-text
role="ref"}

Returns the relative time until the next mix occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_is_bus_bypassing_effects}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_bus_bypassing_effects**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_is_bus_bypassing_effects>`{.interpreted-text
role="ref"}

If `true`, the bus at index `bus_idx` is bypassing effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_is_bus_effect_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_bus_effect_enabled**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, effect_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_is_bus_effect_enabled>`{.interpreted-text
role="ref"}

If `true`, the effect at index `effect_idx` on the bus at index
`bus_idx` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_is_bus_mute}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_bus_mute**(bus_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_is_bus_mute>`{.interpreted-text role="ref"}

If `true`, the bus at index `bus_idx` is muted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_is_bus_solo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_bus_solo**(bus_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioServer_method_is_bus_solo>`{.interpreted-text role="ref"}

If `true`, the bus at index `bus_idx` is in solo mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_is_stream_registered_as_sample}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_stream_registered_as_sample**(stream:
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_is_stream_registered_as_sample>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

If `true`, the stream is registered as a sample. The engine will not
have to register it before playing the sample.

If `false`, the stream will have to be registered before playing it. To
prevent lag spikes, register the stream as sample with
`register_stream_as_sample()<class_AudioServer_method_register_stream_as_sample>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_lock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **lock**()
`🔗<class_AudioServer_method_lock>`{.interpreted-text role="ref"}

Locks the audio driver\'s main loop.

\*\*Note:\*\* Remember to unlock it afterwards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_move_bus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_bus**(index: `int<class_int>`{.interpreted-text role="ref"},
to_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_move_bus>`{.interpreted-text role="ref"}

Moves the bus from index `index` to index `to_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_register_stream_as_sample}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_stream_as_sample**(stream:
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_register_stream_as_sample>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Forces the registration of a stream as a sample.

\*\*Note:\*\* Lag spikes may occur when calling this method, especially
on single-threaded builds. It is suggested to call this method while
loading assets, where the lag spike could be masked, instead of
registering the sample right before it needs to be played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_remove_bus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_bus**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_remove_bus>`{.interpreted-text role="ref"}

Removes the bus at index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_remove_bus_effect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_bus_effect**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, effect_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_remove_bus_effect>`{.interpreted-text
role="ref"}

Removes the effect at index `effect_idx` from the bus at index
`bus_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_bypass_effects}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_bypass_effects**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_bus_bypass_effects>`{.interpreted-text
role="ref"}

If `true`, the bus at index `bus_idx` is bypassing effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_effect_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_effect_enabled**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, effect_idx: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_bus_effect_enabled>`{.interpreted-text
role="ref"}

If `true`, the effect at index `effect_idx` on the bus at index
`bus_idx` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_layout}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_layout**(bus_layout:
`AudioBusLayout<class_AudioBusLayout>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_bus_layout>`{.interpreted-text
role="ref"}

Overwrites the currently used
`AudioBusLayout<class_AudioBusLayout>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_mute}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_mute**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_bus_mute>`{.interpreted-text
role="ref"}

If `true`, the bus at index `bus_idx` is muted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_name**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_bus_name>`{.interpreted-text
role="ref"}

Sets the name of the bus at index `bus_idx` to `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_send}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_send**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, send: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_AudioServer_method_set_bus_send>`{.interpreted-text
role="ref"}

Connects the output of the bus at `bus_idx` to the bus named `send`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_solo}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_solo**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_bus_solo>`{.interpreted-text
role="ref"}

If `true`, the bus at index `bus_idx` is in solo mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_volume_db}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_volume_db**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, volume_db: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioServer_method_set_bus_volume_db>`{.interpreted-text
role="ref"}

Sets the volume in decibels of the bus at index `bus_idx` to
`volume_db`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_bus_volume_linear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bus_volume_linear**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, volume_linear: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AudioServer_method_set_bus_volume_linear>`{.interpreted-text
role="ref"}

Sets the volume as a linear value of the bus at index `bus_idx` to
`volume_linear`.

\*\*Note:\*\* Using this method is equivalent to calling
`set_bus_volume_db()<class_AudioServer_method_set_bus_volume_db>`{.interpreted-text
role="ref"} with the result of
`@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>`{.interpreted-text
role="ref"} on a value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_set_enable_tagging_used_audio_streams}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_enable_tagging_used_audio_streams**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_set_enable_tagging_used_audio_streams>`{.interpreted-text
role="ref"}

If set to `true`, all instances of
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} will call
`AudioStreamPlayback._tag_used_streams()<class_AudioStreamPlayback_private_method__tag_used_streams>`{.interpreted-text
role="ref"} every mix step.

\*\*Note:\*\* This is enabled by default in the editor, as it is used by
editor plugins for the audio stream previews.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_swap_bus_effects}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**swap_bus_effects**(bus_idx: `int<class_int>`{.interpreted-text
role="ref"}, effect_idx: `int<class_int>`{.interpreted-text role="ref"},
by_effect_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioServer_method_swap_bus_effects>`{.interpreted-text
role="ref"}

Swaps the position of two effects in bus `bus_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioServer_method_unlock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **unlock**()
`🔗<class_AudioServer_method_unlock>`{.interpreted-text role="ref"}

Unlocks the audio driver\'s main loop. (After locking it, you should
always unlock it.)
