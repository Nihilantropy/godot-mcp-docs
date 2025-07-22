github_url
:   hide

# ZIPPacker {#class_ZIPPacker}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Allows the creation of ZIP files.

::: rst-class
classref-introduction-group
:::

## Description

This class implements a writer that allows storing the multiple blobs in
a ZIP archive. See also `ZIPReader<class_ZIPReader>`{.interpreted-text
role="ref"} and `PCKPacker<class_PCKPacker>`{.interpreted-text
role="ref"}.

    # Create a ZIP archive with a single file at its root.
    func write_zip_file():
        var writer = ZIPPacker.new()
        var err = writer.open("user://archive.zip")
        if err != OK:
            return err
        writer.start_file("hello.txt")
        writer.write_file("Hello World".to_utf8_buffer())
        writer.close_file()

        writer.close()
        return OK

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

## Enumerations

:::: {#enum_ZIPPacker_ZipAppend}
::: rst-class
classref-enumeration
:::
::::

enum **ZipAppend**: `🔗<enum_ZIPPacker_ZipAppend>`{.interpreted-text
role="ref"}

:::: {#class_ZIPPacker_constant_APPEND_CREATE}
::: rst-class
classref-enumeration-constant
:::
::::

`ZipAppend<enum_ZIPPacker_ZipAppend>`{.interpreted-text role="ref"}
**APPEND_CREATE** = `0`

Create a new zip archive at the given path.

:::: {#class_ZIPPacker_constant_APPEND_CREATEAFTER}
::: rst-class
classref-enumeration-constant
:::
::::

`ZipAppend<enum_ZIPPacker_ZipAppend>`{.interpreted-text role="ref"}
**APPEND_CREATEAFTER** = `1`

Append a new zip archive to the end of the already existing file at the
given path.

:::: {#class_ZIPPacker_constant_APPEND_ADDINZIP}
::: rst-class
classref-enumeration-constant
:::
::::

`ZipAppend<enum_ZIPPacker_ZipAppend>`{.interpreted-text role="ref"}
**APPEND_ADDINZIP** = `2`

Add new files to the existing zip archive at the given path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ZIPPacker_CompressionLevel}
::: rst-class
classref-enumeration
:::
::::

enum **CompressionLevel**:
`🔗<enum_ZIPPacker_CompressionLevel>`{.interpreted-text role="ref"}

:::: {#class_ZIPPacker_constant_COMPRESSION_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionLevel<enum_ZIPPacker_CompressionLevel>`{.interpreted-text
role="ref"} **COMPRESSION_DEFAULT** = `-1`

Start a file with the default Deflate compression level (`6`). This is a
good compromise between speed and file size.

:::: {#class_ZIPPacker_constant_COMPRESSION_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionLevel<enum_ZIPPacker_CompressionLevel>`{.interpreted-text
role="ref"} **COMPRESSION_NONE** = `0`

Start a file with no compression. This is also known as the \"Store\"
compression mode and is the fastest method of packing files inside a ZIP
archive. Consider using this mode for files that are already compressed
(such as JPEG, PNG, MP3, or Ogg Vorbis files).

:::: {#class_ZIPPacker_constant_COMPRESSION_FAST}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionLevel<enum_ZIPPacker_CompressionLevel>`{.interpreted-text
role="ref"} **COMPRESSION_FAST** = `1`

Start a file with the fastest Deflate compression level (`1`). This is
fast to compress, but results in larger file sizes than
`COMPRESSION_DEFAULT<class_ZIPPacker_constant_COMPRESSION_DEFAULT>`{.interpreted-text
role="ref"}. Decompression speed is generally unaffected by the chosen
compression level.

:::: {#class_ZIPPacker_constant_COMPRESSION_BEST}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionLevel<enum_ZIPPacker_CompressionLevel>`{.interpreted-text
role="ref"} **COMPRESSION_BEST** = `9`

Start a file with the best Deflate compression level (`9`). This is slow
to compress, but results in smaller file sizes than
`COMPRESSION_DEFAULT<class_ZIPPacker_constant_COMPRESSION_DEFAULT>`{.interpreted-text
role="ref"}. Decompression speed is generally unaffected by the chosen
compression level.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ZIPPacker_property_compression_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compression_level** =
`-1` `🔗<class_ZIPPacker_property_compression_level>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_compression_level**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_compression_level**()

The compression level used when
`start_file()<class_ZIPPacker_method_start_file>`{.interpreted-text
role="ref"} is called. Use
`CompressionLevel<enum_ZIPPacker_CompressionLevel>`{.interpreted-text
role="ref"} as a reference.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ZIPPacker_method_close}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**close**() `🔗<class_ZIPPacker_method_close>`{.interpreted-text
role="ref"}

Closes the underlying resources used by this instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPPacker_method_close_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**close_file**()
`🔗<class_ZIPPacker_method_close_file>`{.interpreted-text role="ref"}

Stops writing to a file within the archive.

It will fail if there is no open file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPPacker_method_open}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**open**(path: `String<class_String>`{.interpreted-text role="ref"},
append: `ZipAppend<enum_ZIPPacker_ZipAppend>`{.interpreted-text
role="ref"} = 0) `🔗<class_ZIPPacker_method_open>`{.interpreted-text
role="ref"}

Opens a zip file for writing at the given path using the specified write
mode.

This must be called before everything else.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPPacker_method_start_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start_file**(path: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_ZIPPacker_method_start_file>`{.interpreted-text
role="ref"}

Starts writing to a file within the archive. Only one file can be
written at the same time.

Must be called after
`open()<class_ZIPPacker_method_open>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPPacker_method_write_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**write_file**(data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ZIPPacker_method_write_file>`{.interpreted-text role="ref"}

Write the given `data` to the file.

Needs to be called after
`start_file()<class_ZIPPacker_method_start_file>`{.interpreted-text
role="ref"}.
