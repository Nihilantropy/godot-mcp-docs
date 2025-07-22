github_url
:   hide

::: {.meta keywords="network"}
:::

# MultiplayerPeerExtension {#class_MultiplayerPeerExtension}

**Inherits:** `MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text
role="ref"} **\<** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Class that can be inherited to implement custom multiplayer API
networking layers via GDExtension.

::: rst-class
classref-introduction-group
:::

## Description

This class is designed to be inherited from a GDExtension plugin to
implement custom networking layers for the multiplayer API (such as
WebRTC). All the methods below **must** be implemented to have a working
custom multiplayer implementation. See also
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

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

:::: {#class_MultiplayerPeerExtension_private_method__close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_close**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__close>`{.interpreted-text
role="ref"}

Called when the multiplayer peer should be immediately closed (see
`MultiplayerPeer.close()<class_MultiplayerPeer_method_close>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__disconnect_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_disconnect_peer**(p_peer: `int<class_int>`{.interpreted-text
role="ref"}, p_force: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__disconnect_peer>`{.interpreted-text
role="ref"}

Called when the connected `p_peer` should be forcibly disconnected (see
`MultiplayerPeer.disconnect_peer()<class_MultiplayerPeer_method_disconnect_peer>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_available_packet_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_available_packet_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_available_packet_count>`{.interpreted-text
role="ref"}

Called when the available packet count is internally requested by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_connection_status}
::: rst-class
classref-method
:::
::::

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>`{.interpreted-text
role="ref"} **\_get_connection_status**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_connection_status>`{.interpreted-text
role="ref"}

Called when the connection status is requested on the
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.get_connection_status()<class_MultiplayerPeer_method_get_connection_status>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_max_packet_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_max_packet_size**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_max_packet_size>`{.interpreted-text
role="ref"}

Called when the maximum allowed packet size (in bytes) is requested by
the `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_packet}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_get_packet**(r_buffer: `const uint8_t **`, r_buffer_size:
`int32_t*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_packet>`{.interpreted-text
role="ref"}

Called when a packet needs to be received by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"},
with `r_buffer_size` being the size of the binary `r_buffer` in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_packet_channel}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_packet_channel**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_packet_channel>`{.interpreted-text
role="ref"}

Called to get the channel over which the next available packet was
received. See
`MultiplayerPeer.get_packet_channel()<class_MultiplayerPeer_method_get_packet_channel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_packet_mode}
::: rst-class
classref-method
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **\_get_packet_mode**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_packet_mode>`{.interpreted-text
role="ref"}

Called to get the transfer mode the remote peer used to send the next
available packet. See
`MultiplayerPeer.get_packet_mode()<class_MultiplayerPeer_method_get_packet_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_packet_peer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_packet_peer**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_packet_peer>`{.interpreted-text
role="ref"}

Called when the ID of the
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
who sent the most recent packet is requested (see
`MultiplayerPeer.get_packet_peer()<class_MultiplayerPeer_method_get_packet_peer>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_packet_script}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**\_get_packet_script**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_packet_script>`{.interpreted-text
role="ref"}

Called when a packet needs to be received by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}, if
`_get_packet()<class_MultiplayerPeerExtension_private_method__get_packet>`{.interpreted-text
role="ref"} isn\'t implemented. Use this when extending this class via
GDScript.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_transfer_channel}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_transfer_channel**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_transfer_channel>`{.interpreted-text
role="ref"}

Called when the transfer channel to use is read on this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.transfer_channel<class_MultiplayerPeer_property_transfer_channel>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_transfer_mode}
::: rst-class
classref-method
:::
::::

`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"} **\_get_transfer_mode**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_transfer_mode>`{.interpreted-text
role="ref"}

Called when the transfer mode to use is read on this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.transfer_mode<class_MultiplayerPeer_property_transfer_mode>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__get_unique_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_unique_id**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__get_unique_id>`{.interpreted-text
role="ref"}

Called when the unique ID of this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
is requested (see
`MultiplayerPeer.get_unique_id()<class_MultiplayerPeer_method_get_unique_id>`{.interpreted-text
role="ref"}). The value must be between `1` and `2147483647`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__is_refusing_new_connections}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_refusing_new_connections**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__is_refusing_new_connections>`{.interpreted-text
role="ref"}

Called when the \"refuse new connections\" status is requested on this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.refuse_new_connections<class_MultiplayerPeer_property_refuse_new_connections>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__is_server}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_server**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__is_server>`{.interpreted-text
role="ref"}

Called when the \"is server\" status is requested on the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.
See
`MultiplayerAPI.is_server()<class_MultiplayerAPI_method_is_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__is_server_relay_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_server_relay_supported**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__is_server_relay_supported>`{.interpreted-text
role="ref"}

Called to check if the server can act as a relay in the current
configuration. See
`MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__poll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_poll**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__poll>`{.interpreted-text
role="ref"}

Called when the `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text
role="ref"} is polled. See
`MultiplayerAPI.poll()<class_MultiplayerAPI_method_poll>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__put_packet}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_put_packet**(p_buffer: `const uint8_t*`, p_buffer_size:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__put_packet>`{.interpreted-text
role="ref"}

Called when a packet needs to be sent by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"},
with `p_buffer_size` being the size of the binary `p_buffer` in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__put_packet_script}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_put_packet_script**(p_buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__put_packet_script>`{.interpreted-text
role="ref"}

Called when a packet needs to be sent by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}, if
`_put_packet()<class_MultiplayerPeerExtension_private_method__put_packet>`{.interpreted-text
role="ref"} isn\'t implemented. Use this when extending this class via
GDScript.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__set_refuse_new_connections}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_refuse_new_connections**(p_enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__set_refuse_new_connections>`{.interpreted-text
role="ref"}

Called when the \"refuse new connections\" status is set on this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.refuse_new_connections<class_MultiplayerPeer_property_refuse_new_connections>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__set_target_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_target_peer**(p_peer: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__set_target_peer>`{.interpreted-text
role="ref"}

Called when the target peer to use is set for this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.set_target_peer()<class_MultiplayerPeer_method_set_target_peer>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__set_transfer_channel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_transfer_channel**(p_channel: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__set_transfer_channel>`{.interpreted-text
role="ref"}

Called when the channel to use is set for this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.transfer_channel<class_MultiplayerPeer_property_transfer_channel>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerPeerExtension_private_method__set_transfer_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_transfer_mode**(p_mode:
`TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerPeerExtension_private_method__set_transfer_mode>`{.interpreted-text
role="ref"}

Called when the transfer mode is set on this
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
(see
`MultiplayerPeer.transfer_mode<class_MultiplayerPeer_property_transfer_mode>`{.interpreted-text
role="ref"}).
