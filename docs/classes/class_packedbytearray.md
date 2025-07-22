github_url
:   hide

# PackedByteArray {#class_PackedByteArray}

A packed array of bytes.

::: rst-class
classref-introduction-group
:::

## Description

An array specifically designed to hold bytes. Packs data tightly, so it
saves memory for large array sizes.

\*\*PackedByteArray\*\* also provides methods to encode/decode various
types to/from bytes. The way values are encoded is an implementation
detail and shouldn\'t be relied upon when interacting with external
apps.

\*\*Note:\*\* Packed arrays are always passed by reference. To get a
copy of an array that can be modified independently of the original
array, use
`duplicate()<class_PackedByteArray_method_duplicate>`{.interpreted-text
role="ref"}. This is *not* the case for built-in properties and methods.
In these cases the returned packed array is a copy, and changing it will
*not* affect the original value. To update a built-in property of this
type, modify the returned array and then assign it to the property
again.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_PackedByteArray_constructor_PackedByteArray}
::: rst-class
classref-constructor
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**PackedByteArray**()
`🔗<class_PackedByteArray_constructor_PackedByteArray>`{.interpreted-text
role="ref"}

Constructs an empty **PackedByteArray**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**PackedByteArray**(from:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})

Constructs a **PackedByteArray** as a copy of the given
**PackedByteArray**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**PackedByteArray**(from: `Array<class_Array>`{.interpreted-text
role="ref"})

Constructs a new **PackedByteArray**. Optionally, you can pass in a
generic `Array<class_Array>`{.interpreted-text role="ref"} that will be
converted.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PackedByteArray_method_append}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **append**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_append>`{.interpreted-text role="ref"}

Appends an element at the end of the array (alias of
`push_back()<class_PackedByteArray_method_push_back>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_append_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_array**(array:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_append_array>`{.interpreted-text
role="ref"}

Appends a **PackedByteArray** at the end of this array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_bsearch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch**(value:
`int<class_int>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_PackedByteArray_method_bsearch>`{.interpreted-text role="ref"}

Finds the index of an existing value (or the insertion index that
maintains sorting order, if the value is not yet present in the array)
using binary search. Optionally, a `before` specifier can be passed. If
`false`, the returned index comes after all existing entries of the
value in the array.

\*\*Note:\*\* Calling
`bsearch()<class_PackedByteArray_method_bsearch>`{.interpreted-text
role="ref"} on an unsorted array results in unexpected behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_bswap16}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bswap16**(offset: `int<class_int>`{.interpreted-text role="ref"} = 0,
count: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_PackedByteArray_method_bswap16>`{.interpreted-text role="ref"}

Swaps the byte order of `count` 16-bit segments of the array starting at
`offset`. Swap is done in-place. If `count` is less than zero, all
segments to the end of array are processed, if processed data size is
not a multiple of 2, the byte after the last processed 16-bit segment is
not modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_bswap32}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bswap32**(offset: `int<class_int>`{.interpreted-text role="ref"} = 0,
count: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_PackedByteArray_method_bswap32>`{.interpreted-text role="ref"}

Swaps the byte order of `count` 32-bit segments of the array starting at
`offset`. Swap is done in-place. If `count` is less than zero, all
segments to the end of array are processed, if processed data size is
not a multiple of 4, bytes after the last processed 32-bit segment are
not modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_bswap64}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bswap64**(offset: `int<class_int>`{.interpreted-text role="ref"} = 0,
count: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_PackedByteArray_method_bswap64>`{.interpreted-text role="ref"}

Swaps the byte order of `count` 64-bit segments of the array starting at
`offset`. Swap is done in-place. If `count` is less than zero, all
segments to the end of array are processed, if processed data size is
not a multiple of 8, bytes after the last processed 64-bit segment are
not modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_PackedByteArray_method_clear>`{.interpreted-text role="ref"}

Clears the array. This is equivalent to using
`resize()<class_PackedByteArray_method_resize>`{.interpreted-text
role="ref"} with a size of `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_compress}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**compress**(compression_mode: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_compress>`{.interpreted-text
role="ref"}

Returns a new **PackedByteArray** with the data compressed. Set the
compression mode using one of
`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"}\'s constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(value:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_count>`{.interpreted-text
role="ref"}

