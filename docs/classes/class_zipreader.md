github_url
:   hide

# ZIPReader {#class_ZIPReader}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Allows reading the content of a ZIP file.

::: rst-class
classref-introduction-group
:::

## Description

This class implements a reader that can extract the content of
individual files inside a ZIP archive. See also
`ZIPPacker<class_ZIPPacker>`{.interpreted-text role="ref"}.

    # Read a single file from a ZIP archive.
    func read_zip_file():
        var reader = ZIPReader.new()
        var err = reader.open("user://archive.zip")
        if err != OK:
            return PackedByteArray()
        var res = reader.read_file("hello.txt")
        reader.close()
        return res

    # Extract all files from a ZIP archive, preserving the directories within.
    # This acts like the "Extract all" functionality from most archive managers.
    func extract_all_from_zip():
        var reader = ZIPReader.new()
        reader.open("res://archive.zip")

        # Destination directory for the extracted files (this folder must exist before extraction).
        # Not all ZIP archives put everything in a single root folder,
        # which means several files/folders may be created in `root_dir` after extraction.
        var root_dir = DirAccess.open("user://")

        var files = reader.get_files()
        for file_path in files:
            # If the current entry is a directory.
            if file_path.ends_with("/"):
                root_dir.make_dir_recursive(file_path)
                continue

            # Write file contents, creating folders automatically when needed.
            # Not all ZIP archives are strictly ordered, so we need to do this in case
            # the file entry comes before the folder entry.
            root_dir.make_dir_recursive(root_dir.get_current_dir().path_join(file_path).get_base_dir())
            var file = FileAccess.open(root_dir.get_current_dir().path_join(file_path), FileAccess.WRITE)
            var buffer = reader.read_file(file_path)
            file.store_buffer(buffer)

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

:::: {#class_ZIPReader_method_close}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**close**() `🔗<class_ZIPReader_method_close>`{.interpreted-text
role="ref"}

Closes the underlying resources used by this instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_file_exists}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **file_exists**(path:
`String<class_String>`{.interpreted-text role="ref"}, case_sensitive:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_ZIPReader_method_file_exists>`{.interpreted-text role="ref"}

Returns `true` if the file exists in the loaded zip archive.

Must be called after
`open()<class_ZIPReader_method_open>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_get_compression_level}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_compression_level**(path: `String<class_String>`{.interpreted-text
role="ref"}, case_sensitive: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_ZIPReader_method_get_compression_level>`{.interpreted-text
role="ref"}

Returns the compression level of the file in the loaded zip archive.
Returns `-1` if the file doesn\'t exist or any other error occurs. Must
be called after `open()<class_ZIPReader_method_open>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_get_files}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_files**()
`🔗<class_ZIPReader_method_get_files>`{.interpreted-text role="ref"}

Returns the list of names of all files in the loaded archive.

Must be called after
`open()<class_ZIPReader_method_open>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_open}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**open**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ZIPReader_method_open>`{.interpreted-text role="ref"}

Opens the zip archive at the given `path` and reads its file index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_read_file}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**read_file**(path: `String<class_String>`{.interpreted-text
role="ref"}, case_sensitive: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_ZIPReader_method_read_file>`{.interpreted-text role="ref"}

Loads the whole content of a file in the loaded zip archive into memory
and returns it.

Must be called after
`open()<class_ZIPReader_method_open>`{.interpreted-text role="ref"}.
