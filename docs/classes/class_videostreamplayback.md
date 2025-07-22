github_url
:   hide

# VideoStreamPlayback {#class_VideoStreamPlayback}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Internal class used by
`VideoStream<class_VideoStream>`{.interpreted-text role="ref"} to manage
playback state when played from a
`VideoStreamPlayer<class_VideoStreamPlayer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This class is intended to be overridden by video decoder extensions with
custom implementations of
`VideoStream<class_VideoStream>`{.interpreted-text role="ref"}.

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

:::: {#class_VideoStreamPlayback_private_method__get_channels}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_channels**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__get_channels>`{.interpreted-text
role="ref"}

Returns the number of audio channels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__get_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **\_get_length**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__get_length>`{.interpreted-text
role="ref"}

Returns the video duration in seconds, if known, or 0 if unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__get_mix_rate}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_mix_rate**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__get_mix_rate>`{.interpreted-text
role="ref"}

Returns the audio sample rate used for mixing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__get_playback_position}
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
`🔗<class_VideoStreamPlayback_private_method__get_playback_position>`{.interpreted-text
role="ref"}

Return the current playback timestamp. Called in response to the
`VideoStreamPlayer.stream_position<class_VideoStreamPlayer_property_stream_position>`{.interpreted-text
role="ref"} getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__get_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\_get_texture**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__get_texture>`{.interpreted-text
role="ref"}

Allocates a `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
in which decoded video frames will be drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__is_paused}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_paused**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__is_paused>`{.interpreted-text
role="ref"}

Returns the paused status, as set by
`_set_paused()<class_VideoStreamPlayback_private_method__set_paused>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_playing**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__is_playing>`{.interpreted-text
role="ref"}

Returns the playback state, as determined by calls to
`_play()<class_VideoStreamPlayback_private_method__play>`{.interpreted-text
role="ref"} and
`_stop()<class_VideoStreamPlayback_private_method__stop>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_play**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__play>`{.interpreted-text
role="ref"}

Called in response to
`VideoStreamPlayer.autoplay<class_VideoStreamPlayer_property_autoplay>`{.interpreted-text
role="ref"} or
`VideoStreamPlayer.play()<class_VideoStreamPlayer_method_play>`{.interpreted-text
role="ref"}. Note that manual playback may also invoke
`_stop()<class_VideoStreamPlayback_private_method__stop>`{.interpreted-text
role="ref"} multiple times before this method is called.
`_is_playing()<class_VideoStreamPlayback_private_method__is_playing>`{.interpreted-text
role="ref"} should return `true` once playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_seek**(time: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__seek>`{.interpreted-text
role="ref"}

Seeks to `time` seconds. Called in response to the
`VideoStreamPlayer.stream_position<class_VideoStreamPlayer_property_stream_position>`{.interpreted-text
role="ref"} setter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__set_audio_track}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_audio_track**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__set_audio_track>`{.interpreted-text
role="ref"}

Select the audio track `idx`. Called when playback starts, and in
response to the
`VideoStreamPlayer.audio_track<class_VideoStreamPlayer_property_audio_track>`{.interpreted-text
role="ref"} setter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__set_paused}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_paused**(paused: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__set_paused>`{.interpreted-text
role="ref"}

Set the paused status of video playback.
`_is_paused()<class_VideoStreamPlayback_private_method__is_paused>`{.interpreted-text
role="ref"} must return `paused`. Called in response to the
`VideoStreamPlayer.paused<class_VideoStreamPlayer_property_paused>`{.interpreted-text
role="ref"} setter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_stop**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__stop>`{.interpreted-text
role="ref"}

Stops playback. May be called multiple times before
`_play()<class_VideoStreamPlayback_private_method__play>`{.interpreted-text
role="ref"}, or in response to
`VideoStreamPlayer.stop()<class_VideoStreamPlayer_method_stop>`{.interpreted-text
role="ref"}.
`_is_playing()<class_VideoStreamPlayback_private_method__is_playing>`{.interpreted-text
role="ref"} should return `false` once stopped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_private_method__update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_update**(delta: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayback_private_method__update>`{.interpreted-text
role="ref"}

Ticks video playback for `delta` seconds. Called every frame as long as
both
`_is_paused()<class_VideoStreamPlayback_private_method__is_paused>`{.interpreted-text
role="ref"} and
`_is_playing()<class_VideoStreamPlayback_private_method__is_playing>`{.interpreted-text
role="ref"} return `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayback_method_mix_audio}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mix_audio**(num_frames:
`int<class_int>`{.interpreted-text role="ref"}, buffer:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} = PackedFloat32Array(), offset:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_VideoStreamPlayback_method_mix_audio>`{.interpreted-text
role="ref"}

Render `num_frames` audio frames (of
`_get_channels()<class_VideoStreamPlayback_private_method__get_channels>`{.interpreted-text
role="ref"} floats each) from `buffer`, starting from index `offset` in
the array. Returns the number of audio frames rendered, or -1 on error.
