github_url
:   hide

::: {.meta keywords="network"}
:::

# MultiplayerAPI {#class_MultiplayerAPI}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`MultiplayerAPIExtension<class_MultiplayerAPIExtension>`{.interpreted-text
role="ref"},
`SceneMultiplayer<class_SceneMultiplayer>`{.interpreted-text role="ref"}

High-level multiplayer API interface.

::: rst-class
classref-introduction-group
:::

## Description

Base class for high-level multiplayer API implementations. See also
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}.

By default, `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
has a reference to an implementation of this class and uses it to
provide multiplayer capabilities (i.e. RPCs) across the whole scene.

It is possible to override the MultiplayerAPI instance used by specific
tree branches by calling the
`SceneTree.set_multiplayer()<class_SceneTree_method_set_multiplayer>`{.interpreted-text
role="ref"} method, effectively allowing to run both client and server
in the same scene.

It is also possible to extend or replace the default implementation via
scripting or native extensions. See
`MultiplayerAPIExtension<class_MultiplayerAPIExtension>`{.interpreted-text
role="ref"} for details about extensions,
`SceneMultiplayer<class_SceneMultiplayer>`{.interpreted-text role="ref"}
for the details about the default implementation.

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

:::: {#class_MultiplayerAPI_signal_connected_to_server}
::: rst-class
classref-signal
:::
::::

**connected_to_server**()
`🔗<class_MultiplayerAPI_signal_connected_to_server>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} successfully connected to a server. Only emitted on clients.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_signal_connection_failed}
::: rst-class
classref-signal
:::
::::

**connection_failed**()
`🔗<class_MultiplayerAPI_signal_connection_failed>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} fails to establish a connection to a server. Only emitted on
clients.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_signal_peer_connected}
::: rst-class
classref-signal
:::
::::

**peer_connected**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerAPI_signal_peer_connected>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} connects with a new peer. ID is the peer ID of the new peer.
Clients get notified when other clients connect to the same server. Upon
connecting to a server, a client also receives this signal for the
server (with ID being 1).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_signal_peer_disconnected}
::: rst-class
classref-signal
:::
::::

**peer_disconnected**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_MultiplayerAPI_signal_peer_disconnected>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} disconnects from a peer. Clients get notified when other
clients disconnect from the same server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_signal_server_disconnected}
::: rst-class
classref-signal
:::
::::

**server_disconnected**()
`🔗<class_MultiplayerAPI_signal_server_disconnected>`{.interpreted-text
role="ref"}

Emitted when this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} disconnects from server. Only emitted on clients.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_MultiplayerAPI_RPCMode}
::: rst-class
classref-enumeration
:::
::::

enum **RPCMode**: `🔗<enum_MultiplayerAPI_RPCMode>`{.interpreted-text
role="ref"}

:::: {#class_MultiplayerAPI_constant_RPC_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`RPCMode<enum_MultiplayerAPI_RPCMode>`{.interpreted-text role="ref"}
**RPC_MODE_DISABLED** = `0`

Used with
`Node.rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"} to disable a method or property for all RPC calls, making it
unavailable. Default for all methods.

:::: {#class_MultiplayerAPI_constant_RPC_MODE_ANY_PEER}
::: rst-class
classref-enumeration-constant
:::
::::

`RPCMode<enum_MultiplayerAPI_RPCMode>`{.interpreted-text role="ref"}
**RPC_MODE_ANY_PEER** = `1`

Used with
`Node.rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"} to set a method to be callable remotely by any peer.
Analogous to the `@rpc("any_peer")` annotation. Calls are accepted from
all remote peers, no matter if they are node\'s authority or not.

:::: {#class_MultiplayerAPI_constant_RPC_MODE_AUTHORITY}
::: rst-class
classref-enumeration-constant
:::
::::

`RPCMode<enum_MultiplayerAPI_RPCMode>`{.interpreted-text role="ref"}
**RPC_MODE_AUTHORITY** = `2`

Used with
`Node.rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"} to set a method to be callable remotely only by the current
multiplayer authority (which is the server by default). Analogous to the
`@rpc("authority")` annotation. See
`Node.set_multiplayer_authority()<class_Node_method_set_multiplayer_authority>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MultiplayerAPI_property_multiplayer_peer}
::: rst-class
classref-property
:::
::::

`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
**multiplayer_peer**
`🔗<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_multiplayer_peer**(value:
  `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text
  role="ref"})
- `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
  **get_multiplayer_peer**()

The peer object to handle the RPC system (effectively enabling
networking when set). Depending on the peer itself, the MultiplayerAPI
will become a network server (check with
`is_server()<class_MultiplayerAPI_method_is_server>`{.interpreted-text
role="ref"}) and will set root node\'s network mode to authority, or it
will become a regular client peer. All child nodes are set to inherit
the network mode by default. Handling of networking-related events
(connection, disconnection, new clients) is done by connecting to
MultiplayerAPI\'s signals.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MultiplayerAPI_method_create_default_interface}
::: rst-class
classref-method
:::
::::

`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
**create_default_interface**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPI_method_create_default_interface>`{.interpreted-text
role="ref"}

Returns a new instance of the default MultiplayerAPI.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_get_default_interface}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_default_interface**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPI_method_get_default_interface>`{.interpreted-text
role="ref"}

