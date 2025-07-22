github_url
:   hide

# ResourceFormatLoader {#class_ResourceFormatLoader}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Loads a specific resource type from a file.

::: rst-class
classref-introduction-group
:::

## Description

Godot loads resources in the editor or in exported games using
ResourceFormatLoaders. They are queried automatically via the
`ResourceLoader<class_ResourceLoader>`{.interpreted-text role="ref"}
singleton, or when a resource with internal dependencies is loaded. Each
file type may load as a different resource type, so multiple
ResourceFormatLoaders are registered in the engine.

Extending this class allows you to define your own loader. Be sure to
respect the documented return types and values. You should give it a
global class name with `class_name` for it to be registered. Like
built-in ResourceFormatLoaders, it will be called automatically when
loading resources of its handled type(s). You may also implement a
`ResourceFormatSaver<class_ResourceFormatSaver>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* You can also extend
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"} if the resource type you need exists but Godot is unable to
load its format. Choosing one way over another depends on if the format
is suitable or not for the final exported game. For example, it\'s
better to import `.png` textures as `.ctex`
(`CompressedTexture2D<class_CompressedTexture2D>`{.interpreted-text
role="ref"}) first, so they can be loaded with better efficiency on the
graphics card.

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

:::: {#enum_ResourceFormatLoader_CacheMode}
::: rst-class
classref-enumeration
:::
::::

enum **CacheMode**:
`🔗<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text role="ref"}

:::: {#class_ResourceFormatLoader_constant_CACHE_MODE_IGNORE}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text
role="ref"} **CACHE_MODE_IGNORE** = `0`

Neither the main resource (the one requested to be loaded) nor any of
its subresources are retrieved from cache nor stored into it.
Dependencies (external resources) are loaded with
`CACHE_MODE_REUSE<class_ResourceFormatLoader_constant_CACHE_MODE_REUSE>`{.interpreted-text
role="ref"}.

:::: {#class_ResourceFormatLoader_constant_CACHE_MODE_REUSE}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text
role="ref"} **CACHE_MODE_REUSE** = `1`

The main resource (the one requested to be loaded), its subresources,
and its dependencies (external resources) are retrieved from cache if
present, instead of loaded. Those not cached are loaded and then stored
into the cache. The same rules are propagated recursively down the tree
of dependencies (external resources).

:::: {#class_ResourceFormatLoader_constant_CACHE_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text
role="ref"} **CACHE_MODE_REPLACE** = `2`

Like
`CACHE_MODE_REUSE<class_ResourceFormatLoader_constant_CACHE_MODE_REUSE>`{.interpreted-text
role="ref"}, but the cache is checked for the main resource (the one
requested to be loaded) as well as for each of its subresources. Those
already in the cache, as long as the loaded and cached types match, have
their data refreshed from storage into the already existing instances.
Otherwise, they are recreated as completely new objects.

:::: {#class_ResourceFormatLoader_constant_CACHE_MODE_IGNORE_DEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text
role="ref"} **CACHE_MODE_IGNORE_DEEP** = `3`

Like
`CACHE_MODE_IGNORE<class_ResourceFormatLoader_constant_CACHE_MODE_IGNORE>`{.interpreted-text
role="ref"}, but propagated recursively down the tree of dependencies
(external resources).

:::: {#class_ResourceFormatLoader_constant_CACHE_MODE_REPLACE_DEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`CacheMode<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text
role="ref"} **CACHE_MODE_REPLACE_DEEP** = `4`

