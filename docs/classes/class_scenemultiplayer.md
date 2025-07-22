github_url
:   hide

# SceneMultiplayer {#class_SceneMultiplayer}

**Inherits:** `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

High-level multiplayer API implementation.

::: rst-class
classref-introduction-group
:::

## Description

This class is the default implementation of
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"},
used to provide multiplayer functionalities in Godot Engine.

This implementation supports RPCs via
`Node.rpc()<class_Node_method_rpc>`{.interpreted-text role="ref"} and
`Node.rpc_id()<class_Node_method_rpc_id>`{.interpreted-text role="ref"}
and requires
`MultiplayerAPI.rpc()<class_MultiplayerAPI_method_rpc>`{.interpreted-text
role="ref"} to be passed a `Node<class_Node>`{.interpreted-text
role="ref"} (it will fail for other object types).

This implementation additionally provide
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} replication
via the `MultiplayerSpawner<class_MultiplayerSpawner>`{.interpreted-text
role="ref"} and
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"} nodes, and the
`SceneReplicationConfig<class_SceneReplicationConfig>`{.interpreted-text
role="ref"} resource.

\*\*Note:\*\* The high-level multiplayer API protocol is an
implementation detail and isn\'t meant to be used by non-Godot servers.
It may change without notice.

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

## Signals

:::: {#class_SceneMultiplayer_signal_peer_authenticating}
::: rst-class
classref-signal
:::
::::

**peer_authenticating**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SceneMultiplayer_signal_peer_authenticating>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} connects to a new peer and a valid
`auth_callback<class_SceneMultiplayer_property_auth_callback>`{.interpreted-text
role="ref"} is set. In this case, the
`MultiplayerAPI.peer_connected<class_MultiplayerAPI_signal_peer_connected>`{.interpreted-text
role="ref"} will not be emitted until
`complete_auth()<class_SceneMultiplayer_method_complete_auth>`{.interpreted-text
role="ref"} is called with given peer `id`. While in this state, the
peer will not be included in the list returned by
`MultiplayerAPI.get_peers()<class_MultiplayerAPI_method_get_peers>`{.interpreted-text
role="ref"} (but in the one returned by
`get_authenticating_peers()<class_SceneMultiplayer_method_get_authenticating_peers>`{.interpreted-text
role="ref"}), and only authentication data will be sent or received. See
`send_auth()<class_SceneMultiplayer_method_send_auth>`{.interpreted-text
role="ref"} for sending authentication data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_signal_peer_authentication_failed}
::: rst-class
classref-signal
:::
::::

**peer_authentication_failed**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SceneMultiplayer_signal_peer_authentication_failed>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} disconnects from a peer for which authentication had not yet
completed. See
`peer_authenticating<class_SceneMultiplayer_signal_peer_authenticating>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_signal_peer_packet}
::: rst-class
classref-signal
:::
::::

**peer_packet**(id: `int<class_int>`{.interpreted-text role="ref"},
packet: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"})
`🔗<class_SceneMultiplayer_signal_peer_packet>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} receives a `packet` with custom data (see
`send_bytes()<class_SceneMultiplayer_method_send_bytes>`{.interpreted-text
role="ref"}). ID is the peer ID of the peer that sent the packet.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SceneMultiplayer_property_allow_object_decoding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_object_decoding** = `false`
`🔗<class_SceneMultiplayer_property_allow_object_decoding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_object_decoding**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_object_decoding_allowed**()

If `true`, the MultiplayerAPI will allow encoding and decoding of object
during RPCs.

\*\*Warning:\*\* Deserialized objects can contain code which gets
executed. Do not use this option if the serialized object comes from
untrusted sources to avoid potential security threat such as remote code
execution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_auth_callback}
::: rst-class
classref-property
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**auth_callback** = `Callable()`
`🔗<class_SceneMultiplayer_property_auth_callback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auth_callback**(value:
  `Callable<class_Callable>`{.interpreted-text role="ref"})
- `Callable<class_Callable>`{.interpreted-text role="ref"}
  **get_auth_callback**()

The callback to execute when receiving authentication data sent via
`send_auth()<class_SceneMultiplayer_method_send_auth>`{.interpreted-text
role="ref"}. If the `Callable<class_Callable>`{.interpreted-text
role="ref"} is empty (default), peers will be automatically accepted as
soon as they connect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_auth_timeout}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **auth_timeout** =
`3.0`
`🔗<class_SceneMultiplayer_property_auth_timeout>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auth_timeout**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auth_timeout**()

