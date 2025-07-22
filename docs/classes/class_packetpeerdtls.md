github_url
:   hide

# PacketPeerDTLS {#class_PacketPeerDTLS}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

DTLS packet peer.

::: rst-class
classref-introduction-group
:::

## Description

This class represents a DTLS peer connection. It can be used to connect
to a DTLS server, and is returned by
`DTLSServer.take_connection()<class_DTLSServer_method_take_connection>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

\*\*Warning:\*\* TLS certificate revocation and certificate pinning are
currently not supported. Revoked certificates are accepted as long as
they are otherwise valid. If this is a concern, you may want to use
automatically managed certificates with a short validity period.

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

:::: {#enum_PacketPeerDTLS_Status}
::: rst-class
classref-enumeration
:::
::::

enum **Status**: `🔗<enum_PacketPeerDTLS_Status>`{.interpreted-text
role="ref"}

:::: {#class_PacketPeerDTLS_constant_STATUS_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_PacketPeerDTLS_Status>`{.interpreted-text role="ref"}
**STATUS_DISCONNECTED** = `0`

A status representing a **PacketPeerDTLS** that is disconnected.

:::: {#class_PacketPeerDTLS_constant_STATUS_HANDSHAKING}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_PacketPeerDTLS_Status>`{.interpreted-text role="ref"}
**STATUS_HANDSHAKING** = `1`

A status representing a **PacketPeerDTLS** that is currently performing
the handshake with a remote peer.

:::: {#class_PacketPeerDTLS_constant_STATUS_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_PacketPeerDTLS_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTED** = `2`

A status representing a **PacketPeerDTLS** that is connected to a remote
peer.

:::: {#class_PacketPeerDTLS_constant_STATUS_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_PacketPeerDTLS_Status>`{.interpreted-text role="ref"}
**STATUS_ERROR** = `3`

A status representing a **PacketPeerDTLS** in a generic error state.

:::: {#class_PacketPeerDTLS_constant_STATUS_ERROR_HOSTNAME_MISMATCH}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_PacketPeerDTLS_Status>`{.interpreted-text role="ref"}
**STATUS_ERROR_HOSTNAME_MISMATCH** = `4`

An error status that shows a mismatch in the DTLS certificate domain
presented by the host and the domain requested for validation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PacketPeerDTLS_method_connect_to_peer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_to_peer**(packet_peer:
`PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text role="ref"},
hostname: `String<class_String>`{.interpreted-text role="ref"},
client_options: `TLSOptions<class_TLSOptions>`{.interpreted-text
role="ref"} = null)
`🔗<class_PacketPeerDTLS_method_connect_to_peer>`{.interpreted-text
role="ref"}

Connects a `packet_peer` beginning the DTLS handshake using the
underlying `PacketPeerUDP<class_PacketPeerUDP>`{.interpreted-text
role="ref"} which must be connected (see
`PacketPeerUDP.connect_to_host()<class_PacketPeerUDP_method_connect_to_host>`{.interpreted-text
role="ref"}). You can optionally specify the `client_options` to be used
while verifying the TLS connections. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"} and
`TLSOptions.client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerDTLS_method_disconnect_from_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_from_peer**()
`🔗<class_PacketPeerDTLS_method_disconnect_from_peer>`{.interpreted-text
role="ref"}

Disconnects this peer, terminating the DTLS session.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerDTLS_method_get_status}
::: rst-class
classref-method
:::
::::

`Status<enum_PacketPeerDTLS_Status>`{.interpreted-text role="ref"}
**get_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PacketPeerDTLS_method_get_status>`{.interpreted-text
role="ref"}

Returns the status of the connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PacketPeerDTLS_method_poll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **poll**()
`🔗<class_PacketPeerDTLS_method_poll>`{.interpreted-text role="ref"}

Poll the connection to check for incoming packets. Call this frequently
to update the status and keep the connection working.
