github_url
:   hide

# AudioStreamOggVorbis {#class_AudioStreamOggVorbis}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A class representing an Ogg Vorbis audio stream.

::: rst-class
classref-introduction-group
:::

## Description

The AudioStreamOggVorbis class is a specialized
`AudioStream<class_AudioStream>`{.interpreted-text role="ref"} for
handling Ogg Vorbis file formats. It offers functionality for loading
and playing back Ogg Vorbis files, as well as managing looping and other
playback properties. This class is part of the audio stream system,
which also supports WAV files through the
`AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text role="ref"}
class.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
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

## Property Descriptions

:::: {#class_AudioStreamOggVorbis_property_bar_beats}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bar_beats** = `4`
`🔗<class_AudioStreamOggVorbis_property_bar_beats>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bar_beats**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bar_beats**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_property_beat_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **beat_count** = `0`
`🔗<class_AudioStreamOggVorbis_property_beat_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_beat_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_beat_count**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_property_bpm}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bpm** = `0.0`
`🔗<class_AudioStreamOggVorbis_property_bpm>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bpm**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bpm**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `false`
`🔗<class_AudioStreamOggVorbis_property_loop>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_loop**()

If `true`, the audio will play again from the specified
`loop_offset<class_AudioStreamOggVorbis_property_loop_offset>`{.interpreted-text
role="ref"} once it is done playing. Useful for ambient sounds and
background music.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_property_loop_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **loop_offset** =
`0.0`
`🔗<class_AudioStreamOggVorbis_property_loop_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_loop_offset**()

Time in seconds at which the stream starts after being looped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_property_packet_sequence}
::: rst-class
classref-property
:::
::::

`OggPacketSequence<class_OggPacketSequence>`{.interpreted-text
role="ref"} **packet_sequence**
`🔗<class_AudioStreamOggVorbis_property_packet_sequence>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_packet_sequence**(value:
  `OggPacketSequence<class_OggPacketSequence>`{.interpreted-text
  role="ref"})
- `OggPacketSequence<class_OggPacketSequence>`{.interpreted-text
  role="ref"} **get_packet_sequence**()

Contains the raw Ogg data for this stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_property_tags}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} **tags** =
`{}` `🔗<class_AudioStreamOggVorbis_property_tags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tags**(value: `Dictionary<class_Dictionary>`{.interpreted-text
  role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_tags**()

Contains user-defined tags if found in the Ogg Vorbis data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`,
and `date` (`date` does not have a standard date format).

\*\*Note:\*\* No tag is *guaranteed* to be present in every file, so
make sure to account for the keys not always existing.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamOggVorbis_method_load_from_buffer}
::: rst-class
classref-method
:::
::::

`AudioStreamOggVorbis<class_AudioStreamOggVorbis>`{.interpreted-text
role="ref"} **load_from_buffer**(stream_data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamOggVorbis_method_load_from_buffer>`{.interpreted-text
role="ref"}

Creates a new **AudioStreamOggVorbis** instance from the given buffer.
The buffer must contain Ogg Vorbis data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamOggVorbis_method_load_from_file}
::: rst-class
classref-method
:::
::::

`AudioStreamOggVorbis<class_AudioStreamOggVorbis>`{.interpreted-text
role="ref"} **load_from_file**(path:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamOggVorbis_method_load_from_file>`{.interpreted-text
role="ref"}

Creates a new **AudioStreamOggVorbis** instance from the given file
path. The file must be in Ogg Vorbis format.
