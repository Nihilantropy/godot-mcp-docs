github_url
:   hide

# DTLSServer {#class_DTLSServer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Helper class to implement a DTLS server.

::: rst-class
classref-introduction-group
:::

## Description

This class is used to store the state of a DTLS server. Upon
`setup()<class_DTLSServer_method_setup>`{.interpreted-text role="ref"}
it converts connected
`PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text role="ref"} to
`PacketPeerDTLS<class_PacketPeerDTLS>`{.interpreted-text role="ref"}
accepting them via
`take_connection()<class_DTLSServer_method_take_connection>`{.interpreted-text
role="ref"} as DTLS clients. Under the hood, this class is used to store
the DTLS state and cookies of the server. The reason of why the state
and cookies are needed is outside of the scope of this documentation.

Below a small example of how to use it:

::::: tabs
::: code-tab
gdscript

\# server_node.gd extends Node

var dtls = DTLSServer.new() var server = UDPServer.new() var peers =
\[\]

func [ready]{#ready}():

:   server.listen(4242) var key = load(\"key.key\") \# Your private key.
    var cert = load(\"cert.crt\") \# Your X509 certificate.
    dtls.setup(TlsOptions.server(key, cert))

func [process]{#process}(delta):

:   

    while server.is_connection_available():

    :   var peer = server.take_connection() var dtls_peer =
        dtls.take_connection(peer) if dtls_peer.get_status() !=
        PacketPeerDTLS.STATUS_HANDSHAKING: continue \# It is normal that
        50% of the connections fails due to cookie exchange.
        print(\"Peer connected!\") peers.append(dtls_peer)

    for p in peers:

    :   p.poll() \# Must poll to update the state. if p.get_status() ==
        PacketPeerDTLS.STATUS_CONNECTED: while
        p.get_available_packet_count() \> 0: print(\"Received message
        from client: %s\" % p.get_packet().get_string_from_utf8())
        p.put_packet(\"Hello DTLS client\".to_utf8_buffer())
:::

::: code-tab
csharp

// ServerNode.cs using Godot;

public partial class ServerNode : Node { private DtlsServer
[dtls]{#dtls} = new DtlsServer(); private UdpServer [server]{#server} =
new UdpServer(); private Godot.Collections.Array\<PacketPeerDtls\>
[peers]{#peers} = \[\];

> public override void [Ready]{#ready}() {
> [server.Listen]{#server.listen}(4242); var key =
> GD.Load\<CryptoKey\>(\"key.key\"); // Your private key. var cert =
> GD.Load\<X509Certificate\>(\"cert.crt\"); // Your X509 certificate.
> [dtls.Setup]{#dtls.setup}(TlsOptions.Server(key, cert)); }
>
> public override void [Process]{#process}(double delta) { while
> ([server.IsConnectionAvailable]{#server.isconnectionavailable}()) {
> PacketPeerUdp peer =
> [server.TakeConnection]{#server.takeconnection}(); PacketPeerDtls
> dtlsPeer = [dtls.TakeConnection]{#dtls.takeconnection}(peer); if
> (dtlsPeer.GetStatus() != PacketPeerDtls.Status.Handshaking) {
> continue; // It is normal that 50% of the connections fails due to
> cookie exchange. } GD.Print(\"Peer connected!\");
> [peers.Add]{#peers.add}(dtlsPeer); }
>
> > foreach (var p in [peers]{#peers}) { p.Poll(); // Must poll to
> > update the state. if (p.GetStatus() ==
> > PacketPeerDtls.Status.Connected) { while
> > (p.GetAvailablePacketCount() \> 0) { GD.Print(\$\"Received Message
> > From Client: {p.GetPacket().GetStringFromUtf8()}\");
> > p.PutPacket(\"Hello DTLS Client\".ToUtf8Buffer()); } } }
>
> }

}
:::
:::::

::::: tabs
::: code-tab
gdscript

\# client_node.gd extends Node

var dtls = PacketPeerDTLS.new() var udp = PacketPeerUDP.new() var
connected = false

func [ready]{#ready}():

:   udp.connect_to_host(\"127.0.0.1\", 4242) dtls.connect_to_peer(udp,
    false) \# Use true in production for certificate validation!

func [process]{#process}(delta):

:   dtls.poll() if dtls.get_status() == PacketPeerDTLS.STATUS_CONNECTED:
    if !connected: \# Try to contact server dtls.put_packet(\"The answer
    is\... 42!\".to_utf8_buffer()) while
    dtls.get_available_packet_count() \> 0: print(\"Connected: %s\" %
    dtls.get_packet().get_string_from_utf8()) connected = true
:::

::: code-tab
csharp

// ClientNode.cs using Godot; using System.Text;

public partial class ClientNode : Node { private PacketPeerDtls
[dtls]{#dtls} = new PacketPeerDtls(); private PacketPeerUdp [udp]{#udp}
= new PacketPeerUdp(); private bool [connected]{#connected} = false;

> public override void [Ready]{#ready}() {
> [udp.ConnectToHost]{#udp.connecttohost}(\"127.0.0.1\", 4242);
> [dtls.ConnectToPeer]{#dtls.connecttopeer}([udp]{#udp}, validateCerts:
> false); // Use true in production for certificate validation! }
>
> public override void [Process]{#process}(double delta) {
> [dtls.Poll]{#dtls.poll}(); if ([dtls.GetStatus]{#dtls.getstatus}() ==
> PacketPeerDtls.Status.Connected) { if (!\_connected) { // Try to
> contact server [dtls.PutPacket]{#dtls.putpacket}(\"The Answer
> Is..42!\".ToUtf8Buffer()); } while
> ([dtls.GetAvailablePacketCount]{#dtls.getavailablepacketcount}() \> 0)
> { GD.Print(\$\"Connected:
> {[dtls.GetPacket]{#dtls.getpacket}().GetStringFromUtf8()}\");
> [connected]{#connected} = true; } } }

}
:::
:::::

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

:::: {#class_DTLSServer_method_setup}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**setup**(server_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"})
`🔗<class_DTLSServer_method_setup>`{.interpreted-text role="ref"}

Setup the DTLS server to use the given `server_options`. See
`TLSOptions.server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DTLSServer_method_take_connection}
::: rst-class
classref-method
:::
::::

`PacketPeerDTLS<class_PacketPeerDTLS>`{.interpreted-text role="ref"}
**take_connection**(udp_peer:
`PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text role="ref"})
`🔗<class_DTLSServer_method_take_connection>`{.interpreted-text
role="ref"}

Try to initiate the DTLS handshake with the given `udp_peer` which must
be already connected (see
`PacketPeerUDP.connect_to_host()<class_PacketPeerUDP_method_connect_to_host>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* You must check that the state of the return PacketPeerUDP
is
`PacketPeerDTLS.STATUS_HANDSHAKING<class_PacketPeerDTLS_constant_STATUS_HANDSHAKING>`{.interpreted-text
role="ref"}, as it is normal that 50% of the new connections will be
invalid due to cookie exchange.
