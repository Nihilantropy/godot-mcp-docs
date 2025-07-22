github_url
:   hide

# EditorFileSystemImportFormatSupportQuery {#class_EditorFileSystemImportFormatSupportQuery}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Used to query and configure import format support.

::: rst-class
classref-introduction-group
:::

## Description

This class is used to query and configure a certain import format. It is
used in conjunction with asset format import plugins.

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

:::: {#class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_file_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions>`{.interpreted-text
role="ref"}

Return the file extensions supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemImportFormatSupportQuery_private_method__is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_active**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemImportFormatSupportQuery_private_method__is_active>`{.interpreted-text
role="ref"}

Return whether this importer is active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemImportFormatSupportQuery_private_method__query}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_query**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemImportFormatSupportQuery_private_method__query>`{.interpreted-text
role="ref"}

Query support. Return `false` if import must not continue.
