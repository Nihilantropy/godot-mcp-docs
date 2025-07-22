github_url
:   hide

# UDPServer {#class_UDPServer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Helper class to implement a UDP server.

::: rst-class
classref-introduction-group
:::

## Description

A simple server that opens a UDP socket and returns connected
`PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text role="ref"} upon
receiving new packets. See also
`PacketPeerUDP.connect_to_host()<class_PacketPeerUDP_method_connect_to_host>`{.interpreted-text
role="ref"}.

After starting the server
(`listen()<class_UDPServer_method_listen>`{.interpreted-text
role="ref"}), you will need to
`poll()<class_UDPServer_method_poll>`{.interpreted-text role="ref"} it
at regular intervals (e.g. inside
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}) for it to process new packets, delivering them to the
appropriate `PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text
role="ref"}, and taking new connections.

Below a small example of how it can be used:

::::: tabs
::: code-tab
gdscript

\# server_node.gd class_name ServerNode extends Node

var server = UDPServer.new() var peers = \[\]

func [ready]{#ready}():

:   server.listen(4242)

func [process]{#process}(delta):

:   server.poll() \# Important! if server.is_connection_available(): var
    peer = server.take_connection() var packet = peer.get_packet()
    print(\"Accepted peer: %s:%s\" % \[peer.get_packet_ip(),
    peer.get_packet_port()\]) print(\"Received data: %s\" %
    \[packet.get_string_from_utf8()\]) \# Reply so it knows we received
    the message. peer.put_packet(packet) \# Keep a reference so we can
    keep contacting the remote peer. peers.append(peer)

    for i in range(0, peers.size()):

    :   pass \# Do something with the connected peers.
:::

::: code-tab
csharp

// ServerNode.cs using Godot; using System.Collections.Generic;

public partial class ServerNode : Node { private UdpServer
[server]{#server} = new UdpServer(); private List\<PacketPeerUdp\>
[peers]{#peers} = new List\<PacketPeerUdp\>();

> public override void [Ready]{#ready}() {
> [server.Listen]{#server.listen}(4242); }
>
> public override void [Process]{#process}(double delta) {
> [server.Poll]{#server.poll}(); // Important! if
> ([server.IsConnectionAvailable]{#server.isconnectionavailable}()) {
> PacketPeerUdp peer =
> [server.TakeConnection]{#server.takeconnection}(); byte\[\] packet =
> peer.GetPacket(); GD.Print(\$\"Accepted Peer:
> {peer.GetPacketIP()}:{peer.GetPacketPort()}\"); GD.Print(\$\"Received
> Data: {packet.GetStringFromUtf8()}\"); // Reply so it knows we
> received the message. peer.PutPacket(packet); // Keep a reference so
> we can keep contacting the remote peer. [peers.Add]{#peers.add}(peer);
> } foreach (var peer in [peers]{#peers}) { // Do something with the
> peers. } }

}
:::
:::::

::::: tabs
::: code-tab
gdscript

\# client_node.gd class_name ClientNode extends Node

var udp = PacketPeerUDP.new() var connected = false

func [ready]{#ready}():

:   udp.connect_to_host(\"127.0.0.1\", 4242)

func [process]{#process}(delta):

:   

    if !connected:

    :   \# Try to contact server udp.put_packet(\"The answer is\...
        42!\".to_utf8_buffer())

    if udp.get_available_packet_count() \> 0:

    :   print(\"Connected: %s\" %
        udp.get_packet().get_string_from_utf8()) connected = true
:::

::: code-tab
csharp

// ClientNode.cs using Godot;

public partial class ClientNode : Node { private PacketPeerUdp
[udp]{#udp} = new PacketPeerUdp(); private bool [connected]{#connected}
= false;

> public override void [Ready]{#ready}() {
> [udp.ConnectToHost]{#udp.connecttohost}(\"127.0.0.1\", 4242); }
>
> public override void [Process]{#process}(double delta) { if
> (!\_connected) { // Try to contact server
> [udp.PutPacket]{#udp.putpacket}(\"The Answer
> Is..42!\".ToUtf8Buffer()); } if
> ([udp.GetAvailablePacketCount]{#udp.getavailablepacketcount}() \> 0) {
> GD.Print(\$\"Connected:
> {[udp.GetPacket]{#udp.getpacket}().GetStringFromUtf8()}\");
> [connected]{#connected} = true; } }

}
:::
:::::

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

:::: {#class_UDPServer_property_max_pending_connections}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**max_pending_connections** = `16`
`🔗<class_UDPServer_property_max_pending_connections>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_pending_connections**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_pending_connections**()

Define the maximum number of pending connections, during
`poll()<class_UDPServer_method_poll>`{.interpreted-text role="ref"}, any
new pending connection exceeding that value will be automatically
dropped. Setting this value to `0` effectively prevents any new pending
connection to be accepted (e.g. when all your players have connected).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_UDPServer_method_get_local_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_local_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UDPServer_method_get_local_port>`{.interpreted-text
role="ref"}

Returns the local port this server is listening to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UDPServer_method_is_connection_available}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_connection_available**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UDPServer_method_is_connection_available>`{.interpreted-text
role="ref"}

Returns `true` if a packet with a new address/port combination was
received on the socket.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UDPServer_method_is_listening}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_listening**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_UDPServer_method_is_listening>`{.interpreted-text
role="ref"}

Returns `true` if the socket is open and listening on a port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UDPServer_method_listen}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**listen**(port: `int<class_int>`{.interpreted-text role="ref"},
bind_address: `String<class_String>`{.interpreted-text role="ref"} =
\"\*\") `🔗<class_UDPServer_method_listen>`{.interpreted-text
role="ref"}

Starts the server by opening a UDP socket listening on the given `port`.
You can optionally specify a `bind_address` to only listen for packets
sent to that address. See also
`PacketPeerUDP.bind()<class_PacketPeerUDP_method_bind>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UDPServer_method_poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**poll**() `🔗<class_UDPServer_method_poll>`{.interpreted-text
role="ref"}

Call this method at regular intervals (e.g. inside
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}) to process new packets. Any packet from a known
address/port pair will be delivered to the appropriate
`PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text role="ref"},
while any packet received from an unknown address/port pair will be
added as a pending connection (see
`is_connection_available()<class_UDPServer_method_is_connection_available>`{.interpreted-text
role="ref"} and
`take_connection()<class_UDPServer_method_take_connection>`{.interpreted-text
role="ref"}). The maximum number of pending connections is defined via
`max_pending_connections<class_UDPServer_property_max_pending_connections>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UDPServer_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_UDPServer_method_stop>`{.interpreted-text role="ref"}

Stops the server, closing the UDP socket if open. Will close all
connected `PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text
role="ref"} accepted via
`take_connection()<class_UDPServer_method_take_connection>`{.interpreted-text
role="ref"} (remote peers will not be notified).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UDPServer_method_take_connection}
::: rst-class
classref-method
:::
::::

`PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text role="ref"}
**take_connection**()
`🔗<class_UDPServer_method_take_connection>`{.interpreted-text
role="ref"}

Returns the first pending connection (connected to the appropriate
address/port). Will return `null` if no new connection is available. See
also
`is_connection_available()<class_UDPServer_method_is_connection_available>`{.interpreted-text
role="ref"},
`PacketPeerUDP.connect_to_host()<class_PacketPeerUDP_method_connect_to_host>`{.interpreted-text
role="ref"}.
