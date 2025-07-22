github_url
:   hide

::: {.meta keywords="network"}
:::

# MultiplayerAPIExtension {#class_MultiplayerAPIExtension}

**Inherits:** `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class used for extending the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This class can be used to extend or replace the default
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
implementation via script or extensions.

The following example extend the default implementation
(`SceneMultiplayer<class_SceneMultiplayer>`{.interpreted-text
role="ref"}) by logging every RPC being made, and every object being
configured for replication.

:::: tabs
::: code-tab
gdscript

extends MultiplayerAPIExtension class_name LogMultiplayer

\# We want to extend the default SceneMultiplayer. var base_multiplayer
= SceneMultiplayer.new()

func [init]{#init}():

:   \# Just passthrough base signals (copied to var to avoid cyclic
    reference) var cts = connected_to_server var cf = connection_failed
    var sd = server_disconnected var pc = peer_connected var pd =
    peer_disconnected
    base_multiplayer.connected_to_server.connect(func(): cts.emit())
    base_multiplayer.connection_failed.connect(func(): cf.emit())
    base_multiplayer.server_disconnected.connect(func(): sd.emit())
    base_multiplayer.peer_connected.connect(func(id): pc.emit(id))
    base_multiplayer.peer_disconnected.connect(func(id): pd.emit(id))

func [poll]{#poll}():

:   return base_multiplayer.poll()

\# Log RPC being made and forward it to the default multiplayer. func
[rpc]{#rpc}(peer: int, object: Object, method: StringName, args: Array)
-\> Error: print(\"Got RPC for %d: %s::%s(%s)\" % \[peer, object,
method, args\]) return base_multiplayer.rpc(peer, object, method, args)

\# Log configuration add. E.g. root path (nullptr, NodePath),
replication (Node, Spawner\|Synchronizer), custom. func
[object_configuration_add]{#object_configuration_add}(object, config:
Variant) -\> Error: if config is MultiplayerSynchronizer: print(\"Adding
synchronization configuration for %s. Synchronizer: %s\" % \[object,
config\]) elif config is MultiplayerSpawner: print(\"Adding node %s to
the spawn list. Spawner: %s\" % \[object, config\]) return
base_multiplayer.object_configuration_add(object, config)

\# Log configuration remove. E.g. root path (nullptr, NodePath),
replication (Node, Spawner\|Synchronizer), custom. func
[object_configuration_remove]{#object_configuration_remove}(object,
config: Variant) -\> Error: if config is MultiplayerSynchronizer:
print(\"Removing synchronization configuration for %s. Synchronizer:
%s\" % \[object, config\]) elif config is MultiplayerSpawner:
print(\"Removing node %s from the spawn list. Spawner: %s\" % \[object,
config\]) return base_multiplayer.object_configuration_remove(object,
config)

\# These can be optional, but in our case we want to extend
SceneMultiplayer, so forward everything. func
[set_multiplayer_peer]{#set_multiplayer_peer}(p_peer: MultiplayerPeer):
base_multiplayer.multiplayer_peer = p_peer

func [get_multiplayer_peer]{#get_multiplayer_peer}() -\> MultiplayerPeer:

:   return base_multiplayer.multiplayer_peer

func [get_unique_id]{#get_unique_id}() -\> int:

:   return base_multiplayer.get_unique_id()

func [get_remote_sender_id]{#get_remote_sender_id}() -\> int:

:   return base_multiplayer.get_remote_sender_id()

func [get_peer_ids]{#get_peer_ids}() -\> PackedInt32Array:

:   return base_multiplayer.get_peers()
:::
::::

Then in your main scene or in an autoload call
`SceneTree.set_multiplayer()<class_SceneTree_method_set_multiplayer>`{.interpreted-text
role="ref"} to start using your custom
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}:

:::: tabs
::: code-tab
gdscript

\# autoload.gd func [enter_tree]{#enter_tree}(): \# Sets our custom
multiplayer as the main one in SceneTree.
get_tree().set_multiplayer(LogMultiplayer.new())
:::
::::

Native extensions can alternatively use the
`MultiplayerAPI.set_default_interface()<class_MultiplayerAPI_method_set_default_interface>`{.interpreted-text
role="ref"} method during initialization to configure themselves as the
default implementation.

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

:::: {#class_MultiplayerAPIExtension_private_method__get_multiplayer_peer}
::: rst-class
classref-method
:::
::::

`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"}
**\_get_multiplayer_peer**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__get_multiplayer_peer>`{.interpreted-text
role="ref"}

Called when the
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} is retrieved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__get_peer_ids}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_get_peer_ids**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__get_peer_ids>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.get_peers()<class_MultiplayerAPI_method_get_peers>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__get_remote_sender_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_remote_sender_id**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__get_remote_sender_id>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.get_remote_sender_id()<class_MultiplayerAPI_method_get_remote_sender_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__get_unique_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_unique_id**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__get_unique_id>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.get_unique_id()<class_MultiplayerAPI_method_get_unique_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__object_configuration_add}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_object_configuration_add**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, configuration:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__object_configuration_add>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.object_configuration_add()<class_MultiplayerAPI_method_object_configuration_add>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__object_configuration_remove}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_object_configuration_remove**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, configuration:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__object_configuration_remove>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.object_configuration_remove()<class_MultiplayerAPI_method_object_configuration_remove>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_poll**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__poll>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.poll()<class_MultiplayerAPI_method_poll>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__rpc}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_rpc**(peer: `int<class_int>`{.interpreted-text role="ref"}, object:
`Object<class_Object>`{.interpreted-text role="ref"}, method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, args:
`Array<class_Array>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__rpc>`{.interpreted-text
role="ref"}

Callback for
`MultiplayerAPI.rpc()<class_MultiplayerAPI_method_rpc>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerAPIExtension_private_method__set_multiplayer_peer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_multiplayer_peer**(multiplayer_peer:
`MultiplayerPeer<class_MultiplayerPeer>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerAPIExtension_private_method__set_multiplayer_peer>`{.interpreted-text
role="ref"}

Called when the
`MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>`{.interpreted-text
role="ref"} is set.
