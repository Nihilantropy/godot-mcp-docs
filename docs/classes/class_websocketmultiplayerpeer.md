github_url
:   hide

# WebSocketMultiplayerPeer {#class_WebSocketMultiplayerPeer}

**Inherits:** `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text
role="ref"} **\<** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class for WebSocket server and client.

::: rst-class
classref-introduction-group
:::

## Description

Base class for WebSocket server and client, allowing them to be used as
multiplayer peer for the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

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

:::: {#class_WebSocketMultiplayerPeer_property_handshake_headers}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **handshake_headers** = `PackedStringArray()`
`🔗<class_WebSocketMultiplayerPeer_property_handshake_headers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_handshake_headers**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_handshake_headers**()

The extra headers to use during handshake. See
`WebSocketPeer.handshake_headers<class_WebSocketPeer_property_handshake_headers>`{.interpreted-text
role="ref"} for more details.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_property_handshake_timeout}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **handshake_timeout**
= `3.0`
`🔗<class_WebSocketMultiplayerPeer_property_handshake_timeout>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_handshake_timeout**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_handshake_timeout**()

The maximum time each peer can stay in a connecting state before being
dropped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_property_inbound_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **inbound_buffer_size** =
`65535`
`🔗<class_WebSocketMultiplayerPeer_property_inbound_buffer_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inbound_buffer_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_inbound_buffer_size**()

The inbound buffer size for connected peers. See
`WebSocketPeer.inbound_buffer_size<class_WebSocketPeer_property_inbound_buffer_size>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_property_max_queued_packets}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_queued_packets** =
`4096`
`🔗<class_WebSocketMultiplayerPeer_property_max_queued_packets>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_queued_packets**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_queued_packets**()

The maximum number of queued packets for connected peers. See
`WebSocketPeer.max_queued_packets<class_WebSocketPeer_property_max_queued_packets>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_property_outbound_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outbound_buffer_size**
= `65535`
`🔗<class_WebSocketMultiplayerPeer_property_outbound_buffer_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outbound_buffer_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_outbound_buffer_size**()

The outbound buffer size for connected peers. See
`WebSocketPeer.outbound_buffer_size<class_WebSocketPeer_property_outbound_buffer_size>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_property_supported_protocols}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **supported_protocols** = `PackedStringArray()`
`🔗<class_WebSocketMultiplayerPeer_property_supported_protocols>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_supported_protocols**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_supported_protocols**()

The supported WebSocket sub-protocols. See
`WebSocketPeer.supported_protocols<class_WebSocketPeer_property_supported_protocols>`{.interpreted-text
role="ref"} for more details.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_WebSocketMultiplayerPeer_method_create_client}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_client**(url: `String<class_String>`{.interpreted-text
role="ref"}, tls_client_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"} = null)
`🔗<class_WebSocketMultiplayerPeer_method_create_client>`{.interpreted-text
role="ref"}

Starts a new multiplayer client connecting to the given `url`. TLS
certificates will be verified against the hostname when connecting using
the `wss://` protocol. You can pass the optional `tls_client_options`
parameter to customize the trusted certification authorities, or disable
the common name verification. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"} and
`TLSOptions.client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It is recommended to specify the scheme part of the URL,
i.e. the `url` should start with either `ws://` or `wss://`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_method_create_server}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_server**(port: `int<class_int>`{.interpreted-text role="ref"},
bind_address: `String<class_String>`{.interpreted-text role="ref"} =
\"\*\", tls_server_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"} = null)
`🔗<class_WebSocketMultiplayerPeer_method_create_server>`{.interpreted-text
role="ref"}

Starts a new multiplayer server listening on the given `port`. You can
optionally specify a `bind_address`, and provide valid
`tls_server_options` to use TLS. See
`TLSOptions.server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_method_get_peer}
::: rst-class
classref-method
:::
::::

`WebSocketPeer<class_WebSocketPeer>`{.interpreted-text role="ref"}
**get_peer**(peer_id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketMultiplayerPeer_method_get_peer>`{.interpreted-text
role="ref"}

Returns the `WebSocketPeer<class_WebSocketPeer>`{.interpreted-text
role="ref"} associated to the given `peer_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_method_get_peer_address}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_peer_address**(id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketMultiplayerPeer_method_get_peer_address>`{.interpreted-text
role="ref"}

Returns the IP address of the given peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketMultiplayerPeer_method_get_peer_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_peer_port**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketMultiplayerPeer_method_get_peer_port>`{.interpreted-text
role="ref"}

Returns the remote port of the given peer.
