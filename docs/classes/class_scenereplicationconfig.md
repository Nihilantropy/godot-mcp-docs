github_url
:   hide

# SceneReplicationConfig {#class_SceneReplicationConfig}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Configuration for properties to synchronize with a
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"}.

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

:::: {#enum_SceneReplicationConfig_ReplicationMode}
::: rst-class
classref-enumeration
:::
::::

enum **ReplicationMode**:
`🔗<enum_SceneReplicationConfig_ReplicationMode>`{.interpreted-text
role="ref"}

:::: {#class_SceneReplicationConfig_constant_REPLICATION_MODE_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`{.interpreted-text
role="ref"} **REPLICATION_MODE_NEVER** = `0`

Do not keep the given property synchronized.

:::: {#class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`{.interpreted-text
role="ref"} **REPLICATION_MODE_ALWAYS** = `1`

Replicate the given property on process by constantly sending updates
using unreliable transfer mode.

:::: {#class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`{.interpreted-text
role="ref"} **REPLICATION_MODE_ON_CHANGE** = `2`

Replicate the given property on process by sending updates using
reliable transfer mode when its value changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SceneReplicationConfig_method_add_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_property**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_SceneReplicationConfig_method_add_property>`{.interpreted-text
role="ref"}

Adds the property identified by the given `path` to the list of the
properties being synchronized, optionally passing an `index`.

\*\*Note:\*\* For details on restrictions and limitations on property
synchronization, see
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_get_properties}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\]
**get_properties**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneReplicationConfig_method_get_properties>`{.interpreted-text
role="ref"}

Returns a list of synchronized property
`NodePath<class_NodePath>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_has_property}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_property**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneReplicationConfig_method_has_property>`{.interpreted-text
role="ref"}

Returns `true` if the given `path` is configured for synchronization.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_get_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**property_get_index**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneReplicationConfig_method_property_get_index>`{.interpreted-text
role="ref"}

Finds the index of the given `path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_get_replication_mode}
::: rst-class
classref-method
:::
::::

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`{.interpreted-text
role="ref"} **property_get_replication_mode**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SceneReplicationConfig_method_property_get_replication_mode>`{.interpreted-text
role="ref"}

Returns the replication mode for the property identified by the given
`path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_get_spawn}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**property_get_spawn**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SceneReplicationConfig_method_property_get_spawn>`{.interpreted-text
role="ref"}

Returns `true` if the property identified by the given `path` is
configured to be synchronized on spawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_get_sync}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**property_get_sync**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`🔗<class_SceneReplicationConfig_method_property_get_sync>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`property_get_replication_mode()<class_SceneReplicationConfig_method_property_get_replication_mode>`{.interpreted-text
role="ref"} instead.

Returns `true` if the property identified by the given `path` is
configured to be synchronized on process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_get_watch}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**property_get_watch**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SceneReplicationConfig_method_property_get_watch>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`property_get_replication_mode()<class_SceneReplicationConfig_method_property_get_replication_mode>`{.interpreted-text
role="ref"} instead.

Returns `true` if the property identified by the given `path` is
configured to be reliably synchronized when changes are detected on
process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_set_replication_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**property_set_replication_mode**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, mode:
`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`{.interpreted-text
role="ref"})
`🔗<class_SceneReplicationConfig_method_property_set_replication_mode>`{.interpreted-text
role="ref"}

Sets the synchronization mode for the property identified by the given
`path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_set_spawn}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**property_set_spawn**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SceneReplicationConfig_method_property_set_spawn>`{.interpreted-text
role="ref"}

Sets whether the property identified by the given `path` is configured
to be synchronized on spawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_set_sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**property_set_sync**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SceneReplicationConfig_method_property_set_sync>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`property_set_replication_mode()<class_SceneReplicationConfig_method_property_set_replication_mode>`{.interpreted-text
role="ref"} with
`REPLICATION_MODE_ALWAYS<class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS>`{.interpreted-text
role="ref"} instead.

Sets whether the property identified by the given `path` is configured
to be synchronized on process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_property_set_watch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**property_set_watch**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SceneReplicationConfig_method_property_set_watch>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`property_set_replication_mode()<class_SceneReplicationConfig_method_property_set_replication_mode>`{.interpreted-text
role="ref"} with
`REPLICATION_MODE_ON_CHANGE<class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE>`{.interpreted-text
role="ref"} instead.

Sets whether the property identified by the given `path` is configured
to be reliably synchronized when changes are detected on process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneReplicationConfig_method_remove_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_property**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`🔗<class_SceneReplicationConfig_method_remove_property>`{.interpreted-text
role="ref"}

Removes the property identified by the given `path` from the
configuration.
