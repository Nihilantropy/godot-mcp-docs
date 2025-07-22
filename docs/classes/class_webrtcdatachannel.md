github_url
:   hide

# WebRTCDataChannel {#class_WebRTCDataChannel}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`WebRTCDataChannelExtension<class_WebRTCDataChannelExtension>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this class. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

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

## Enumerations

:::: {#enum_WebRTCDataChannel_WriteMode}
::: rst-class
classref-enumeration
:::
::::

enum **WriteMode**:
`🔗<enum_WebRTCDataChannel_WriteMode>`{.interpreted-text role="ref"}

:::: {#class_WebRTCDataChannel_constant_WRITE_MODE_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`WriteMode<enum_WebRTCDataChannel_WriteMode>`{.interpreted-text
role="ref"} **WRITE_MODE_TEXT** = `0`

Tells the channel to send data over this channel as text. An external
peer (non-Godot) would receive this as a string.

:::: {#class_WebRTCDataChannel_constant_WRITE_MODE_BINARY}
::: rst-class
classref-enumeration-constant
:::
::::

`WriteMode<enum_WebRTCDataChannel_WriteMode>`{.interpreted-text
role="ref"} **WRITE_MODE_BINARY** = `1`

Tells the channel to send data over this channel as binary. An external
peer (non-Godot) would receive this as array buffer or blob.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_WebRTCDataChannel_ChannelState}
::: rst-class
classref-enumeration
:::
::::

enum **ChannelState**:
`🔗<enum_WebRTCDataChannel_ChannelState>`{.interpreted-text role="ref"}

:::: {#class_WebRTCDataChannel_constant_STATE_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`ChannelState<enum_WebRTCDataChannel_ChannelState>`{.interpreted-text
role="ref"} **STATE_CONNECTING** = `0`

The channel was created, but it\'s still trying to connect.

:::: {#class_WebRTCDataChannel_constant_STATE_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`ChannelState<enum_WebRTCDataChannel_ChannelState>`{.interpreted-text
role="ref"} **STATE_OPEN** = `1`

The channel is currently open, and data can flow over it.

:::: {#class_WebRTCDataChannel_constant_STATE_CLOSING}
::: rst-class
classref-enumeration-constant
:::
::::

`ChannelState<enum_WebRTCDataChannel_ChannelState>`{.interpreted-text
role="ref"} **STATE_CLOSING** = `2`

The channel is being closed, no new messages will be accepted, but those
already in queue will be flushed.

:::: {#class_WebRTCDataChannel_constant_STATE_CLOSED}
::: rst-class
classref-enumeration-constant
:::
::::

`ChannelState<enum_WebRTCDataChannel_ChannelState>`{.interpreted-text
role="ref"} **STATE_CLOSED** = `3`

The channel was closed, or connection failed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_WebRTCDataChannel_property_write_mode}
::: rst-class
classref-property
:::
::::

`WriteMode<enum_WebRTCDataChannel_WriteMode>`{.interpreted-text
role="ref"} **write_mode** = `1`
`🔗<class_WebRTCDataChannel_property_write_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_write_mode**(value:
  `WriteMode<enum_WebRTCDataChannel_WriteMode>`{.interpreted-text
  role="ref"})
- `WriteMode<enum_WebRTCDataChannel_WriteMode>`{.interpreted-text
  role="ref"} **get_write_mode**()

The transfer mode to use when sending outgoing packet. Either text or
binary.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_WebRTCDataChannel_method_close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**()
`🔗<class_WebRTCDataChannel_method_close>`{.interpreted-text role="ref"}

Closes this data channel, notifying the other peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_buffered_amount}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_buffered_amount**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_buffered_amount>`{.interpreted-text
role="ref"}

Returns the number of bytes currently queued to be sent over this
channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_id>`{.interpreted-text
role="ref"}

Returns the ID assigned to this channel during creation (or
auto-assigned during negotiation).

If the channel is not negotiated out-of-band the ID will only be
available after the connection is established (will return `65535` until
then).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_label}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_label**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_label>`{.interpreted-text
role="ref"}

Returns the label assigned to this channel during creation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_max_packet_life_time}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_max_packet_life_time**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_max_packet_life_time>`{.interpreted-text
role="ref"}

Returns the `maxPacketLifeTime` value assigned to this channel during
creation.

Will be `65535` if not specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_max_retransmits}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_max_retransmits**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_max_retransmits>`{.interpreted-text
role="ref"}

Returns the `maxRetransmits` value assigned to this channel during
creation.

Will be `65535` if not specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_protocol}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_protocol**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_protocol>`{.interpreted-text
role="ref"}

Returns the sub-protocol assigned to this channel during creation. An
empty string if not specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_get_ready_state}
::: rst-class
classref-method
:::
::::

`ChannelState<enum_WebRTCDataChannel_ChannelState>`{.interpreted-text
role="ref"} **get_ready_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_get_ready_state>`{.interpreted-text
role="ref"}

Returns the current state of this channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_is_negotiated}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_negotiated**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_is_negotiated>`{.interpreted-text
role="ref"}

Returns `true` if this channel was created with out-of-band
configuration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_is_ordered}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_ordered**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_is_ordered>`{.interpreted-text
role="ref"}

Returns `true` if this channel was created with ordering enabled
(default).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**poll**() `🔗<class_WebRTCDataChannel_method_poll>`{.interpreted-text
role="ref"}

Reserved, but not used for now.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCDataChannel_method_was_string_packet}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **was_string_packet**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCDataChannel_method_was_string_packet>`{.interpreted-text
role="ref"}

Returns `true` if the last received packet was transferred as text. See
`write_mode<class_WebRTCDataChannel_property_write_mode>`{.interpreted-text
role="ref"}.