Like
`CACHE_MODE_REPLACE<class_ResourceFormatLoader_constant_CACHE_MODE_REPLACE>`{.interpreted-text
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

:::: {#class_ResourceFormatLoader_private_method__exists}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_exists**(path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__exists>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__get_classes_used}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_classes_used**(path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__get_classes_used>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__get_dependencies}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_dependencies**(path:
`String<class_String>`{.interpreted-text role="ref"}, add_types:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__get_dependencies>`{.interpreted-text
role="ref"}

Should return the dependencies for the resource at the given `path`.
Each dependency is a string composed of one to three sections separated
by `::`, with trailing empty sections omitted:

- The first section should contain the UID if the resource has one.
  Otherwise, it should contain the file path.
- The second section should contain the class name of the dependency if
  `add_types` is `true`. Otherwise, it should be empty.
- The third section should contain the fallback path if the resource has
  a UID. Otherwise, it should be empty.

<!-- -->

    func _get_dependencies(path, add_types):
        return [
            "uid://fqgvuwrkuixh::Script::res://script.gd",
            "uid://fqgvuwrkuixh::::res://script.gd",
            "res://script.gd::Script",
            "res://script.gd",
        ]

\*\*Note:\*\* Custom resource types defined by scripts aren\'t known by
the `ClassDB<class_ClassDB>`{.interpreted-text role="ref"}, so
`"Resource"` can be used for the class name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__get_recognized_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_recognized_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}

Gets the list of extensions for files this loader is able to read.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__get_resource_script_class}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_resource_script_class**(path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__get_resource_script_class>`{.interpreted-text
role="ref"}

Returns the script class name associated with the
`Resource<class_Resource>`{.interpreted-text role="ref"} under the given
`path`. If the resource has no script or the script isn\'t a named
class, it should return `""`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__get_resource_type}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_resource_type**(path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__get_resource_type>`{.interpreted-text
role="ref"}

Gets the class name of the resource associated with the given path. If
the loader cannot handle it, it should return `""`.

\*\*Note:\*\* Custom resource types defined by scripts aren\'t known by
the `ClassDB<class_ClassDB>`{.interpreted-text role="ref"}, so you might
just return `"Resource"` for them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__get_resource_uid}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_resource_uid**(path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__get_resource_uid>`{.interpreted-text
role="ref"}

Should return the unique ID for the resource associated with the given
path. If this method is not overridden, a `.uid` file is generated along
with the resource file, containing the unique ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__handles_type}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_handles_type**(type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__handles_type>`{.interpreted-text
role="ref"}

Tells which resource class this loader can load.

\*\*Note:\*\* Custom resource types defined by scripts aren\'t known by
the `ClassDB<class_ClassDB>`{.interpreted-text role="ref"}, so you might
just handle `"Resource"` for them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__load}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **\_load**(path:
`String<class_String>`{.interpreted-text role="ref"}, original_path:
`String<class_String>`{.interpreted-text role="ref"}, use_sub_threads:
`bool<class_bool>`{.interpreted-text role="ref"}, cache_mode:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__load>`{.interpreted-text
role="ref"}

Loads a resource when the engine finds this loader to be compatible. If
the loaded resource is the result of an import, `original_path` will
target the source file. Returns a
`Resource<class_Resource>`{.interpreted-text role="ref"} object on
success, or an `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} constant in case of failure.

The `cache_mode` property defines whether and how the cache should be
used or updated when loading the resource. See
`CacheMode<enum_ResourceFormatLoader_CacheMode>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__recognize_path}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_recognize_path**(path: `String<class_String>`{.interpreted-text
role="ref"}, type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__recognize_path>`{.interpreted-text
role="ref"}

Tells whether or not this loader should load a resource from its
resource path for a given type.

If it is not implemented, the default behavior returns whether the
path\'s extension is within the ones provided by
`_get_recognized_extensions()<class_ResourceFormatLoader_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}, and if the type is within the ones provided by
`_get_resource_type()<class_ResourceFormatLoader_private_method__get_resource_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatLoader_private_method__rename_dependencies}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_rename_dependencies**(path: `String<class_String>`{.interpreted-text
role="ref"}, renames: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatLoader_private_method__rename_dependencies>`{.interpreted-text
role="ref"}

If implemented, renames dependencies within the given resource and saves
it. `renames` is a dictionary `{ String => String }` mapping old
dependency paths to new paths.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constant
in case of failure.