Returns the number of times an element is in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_double}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**decode_double**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_double>`{.interpreted-text
role="ref"}

Decodes a 64-bit floating-point number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if
a valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_float}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**decode_float**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_float>`{.interpreted-text
role="ref"}

Decodes a 32-bit floating-point number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if
a valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_half}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**decode_half**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_half>`{.interpreted-text
role="ref"}

Decodes a 16-bit floating-point number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if
a valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_s8}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_s8**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_s8>`{.interpreted-text
role="ref"}

Decodes a 8-bit signed integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_s16}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_s16**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_s16>`{.interpreted-text
role="ref"}

Decodes a 16-bit signed integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_s32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_s32**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_s32>`{.interpreted-text
role="ref"}

Decodes a 32-bit signed integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_s64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_s64**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_s64>`{.interpreted-text
role="ref"}

Decodes a 64-bit signed integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_u8}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_u8**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_u8>`{.interpreted-text
role="ref"}

Decodes a 8-bit unsigned integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_u16}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_u16**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_u16>`{.interpreted-text
role="ref"}

Decodes a 16-bit unsigned integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_u32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_u32**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_u32>`{.interpreted-text
role="ref"}

Decodes a 32-bit unsigned integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_u64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_u64**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_u64>`{.interpreted-text
role="ref"}

Decodes a 64-bit unsigned integer number from the bytes starting at
`byte_offset`. Fails if the byte count is insufficient. Returns `0` if a
valid number can\'t be decoded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_var}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**decode_var**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_var>`{.interpreted-text
role="ref"}

Decodes a `Variant<class_Variant>`{.interpreted-text role="ref"} from
the bytes starting at `byte_offset`. Returns `null` if a valid variant
can\'t be decoded or the value is
`Object<class_Object>`{.interpreted-text role="ref"}-derived and
`allow_objects` is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decode_var_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**decode_var_size**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decode_var_size>`{.interpreted-text
role="ref"}

Decodes a size of a `Variant<class_Variant>`{.interpreted-text
role="ref"} from the bytes starting at `byte_offset`. Requires at least
4 bytes of data starting at the offset, otherwise fails.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decompress}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**decompress**(buffer_size: `int<class_int>`{.interpreted-text
role="ref"}, compression_mode: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decompress>`{.interpreted-text
role="ref"}

Returns a new **PackedByteArray** with the data decompressed. Set
`buffer_size` to the size of the uncompressed data. Set the compression
mode using one of
`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"}\'s constants.

\*\*Note:\*\* Decompression is not guaranteed to work with data not
compressed by Godot, for example if data compressed with the deflate
compression mode lacks a checksum or header.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_decompress_dynamic}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**decompress_dynamic**(max_output_size:
`int<class_int>`{.interpreted-text role="ref"}, compression_mode:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_decompress_dynamic>`{.interpreted-text
role="ref"}

Returns a new **PackedByteArray** with the data decompressed. Set the
compression mode using one of
`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"}\'s constants. **This method only accepts brotli, gzip, and
deflate compression modes.**

This method is potentially slower than
`decompress()<class_PackedByteArray_method_decompress>`{.interpreted-text
role="ref"}, as it may have to re-allocate its output buffer multiple
times while decompressing, whereas
`decompress()<class_PackedByteArray_method_decompress>`{.interpreted-text
role="ref"} knows it\'s output buffer size from the beginning.

GZIP has a maximal compression ratio of 1032:1, meaning it\'s very
possible for a small compressed payload to decompress to a potentially
very large output. To guard against this, you may provide a maximum size
this function is allowed to allocate in bytes via `max_output_size`.
Passing -1 will allow for unbounded output. If any positive value is
passed, and the decompression exceeds that amount in bytes, then an
error will be returned.

\*\*Note:\*\* Decompression is not guaranteed to work with data not
compressed by Godot, for example if data compressed with the deflate
compression mode lacks a checksum or header.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_duplicate}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**duplicate**()
`🔗<class_PackedByteArray_method_duplicate>`{.interpreted-text
role="ref"}

Creates a copy of the array, and returns it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_double}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_double**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_double>`{.interpreted-text
role="ref"}

