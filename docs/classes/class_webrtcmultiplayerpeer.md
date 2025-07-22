github_url
:   hide

# WebRTCMultiplayerPeer {#class_WebRTCMultiplayerPeer}

**Inherits:** `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text
role="ref"} **\<** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A simple interface to create a peer-to-peer mesh network composed of
`WebRTCPeerConnection<class_WebRTCPeerConnection>`{.interpreted-text
role="ref"} that is compatible with the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This class constructs a full mesh of
`WebRTCPeerConnection<class_WebRTCPeerConnection>`{.interpreted-text
role="ref"} (one connection for each peer) that can be used as a
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"}.

You can add each
`WebRTCPeerConnection<class_WebRTCPeerConnection>`{.interpreted-text
role="ref"} via
`add_peer()<class_WebRTCMultiplayerPeer_method_add_peer>`{.interpreted-text
role="ref"} or remove them via
`remove_peer()<class_WebRTCMultiplayerPeer_method_remove_peer>`{.interpreted-text
role="ref"}. Peers must be added in
`WebRTCPeerConnection.STATE_NEW<class_WebRTCPeerConnection_constant_STATE_NEW>`{.interpreted-text
role="ref"} state to allow it to create the appropriate channels. This
class will not create offers nor set descriptions, it will only poll
them, and notify connections and disconnections.

When creating the peer via
`create_client()<class_WebRTCMultiplayerPeer_method_create_client>`{.interpreted-text
role="ref"} or
`create_server()<class_WebRTCMultiplayerPeer_method_create_server>`{.interpreted-text
role="ref"} the
`MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>`{.interpreted-text
role="ref"} method will return `true` enabling peer exchange and packet
relaying when supported by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
implementation.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

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

:::: {#class_WebRTCMultiplayerPeer_method_add_peer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_peer**(peer:
`WebRTCPeerConnection<class_WebRTCPeerConnection>`{.interpreted-text
role="ref"}, peer_id: `int<class_int>`{.interpreted-text role="ref"},
unreliable_lifetime: `int<class_int>`{.interpreted-text role="ref"} = 1)
`🔗<class_WebRTCMultiplayerPeer_method_add_peer>`{.interpreted-text
role="ref"}

Add a new peer to the mesh with the given `peer_id`. The
`WebRTCPeerConnection<class_WebRTCPeerConnection>`{.interpreted-text
role="ref"} must be in state
`WebRTCPeerConnection.STATE_NEW<class_WebRTCPeerConnection_constant_STATE_NEW>`{.interpreted-text
role="ref"}.

Three channels will be created for reliable, unreliable, and ordered
transport. The value of `unreliable_lifetime` will be passed to the
`"maxPacketLifetime"` option when creating unreliable and ordered
channels (see
`WebRTCPeerConnection.create_data_channel()<class_WebRTCPeerConnection_method_create_data_channel>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_create_client}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_client**(peer_id: `int<class_int>`{.interpreted-text
role="ref"}, channels_config: `Array<class_Array>`{.interpreted-text
role="ref"} = \[\])
`🔗<class_WebRTCMultiplayerPeer_method_create_client>`{.interpreted-text
role="ref"}

Initialize the multiplayer peer as a client with the given `peer_id`
(must be between 2 and 2147483647). In this mode, you should only call
`add_peer()<class_WebRTCMultiplayerPeer_method_add_peer>`{.interpreted-text
role="ref"} once and with `peer_id` of `1`. This mode enables
`MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>`{.interpreted-text
role="ref"}, allowing the upper
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
layer to perform peer exchange and packet relaying.

You can optionally specify a `channels_config` array of
`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} which will be used to create extra channels (WebRTC only
supports one transfer mode per channel).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_create_mesh}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_mesh**(peer_id: `int<class_int>`{.interpreted-text role="ref"},
channels_config: `Array<class_Array>`{.interpreted-text role="ref"} =
\[\])
`🔗<class_WebRTCMultiplayerPeer_method_create_mesh>`{.interpreted-text
role="ref"}

Initialize the multiplayer peer as a mesh (i.e. all peers connect to
each other) with the given `peer_id` (must be between 1 and 2147483647).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_create_server}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_server**(channels_config:
`Array<class_Array>`{.interpreted-text role="ref"} = \[\])
`🔗<class_WebRTCMultiplayerPeer_method_create_server>`{.interpreted-text
role="ref"}

Initialize the multiplayer peer as a server (with unique ID of `1`).
This mode enables
`MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>`{.interpreted-text
role="ref"}, allowing the upper
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
layer to perform peer exchange and packet relaying.

You can optionally specify a `channels_config` array of
`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} which will be used to create extra channels (WebRTC only
supports one transfer mode per channel).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_get_peer}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_peer**(peer_id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_WebRTCMultiplayerPeer_method_get_peer>`{.interpreted-text
role="ref"}

Returns a dictionary representation of the peer with given `peer_id`
with three keys. `"connection"` containing the
`WebRTCPeerConnection<class_WebRTCPeerConnection>`{.interpreted-text
role="ref"} to this peer, `"channels"` an array of three
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"}, and `"connected"` a boolean representing if the peer
connection is currently connected (all three channels are open).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_get_peers}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_peers**()
`🔗<class_WebRTCMultiplayerPeer_method_get_peers>`{.interpreted-text
role="ref"}

Returns a dictionary which keys are the peer ids and values the peer
representation as in
`get_peer()<class_WebRTCMultiplayerPeer_method_get_peer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_has_peer}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_peer**(peer_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_WebRTCMultiplayerPeer_method_has_peer>`{.interpreted-text
role="ref"}

Returns `true` if the given `peer_id` is in the peers map (it might not
be connected though).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCMultiplayerPeer_method_remove_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_peer**(peer_id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_WebRTCMultiplayerPeer_method_remove_peer>`{.interpreted-text
role="ref"}

Remove the peer with given `peer_id` from the mesh. If the peer was
connected, and
`MultiplayerPeer.peer_connected<class_MultiplayerPeer_signal_peer_connected>`{.interpreted-text
role="ref"} was emitted for it, then
`MultiplayerPeer.peer_disconnected<class_MultiplayerPeer_signal_peer_disconnected>`{.interpreted-text
role="ref"} will be emitted.
