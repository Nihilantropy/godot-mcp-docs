github_url
:   hide

# StreamPeer {#class_StreamPeer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`StreamPeerBuffer<class_StreamPeerBuffer>`{.interpreted-text
role="ref"},
`StreamPeerExtension<class_StreamPeerExtension>`{.interpreted-text
role="ref"}, `StreamPeerGZIP<class_StreamPeerGZIP>`{.interpreted-text
role="ref"}, `StreamPeerTCP<class_StreamPeerTCP>`{.interpreted-text
role="ref"}, `StreamPeerTLS<class_StreamPeerTLS>`{.interpreted-text
role="ref"}

Abstract base class for interacting with streams.

::: rst-class
classref-introduction-group
:::

## Description

StreamPeer is an abstract base class mostly used for stream-based
protocols (such as TCP). It provides an API for sending and receiving
data through streams as raw data or strings.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

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

:::: {#class_StreamPeer_property_big_endian}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **big_endian** =
`false` `🔗<class_StreamPeer_property_big_endian>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_big_endian**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_big_endian_enabled**()

If `true`, this **StreamPeer** will using big-endian format for encoding
and decoding.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StreamPeer_method_get_8}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_8**()
`🔗<class_StreamPeer_method_get_8>`{.interpreted-text role="ref"}

Gets a signed byte from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_16}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_16**()
`🔗<class_StreamPeer_method_get_16>`{.interpreted-text role="ref"}

Gets a signed 16-bit value from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_32**()
`🔗<class_StreamPeer_method_get_32>`{.interpreted-text role="ref"}

Gets a signed 32-bit value from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_64**()
`🔗<class_StreamPeer_method_get_64>`{.interpreted-text role="ref"}

Gets a signed 64-bit value from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_available_bytes}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_available_bytes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeer_method_get_available_bytes>`{.interpreted-text
role="ref"}

Returns the number of bytes this **StreamPeer** has available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_data}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_data**(bytes:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_get_data>`{.interpreted-text role="ref"}

Returns a chunk data with the received bytes. The number of bytes to be
received can be requested in the `bytes` argument. If not enough bytes
are available, the function will block until the desired amount is
received. This function returns two values, an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} code and
a data array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_double}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_double**()
`🔗<class_StreamPeer_method_get_double>`{.interpreted-text role="ref"}

Gets a double-precision float from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_float}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_float**()
`🔗<class_StreamPeer_method_get_float>`{.interpreted-text role="ref"}

Gets a single-precision float from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_half}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_half**()
`🔗<class_StreamPeer_method_get_half>`{.interpreted-text role="ref"}

Gets a half-precision float from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_partial_data}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_partial_data**(bytes: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_StreamPeer_method_get_partial_data>`{.interpreted-text
role="ref"}

Returns a chunk data with the received bytes. The number of bytes to be
received can be requested in the `bytes` argument. If not enough bytes
are available, the function will return how many were actually received.
This function returns two values: an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} code and
a data array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string**(bytes: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_StreamPeer_method_get_string>`{.interpreted-text
role="ref"}

Gets an ASCII string with byte-length `bytes` from the stream. If
`bytes` is negative (default) the length will be read from the stream
using the reverse process of
`put_string()<class_StreamPeer_method_put_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_u8}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_u8**()
`🔗<class_StreamPeer_method_get_u8>`{.interpreted-text role="ref"}

Gets an unsigned byte from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_u16}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_u16**()
`🔗<class_StreamPeer_method_get_u16>`{.interpreted-text role="ref"}

Gets an unsigned 16-bit value from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_u32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_u32**()
`🔗<class_StreamPeer_method_get_u32>`{.interpreted-text role="ref"}

Gets an unsigned 32-bit value from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_u64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_u64**()
`🔗<class_StreamPeer_method_get_u64>`{.interpreted-text role="ref"}

