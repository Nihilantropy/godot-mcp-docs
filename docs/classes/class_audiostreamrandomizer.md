github_url
:   hide

# AudioStreamRandomizer {#class_AudioStreamRandomizer}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Wraps a pool of audio streams with pitch and volume shifting.

::: rst-class
classref-introduction-group
:::

## Description

Picks a random AudioStream from the pool, depending on the playback
mode, and applies random pitch shifting and volume shifting during
playback.

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

## Enumerations

:::: {#enum_AudioStreamRandomizer_PlaybackMode}
::: rst-class
classref-enumeration
:::
::::

enum **PlaybackMode**:
`🔗<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamRandomizer_constant_PLAYBACK_RANDOM_NO_REPEATS}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
role="ref"} **PLAYBACK_RANDOM_NO_REPEATS** = `0`

Pick a stream at random according to the probability weights chosen for
each stream, but avoid playing the same stream twice in a row whenever
possible. If only 1 sound is present in the pool, the same sound will
always play, effectively allowing repeats to occur.

:::: {#class_AudioStreamRandomizer_constant_PLAYBACK_RANDOM}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
role="ref"} **PLAYBACK_RANDOM** = `1`

Pick a stream at random according to the probability weights chosen for
each stream. If only 1 sound is present in the pool, the same sound will
always play.

:::: {#class_AudioStreamRandomizer_constant_PLAYBACK_SEQUENTIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
role="ref"} **PLAYBACK_SEQUENTIAL** = `2`

Play streams in the order they appear in the stream pool. If only 1
sound is present in the pool, the same sound will always play.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamRandomizer_property_playback_mode}
::: rst-class
classref-property
:::
::::

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
role="ref"} **playback_mode** = `0`
`🔗<class_AudioStreamRandomizer_property_playback_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_playback_mode**(value:
  `PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
  role="ref"})
- `PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`{.interpreted-text
  role="ref"} **get_playback_mode**()

Controls how this AudioStreamRandomizer picks which AudioStream to play
next.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_property_random_pitch}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **random_pitch** =
`1.0`
`🔗<class_AudioStreamRandomizer_property_random_pitch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_random_pitch**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_random_pitch**()

The intensity of random pitch variation. A value of 1 means no
variation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_property_random_volume_offset_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**random_volume_offset_db** = `0.0`
`🔗<class_AudioStreamRandomizer_property_random_volume_offset_db>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_random_volume_offset_db**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_random_volume_offset_db**()

The intensity of random volume variation. A value of 0 means no
variation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_property_streams_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **streams_count** = `0`
`🔗<class_AudioStreamRandomizer_property_streams_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_streams_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_streams_count**()

The number of streams in the stream pool.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamRandomizer_method_add_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_stream**(index: `int<class_int>`{.interpreted-text role="ref"},
stream: `AudioStream<class_AudioStream>`{.interpreted-text role="ref"},
weight: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_AudioStreamRandomizer_method_add_stream>`{.interpreted-text
role="ref"}

Insert a stream at the specified index. If the index is less than zero,
the insertion occurs at the end of the underlying pool.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_method_get_stream}
::: rst-class
classref-method
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**get_stream**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamRandomizer_method_get_stream>`{.interpreted-text
role="ref"}

Returns the stream at the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_method_get_stream_probability_weight}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_stream_probability_weight**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamRandomizer_method_get_stream_probability_weight>`{.interpreted-text
role="ref"}

Returns the probability weight associated with the stream at the given
index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_method_move_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_stream**(index_from: `int<class_int>`{.interpreted-text
role="ref"}, index_to: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamRandomizer_method_move_stream>`{.interpreted-text
role="ref"}

Move a stream from one index to another.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_method_remove_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_stream**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamRandomizer_method_remove_stream>`{.interpreted-text
role="ref"}

Remove the stream at the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_method_set_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stream**(index: `int<class_int>`{.interpreted-text role="ref"},
stream: `AudioStream<class_AudioStream>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamRandomizer_method_set_stream>`{.interpreted-text
role="ref"}

Set the AudioStream at the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamRandomizer_method_set_stream_probability_weight}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stream_probability_weight**(index:
`int<class_int>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamRandomizer_method_set_stream_probability_weight>`{.interpreted-text
role="ref"}

Set the probability weight of the stream at the specified index. The
higher this value, the more likely that the randomizer will choose this
stream during random playback modes.
