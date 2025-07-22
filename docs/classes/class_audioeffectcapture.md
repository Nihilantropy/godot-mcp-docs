github_url
:   hide

# AudioEffectCapture {#class_AudioEffectCapture}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Captures audio from an audio bus in real-time.

::: rst-class
classref-introduction-group
:::

## Description

AudioEffectCapture is an AudioEffect which copies all audio frames from
the attached audio effect bus into its internal ring buffer.

Application code should consume these audio frames from this ring buffer
using
`get_buffer()<class_AudioEffectCapture_method_get_buffer>`{.interpreted-text
role="ref"} and process it as needed, for example to capture data from
an
`AudioStreamMicrophone<class_AudioStreamMicrophone>`{.interpreted-text
role="ref"}, implement application-defined effects, or to transmit audio
over the network. When capturing audio data from a microphone, the
format of the samples will be stereo 32-bit floating-point PCM.

Unlike `AudioEffectRecord<class_AudioEffectRecord>`{.interpreted-text
role="ref"}, this effect only returns the raw audio samples instead of
encoding them into an `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
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

:::: {#class_AudioEffectCapture_property_buffer_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **buffer_length** =
`0.1`
`🔗<class_AudioEffectCapture_property_buffer_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffer_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_buffer_length**()

Length of the internal ring buffer, in seconds. Setting the buffer
length will have no effect if already initialized.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioEffectCapture_method_can_get_buffer}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**can_get_buffer**(frames: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectCapture_method_can_get_buffer>`{.interpreted-text
role="ref"}

Returns `true` if at least `frames` audio frames are available to read
in the internal ring buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCapture_method_clear_buffer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_buffer**()
`🔗<class_AudioEffectCapture_method_clear_buffer>`{.interpreted-text
role="ref"}

Clears the internal ring buffer.

\*\*Note:\*\* Calling this during a capture can cause the loss of
samples which causes popping in the playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCapture_method_get_buffer}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_buffer**(frames: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectCapture_method_get_buffer>`{.interpreted-text
role="ref"}

Gets the next `frames` audio samples from the internal ring buffer.

Returns a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} containing exactly `frames` audio samples if available, or
an empty
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} if insufficient data was available.

The samples are signed floating-point PCM between `-1` and `1`. You will
have to scale them if you want to use them as 8 or 16-bit integer
samples. (`v = 0x7fff * samples[0].x`)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCapture_method_get_buffer_length_frames}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_buffer_length_frames**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectCapture_method_get_buffer_length_frames>`{.interpreted-text
role="ref"}

Returns the total size of the internal ring buffer in frames.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCapture_method_get_discarded_frames}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_discarded_frames**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectCapture_method_get_discarded_frames>`{.interpreted-text
role="ref"}

Returns the number of audio frames discarded from the audio bus due to
full buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCapture_method_get_frames_available}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_frames_available**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectCapture_method_get_frames_available>`{.interpreted-text
role="ref"}

Returns the number of frames available to read using
`get_buffer()<class_AudioEffectCapture_method_get_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectCapture_method_get_pushed_frames}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_pushed_frames**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectCapture_method_get_pushed_frames>`{.interpreted-text
role="ref"}

Returns the number of audio frames inserted from the audio bus.
