github_url
:   hide

# TCPServer {#class_TCPServer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A TCP server.

::: rst-class
classref-introduction-group
:::

## Description

A TCP server. Listens to connections on a port and returns a
`StreamPeerTCP<class_StreamPeerTCP>`{.interpreted-text role="ref"} when
it gets an incoming connection.

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

:::: {#class_TCPServer_method_get_local_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_local_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TCPServer_method_get_local_port>`{.interpreted-text
role="ref"}

Returns the local port this server is listening to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TCPServer_method_is_connection_available}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_connection_available**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TCPServer_method_is_connection_available>`{.interpreted-text
role="ref"}

Returns `true` if a connection is available for taking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TCPServer_method_is_listening}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_listening**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TCPServer_method_is_listening>`{.interpreted-text
role="ref"}

Returns `true` if the server is currently listening for connections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TCPServer_method_listen}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**listen**(port: `int<class_int>`{.interpreted-text role="ref"},
bind_address: `String<class_String>`{.interpreted-text role="ref"} =
\"\*\") `🔗<class_TCPServer_method_listen>`{.interpreted-text
role="ref"}

Listen on the `port` binding to `bind_address`.

If `bind_address` is set as `"*"` (default), the server will listen on
all available addresses (both IPv4 and IPv6).

If `bind_address` is set as `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6),
the server will listen on all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`,
`"::1"`, etc.), the server will only listen on the interface with that
address (or fail if no interface with the given address exists).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TCPServer_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_TCPServer_method_stop>`{.interpreted-text role="ref"}

Stops listening.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TCPServer_method_take_connection}
::: rst-class
classref-method
:::
::::

`StreamPeerTCP<class_StreamPeerTCP>`{.interpreted-text role="ref"}
**take_connection**()
`🔗<class_TCPServer_method_take_connection>`{.interpreted-text
role="ref"}

If a connection is available, returns a StreamPeerTCP with the
connection.
