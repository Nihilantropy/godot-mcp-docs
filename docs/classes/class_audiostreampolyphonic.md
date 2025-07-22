github_url
:   hide

# AudioStreamPolyphonic {#class_AudioStreamPolyphonic}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

AudioStream that lets the user play custom streams at any time from
code, simultaneously using a single player.

::: rst-class
classref-introduction-group
:::

## Description

AudioStream that lets the user play custom streams at any time from
code, simultaneously using a single player.

Playback control is done via the
`AudioStreamPlaybackPolyphonic<class_AudioStreamPlaybackPolyphonic>`{.interpreted-text
role="ref"} instance set inside the player, which can be obtained via
`AudioStreamPlayer.get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>`{.interpreted-text
role="ref"},
`AudioStreamPlayer2D.get_stream_playback()<class_AudioStreamPlayer2D_method_get_stream_playback>`{.interpreted-text
role="ref"} or
`AudioStreamPlayer3D.get_stream_playback()<class_AudioStreamPlayer3D_method_get_stream_playback>`{.interpreted-text
role="ref"} methods. Obtaining the playback instance is only valid after
the `stream` property is set as an **AudioStreamPolyphonic** in those
players.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamPolyphonic_property_polyphony}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **polyphony** = `32`
`🔗<class_AudioStreamPolyphonic_property_polyphony>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polyphony**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_polyphony**()

Maximum amount of simultaneous streams that can be played.