Encodes a 64-bit floating-point number as bytes at the index of
`byte_offset` bytes. The array must have at least 8 bytes of allocated
space, starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_float}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_float**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_float>`{.interpreted-text
role="ref"}

Encodes a 32-bit floating-point number as bytes at the index of
`byte_offset` bytes. The array must have at least 4 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_half}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_half**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_half>`{.interpreted-text
role="ref"}

Encodes a 16-bit floating-point number as bytes at the index of
`byte_offset` bytes. The array must have at least 2 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_s8}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_s8**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_s8>`{.interpreted-text
role="ref"}

Encodes a 8-bit signed integer number (signed byte) at the index of
`byte_offset` bytes. The array must have at least 1 byte of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_s16}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_s16**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_s16>`{.interpreted-text
role="ref"}

Encodes a 16-bit signed integer number as bytes at the index of
`byte_offset` bytes. The array must have at least 2 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_s32}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_s32**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_s32>`{.interpreted-text
role="ref"}

Encodes a 32-bit signed integer number as bytes at the index of
`byte_offset` bytes. The array must have at least 4 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_s64}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_s64**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_s64>`{.interpreted-text
role="ref"}

Encodes a 64-bit signed integer number as bytes at the index of
`byte_offset` bytes. The array must have at least 8 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_u8}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_u8**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_u8>`{.interpreted-text
role="ref"}

Encodes a 8-bit unsigned integer number (byte) at the index of
`byte_offset` bytes. The array must have at least 1 byte of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_u16}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_u16**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_u16>`{.interpreted-text
role="ref"}

Encodes a 16-bit unsigned integer number as bytes at the index of
`byte_offset` bytes. The array must have at least 2 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_u32}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_u32**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_u32>`{.interpreted-text
role="ref"}

Encodes a 32-bit unsigned integer number as bytes at the index of
`byte_offset` bytes. The array must have at least 4 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_u64}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**encode_u64**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_encode_u64>`{.interpreted-text
role="ref"}

Encodes a 64-bit unsigned integer number as bytes at the index of
`byte_offset` bytes. The array must have at least 8 bytes of space,
starting at the offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_encode_var}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**encode_var**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"}, allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_PackedByteArray_method_encode_var>`{.interpreted-text
role="ref"}

Encodes a `Variant<class_Variant>`{.interpreted-text role="ref"} at the
index of `byte_offset` bytes. A sufficient space must be allocated,
depending on the encoded variant\'s size. If `allow_objects` is `false`,
`Object<class_Object>`{.interpreted-text role="ref"}-derived values are
not permitted and will instead be serialized as ID-only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_erase}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **erase**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_erase>`{.interpreted-text role="ref"}

Removes the first occurrence of a value from the array and returns
`true`. If the value does not exist in the array, nothing happens and
`false` is returned. To remove an element by index, use
`remove_at()<class_PackedByteArray_method_remove_at>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_fill}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_fill>`{.interpreted-text role="ref"}

Assigns the given value to all elements in the array. This can typically
be used together with
`resize()<class_PackedByteArray_method_resize>`{.interpreted-text
role="ref"} to create an array with a given size and initialized
elements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_find}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(value:
`int<class_int>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_find>`{.interpreted-text
role="ref"}

Searches the array for a value and returns its index or `-1` if not
found. Optionally, the initial search index can be passed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_get>`{.interpreted-text
role="ref"}

