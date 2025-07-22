github_url
:   hide

# AudioStreamSynchronized {#class_AudioStreamSynchronized}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Stream that can be fitted with sub-streams, which will be played
in-sync.

::: rst-class
classref-introduction-group
:::

## Description

This is a stream that can be fitted with sub-streams, which will be
played in-sync. The streams begin at exactly the same time when play is
pressed, and will end when the last of them ends. If one of the
sub-streams loops, then playback will continue.

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

:::: {#class_AudioStreamSynchronized_constant_MAX_STREAMS}
::: rst-class
classref-constant
:::
::::

**MAX_STREAMS** = `32`
`🔗<class_AudioStreamSynchronized_constant_MAX_STREAMS>`{.interpreted-text
role="ref"}

Maximum amount of streams that can be synchronized.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamSynchronized_property_stream_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **stream_count** = `0`
`🔗<class_AudioStreamSynchronized_property_stream_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_stream_count**()

Set the total amount of streams that will be played back synchronized.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamSynchronized_method_get_sync_stream}
::: rst-class
classref-method
:::
::::

`AudioStream<class_AudioStream>`{.interpreted-text role="ref"}
**get_sync_stream**(stream_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamSynchronized_method_get_sync_stream>`{.interpreted-text
role="ref"}

Get one of the synchronized streams, by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamSynchronized_method_get_sync_stream_volume}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_sync_stream_volume**(stream_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamSynchronized_method_get_sync_stream_volume>`{.interpreted-text
role="ref"}

Get the volume of one of the synchronized streams, by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamSynchronized_method_set_sync_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_sync_stream**(stream_index: `int<class_int>`{.interpreted-text
role="ref"}, audio_stream:
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamSynchronized_method_set_sync_stream>`{.interpreted-text
role="ref"}

Set one of the synchronized streams, by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamSynchronized_method_set_sync_stream_volume}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_sync_stream_volume**(stream_index:
`int<class_int>`{.interpreted-text role="ref"}, volume_db:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamSynchronized_method_set_sync_stream_volume>`{.interpreted-text
role="ref"}

Set the volume of one of the synchronized streams, by index.
