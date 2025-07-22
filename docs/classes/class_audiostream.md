github_url
:   hide

# AudioStream {#class_AudioStream}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioStreamGenerator<class_AudioStreamGenerator>`{.interpreted-text
role="ref"},
`AudioStreamInteractive<class_AudioStreamInteractive>`{.interpreted-text
role="ref"},
`AudioStreamMicrophone<class_AudioStreamMicrophone>`{.interpreted-text
role="ref"}, `AudioStreamMP3<class_AudioStreamMP3>`{.interpreted-text
role="ref"},
`AudioStreamOggVorbis<class_AudioStreamOggVorbis>`{.interpreted-text
role="ref"},
`AudioStreamPlaylist<class_AudioStreamPlaylist>`{.interpreted-text
role="ref"},
`AudioStreamPolyphonic<class_AudioStreamPolyphonic>`{.interpreted-text
role="ref"},
`AudioStreamRandomizer<class_AudioStreamRandomizer>`{.interpreted-text
role="ref"},
`AudioStreamSynchronized<class_AudioStreamSynchronized>`{.interpreted-text
role="ref"}, `AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text
role="ref"}

Base class for audio streams.

::: rst-class
classref-introduction-group
:::

## Description

Base class for audio streams. Audio streams are used for sound effects
and music playback, and support WAV (via
`AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text role="ref"})
and Ogg (via
`AudioStreamOggVorbis<class_AudioStreamOggVorbis>`{.interpreted-text
role="ref"}) file formats.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`{.interpreted-text
  role="doc"}
- [Audio Generator
  Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record
  Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer
  Demo](https://godotengine.org/asset-library/asset/2762)

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

:::: {#class_AudioStream_signal_parameter_list_changed}
::: rst-class
classref-signal
:::
::::

**parameter_list_changed**()
`🔗<class_AudioStream_signal_parameter_list_changed>`{.interpreted-text
role="ref"}

Signal to be emitted to notify when the parameter list changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStream_private_method__get_bar_beats}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_bar_beats**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_bar_beats>`{.interpreted-text
role="ref"}

Override this method to return the bar beats of this stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__get_beat_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_beat_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_beat_count>`{.interpreted-text
role="ref"}

Overridable method. Should return the total number of beats of this
audio stream. Used by the engine to determine the position of every
beat.

Ideally, the returned value should be based off the stream\'s sample
rate
(`AudioStreamWAV.mix_rate<class_AudioStreamWAV_property_mix_rate>`{.interpreted-text
role="ref"}, for example).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__get_bpm}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **\_get_bpm**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_bpm>`{.interpreted-text
role="ref"}

Overridable method. Should return the tempo of this audio stream, in
beats per minute (BPM). Used by the engine to determine the position of
every beat.

Ideally, the returned value should be based off the stream\'s sample
rate
(`AudioStreamWAV.mix_rate<class_AudioStreamWAV_property_mix_rate>`{.interpreted-text
role="ref"}, for example).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__get_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **\_get_length**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_length>`{.interpreted-text
role="ref"}

Override this method to customize the returned value of
`get_length()<class_AudioStream_method_get_length>`{.interpreted-text
role="ref"}. Should return the length of this audio stream, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__get_parameter_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_parameter_list**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_parameter_list>`{.interpreted-text
role="ref"}

Return the controllable parameters of this stream. This array contains
dictionaries with a property info description format (see
`Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}). Additionally, the default value for this parameter must be
added tho each dictionary in \"default_value\" field.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__get_stream_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_stream_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_stream_name>`{.interpreted-text
role="ref"}

Override this method to customize the name assigned to this audio
stream. Unused by the engine.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__get_tags}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_tags**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__get_tags>`{.interpreted-text
role="ref"}

Override this method to customize the tags for this audio stream. Should
return a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} of
strings with the tag as the key and its content as the value.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`,
and `date`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__has_loop}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has_loop**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__has_loop>`{.interpreted-text
role="ref"}

Override this method to return `true` if this stream has a loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__instantiate_playback}
::: rst-class
classref-method
:::
::::

`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **\_instantiate_playback**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__instantiate_playback>`{.interpreted-text
role="ref"}

Override this method to customize the returned value of
`instantiate_playback()<class_AudioStream_method_instantiate_playback>`{.interpreted-text
role="ref"}. Should return a new
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} created when the stream is played (such as by an
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_private_method__is_monophonic}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_monophonic**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_private_method__is_monophonic>`{.interpreted-text
role="ref"}

Override this method to customize the returned value of
`is_monophonic()<class_AudioStream_method_is_monophonic>`{.interpreted-text
role="ref"}. Should return `true` if this audio stream only supports one
channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_method_can_be_sampled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_be_sampled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_method_can_be_sampled>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Returns if the current **AudioStream** can be used as a sample. Only
static streams can be sampled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_method_generate_sample}
::: rst-class
classref-method
:::
::::

`AudioSample<class_AudioSample>`{.interpreted-text role="ref"}
**generate_sample**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_method_generate_sample>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Generates an `AudioSample<class_AudioSample>`{.interpreted-text
role="ref"} based on the current stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_method_get_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AudioStream_method_get_length>`{.interpreted-text
role="ref"}

Returns the length of the audio stream in seconds. If this stream is an
`AudioStreamRandomizer<class_AudioStreamRandomizer>`{.interpreted-text
role="ref"}, returns the length of the last played stream. If this
stream has an indefinite length (such as for
`AudioStreamGenerator<class_AudioStreamGenerator>`{.interpreted-text
role="ref"} and
`AudioStreamMicrophone<class_AudioStreamMicrophone>`{.interpreted-text
role="ref"}), returns `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_method_instantiate_playback}
::: rst-class
classref-method
:::
::::

`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **instantiate_playback**()
`🔗<class_AudioStream_method_instantiate_playback>`{.interpreted-text
role="ref"}

Returns a newly created
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} intended to play this audio stream. Useful for when you want
to extend
`_instantiate_playback()<class_AudioStream_private_method__instantiate_playback>`{.interpreted-text
role="ref"} but call
`instantiate_playback()<class_AudioStream_method_instantiate_playback>`{.interpreted-text
role="ref"} from an internally held AudioStream subresource. An example
of this can be found in the source code for
`AudioStreamRandomPitch::instantiate_playback`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_method_is_meta_stream}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_meta_stream**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_method_is_meta_stream>`{.interpreted-text
role="ref"}

Returns `true` if the stream is a collection of other streams, `false`
otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStream_method_is_monophonic}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_monophonic**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStream_method_is_monophonic>`{.interpreted-text
role="ref"}

Returns `true` if this audio stream only supports one channel
(*monophony*), or `false` if the audio stream supports two or more
channels (*polyphony*).
