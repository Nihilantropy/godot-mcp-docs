github_url
:   hide

::: {.meta keywords="network"}
:::

# MultiplayerPeer {#class_MultiplayerPeer}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`ENetMultiplayerPeer<class_ENetMultiplayerPeer>`{.interpreted-text
role="ref"},
`MultiplayerPeerExtension<class_MultiplayerPeerExtension>`{.interpreted-text
role="ref"},
`OfflineMultiplayerPeer<class_OfflineMultiplayerPeer>`{.interpreted-text
role="ref"},
`WebRTCMultiplayerPeer<class_WebRTCMultiplayerPeer>`{.interpreted-text
role="ref"},
`WebSocketMultiplayerPeer<class_WebSocketMultiplayerPeer>`{.interpreted-text
role="ref"}

Abstract class for specialized
`PacketPeer<class_PacketPeer>`{.interpreted-text role="ref"}s used by
the `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Manages the connection with one or more remote peers acting as server or
client and assigning unique IDs to each of them. See also
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
protocol is an implementation detail and isn\'t meant to be used by
non-Godot servers. It may change without notice.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `High-level multiplayer <../tutorials/networking/high_level_multiplayer>`{.interpreted-text
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

## Signals

:::: {#class_MultiplayerPeer_signal_peer_connected}
::: rst-class
classref-signal
:::
::::

**peer_connected**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerPeer_signal_peer_connected>`{.interpreted-text
role="ref"}

Emitted when a remote peer connects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_signal_peer_disconnected}
::: rst-class
classref-signal
:::
::::

**peer_disconnected**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_MultiplayerPeer_signal_peer_disconnected>`{.interpreted-text
role="ref"}

Emitted when a remote peer has disconnected.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_MultiplayerPeer_ConnectionStatus}
::: rst-class
classref-enumeration
:::
::::

enum **ConnectionStatus**:
`🔗<enum_MultiplayerPeer_ConnectionStatus>`{.interpreted-text
role="ref"}

:::: {#class_MultiplayerPeer_constant_CONNECTION_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>`{.interpreted-text
role="ref"} **CONNECTION_DISCONNECTED** = `0`

The MultiplayerPeer is disconnected.

:::: {#class_MultiplayerPeer_constant_CONNECTION_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>`{.interpreted-text
role="ref"} **CONNECTION_CONNECTING** = `1`

The MultiplayerPeer is currently connecting to a server.

:::: {#class_MultiplayerPeer_constant_CONNECTION_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>`{.interpreted-text
role="ref"} **CONNECTION_CONNECTED** = `2`

This MultiplayerPeer is connected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_MultiplayerPeer_TransferMode}
::: rst-class
classref-enumeration
:::
::::

enum **TransferMode**:
`🔗<enum_MultiplayerPeer_TransferMode>`{.interpreted-text role="ref"}

