github_url
:   hide

# ResourceImporterMP3 {#class_ResourceImporterMP3}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports an MP3 audio file for playback.

::: rst-class
classref-introduction-group
:::

## Description

MP3 is a lossy audio format, with worse audio quality compared to
`ResourceImporterOggVorbis<class_ResourceImporterOggVorbis>`{.interpreted-text
role="ref"} at a given bitrate.

In most cases, it\'s recommended to use Ogg Vorbis over MP3. However, if
you\'re using an MP3 sound source with no higher quality source
available, then it\'s recommended to use the MP3 file directly to avoid
double lossy compression.

MP3 requires more CPU to decode than
`ResourceImporterWAV<class_ResourceImporterWAV>`{.interpreted-text
role="ref"}. If you need to play a lot of simultaneous sounds, it\'s
recommended to use WAV for those sounds instead, especially if targeting
low-end devices.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing audio samples <../tutorials/assets_pipeline/importing_audio_samples>`{.interpreted-text
  role="doc"}

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

:::: {#class_ResourceImporterMP3_property_bar_beats}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bar_beats** = `4`
`🔗<class_ResourceImporterMP3_property_bar_beats>`{.interpreted-text
role="ref"}

The number of bars within a single beat in the audio track. This is only
relevant for music that wishes to make use of interactive music
functionality, not sound effects.

A more convenient editor for
`bar_beats<class_ResourceImporterMP3_property_bar_beats>`{.interpreted-text
role="ref"} is provided in the **Advanced Import Settings** dialog, as
it lets you preview your changes without having to reimport the audio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterMP3_property_beat_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **beat_count** = `0`
`🔗<class_ResourceImporterMP3_property_beat_count>`{.interpreted-text
role="ref"}

The beat count of the audio track. This is only relevant for music that
wishes to make use of interactive music functionality, not sound
effects.

A more convenient editor for
`beat_count<class_ResourceImporterMP3_property_beat_count>`{.interpreted-text
role="ref"} is provided in the **Advanced Import Settings** dialog, as
it lets you preview your changes without having to reimport the audio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterMP3_property_bpm}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bpm** = `0`
`🔗<class_ResourceImporterMP3_property_bpm>`{.interpreted-text
role="ref"}

The beats per minute of the audio track. This should match the BPM
measure that was used to compose the track. This is only relevant for
music that wishes to make use of interactive music functionality, not
sound effects.

A more convenient editor for
`bpm<class_ResourceImporterMP3_property_bpm>`{.interpreted-text
role="ref"} is provided in the **Advanced Import Settings** dialog, as
it lets you preview your changes without having to reimport the audio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterMP3_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `false`
`🔗<class_ResourceImporterMP3_property_loop>`{.interpreted-text
role="ref"}

If enabled, the audio will begin playing at the beginning after playback
ends by reaching the end of the audio.

\*\*Note:\*\* In
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"}, the
`AudioStreamPlayer.finished<class_AudioStreamPlayer_signal_finished>`{.interpreted-text
role="ref"} signal won\'t be emitted for looping audio when it reaches
the end of the audio file, as the audio will keep playing indefinitely.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterMP3_property_loop_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **loop_offset** = `0`
`🔗<class_ResourceImporterMP3_property_loop_offset>`{.interpreted-text
role="ref"}

Determines where audio will start to loop after playback reaches the end
of the audio. This can be used to only loop a part of the audio file,
which is useful for some ambient sounds or music. The value is
determined in seconds relative to the beginning of the audio. A value of
`0.0` will loop the entire audio file.

Only has an effect if
`loop<class_ResourceImporterMP3_property_loop>`{.interpreted-text
role="ref"} is `true`.

A more convenient editor for
`loop_offset<class_ResourceImporterMP3_property_loop_offset>`{.interpreted-text
role="ref"} is provided in the **Advanced Import Settings** dialog, as
it lets you preview your changes without having to reimport the audio.
