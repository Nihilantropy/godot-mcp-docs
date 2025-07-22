github_url
:   hide

# AudioStreamPlaylist {#class_AudioStreamPlaylist}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"} that
includes sub-streams and plays them back like a playlist.

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

## Constants

:::: {#class_AudioStreamPlaylist_constant_MAX_STREAMS}
::: rst-class
classref-constant
:::
::::

**MAX_STREAMS** = `64`
`🔗<class_AudioStreamPlaylist_constant_MAX_STREAMS>`{.interpreted-text
role="ref"}

Maximum amount of streams supported in the playlist.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamPlaylist_property_fade_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fade_time** = `0.3`
`🔗<class_AudioStreamPlaylist_property_fade_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fade_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_fade_time**()

Fade time used when a stream ends, when going to the next one. Streams
are expected to have an extra bit of audio after the end to help with
fading.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaylist_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `true`
`🔗<class_AudioStreamPlaylist_property_loop>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_loop**()

If `true`, the playlist will loop, otherwise the playlist will end when
the last stream is finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaylist_property_shuffle}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shuffle** = `false`
`🔗<class_AudioStreamPlaylist_property_shuffle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shuffle**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_shuffle**()

If `true`, the playlist will shuffle each time playback starts and each
time it loops.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaylist_property_stream_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stream_count** = `0`
`🔗<class_AudioStreamPlaylist_property_stream_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_stream_count**()

Amount of streams in the playlist.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamPlaylist_method_get_bpm}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_bpm**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlaylist_method_get_bpm>`{.interpreted-text
role="ref"}

Returns the BPM of the playlist, which can vary depending on the clip
being played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaylist_method_get_list_stream}
::: rst-class
classref-method
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**get_list_stream**(stream_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlaylist_method_get_list_stream>`{.interpreted-text
role="ref"}

Returns the stream at playback position index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaylist_method_set_list_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_list_stream**(stream_index: `int<class_int>`{.interpreted-text
role="ref"}, audio_stream:
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamPlaylist_method_set_list_stream>`{.interpreted-text
role="ref"}

Sets the stream at playback position index.
