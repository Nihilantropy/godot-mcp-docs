github_url
:   hide

# ENetPacketPeer {#class_ENetPacketPeer}

**Inherits:** `PacketPeer<class_PacketPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A wrapper class for an
[ENetPeer](http://enet.bespin.org/group__peer.html).

::: rst-class
classref-introduction-group
:::

## Description

A PacketPeer implementation representing a peer of an
`ENetConnection<class_ENetConnection>`{.interpreted-text role="ref"}.

This class cannot be instantiated directly but can be retrieved during
`ENetConnection.service()<class_ENetConnection_method_service>`{.interpreted-text
role="ref"} or via
`ENetConnection.get_peers()<class_ENetConnection_method_get_peers>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

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

:::: {#enum_ENetPacketPeer_PeerState}
::: rst-class
classref-enumeration
:::
::::

enum **PeerState**:
`🔗<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}

:::: {#class_ENetPacketPeer_constant_STATE_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_DISCONNECTED** = `0`

The peer is disconnected.

:::: {#class_ENetPacketPeer_constant_STATE_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_CONNECTING** = `1`

The peer is currently attempting to connect.

:::: {#class_ENetPacketPeer_constant_STATE_ACKNOWLEDGING_CONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_ACKNOWLEDGING_CONNECT** = `2`

The peer has acknowledged the connection request.

:::: {#class_ENetPacketPeer_constant_STATE_CONNECTION_PENDING}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_CONNECTION_PENDING** = `3`

The peer is currently connecting.

:::: {#class_ENetPacketPeer_constant_STATE_CONNECTION_SUCCEEDED}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_CONNECTION_SUCCEEDED** = `4`

The peer has successfully connected, but is not ready to communicate
with yet
(`STATE_CONNECTED<class_ENetPacketPeer_constant_STATE_CONNECTED>`{.interpreted-text
role="ref"}).

:::: {#class_ENetPacketPeer_constant_STATE_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_CONNECTED** = `5`

The peer is currently connected and ready to communicate with.

:::: {#class_ENetPacketPeer_constant_STATE_DISCONNECT_LATER}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_DISCONNECT_LATER** = `6`

The peer is expected to disconnect after it has no more outgoing packets
to send.

:::: {#class_ENetPacketPeer_constant_STATE_DISCONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_DISCONNECTING** = `7`

The peer is currently disconnecting.

:::: {#class_ENetPacketPeer_constant_STATE_ACKNOWLEDGING_DISCONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_ACKNOWLEDGING_DISCONNECT** = `8`

The peer has acknowledged the disconnection request.

:::: {#class_ENetPacketPeer_constant_STATE_ZOMBIE}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**STATE_ZOMBIE** = `9`

The peer has lost connection, but is not considered truly disconnected
(as the peer didn\'t acknowledge the disconnection request).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ENetPacketPeer_PeerStatistic}
::: rst-class
classref-enumeration
:::
::::

enum **PeerStatistic**:
`🔗<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text role="ref"}

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_LOSS}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_LOSS** = `0`

Mean packet loss of reliable packets as a ratio with respect to the
`PACKET_LOSS_SCALE<class_ENetPacketPeer_constant_PACKET_LOSS_SCALE>`{.interpreted-text
role="ref"}.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_LOSS_VARIANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_LOSS_VARIANCE** = `1`

Packet loss variance.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_LOSS_EPOCH}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_LOSS_EPOCH** = `2`

The time at which packet loss statistics were last updated (in
milliseconds since the connection started). The interval for packet loss
statistics updates is 10 seconds, and at least one packet must have been
sent since the last statistics update.

:::: {#class_ENetPacketPeer_constant_PEER_ROUND_TRIP_TIME}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_ROUND_TRIP_TIME** = `3`

Mean packet round trip time for reliable packets.

:::: {#class_ENetPacketPeer_constant_PEER_ROUND_TRIP_TIME_VARIANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_ROUND_TRIP_TIME_VARIANCE** = `4`

Variance of the mean round trip time.

:::: {#class_ENetPacketPeer_constant_PEER_LAST_ROUND_TRIP_TIME}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_LAST_ROUND_TRIP_TIME** = `5`

Last recorded round trip time for a reliable packet.

:::: {#class_ENetPacketPeer_constant_PEER_LAST_ROUND_TRIP_TIME_VARIANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_LAST_ROUND_TRIP_TIME_VARIANCE** = `6`

Variance of the last trip time recorded.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE** = `7`

The peer\'s current throttle status.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE_LIMIT** = `8`

The maximum number of unreliable packets that should not be dropped.
This value is always greater than or equal to `1`. The initial value is
equal to
`PACKET_THROTTLE_SCALE<class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE>`{.interpreted-text
role="ref"}.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_COUNTER}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE_COUNTER** = `9`

Internal value used to increment the packet throttle counter. The value
is hardcoded to `7` and cannot be changed. You probably want to look at
`PEER_PACKET_THROTTLE_ACCELERATION<class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_ACCELERATION>`{.interpreted-text
role="ref"} instead.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_EPOCH}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE_EPOCH** = `10`

The time at which throttle statistics were last updated (in milliseconds
since the connection started). The interval for throttle statistics
updates is
`PEER_PACKET_THROTTLE_INTERVAL<class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_INTERVAL>`{.interpreted-text
role="ref"}.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_ACCELERATION}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE_ACCELERATION** = `11`

The throttle\'s acceleration factor. Higher values will make ENet adapt
to fluctuating network conditions faster, causing unrelaible packets to
be sent *more* often. The default value is `2`.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_DECELERATION}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE_DECELERATION** = `12`

