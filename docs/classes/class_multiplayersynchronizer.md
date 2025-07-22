github_url
:   hide

::: {.meta keywords="network"}
:::

# MultiplayerSynchronizer {#class_MultiplayerSynchronizer}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Synchronizes properties from the multiplayer authority to the remote
peers.

::: rst-class
classref-introduction-group
:::

## Description

By default, **MultiplayerSynchronizer** synchronizes configured
properties to all peers.

Visibility can be handled directly with
`set_visibility_for()<class_MultiplayerSynchronizer_method_set_visibility_for>`{.interpreted-text
role="ref"} or as-needed with
`add_visibility_filter()<class_MultiplayerSynchronizer_method_add_visibility_filter>`{.interpreted-text
role="ref"} and
`update_visibility()<class_MultiplayerSynchronizer_method_update_visibility>`{.interpreted-text
role="ref"}.

`MultiplayerSpawner<class_MultiplayerSpawner>`{.interpreted-text
role="ref"}s will handle nodes according to visibility of synchronizers
as long as the node at
`root_path<class_MultiplayerSynchronizer_property_root_path>`{.interpreted-text
role="ref"} was spawned by one.

Internally, **MultiplayerSynchronizer** uses
`MultiplayerAPI.object_configuration_add()<class_MultiplayerAPI_method_object_configuration_add>`{.interpreted-text
role="ref"} to notify synchronization start passing the
`Node<class_Node>`{.interpreted-text role="ref"} at
`root_path<class_MultiplayerSynchronizer_property_root_path>`{.interpreted-text
role="ref"} as the `object` and itself as the `configuration`, and uses
`MultiplayerAPI.object_configuration_remove()<class_MultiplayerAPI_method_object_configuration_remove>`{.interpreted-text
role="ref"} to notify synchronization end in a similar way.

\*\*Note:\*\* Synchronization is not supported for
`Object<class_Object>`{.interpreted-text role="ref"} type properties,
like `Resource<class_Resource>`{.interpreted-text role="ref"}.
Properties that are unique to each peer, like the instance IDs of
`Object<class_Object>`{.interpreted-text role="ref"}s (see
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}) or `RID<class_RID>`{.interpreted-text role="ref"}s, will
also not work in synchronization.

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

## Signals

:::: {#class_MultiplayerSynchronizer_signal_delta_synchronized}
::: rst-class
classref-signal
:::
::::

**delta_synchronized**()
`🔗<class_MultiplayerSynchronizer_signal_delta_synchronized>`{.interpreted-text
role="ref"}

Emitted when a new delta synchronization state is received by this
synchronizer after the properties have been updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_signal_synchronized}
::: rst-class
classref-signal
:::
::::

**synchronized**()
`🔗<class_MultiplayerSynchronizer_signal_synchronized>`{.interpreted-text
role="ref"}

Emitted when a new synchronization state is received by this
synchronizer after the properties have been updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_signal_visibility_changed}
::: rst-class
classref-signal
:::
::::

**visibility_changed**(for_peer: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_MultiplayerSynchronizer_signal_visibility_changed>`{.interpreted-text
role="ref"}

Emitted when visibility of `for_peer` is updated. See
`update_visibility()<class_MultiplayerSynchronizer_method_update_visibility>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_MultiplayerSynchronizer_VisibilityUpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **VisibilityUpdateMode**:
`🔗<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_MultiplayerSynchronizer_constant_VISIBILITY_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
role="ref"} **VISIBILITY_PROCESS_IDLE** = `0`

Visibility filters are updated during process frames (see
`Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_MultiplayerSynchronizer_constant_VISIBILITY_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
role="ref"} **VISIBILITY_PROCESS_PHYSICS** = `1`

