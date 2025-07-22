github_url
:   hide

# AudioEffectRecord {#class_AudioEffectRecord}

**Inherits:** `AudioEffect<class_AudioEffect>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Audio effect used for recording the sound from an audio bus.

::: rst-class
classref-introduction-group
:::

## Description

Allows the user to record the sound from an audio bus into an
`AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text role="ref"}.
When used on the \"Master\" audio bus, this includes all audio output by
Godot.

Unlike `AudioEffectCapture<class_AudioEffectCapture>`{.interpreted-text
role="ref"}, this effect encodes the recording with the given format
(8-bit, 16-bit, or compressed) instead of giving access to the raw audio
samples.

Can be used (with an
`AudioStreamMicrophone<class_AudioStreamMicrophone>`{.interpreted-text
role="ref"}) to record from a microphone.

\*\*Note:\*\*
`ProjectSettings.audio/driver/enable_input<class_ProjectSettings_property_audio/driver/enable_input>`{.interpreted-text
role="ref"} must be `true` for audio input to work. See also that
setting\'s description for caveats related to permissions and operating
system privacy settings.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Recording with microphone <../tutorials/audio/recording_with_microphone>`{.interpreted-text
  role="doc"}
- [Audio Microphone Record
  Demo](https://godotengine.org/asset-library/asset/2760)

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

:::: {#class_AudioEffectRecord_property_format}
::: rst-class
classref-property
:::
::::

`Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
**format** = `1`
`🔗<class_AudioEffectRecord_property_format>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_format**(value:
  `Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"})
- `Format<enum_AudioStreamWAV_Format>`{.interpreted-text role="ref"}
  **get_format**()

Specifies the format in which the sample will be recorded.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AudioEffectRecord_method_get_recording}
::: rst-class
classref-method
:::
::::

`AudioStreamWAV<class_AudioStreamWAV>`{.interpreted-text role="ref"}
**get_recording**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectRecord_method_get_recording>`{.interpreted-text
role="ref"}

Returns the recorded sample.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectRecord_method_is_recording_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_recording_active**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectRecord_method_is_recording_active>`{.interpreted-text
role="ref"}

Returns whether the recording is active or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectRecord_method_set_recording_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_recording_active**(record: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_AudioEffectRecord_method_set_recording_active>`{.interpreted-text
role="ref"}

If `true`, the sound will be recorded. Note that restarting the
recording will remove the previously recorded sample.
