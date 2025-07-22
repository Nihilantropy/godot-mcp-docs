github_url
:   hide

# EditorResourcePreview {#class_EditorResourcePreview}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node used to generate previews of resources or files.

::: rst-class
classref-introduction-group
:::

## Description

This node is used to generate previews for resources or files.

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_resource_previewer()<class_EditorInterface_method_get_resource_previewer>`{.interpreted-text
role="ref"}.

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

## Signals

:::: {#class_EditorResourcePreview_signal_preview_invalidated}
::: rst-class
classref-signal
:::
::::

**preview_invalidated**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorResourcePreview_signal_preview_invalidated>`{.interpreted-text
role="ref"}

Emitted if a preview was invalidated (changed). `path` corresponds to
the path of the preview.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorResourcePreview_method_add_preview_generator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_preview_generator**(generator:
`EditorResourcePreviewGenerator<class_EditorResourcePreviewGenerator>`{.interpreted-text
role="ref"})
`🔗<class_EditorResourcePreview_method_add_preview_generator>`{.interpreted-text
role="ref"}

Create an own, custom preview generator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreview_method_check_for_invalidation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**check_for_invalidation**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorResourcePreview_method_check_for_invalidation>`{.interpreted-text
role="ref"}

Check if the resource changed, if so, it will be invalidated and the
corresponding signal emitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreview_method_queue_edited_resource_preview}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_edited_resource_preview**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"}, receiver:
`Object<class_Object>`{.interpreted-text role="ref"}, receiver_func:
`StringName<class_StringName>`{.interpreted-text role="ref"}, userdata:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_EditorResourcePreview_method_queue_edited_resource_preview>`{.interpreted-text
role="ref"}

Queue the `resource` being edited for preview. Once the preview is
ready, the `receiver`\'s `receiver_func` will be called. The
`receiver_func` must take the following four arguments:
`String<class_String>`{.interpreted-text role="ref"} path,
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} preview,
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
thumbnail_preview, `Variant<class_Variant>`{.interpreted-text
role="ref"} userdata. `userdata` can be anything, and will be returned
when `receiver_func` is called.

\*\*Note:\*\* If it was not possible to create the preview the
`receiver_func` will still be called, but the preview will be `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreview_method_queue_resource_preview}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_resource_preview**(path:
`String<class_String>`{.interpreted-text role="ref"}, receiver:
`Object<class_Object>`{.interpreted-text role="ref"}, receiver_func:
`StringName<class_StringName>`{.interpreted-text role="ref"}, userdata:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_EditorResourcePreview_method_queue_resource_preview>`{.interpreted-text
role="ref"}

Queue a resource file located at `path` for preview. Once the preview is
ready, the `receiver`\'s `receiver_func` will be called. The
`receiver_func` must take the following four arguments:
`String<class_String>`{.interpreted-text role="ref"} path,
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} preview,
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
thumbnail_preview, `Variant<class_Variant>`{.interpreted-text
role="ref"} userdata. `userdata` can be anything, and will be returned
when `receiver_func` is called.

\*\*Note:\*\* If it was not possible to create the preview the
`receiver_func` will still be called, but the preview will be `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreview_method_remove_preview_generator}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_preview_generator**(generator:
`EditorResourcePreviewGenerator<class_EditorResourcePreviewGenerator>`{.interpreted-text
role="ref"})
`🔗<class_EditorResourcePreview_method_remove_preview_generator>`{.interpreted-text
role="ref"}

Removes a custom preview generator.
