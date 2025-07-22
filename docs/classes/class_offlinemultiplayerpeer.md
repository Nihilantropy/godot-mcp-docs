github_url
:   hide

# OfflineMultiplayerPeer {#class_OfflineMultiplayerPeer}

**Inherits:** `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text
role="ref"} **\<** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
which is always connected and acts as a server.

::: rst-class
classref-introduction-group
:::

## Description

This is the default
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} for the
`Node.multiplayer<class_Node_property_multiplayer>`{.interpreted-text
role="ref"}. It mimics the behavior of a server with no peers connected.

This means that the `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"} will act as the multiplayer authority by default. Calls to
`MultiplayerAPI.is_server()<class_MultiplayerAPI_method_is_server>`{.interpreted-text
role="ref"} will return `true`, and calls to
`MultiplayerAPI.get_unique_id()<class_MultiplayerAPI_method_get_unique_id>`{.interpreted-text
role="ref"} will return
`MultiplayerPeer.TARGET_PEER_SERVER<class_MultiplayerPeer_constant_TARGET_PEER_SERVER>`{.interpreted-text
role="ref"}.
