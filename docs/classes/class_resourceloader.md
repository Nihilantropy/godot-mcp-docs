github_url
:   hide

# ResourceLoader {#class_ResourceLoader}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton for loading resource files.

::: rst-class
classref-introduction-group
:::

## Description

A singleton used to load resource files from the filesystem.

It uses the many
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"} classes registered in the engine (either built-in or from a
plugin) to load files into memory and convert them to a format that can
be used by the engine.

\*\*Note:\*\* You have to import the files into the engine first to load
them using `load()<class_ResourceLoader_method_load>`{.interpreted-text
role="ref"}. If you want to load `Image<class_Image>`{.interpreted-text
role="ref"}s at run-time, you may use
`Image.load()<class_Image_method_load>`{.interpreted-text role="ref"}.
If you want to import audio files, you can use the snippet described in
`AudioStreamMP3.data<class_AudioStreamMP3_property_data>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Non-resource files such as plain text files cannot be read
using **ResourceLoader**. Use
`FileAccess<class_FileAccess>`{.interpreted-text role="ref"} for those
files instead, and be aware that non-resource files are not exported by
default (see notes in the
`FileAccess<class_FileAccess>`{.interpreted-text role="ref"} class
description for instructions on exporting them).

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Operating System Testing
  Demo](https://godotengine.org/asset-library/asset/2789)

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

:::: {#enum_ResourceLoader_ThreadLoadStatus}
::: rst-class
classref-enumeration
:::
::::

enum **ThreadLoadStatus**:
`🔗<enum_ResourceLoader_ThreadLoadStatus>`{.interpreted-text role="ref"}

:::: {#class_ResourceLoader_constant_THREAD_LOAD_INVALID_RESOURCE}
::: rst-class
classref-enumeration-constant
:::
::::

`ThreadLoadStatus<enum_ResourceLoader_ThreadLoadStatus>`{.interpreted-text
role="ref"} **THREAD_LOAD_INVALID_RESOURCE** = `0`

The resource is invalid, or has not been loaded with
`load_threaded_request()<class_ResourceLoader_method_load_threaded_request>`{.interpreted-text
role="ref"}.

:::: {#class_ResourceLoader_constant_THREAD_LOAD_IN_PROGRESS}
::: rst-class
classref-enumeration-constant
:::
::::

`ThreadLoadStatus<enum_ResourceLoader_ThreadLoadStatus>`{.interpreted-text
role="ref"} **THREAD_LOAD_IN_PROGRESS** = `1`

The resource is still being loaded.

:::: {#class_ResourceLoader_constant_THREAD_LOAD_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`ThreadLoadStatus<enum_ResourceLoader_ThreadLoadStatus>`{.interpreted-text
role="ref"} **THREAD_LOAD_FAILED** = `2`

Some error occurred during loading and it failed.

:::: {#class_ResourceLoader_constant_THREAD_LOAD_LOADED}
::: rst-class
classref-enumeration-constant
:::
::::

`ThreadLoadStatus<enum_ResourceLoader_ThreadLoadStatus>`{.interpreted-text
role="ref"} **THREAD_LOAD_LOADED** = `3`

The resource was loaded successfully and can be accessed via
`load_threaded_get()<class_ResourceLoader_method_load_threaded_get>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ResourceLoader_CacheMode}
::: rst-class
classref-enumeration
:::
::::

