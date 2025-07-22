github_url
:   hide

# ENetMultiplayerPeer {#class_ENetMultiplayerPeer}

**Inherits:** `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text
role="ref"} **\<** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A MultiplayerPeer implementation using the
[ENet](http://enet.bespin.org/index.html) library.

::: rst-class
classref-introduction-group
:::

## Description

A MultiplayerPeer implementation that should be passed to
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} after being initialized as either a client, server, or mesh.
Events can then be handled by connecting to
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
signals. See `ENetConnection<class_ENetConnection>`{.interpreted-text
role="ref"} for more information on the ENet library wrapper.

\*\*Note:\*\* ENet only uses UDP, not TCP. When forwarding the server
port to make your server accessible on the public Internet, you only
need to forward the server port in UDP. You can use the
`UPNP<class_UPNP>`{.interpreted-text role="ref"} class to try to forward
the server port automatically when starting the server.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `High-level multiplayer <../tutorials/networking/high_level_multiplayer>`{.interpreted-text
  role="doc"}
- [API documentation on the ENet
  website](http://enet.bespin.org/usergroup0.html)

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

:::: {#class_ENetMultiplayerPeer_property_host}
::: rst-class
classref-property
:::
::::

`ENetConnection<class_ENetConnection>`{.interpreted-text role="ref"}
**host** `🔗<class_ENetMultiplayerPeer_property_host>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `ENetConnection<class_ENetConnection>`{.interpreted-text role="ref"}
  **get_host**()

The underlying `ENetConnection<class_ENetConnection>`{.interpreted-text
role="ref"} created after
`create_client()<class_ENetMultiplayerPeer_method_create_client>`{.interpreted-text
role="ref"} and
`create_server()<class_ENetMultiplayerPeer_method_create_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ENetMultiplayerPeer_method_add_mesh_peer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_mesh_peer**(peer_id: `int<class_int>`{.interpreted-text
role="ref"}, host:
`ENetConnection<class_ENetConnection>`{.interpreted-text role="ref"})
`🔗<class_ENetMultiplayerPeer_method_add_mesh_peer>`{.interpreted-text
role="ref"}

Add a new remote peer with the given `peer_id` connected to the given
`host`.

\*\*Note:\*\* The `host` must have exactly one peer in the
`ENetPacketPeer.STATE_CONNECTED<class_ENetPacketPeer_constant_STATE_CONNECTED>`{.interpreted-text
role="ref"} state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetMultiplayerPeer_method_create_client}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_client**(address: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"},
channel_count: `int<class_int>`{.interpreted-text role="ref"} = 0,
in_bandwidth: `int<class_int>`{.interpreted-text role="ref"} = 0,
out_bandwidth: `int<class_int>`{.interpreted-text role="ref"} = 0,
local_port: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_ENetMultiplayerPeer_method_create_client>`{.interpreted-text
role="ref"}

Create client that connects to a server at `address` using specified
`port`. The given address needs to be either a fully qualified domain
name (e.g. `"www.example.com"`) or an IP address in IPv4 or IPv6 format
(e.g. `"192.168.1.1"`). The `port` is the port the server is listening
on. The `channel_count` parameter can be used to specify the number of
ENet channels allocated for the connection. The `in_bandwidth` and
`out_bandwidth` parameters can be used to limit the incoming and
outgoing bandwidth to the given number of bytes per second. The default
of 0 means unlimited bandwidth. Note that ENet will strategically drop
packets on specific sides of a connection between peers to ensure the
peer\'s bandwidth is not overwhelmed. The bandwidth parameters also
determine the window size of a connection which limits the amount of
reliable packets that may be in transit at any given time. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if a client was created,
`@GlobalScope.ERR_ALREADY_IN_USE<class_@GlobalScope_constant_ERR_ALREADY_IN_USE>`{.interpreted-text
role="ref"} if this ENetMultiplayerPeer instance already has an open
connection (in which case you need to call
`MultiplayerPeer.close()<class_MultiplayerPeer_method_close>`{.interpreted-text
role="ref"} first) or
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"} if the client could not be created. If `local_port` is
specified, the client will also listen to the given port; this is useful
for some NAT traversal techniques.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetMultiplayerPeer_method_create_mesh}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_mesh**(unique_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_ENetMultiplayerPeer_method_create_mesh>`{.interpreted-text
role="ref"}

Initialize this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
in mesh mode. The provided `unique_id` will be used as the local peer
network unique ID once assigned as the
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"}. In the mesh configuration you will need to set up each new
peer manually using
`ENetConnection<class_ENetConnection>`{.interpreted-text role="ref"}
before calling
`add_mesh_peer()<class_ENetMultiplayerPeer_method_add_mesh_peer>`{.interpreted-text
role="ref"}. While this technique is more advanced, it allows for better
control over the connection process (e.g. when dealing with NAT
punch-through) and for better distribution of the network load (which
would otherwise be more taxing on the server).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetMultiplayerPeer_method_create_server}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_server**(port: `int<class_int>`{.interpreted-text role="ref"},
max_clients: `int<class_int>`{.interpreted-text role="ref"} = 32,
max_channels: `int<class_int>`{.interpreted-text role="ref"} = 0,
in_bandwidth: `int<class_int>`{.interpreted-text role="ref"} = 0,
out_bandwidth: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_ENetMultiplayerPeer_method_create_server>`{.interpreted-text
role="ref"}

Create server that listens to connections via `port`. The port needs to
be an available, unused port between 0 and 65535. Note that ports below
1024 are privileged and may require elevated permissions depending on
the platform. To change the interface the server listens on, use
`set_bind_ip()<class_ENetMultiplayerPeer_method_set_bind_ip>`{.interpreted-text
role="ref"}. The default IP is the wildcard `"*"`, which listens on all
available interfaces. `max_clients` is the maximum number of clients
that are allowed at once, any number up to 4095 may be used, although
the achievable number of simultaneous clients may be far lower and
depends on the application. For additional details on the bandwidth
parameters, see
`create_client()<class_ENetMultiplayerPeer_method_create_client>`{.interpreted-text
role="ref"}. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if a server was created,
`@GlobalScope.ERR_ALREADY_IN_USE<class_@GlobalScope_constant_ERR_ALREADY_IN_USE>`{.interpreted-text
role="ref"} if this ENetMultiplayerPeer instance already has an open
connection (in which case you need to call
`MultiplayerPeer.close()<class_MultiplayerPeer_method_close>`{.interpreted-text
role="ref"} first) or
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"} if the server could not be created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetMultiplayerPeer_method_get_peer}
::: rst-class
classref-method
:::
::::

`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"}
**get_peer**(id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetMultiplayerPeer_method_get_peer>`{.interpreted-text
role="ref"}

Returns the `ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text
role="ref"} associated to the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetMultiplayerPeer_method_set_bind_ip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bind_ip**(ip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ENetMultiplayerPeer_method_set_bind_ip>`{.interpreted-text
role="ref"}

The IP used when creating a server. This is set to the wildcard `"*"` by
default, which binds to all available interfaces. The given IP needs to
be in IPv4 or IPv6 address format, for example: `"192.168.1.1"`.
