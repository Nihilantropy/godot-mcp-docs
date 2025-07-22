github_url
:   hide

# VideoStreamPlayer {#class_VideoStreamPlayer}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control used for video playback.

::: rst-class
classref-introduction-group
:::

## Description

A control used for playback of
`VideoStream<class_VideoStream>`{.interpreted-text role="ref"}
resources.

Supported video formats are [Ogg Theora](https://www.theora.org/)
(`.ogv`, `VideoStreamTheora<class_VideoStreamTheora>`{.interpreted-text
role="ref"}) and any format exposed via a GDExtension plugin.

\*\*Warning:\*\* On Web, video playback *will* perform poorly due to
missing architecture-specific assembly optimizations.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Playing videos <../tutorials/animation/playing_videos>`{.interpreted-text
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

:::: {#class_VideoStreamPlayer_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_VideoStreamPlayer_signal_finished>`{.interpreted-text
role="ref"}

Emitted when playback is finished.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VideoStreamPlayer_property_audio_track}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **audio_track** = `0`
`🔗<class_VideoStreamPlayer_property_audio_track>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_audio_track**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_audio_track**()

The embedded audio track to play.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_autoplay}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autoplay** = `false`
`🔗<class_VideoStreamPlayer_property_autoplay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoplay**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_autoplay**()

If `true`, playback starts when the scene loads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_buffering_msec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buffering_msec** =
`500`
`🔗<class_VideoStreamPlayer_property_buffering_msec>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffering_msec**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_buffering_msec**()

Amount of time in milliseconds to store in buffer while playing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_bus}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **bus** =
`&"Master"` `🔗<class_VideoStreamPlayer_property_bus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bus**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_bus**()

Audio bus to use for sound playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_expand}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **expand** = `false`
`🔗<class_VideoStreamPlayer_property_expand>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_expand**()

If `true`, the video scales to the control size. Otherwise, the control
minimum size will be automatically adjusted to match the video stream\'s
dimensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `false`
`🔗<class_VideoStreamPlayer_property_loop>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_loop**()

If `true`, the video restarts when it reaches its end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_paused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **paused** = `false`
`🔗<class_VideoStreamPlayer_property_paused>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_paused**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_paused**()

If `true`, the video is paused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **speed_scale** =
`1.0`
`🔗<class_VideoStreamPlayer_property_speed_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_speed_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_speed_scale**()

The stream\'s current speed scale. `1.0` is the normal speed, while
`2.0` is double speed and `0.5` is half speed. A speed scale of `0.0`
pauses the video, similar to setting
`paused<class_VideoStreamPlayer_property_paused>`{.interpreted-text
role="ref"} to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_stream}
::: rst-class
classref-property
:::
::::

`VideoStream<class_VideoStream>`{.interpreted-text role="ref"}
**stream**
`🔗<class_VideoStreamPlayer_property_stream>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream**(value:
  `VideoStream<class_VideoStream>`{.interpreted-text role="ref"})
- `VideoStream<class_VideoStream>`{.interpreted-text role="ref"}
  **get_stream**()

The assigned video stream. See description for supported formats.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_stream_position}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **stream_position**
`🔗<class_VideoStreamPlayer_property_stream_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream_position**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_stream_position**()

The current position of the stream, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_volume}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume**
`🔗<class_VideoStreamPlayer_property_volume>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_volume**()

Audio volume as a linear value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_property_volume_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **volume_db** = `0.0`
`🔗<class_VideoStreamPlayer_property_volume_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_volume_db**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_volume_db**()

Audio volume in dB.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VideoStreamPlayer_method_get_stream_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_stream_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayer_method_get_stream_length>`{.interpreted-text
role="ref"}

The length of the current stream, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_method_get_stream_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_stream_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayer_method_get_stream_name>`{.interpreted-text
role="ref"}

Returns the video stream\'s name, or `"<No Stream>"` if no video stream
is assigned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_method_get_video_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_video_texture**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayer_method_get_video_texture>`{.interpreted-text
role="ref"}

Returns the current frame as a
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_method_is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStreamPlayer_method_is_playing>`{.interpreted-text
role="ref"}

Returns `true` if the video is playing.

\*\*Note:\*\* The video is still considered playing if paused during
playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **play**()
`🔗<class_VideoStreamPlayer_method_play>`{.interpreted-text role="ref"}

Starts the video playback from the beginning. If the video is paused,
this will not unpause the video.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VideoStreamPlayer_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_VideoStreamPlayer_method_stop>`{.interpreted-text role="ref"}

Stops the video playback and sets the stream position to 0.

\*\*Note:\*\* Although the stream position will be set to 0, the first
frame of the video stream won\'t become the current frame.