The throttle\'s deceleration factor. Higher values will make ENet adapt
to fluctuating network conditions faster, causing unrelaible packets to
be sent *less* often. The default value is `2`.

:::: {#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_INTERVAL}
::: rst-class
classref-enumeration-constant
:::
::::

`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"} **PEER_PACKET_THROTTLE_INTERVAL** = `13`

The interval over which the lowest mean round trip time should be
measured for use by the throttle mechanism (in milliseconds). The
default value is `5000`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_ENetPacketPeer_constant_PACKET_LOSS_SCALE}
::: rst-class
classref-constant
:::
::::

**PACKET_LOSS_SCALE** = `65536`
`🔗<class_ENetPacketPeer_constant_PACKET_LOSS_SCALE>`{.interpreted-text
role="ref"}

The reference scale for packet loss. See
`get_statistic()<class_ENetPacketPeer_method_get_statistic>`{.interpreted-text
role="ref"} and
`PEER_PACKET_LOSS<class_ENetPacketPeer_constant_PEER_PACKET_LOSS>`{.interpreted-text
role="ref"}.

:::: {#class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE}
::: rst-class
classref-constant
:::
::::

**PACKET_THROTTLE_SCALE** = `32`
`🔗<class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE>`{.interpreted-text
role="ref"}

The reference value for throttle configuration. The default value is
`32`. See
`throttle_configure()<class_ENetPacketPeer_method_throttle_configure>`{.interpreted-text
role="ref"}.

:::: {#class_ENetPacketPeer_constant_FLAG_RELIABLE}
::: rst-class
classref-constant
:::
::::

**FLAG_RELIABLE** = `1`
`🔗<class_ENetPacketPeer_constant_FLAG_RELIABLE>`{.interpreted-text
role="ref"}

Mark the packet to be sent as reliable.

:::: {#class_ENetPacketPeer_constant_FLAG_UNSEQUENCED}
::: rst-class
classref-constant
:::
::::

**FLAG_UNSEQUENCED** = `2`
`🔗<class_ENetPacketPeer_constant_FLAG_UNSEQUENCED>`{.interpreted-text
role="ref"}

Mark the packet to be sent unsequenced (unreliable).

:::: {#class_ENetPacketPeer_constant_FLAG_UNRELIABLE_FRAGMENT}
::: rst-class
classref-constant
:::
::::

**FLAG_UNRELIABLE_FRAGMENT** = `8`
`🔗<class_ENetPacketPeer_constant_FLAG_UNRELIABLE_FRAGMENT>`{.interpreted-text
role="ref"}

Mark the packet to be sent unreliable even if the packet is too big and
needs fragmentation (increasing the chance of it being dropped).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ENetPacketPeer_method_get_channels}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_channels**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetPacketPeer_method_get_channels>`{.interpreted-text
role="ref"}

Returns the number of channels allocated for communication with peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_get_packet_flags}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_packet_flags**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetPacketPeer_method_get_packet_flags>`{.interpreted-text
role="ref"}

Returns the ENet flags of the next packet in the received queue. See
`FLAG_*` constants for available packet flags. Note that not all flags
are replicated from the sending peer to the receiving peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_get_remote_address}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_remote_address**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetPacketPeer_method_get_remote_address>`{.interpreted-text
role="ref"}

Returns the IP address of this peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_get_remote_port}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_remote_port**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetPacketPeer_method_get_remote_port>`{.interpreted-text
role="ref"}

Returns the remote port of this peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_get_state}
::: rst-class
classref-method
:::
::::

`PeerState<enum_ENetPacketPeer_PeerState>`{.interpreted-text role="ref"}
**get_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetPacketPeer_method_get_state>`{.interpreted-text
role="ref"}

Returns the current peer state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_get_statistic}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_statistic**(statistic:
`PeerStatistic<enum_ENetPacketPeer_PeerStatistic>`{.interpreted-text
role="ref"})
`🔗<class_ENetPacketPeer_method_get_statistic>`{.interpreted-text
role="ref"}

