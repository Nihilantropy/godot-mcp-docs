github_url
:   hide

# ResourceFormatSaver {#class_ResourceFormatSaver}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Saves a specific resource type to a file.

::: rst-class
classref-introduction-group
:::

## Description

The engine can save resources when you do it from the editor, or when
you use the `ResourceSaver<class_ResourceSaver>`{.interpreted-text
role="ref"} singleton. This is accomplished thanks to multiple
**ResourceFormatSaver**s, each handling its own format and called
automatically by the engine.

By default, Godot saves resources as `.tres` (text-based), `.res`
(binary) or another built-in format, but you can choose to create your
own format by extending this class. Be sure to respect the documented
return types and values. You should give it a global class name with
`class_name` for it to be registered. Like built-in
ResourceFormatSavers, it will be called automatically when saving
resources of its recognized type(s). You may also implement a
`ResourceFormatLoader<class_ResourceFormatLoader>`{.interpreted-text
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

## Method Descriptions

:::: {#class_ResourceFormatSaver_private_method__get_recognized_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_recognized_extensions**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatSaver_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}

Returns the list of extensions available for saving the resource object,
provided it is recognized (see
`_recognize()<class_ResourceFormatSaver_private_method__recognize>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatSaver_private_method__recognize}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_recognize**(resource: `Resource<class_Resource>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatSaver_private_method__recognize>`{.interpreted-text
role="ref"}

Returns whether the given resource object can be saved by this saver.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatSaver_private_method__recognize_path}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_recognize_path**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatSaver_private_method__recognize_path>`{.interpreted-text
role="ref"}

Returns `true` if this saver handles a given save path and `false`
otherwise.

If this method is not implemented, the default behavior returns whether
the path\'s extension is within the ones provided by
`_get_recognized_extensions()<class_ResourceFormatSaver_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatSaver_private_method__save}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_save**(resource: `Resource<class_Resource>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"},
flags: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatSaver_private_method__save>`{.interpreted-text
role="ref"}

Saves the given resource object to a file at the target `path`. `flags`
is a bitmask composed with
`SaverFlags<enum_ResourceSaver_SaverFlags>`{.interpreted-text
role="ref"} constants.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constant
in case of failure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceFormatSaver_private_method__set_uid}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_set_uid**(path: `String<class_String>`{.interpreted-text
role="ref"}, uid: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceFormatSaver_private_method__set_uid>`{.interpreted-text
role="ref"}

Sets a new UID for the resource at the given `path`. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constant
in case of failure.
