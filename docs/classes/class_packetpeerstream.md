github_url
:   hide

# PacketPeerStream {#class_PacketPeerStream}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Wrapper to use a PacketPeer over a StreamPeer.

::: rst-class
classref-introduction-group
:::

## Description

PacketStreamPeer provides a wrapper for working using packets over a
stream. This allows for using packet based code with StreamPeers.
PacketPeerStream implements a custom protocol over the StreamPeer, so
the user should not read or write to the wrapped StreamPeer directly.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PacketPeerStream_property_input_buffer_max_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **input_buffer_max_size**
= `65532`
`🔗<class_PacketPeerStream_property_input_buffer_max_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_input_buffer_max_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_input_buffer_max_size**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerStream_property_output_buffer_max_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**output_buffer_max_size** = `65532`
`🔗<class_PacketPeerStream_property_output_buffer_max_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_output_buffer_max_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_output_buffer_max_size**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerStream_property_stream_peer}
::: rst-class
classref-property
:::
::::

`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"}
**stream_peer**
`🔗<class_PacketPeerStream_property_stream_peer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stream_peer**(value:
  `StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"})
- `StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"}
  **get_stream_peer**()

The wrapped `StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"}
object.