Returns the requested `statistic` for this peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_active**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ENetPacketPeer_method_is_active>`{.interpreted-text
role="ref"}

Returns `true` if the peer is currently active (i.e. the associated
`ENetConnection<class_ENetConnection>`{.interpreted-text role="ref"} is
still valid).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_peer_disconnect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**peer_disconnect**(data: `int<class_int>`{.interpreted-text role="ref"}
= 0) `🔗<class_ENetPacketPeer_method_peer_disconnect>`{.interpreted-text
role="ref"}

Request a disconnection from a peer. An
`ENetConnection.EVENT_DISCONNECT<class_ENetConnection_constant_EVENT_DISCONNECT>`{.interpreted-text
role="ref"} will be generated during
`ENetConnection.service()<class_ENetConnection_method_service>`{.interpreted-text
role="ref"} once the disconnection is complete.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_peer_disconnect_later}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**peer_disconnect_later**(data: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_ENetPacketPeer_method_peer_disconnect_later>`{.interpreted-text
role="ref"}

Request a disconnection from a peer, but only after all queued outgoing
packets are sent. An
`ENetConnection.EVENT_DISCONNECT<class_ENetConnection_constant_EVENT_DISCONNECT>`{.interpreted-text
role="ref"} will be generated during
`ENetConnection.service()<class_ENetConnection_method_service>`{.interpreted-text
role="ref"} once the disconnection is complete.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_peer_disconnect_now}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**peer_disconnect_now**(data: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_ENetPacketPeer_method_peer_disconnect_now>`{.interpreted-text
role="ref"}

Force an immediate disconnection from a peer. No
`ENetConnection.EVENT_DISCONNECT<class_ENetConnection_constant_EVENT_DISCONNECT>`{.interpreted-text
role="ref"} will be generated. The foreign peer is not guaranteed to
receive the disconnect notification, and is reset immediately upon
return from this function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_ping}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **ping**()
`🔗<class_ENetPacketPeer_method_ping>`{.interpreted-text role="ref"}

Sends a ping request to a peer. ENet automatically pings all connected
peers at regular intervals, however, this function may be called to
ensure more frequent ping requests.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_ping_interval}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**ping_interval**(ping_interval: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_ENetPacketPeer_method_ping_interval>`{.interpreted-text
role="ref"}

Sets the `ping_interval` in milliseconds at which pings will be sent to
a peer. Pings are used both to monitor the liveness of the connection
and also to dynamically adjust the throttle during periods of low
traffic so that the throttle has reasonable responsiveness during
traffic spikes. The default ping interval is `500` milliseconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_reset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reset**()
`🔗<class_ENetPacketPeer_method_reset>`{.interpreted-text role="ref"}

Forcefully disconnects a peer. The foreign host represented by the peer
is not notified of the disconnection and will timeout on its connection
to the local host.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_send}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**send**(channel: `int<class_int>`{.interpreted-text role="ref"},
packet: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ENetPacketPeer_method_send>`{.interpreted-text role="ref"}

Queues a `packet` to be sent over the specified `channel`. See `FLAG_*`
constants for available packet flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_set_timeout}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_timeout**(timeout: `int<class_int>`{.interpreted-text role="ref"},
timeout_min: `int<class_int>`{.interpreted-text role="ref"},
timeout_max: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ENetPacketPeer_method_set_timeout>`{.interpreted-text
role="ref"}

Sets the timeout parameters for a peer. The timeout parameters control
how and when a peer will timeout from a failure to acknowledge reliable
traffic. Timeout values are expressed in milliseconds.

The `timeout` is a factor that, multiplied by a value based on the
average round trip time, will determine the timeout limit for a reliable
packet. When that limit is reached, the timeout will be doubled, and the
peer will be disconnected if that limit has reached `timeout_min`. The
`timeout_max` parameter, on the other hand, defines a fixed timeout for
which any packet must be acknowledged or the peer will be dropped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ENetPacketPeer_method_throttle_configure}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**throttle_configure**(interval: `int<class_int>`{.interpreted-text
role="ref"}, acceleration: `int<class_int>`{.interpreted-text
role="ref"}, deceleration: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_ENetPacketPeer_method_throttle_configure>`{.interpreted-text
role="ref"}

Configures throttle parameter for a peer.

Unreliable packets are dropped by ENet in response to the varying
conditions of the Internet connection to the peer. The throttle
represents a probability that an unreliable packet should not be dropped
and thus sent by ENet to the peer. By measuring fluctuations in round
trip times of reliable packets over the specified `interval`, ENet will
either increase the probability by the amount specified in the
`acceleration` parameter, or decrease it by the amount specified in the
`deceleration` parameter (both are ratios to
`PACKET_THROTTLE_SCALE<class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE>`{.interpreted-text
role="ref"}).

When the throttle has a value of
`PACKET_THROTTLE_SCALE<class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE>`{.interpreted-text
role="ref"}, no unreliable packets are dropped by ENet, and so 100% of
all unreliable packets will be sent.

When the throttle has a value of `0`, all unreliable packets are dropped
by ENet, and so 0% of all unreliable packets will be sent.

Intermediate values for the throttle represent intermediate
probabilities between 0% and 100% of unreliable packets being sent. The
bandwidth limits of the local and foreign hosts are taken into account
to determine a sensible limit for the throttle probability above which
it should not raise even in the best of conditions.
