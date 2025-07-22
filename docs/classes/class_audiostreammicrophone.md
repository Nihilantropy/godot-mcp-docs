github_url
:   hide

# AudioStreamMicrophone {#class_AudioStreamMicrophone}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Plays real-time audio input data.

::: rst-class
classref-introduction-group
:::

## Description

When used directly in an
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"} node, **AudioStreamMicrophone** plays back microphone input
in real-time. This can be used in conjunction with
`AudioEffectCapture<class_AudioEffectCapture>`{.interpreted-text
role="ref"} to process the data or save it.

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
- [Audio Mic Record
  Demo](https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record)
