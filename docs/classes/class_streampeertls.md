github_url
:   hide

# StreamPeerTLS {#class_StreamPeerTLS}

**Inherits:** `StreamPeer<class_StreamPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A stream peer that handles TLS connections.

::: rst-class
classref-introduction-group
:::

## Description

A stream peer that handles TLS connections. This object can be used to
connect to a TLS server or accept a single TLS client connection.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `TLS certificates <../tutorials/networking/ssl_certificates>`{.interpreted-text
  role="doc"}

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

:::: {#enum_StreamPeerTLS_Status}
::: rst-class
classref-enumeration
:::
::::

enum **Status**: `🔗<enum_StreamPeerTLS_Status>`{.interpreted-text
role="ref"}

:::: {#class_StreamPeerTLS_constant_STATUS_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTLS_Status>`{.interpreted-text role="ref"}
**STATUS_DISCONNECTED** = `0`

A status representing a **StreamPeerTLS** that is disconnected.

:::: {#class_StreamPeerTLS_constant_STATUS_HANDSHAKING}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTLS_Status>`{.interpreted-text role="ref"}
**STATUS_HANDSHAKING** = `1`

A status representing a **StreamPeerTLS** during handshaking.

:::: {#class_StreamPeerTLS_constant_STATUS_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTLS_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTED** = `2`

A status representing a **StreamPeerTLS** that is connected to a host.

:::: {#class_StreamPeerTLS_constant_STATUS_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTLS_Status>`{.interpreted-text role="ref"}
**STATUS_ERROR** = `3`

A status representing a **StreamPeerTLS** in error state.

:::: {#class_StreamPeerTLS_constant_STATUS_ERROR_HOSTNAME_MISMATCH}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTLS_Status>`{.interpreted-text role="ref"}
**STATUS_ERROR_HOSTNAME_MISMATCH** = `4`

An error status that shows a mismatch in the TLS certificate domain
presented by the host and the domain requested for validation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StreamPeerTLS_method_accept_stream}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**accept_stream**(stream:
`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"},
server_options: `TLSOptions<class_TLSOptions>`{.interpreted-text
role="ref"})
`🔗<class_StreamPeerTLS_method_accept_stream>`{.interpreted-text
role="ref"}

Accepts a peer connection as a server using the given `server_options`.
See
`TLSOptions.server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTLS_method_connect_to_stream}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_to_stream**(stream:
`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"},
common_name: `String<class_String>`{.interpreted-text role="ref"},
client_options: `TLSOptions<class_TLSOptions>`{.interpreted-text
role="ref"} = null)
`🔗<class_StreamPeerTLS_method_connect_to_stream>`{.interpreted-text
role="ref"}

Connects to a peer using an underlying
`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"} `stream`
and verifying the remote certificate is correctly signed for the given
`common_name`. You can pass the optional `client_options` parameter to
customize the trusted certification authorities, or disable the common
name verification. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"} and
`TLSOptions.client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTLS_method_disconnect_from_stream}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_from_stream**()
`🔗<class_StreamPeerTLS_method_disconnect_from_stream>`{.interpreted-text
role="ref"}

Disconnects from host.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTLS_method_get_status}
::: rst-class
classref-method
:::
::::

`Status<enum_StreamPeerTLS_Status>`{.interpreted-text role="ref"}
**get_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerTLS_method_get_status>`{.interpreted-text
role="ref"}

Returns the status of the connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTLS_method_get_stream}
::: rst-class
classref-method
:::
::::

`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"}
**get_stream**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerTLS_method_get_stream>`{.interpreted-text
role="ref"}

Returns the underlying `StreamPeer<class_StreamPeer>`{.interpreted-text
role="ref"} connection, used in
`accept_stream()<class_StreamPeerTLS_method_accept_stream>`{.interpreted-text
role="ref"} or
`connect_to_stream()<class_StreamPeerTLS_method_connect_to_stream>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTLS_method_poll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **poll**()
`🔗<class_StreamPeerTLS_method_poll>`{.interpreted-text role="ref"}

Poll the connection to check for incoming bytes. Call this right before
`StreamPeer.get_available_bytes()<class_StreamPeer_method_get_available_bytes>`{.interpreted-text
role="ref"} for it to work properly.
