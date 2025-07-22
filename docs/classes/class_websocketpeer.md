github_url
:   hide

# WebSocketPeer {#class_WebSocketPeer}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A WebSocket connection.

::: rst-class
classref-introduction-group
:::

## Description

This class represents WebSocket connection, and can be used as a
WebSocket client (RFC 6455-compliant) or as a remote peer of a WebSocket
server.

You can send WebSocket binary frames using
`PacketPeer.put_packet()<class_PacketPeer_method_put_packet>`{.interpreted-text
role="ref"}, and WebSocket text frames using
`send()<class_WebSocketPeer_method_send>`{.interpreted-text role="ref"}
(prefer text frames when interacting with text-based API). You can check
the frame type of the last packet via
`was_string_packet()<class_WebSocketPeer_method_was_string_packet>`{.interpreted-text
role="ref"}.

To start a WebSocket client, first call
`connect_to_url()<class_WebSocketPeer_method_connect_to_url>`{.interpreted-text
role="ref"}, then regularly call
`poll()<class_WebSocketPeer_method_poll>`{.interpreted-text role="ref"}
(e.g. during `Node<class_Node>`{.interpreted-text role="ref"} process).
You can query the socket state via
`get_ready_state()<class_WebSocketPeer_method_get_ready_state>`{.interpreted-text
role="ref"}, get the number of pending packets using
`PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`{.interpreted-text
role="ref"}, and retrieve them via
`PacketPeer.get_packet()<class_PacketPeer_method_get_packet>`{.interpreted-text
role="ref"}.

:::: tabs
::: code-tab
gdscript

extends Node

var socket = WebSocketPeer.new()

