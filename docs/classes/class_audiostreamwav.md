github_url
:   hide

# AudioStreamWAV {#class_AudioStreamWAV}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Stores audio data loaded from WAV files.

::: rst-class
classref-introduction-group
:::

## Description

AudioStreamWAV stores sound samples loaded from WAV files. To play the
stored sound, use an
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"} (for non-positional audio) or
`AudioStreamPlayer2D<class_AudioStreamPlayer2D>`{.interpreted-text
role="ref"}/`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"} (for positional audio). The sound can be looped.

This class can also be used to store dynamically-generated PCM audio
data. See also
`AudioStreamGenerator<class_AudioStreamGenerator>`{.interpreted-text
role="ref"} for procedural audio generation.

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

## Enumerations

:::: {#enum_AudioStreamWAV_Format}
::: rst-class
classref-enumeration
:::
::::

enum **Format**: `🔗<enum_AudioStreamWAV_Format>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamWAV_constant_FORMAT_8_BITS}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
**FORMAT_8_BITS** = `0`

8-bit PCM audio codec.

:::: {#class_AudioStreamWAV_constant_FORMAT_16_BITS}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
**FORMAT_16_BITS** = `1`

16-bit PCM audio codec.

:::: {#class_AudioStreamWAV_constant_FORMAT_IMA_ADPCM}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
**FORMAT_IMA_ADPCM** = `2`

Audio is lossily compressed as IMA ADPCM.

:::: {#class_AudioStreamWAV_constant_FORMAT_QOA}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
**FORMAT_QOA** = `3`

Audio is lossily compressed as [Quite OK Audio](https://qoaformat.org/).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AudioStreamWAV_LoopMode}
::: rst-class
classref-enumeration
:::
::::

enum **LoopMode**: `🔗<enum_AudioStreamWAV_LoopMode>`{.interpreted-text
role="ref"}

:::: {#class_AudioStreamWAV_constant_LOOP_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text role="ref"}
**LOOP_DISABLED** = `0`

Audio does not loop.

:::: {#class_AudioStreamWAV_constant_LOOP_FORWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text role="ref"}
**LOOP_FORWARD** = `1`

Audio loops the data between
`loop_begin<class_AudioStreamWAV_property_loop_begin>`{.interpreted-text
role="ref"} and
`loop_end<class_AudioStreamWAV_property_loop_end>`{.interpreted-text
role="ref"}, playing forward only.

:::: {#class_AudioStreamWAV_constant_LOOP_PINGPONG}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text role="ref"}
**LOOP_PINGPONG** = `2`

Audio loops the data between
`loop_begin<class_AudioStreamWAV_property_loop_begin>`{.interpreted-text
role="ref"} and
`loop_end<class_AudioStreamWAV_property_loop_end>`{.interpreted-text
role="ref"}, playing back and forth.

:::: {#class_AudioStreamWAV_constant_LOOP_BACKWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text role="ref"}
**LOOP_BACKWARD** = `3`

Audio loops the data between
`loop_begin<class_AudioStreamWAV_property_loop_begin>`{.interpreted-text
role="ref"} and
`loop_end<class_AudioStreamWAV_property_loop_end>`{.interpreted-text
role="ref"}, playing backward only.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamWAV_property_data}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**data** = `PackedByteArray()`
`🔗<class_AudioStreamWAV_property_data>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_data**(value:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_data**()

Contains the audio data in bytes.

\*\*Note:\*\* If
`format<class_AudioStreamWAV_property_format>`{.interpreted-text
role="ref"} is set to
`FORMAT_8_BITS<class_AudioStreamWAV_constant_FORMAT_8_BITS>`{.interpreted-text
role="ref"}, this property expects signed 8-bit PCM data. To convert
from unsigned 8-bit PCM, subtract 128 from each byte.

\*\*Note:\*\* If
`format<class_AudioStreamWAV_property_format>`{.interpreted-text
role="ref"} is set to
`FORMAT_QOA<class_AudioStreamWAV_constant_FORMAT_QOA>`{.interpreted-text
role="ref"}, this property expects data from a full QOA file.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_format}
::: rst-class
classref-property
:::
::::

`Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
**format** = `0`
`🔗<class_AudioStreamWAV_property_format>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_format**(value:
  `Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"})
- `Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
  **get_format**()

Audio format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_loop_begin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **loop_begin** = `0`
`🔗<class_AudioStreamWAV_property_loop_begin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_begin**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_loop_begin**()

The loop start point (in number of samples, relative to the beginning of
the stream).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_loop_end}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **loop_end** = `0`
`🔗<class_AudioStreamWAV_property_loop_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_end**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_loop_end**()

The loop end point (in number of samples, relative to the beginning of
the stream).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_loop_mode}
::: rst-class
classref-property
:::
::::

`LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text role="ref"}
**loop_mode** = `0`
`🔗<class_AudioStreamWAV_property_loop_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_mode**(value:
  `LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text
  role="ref"})
- `LoopMode<enum_AudioStreamWAV_LoopMode>`{.interpreted-text role="ref"}
  **get_loop_mode**()

The loop mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_mix_rate}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mix_rate** = `44100`
`🔗<class_AudioStreamWAV_property_mix_rate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mix_rate**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_mix_rate**()

The sample rate for mixing this audio. Higher values require more
storage space, but result in better quality.

In games, common sample rates in use are `11025`, `16000`, `22050`,
`32000`, `44100`, and `48000`.

According to the [Nyquist-Shannon sampling
theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem),
there is no quality difference to human hearing when going past 40,000
Hz (since most humans can only hear up to \~20,000 Hz, often less). If
you are using lower-pitched sounds such as voices, lower sample rates
such as `32000` or `22050` may be usable with no loss in quality.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_stereo}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **stereo** = `false`
`🔗<class_AudioStreamWAV_property_stereo>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stereo**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_stereo**()

If `true`, audio is stereo.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_property_tags}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} **tags** =
`{}` `🔗<class_AudioStreamWAV_property_tags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tags**(value: `Dictionary<class_Dictionary>`{.interpreted-text
  role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_tags**()

Contains user-defined tags if found in the WAV data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`,
and `date` (`date` does not have a standard date format).