enum **CacheMode**:
`🔗<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}

:::: {#class_ResourceLoader_constant_CACHE_MODE_IGNORE}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
**CACHE_MODE_IGNORE** = `0`

Neither the main resource (the one requested to be loaded) nor any of
its subresources are retrieved from cache nor stored into it.
Dependencies (external resources) are loaded with
`CACHE_MODE_REUSE<class_ResourceLoader_constant_CACHE_MODE_REUSE>`{.interpreted-text
role="ref"}.

:::: {#class_ResourceLoader_constant_CACHE_MODE_REUSE}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
**CACHE_MODE_REUSE** = `1`

The main resource (the one requested to be loaded), its subresources,
and its dependencies (external resources) are retrieved from cache if
present, instead of loaded. Those not cached are loaded and then stored
into the cache. The same rules are propagated recursively down the tree
of dependencies (external resources).

:::: {#class_ResourceLoader_constant_CACHE_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
**CACHE_MODE_REPLACE** = `2`

Like
`CACHE_MODE_REUSE<class_ResourceLoader_constant_CACHE_MODE_REUSE>`{.interpreted-text
role="ref"}, but the cache is checked for the main resource (the one
requested to be loaded) as well as for each of its subresources. Those
already in the cache, as long as the loaded and cached types match, have
their data refreshed from storage into the already existing instances.
Otherwise, they are recreated as completely new objects.

:::: {#class_ResourceLoader_constant_CACHE_MODE_IGNORE_DEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
**CACHE_MODE_IGNORE_DEEP** = `3`

Like
`CACHE_MODE_IGNORE<class_ResourceLoader_constant_CACHE_MODE_IGNORE>`{.interpreted-text
role="ref"}, but propagated recursively down the tree of dependencies
(external resources).

:::: {#class_ResourceLoader_constant_CACHE_MODE_REPLACE_DEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
**CACHE_MODE_REPLACE_DEEP** = `4`

Like
`CACHE_MODE_REPLACE<class_ResourceLoader_constant_CACHE_MODE_REPLACE>`{.interpreted-text
role="ref"}, but propagated recursively down the tree of dependencies
(external resources).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ResourceLoader_method_add_resource_format_loader}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_resource_format_loader**(format_loader:
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"}, at_front: `bool<class_bool>`{.interpreted-text role="ref"}
= false)
`🔗<class_ResourceLoader_method_add_resource_format_loader>`{.interpreted-text
role="ref"}

Registers a new
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"}. The ResourceLoader will use the ResourceFormatLoader as
described in
`load()<class_ResourceLoader_method_load>`{.interpreted-text
role="ref"}.

This method is performed implicitly for ResourceFormatLoaders written in
GDScript (see
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_exists}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **exists**(path:
`String<class_String>`{.interpreted-text role="ref"}, type_hint:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_ResourceLoader_method_exists>`{.interpreted-text role="ref"}

Returns whether a recognized resource exists for the given `path`.

An optional `type_hint` can be used to further specify the
`Resource<class_Resource>`{.interpreted-text role="ref"} type that
should be handled by the
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"}. Anything that inherits from
`Resource<class_Resource>`{.interpreted-text role="ref"} can be used as
a type hint, for example `Image<class_Image>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If you use
`Resource.take_over_path()<class_Resource_method_take_over_path>`{.interpreted-text
role="ref"}, this method will return `true` for the taken path even if
the resource wasn\'t saved (i.e. exists only in resource cache).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_get_cached_ref}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**get_cached_ref**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ResourceLoader_method_get_cached_ref>`{.interpreted-text
role="ref"}

Returns the cached resource reference for the given `path`.

\*\*Note:\*\* If the resource is not cached, the returned
`Resource<class_Resource>`{.interpreted-text role="ref"} will be
invalid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_get_dependencies}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_dependencies**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ResourceLoader_method_get_dependencies>`{.interpreted-text
role="ref"}

Returns the dependencies for the resource at the given `path`.

Each dependency is a string that can be divided into sections by `::`.
There can be either one section or three sections, with the second
section always being empty. When there is one section, it contains the
file path. When there are three sections, the first section contains the
UID and the third section contains the fallback path.

    for dependency in ResourceLoader.get_dependencies(path):
        if dependency.contains("::"):
            print(dependency.get_slice("::", 0)) # Prints the UID.
            print(dependency.get_slice("::", 2)) # Prints the fallback path.
        else:
            print(dependency) # Prints the path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_get_recognized_extensions_for_type}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_recognized_extensions_for_type**(type:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ResourceLoader_method_get_recognized_extensions_for_type>`{.interpreted-text
role="ref"}

Returns the list of recognized extensions for a resource type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_get_resource_uid}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_resource_uid**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ResourceLoader_method_get_resource_uid>`{.interpreted-text
role="ref"}

Returns the ID associated with a given resource path, or `-1` when no
such ID exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_has_cached}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_cached**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ResourceLoader_method_has_cached>`{.interpreted-text
role="ref"}

Returns whether a cached resource is available for the given `path`.

