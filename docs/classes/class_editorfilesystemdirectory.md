github_url
:   hide

# EditorFileSystemDirectory {#class_EditorFileSystemDirectory}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A directory for the resource filesystem.

::: rst-class
classref-introduction-group
:::

## Description

A more generalized, low-level variation of the directory concept.

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

:::: {#class_EditorFileSystemDirectory_method_find_dir_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_dir_index**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_find_dir_index>`{.interpreted-text
role="ref"}

Returns the index of the directory with name `name` or `-1` if not
found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_find_file_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_file_index**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_find_file_index>`{.interpreted-text
role="ref"}

Returns the index of the file with name `name` or `-1` if not found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_file**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file>`{.interpreted-text
role="ref"}

Returns the name of the file at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_file_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file_count>`{.interpreted-text
role="ref"}

Returns the number of files in this directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file_import_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_file_import_is_valid**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file_import_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the file at index `idx` imported properly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_file_path**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file_path>`{.interpreted-text
role="ref"}

Returns the path to the file at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file_script_class_extends}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_file_script_class_extends**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file_script_class_extends>`{.interpreted-text
role="ref"}

Returns the base class of the script class defined in the file at index
`idx`. If the file doesn\'t define a script class using the `class_name`
syntax, this will return an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file_script_class_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_file_script_class_name**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file_script_class_name>`{.interpreted-text
role="ref"}

Returns the name of the script class defined in the file at index `idx`.
If the file doesn\'t define a script class using the `class_name`
syntax, this will return an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_file_type}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_file_type**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_file_type>`{.interpreted-text
role="ref"}

Returns the resource type of the file at index `idx`. This returns a
string such as `"Resource"` or `"GDScript"`, *not* a file extension such
as `".gd"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_name**()
`🔗<class_EditorFileSystemDirectory_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of this directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_parent}
::: rst-class
classref-method
:::
::::

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>`{.interpreted-text
role="ref"} **get_parent**()
`🔗<class_EditorFileSystemDirectory_method_get_parent>`{.interpreted-text
role="ref"}

Returns the parent directory for this directory or `null` if called on a
directory at `res://` or `user://`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_path>`{.interpreted-text
role="ref"}

Returns the path to this directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_subdir}
::: rst-class
classref-method
:::
::::

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>`{.interpreted-text
role="ref"} **get_subdir**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystemDirectory_method_get_subdir>`{.interpreted-text
role="ref"}

Returns the subdirectory at index `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystemDirectory_method_get_subdir_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_subdir_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystemDirectory_method_get_subdir_count>`{.interpreted-text
role="ref"}

Returns the number of subdirectories in this directory.