:::: {#class_MultiplayerPeer_constant_TRANSFER_MODE_UNRELIABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **TRANSFER_MODE_UNRELIABLE** = `0`

Packets are not acknowledged, no resend attempts are made for lost
packets. Packets may arrive in any order. Potentially faster than
`TRANSFER_MODE_UNRELIABLE_ORDERED<class_MultiplayerPeer_constant_TRANSFER_MODE_UNRELIABLE_ORDERED>`{.interpreted-text
role="ref"}. Use for non-critical data, and always consider whether the
order matters.

:::: {#class_MultiplayerPeer_constant_TRANSFER_MODE_UNRELIABLE_ORDERED}
::: rst-class
classref-enumeration-constant
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **TRANSFER_MODE_UNRELIABLE_ORDERED** = `1`

Packets are not acknowledged, no resend attempts are made for lost
packets. Packets are received in the order they were sent in.
Potentially faster than
`TRANSFER_MODE_RELIABLE<class_MultiplayerPeer_constant_TRANSFER_MODE_RELIABLE>`{.interpreted-text
role="ref"}. Use for non-critical data or data that would be outdated if
received late due to resend attempt(s) anyway, for example movement and
positional data.

:::: {#class_MultiplayerPeer_constant_TRANSFER_MODE_RELIABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **TRANSFER_MODE_RELIABLE** = `2`

Packets must be received and resend attempts should be made until the
packets are acknowledged. Packets must be received in the order they
were sent in. Most reliable transfer mode, but potentially the slowest
due to the overhead. Use for critical data that must be transmitted and
arrive in order, for example an ability being triggered or a chat
message. Consider carefully if the information really is critical, and
use sparingly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST}
::: rst-class
classref-constant
:::
::::

**TARGET_PEER_BROADCAST** = `0`
`🔗<class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST>`{.interpreted-text
role="ref"}

Packets are sent to all connected peers.

:::: {#class_MultiplayerPeer_constant_TARGET_PEER_SERVER}
::: rst-class
classref-constant
:::
::::

**TARGET_PEER_SERVER** = `1`
`🔗<class_MultiplayerPeer_constant_TARGET_PEER_SERVER>`{.interpreted-text
role="ref"}

Packets are sent to the remote peer acting as server.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MultiplayerPeer_property_refuse_new_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**refuse_new_connections** = `false`
`🔗<class_MultiplayerPeer_property_refuse_new_connections>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_refuse_new_connections**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_refusing_new_connections**()

If `true`, this **MultiplayerPeer** refuses new connections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_property_transfer_channel}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **transfer_channel** =
`0`
`🔗<class_MultiplayerPeer_property_transfer_channel>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transfer_channel**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_transfer_channel**()

The channel to use to send packets. Many network APIs such as ENet and
WebRTC allow the creation of multiple independent channels which
behaves, in a way, like separate connections. This means that reliable
data will only block delivery of other packets on that channel, and
ordering will only be in respect to the channel the packet is being sent
on. Using different channels to send **different and independent** state
updates is a common way to optimize network usage and decrease latency
in fast-paced games.

\*\*Note:\*\* The default channel (`0`) actually works as 3 separate
channels (one for each
`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"}) so that
`TRANSFER_MODE_RELIABLE<class_MultiplayerPeer_constant_TRANSFER_MODE_RELIABLE>`{.interpreted-text
role="ref"} and
`TRANSFER_MODE_UNRELIABLE_ORDERED<class_MultiplayerPeer_constant_TRANSFER_MODE_UNRELIABLE_ORDERED>`{.interpreted-text
role="ref"} does not interact with each other by default. Refer to the
specific network API documentation (e.g. ENet or WebRTC) to learn how to
set up channels correctly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_property_transfer_mode}
::: rst-class
classref-property
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **transfer_mode** = `2`
`🔗<class_MultiplayerPeer_property_transfer_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transfer_mode**(value:
  `TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
  role="ref"})
- `TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
  role="ref"} **get_transfer_mode**()

The manner in which to send packets to the target peer. See the
`set_target_peer()<class_MultiplayerPeer_method_set_target_peer>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MultiplayerPeer_method_close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**()
`🔗<class_MultiplayerPeer_method_close>`{.interpreted-text role="ref"}

Immediately close the multiplayer peer returning to the state
`CONNECTION_DISCONNECTED<class_MultiplayerPeer_constant_CONNECTION_DISCONNECTED>`{.interpreted-text
role="ref"}. Connected peers will be dropped without emitting
`peer_disconnected<class_MultiplayerPeer_signal_peer_disconnected>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_disconnect_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_peer**(peer: `int<class_int>`{.interpreted-text
role="ref"}, force: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_MultiplayerPeer_method_disconnect_peer>`{.interpreted-text
role="ref"}

Disconnects the given `peer` from this host. If `force` is `true` the
`peer_disconnected<class_MultiplayerPeer_signal_peer_disconnected>`{.interpreted-text
role="ref"} signal will not be emitted for this peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_generate_unique_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **generate_unique_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_generate_unique_id>`{.interpreted-text
role="ref"}

Returns a randomly generated integer that can be used as a network
unique ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_get_connection_status}
::: rst-class
classref-method
:::
::::

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>`{.interpreted-text
role="ref"} **get_connection_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_get_connection_status>`{.interpreted-text
role="ref"}

Returns the current state of the connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_get_packet_channel}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_packet_channel**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_get_packet_channel>`{.interpreted-text
role="ref"}

Returns the channel over which the next available packet was received.
See
`PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_get_packet_mode}
::: rst-class
classref-method
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **get_packet_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_get_packet_mode>`{.interpreted-text
role="ref"}

Returns the transfer mode the remote peer used to send the next
available packet. See
`PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_get_packet_peer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_packet_peer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_get_packet_peer>`{.interpreted-text
role="ref"}

Returns the ID of the **MultiplayerPeer** who sent the next available
packet. See
`PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_get_unique_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_unique_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_get_unique_id>`{.interpreted-text
role="ref"}

Returns the ID of this **MultiplayerPeer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_is_server_relay_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_server_relay_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeer_method_is_server_relay_supported>`{.interpreted-text
role="ref"}

Returns `true` if the server can act as a relay in the current
configuration. That is, if the higher level
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
should notify connected clients of other peers, and implement a relay
protocol to allow communication between them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_poll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **poll**()
`🔗<class_MultiplayerPeer_method_poll>`{.interpreted-text role="ref"}

Waits up to 1 second to receive a new network event.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeer_method_set_target_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_target_peer**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerPeer_method_set_target_peer>`{.interpreted-text
role="ref"}

Sets the peer to which packets will be sent.

The `id` can be one of:
`TARGET_PEER_BROADCAST<class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST>`{.interpreted-text
role="ref"} to send to all connected peers,
`TARGET_PEER_SERVER<class_MultiplayerPeer_constant_TARGET_PEER_SERVER>`{.interpreted-text
role="ref"} to send to the peer acting as server, a valid peer ID to
send to that specific peer, a negative peer ID to send to all peers
except that one. By default, the target peer is
`TARGET_PEER_BROADCAST<class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST>`{.interpreted-text
role="ref"}.
