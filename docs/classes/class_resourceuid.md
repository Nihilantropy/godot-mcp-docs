github_url
:   hide

# ResourceUID {#class_ResourceUID}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton that manages the unique identifiers of all resources within
a project.

::: rst-class
classref-introduction-group
:::

## Description

Resource UIDs (Unique IDentifiers) allow the engine to keep references
between resources intact, even if files are renamed or moved. They can
be accessed with `uid://`.

\*\*ResourceUID\*\* keeps track of all registered resource UIDs in a
project, generates new UIDs, and converts between their string and
integer representations.

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

## Constants

:::: {#class_ResourceUID_constant_INVALID_ID}
::: rst-class
classref-constant
:::
::::

**INVALID_ID** = `-1`
`🔗<class_ResourceUID_constant_INVALID_ID>`{.interpreted-text
role="ref"}

The value to use for an invalid UID, for example if the resource could
not be loaded.

Its text representation is `uid://<invalid>`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ResourceUID_method_add_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **add_id**(id:
`int<class_int>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ResourceUID_method_add_id>`{.interpreted-text role="ref"}

Adds a new UID value which is mapped to the given resource path.

Fails with an error if the UID already exists, so be sure to check
`has_id()<class_ResourceUID_method_has_id>`{.interpreted-text
role="ref"} beforehand, or use
`set_id()<class_ResourceUID_method_set_id>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_create_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **create_id**()
`🔗<class_ResourceUID_method_create_id>`{.interpreted-text role="ref"}

Generates a random resource UID which is guaranteed to be unique within
the list of currently loaded UIDs.

In order for this UID to be registered, you must call
`add_id()<class_ResourceUID_method_add_id>`{.interpreted-text
role="ref"} or
`set_id()<class_ResourceUID_method_set_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_create_id_for_path}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**create_id_for_path**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ResourceUID_method_create_id_for_path>`{.interpreted-text
role="ref"}

Like `create_id()<class_ResourceUID_method_create_id>`{.interpreted-text
role="ref"}, but the UID is seeded with the provided `path` and project
name. UIDs generated for that path will be always the same within the
current project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_ensure_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ensure_path**(path_or_uid: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceUID_method_ensure_path>`{.interpreted-text role="ref"}

Returns a path, converting `path_or_uid` if necessary. Prints an error
if provided an invalid UID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_get_id_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_id_path**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceUID_method_get_id_path>`{.interpreted-text role="ref"}

Returns the path that the given UID value refers to.

Fails with an error if the UID does not exist, so be sure to check
`has_id()<class_ResourceUID_method_has_id>`{.interpreted-text
role="ref"} beforehand.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_has_id}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_id**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ResourceUID_method_has_id>`{.interpreted-text
role="ref"}

Returns whether the given UID value is known to the cache.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_id_to_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **id_to_text**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ResourceUID_method_id_to_text>`{.interpreted-text
role="ref"}

Converts the given UID to a `uid://` string value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_path_to_uid}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**path_to_uid**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceUID_method_path_to_uid>`{.interpreted-text role="ref"}

Converts the provided resource `path` to a UID. Returns the unchanged
path if it has no associated UID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_remove_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_id**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ResourceUID_method_remove_id>`{.interpreted-text role="ref"}

Removes a loaded UID value from the cache.

Fails with an error if the UID does not exist, so be sure to check
`has_id()<class_ResourceUID_method_has_id>`{.interpreted-text
role="ref"} beforehand.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_set_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set_id**(id:
`int<class_int>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ResourceUID_method_set_id>`{.interpreted-text role="ref"}

Updates the resource path of an existing UID.

Fails with an error if the UID does not exist, so be sure to check
`has_id()<class_ResourceUID_method_has_id>`{.interpreted-text
role="ref"} beforehand, or use
`add_id()<class_ResourceUID_method_add_id>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_text_to_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **text_to_id**(text_id:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ResourceUID_method_text_to_id>`{.interpreted-text
role="ref"}

Extracts the UID value from the given `uid://` string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceUID_method_uid_to_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**uid_to_path**(uid: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceUID_method_uid_to_path>`{.interpreted-text role="ref"}

Converts the provided `uid` to a path. Prints an error if the UID is
invalid.