Returns the byte at the given `index` in the array. If `index`
out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most
notably, when this method fails, it doesn\'t pause project execution if
run from the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get_string_from_ascii}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string_from_ascii**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_get_string_from_ascii>`{.interpreted-text
role="ref"}

Converts ASCII/Latin-1 encoded array to
`String<class_String>`{.interpreted-text role="ref"}. Fast alternative
to
`get_string_from_utf8()<class_PackedByteArray_method_get_string_from_utf8>`{.interpreted-text
role="ref"} if the content is ASCII/Latin-1 only. Unlike the UTF-8
function this function maps every byte to a character in the array.
Multibyte sequences will not be interpreted correctly. For parsing user
input always use
`get_string_from_utf8()<class_PackedByteArray_method_get_string_from_utf8>`{.interpreted-text
role="ref"}. This is the inverse of
`String.to_ascii_buffer()<class_String_method_to_ascii_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get_string_from_multibyte_char}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string_from_multibyte_char**(encoding:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_get_string_from_multibyte_char>`{.interpreted-text
role="ref"}

Converts system multibyte code page encoded array to
`String<class_String>`{.interpreted-text role="ref"}. If conversion
fails, empty string is returned. This is the inverse of
`String.to_multibyte_char_buffer()<class_String_method_to_multibyte_char_buffer>`{.interpreted-text
role="ref"}.

The values permitted for `encoding` are system dependent. If `encoding`
is empty string, system default encoding is used.

- For Windows, see [Code Page
  Identifiers](https://learn.microsoft.com/en-us/windows/win32/Intl/code-page-identifiers)
  .NET names.
- For macOS and Linux/BSD, see `libiconv` library documentation and
  `iconv --list` for a list of supported encodings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get_string_from_utf8}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string_from_utf8**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_get_string_from_utf8>`{.interpreted-text
role="ref"}

Converts UTF-8 encoded array to `String<class_String>`{.interpreted-text
role="ref"}. Slower than
`get_string_from_ascii()<class_PackedByteArray_method_get_string_from_ascii>`{.interpreted-text
role="ref"} but supports UTF-8 encoded data. Use this function if you
are unsure about the source of the data. For user input this function
should always be preferred. Returns empty string if source array is not
valid UTF-8 string. This is the inverse of
`String.to_utf8_buffer()<class_String_method_to_utf8_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get_string_from_utf16}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string_from_utf16**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_get_string_from_utf16>`{.interpreted-text
role="ref"}

Converts UTF-16 encoded array to
`String<class_String>`{.interpreted-text role="ref"}. If the BOM is
missing, little-endianness is assumed. Returns empty string if source
array is not valid UTF-16 string. This is the inverse of
`String.to_utf16_buffer()<class_String_method_to_utf16_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get_string_from_utf32}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string_from_utf32**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_get_string_from_utf32>`{.interpreted-text
role="ref"}

Converts UTF-32 encoded array to
`String<class_String>`{.interpreted-text role="ref"}. Returns empty
string if source array is not valid UTF-32 string. This is the inverse
of
`String.to_utf32_buffer()<class_String_method_to_utf32_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_get_string_from_wchar}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string_from_wchar**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_get_string_from_wchar>`{.interpreted-text
role="ref"}

Converts wide character (`wchar_t`, UTF-16 on Windows, UTF-32 on other
platforms) encoded array to `String<class_String>`{.interpreted-text
role="ref"}. Returns empty string if source array is not valid wide
string. This is the inverse of
`String.to_wchar_buffer()<class_String_method_to_wchar_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(value:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the array contains `value`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_has_encoded_var}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_encoded_var**(byte_offset: `int<class_int>`{.interpreted-text
role="ref"}, allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_has_encoded_var>`{.interpreted-text
role="ref"}

Returns `true` if a valid `Variant<class_Variant>`{.interpreted-text
role="ref"} value can be decoded at the `byte_offset`. Returns `false`
otherwise or when the value is `Object<class_Object>`{.interpreted-text
role="ref"}-derived and `allow_objects` is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_hex_encode}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **hex_encode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_hex_encode>`{.interpreted-text
role="ref"}

Returns a hexadecimal representation of this array as a
`String<class_String>`{.interpreted-text role="ref"}.

::::: tabs
::: code-tab
gdscript

var array = PackedByteArray(\[11, 46, 255\]) print(array.hex_encode())
\# Prints \"0b2eff\"
:::

::: code-tab
csharp

byte\[\] array = \[11, 46, 255\]; GD.Print(array.HexEncode()); // Prints
\"0b2eff\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_insert}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **insert**(at_index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_insert>`{.interpreted-text role="ref"}

