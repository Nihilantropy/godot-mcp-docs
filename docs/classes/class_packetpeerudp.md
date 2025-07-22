github_url
:   hide

# PacketPeerUDP {#class_PacketPeerUDP}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

UDP packet peer.

::: rst-class
classref-introduction-group
:::

## Description

UDP packet peer. Can be used to send and receive raw UDP packets as well
as `Variant<class_Variant>`{.interpreted-text role="ref"}s.

\*\*Example:\*\* Send a packet:

    var peer = PacketPeerUDP.new()

    # Optionally, you can select the local port used to send the packet.
    peer.bind(4444)

    peer.set_dest_address("1.1.1.1", 4433)
    peer.put_packet("hello".to_utf8_buffer())

\*\*Example:\*\* Listen for packets:

    var peer

    func _ready():
        peer = PacketPeerUDP.new()
        peer.bind(4433)


    func _process(_delta):
        if peer.get_available_packet_count() > 0:
            var array_bytes = peer.get_packet()
            var packet_string = array_bytes.get_string_from_ascii()
            print("Received message: ", packet_string)

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

:::: {#class_PacketPeerUDP_method_bind}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**bind**(port: `int<class_int>`{.interpreted-text role="ref"},
bind_address: `String<class_String>`{.interpreted-text role="ref"} =
\"\*\", recv_buf_size: `int<class_int>`{.interpreted-text role="ref"} =
65536) `🔗<class_PacketPeerUDP_method_bind>`{.interpreted-text
role="ref"}

Binds this **PacketPeerUDP** to the specified `port` and `bind_address`
with a buffer size `recv_buf_size`, allowing it to receive incoming
packets.

If `bind_address` is set to `"*"` (default), the peer will be bound on
all available addresses (both IPv4 and IPv6).

If `bind_address` is set to `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6),
the peer will be bound to all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`,
`"::1"`, etc.), the peer will only be bound to the interface with that
address (or fail if no interface with the given address exists).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**()
`🔗<class_PacketPeerUDP_method_close>`{.interpreted-text role="ref"}

Closes the **PacketPeerUDP**\'s underlying UDP socket.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_connect_to_host}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_to_host**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PacketPeerUDP_method_connect_to_host>`{.interpreted-text
role="ref"}

Calling this method connects this UDP peer to the given `host`/`port`
pair. UDP is in reality connectionless, so this option only means that
incoming packets from different addresses are automatically discarded,
and that outgoing packets are always sent to the connected address
(future calls to
`set_dest_address()<class_PacketPeerUDP_method_set_dest_address>`{.interpreted-text
role="ref"} are not allowed). This method does not send any data to the
remote peer, to do that, use
`PacketPeer.put_var()<class_PacketPeer_method_put_var>`{.interpreted-text
role="ref"} or
`PacketPeer.put_packet()<class_PacketPeer_method_put_packet>`{.interpreted-text
role="ref"} as usual. See also
`UDPServer<class_UDPServer>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Connecting to the remote peer does not help to protect
from malicious attacks like IP spoofing, etc. Think about using an
encryption technique like TLS or DTLS if you feel like your application
is transferring sensitive information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_get_local_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_local_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeerUDP_method_get_local_port>`{.interpreted-text
role="ref"}

Returns the local port to which this peer is bound.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_get_packet_ip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_packet_ip**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeerUDP_method_get_packet_ip>`{.interpreted-text
role="ref"}

Returns the IP of the remote peer that sent the last packet(that was
received with
`PacketPeer.get_packet()<class_PacketPeer_method_get_packet>`{.interpreted-text
role="ref"} or
`PacketPeer.get_var()<class_PacketPeer_method_get_var>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_get_packet_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_packet_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeerUDP_method_get_packet_port>`{.interpreted-text
role="ref"}

Returns the port of the remote peer that sent the last packet(that was
received with
`PacketPeer.get_packet()<class_PacketPeer_method_get_packet>`{.interpreted-text
role="ref"} or
`PacketPeer.get_var()<class_PacketPeer_method_get_var>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_is_bound}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_bound**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PacketPeerUDP_method_is_bound>`{.interpreted-text
role="ref"}

Returns whether this **PacketPeerUDP** is bound to an address and can
receive packets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_is_socket_connected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_socket_connected**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeerUDP_method_is_socket_connected>`{.interpreted-text
role="ref"}

Returns `true` if the UDP socket is open and has been connected to a
remote address. See
`connect_to_host()<class_PacketPeerUDP_method_connect_to_host>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_join_multicast_group}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**join_multicast_group**(multicast_address:
`String<class_String>`{.interpreted-text role="ref"}, interface_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PacketPeerUDP_method_join_multicast_group>`{.interpreted-text
role="ref"}

Joins the multicast group specified by `multicast_address` using the
interface identified by `interface_name`.

You can join the same multicast group with multiple interfaces. Use
`IP.get_local_interfaces()<class_IP_method_get_local_interfaces>`{.interpreted-text
role="ref"} to know which are available.

\*\*Note:\*\* Some Android devices might require the
`CHANGE_WIFI_MULTICAST_STATE` permission for multicast to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_leave_multicast_group}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**leave_multicast_group**(multicast_address:
`String<class_String>`{.interpreted-text role="ref"}, interface_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PacketPeerUDP_method_leave_multicast_group>`{.interpreted-text
role="ref"}

Removes the interface identified by `interface_name` from the multicast
group specified by `multicast_address`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_set_broadcast_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_broadcast_enabled**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_PacketPeerUDP_method_set_broadcast_enabled>`{.interpreted-text
role="ref"}

Enable or disable sending of broadcast packets (e.g.
`set_dest_address("255.255.255.255", 4343)`. This option is disabled by
default.

\*\*Note:\*\* Some Android devices might require the
`CHANGE_WIFI_MULTICAST_STATE` permission and this option to be enabled
to receive broadcast packets too.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_set_dest_address}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_dest_address**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PacketPeerUDP_method_set_dest_address>`{.interpreted-text
role="ref"}

Sets the destination address and port for sending packets and variables.
A hostname will be resolved using DNS if needed.

\*\*Note:\*\*
`set_broadcast_enabled()<class_PacketPeerUDP_method_set_broadcast_enabled>`{.interpreted-text
role="ref"} must be enabled before sending packets to a broadcast
address (e.g. `255.255.255.255`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerUDP_method_wait}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**wait**() `🔗<class_PacketPeerUDP_method_wait>`{.interpreted-text
role="ref"}

Waits for a packet to arrive on the bound address. See
`bind()<class_PacketPeerUDP_method_bind>`{.interpreted-text role="ref"}.

\*\*Note:\*\*
`wait()<class_PacketPeerUDP_method_wait>`{.interpreted-text role="ref"}
can\'t be interrupted once it has been called. This can be worked around
by allowing the other party to send a specific \"death pill\" packet
like this:

::::: tabs
::: code-tab
gdscript

socket = PacketPeerUDP.new() \# Server
socket.set_dest_address(\"127.0.0.1\", 789) socket.put_packet(\"Time to
stop\".to_ascii_buffer())

\# Client while socket.wait() == OK: var data =
socket.get_packet().get_string_from_ascii() if data == \"Time to stop\":
return
:::

::: code-tab
csharp

var socket = new PacketPeerUdp(); // Server
socket.SetDestAddress(\"127.0.0.1\", 789); socket.PutPacket(\"Time to
stop\".ToAsciiBuffer());

// Client while (socket.Wait() == OK) { string data =
socket.GetPacket().GetStringFromASCII(); if (data == \"Time to stop\") {
return; } }
:::
:::::
