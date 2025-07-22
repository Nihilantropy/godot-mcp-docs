github_url
:   hide

# StreamPeerTCP {#class_StreamPeerTCP}

**Inherits:** `StreamPeer<class_StreamPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A stream peer that handles TCP connections.

::: rst-class
classref-introduction-group
:::

## Description

A stream peer that handles TCP connections. This object can be used to
connect to TCP servers, or also is returned by a TCP server.

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

## Enumerations

:::: {#enum_StreamPeerTCP_Status}
::: rst-class
classref-enumeration
:::
::::

enum **Status**: `🔗<enum_StreamPeerTCP_Status>`{.interpreted-text
role="ref"}

:::: {#class_StreamPeerTCP_constant_STATUS_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTCP_Status>`{.interpreted-text role="ref"}
**STATUS_NONE** = `0`

The initial status of the **StreamPeerTCP**. This is also the status
after disconnecting.

:::: {#class_StreamPeerTCP_constant_STATUS_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTCP_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTING** = `1`

A status representing a **StreamPeerTCP** that is connecting to a host.

:::: {#class_StreamPeerTCP_constant_STATUS_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTCP_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTED** = `2`

A status representing a **StreamPeerTCP** that is connected to a host.

:::: {#class_StreamPeerTCP_constant_STATUS_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_StreamPeerTCP_Status>`{.interpreted-text role="ref"}
**STATUS_ERROR** = `3`

A status representing a **StreamPeerTCP** in error state.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StreamPeerTCP_method_bind}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**bind**(port: `int<class_int>`{.interpreted-text role="ref"}, host:
`String<class_String>`{.interpreted-text role="ref"} = \"\*\")
`🔗<class_StreamPeerTCP_method_bind>`{.interpreted-text role="ref"}

Opens the TCP socket, and binds it to the specified local address.

This method is generally not needed, and only used to force the
subsequent call to
`connect_to_host()<class_StreamPeerTCP_method_connect_to_host>`{.interpreted-text
role="ref"} to use the specified `host` and `port` as source address.
This can be desired in some NAT punchthrough techniques, or when forcing
the source network interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_connect_to_host}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_to_host**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeerTCP_method_connect_to_host>`{.interpreted-text
role="ref"}

Connects to the specified `host:port` pair. A hostname will be resolved
if valid. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_disconnect_from_host}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_from_host**()
`🔗<class_StreamPeerTCP_method_disconnect_from_host>`{.interpreted-text
role="ref"}

Disconnects from host.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_get_connected_host}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_connected_host**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerTCP_method_get_connected_host>`{.interpreted-text
role="ref"}

Returns the IP of this peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_get_connected_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_connected_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerTCP_method_get_connected_port>`{.interpreted-text
role="ref"}

Returns the port of this peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_get_local_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_local_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerTCP_method_get_local_port>`{.interpreted-text
role="ref"}

Returns the local port to which this peer is bound.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_get_status}
::: rst-class
classref-method
:::
::::

`Status<enum_StreamPeerTCP_Status>`{.interpreted-text role="ref"}
**get_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerTCP_method_get_status>`{.interpreted-text
role="ref"}

Returns the status of the connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**poll**() `🔗<class_StreamPeerTCP_method_poll>`{.interpreted-text
role="ref"}

Poll the socket, updating its state. See
`get_status()<class_StreamPeerTCP_method_get_status>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerTCP_method_set_no_delay}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_no_delay**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_StreamPeerTCP_method_set_no_delay>`{.interpreted-text
role="ref"}

If `enabled` is `true`, packets will be sent immediately. If `enabled`
is `false` (the default), packet transfers will be delayed and combined
using [Nagle\'s
algorithm](https://en.wikipedia.org/wiki/Nagle%27s_algorithm).

\*\*Note:\*\* It\'s recommended to leave this disabled for applications
that send large packets or need to transfer a lot of data, as enabling
this can decrease the total available bandwidth.
