github_url
:   hide

# AudioStreamPlaybackInteractive {#class_AudioStreamPlaybackInteractive}

**Inherits:**
`AudioStreamPlayback<class_AudioStreamPlayback>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Playback component of
`AudioStreamInteractive<class_AudioStreamInteractive>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Playback component of
`AudioStreamInteractive<class_AudioStreamInteractive>`{.interpreted-text
role="ref"}. Contains functions to change the currently played clip.

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

:::: {#class_AudioStreamPlaybackInteractive_method_get_current_clip_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_current_clip_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioStreamPlaybackInteractive_method_get_current_clip_index>`{.interpreted-text
role="ref"}

Return the index of the currently playing clip. You can use this to get
the name of the currently playing clip with
`AudioStreamInteractive.get_clip_name()<class_AudioStreamInteractive_method_get_clip_name>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Get the currently playing clip name from inside an
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"} node.

:::: tabs
::: code-tab
gdscript

var playing_clip_name =
stream.get_clip_name(get_stream_playback().get_current_clip_index())
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaybackInteractive_method_switch_to_clip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**switch_to_clip**(clip_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AudioStreamPlaybackInteractive_method_switch_to_clip>`{.interpreted-text
role="ref"}

Switch to a clip (by index).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**switch_to_clip_by_name**(clip_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name>`{.interpreted-text
role="ref"}

Switch to a clip (by name).
