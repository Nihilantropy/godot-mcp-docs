github_url
:   hide

# ResourceImporterWAV {#class_ResourceImporterWAV}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a WAV audio file for playback.

::: rst-class
classref-introduction-group
:::

## Description

WAV is an uncompressed format, which can provide higher quality compared
to Ogg Vorbis and MP3. It also has the lowest CPU cost to decode. This
means high numbers of WAV sounds can be played at the same time, even on
low-end devices.

By default, Godot imports WAV files using the lossy Quite OK Audio
compression. You may change this by setting the
`compress/mode<class_ResourceImporterWAV_property_compress/mode>`{.interpreted-text
role="ref"} property.

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

:::: {#class_ResourceImporterWAV_property_compress/mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compress/mode** = `2`
`🔗<class_ResourceImporterWAV_property_compress/mode>`{.interpreted-text
role="ref"}

The compression mode to use on import.

- **PCM (Uncompressed):** Imports audio data without any form of
  compression, preserving the highest possible quality. It has the
  lowest CPU cost, but the highest memory usage.
- **IMA ADPCM:** Applies fast, lossy compression during import,
  noticeably decreasing the quality, but with low CPU cost and memory
  usage. Does not support seeking and only Forward loop mode is
  supported.
- **\`Quite OK Audio \<https://qoaformat.org/\>\`\_\_:** Also applies
  lossy compression on import, having a slightly higher CPU cost
  compared to IMA ADPCM, but much higher quality and the lowest memory
  usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_edit/loop_begin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **edit/loop_begin** = `0`
`🔗<class_ResourceImporterWAV_property_edit/loop_begin>`{.interpreted-text
role="ref"}

The begin loop point to use when
`edit/loop_mode<class_ResourceImporterWAV_property_edit/loop_mode>`{.interpreted-text
role="ref"} is **Forward**, **Ping-Pong**, or **Backward**. This is set
in samples after the beginning of the audio file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_edit/loop_end}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **edit/loop_end** = `-1`
`🔗<class_ResourceImporterWAV_property_edit/loop_end>`{.interpreted-text
role="ref"}

The end loop point to use when
`edit/loop_mode<class_ResourceImporterWAV_property_edit/loop_mode>`{.interpreted-text
role="ref"} is **Forward**, **Ping-Pong**, or **Backward**. This is set
in samples after the beginning of the audio file. A value of `-1` uses
the end of the audio file as the end loop point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_edit/loop_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **edit/loop_mode** = `0`
`🔗<class_ResourceImporterWAV_property_edit/loop_mode>`{.interpreted-text
role="ref"}

Controls how audio should loop.

- **Detect From WAV:** Uses loop information from the WAV metadata.
- **Disabled:** Don\'t loop audio, even if the metadata indicates the
  file playback should loop.
- **Forward:** Standard audio looping. Plays the audio forward from the
  beginning to
  `edit/loop_end<class_ResourceImporterWAV_property_edit/loop_end>`{.interpreted-text
  role="ref"}, then returns to
  `edit/loop_begin<class_ResourceImporterWAV_property_edit/loop_begin>`{.interpreted-text
  role="ref"} and repeats.
- **Ping-Pong:** Plays the audio forward until
  `edit/loop_end<class_ResourceImporterWAV_property_edit/loop_end>`{.interpreted-text
  role="ref"}, then backwards to
  `edit/loop_begin<class_ResourceImporterWAV_property_edit/loop_begin>`{.interpreted-text
  role="ref"}, repeating this cycle.
- **Backward:** Plays the audio backwards from
  `edit/loop_end<class_ResourceImporterWAV_property_edit/loop_end>`{.interpreted-text
  role="ref"} to
  `edit/loop_begin<class_ResourceImporterWAV_property_edit/loop_begin>`{.interpreted-text
  role="ref"}, then repeats.

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

:::: {#class_ResourceImporterWAV_property_edit/normalize}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **edit/normalize** =
`false`
`🔗<class_ResourceImporterWAV_property_edit/normalize>`{.interpreted-text
role="ref"}

If `true`, normalize the audio volume so that its peak volume is equal
to 0 dB. When enabled, normalization will make audio sound louder
depending on its original peak volume.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_edit/trim}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **edit/trim** = `false`
`🔗<class_ResourceImporterWAV_property_edit/trim>`{.interpreted-text
role="ref"}

If `true`, automatically trim the beginning and end of the audio if
it\'s lower than -50 dB after normalization (see
`edit/normalize<class_ResourceImporterWAV_property_edit/normalize>`{.interpreted-text
role="ref"}). This prevents having files with silence at the beginning
or end, which increases their size unnecessarily and adds latency to the
moment they are played back. A fade-in/fade-out period of 500 samples is
also used during trimming to avoid audible pops.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_force/8_bit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force/8_bit** =
`false`
`🔗<class_ResourceImporterWAV_property_force/8_bit>`{.interpreted-text
role="ref"}

If `true`, forces the imported audio to use 8-bit quantization if the
source file is 16-bit or higher.

Enabling this is generally not recommended, as 8-bit quantization
decreases audio quality significantly. If you need smaller file sizes,
consider using Ogg Vorbis or MP3 audio instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_force/max_rate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force/max_rate** =
`false`
`🔗<class_ResourceImporterWAV_property_force/max_rate>`{.interpreted-text
role="ref"}

If set to a value greater than `0`, forces the audio\'s sample rate to
be reduced to a value lower than or equal to the value specified in
`force/max_rate_hz<class_ResourceImporterWAV_property_force/max_rate_hz>`{.interpreted-text
role="ref"}.

This can decrease file size noticeably on certain sounds, without
impacting quality depending on the actual sound\'s contents. See [Best
practices](../tutorials/assets_pipeline/importing_audio_samples.html#doc-importing-audio-samples-best-practices)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_force/max_rate_hz}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **force/max_rate_hz**
= `44100`
`🔗<class_ResourceImporterWAV_property_force/max_rate_hz>`{.interpreted-text
role="ref"}

The frequency to limit the imported audio sample to (in Hz). Only
effective if
`force/max_rate<class_ResourceImporterWAV_property_force/max_rate>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterWAV_property_force/mono}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force/mono** =
`false`
`🔗<class_ResourceImporterWAV_property_force/mono>`{.interpreted-text
role="ref"}

If `true`, forces the imported audio to be mono if the source file is
stereo. This decreases the file size by 50% by merging the two channels
into one.
