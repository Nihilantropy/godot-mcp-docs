github_url
:   hide

# AudioStreamPlayback {#class_AudioStreamPlayback}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioStreamPlaybackInteractive<class_AudioStreamPlaybackInteractive>`{.interpreted-text
role="ref"},
`AudioStreamPlaybackPlaylist<class_AudioStreamPlaybackPlaylist>`{.interpreted-text
role="ref"},
`AudioStreamPlaybackPolyphonic<class_AudioStreamPlaybackPolyphonic>`{.interpreted-text
role="ref"},
`AudioStreamPlaybackResampled<class_AudioStreamPlaybackResampled>`{.interpreted-text
role="ref"},
`AudioStreamPlaybackSynchronized<class_AudioStreamPlaybackSynchronized>`{.interpreted-text
role="ref"}

Meta class for playing back audio.

::: rst-class
classref-introduction-group
:::

## Description

Can play, loop, pause a scroll through audio. See
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"} and
`AudioStreamOggVorbis<class_AudioStreamOggVorbis>`{.interpreted-text
role="ref"} for usage.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Audio Generator
  Demo](https://godotengine.org/asset-library/asset/2759)

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

## Method Descriptions

:::: {#class_AudioStreamPlayback_private_method__get_loop_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_loop_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__get_loop_count>`{.interpreted-text
role="ref"}

Overridable method. Should return how many times this audio stream has
looped. Most built-in playbacks always return `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__get_parameter}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_parameter**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__get_parameter>`{.interpreted-text
role="ref"}

Return the current value of a playback parameter by name (see
`AudioStream._get_parameter_list()<class_AudioStream_private_method__get_parameter_list>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__get_playback_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_playback_position**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__get_playback_position>`{.interpreted-text
role="ref"}

Overridable method. Should return the current progress along the audio
stream, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_playing**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__is_playing>`{.interpreted-text
role="ref"}

Overridable method. Should return `true` if this playback is active and
playing its audio stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__mix}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_mix**(buffer:
`AudioFrame*`, rate_scale: `float<class_float>`{.interpreted-text
role="ref"}, frames: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__mix>`{.interpreted-text
role="ref"}

Override this method to customize how the audio stream is mixed. This
method is called even if the playback is not active.

\*\*Note:\*\* It is not useful to override this method in GDScript or
C#. Only GDExtension can take advantage of it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_seek**(position: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__seek>`{.interpreted-text
role="ref"}

Override this method to customize what happens when seeking this audio
stream at the given `position`, such as by calling
`AudioStreamPlayer.seek()<class_AudioStreamPlayer_method_seek>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__set_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_parameter**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__set_parameter>`{.interpreted-text
role="ref"}

Set the current value of a playback parameter by name (see
`AudioStream._get_parameter_list()<class_AudioStream_private_method__get_parameter_list>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__start}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_start**(from_pos: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__start>`{.interpreted-text
role="ref"}

Override this method to customize what happens when the playback starts
at the given position, such as by calling
`AudioStreamPlayer.play()<class_AudioStreamPlayer_method_play>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_stop**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__stop>`{.interpreted-text
role="ref"}

Override this method to customize what happens when the playback is
stopped, such as by calling
`AudioStreamPlayer.stop()<class_AudioStreamPlayer_method_stop>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_private_method__tag_used_streams}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_tag_used_streams**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_private_method__tag_used_streams>`{.interpreted-text
role="ref"}

Overridable method. Called whenever the audio stream is mixed if the
playback is active and
`AudioServer.set_enable_tagging_used_audio_streams()<class_AudioServer_method_set_enable_tagging_used_audio_streams>`{.interpreted-text
role="ref"} has been set to `true`. Editor plugins may use this method
to \"tag\" the current position along the audio stream and display it in
a preview.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_get_loop_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_loop_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_method_get_loop_count>`{.interpreted-text
role="ref"}

Returns the number of times the stream has looped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_get_playback_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_playback_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_method_get_playback_position>`{.interpreted-text
role="ref"}

Returns the current position in the stream, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_get_sample_playback}
::: rst-class
classref-method
:::
::::

`AudioSamplePlayback<class_AudioSamplePlayback>`{.interpreted-text
role="ref"} **get_sample_playback**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_method_get_sample_playback>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Returns the
`AudioSamplePlayback<class_AudioSamplePlayback>`{.interpreted-text
role="ref"} associated with this **AudioStreamPlayback** for playing
back the audio sample of this stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlayback_method_is_playing>`{.interpreted-text
role="ref"}

Returns `true` if the stream is playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_mix_audio}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **mix_audio**(rate_scale:
`float<class_float>`{.interpreted-text role="ref"}, frames:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamPlayback_method_mix_audio>`{.interpreted-text
role="ref"}

Mixes up to `frames` of audio from the stream from the current position,
at a rate of `rate_scale`, advancing the stream.

Returns a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} where each element holds the left and right channel volume
levels of each frame.

\*\*Note:\*\* Can return fewer frames than requested, make sure to use
the size of the return value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **seek**(time:
`float<class_float>`{.interpreted-text role="ref"} = 0.0)
`🔗<class_AudioStreamPlayback_method_seek>`{.interpreted-text
role="ref"}

Seeks the stream at the given `time`, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_set_sample_playback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_sample_playback**(playback_sample:
`AudioSamplePlayback<class_AudioSamplePlayback>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamPlayback_method_set_sample_playback>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Associates
`AudioSamplePlayback<class_AudioSamplePlayback>`{.interpreted-text
role="ref"} to this **AudioStreamPlayback** for playing back the audio
sample of this stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_start}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start**(from_pos: `float<class_float>`{.interpreted-text role="ref"} =
0.0) `🔗<class_AudioStreamPlayback_method_start>`{.interpreted-text
role="ref"}

Starts the stream from the given `from_pos`, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlayback_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_AudioStreamPlayback_method_stop>`{.interpreted-text
role="ref"}

Stops the stream.
