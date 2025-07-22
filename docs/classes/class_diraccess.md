github_url
:   hide

::: {.meta keywords="directory, path, folder"}
:::

# DirAccess {#class_DirAccess}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides methods for managing directories and their content.

::: rst-class
classref-introduction-group
:::

## Description

This class is used to manage directories and their content, even outside
of the project folder.

\*\*DirAccess\*\* can\'t be instantiated directly. Instead it is created
with a static method that takes a path for which it will be opened.

Most of the methods have a static alternative that can be used without
creating a **DirAccess**. Static methods only support absolute paths
(including `res://` and `user://`).

    # Standard
    var dir = DirAccess.open("user://levels")
    dir.make_dir("world1")
    # Static
    DirAccess.make_dir_absolute("user://levels/world1")

\*\*Note:\*\* Accessing project (\"res://\") directories once exported
may behave unexpectedly as some files are converted to engine-specific
formats and their original source files may not be present in the
expected PCK package. Because of this, to access resources in an
exported project, it is recommended to use
`ResourceLoader<class_ResourceLoader>`{.interpreted-text role="ref"}
instead of `FileAccess<class_FileAccess>`{.interpreted-text role="ref"}.

Here is an example on how to iterate through the files of a directory:

::::: tabs
::: code-tab
gdscript

func dir_contents(path):

:   var dir = DirAccess.open(path) if dir: dir.list_dir_begin() var
    file_name = dir.get_next() while file_name != \"\": if
    dir.current_is_dir(): print(\"Found directory: \" + file_name) else:
    print(\"Found file: \" + file_name) file_name = dir.get_next() else:
    print(\"An error occurred when trying to access the path.\")
:::

::: code-tab
csharp

public void DirContents(string path) { using var dir =
DirAccess.Open(path); if (dir != null) { dir.ListDirBegin(); string
fileName = dir.GetNext(); while (fileName != \"\") { if
(dir.CurrentIsDir()) { GD.Print(\$\"Found directory: {fileName}\"); }
else { GD.Print(\$\"Found file: {fileName}\"); } fileName =
dir.GetNext(); } } else { GD.Print(\"An error occurred when trying to
access the path.\"); } }
:::
:::::

Keep in mind that file names may change or be remapped after export. If
you want to see the actual resource file list as it appears in the
editor, use
`ResourceLoader.list_directory()<class_ResourceLoader_method_list_directory>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `File system <../tutorials/scripting/filesystem>`{.interpreted-text
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

:::: {#class_DirAccess_property_include_hidden}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **include_hidden**
`🔗<class_DirAccess_property_include_hidden>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_include_hidden**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_include_hidden**()

If `true`, hidden files are included when navigating the directory.

Affects
`list_dir_begin()<class_DirAccess_method_list_dir_begin>`{.interpreted-text
role="ref"},
`get_directories()<class_DirAccess_method_get_directories>`{.interpreted-text
role="ref"} and
`get_files()<class_DirAccess_method_get_files>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_property_include_navigational}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**include_navigational**
`🔗<class_DirAccess_property_include_navigational>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_include_navigational**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_include_navigational**()

If `true`, `.` and `..` are included when navigating the directory.

Affects
`list_dir_begin()<class_DirAccess_method_list_dir_begin>`{.interpreted-text
role="ref"} and
`get_directories()<class_DirAccess_method_get_directories>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_DirAccess_method_change_dir}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**change_dir**(to_dir: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_DirAccess_method_change_dir>`{.interpreted-text
role="ref"}

Changes the currently opened directory to the one passed as an argument.
The argument can be relative to the current directory (e.g. `newdir` or
`../newdir`), or an absolute path (e.g. `/tmp/newdir` or
`res://somedir/newdir`).

Returns one of the `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} code constants
(`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success).

\*\*Note:\*\* The new directory must be within the same scope, e.g. when
you had opened a directory inside `res://`, you can\'t change it to
`user://` directory. If you need to open a directory in another access
scope, use `open()<class_DirAccess_method_open>`{.interpreted-text
role="ref"} to create a new instance instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_copy}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**copy**(from: `String<class_String>`{.interpreted-text role="ref"}, to:
`String<class_String>`{.interpreted-text role="ref"}, chmod_flags:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_DirAccess_method_copy>`{.interpreted-text role="ref"}

Copies the `from` file to the `to` destination. Both arguments should be
paths to files, either relative or absolute. If the destination file
exists and is not access-protected, it will be overwritten.

If `chmod_flags` is different than `-1`, the Unix permissions for the
destination path will be set to the provided value, if available on the
current operating system.

Returns one of the `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} code constants
(`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_copy_absolute}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**copy_absolute**(from: `String<class_String>`{.interpreted-text
role="ref"}, to: `String<class_String>`{.interpreted-text role="ref"},
chmod_flags: `int<class_int>`{.interpreted-text role="ref"} = -1)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_copy_absolute>`{.interpreted-text role="ref"}

Static version of
`copy()<class_DirAccess_method_copy>`{.interpreted-text role="ref"}.
Supports only absolute paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_create_link}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_link**(source: `String<class_String>`{.interpreted-text
role="ref"}, target: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_DirAccess_method_create_link>`{.interpreted-text
role="ref"}

Creates symbolic link between files or folders.

\*\*Note:\*\* On Windows, this method works only if the application is
running with elevated privileges or Developer Mode is enabled.

\*\*Note:\*\* This method is implemented on macOS, Linux, and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_create_temp}
::: rst-class
classref-method
:::
::::

`DirAccess<class_DirAccess>`{.interpreted-text role="ref"}
**create_temp**(prefix: `String<class_String>`{.interpreted-text
role="ref"} = \"\", keep: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_DirAccess_method_create_temp>`{.interpreted-text
role="ref"}

Creates a temporary directory. This directory will be freed when the
returned **DirAccess** is freed.

If `prefix` is not empty, it will be prefixed to the directory name,
separated by a `-`.

If `keep` is `true`, the directory is not deleted when the returned
**DirAccess** is freed.

Returns `null` if opening the directory failed. You can use
`get_open_error()<class_DirAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_current_is_dir}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **current_is_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_current_is_dir>`{.interpreted-text
role="ref"}

Returns whether the current item processed with the last
`get_next()<class_DirAccess_method_get_next>`{.interpreted-text
role="ref"} call is a directory (`.` and `..` are considered
directories).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_dir_exists}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **dir_exists**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_dir_exists>`{.interpreted-text role="ref"}

Returns whether the target directory exists. The argument can be
relative to the current directory, or an absolute path.

\*\*Note:\*\* The returned `bool<class_bool>`{.interpreted-text
role="ref"} in the editor and after exporting when used on a path in the
`res://` directory may be different. Some files are converted to
engine-specific formats when exported, potentially changing the
directory structure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_dir_exists_absolute}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**dir_exists_absolute**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_dir_exists_absolute>`{.interpreted-text
role="ref"}

Static version of
`dir_exists()<class_DirAccess_method_dir_exists>`{.interpreted-text
role="ref"}. Supports only absolute paths.

\*\*Note:\*\* The returned `bool<class_bool>`{.interpreted-text
role="ref"} in the editor and after exporting when used on a path in the
`res://` directory may be different. Some files are converted to
engine-specific formats when exported, potentially changing the
directory structure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_file_exists}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **file_exists**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_file_exists>`{.interpreted-text role="ref"}

Returns whether the target file exists. The argument can be relative to
the current directory, or an absolute path.

For a static equivalent, use
`FileAccess.file_exists()<class_FileAccess_method_file_exists>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Many resources types are imported (e.g. textures or sound
files), and their source asset will not be included in the exported
game, as only the imported version is used. See
`ResourceLoader.exists()<class_ResourceLoader_method_exists>`{.interpreted-text
role="ref"} for an alternative approach that takes resource remapping
into account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_current_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_dir**(include_drive: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_get_current_dir>`{.interpreted-text
role="ref"}

Returns the absolute path to the currently opened directory (e.g.
`res://folder` or `C:\tmp\folder`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_current_drive}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_current_drive**()
`🔗<class_DirAccess_method_get_current_drive>`{.interpreted-text
role="ref"}

Returns the currently opened directory\'s drive index. See
`get_drive_name()<class_DirAccess_method_get_drive_name>`{.interpreted-text
role="ref"} to convert returned index to the name of the drive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_directories}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_directories**()
`🔗<class_DirAccess_method_get_directories>`{.interpreted-text
role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} containing filenames of the directory contents, excluding
files. The array is sorted alphabetically.

Affected by
`include_hidden<class_DirAccess_property_include_hidden>`{.interpreted-text
role="ref"} and
`include_navigational<class_DirAccess_property_include_navigational>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The returned directories in the editor and after exporting
in the `res://` directory may differ as some files are converted to
engine-specific formats when exported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_directories_at}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_directories_at**(path:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_get_directories_at>`{.interpreted-text
role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} containing filenames of the directory contents, excluding
files, at the given `path`. The array is sorted alphabetically.

Use
`get_directories()<class_DirAccess_method_get_directories>`{.interpreted-text
role="ref"} if you want more control of what gets included.

\*\*Note:\*\* The returned directories in the editor and after exporting
in the `res://` directory may differ as some files are converted to
engine-specific formats when exported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_drive_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_drive_count**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_get_drive_count>`{.interpreted-text
role="ref"}

On Windows, returns the number of drives (partitions) mounted on the
current filesystem.

On macOS, returns the number of mounted volumes.

On Linux, returns the number of mounted volumes and GTK 3 bookmarks.

On other platforms, the method returns 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_drive_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_drive_name**(idx: `int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_get_drive_name>`{.interpreted-text
role="ref"}

On Windows, returns the name of the drive (partition) passed as an
argument (e.g. `C:`).

On macOS, returns the path to the mounted volume passed as an argument.

On Linux, returns the path to the mounted volume or GTK 3 bookmark
passed as an argument.

On other platforms, or if the requested drive does not exist, the method
returns an empty String.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_files}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_files**()
`🔗<class_DirAccess_method_get_files>`{.interpreted-text role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} containing filenames of the directory contents, excluding
directories. The array is sorted alphabetically.

Affected by
`include_hidden<class_DirAccess_property_include_hidden>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When used on a `res://` path in an exported project, only
the files actually included in the PCK at the given folder level are
returned. In practice, this means that since imported resources are
stored in a top-level `.godot/` folder, only paths to `*.gd` and
`*.import` files are returned (plus a few files such as `project.godot`
or `project.binary` and the project icon). In an exported project, the
list of returned files will also vary depending on whether
`ProjectSettings.editor/export/convert_text_resources_to_binary<class_ProjectSettings_property_editor/export/convert_text_resources_to_binary>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_files_at}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_files_at**(path:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_DirAccess_method_get_files_at>`{.interpreted-text
role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} containing filenames of the directory contents, excluding
directories, at the given `path`. The array is sorted alphabetically.

Use `get_files()<class_DirAccess_method_get_files>`{.interpreted-text
role="ref"} if you want more control of what gets included.

\*\*Note:\*\* When used on a `res://` path in an exported project, only
the files included in the PCK at the given folder level are returned. In
practice, this means that since imported resources are stored in a
top-level `.godot/` folder, only paths to `.gd` and `.import` files are
returned (plus a few other files, such as `project.godot` or
`project.binary` and the project icon). In an exported project, the list
of returned files will also vary depending on
`ProjectSettings.editor/export/convert_text_resources_to_binary<class_ProjectSettings_property_editor/export/convert_text_resources_to_binary>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_filesystem_type}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_filesystem_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_get_filesystem_type>`{.interpreted-text
role="ref"}

Returns file system type name of the current directory\'s disk. Returned
values are uppercase strings like `NTFS`, `FAT32`, `EXFAT`, `APFS`,
`EXT4`, `BTRFS`, and so on.

\*\*Note:\*\* This method is implemented on macOS, Linux, Windows and
for PCK virtual file system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_next}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_next**()
`🔗<class_DirAccess_method_get_next>`{.interpreted-text role="ref"}

Returns the next element (file or directory) in the current directory.

The name of the file or directory is returned (and not its full path).
Once the stream has been fully processed, the method returns an empty
`String<class_String>`{.interpreted-text role="ref"} and closes the
stream automatically (i.e.
`list_dir_end()<class_DirAccess_method_list_dir_end>`{.interpreted-text
role="ref"} would not be mandatory in such a case).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_open_error}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**get_open_error**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_get_open_error>`{.interpreted-text
role="ref"}

Returns the result of the last
`open()<class_DirAccess_method_open>`{.interpreted-text role="ref"} call
in the current thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_get_space_left}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_space_left**()
`🔗<class_DirAccess_method_get_space_left>`{.interpreted-text
role="ref"}

Returns the available space on the current directory\'s disk, in bytes.
Returns `0` if the platform-specific method to query the available space
fails.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_is_bundle}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_bundle**(path:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_DirAccess_method_is_bundle>`{.interpreted-text
role="ref"}

Returns `true` if the directory is a macOS bundle.

\*\*Note:\*\* This method is implemented on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_is_case_sensitive}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_case_sensitive**(path: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_is_case_sensitive>`{.interpreted-text
role="ref"}

Returns `true` if the file system or directory use case sensitive file
names.

\*\*Note:\*\* This method is implemented on macOS, Linux (for EXT4 and
F2FS filesystems only) and Windows. On other platforms, it always
returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_is_equivalent}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_equivalent**(path_a: `String<class_String>`{.interpreted-text
role="ref"}, path_b: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_is_equivalent>`{.interpreted-text role="ref"}

Returns `true` if paths `path_a` and `path_b` resolve to the same file
system object. Returns `false` otherwise, even if the files are
bit-for-bit identical (e.g., identical copies of the file that are not
symbolic links).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_is_link}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_link**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_is_link>`{.interpreted-text role="ref"}

Returns `true` if the file or directory is a symbolic link, directory
junction, or other reparse point.

\*\*Note:\*\* This method is implemented on macOS, Linux, and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_list_dir_begin}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**list_dir_begin**()
`🔗<class_DirAccess_method_list_dir_begin>`{.interpreted-text
role="ref"}

Initializes the stream used to list all files and directories using the
`get_next()<class_DirAccess_method_get_next>`{.interpreted-text
role="ref"} function, closing the currently opened stream if needed.
Once the stream has been processed, it should typically be closed with
`list_dir_end()<class_DirAccess_method_list_dir_end>`{.interpreted-text
role="ref"}.

Affected by
`include_hidden<class_DirAccess_property_include_hidden>`{.interpreted-text
role="ref"} and
`include_navigational<class_DirAccess_property_include_navigational>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The order of files and directories returned by this method
is not deterministic, and can vary between operating systems. If you
want a list of all files or folders sorted alphabetically, use
`get_files()<class_DirAccess_method_get_files>`{.interpreted-text
role="ref"} or
`get_directories()<class_DirAccess_method_get_directories>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_list_dir_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**list_dir_end**()
`🔗<class_DirAccess_method_list_dir_end>`{.interpreted-text role="ref"}

Closes the current stream opened with
`list_dir_begin()<class_DirAccess_method_list_dir_begin>`{.interpreted-text
role="ref"} (whether it has been fully processed with
`get_next()<class_DirAccess_method_get_next>`{.interpreted-text
role="ref"} does not matter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_make_dir}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**make_dir**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_make_dir>`{.interpreted-text role="ref"}

Creates a directory. The argument can be relative to the current
directory, or an absolute path. The target directory should be placed in
an already existing directory (to create the full path recursively, see
`make_dir_recursive()<class_DirAccess_method_make_dir_recursive>`{.interpreted-text
role="ref"}).

Returns one of the `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} code constants
(`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_make_dir_absolute}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**make_dir_absolute**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_make_dir_absolute>`{.interpreted-text
role="ref"}

Static version of
`make_dir()<class_DirAccess_method_make_dir>`{.interpreted-text
role="ref"}. Supports only absolute paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_make_dir_recursive}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**make_dir_recursive**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_DirAccess_method_make_dir_recursive>`{.interpreted-text
role="ref"}

Creates a target directory and all necessary intermediate directories in
its path, by calling
`make_dir()<class_DirAccess_method_make_dir>`{.interpreted-text
role="ref"} recursively. The argument can be relative to the current
directory, or an absolute path.

Returns one of the `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} code constants
(`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_make_dir_recursive_absolute}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**make_dir_recursive_absolute**(path:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_make_dir_recursive_absolute>`{.interpreted-text
role="ref"}

Static version of
`make_dir_recursive()<class_DirAccess_method_make_dir_recursive>`{.interpreted-text
role="ref"}. Supports only absolute paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_open}
::: rst-class
classref-method
:::
::::

`DirAccess<class_DirAccess>`{.interpreted-text role="ref"}
**open**(path: `String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_DirAccess_method_open>`{.interpreted-text
role="ref"}

Creates a new **DirAccess** object and opens an existing directory of
the filesystem. The `path` argument can be within the project tree
(`res://folder`), the user directory (`user://folder`) or an absolute
path of the user filesystem (e.g. `/tmp/folder` or `C:\tmp\folder`).

Returns `null` if opening the directory failed. You can use
`get_open_error()<class_DirAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_read_link}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **read_link**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_read_link>`{.interpreted-text role="ref"}

Returns target of the symbolic link.

\*\*Note:\*\* This method is implemented on macOS, Linux, and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_remove}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**remove**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_remove>`{.interpreted-text role="ref"}

Permanently deletes the target file or an empty directory. The argument
can be relative to the current directory, or an absolute path. If the
target directory is not empty, the operation will fail.

If you don\'t want to delete the file/directory permanently, use
`OS.move_to_trash()<class_OS_method_move_to_trash>`{.interpreted-text
role="ref"} instead.

Returns one of the `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} code constants
(`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_remove_absolute}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**remove_absolute**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_remove_absolute>`{.interpreted-text
role="ref"}

Static version of
`remove()<class_DirAccess_method_remove>`{.interpreted-text role="ref"}.
Supports only absolute paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_rename}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**rename**(from: `String<class_String>`{.interpreted-text role="ref"},
to: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DirAccess_method_rename>`{.interpreted-text role="ref"}

Renames (move) the `from` file or directory to the `to` destination.
Both arguments should be paths to files or directories, either relative
or absolute. If the destination file or directory exists and is not
access-protected, it will be overwritten.

Returns one of the `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} code constants
(`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirAccess_method_rename_absolute}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**rename_absolute**(from: `String<class_String>`{.interpreted-text
role="ref"}, to: `String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_DirAccess_method_rename_absolute>`{.interpreted-text
role="ref"}

Static version of
`rename()<class_DirAccess_method_rename>`{.interpreted-text role="ref"}.
Supports only absolute paths.