Gets an unsigned 64-bit value from the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_utf8_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_utf8_string**(bytes: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_StreamPeer_method_get_utf8_string>`{.interpreted-text
role="ref"}

Gets a UTF-8 string with byte-length `bytes` from the stream (this
decodes the string sent as UTF-8). If `bytes` is negative (default) the
length will be read from the stream using the reverse process of
`put_utf8_string()<class_StreamPeer_method_put_utf8_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_get_var}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_var**(allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_StreamPeer_method_get_var>`{.interpreted-text role="ref"}

Gets a Variant from the stream. If `allow_objects` is `true`, decoding
objects is allowed.

Internally, this uses the same decoding mechanism as the
`@GlobalScope.bytes_to_var()<class_@GlobalScope_method_bytes_to_var>`{.interpreted-text
role="ref"} method.

\*\*Warning:\*\* Deserialized objects can contain code which gets
executed. Do not use this option if the serialized object comes from
untrusted sources to avoid potential security threats such as remote
code execution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_8}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_8**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_8>`{.interpreted-text role="ref"}

Puts a signed byte into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_16}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_16**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_16>`{.interpreted-text role="ref"}

Puts a signed 16-bit value into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_32}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_32**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_32>`{.interpreted-text role="ref"}

Puts a signed 32-bit value into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_64}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_64**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_64>`{.interpreted-text role="ref"}

Puts a signed 64-bit value into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_data}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**put_data**(data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_data>`{.interpreted-text role="ref"}

Sends a chunk of data through the connection, blocking if necessary
until the data is done sending. This function returns an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_double}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_double**(value: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_StreamPeer_method_put_double>`{.interpreted-text
role="ref"}

Puts a double-precision float into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_float}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_float**(value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_float>`{.interpreted-text role="ref"}

Puts a single-precision float into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_half}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_half**(value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_half>`{.interpreted-text role="ref"}

Puts a half-precision float into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_partial_data}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**put_partial_data**(data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_partial_data>`{.interpreted-text
role="ref"}

Sends a chunk of data through the connection. If all the data could not
be sent at once, only part of it will. This function returns two values,
an `Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} code
and an integer, describing how much data was actually sent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_string}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_string**(value: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_StreamPeer_method_put_string>`{.interpreted-text
role="ref"}

Puts a zero-terminated ASCII string into the stream prepended by a
32-bit unsigned integer representing its size.

\*\*Note:\*\* To put an ASCII string without prepending its size, you
can use `put_data()<class_StreamPeer_method_put_data>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

put_data(\"Hello world\".to_ascii_buffer())
:::

::: code-tab
csharp

PutData(\"Hello World\".ToAsciiBuffer());
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_u8}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_u8**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_u8>`{.interpreted-text role="ref"}

Puts an unsigned byte into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_u16}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_u16**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_u16>`{.interpreted-text role="ref"}

Puts an unsigned 16-bit value into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_u32}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_u32**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_u32>`{.interpreted-text role="ref"}

Puts an unsigned 32-bit value into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_u64}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_u64**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeer_method_put_u64>`{.interpreted-text role="ref"}

Puts an unsigned 64-bit value into the stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_utf8_string}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_utf8_string**(value: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_StreamPeer_method_put_utf8_string>`{.interpreted-text
role="ref"}

Puts a zero-terminated UTF-8 string into the stream prepended by a 32
bits unsigned integer representing its size.

\*\*Note:\*\* To put a UTF-8 string without prepending its size, you can
use `put_data()<class_StreamPeer_method_put_data>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

put_data(\"Hello world\".to_utf8_buffer())
:::

::: code-tab
csharp

PutData(\"Hello World\".ToUtf8Buffer());
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeer_method_put_var}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**put_var**(value: `Variant<class_Variant>`{.interpreted-text
role="ref"}, full_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_StreamPeer_method_put_var>`{.interpreted-text role="ref"}

Puts a Variant into the stream. If `full_objects` is `true` encoding
objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the
`@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"} method.
