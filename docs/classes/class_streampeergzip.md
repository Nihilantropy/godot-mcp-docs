github_url
:   hide

# StreamPeerGZIP {#class_StreamPeerGZIP}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `StreamPeer<class_StreamPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A stream peer that handles GZIP and deflate compression/decompression.

::: rst-class
classref-introduction-group
:::

## Description

This class allows to compress or decompress data using GZIP/deflate in a
streaming fashion. This is particularly useful when compressing or
decompressing files that have to be sent through the network without
needing to allocate them all in memory.

After starting the stream via
`start_compression()<class_StreamPeerGZIP_method_start_compression>`{.interpreted-text
role="ref"} (or
`start_decompression()<class_StreamPeerGZIP_method_start_decompression>`{.interpreted-text
role="ref"}), calling
`StreamPeer.put_partial_data()<class_StreamPeer_method_put_partial_data>`{.interpreted-text
role="ref"} on this stream will compress (or decompress) the data,
writing it to the internal buffer. Calling
`StreamPeer.get_available_bytes()<class_StreamPeer_method_get_available_bytes>`{.interpreted-text
role="ref"} will return the pending bytes in the internal buffer, and
`StreamPeer.get_partial_data()<class_StreamPeer_method_get_partial_data>`{.interpreted-text
role="ref"} will retrieve the compressed (or decompressed) bytes from
it. When the stream is over, you must call
`finish()<class_StreamPeerGZIP_method_finish>`{.interpreted-text
role="ref"} to ensure the internal buffer is properly flushed (make sure
to call
`StreamPeer.get_available_bytes()<class_StreamPeer_method_get_available_bytes>`{.interpreted-text
role="ref"} on last time to check if more data needs to be read after
that).

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

:::: {#class_StreamPeerGZIP_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_StreamPeerGZIP_method_clear>`{.interpreted-text role="ref"}

Clears this stream, resetting the internal state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerGZIP_method_finish}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**finish**() `🔗<class_StreamPeerGZIP_method_finish>`{.interpreted-text
role="ref"}

Finalizes the stream, compressing any buffered chunk left.

You must call it only when you are compressing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerGZIP_method_start_compression}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start_compression**(use_deflate: `bool<class_bool>`{.interpreted-text
role="ref"} = false, buffer_size: `int<class_int>`{.interpreted-text
role="ref"} = 65535)
`🔗<class_StreamPeerGZIP_method_start_compression>`{.interpreted-text
role="ref"}

Start the stream in compression mode with the given `buffer_size`, if
`use_deflate` is `true` uses deflate instead of GZIP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerGZIP_method_start_decompression}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start_decompression**(use_deflate:
`bool<class_bool>`{.interpreted-text role="ref"} = false, buffer_size:
`int<class_int>`{.interpreted-text role="ref"} = 65535)
`🔗<class_StreamPeerGZIP_method_start_decompression>`{.interpreted-text
role="ref"}

Start the stream in decompression mode with the given `buffer_size`, if
`use_deflate` is `true` uses deflate instead of GZIP.