If set to a value greater than `0.0`, the maximum duration in seconds
peers can stay in the authenticating state, after which the
authentication will automatically fail. See the
`peer_authenticating<class_SceneMultiplayer_signal_peer_authenticating>`{.interpreted-text
role="ref"} and
`peer_authentication_failed<class_SceneMultiplayer_signal_peer_authentication_failed>`{.interpreted-text
role="ref"} signals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_max_delta_packet_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_delta_packet_size**
= `65535`
`🔗<class_SceneMultiplayer_property_max_delta_packet_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_delta_packet_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_delta_packet_size**()

Maximum size of each delta packet. Higher values increase the chance of
receiving full updates in a single frame, but also the chance of causing
networking congestion (higher latency, disconnections). See
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_max_sync_packet_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_sync_packet_size**
= `1350`
`🔗<class_SceneMultiplayer_property_max_sync_packet_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_sync_packet_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_sync_packet_size**()

Maximum size of each synchronization packet. Higher values increase the
chance of receiving full updates in a single frame, but also the chance
of packet loss. See
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_refuse_new_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**refuse_new_connections** = `false`
`🔗<class_SceneMultiplayer_property_refuse_new_connections>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_refuse_new_connections**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_refusing_new_connections**()

If `true`, the MultiplayerAPI\'s
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} refuses new incoming connections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_root_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **root_path** =
`NodePath("")`
`🔗<class_SceneMultiplayer_property_root_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_path**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_root_path**()

The root path to use for RPCs and replication. Instead of an absolute
path, a relative path will be used to find the node upon which the RPC
should be executed.

This effectively allows to have different branches of the scene tree to
be managed by different MultiplayerAPI, allowing for example to run both
client and server in the same scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_property_server_relay}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **server_relay** =
`true`
`🔗<class_SceneMultiplayer_property_server_relay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_server_relay_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_server_relay_enabled**()

Enable or disable the server feature that notifies clients of other
peers\' connection/disconnection, and relays messages between them. When
this option is `false`, clients won\'t be automatically notified of
other peers and won\'t be able to send them packets through the server.

\*\*Note:\*\* Changing this option while other peers are connected may
lead to unexpected behaviors.

\*\*Note:\*\* Support for this feature may depend on the current
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
configuration. See
`MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SceneMultiplayer_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_SceneMultiplayer_method_clear>`{.interpreted-text role="ref"}

Clears the current SceneMultiplayer network state (you shouldn\'t call
this unless you know what you are doing).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_method_complete_auth}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**complete_auth**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SceneMultiplayer_method_complete_auth>`{.interpreted-text
role="ref"}

Mark the authentication step as completed for the remote peer identified
by `id`. The
`MultiplayerAPI.peer_connected<class_MultiplayerAPI_signal_peer_connected>`{.interpreted-text
role="ref"} signal will be emitted for this peer once the remote side
also completes the authentication. No further authentication messages
are expected to be received from this peer.

If a peer disconnects before completing authentication, either due to a
network issue, the
`auth_timeout<class_SceneMultiplayer_property_auth_timeout>`{.interpreted-text
role="ref"} expiring, or manually calling
`disconnect_peer()<class_SceneMultiplayer_method_disconnect_peer>`{.interpreted-text
role="ref"}, the
`peer_authentication_failed<class_SceneMultiplayer_signal_peer_authentication_failed>`{.interpreted-text
role="ref"} signal will be emitted instead of
`MultiplayerAPI.peer_disconnected<class_MultiplayerAPI_signal_peer_disconnected>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_method_disconnect_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_peer**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SceneMultiplayer_method_disconnect_peer>`{.interpreted-text
role="ref"}

Disconnects the peer identified by `id`, removing it from the list of
connected peers, and closing the underlying connection with it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_method_get_authenticating_peers}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_authenticating_peers**()
`🔗<class_SceneMultiplayer_method_get_authenticating_peers>`{.interpreted-text
role="ref"}

Returns the IDs of the peers currently trying to authenticate with this
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_method_send_auth}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**send_auth**(id: `int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_SceneMultiplayer_method_send_auth>`{.interpreted-text
role="ref"}

Sends the specified `data` to the remote peer identified by `id` as part
of an authentication message. This can be used to authenticate peers,
and control when
`MultiplayerAPI.peer_connected<class_MultiplayerAPI_signal_peer_connected>`{.interpreted-text
role="ref"} is emitted (and the remote peer accepted as one of the
connected peers).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneMultiplayer_method_send_bytes}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**send_bytes**(bytes:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
id: `int<class_int>`{.interpreted-text role="ref"} = 0, mode:
`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} = 2, channel: `int<class_int>`{.interpreted-text role="ref"}
= 0) `🔗<class_SceneMultiplayer_method_send_bytes>`{.interpreted-text
role="ref"}

Sends the given raw `bytes` to a specific peer identified by `id` (see
`MultiplayerPeer.set_target_peer()<class_MultiplayerPeer_method_set_target_peer>`{.interpreted-text
role="ref"}). Default ID is `0`, i.e. broadcast to all peers.
