github_url
:   hide

# ResourceSaver {#class_ResourceSaver}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton for saving `Resource<class_Resource>`{.interpreted-text
role="ref"}s to the filesystem.

::: rst-class
classref-introduction-group
:::

## Description

A singleton for saving resource types to the filesystem.

It uses the many
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"} classes registered in the engine (either built-in or from a
plugin) to save resource data to text-based (e.g. `.tres` or `.tscn`) or
binary files (e.g. `.res` or `.scn`).

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

:::: {#enum_ResourceSaver_SaverFlags}
::: rst-class
classref-enumeration
:::
::::

flags **SaverFlags**:
`🔗<enum_ResourceSaver_SaverFlags>`{.interpreted-text role="ref"}

:::: {#class_ResourceSaver_constant_FLAG_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_NONE** = `0`

No resource saving option.

:::: {#class_ResourceSaver_constant_FLAG_RELATIVE_PATHS}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_RELATIVE_PATHS** = `1`

Save the resource with a path relative to the scene which uses it.

:::: {#class_ResourceSaver_constant_FLAG_BUNDLE_RESOURCES}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_BUNDLE_RESOURCES** = `2`

Bundles external resources.

:::: {#class_ResourceSaver_constant_FLAG_CHANGE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_CHANGE_PATH** = `4`

Changes the
`Resource.resource_path<class_Resource_property_resource_path>`{.interpreted-text
role="ref"} of the saved resource to match its new location.

:::: {#class_ResourceSaver_constant_FLAG_OMIT_EDITOR_PROPERTIES}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_OMIT_EDITOR_PROPERTIES** = `8`

Do not save editor-specific metadata (identified by their `__editor`
prefix).

:::: {#class_ResourceSaver_constant_FLAG_SAVE_BIG_ENDIAN}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_SAVE_BIG_ENDIAN** = `16`

Save as big endian (see
`FileAccess.big_endian<class_FileAccess_property_big_endian>`{.interpreted-text
role="ref"}).

:::: {#class_ResourceSaver_constant_FLAG_COMPRESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_COMPRESS** = `32`

Compress the resource on save using
`FileAccess.COMPRESSION_ZSTD<class_FileAccess_constant_COMPRESSION_ZSTD>`{.interpreted-text
role="ref"}. Only available for binary resource types.

:::: {#class_ResourceSaver_constant_FLAG_REPLACE_SUBRESOURCE_PATHS}
::: rst-class
classref-enumeration-constant
:::
::::

`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} **FLAG_REPLACE_SUBRESOURCE_PATHS** = `64`

Take over the paths of the saved subresources (see
`Resource.take_over_path()<class_Resource_method_take_over_path>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ResourceSaver_method_add_resource_format_saver}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_resource_format_saver**(format_saver:
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"}, at_front: `bool<class_bool>`{.interpreted-text role="ref"}
= false)
`🔗<class_ResourceSaver_method_add_resource_format_saver>`{.interpreted-text
role="ref"}

Registers a new
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"}. The ResourceSaver will use the ResourceFormatSaver as
described in `save()<class_ResourceSaver_method_save>`{.interpreted-text
role="ref"}.

This method is performed implicitly for ResourceFormatSavers written in
GDScript (see
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceSaver_method_get_recognized_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_recognized_extensions**(type:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_ResourceSaver_method_get_recognized_extensions>`{.interpreted-text
role="ref"}

Returns the list of extensions available for saving a resource of a
given type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceSaver_method_get_resource_id_for_path}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_resource_id_for_path**(path:
`String<class_String>`{.interpreted-text role="ref"}, generate:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_ResourceSaver_method_get_resource_id_for_path>`{.interpreted-text
role="ref"}

Returns the resource ID for the given path. If `generate` is `true`, a
new resource ID will be generated if one for the path is not found. If
`generate` is `false` and the path is not found,
`ResourceUID.INVALID_ID<class_ResourceUID_constant_INVALID_ID>`{.interpreted-text
role="ref"} is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceSaver_method_remove_resource_format_saver}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_resource_format_saver**(format_saver:
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"})
`🔗<class_ResourceSaver_method_remove_resource_format_saver>`{.interpreted-text
role="ref"}

Unregisters the given
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceSaver_method_save}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save**(resource: `Resource<class_Resource>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"}
= \"\", flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_ResourceSaver_method_save>`{.interpreted-text role="ref"}

Saves a resource to disk to the given path, using a
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"} that recognizes the resource object. If `path` is empty,
**ResourceSaver** will try to use
`Resource.resource_path<class_Resource_property_resource_path>`{.interpreted-text
role="ref"}.

The `flags` bitmask can be specified to customize the save behavior.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success.

\*\*Note:\*\* When the project is running, any generated UID associated
with the resource will not be saved as the required code is only
executed in editor mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceSaver_method_set_uid}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_uid**(resource: `String<class_String>`{.interpreted-text
role="ref"}, uid: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ResourceSaver_method_set_uid>`{.interpreted-text role="ref"}

Sets the UID of the given `resource` path to `uid`. You can generate a
new UID using
`ResourceUID.create_id()<class_ResourceUID_method_create_id>`{.interpreted-text
role="ref"}.

Since resources will normally get a UID automatically, this method is
only useful in very specific cases.