Inserts a new element at a given position in the array. The position
must be valid, or at the end of the array (`idx == size()`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the array is empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_push_back}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_back**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_push_back>`{.interpreted-text
role="ref"}

Appends an element at the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_remove_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_at**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_remove_at>`{.interpreted-text
role="ref"}

Removes an element from the array by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_resize}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize**(new_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_resize>`{.interpreted-text role="ref"}

Sets the size of the array. If the array is grown, reserves elements at
the end of the array. If the array is shrunk, truncates the array to the
new size. Calling
`resize()<class_PackedByteArray_method_resize>`{.interpreted-text
role="ref"} once and assigning the new values is faster than adding new
elements one by one.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the following
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constants
if this method fails:
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if the size is negative, or
`@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>`{.interpreted-text
role="ref"} if allocations fail. Use
`size()<class_PackedByteArray_method_size>`{.interpreted-text
role="ref"} to find the actual size of the array after resize.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_reverse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_PackedByteArray_method_reverse>`{.interpreted-text role="ref"}

Reverses the order of the elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_rfind}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(value:
`int<class_int>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_rfind>`{.interpreted-text
role="ref"}

Searches the array in reverse order. Optionally, a start search index
can be passed. If negative, the start index is considered relative to
the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set**(index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_method_set>`{.interpreted-text role="ref"}

Changes the byte at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_size>`{.interpreted-text
role="ref"}

Returns the number of elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_slice}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**slice**(begin: `int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"} = 2147483647)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedByteArray_method_slice>`{.interpreted-text
role="ref"}

Returns the slice of the **PackedByteArray**, from `begin` (inclusive)
to `end` (exclusive), as a new **PackedByteArray**.

The absolute value of `begin` and `end` will be clamped to the array
size, so the default value for `end` makes it slice to the size of the
array by default (i.e. `arr.slice(1)` is a shorthand for
`arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the
end of the array (i.e. `arr.slice(0, -2)` is a shorthand for
`arr.slice(0, arr.size() - 2)`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_sort}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_PackedByteArray_method_sort>`{.interpreted-text role="ref"}

Sorts the elements of the array in ascending order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_color_array}
::: rst-class
classref-method
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**to_color_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_color_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, where each block of 16 bytes has been converted to a
`Color<class_Color>`{.interpreted-text role="ref"} variant.

\*\*Note:\*\* The size of the input array must be a multiple of 16 (size
of four 32-bit float variables). The size of the new array will be
`byte_array.size() / 16`. If the original data can\'t be converted to
`Color<class_Color>`{.interpreted-text role="ref"} variants, the
resulting data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_float32_array}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **to_float32_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_float32_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, where each block of 4 bytes has been converted to a 32-bit
float (C++ `float`).

The size of the input array must be a multiple of 4 (size of 32-bit
float). The size of the new array will be `byte_array.size() / 4`.

If the original data can\'t be converted to 32-bit floats, the resulting
data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_float64_array}
::: rst-class
classref-method
:::
::::