func [ready]{#ready}():

:   socket.connect_to_url(\"wss://example.com\")

func [process]{#process}(delta):

:   socket.poll() var state = socket.get_ready_state() if state ==
    WebSocketPeer.STATE_OPEN: while socket.get_available_packet_count():
    print(\"Packet: \", socket.get_packet()) elif state ==
    WebSocketPeer.STATE_CLOSING: \# Keep polling to achieve proper
    close. pass elif state == WebSocketPeer.STATE_CLOSED: var code =
    socket.get_close_code() var reason = socket.get_close_reason()
    print(\"WebSocket closed with code: %d, reason %s. Clean: %s\" %
    \[code, reason, code != -1\]) set_process(false) \# Stop processing.
:::
::::

To use the peer as part of a WebSocket server refer to
`accept_stream()<class_WebSocketPeer_method_accept_stream>`{.interpreted-text
role="ref"} and the online tutorial.

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

:::: {#enum_WebSocketPeer_WriteMode}
::: rst-class
classref-enumeration
:::
::::

enum **WriteMode**: `🔗<enum_WebSocketPeer_WriteMode>`{.interpreted-text
role="ref"}

:::: {#class_WebSocketPeer_constant_WRITE_MODE_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`WriteMode<enum_WebSocketPeer_WriteMode>`{.interpreted-text role="ref"}
**WRITE_MODE_TEXT** = `0`

Specifies that WebSockets messages should be transferred as text payload
(only valid UTF-8 is allowed).

:::: {#class_WebSocketPeer_constant_WRITE_MODE_BINARY}
::: rst-class
classref-enumeration-constant
:::
::::

`WriteMode<enum_WebSocketPeer_WriteMode>`{.interpreted-text role="ref"}
**WRITE_MODE_BINARY** = `1`

Specifies that WebSockets messages should be transferred as binary
payload (any byte combination is allowed).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_WebSocketPeer_State}
::: rst-class
classref-enumeration
:::
::::

enum **State**: `🔗<enum_WebSocketPeer_State>`{.interpreted-text
role="ref"}

:::: {#class_WebSocketPeer_constant_STATE_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`State<enum_WebSocketPeer_State>`{.interpreted-text role="ref"}
**STATE_CONNECTING** = `0`

Socket has been created. The connection is not yet open.

:::: {#class_WebSocketPeer_constant_STATE_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`State<enum_WebSocketPeer_State>`{.interpreted-text role="ref"}
**STATE_OPEN** = `1`

The connection is open and ready to communicate.

:::: {#class_WebSocketPeer_constant_STATE_CLOSING}
::: rst-class
classref-enumeration-constant
:::
::::

`State<enum_WebSocketPeer_State>`{.interpreted-text role="ref"}
**STATE_CLOSING** = `2`

The connection is in the process of closing. This means a close request
has been sent to the remote peer but confirmation has not been received.

:::: {#class_WebSocketPeer_constant_STATE_CLOSED}
::: rst-class
classref-enumeration-constant
:::
::::

`State<enum_WebSocketPeer_State>`{.interpreted-text role="ref"}
**STATE_CLOSED** = `3`

The connection is closed or couldn\'t be opened.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_WebSocketPeer_property_handshake_headers}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **handshake_headers** = `PackedStringArray()`
`🔗<class_WebSocketPeer_property_handshake_headers>`{.interpreted-text
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

The extra HTTP headers to be sent during the WebSocket handshake.

\*\*Note:\*\* Not supported in Web exports due to browsers\'
restrictions.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_property_heartbeat_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**heartbeat_interval** = `0.0`
`🔗<class_WebSocketPeer_property_heartbeat_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_heartbeat_interval**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_heartbeat_interval**()

The interval (in seconds) at which the peer will automatically send
WebSocket \"ping\" control frames. When set to `0`, no \"ping\" control
frames will be sent.

\*\*Note:\*\* Has no effect in Web exports due to browser restrictions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_property_inbound_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **inbound_buffer_size** =
`65535`
`🔗<class_WebSocketPeer_property_inbound_buffer_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inbound_buffer_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_inbound_buffer_size**()

The size of the input buffer in bytes (roughly the maximum amount of
memory that will be allocated for the inbound packets).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_property_max_queued_packets}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_queued_packets** =
`4096`
`🔗<class_WebSocketPeer_property_max_queued_packets>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_queued_packets**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_queued_packets**()

The maximum amount of packets that will be allowed in the queues (both
inbound and outbound).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_property_outbound_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outbound_buffer_size**
= `65535`
`🔗<class_WebSocketPeer_property_outbound_buffer_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outbound_buffer_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_outbound_buffer_size**()

The size of the input buffer in bytes (roughly the maximum amount of
memory that will be allocated for the outbound packets).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_property_supported_protocols}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **supported_protocols** = `PackedStringArray()`
`🔗<class_WebSocketPeer_property_supported_protocols>`{.interpreted-text
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

The WebSocket sub-protocols allowed during the WebSocket handshake.

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

:::: {#class_WebSocketPeer_method_accept_stream}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**accept_stream**(stream:
`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"})
`🔗<class_WebSocketPeer_method_accept_stream>`{.interpreted-text
role="ref"}

Accepts a peer connection performing the HTTP handshake as a WebSocket
server. The `stream` must be a valid TCP stream retrieved via
`TCPServer.take_connection()<class_TCPServer_method_take_connection>`{.interpreted-text
role="ref"}, or a TLS stream accepted via
`StreamPeerTLS.accept_stream()<class_StreamPeerTLS_method_accept_stream>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Not supported in Web exports due to browsers\'
restrictions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**(code:
`int<class_int>`{.interpreted-text role="ref"} = 1000, reason:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_WebSocketPeer_method_close>`{.interpreted-text role="ref"}

Closes this WebSocket connection. `code` is the status code for the
closure (see RFC 6455 section 7.4 for a list of valid status codes).
`reason` is the human readable reason for closing the connection (can be
any UTF-8 string that\'s smaller than 123 bytes). If `code` is negative,
the connection will be closed immediately without notifying the remote
peer.

\*\*Note:\*\* To achieve a clean close, you will need to keep polling
until
`STATE_CLOSED<class_WebSocketPeer_constant_STATE_CLOSED>`{.interpreted-text
role="ref"} is reached.

\*\*Note:\*\* The Web export might not support all status codes. Please
refer to browser-specific documentation for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_connect_to_url}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_to_url**(url: `String<class_String>`{.interpreted-text
role="ref"}, tls_client_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"} = null)
`🔗<class_WebSocketPeer_method_connect_to_url>`{.interpreted-text
role="ref"}

Connects to the given URL. TLS certificates will be verified against the
hostname when connecting using the `wss://` protocol. You can pass the
optional `tls_client_options` parameter to customize the trusted
certification authorities, or disable the common name verification. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"} and
`TLSOptions.client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is non-blocking, and will return
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} before the connection is established as long as the provided
parameters are valid and the peer is not in an invalid state (e.g.
already connected). Regularly call
`poll()<class_WebSocketPeer_method_poll>`{.interpreted-text role="ref"}
(e.g. during `Node<class_Node>`{.interpreted-text role="ref"} process)
and check the result of
`get_ready_state()<class_WebSocketPeer_method_get_ready_state>`{.interpreted-text
role="ref"} to know whether the connection succeeds or fails.

\*\*Note:\*\* To avoid mixed content warnings or errors in Web, you may
have to use a `url` that starts with `wss://` (secure) instead of
`ws://`. When doing so, make sure to use the fully qualified domain name
that matches the one defined in the server\'s TLS certificate. Do not
connect directly via the IP address for `wss://` connections, as it
won\'t match with the TLS certificate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_close_code}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_close_code**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_close_code>`{.interpreted-text
role="ref"}

Returns the received WebSocket close frame status code, or `-1` when the
connection was not cleanly closed. Only call this method when
`get_ready_state()<class_WebSocketPeer_method_get_ready_state>`{.interpreted-text
role="ref"} returns
`STATE_CLOSED<class_WebSocketPeer_constant_STATE_CLOSED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_close_reason}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_close_reason**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_close_reason>`{.interpreted-text
role="ref"}

Returns the received WebSocket close frame status reason string. Only
call this method when
`get_ready_state()<class_WebSocketPeer_method_get_ready_state>`{.interpreted-text
role="ref"} returns
`STATE_CLOSED<class_WebSocketPeer_constant_STATE_CLOSED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_connected_host}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_connected_host**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_connected_host>`{.interpreted-text
role="ref"}

Returns the IP address of the connected peer.

\*\*Note:\*\* Not available in the Web export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_connected_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_connected_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_connected_port>`{.interpreted-text
role="ref"}

Returns the remote port of the connected peer.

\*\*Note:\*\* Not available in the Web export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_current_outbound_buffered_amount}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_current_outbound_buffered_amount**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_current_outbound_buffered_amount>`{.interpreted-text
role="ref"}

Returns the current amount of data in the outbound websocket buffer.
**Note:** Web exports use WebSocket.bufferedAmount, while other
platforms use an internal buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_ready_state}
::: rst-class
classref-method
:::
::::

`State<enum_WebSocketPeer_State>`{.interpreted-text role="ref"}
**get_ready_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_ready_state>`{.interpreted-text
role="ref"}

Returns the ready state of the connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_requested_url}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_requested_url**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_requested_url>`{.interpreted-text
role="ref"}

Returns the URL requested by this peer. The URL is derived from the
`url` passed to
`connect_to_url()<class_WebSocketPeer_method_connect_to_url>`{.interpreted-text
role="ref"} or from the HTTP headers when acting as server (i.e. when
using
`accept_stream()<class_WebSocketPeer_method_accept_stream>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_get_selected_protocol}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_selected_protocol**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_get_selected_protocol>`{.interpreted-text
role="ref"}

Returns the selected WebSocket sub-protocol for this connection or an
empty string if the sub-protocol has not been selected yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_poll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **poll**()
`🔗<class_WebSocketPeer_method_poll>`{.interpreted-text role="ref"}

Updates the connection state and receive incoming packets. Call this
function regularly to keep it in a clean state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_send}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**send**(message:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
write_mode: `WriteMode<enum_WebSocketPeer_WriteMode>`{.interpreted-text
role="ref"} = 1) `🔗<class_WebSocketPeer_method_send>`{.interpreted-text
role="ref"}

Sends the given `message` using the desired `write_mode`. When sending a
`String<class_String>`{.interpreted-text role="ref"}, prefer using
`send_text()<class_WebSocketPeer_method_send_text>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_send_text}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**send_text**(message: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_WebSocketPeer_method_send_text>`{.interpreted-text role="ref"}

Sends the given `message` using WebSocket text mode. Prefer this method
over
`PacketPeer.put_packet()<class_PacketPeer_method_put_packet>`{.interpreted-text
role="ref"} when interacting with third-party text-based API (e.g. when
using `JSON<class_JSON>`{.interpreted-text role="ref"} formatted
messages).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_set_no_delay}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_no_delay**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_WebSocketPeer_method_set_no_delay>`{.interpreted-text
role="ref"}

Disable Nagle\'s algorithm on the underlying TCP socket (default). See
`StreamPeerTCP.set_no_delay()<class_StreamPeerTCP_method_set_no_delay>`{.interpreted-text
role="ref"} for more information.

\*\*Note:\*\* Not available in the Web export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebSocketPeer_method_was_string_packet}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **was_string_packet**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebSocketPeer_method_was_string_packet>`{.interpreted-text
role="ref"}

Returns `true` if the last received packet was sent as a text payload.
See `WriteMode<enum_WebSocketPeer_WriteMode>`{.interpreted-text
role="ref"}.
