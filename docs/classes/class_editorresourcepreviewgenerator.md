github_url
:   hide

# EditorResourcePreviewGenerator {#class_EditorResourcePreviewGenerator}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Custom generator of previews.

::: rst-class
classref-introduction-group
:::

## Description

Custom code to generate previews. Check
`EditorSettings.filesystem/file_dialog/thumbnail_size<class_EditorSettings_property_filesystem/file_dialog/thumbnail_size>`{.interpreted-text
role="ref"} to find a proper size to generate previews at.

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

:::: {#class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_generate_small_preview**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview>`{.interpreted-text
role="ref"}

If this function returns `true`, the generator will call
`_generate()<class_EditorResourcePreviewGenerator_private_method__generate>`{.interpreted-text
role="ref"} or
`_generate_from_path()<class_EditorResourcePreviewGenerator_private_method__generate_from_path>`{.interpreted-text
role="ref"} for small previews as well.

By default, it returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreviewGenerator_private_method__generate}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\_generate**(resource: `Resource<class_Resource>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, metadata: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePreviewGenerator_private_method__generate>`{.interpreted-text
role="ref"}

Generate a preview from a given resource with the specified size. This
must always be implemented.

Returning `null` is an OK way to fail and let another generator take
care.

Care must be taken because this function is always called from a thread
(not the main thread).

`metadata` dictionary can be modified to store file-specific metadata
that can be used in
`EditorResourceTooltipPlugin._make_tooltip_for_path()<class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path>`{.interpreted-text
role="ref"} (like image size, sample length etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreviewGenerator_private_method__generate_from_path}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\_generate_from_path**(path: `String<class_String>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, metadata: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePreviewGenerator_private_method__generate_from_path>`{.interpreted-text
role="ref"}

Generate a preview directly from a path with the specified size.
Implementing this is optional, as default code will load and call
`_generate()<class_EditorResourcePreviewGenerator_private_method__generate>`{.interpreted-text
role="ref"}.

Returning `null` is an OK way to fail and let another generator take
care.

Care must be taken because this function is always called from a thread
(not the main thread).

`metadata` dictionary can be modified to store file-specific metadata
that can be used in
`EditorResourceTooltipPlugin._make_tooltip_for_path()<class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path>`{.interpreted-text
role="ref"} (like image size, sample length etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_generate_small_preview_automatically**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically>`{.interpreted-text
role="ref"}

If this function returns `true`, the generator will automatically
generate the small previews from the normal preview texture generated by
the methods
`_generate()<class_EditorResourcePreviewGenerator_private_method__generate>`{.interpreted-text
role="ref"} or
`_generate_from_path()<class_EditorResourcePreviewGenerator_private_method__generate_from_path>`{.interpreted-text
role="ref"}.

By default, it returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePreviewGenerator_private_method__handles}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_handles**(type:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePreviewGenerator_private_method__handles>`{.interpreted-text
role="ref"}

Returns `true` if your generator supports the resource of type `type`.