`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} **to_float64_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_float64_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}, where each block of 8 bytes has been converted to a 64-bit
float (C++ `double`, Godot `float<class_float>`{.interpreted-text
role="ref"}).

The size of the input array must be a multiple of 8 (size of 64-bit
double). The size of the new array will be `byte_array.size() / 8`.

If the original data can\'t be converted to 64-bit floats, the resulting
data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_int32_array}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**to_int32_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_int32_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, where each block of 4 bytes has been converted to a signed
32-bit integer (C++ `int32_t`).

The size of the input array must be a multiple of 4 (size of 32-bit
integer). The size of the new array will be `byte_array.size() / 4`.

If the original data can\'t be converted to signed 32-bit integers, the
resulting data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_int64_array}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**to_int64_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_int64_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"}, where each block of 8 bytes has been converted to a signed
64-bit integer (C++ `int64_t`, Godot `int<class_int>`{.interpreted-text
role="ref"}).

The size of the input array must be a multiple of 8 (size of 64-bit
integer). The size of the new array will be `byte_array.size() / 8`.

If the original data can\'t be converted to signed 64-bit integers, the
resulting data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_vector2_array}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **to_vector2_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_vector2_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, where each block of 8 bytes or 16 bytes (32-bit or 64-bit)
has been converted to a `Vector2<class_Vector2>`{.interpreted-text
role="ref"} variant.

\*\*Note:\*\* The size of the input array must be a multiple of 8 or 16
(depending on the build settings, see
`Vector2<class_Vector2>`{.interpreted-text role="ref"} for more
details). The size of the new array will be
`byte_array.size() / (8 or 16)`. If the original data can\'t be
converted to `Vector2<class_Vector2>`{.interpreted-text role="ref"}
variants, the resulting data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_vector3_array}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **to_vector3_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_vector3_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, where each block of 12 or 24 bytes (32-bit or 64-bit) has
been converted to a `Vector3<class_Vector3>`{.interpreted-text
role="ref"} variant.

\*\*Note:\*\* The size of the input array must be a multiple of 12 or 24
(depending on the build settings, see
`Vector3<class_Vector3>`{.interpreted-text role="ref"} for more
details). The size of the new array will be
`byte_array.size() / (12 or 24)`. If the original data can\'t be
converted to `Vector3<class_Vector3>`{.interpreted-text role="ref"}
variants, the resulting data is undefined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_method_to_vector4_array}
::: rst-class
classref-method
:::
::::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **to_vector4_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedByteArray_method_to_vector4_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"}, where each block of 16 or 32 bytes (32-bit or 64-bit) has
been converted to a `Vector4<class_Vector4>`{.interpreted-text
role="ref"} variant.

\*\*Note:\*\* The size of the input array must be a multiple of 16 or 32
(depending on the build settings, see
`Vector4<class_Vector4>`{.interpreted-text role="ref"} for more
details). The size of the new array will be
`byte_array.size() / (16 or 32)`. If the original data can\'t be
converted to `Vector4<class_Vector4>`{.interpreted-text role="ref"}
variants, the resulting data is undefined.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_PackedByteArray_operator_neq_PackedByteArray}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_operator_neq_PackedByteArray>`{.interpreted-text
role="ref"}

Returns `true` if contents of the arrays differ.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_operator_sum_PackedByteArray}
::: rst-class
classref-operator
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**operator +**(right:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_operator_sum_PackedByteArray>`{.interpreted-text
role="ref"}

Returns a new **PackedByteArray** with contents of `right` added at the
end of this array. For better performance, consider using
`append_array()<class_PackedByteArray_method_append_array>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_operator_eq_PackedByteArray}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_operator_eq_PackedByteArray>`{.interpreted-text
role="ref"}

Returns `true` if contents of both arrays are the same, i.e. they have
all equal bytes at the corresponding indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedByteArray_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \[\]**(index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedByteArray_operator_idx_int>`{.interpreted-text
role="ref"}

Returns the byte at index `index`. Negative indices can be used to
access the elements starting from the end. Using index out of array\'s
bounds will result in an error.

Note that the byte is returned as a 64-bit
`int<class_int>`{.interpreted-text role="ref"}.