Once a resource has been loaded by the engine, it is cached in memory
for faster access, and future calls to the
`load()<class_ResourceLoader_method_load>`{.interpreted-text role="ref"}
method will use the cached version. The cached resource can be
overridden by using
`Resource.take_over_path()<class_Resource_method_take_over_path>`{.interpreted-text
role="ref"} on a new resource for that same path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_list_directory}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **list_directory**(directory_path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ResourceLoader_method_list_directory>`{.interpreted-text
role="ref"}

Lists a directory, returning all resources and subdirectories contained
within. The resource files have the original file names as visible in
the editor before exporting. The directories have `"/"` appended.

    # Prints ["extra_data/", "model.gltf", "model.tscn", "model_slime.png"]
    print(ResourceLoader.list_directory("res://assets/enemies/slime"))

\*\*Note:\*\* The order of files and directories returned by this method
is not deterministic, and can vary between operating systems.

\*\*Note:\*\* To normally traverse the filesystem, see
`DirAccess<class_DirAccess>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_load}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"} **load**(path:
`String<class_String>`{.interpreted-text role="ref"}, type_hint:
`String<class_String>`{.interpreted-text role="ref"} = \"\", cache_mode:
`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
= 1) `🔗<class_ResourceLoader_method_load>`{.interpreted-text
role="ref"}

Loads a resource at the given `path`, caching the result for further
access.

The registered
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"}s are queried sequentially to find the first one which can
handle the file\'s extension, and then attempt loading. If loading
fails, the remaining ResourceFormatLoaders are also attempted.

An optional `type_hint` can be used to further specify the
`Resource<class_Resource>`{.interpreted-text role="ref"} type that
should be handled by the
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"}. Anything that inherits from
`Resource<class_Resource>`{.interpreted-text role="ref"} can be used as
a type hint, for example `Image<class_Image>`{.interpreted-text
role="ref"}.

The `cache_mode` property defines whether and how the cache should be
used or updated when loading the resource.

Returns an empty resource if no
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"} could handle the file, and prints an error if no file is
found at the specified path.

GDScript has a simplified
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"} built-in method which can be used in most situations,
leaving the use of **ResourceLoader** for more advanced scenarios.

\*\*Note:\*\* If
`ProjectSettings.editor/export/convert_text_resources_to_binary<class_ProjectSettings_property_editor/export/convert_text_resources_to_binary>`{.interpreted-text
role="ref"} is `true`,
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"} will not be able to read converted files in an exported
project. If you rely on run-time loading of files present within the
PCK, set
`ProjectSettings.editor/export/convert_text_resources_to_binary<class_ProjectSettings_property_editor/export/convert_text_resources_to_binary>`{.interpreted-text
role="ref"} to `false`.

\*\*Note:\*\* Relative paths will be prefixed with `"res://"` before
loading, to avoid unexpected results make sure your paths are absolute.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_load_threaded_get}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**load_threaded_get**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ResourceLoader_method_load_threaded_get>`{.interpreted-text
role="ref"}

Returns the resource loaded by
`load_threaded_request()<class_ResourceLoader_method_load_threaded_request>`{.interpreted-text
role="ref"}.

If this is called before the loading thread is done (i.e.
`load_threaded_get_status()<class_ResourceLoader_method_load_threaded_get_status>`{.interpreted-text
role="ref"} is not
`THREAD_LOAD_LOADED<class_ResourceLoader_constant_THREAD_LOAD_LOADED>`{.interpreted-text
role="ref"}), the calling thread will be blocked until the resource has
finished loading. However, it\'s recommended to use
`load_threaded_get_status()<class_ResourceLoader_method_load_threaded_get_status>`{.interpreted-text
role="ref"} to known when the load has actually completed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_load_threaded_get_status}
::: rst-class
classref-method
:::
::::

`ThreadLoadStatus<enum_ResourceLoader_ThreadLoadStatus>`{.interpreted-text
role="ref"} **load_threaded_get_status**(path:
`String<class_String>`{.interpreted-text role="ref"}, progress:
`Array<class_Array>`{.interpreted-text role="ref"} = \[\])
`🔗<class_ResourceLoader_method_load_threaded_get_status>`{.interpreted-text
role="ref"}

Returns the status of a threaded loading operation started with
`load_threaded_request()<class_ResourceLoader_method_load_threaded_request>`{.interpreted-text
role="ref"} for the resource at `path`.

An array variable can optionally be passed via `progress`, and will
return a one-element array containing the ratio of completion of the
threaded loading (between `0.0` and `1.0`).

\*\*Note:\*\* The recommended way of using this method is to call it
during different frames (e.g., in
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, instead of a loop).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_load_threaded_request}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_threaded_request**(path: `String<class_String>`{.interpreted-text
role="ref"}, type_hint: `String<class_String>`{.interpreted-text
role="ref"} = \"\", use_sub_threads:
`bool<class_bool>`{.interpreted-text role="ref"} = false, cache_mode:
`CacheMode<enum_ResourceLoader_CacheMode>`{.interpreted-text role="ref"}
= 1)
`🔗<class_ResourceLoader_method_load_threaded_request>`{.interpreted-text
role="ref"}

Loads the resource using threads. If `use_sub_threads` is `true`,
multiple threads will be used to load the resource, which makes loading
faster, but may affect the main thread (and thus cause game slowdowns).

The `cache_mode` parameter defines whether and how the cache should be
used or updated when loading the resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_remove_resource_format_loader}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_resource_format_loader**(format_loader:
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"})
`🔗<class_ResourceLoader_method_remove_resource_format_loader>`{.interpreted-text
role="ref"}

Unregisters the given
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceLoader_method_set_abort_on_missing_resources}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_abort_on_missing_resources**(abort:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ResourceLoader_method_set_abort_on_missing_resources>`{.interpreted-text
role="ref"}

Changes the behavior on missing sub-resources. The default behavior is
to abort loading.
