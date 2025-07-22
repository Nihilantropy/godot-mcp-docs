github_url
:   hide

# ENetConnection {#class_ENetConnection}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A wrapper class for an
[ENetHost](http://enet.bespin.org/group__host.html).

::: rst-class
classref-introduction-group
:::

## Description

ENet\'s purpose is to provide a relatively thin, simple and robust
network communication layer on top of UDP (User Datagram Protocol).

::: rst-class
classref-introduction-group
:::

## Tutorials

- [API documentation on the ENet
  website](http://enet.bespin.org/usergroup0.html)

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

:::: {#enum_ENetConnection_CompressionMode}
::: rst-class
classref-enumeration
:::
::::

enum **CompressionMode**:
`🔗<enum_ENetConnection_CompressionMode>`{.interpreted-text role="ref"}

:::: {#class_ENetConnection_constant_COMPRESS_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_ENetConnection_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESS_NONE** = `0`

No compression. This uses the most bandwidth, but has the upside of
requiring the fewest CPU resources. This option may also be used to make
network debugging using tools like Wireshark easier.

:::: {#class_ENetConnection_constant_COMPRESS_RANGE_CODER}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_ENetConnection_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESS_RANGE_CODER** = `1`

ENet\'s built-in range encoding. Works well on small packets, but is not
the most efficient algorithm on packets larger than 4 KB.

:::: {#class_ENetConnection_constant_COMPRESS_FASTLZ}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_ENetConnection_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESS_FASTLZ** = `2`

[FastLZ](https://fastlz.org/) compression. This option uses less CPU
resources compared to
`COMPRESS_ZLIB<class_ENetConnection_constant_COMPRESS_ZLIB>`{.interpreted-text
role="ref"}, at the expense of using more bandwidth.

:::: {#class_ENetConnection_constant_COMPRESS_ZLIB}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_ENetConnection_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESS_ZLIB** = `3`

[Zlib](https://www.zlib.net/) compression. This option uses less
bandwidth compared to
`COMPRESS_FASTLZ<class_ENetConnection_constant_COMPRESS_FASTLZ>`{.interpreted-text
role="ref"}, at the expense of using more CPU resources.

:::: {#class_ENetConnection_constant_COMPRESS_ZSTD}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressionMode<enum_ENetConnection_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESS_ZSTD** = `4`

[Zstandard](https://facebook.github.io/zstd/) compression. Note that
this algorithm is not very efficient on packets smaller than 4 KB.
Therefore, it\'s recommended to use other compression algorithms in most
cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ENetConnection_EventType}
::: rst-class
classref-enumeration
:::
::::

enum **EventType**:
`🔗<enum_ENetConnection_EventType>`{.interpreted-text role="ref"}

:::: {#class_ENetConnection_constant_EVENT_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`EventType<enum_ENetConnection_EventType>`{.interpreted-text role="ref"}
**EVENT_ERROR** = `-1`

An error occurred during
`service()<class_ENetConnection_method_service>`{.interpreted-text
role="ref"}. You will likely need to
`destroy()<class_ENetConnection_method_destroy>`{.interpreted-text
role="ref"} the host and recreate it.

:::: {#class_ENetConnection_constant_EVENT_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`EventType<enum_ENetConnection_EventType>`{.interpreted-text role="ref"}
**EVENT_NONE** = `0`

No event occurred within the specified time limit.

:::: {#class_ENetConnection_constant_EVENT_CONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`EventType<enum_ENetConnection_EventType>`{.interpreted-text role="ref"}
**EVENT_CONNECT** = `1`

A connection request initiated by enet_host_connect has completed. The
array will contain the peer which successfully connected.

:::: {#class_ENetConnection_constant_EVENT_DISCONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`EventType<enum_ENetConnection_EventType>`{.interpreted-text role="ref"}
**EVENT_DISCONNECT** = `2`

A peer has disconnected. This event is generated on a successful
completion of a disconnect initiated by
`ENetPacketPeer.peer_disconnect()<class_ENetPacketPeer_method_peer_disconnect>`{.interpreted-text
role="ref"}, if a peer has timed out, or if a connection request
initialized by
`connect_to_host()<class_ENetConnection_method_connect_to_host>`{.interpreted-text
role="ref"} has timed out. The array will contain the peer which
disconnected. The data field contains user supplied data describing the
disconnection, or 0, if none is available.

:::: {#class_ENetConnection_constant_EVENT_RECEIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`EventType<enum_ENetConnection_EventType>`{.interpreted-text role="ref"}
**EVENT_RECEIVE** = `3`

A packet has been received from a peer. The array will contain the peer
which sent the packet and the channel number upon which the packet was
received. The received packet will be queued to the associated
`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ENetConnection_HostStatistic}
::: rst-class
classref-enumeration
:::
::::

enum **HostStatistic**:
`🔗<enum_ENetConnection_HostStatistic>`{.interpreted-text role="ref"}

:::: {#class_ENetConnection_constant_HOST_TOTAL_SENT_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`HostStatistic<enum_ENetConnection_HostStatistic>`{.interpreted-text
role="ref"} **HOST_TOTAL_SENT_DATA** = `0`

Total data sent.

:::: {#class_ENetConnection_constant_HOST_TOTAL_SENT_PACKETS}
::: rst-class
classref-enumeration-constant
:::
::::

`HostStatistic<enum_ENetConnection_HostStatistic>`{.interpreted-text
role="ref"} **HOST_TOTAL_SENT_PACKETS** = `1`

Total UDP packets sent.

:::: {#class_ENetConnection_constant_HOST_TOTAL_RECEIVED_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`HostStatistic<enum_ENetConnection_HostStatistic>`{.interpreted-text
role="ref"} **HOST_TOTAL_RECEIVED_DATA** = `2`

Total data received.

:::: {#class_ENetConnection_constant_HOST_TOTAL_RECEIVED_PACKETS}
::: rst-class
classref-enumeration-constant
:::
::::

`HostStatistic<enum_ENetConnection_HostStatistic>`{.interpreted-text
role="ref"} **HOST_TOTAL_RECEIVED_PACKETS** = `3`

Total UDP packets received.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ENetConnection_method_bandwidth_limit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bandwidth_limit**(in_bandwidth: `int<class_int>`{.interpreted-text
role="ref"} = 0, out_bandwidth: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_ENetConnection_method_bandwidth_limit>`{.interpreted-text
role="ref"}

Adjusts the bandwidth limits of a host.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_broadcast}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**broadcast**(channel: `int<class_int>`{.interpreted-text role="ref"},
packet: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ENetConnection_method_broadcast>`{.interpreted-text
role="ref"}

Queues a `packet` to be sent to all peers associated with the host over
the specified `channel`. See
`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"}
`FLAG_*` constants for available packet flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_channel_limit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**channel_limit**(limit: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ENetConnection_method_channel_limit>`{.interpreted-text
role="ref"}

Limits the maximum allowed channels of future incoming connections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_compress}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compress**(mode:
`CompressionMode<enum_ENetConnection_CompressionMode>`{.interpreted-text
role="ref"})
`🔗<class_ENetConnection_method_compress>`{.interpreted-text role="ref"}

Sets the compression method used for network packets. These have
different tradeoffs of compression speed versus bandwidth, you may need
to test which one works best for your use case if you use compression at
all.

\*\*Note:\*\* Most games\' network design involve sending many small
packets frequently (smaller than 4 KB each). If in doubt, it is
recommended to keep the default compression algorithm as it works best
on these small packets.

\*\*Note:\*\* The compression mode must be set to the same value on both
the server and all its clients. Clients will fail to connect if the
compression mode set on the client differs from the one set on the
server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_connect_to_host}
::: rst-class
classref-method
:::
::::

`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"}
**connect_to_host**(address: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"},
channels: `int<class_int>`{.interpreted-text role="ref"} = 0, data:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_ENetConnection_method_connect_to_host>`{.interpreted-text
role="ref"}

Initiates a connection to a foreign `address` using the specified `port`
and allocating the requested `channels`. Optional `data` can be passed
during connection in the form of a 32 bit integer.

\*\*Note:\*\* You must call either
`create_host()<class_ENetConnection_method_create_host>`{.interpreted-text
role="ref"} or
`create_host_bound()<class_ENetConnection_method_create_host_bound>`{.interpreted-text
role="ref"} on both ends before calling this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_create_host}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_host**(max_peers: `int<class_int>`{.interpreted-text
role="ref"} = 32, max_channels: `int<class_int>`{.interpreted-text
role="ref"} = 0, in_bandwidth: `int<class_int>`{.interpreted-text
role="ref"} = 0, out_bandwidth: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_ENetConnection_method_create_host>`{.interpreted-text
role="ref"}

Creates an ENetHost that allows up to `max_peers` connected peers, each
allocating up to `max_channels` channels, optionally limiting bandwidth
to `in_bandwidth` and `out_bandwidth` (if greater than zero).

This method binds a random available dynamic UDP port on the host
machine at the *unspecified* address. Use
`create_host_bound()<class_ENetConnection_method_create_host_bound>`{.interpreted-text
role="ref"} to specify the address and port.

\*\*Note:\*\* It is necessary to create a host in both client and server
in order to establish a connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_create_host_bound}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_host_bound**(bind_address:
`String<class_String>`{.interpreted-text role="ref"}, bind_port:
`int<class_int>`{.interpreted-text role="ref"}, max_peers:
`int<class_int>`{.interpreted-text role="ref"} = 32, max_channels:
`int<class_int>`{.interpreted-text role="ref"} = 0, in_bandwidth:
`int<class_int>`{.interpreted-text role="ref"} = 0, out_bandwidth:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_ENetConnection_method_create_host_bound>`{.interpreted-text
role="ref"}

Creates an ENetHost bound to the given `bind_address` and `bind_port`
that allows up to `max_peers` connected peers, each allocating up to
`max_channels` channels, optionally limiting bandwidth to `in_bandwidth`
and `out_bandwidth` (if greater than zero).

\*\*Note:\*\* It is necessary to create a host in both client and server
in order to establish a connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_destroy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **destroy**()
`🔗<class_ENetConnection_method_destroy>`{.interpreted-text role="ref"}

Destroys the host and all resources associated with it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_dtls_client_setup}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**dtls_client_setup**(hostname: `String<class_String>`{.interpreted-text
role="ref"}, client_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"} = null)
`🔗<class_ENetConnection_method_dtls_client_setup>`{.interpreted-text
role="ref"}

Configure this ENetHost to use the custom Godot extension allowing DTLS
encryption for ENet clients. Call this before
`connect_to_host()<class_ENetConnection_method_connect_to_host>`{.interpreted-text
role="ref"} to have ENet connect using DTLS validating the server
certificate against `hostname`. You can pass the optional
`client_options` parameter to customize the trusted certification
authorities, or disable the common name verification. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"} and
`TLSOptions.client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_dtls_server_setup}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**dtls_server_setup**(server_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"})
`🔗<class_ENetConnection_method_dtls_server_setup>`{.interpreted-text
role="ref"}

Configure this ENetHost to use the custom Godot extension allowing DTLS
encryption for ENet servers. Call this right after
`create_host_bound()<class_ENetConnection_method_create_host_bound>`{.interpreted-text
role="ref"} to have ENet expect peers to connect using DTLS. See
`TLSOptions.server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_flush}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **flush**()
`🔗<class_ENetConnection_method_flush>`{.interpreted-text role="ref"}

Sends any queued packets on the host specified to its designated peers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_get_local_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_local_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetConnection_method_get_local_port>`{.interpreted-text
role="ref"}

Returns the local port to which this peer is bound.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_get_max_channels}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_max_channels**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetConnection_method_get_max_channels>`{.interpreted-text
role="ref"}

Returns the maximum number of channels allowed for connected peers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_get_peers}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text
role="ref"}\] **get_peers**()
`🔗<class_ENetConnection_method_get_peers>`{.interpreted-text
role="ref"}

Returns the list of peers associated with this host.

\*\*Note:\*\* This list might include some peers that are not fully
connected or are still being disconnected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_pop_statistic}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**pop_statistic**(statistic:
`HostStatistic<enum_ENetConnection_HostStatistic>`{.interpreted-text
role="ref"})
`🔗<class_ENetConnection_method_pop_statistic>`{.interpreted-text
role="ref"}

Returns and resets host statistics.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_refuse_new_connections}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**refuse_new_connections**(refuse: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_ENetConnection_method_refuse_new_connections>`{.interpreted-text
role="ref"}

Configures the DTLS server to automatically drop new connections.

\*\*Note:\*\* This method is only relevant after calling
`dtls_server_setup()<class_ENetConnection_method_dtls_server_setup>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_service}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **service**(timeout:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_ENetConnection_method_service>`{.interpreted-text role="ref"}

Waits for events on this connection and shuttles packets between the
host and its peers, with the given `timeout` (in milliseconds). The
returned `Array<class_Array>`{.interpreted-text role="ref"} will have 4
elements. An
`EventType<enum_ENetConnection_EventType>`{.interpreted-text
role="ref"}, the
`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"}
which generated the event, the event associated data (if any), the event
associated channel (if any). If the generated event is
`EVENT_RECEIVE<class_ENetConnection_constant_EVENT_RECEIVE>`{.interpreted-text
role="ref"}, the received packet will be queued to the associated
`ENetPacketPeer<class_ENetPacketPeer>`{.interpreted-text role="ref"}.

Call this function regularly to handle connections, disconnections, and
to receive new packets.

\*\*Note:\*\* This method must be called on both ends involved in the
event (sending and receiving hosts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetConnection_method_socket_send}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**socket_send**(destination_address:
`String<class_String>`{.interpreted-text role="ref"}, destination_port:
`int<class_int>`{.interpreted-text role="ref"}, packet:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ENetConnection_method_socket_send>`{.interpreted-text
role="ref"}

Sends a `packet` toward a destination from the address and port
currently bound by this ENetConnection instance.

This is useful as it serves to establish entries in NAT routing tables
on all devices between this bound instance and the public facing
internet, allowing a prospective client\'s connection packets to be
routed backward through the NAT device(s) between the public internet
and this host.

This requires forward knowledge of a prospective client\'s address and
communication port as seen by the public internet - after any NAT
devices have handled their connection request. This information can be
obtained by a [STUN](https://en.wikipedia.org/wiki/STUN) service, and
must be handed off to your host by an entity that is not the prospective
client. This will never work for a client behind a Symmetric NAT due to
the nature of the Symmetric NAT routing algorithm, as their IP and Port
cannot be known beforehand.
