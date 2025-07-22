github_url
:   hide

::: {.meta keywords="network"}
:::

# MultiplayerSpawner {#class_MultiplayerSpawner}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Automatically replicates spawnable nodes from the authority to other
multiplayer peers.

::: rst-class
classref-introduction-group
:::

## Description

Spawnable scenes can be configured in the editor or through code (see
`add_spawnable_scene()<class_MultiplayerSpawner_method_add_spawnable_scene>`{.interpreted-text
role="ref"}).

Also supports custom node spawns through
`spawn()<class_MultiplayerSpawner_method_spawn>`{.interpreted-text
role="ref"}, calling
`spawn_function<class_MultiplayerSpawner_property_spawn_function>`{.interpreted-text
role="ref"} on all peers.

Internally, **MultiplayerSpawner** uses
`MultiplayerAPI.object_configuration_add()<class_MultiplayerAPI_method_object_configuration_add>`{.interpreted-text
role="ref"} to notify spawns passing the spawned node as the `object`
and itself as the `configuration`, and
`MultiplayerAPI.object_configuration_remove()<class_MultiplayerAPI_method_object_configuration_remove>`{.interpreted-text
role="ref"} to notify despawns in a similar way.

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

:::: {#class_MultiplayerSpawner_signal_despawned}
::: rst-class
classref-signal
:::
::::

**despawned**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerSpawner_signal_despawned>`{.interpreted-text
role="ref"}

Emitted when a spawnable scene or custom spawn was despawned by the
multiplayer authority. Only called on remote peers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_signal_spawned}
::: rst-class
classref-signal
:::
::::

**spawned**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_MultiplayerSpawner_signal_spawned>`{.interpreted-text
role="ref"}

Emitted when a spawnable scene or custom spawn was spawned by the
multiplayer authority. Only called on remote peers.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MultiplayerSpawner_property_spawn_function}
::: rst-class
classref-property
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**spawn_function**
`🔗<class_MultiplayerSpawner_property_spawn_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spawn_function**(value:
  `Callable<class_Callable>`{.interpreted-text role="ref"})
- `Callable<class_Callable>`{.interpreted-text role="ref"}
  **get_spawn_function**()

Method called on all peers when a custom
`spawn()<class_MultiplayerSpawner_method_spawn>`{.interpreted-text
role="ref"} is requested by the authority. Will receive the `data`
parameter, and should return a `Node<class_Node>`{.interpreted-text
role="ref"} that is not in the scene tree.

\*\*Note:\*\* The returned node should **not** be added to the scene
with `Node.add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}. This is done automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_property_spawn_limit}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **spawn_limit** = `0`
`🔗<class_MultiplayerSpawner_property_spawn_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spawn_limit**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_spawn_limit**()

Maximum number of nodes allowed to be spawned by this spawner. Includes
both spawnable scenes and custom spawns.

When set to `0` (the default), there is no limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_property_spawn_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **spawn_path**
= `NodePath("")`
`🔗<class_MultiplayerSpawner_property_spawn_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spawn_path**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_spawn_path**()

Path to the spawn root. Spawnable scenes that are added as direct
children are replicated to other peers.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MultiplayerSpawner_method_add_spawnable_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_spawnable_scene**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_MultiplayerSpawner_method_add_spawnable_scene>`{.interpreted-text
role="ref"}

Adds a scene path to spawnable scenes, making it automatically
replicated from the multiplayer authority to other peers when added as
children of the node pointed by
`spawn_path<class_MultiplayerSpawner_property_spawn_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_method_clear_spawnable_scenes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_spawnable_scenes**()
`🔗<class_MultiplayerSpawner_method_clear_spawnable_scenes>`{.interpreted-text
role="ref"}

Clears all spawnable scenes. Does not despawn existing instances on
remote peers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_method_get_spawnable_scene}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_spawnable_scene**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerSpawner_method_get_spawnable_scene>`{.interpreted-text
role="ref"}

Returns the spawnable scene path by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_method_get_spawnable_scene_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_spawnable_scene_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiplayerSpawner_method_get_spawnable_scene_count>`{.interpreted-text
role="ref"}

Returns the count of spawnable scene paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiplayerSpawner_method_spawn}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **spawn**(data:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`🔗<class_MultiplayerSpawner_method_spawn>`{.interpreted-text
role="ref"}

Requests a custom spawn, with `data` passed to
`spawn_function<class_MultiplayerSpawner_property_spawn_function>`{.interpreted-text
role="ref"} on all peers. Returns the locally spawned node instance
already inside the scene tree, and added as a child of the node pointed
by
`spawn_path<class_MultiplayerSpawner_property_spawn_path>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Spawnable scenes are spawned automatically.
`spawn()<class_MultiplayerSpawner_method_spawn>`{.interpreted-text
role="ref"} is only needed for custom spawns.