Returns the default MultiplayerAPI implementation class name. This is
usually `"SceneMultiplayer"` when
`SceneMultiplayer<class_SceneMultiplayer>`{.interpreted-text role="ref"}
is available. See
`set_default_interface()<class_MultiplayerAPI_method_set_default_interface>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_get_peers}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_peers**()
`🔗<class_MultiplayerAPI_method_get_peers>`{.interpreted-text
role="ref"}

Returns the peer IDs of all connected peers of this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_get_remote_sender_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_remote_sender_id**()
`🔗<class_MultiplayerAPI_method_get_remote_sender_id>`{.interpreted-text
role="ref"}

Returns the sender\'s peer ID for the RPC currently being executed.

\*\*Note:\*\* This method returns `0` when called outside of an RPC. As
such, the original peer ID may be lost when code execution is delayed
(such as with GDScript\'s `await` keyword).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_get_unique_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_unique_id**()
`🔗<class_MultiplayerAPI_method_get_unique_id>`{.interpreted-text
role="ref"}

Returns the unique peer ID of this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_has_multiplayer_peer}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_multiplayer_peer**()
`🔗<class_MultiplayerAPI_method_has_multiplayer_peer>`{.interpreted-text
role="ref"}

Returns `true` if there is a
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_is_server}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_server**()
`🔗<class_MultiplayerAPI_method_is_server>`{.interpreted-text
role="ref"}

Returns `true` if this MultiplayerAPI\'s
`multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} is valid and in server mode (listening for connections).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_object_configuration_add}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**object_configuration_add**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, configuration:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerAPI_method_object_configuration_add>`{.interpreted-text
role="ref"}

Notifies the MultiplayerAPI of a new `configuration` for the given
`object`. This method is used internally by
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} to configure
the root path for this MultiplayerAPI (passing `null` and a valid
`NodePath<class_NodePath>`{.interpreted-text role="ref"} as
`configuration`). This method can be further used by MultiplayerAPI
implementations to provide additional features, refer to specific
implementation (e.g.
`SceneMultiplayer<class_SceneMultiplayer>`{.interpreted-text
role="ref"}) for details on how they use it.

\*\*Note:\*\* This method is mostly relevant when extending or
overriding the MultiplayerAPI behavior via
`MultiplayerAPIExtension<class_MultiplayerAPIExtension>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_object_configuration_remove}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**object_configuration_remove**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, configuration:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerAPI_method_object_configuration_remove>`{.interpreted-text
role="ref"}

Notifies the MultiplayerAPI to remove a `configuration` for the given
`object`. This method is used internally by
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} to configure
the root path for this MultiplayerAPI (passing `null` and an empty
`NodePath<class_NodePath>`{.interpreted-text role="ref"} as
`configuration`). This method can be further used by MultiplayerAPI
implementations to provide additional features, refer to specific
implementation (e.g.
`SceneMultiplayer<class_SceneMultiplayer>`{.interpreted-text
role="ref"}) for details on how they use it.

\*\*Note:\*\* This method is mostly relevant when extending or
overriding the MultiplayerAPI behavior via
`MultiplayerAPIExtension<class_MultiplayerAPIExtension>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**poll**() `🔗<class_MultiplayerAPI_method_poll>`{.interpreted-text
role="ref"}

Method used for polling the MultiplayerAPI. You only need to worry about
this if you set
`SceneTree.multiplayer_poll<class_SceneTree_property_multiplayer_poll>`{.interpreted-text
role="ref"} to `false`. By default,
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} will poll its
MultiplayerAPI(s) for you.

\*\*Note:\*\* This method results in RPCs being called, so they will be
executed in the same context of this function (e.g. `_process`,
`physics`, `Thread<class_Thread>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_rpc}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**rpc**(peer: `int<class_int>`{.interpreted-text role="ref"}, object:
`Object<class_Object>`{.interpreted-text role="ref"}, method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, arguments:
`Array<class_Array>`{.interpreted-text role="ref"} = \[\])
`🔗<class_MultiplayerAPI_method_rpc>`{.interpreted-text role="ref"}

Sends an RPC to the target `peer`. The given `method` will be called on
the remote `object` with the provided `arguments`. The RPC may also be
called locally depending on the implementation and RPC configuration.
See `Node.rpc()<class_Node_method_rpc>`{.interpreted-text role="ref"}
and `Node.rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Prefer using
`Node.rpc()<class_Node_method_rpc>`{.interpreted-text role="ref"},
`Node.rpc_id()<class_Node_method_rpc_id>`{.interpreted-text role="ref"},
or `my_method.rpc(peer, arg1, arg2, ...)` (in GDScript), since they are
faster. This method is mostly useful in conjunction with
`MultiplayerAPIExtension<class_MultiplayerAPIExtension>`{.interpreted-text
role="ref"} when extending or replacing the multiplayer capabilities.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPI_method_set_default_interface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_default_interface**(interface_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPI_method_set_default_interface>`{.interpreted-text
role="ref"}

Sets the default MultiplayerAPI implementation class. This method can be
used by modules and extensions to configure which implementation will be
used by `SceneTree<class_SceneTree>`{.interpreted-text role="ref"} when
the engine starts.