Visibility filters are updated during physics frames (see
`Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_MultiplayerSynchronizer_constant_VISIBILITY_PROCESS_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
role="ref"} **VISIBILITY_PROCESS_NONE** = `2`

Visibility filters are not updated automatically, and must be updated
manually by calling
`update_visibility()<class_MultiplayerSynchronizer_method_update_visibility>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MultiplayerSynchronizer_property_delta_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **delta_interval** =
`0.0`
`🔗<class_MultiplayerSynchronizer_property_delta_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_delta_interval**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_delta_interval**()

Time interval between delta synchronizations. Used when the replication
is set to
`SceneReplicationConfig.REPLICATION_MODE_ON_CHANGE<class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE>`{.interpreted-text
role="ref"}. If set to `0.0` (the default), delta synchronizations
happen every network process frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_property_public_visibility}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **public_visibility** =
`true`
`🔗<class_MultiplayerSynchronizer_property_public_visibility>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_public**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_visibility_public**()

Whether synchronization should be visible to all peers by default. See
`set_visibility_for()<class_MultiplayerSynchronizer_method_set_visibility_for>`{.interpreted-text
role="ref"} and
`add_visibility_filter()<class_MultiplayerSynchronizer_method_add_visibility_filter>`{.interpreted-text
role="ref"} for ways of configuring fine-grained visibility options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_property_replication_config}
::: rst-class
classref-property
:::
::::

`SceneReplicationConfig<class_SceneReplicationConfig>`{.interpreted-text
role="ref"} **replication_config**
`🔗<class_MultiplayerSynchronizer_property_replication_config>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_replication_config**(value:
  `SceneReplicationConfig<class_SceneReplicationConfig>`{.interpreted-text
  role="ref"})
- `SceneReplicationConfig<class_SceneReplicationConfig>`{.interpreted-text
  role="ref"} **get_replication_config**()

Resource containing which properties to synchronize.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_property_replication_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**replication_interval** = `0.0`
`🔗<class_MultiplayerSynchronizer_property_replication_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_replication_interval**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_replication_interval**()

Time interval between synchronizations. Used when the replication is set
to
`SceneReplicationConfig.REPLICATION_MODE_ALWAYS<class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS>`{.interpreted-text
role="ref"}. If set to `0.0` (the default), synchronizations happen
every network process frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_property_root_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **root_path** =
`NodePath("..")`
`🔗<class_MultiplayerSynchronizer_property_root_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_path**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_root_path**()

Node path that replicated properties are relative to.

If
`root_path<class_MultiplayerSynchronizer_property_root_path>`{.interpreted-text
role="ref"} was spawned by a
`MultiplayerSpawner<class_MultiplayerSpawner>`{.interpreted-text
role="ref"}, the node will be also be spawned and despawned based on
this synchronizer visibility options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_property_visibility_update_mode}
::: rst-class
classref-property
:::
::::

`VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
role="ref"} **visibility_update_mode** = `0`
`🔗<class_MultiplayerSynchronizer_property_visibility_update_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_update_mode**(value:
  `VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
  role="ref"})
- `VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>`{.interpreted-text
  role="ref"} **get_visibility_update_mode**()

Specifies when visibility filters are updated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MultiplayerSynchronizer_method_add_visibility_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_visibility_filter**(filter:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerSynchronizer_method_add_visibility_filter>`{.interpreted-text
role="ref"}

Adds a peer visibility filter for this synchronizer.

`filter` should take a peer ID `int<class_int>`{.interpreted-text
role="ref"} and return a `bool<class_bool>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_method_get_visibility_for}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_visibility_for**(peer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerSynchronizer_method_get_visibility_for>`{.interpreted-text
role="ref"}

Queries the current visibility for peer `peer`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_method_remove_visibility_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_visibility_filter**(filter:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerSynchronizer_method_remove_visibility_filter>`{.interpreted-text
role="ref"}

Removes a peer visibility filter from this synchronizer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_method_set_visibility_for}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_visibility_for**(peer: `int<class_int>`{.interpreted-text
role="ref"}, visible: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerSynchronizer_method_set_visibility_for>`{.interpreted-text
role="ref"}

Sets the visibility of `peer` to `visible`. If `peer` is `0`, the value
of
`public_visibility<class_MultiplayerSynchronizer_property_public_visibility>`{.interpreted-text
role="ref"} will be updated instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSynchronizer_method_update_visibility}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_visibility**(for_peer: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_MultiplayerSynchronizer_method_update_visibility>`{.interpreted-text
role="ref"}

Updates the visibility of `for_peer` according to visibility filters. If
`for_peer` is `0` (the default), all peers\' visibilties are updated.
