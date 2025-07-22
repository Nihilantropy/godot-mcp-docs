github_url
:   hide

# VideoStream {#class_VideoStream}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VideoStreamTheora<class_VideoStreamTheora>`{.interpreted-text
role="ref"}

Base resource for video streams.

::: rst-class
classref-introduction-group
:::

## Description

Base resource type for all video streams. Classes that derive from
**VideoStream** can all be used as resource types to play back videos in
`VideoStreamPlayer<class_VideoStreamPlayer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Playing videos <../tutorials/animation/playing_videos>`{.interpreted-text
  role="doc"}
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

:::: {#class_VideoStream_property_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **file** = `""`
`🔗<class_VideoStream_property_file>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_file**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_file**()

The video file path or URI that this **VideoStream** resource handles.

For `VideoStreamTheora<class_VideoStreamTheora>`{.interpreted-text
role="ref"}, this filename should be an Ogg Theora video file with the
`.ogv` extension.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VideoStream_private_method__instantiate_playback}
::: rst-class
classref-method
:::
::::

`VideoStreamPlayback<class_VideoStreamPlayback>`{.interpreted-text
role="ref"} **\_instantiate_playback**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_VideoStream_private_method__instantiate_playback>`{.interpreted-text
role="ref"}

Called when the video starts playing, to initialize and return a
subclass of
`VideoStreamPlayback<class_VideoStreamPlayback>`{.interpreted-text
role="ref"}.
