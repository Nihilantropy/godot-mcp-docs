github_url
:   hide

# WebRTCPeerConnection {#class_WebRTCPeerConnection}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`WebRTCPeerConnectionExtension<class_WebRTCPeerConnectionExtension>`{.interpreted-text
role="ref"}

Interface to a WebRTC peer connection.

::: rst-class
classref-introduction-group
:::

## Description

A WebRTC connection between the local computer and a remote peer.
Provides an interface to connect, maintain and monitor the connection.

Setting up a WebRTC connection between two peers may not seem a trivial
task, but it can be broken down into 3 main steps:

- The peer that wants to initiate the connection (`A` from now on)
  creates an offer and send it to the other peer (`B` from now on).
- `B` receives the offer, generate and answer, and sends it to `A`).
- `A` and `B` then generates and exchange ICE candidates with each
  other.

After these steps, the connection should become connected. Keep on
reading or look into the tutorial for more information.

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

## Signals

:::: {#class_WebRTCPeerConnection_signal_data_channel_received}
::: rst-class
classref-signal
:::
::::

**data_channel_received**(channel:
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"})
`🔗<class_WebRTCPeerConnection_signal_data_channel_received>`{.interpreted-text
role="ref"}

Emitted when a new in-band channel is received, i.e. when the channel
was created with `negotiated: false` (default).

The object will be an instance of
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"}. You must keep a reference of it or it will be closed
automatically. See
`create_data_channel()<class_WebRTCPeerConnection_method_create_data_channel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_signal_ice_candidate_created}
::: rst-class
classref-signal
:::
::::

**ice_candidate_created**(media:
`String<class_String>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_WebRTCPeerConnection_signal_ice_candidate_created>`{.interpreted-text
role="ref"}

Emitted when a new ICE candidate has been created. The three parameters
are meant to be passed to the remote peer over the signaling server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_signal_session_description_created}
::: rst-class
classref-signal
:::
::::

**session_description_created**(type:
`String<class_String>`{.interpreted-text role="ref"}, sdp:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_WebRTCPeerConnection_signal_session_description_created>`{.interpreted-text
role="ref"}

Emitted after a successful call to
`create_offer()<class_WebRTCPeerConnection_method_create_offer>`{.interpreted-text
role="ref"} or
`set_remote_description()<class_WebRTCPeerConnection_method_set_remote_description>`{.interpreted-text
role="ref"} (when it generates an answer). The parameters are meant to
be passed to
`set_local_description()<class_WebRTCPeerConnection_method_set_local_description>`{.interpreted-text
role="ref"} on this object, and sent to the remote peer over the
signaling server.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_WebRTCPeerConnection_ConnectionState}
::: rst-class
classref-enumeration
:::
::::

enum **ConnectionState**:
`🔗<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"}

:::: {#class_WebRTCPeerConnection_constant_STATE_NEW}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **STATE_NEW** = `0`

The connection is new, data channels and an offer can be created in this
state.

:::: {#class_WebRTCPeerConnection_constant_STATE_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **STATE_CONNECTING** = `1`

The peer is connecting, ICE is in progress, none of the transports has
failed.

:::: {#class_WebRTCPeerConnection_constant_STATE_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **STATE_CONNECTED** = `2`

The peer is connected, all ICE transports are connected.

:::: {#class_WebRTCPeerConnection_constant_STATE_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **STATE_DISCONNECTED** = `3`

At least one ICE transport is disconnected.

:::: {#class_WebRTCPeerConnection_constant_STATE_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **STATE_FAILED** = `4`

One or more of the ICE transports failed.

:::: {#class_WebRTCPeerConnection_constant_STATE_CLOSED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **STATE_CLOSED** = `5`

The peer connection is closed (after calling
`close()<class_WebRTCPeerConnection_method_close>`{.interpreted-text
role="ref"} for example).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_WebRTCPeerConnection_GatheringState}
::: rst-class
classref-enumeration
:::
::::

enum **GatheringState**:
`🔗<enum_WebRTCPeerConnection_GatheringState>`{.interpreted-text
role="ref"}

:::: {#class_WebRTCPeerConnection_constant_GATHERING_STATE_NEW}
::: rst-class
classref-enumeration-constant
:::
::::

`GatheringState<enum_WebRTCPeerConnection_GatheringState>`{.interpreted-text
role="ref"} **GATHERING_STATE_NEW** = `0`

The peer connection was just created and hasn\'t done any networking
yet.

:::: {#class_WebRTCPeerConnection_constant_GATHERING_STATE_GATHERING}
::: rst-class
classref-enumeration-constant
:::
::::

`GatheringState<enum_WebRTCPeerConnection_GatheringState>`{.interpreted-text
role="ref"} **GATHERING_STATE_GATHERING** = `1`

The ICE agent is in the process of gathering candidates for the
connection.

:::: {#class_WebRTCPeerConnection_constant_GATHERING_STATE_COMPLETE}
::: rst-class
classref-enumeration-constant
:::
::::

`GatheringState<enum_WebRTCPeerConnection_GatheringState>`{.interpreted-text
role="ref"} **GATHERING_STATE_COMPLETE** = `2`

The ICE agent has finished gathering candidates. If something happens
that requires collecting new candidates, such as a new interface being
added or the addition of a new ICE server, the state will revert to
gathering to gather those candidates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_WebRTCPeerConnection_SignalingState}
::: rst-class
classref-enumeration
:::
::::

enum **SignalingState**:
`🔗<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"}

:::: {#class_WebRTCPeerConnection_constant_SIGNALING_STATE_STABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **SIGNALING_STATE_STABLE** = `0`

There is no ongoing exchange of offer and answer underway. This may mean
that the **WebRTCPeerConnection** is new
(`STATE_NEW<class_WebRTCPeerConnection_constant_STATE_NEW>`{.interpreted-text
role="ref"}) or that negotiation is complete and a connection has been
established
(`STATE_CONNECTED<class_WebRTCPeerConnection_constant_STATE_CONNECTED>`{.interpreted-text
role="ref"}).

:::: {#class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_LOCAL_OFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **SIGNALING_STATE_HAVE_LOCAL_OFFER** = `1`

The local peer has called
`set_local_description()<class_WebRTCPeerConnection_method_set_local_description>`{.interpreted-text
role="ref"}, passing in SDP representing an offer (usually created by
calling
`create_offer()<class_WebRTCPeerConnection_method_create_offer>`{.interpreted-text
role="ref"}), and the offer has been applied successfully.

:::: {#class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_REMOTE_OFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **SIGNALING_STATE_HAVE_REMOTE_OFFER** = `2`

The remote peer has created an offer and used the signaling server to
deliver it to the local peer, which has set the offer as the remote
description by calling
`set_remote_description()<class_WebRTCPeerConnection_method_set_remote_description>`{.interpreted-text
role="ref"}.

:::: {#class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_LOCAL_PRANSWER}
::: rst-class
classref-enumeration-constant
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **SIGNALING_STATE_HAVE_LOCAL_PRANSWER** = `3`

The offer sent by the remote peer has been applied and an answer has
been created and applied by calling
`set_local_description()<class_WebRTCPeerConnection_method_set_local_description>`{.interpreted-text
role="ref"}. This provisional answer describes the supported media
formats and so forth, but may not have a complete set of ICE candidates
included. Further candidates will be delivered separately later.

:::: {#class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_REMOTE_PRANSWER}
::: rst-class
classref-enumeration-constant
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **SIGNALING_STATE_HAVE_REMOTE_PRANSWER** = `4`

A provisional answer has been received and successfully applied in
response to an offer previously sent and established by calling
`set_local_description()<class_WebRTCPeerConnection_method_set_local_description>`{.interpreted-text
role="ref"}.

:::: {#class_WebRTCPeerConnection_constant_SIGNALING_STATE_CLOSED}
::: rst-class
classref-enumeration-constant
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **SIGNALING_STATE_CLOSED** = `5`

The **WebRTCPeerConnection** has been closed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_WebRTCPeerConnection_method_add_ice_candidate}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_ice_candidate**(media: `String<class_String>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"},
name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_WebRTCPeerConnection_method_add_ice_candidate>`{.interpreted-text
role="ref"}

Add an ice candidate generated by a remote peer (and received over the
signaling server). See
`ice_candidate_created<class_WebRTCPeerConnection_signal_ice_candidate_created>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**()
`🔗<class_WebRTCPeerConnection_method_close>`{.interpreted-text
role="ref"}

Close the peer connection and all data channels associated with it.

\*\*Note:\*\* You cannot reuse this object for a new connection unless
you call
`initialize()<class_WebRTCPeerConnection_method_initialize>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_create_data_channel}
::: rst-class
classref-method
:::
::::

`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"} **create_data_channel**(label:
`String<class_String>`{.interpreted-text role="ref"}, options:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} = {})
`🔗<class_WebRTCPeerConnection_method_create_data_channel>`{.interpreted-text
role="ref"}

Returns a new
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"} (or `null` on failure) with given `label` and optionally
configured via the `options` dictionary. This method can only be called
when the connection is in state
`STATE_NEW<class_WebRTCPeerConnection_constant_STATE_NEW>`{.interpreted-text
role="ref"}.

There are two ways to create a working data channel: either call
`create_data_channel()<class_WebRTCPeerConnection_method_create_data_channel>`{.interpreted-text
role="ref"} on only one of the peer and listen to
`data_channel_received<class_WebRTCPeerConnection_signal_data_channel_received>`{.interpreted-text
role="ref"} on the other, or call
`create_data_channel()<class_WebRTCPeerConnection_method_create_data_channel>`{.interpreted-text
role="ref"} on both peers, with the same values, and the `"negotiated"`
option set to `true`.

Valid `options` are:

    {
        "negotiated": true, # When set to true (default off), means the channel is negotiated out of band. "id" must be set too. "data_channel_received" will not be called.
        "id": 1, # When "negotiated" is true this value must also be set to the same value on both peer.

        # Only one of maxRetransmits and maxPacketLifeTime can be specified, not both. They make the channel unreliable (but also better at real time).
        "maxRetransmits": 1, # Specify the maximum number of attempt the peer will make to retransmits packets if they are not acknowledged.
        "maxPacketLifeTime": 100, # Specify the maximum amount of time before giving up retransmitions of unacknowledged packets (in milliseconds).
        "ordered": true, # When in unreliable mode (i.e. either "maxRetransmits" or "maxPacketLifetime" is set), "ordered" (true by default) specify if packet ordering is to be enforced.

        "protocol": "my-custom-protocol", # A custom sub-protocol string for this channel.
    }

\*\*Note:\*\* You must keep a reference to channels created this way, or
it will be closed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_create_offer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_offer**()
`🔗<class_WebRTCPeerConnection_method_create_offer>`{.interpreted-text
role="ref"}

Creates a new SDP offer to start a WebRTC connection with a remote peer.
At least one
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"} must have been created before calling this method.

If this functions returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"},
`session_description_created<class_WebRTCPeerConnection_signal_session_description_created>`{.interpreted-text
role="ref"} will be called when the session is ready to be sent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_get_connection_state}
::: rst-class
classref-method
:::
::::

`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>`{.interpreted-text
role="ref"} **get_connection_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCPeerConnection_method_get_connection_state>`{.interpreted-text
role="ref"}

Returns the connection state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_get_gathering_state}
::: rst-class
classref-method
:::
::::

`GatheringState<enum_WebRTCPeerConnection_GatheringState>`{.interpreted-text
role="ref"} **get_gathering_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCPeerConnection_method_get_gathering_state>`{.interpreted-text
role="ref"}

Returns the ICE
`GatheringState<enum_WebRTCPeerConnection_GatheringState>`{.interpreted-text
role="ref"} of the connection. This lets you detect, for example, when
collection of ICE candidates has finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_get_signaling_state}
::: rst-class
classref-method
:::
::::

`SignalingState<enum_WebRTCPeerConnection_SignalingState>`{.interpreted-text
role="ref"} **get_signaling_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCPeerConnection_method_get_signaling_state>`{.interpreted-text
role="ref"}

Returns the signaling state on the local end of the connection while
connecting or reconnecting to another peer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_initialize}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**initialize**(configuration:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} = {})
`🔗<class_WebRTCPeerConnection_method_initialize>`{.interpreted-text
role="ref"}

Re-initialize this peer connection, closing any previously active
connection, and going back to state
`STATE_NEW<class_WebRTCPeerConnection_constant_STATE_NEW>`{.interpreted-text
role="ref"}. A dictionary of `configuration` options can be passed to
configure the peer connection.

Valid `configuration` options are:

    {
        "iceServers": [
            {
                "urls": [ "stun:stun.example.com:3478" ], # One or more STUN servers.
            },
            {
                "urls": [ "turn:turn.example.com:3478" ], # One or more TURN servers.
                "username": "a_username", # Optional username for the TURN server.
                "credential": "a_password", # Optional password for the TURN server.
            }
        ]
    }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**poll**()
`🔗<class_WebRTCPeerConnection_method_poll>`{.interpreted-text
role="ref"}

Call this method frequently (e.g. in
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} or
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}) to properly receive signals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_set_default_extension}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_default_extension**(extension_class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_WebRTCPeerConnection_method_set_default_extension>`{.interpreted-text
role="ref"}

Sets the `extension_class` as the default
`WebRTCPeerConnectionExtension<class_WebRTCPeerConnectionExtension>`{.interpreted-text
role="ref"} returned when creating a new **WebRTCPeerConnection**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_set_local_description}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_local_description**(type: `String<class_String>`{.interpreted-text
role="ref"}, sdp: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_WebRTCPeerConnection_method_set_local_description>`{.interpreted-text
role="ref"}

Sets the SDP description of the local peer. This should be called in
response to
`session_description_created<class_WebRTCPeerConnection_signal_session_description_created>`{.interpreted-text
role="ref"}.

After calling this function the peer will start emitting
`ice_candidate_created<class_WebRTCPeerConnection_signal_ice_candidate_created>`{.interpreted-text
role="ref"} (unless an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} different
from `@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} is returned).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebRTCPeerConnection_method_set_remote_description}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_remote_description**(type:
`String<class_String>`{.interpreted-text role="ref"}, sdp:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_WebRTCPeerConnection_method_set_remote_description>`{.interpreted-text
role="ref"}

Sets the SDP description of the remote peer. This should be called with
the values generated by a remote peer and received over the signaling
server.

If `type` is `"offer"` the peer will emit
`session_description_created<class_WebRTCPeerConnection_signal_session_description_created>`{.interpreted-text
role="ref"} with the appropriate answer.

If `type` is `"answer"` the peer will start emitting
`ice_candidate_created<class_WebRTCPeerConnection_signal_ice_candidate_created>`{.interpreted-text
role="ref"}.