\*\*Note:\*\* No tag is *guaranteed* to be present in every file, so
make sure to account for the keys not always existing.

\*\*Note:\*\* Only WAV files using a `LIST` chunk with an identifier of
`INFO` to encode the tags are currently supported.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioStreamWAV_method_load_from_buffer}
::: rst-class
classref-method
:::
::::

`AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text role="ref"}
**load_from_buffer**(stream_data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
options: `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} =
{})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamWAV_method_load_from_buffer>`{.interpreted-text
role="ref"}

Creates a new **AudioStreamWAV** instance from the given buffer. The
buffer must contain WAV data.

The keys and values of `options` match the properties of
`ResourceImporterWAV<class_ResourceImporterWAV>`{.interpreted-text
role="ref"}. The usage of `options` is identical to
`load_from_file()<class_AudioStreamWAV_method_load_from_file>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_method_load_from_file}
::: rst-class
classref-method
:::
::::

`AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text role="ref"}
**load_from_file**(path: `String<class_String>`{.interpreted-text
role="ref"}, options: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} = {})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamWAV_method_load_from_file>`{.interpreted-text
role="ref"}

Creates a new **AudioStreamWAV** instance from the given file path. The
file must be in WAV format.

The keys and values of `options` match the properties of
`ResourceImporterWAV<class_ResourceImporterWAV>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Load the first file dropped as a WAV and play it:

    @onready var audio_player = $AudioStreamPlayer

    func _ready():
        get_window().files_dropped.connect(_on_files_dropped)

    func _on_files_dropped(files):
        if files[0].get_extension() == "wav":
            audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                    "force/max_rate": true,
                    "force/max_rate_hz": 11025
                })
            audio_player.play()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamWAV_method_save_to_wav}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_to_wav**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamWAV_method_save_to_wav>`{.interpreted-text
role="ref"}

Saves the AudioStreamWAV as a WAV file to `path`. Samples with IMA ADPCM
or Quite OK Audio formats can\'t be saved.

\*\*Note:\*\* A `.wav` extension is automatically appended to `path` if
it is missing.
