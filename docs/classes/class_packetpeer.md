github_url
:   hide

# PacketPeer {#class_PacketPeer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"},
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"},
`PacketPeerDTLS<class_PacketPeerDTLS>`{.interpreted-text role="ref"},
`PacketPeerExtension<class_PacketPeerExtension>`{.interpreted-text
role="ref"},
`PacketPeerStream<class_PacketPeerStream>`{.interpreted-text
role="ref"}, `PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text
role="ref"},
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"}, `WebSocketPeer<class_WebSocketPeer>`{.interpreted-text
role="ref"}

Abstraction and base class for packet-based protocols.

::: rst-class
classref-introduction-group
:::

## Description

PacketPeer is an abstraction and base class for packet-based protocols
(such as UDP). It provides an API for sending and receiving packets both
as raw data or variables. This makes it easy to transfer data over a
protocol, without having to encode data as low-level bytes or having to
worry about network ordering.

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

:::: {#class_PacketPeer_property_encode_buffer_max_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**encode_buffer_max_size** = `8388608`
`🔗<class_PacketPeer_property_encode_buffer_max_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_encode_buffer_max_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_encode_buffer_max_size**()

Maximum buffer size allowed when encoding
`Variant<class_Variant>`{.interpreted-text role="ref"}s. Raise this
value to support heavier memory allocations.

The `put_var()<class_PacketPeer_method_put_var>`{.interpreted-text
role="ref"} method allocates memory on the stack, and the buffer used
will grow automatically to the closest power of two to match the size of
the `Variant<class_Variant>`{.interpreted-text role="ref"}. If the
`Variant<class_Variant>`{.interpreted-text role="ref"} is bigger than
`encode_buffer_max_size<class_PacketPeer_property_encode_buffer_max_size>`{.interpreted-text
role="ref"}, the method will error out with
`@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PacketPeer_method_get_available_packet_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_available_packet_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeer_method_get_available_packet_count>`{.interpreted-text
role="ref"}

Returns the number of packets currently available in the ring-buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeer_method_get_packet}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_packet**()
`🔗<class_PacketPeer_method_get_packet>`{.interpreted-text role="ref"}

Gets a raw packet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeer_method_get_packet_error}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**get_packet_error**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeer_method_get_packet_error>`{.interpreted-text
role="ref"}

Returns the error state of the last packet received (via
`get_packet()<class_PacketPeer_method_get_packet>`{.interpreted-text
role="ref"} and
`get_var()<class_PacketPeer_method_get_var>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeer_method_get_var}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_var**(allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_PacketPeer_method_get_var>`{.interpreted-text role="ref"}

Gets a Variant. If `allow_objects` is `true`, decoding objects is
allowed.

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

:::: {#class_PacketPeer_method_put_packet}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**put_packet**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_PacketPeer_method_put_packet>`{.interpreted-text role="ref"}

Sends a raw packet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeer_method_put_var}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**put_var**(var: `Variant<class_Variant>`{.interpreted-text role="ref"},
full_objects: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PacketPeer_method_put_var>`{.interpreted-text role="ref"}

Sends a `Variant<class_Variant>`{.interpreted-text role="ref"} as a
packet. If `full_objects` is `true`, encoding objects is allowed (and
can potentially include code).

Internally, this uses the same encoding mechanism as the
`@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"} method.
