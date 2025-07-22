github_url
:   hide

# AudioStreamGeneratorPlayback {#class_AudioStreamGeneratorPlayback}

**Inherits:**
`AudioStreamPlaybackResampled<class_AudioStreamPlaybackResampled>`{.interpreted-text
role="ref"} **\<**
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Plays back audio generated using
`AudioStreamGenerator<class_AudioStreamGenerator>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This class is meant to be used with
`AudioStreamGenerator<class_AudioStreamGenerator>`{.interpreted-text
role="ref"} to play back the generated audio in real-time.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Audio Generator
  Demo](https://godotengine.org/asset-library/asset/2759)
- [Godot 3.2 will get new audio
  features](https://godotengine.org/article/godot-32-will-get-new-audio-features)

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

## Method Descriptions

:::: {#class_AudioStreamGeneratorPlayback_method_can_push_buffer}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**can_push_buffer**(amount: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamGeneratorPlayback_method_can_push_buffer>`{.interpreted-text
role="ref"}

Returns `true` if a buffer of the size `amount` can be pushed to the
audio sample data buffer without overflowing it, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamGeneratorPlayback_method_clear_buffer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_buffer**()
`🔗<class_AudioStreamGeneratorPlayback_method_clear_buffer>`{.interpreted-text
role="ref"}

Clears the audio sample data buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamGeneratorPlayback_method_get_frames_available}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_frames_available**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamGeneratorPlayback_method_get_frames_available>`{.interpreted-text
role="ref"}

Returns the number of frames that can be pushed to the audio sample data
buffer without overflowing it. If the result is `0`, the buffer is full.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamGeneratorPlayback_method_get_skips}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_skips**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamGeneratorPlayback_method_get_skips>`{.interpreted-text
role="ref"}

Returns the number of times the playback skipped due to a buffer
underrun in the audio sample data. This value is reset at the start of
the playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamGeneratorPlayback_method_push_buffer}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_buffer**(frames:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamGeneratorPlayback_method_push_buffer>`{.interpreted-text
role="ref"}

Pushes several audio data frames to the buffer. This is usually more
efficient than
`push_frame()<class_AudioStreamGeneratorPlayback_method_push_frame>`{.interpreted-text
role="ref"} in C# and compiled languages via GDExtension, but
`push_buffer()<class_AudioStreamGeneratorPlayback_method_push_buffer>`{.interpreted-text
role="ref"} may be *less* efficient in GDScript.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamGeneratorPlayback_method_push_frame}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_frame**(frame:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamGeneratorPlayback_method_push_frame>`{.interpreted-text
role="ref"}

Pushes a single audio data frame to the buffer. This is usually less
efficient than
`push_buffer()<class_AudioStreamGeneratorPlayback_method_push_buffer>`{.interpreted-text
role="ref"} in C# and compiled languages via GDExtension, but
`push_frame()<class_AudioStreamGeneratorPlayback_method_push_frame>`{.interpreted-text
role="ref"} may be *more* efficient in GDScript.
