github_url
:   hide

# NavigationServer2D {#class_NavigationServer2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A server interface for low-level 2D navigation access.

::: rst-class
classref-introduction-group
:::

## Description

NavigationServer2D is the server that handles navigation maps, regions
and agents. It does not handle A\* navigation from
`AStar2D<class_AStar2D>`{.interpreted-text role="ref"} or
`AStarGrid2D<class_AStarGrid2D>`{.interpreted-text role="ref"}.

Maps are divided into regions, which are composed of navigation
polygons. Together, they define the traversable areas in the 2D world.

\*\*Note:\*\* Most **NavigationServer2D** changes take effect after the
next physics frame and not immediately. This includes all changes made
to maps, regions or agents by navigation-related nodes in the scene tree
or made through scripts.

For two regions to be connected to each other, they must share a similar
edge. An edge is considered connected to another if both of its two
vertices are at a distance less than `edge_connection_margin` to the
respective other edge\'s vertex.

You may assign navigation layers to regions with
`region_set_navigation_layers()<class_NavigationServer2D_method_region_set_navigation_layers>`{.interpreted-text
role="ref"}, which then can be checked upon when requesting a path with
`map_get_path()<class_NavigationServer2D_method_map_get_path>`{.interpreted-text
role="ref"}. This can be used to allow or deny certain areas for some
objects.

To use the collision avoidance system, you may use agents. You can set
an agent\'s target velocity, then the servers will emit a callback with
a modified velocity.

\*\*Note:\*\* The collision avoidance system ignores regions. Using the
modified velocity directly may move an agent outside of the traversable
area. This is a limitation of the collision avoidance system, any more
complex situation may require the use of the physics engine.

This server keeps tracks of any call and executes them during the sync
phase. This means that you can request any change to the map, using any
thread, without worrying.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationServer <../tutorials/navigation/navigation_using_navigationservers>`{.interpreted-text
  role="doc"}
- [Navigation Polygon 2D
  Demo](https://godotengine.org/asset-library/asset/2722)

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

:::: {#class_NavigationServer2D_signal_avoidance_debug_changed}
::: rst-class
classref-signal
:::
::::

**avoidance_debug_changed**()
`🔗<class_NavigationServer2D_signal_avoidance_debug_changed>`{.interpreted-text
role="ref"}

Emitted when avoidance debug settings are changed. Only available in
debug builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_signal_map_changed}
::: rst-class
classref-signal
:::
::::

**map_changed**(map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_signal_map_changed>`{.interpreted-text
role="ref"}

Emitted when a navigation map is updated, when a region moves or is
modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_signal_navigation_debug_changed}
::: rst-class
classref-signal
:::
::::

**navigation_debug_changed**()
`🔗<class_NavigationServer2D_signal_navigation_debug_changed>`{.interpreted-text
role="ref"}

Emitted when navigation debug settings are changed. Only available in
debug builds.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_NavigationServer2D_ProcessInfo}
::: rst-class
classref-enumeration
:::
::::

enum **ProcessInfo**:
`🔗<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text role="ref"}

:::: {#class_NavigationServer2D_constant_INFO_ACTIVE_MAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_ACTIVE_MAPS** = `0`

Constant to get the number of active navigation maps.

:::: {#class_NavigationServer2D_constant_INFO_REGION_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_REGION_COUNT** = `1`

Constant to get the number of active navigation regions.

:::: {#class_NavigationServer2D_constant_INFO_AGENT_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_AGENT_COUNT** = `2`

Constant to get the number of active navigation agents processing
avoidance.

:::: {#class_NavigationServer2D_constant_INFO_LINK_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_LINK_COUNT** = `3`

Constant to get the number of active navigation links.

:::: {#class_NavigationServer2D_constant_INFO_POLYGON_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_POLYGON_COUNT** = `4`

Constant to get the number of navigation mesh polygons.

:::: {#class_NavigationServer2D_constant_INFO_EDGE_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_EDGE_COUNT** = `5`

Constant to get the number of navigation mesh polygon edges.

:::: {#class_NavigationServer2D_constant_INFO_EDGE_MERGE_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_EDGE_MERGE_COUNT** = `6`

Constant to get the number of navigation mesh polygon edges that were
merged due to edge key overlap.

:::: {#class_NavigationServer2D_constant_INFO_EDGE_CONNECTION_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_EDGE_CONNECTION_COUNT** = `7`

Constant to get the number of navigation mesh polygon edges that are
considered connected by edge proximity.

:::: {#class_NavigationServer2D_constant_INFO_EDGE_FREE_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_EDGE_FREE_COUNT** = `8`

Constant to get the number of navigation mesh polygon edges that could
not be merged but may be still connected by edge proximity or with
links.

:::: {#class_NavigationServer2D_constant_INFO_OBSTACLE_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_OBSTACLE_COUNT** = `9`

Constant to get the number of active navigation obstacles.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationServer2D_method_agent_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **agent_create**()
`🔗<class_NavigationServer2D_method_agent_create>`{.interpreted-text
role="ref"}

Creates the agent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_avoidance_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**agent_get_avoidance_enabled**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_avoidance_enabled>`{.interpreted-text
role="ref"}

Return `true` if the specified `agent` uses avoidance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_avoidance_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**agent_get_avoidance_layers**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_avoidance_layers>`{.interpreted-text
role="ref"}

Returns the `avoidance_layers` bitmask of the specified `agent`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_avoidance_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**agent_get_avoidance_mask**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_avoidance_mask>`{.interpreted-text
role="ref"}

Returns the `avoidance_mask` bitmask of the specified `agent`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_avoidance_priority}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**agent_get_avoidance_priority**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_avoidance_priority>`{.interpreted-text
role="ref"}

Returns the `avoidance_priority` of the specified `agent`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **agent_get_map**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_map>`{.interpreted-text
role="ref"}

Returns the navigation map `RID<class_RID>`{.interpreted-text
role="ref"} the requested `agent` is currently assigned to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_max_neighbors}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**agent_get_max_neighbors**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_max_neighbors>`{.interpreted-text
role="ref"}

Returns the maximum number of other agents the specified `agent` takes
into account in the navigation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_max_speed}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**agent_get_max_speed**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_max_speed>`{.interpreted-text
role="ref"}

Returns the maximum speed of the specified `agent`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_neighbor_distance}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**agent_get_neighbor_distance**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_neighbor_distance>`{.interpreted-text
role="ref"}

Returns the maximum distance to other agents the specified `agent` takes
into account in the navigation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_paused}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**agent_get_paused**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_paused>`{.interpreted-text
role="ref"}

Returns `true` if the specified `agent` is paused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**agent_get_position**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_position>`{.interpreted-text
role="ref"}

Returns the position of the specified `agent` in world space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_radius}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**agent_get_radius**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_radius>`{.interpreted-text
role="ref"}

Returns the radius of the specified `agent`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_time_horizon_agents}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**agent_get_time_horizon_agents**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_time_horizon_agents>`{.interpreted-text
role="ref"}

Returns the minimal amount of time for which the specified `agent`\'s
velocities that are computed by the simulation are safe with respect to
other agents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_time_horizon_obstacles}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**agent_get_time_horizon_obstacles**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_time_horizon_obstacles>`{.interpreted-text
role="ref"}

Returns the minimal amount of time for which the specified `agent`\'s
velocities that are computed by the simulation are safe with respect to
static avoidance obstacles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_get_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**agent_get_velocity**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_get_velocity>`{.interpreted-text
role="ref"}

Returns the velocity of the specified `agent`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_has_avoidance_callback}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**agent_has_avoidance_callback**(agent:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_has_avoidance_callback>`{.interpreted-text
role="ref"}

Return `true` if the specified `agent` has an avoidance callback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_is_map_changed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**agent_is_map_changed**(agent: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_agent_is_map_changed>`{.interpreted-text
role="ref"}

Returns `true` if the map got changed the previous frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_avoidance_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_avoidance_callback**(agent:
`RID<class_RID>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_avoidance_callback>`{.interpreted-text
role="ref"}

Sets the callback `Callable<class_Callable>`{.interpreted-text
role="ref"} that gets called after each avoidance processing step for
the `agent`. The calculated `safe_velocity` will be dispatched with a
signal to the object just before the physics calculations.

\*\*Note:\*\* Created callbacks are always processed independently of
the SceneTree state as long as the agent is on a navigation map and not
freed. To disable the dispatch of a callback from an agent use
`agent_set_avoidance_callback()<class_NavigationServer2D_method_agent_set_avoidance_callback>`{.interpreted-text
role="ref"} again with an empty
`Callable<class_Callable>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_avoidance_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_avoidance_enabled**(agent:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_avoidance_enabled>`{.interpreted-text
role="ref"}

If `enabled` is `true`, the specified `agent` uses avoidance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_avoidance_layers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_avoidance_layers**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, layers: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_avoidance_layers>`{.interpreted-text
role="ref"}

Set the agent\'s `avoidance_layers` bitmask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_avoidance_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_avoidance_mask**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_avoidance_mask>`{.interpreted-text
role="ref"}

Set the agent\'s `avoidance_mask` bitmask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_avoidance_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_avoidance_priority**(agent:
`RID<class_RID>`{.interpreted-text role="ref"}, priority:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_avoidance_priority>`{.interpreted-text
role="ref"}

Set the agent\'s `avoidance_priority` with a `priority` between 0.0
(lowest priority) to 1.0 (highest priority).

The specified `agent` does not adjust the velocity for other agents that
would match the `avoidance_mask` but have a lower `avoidance_priority`.
This in turn makes the other agents with lower priority adjust their
velocities even more to avoid collision with this agent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_map**(agent: `RID<class_RID>`{.interpreted-text role="ref"},
map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_map>`{.interpreted-text
role="ref"}

Puts the agent in the map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_max_neighbors}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_max_neighbors**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, count: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_max_neighbors>`{.interpreted-text
role="ref"}

Sets the maximum number of other agents the agent takes into account in
the navigation. The larger this number, the longer the running time of
the simulation. If the number is too low, the simulation will not be
safe.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_max_speed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_max_speed**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, max_speed: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_max_speed>`{.interpreted-text
role="ref"}

Sets the maximum speed of the agent. Must be positive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_neighbor_distance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_neighbor_distance**(agent:
`RID<class_RID>`{.interpreted-text role="ref"}, distance:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_neighbor_distance>`{.interpreted-text
role="ref"}

Sets the maximum distance to other agents this agent takes into account
in the navigation. The larger this number, the longer the running time
of the simulation. If the number is too low, the simulation will not be
safe.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_paused}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_paused**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, paused: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_paused>`{.interpreted-text
role="ref"}

If `paused` is `true` the specified `agent` will not be processed. For
example, it will not calculate avoidance velocities or receive avoidance
callbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_position**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_position>`{.interpreted-text
role="ref"}

Sets the position of the agent in world space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_radius**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, radius: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_radius>`{.interpreted-text
role="ref"}

Sets the radius of the agent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_time_horizon_agents}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_time_horizon_agents**(agent:
`RID<class_RID>`{.interpreted-text role="ref"}, time_horizon:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_time_horizon_agents>`{.interpreted-text
role="ref"}

The minimal amount of time for which the agent\'s velocities that are
computed by the simulation are safe with respect to other agents. The
larger this number, the sooner this agent will respond to the presence
of other agents, but the less freedom this agent has in choosing its
velocities. A too high value will slow down agents movement
considerably. Must be positive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_time_horizon_obstacles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_time_horizon_obstacles**(agent:
`RID<class_RID>`{.interpreted-text role="ref"}, time_horizon:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_time_horizon_obstacles>`{.interpreted-text
role="ref"}

The minimal amount of time for which the agent\'s velocities that are
computed by the simulation are safe with respect to static avoidance
obstacles. The larger this number, the sooner this agent will respond to
the presence of static avoidance obstacles, but the less freedom this
agent has in choosing its velocities. A too high value will slow down
agents movement considerably. Must be positive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_velocity**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, velocity: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_velocity>`{.interpreted-text
role="ref"}

Sets `velocity` as the new wanted velocity for the specified `agent`.
The avoidance simulation will try to fulfill this velocity if possible
but will modify it to avoid collision with other agent\'s and obstacles.
When an agent is teleported to a new position far away use
`agent_set_velocity_forced()<class_NavigationServer2D_method_agent_set_velocity_forced>`{.interpreted-text
role="ref"} instead to reset the internal velocity state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_agent_set_velocity_forced}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**agent_set_velocity_forced**(agent: `RID<class_RID>`{.interpreted-text
role="ref"}, velocity: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_agent_set_velocity_forced>`{.interpreted-text
role="ref"}

Replaces the internal velocity in the collision avoidance simulation
with `velocity` for the specified `agent`. When an agent is teleported
to a new position far away this function should be used in the same
frame. If called frequently this function can get agents stuck.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_bake_from_source_geometry_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bake_from_source_geometry_data**(navigation_polygon:
`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"}, source_geometry_data:
`NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable())
`🔗<class_NavigationServer2D_method_bake_from_source_geometry_data>`{.interpreted-text
role="ref"}

Bakes the provided `navigation_polygon` with the data from the provided
`source_geometry_data`. After the process is finished the optional
`callback` will be called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_bake_from_source_geometry_data_async}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bake_from_source_geometry_data_async**(navigation_polygon:
`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"}, source_geometry_data:
`NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable())
`🔗<class_NavigationServer2D_method_bake_from_source_geometry_data_async>`{.interpreted-text
role="ref"}

Bakes the provided `navigation_polygon` with the data from the provided
`source_geometry_data` as an async task running on a background thread.
After the process is finished the optional `callback` will be called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_free_rid>`{.interpreted-text
role="ref"}

Destroys the given RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_get_debug_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_debug_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_get_debug_enabled>`{.interpreted-text
role="ref"}

Returns `true` when the NavigationServer has debug enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_get_maps}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**get_maps**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_get_maps>`{.interpreted-text
role="ref"}

Returns all created navigation map `RID<class_RID>`{.interpreted-text
role="ref"}s on the NavigationServer. This returns both 2D and 3D
created navigation maps as there is technically no distinction between
them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_get_process_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_process_info**(process_info:
`ProcessInfo<enum_NavigationServer2D_ProcessInfo>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_get_process_info>`{.interpreted-text
role="ref"}

Returns information about the current state of the NavigationServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_is_baking_navigation_polygon}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_baking_navigation_polygon**(navigation_polygon:
`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_is_baking_navigation_polygon>`{.interpreted-text
role="ref"}

Returns `true` when the provided navigation polygon is being baked on a
background thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **link_create**()
`🔗<class_NavigationServer2D_method_link_create>`{.interpreted-text
role="ref"}

Create a new link between two positions on a map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**link_get_enabled**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the specified `link` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_end_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**link_get_end_position**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_end_position>`{.interpreted-text
role="ref"}

Returns the ending position of this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_enter_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**link_get_enter_cost**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_enter_cost>`{.interpreted-text
role="ref"}

Returns the enter cost of this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_iteration_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**link_get_iteration_id**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_iteration_id>`{.interpreted-text
role="ref"}

Returns the current iteration ID of the navigation link. Every time the
navigation link changes and synchronizes, the iteration ID increases. An
iteration ID of `0` means the navigation link has never synchronized.

\*\*Note:\*\* The iteration ID will wrap around to `1` after reaching
its range limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **link_get_map**(link:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_map>`{.interpreted-text
role="ref"}

Returns the navigation map `RID<class_RID>`{.interpreted-text
role="ref"} the requested `link` is currently assigned to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_navigation_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**link_get_navigation_layers**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_navigation_layers>`{.interpreted-text
role="ref"}

Returns the navigation layers for this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_owner_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**link_get_owner_id**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_owner_id>`{.interpreted-text
role="ref"}

Returns the `ObjectID` of the object which manages this link.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_start_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**link_get_start_position**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_start_position>`{.interpreted-text
role="ref"}

Returns the starting position of this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_get_travel_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**link_get_travel_cost**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_get_travel_cost>`{.interpreted-text
role="ref"}

Returns the travel cost of this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_is_bidirectional}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**link_is_bidirectional**(link: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_link_is_bidirectional>`{.interpreted-text
role="ref"}

Returns whether this `link` can be travelled in both directions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_bidirectional}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_bidirectional**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, bidirectional: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_link_set_bidirectional>`{.interpreted-text
role="ref"}

Sets whether this `link` can be travelled in both directions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_enabled**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_link_set_enabled>`{.interpreted-text
role="ref"}

If `enabled` is `true`, the specified `link` will contribute to its
current navigation map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_end_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_end_position**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_link_set_end_position>`{.interpreted-text
role="ref"}

Sets the exit position for the `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_enter_cost}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_enter_cost**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, enter_cost: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_link_set_enter_cost>`{.interpreted-text
role="ref"}

Sets the `enter_cost` for this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_map**(link: `RID<class_RID>`{.interpreted-text role="ref"},
map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_link_set_map>`{.interpreted-text
role="ref"}

Sets the navigation map `RID<class_RID>`{.interpreted-text role="ref"}
for the link.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_navigation_layers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_navigation_layers**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, navigation_layers: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_link_set_navigation_layers>`{.interpreted-text
role="ref"}

Set the links\'s navigation layers. This allows selecting links from a
path request (when using
`map_get_path()<class_NavigationServer2D_method_map_get_path>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_owner_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_owner_id**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, owner_id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_link_set_owner_id>`{.interpreted-text
role="ref"}

Set the `ObjectID` of the object which manages this link.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_start_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_start_position**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_link_set_start_position>`{.interpreted-text
role="ref"}

Sets the entry position for this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_link_set_travel_cost}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**link_set_travel_cost**(link: `RID<class_RID>`{.interpreted-text
role="ref"}, travel_cost: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_link_set_travel_cost>`{.interpreted-text
role="ref"}

Sets the `travel_cost` for this `link`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **map_create**()
`🔗<class_NavigationServer2D_method_map_create>`{.interpreted-text
role="ref"}

Create a new map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_force_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_force_update**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_map_force_update>`{.interpreted-text
role="ref"}

**Deprecated:** This method is no longer supported, as it is
incompatible with asynchronous updates. It can only be used in a
single-threaded context, at your own risk.

This function immediately forces synchronization of the specified
navigation `map` `RID<class_RID>`{.interpreted-text role="ref"}. By
default navigation maps are only synchronized at the end of each physics
frame. This function can be used to immediately (re)calculate all the
navigation meshes and region connections of the navigation map. This
makes it possible to query a navigation path for a changed map
immediately and in the same frame (multiple times if needed).

Due to technical restrictions the current NavigationServer command queue
will be flushed. This means all already queued update commands for this
physics frame will be executed, even those intended for other maps,
regions and agents not part of the specified map. The expensive
computation of the navigation meshes and region connections of a map
will only be done for the specified map. Other maps will receive the
normal synchronization at the end of the physics frame. Should the
specified map receive changes after the forced update it will update
again as well when the other maps receive their update.

Avoidance processing and dispatch of the `safe_velocity` signals is
unaffected by this function and continues to happen for all maps and
agents at the end of the physics frame.

\*\*Note:\*\* With great power comes great responsibility. This function
should only be used by users that really know what they are doing and
have a good reason for it. Forcing an immediate update of a navigation
map requires locking the NavigationServer and flushing the entire
NavigationServer command queue. Not only can this severely impact the
performance of a game but it can also introduce bugs if used
inappropriately without much foresight.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_agents}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**map_get_agents**(map: `RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_agents>`{.interpreted-text
role="ref"}

Returns all navigation agents `RID<class_RID>`{.interpreted-text
role="ref"}s that are currently assigned to the requested navigation
`map`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_cell_size}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**map_get_cell_size**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_cell_size>`{.interpreted-text
role="ref"}

Returns the map cell size used to rasterize the navigation mesh
vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_closest_point}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**map_get_closest_point**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, to_point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_closest_point>`{.interpreted-text
role="ref"}

Returns the navigation mesh surface point closest to the provided
`to_point` on the navigation `map`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_closest_point_owner}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**map_get_closest_point_owner**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, to_point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_closest_point_owner>`{.interpreted-text
role="ref"}

Returns the owner region RID for the navigation mesh surface point
closest to the provided `to_point` on the navigation `map`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_edge_connection_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**map_get_edge_connection_margin**(map:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_edge_connection_margin>`{.interpreted-text
role="ref"}

Returns the edge connection margin of the map. The edge connection
margin is a distance used to connect two regions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_iteration_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**map_get_iteration_id**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_iteration_id>`{.interpreted-text
role="ref"}

Returns the current iteration id of the navigation map. Every time the
navigation map changes and synchronizes the iteration id increases. An
iteration id of 0 means the navigation map has never synchronized.

\*\*Note:\*\* The iteration id will wrap back to 1 after reaching its
range limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_link_connection_radius}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**map_get_link_connection_radius**(map:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_link_connection_radius>`{.interpreted-text
role="ref"}

Returns the link connection radius of the map. This distance is the
maximum range any link will search for navigation mesh polygons to
connect to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_links}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**map_get_links**(map: `RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_links>`{.interpreted-text
role="ref"}

Returns all navigation link `RID<class_RID>`{.interpreted-text
role="ref"}s that are currently assigned to the requested navigation
`map`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_merge_rasterizer_cell_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**map_get_merge_rasterizer_cell_scale**(map:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_merge_rasterizer_cell_scale>`{.interpreted-text
role="ref"}

Returns map\'s internal merge rasterizer cell scale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_obstacles}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**map_get_obstacles**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_obstacles>`{.interpreted-text
role="ref"}

Returns all navigation obstacle `RID<class_RID>`{.interpreted-text
role="ref"}s that are currently assigned to the requested navigation
`map`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_path}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **map_get_path**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, origin: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, destination: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, optimize: `bool<class_bool>`{.interpreted-text role="ref"},
navigation_layers: `int<class_int>`{.interpreted-text role="ref"} = 1)
`🔗<class_NavigationServer2D_method_map_get_path>`{.interpreted-text
role="ref"}

Returns the navigation path to reach the destination from the origin.
`navigation_layers` is a bitmask of all region navigation layers that
are allowed to be in the path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_random_point}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**map_get_random_point**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, navigation_layers: `int<class_int>`{.interpreted-text
role="ref"}, uniformly: `bool<class_bool>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_random_point>`{.interpreted-text
role="ref"}

Returns a random position picked from all map region polygons with
matching `navigation_layers`.

If `uniformly` is `true`, all map regions, polygons, and faces are
weighted by their surface area (slower).

If `uniformly` is `false`, just a random region and a random polygon are
picked (faster).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_regions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**map_get_regions**(map: `RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_regions>`{.interpreted-text
role="ref"}

Returns all navigation regions `RID<class_RID>`{.interpreted-text
role="ref"}s that are currently assigned to the requested navigation
`map`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_use_async_iterations}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**map_get_use_async_iterations**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_use_async_iterations>`{.interpreted-text
role="ref"}

Returns `true` if the `map` synchronization uses an async process that
runs on a background thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_get_use_edge_connections}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**map_get_use_edge_connections**(map: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_get_use_edge_connections>`{.interpreted-text
role="ref"}

Returns whether the navigation `map` allows navigation regions to use
edge connections to connect with other navigation regions within
proximity of the navigation map edge connection margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **map_is_active**(map:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_map_is_active>`{.interpreted-text
role="ref"}

Returns `true` if the map is active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_active**(map: `RID<class_RID>`{.interpreted-text role="ref"},
active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_map_set_active>`{.interpreted-text
role="ref"}

Sets the map active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_cell_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_cell_size**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, cell_size: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_map_set_cell_size>`{.interpreted-text
role="ref"}

Sets the map cell size used to rasterize the navigation mesh vertices.
Must match with the cell size of the used navigation meshes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_edge_connection_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_edge_connection_margin**(map:
`RID<class_RID>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_map_set_edge_connection_margin>`{.interpreted-text
role="ref"}

Set the map edge connection margin used to weld the compatible region
edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_link_connection_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_link_connection_radius**(map:
`RID<class_RID>`{.interpreted-text role="ref"}, radius:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_map_set_link_connection_radius>`{.interpreted-text
role="ref"}

Set the map\'s link connection radius used to connect links to
navigation polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_merge_rasterizer_cell_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_merge_rasterizer_cell_scale**(map:
`RID<class_RID>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_map_set_merge_rasterizer_cell_scale>`{.interpreted-text
role="ref"}

Set the map\'s internal merge rasterizer cell scale used to control
merging sensitivity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_use_async_iterations}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_use_async_iterations**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_map_set_use_async_iterations>`{.interpreted-text
role="ref"}

If `enabled` is `true` the `map` synchronization uses an async process
that runs on a background thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_map_set_use_edge_connections}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**map_set_use_edge_connections**(map: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_map_set_use_edge_connections>`{.interpreted-text
role="ref"}

Set the navigation `map` edge connection use. If `enabled` is `true`,
the navigation map allows navigation regions to use edge connections to
connect with other navigation regions within proximity of the navigation
map edge connection margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **obstacle_create**()
`🔗<class_NavigationServer2D_method_obstacle_create>`{.interpreted-text
role="ref"}

Creates a new navigation obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_avoidance_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**obstacle_get_avoidance_enabled**(obstacle:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_avoidance_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the provided `obstacle` has avoidance enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_avoidance_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**obstacle_get_avoidance_layers**(obstacle:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_avoidance_layers>`{.interpreted-text
role="ref"}

Returns the `avoidance_layers` bitmask of the specified `obstacle`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**obstacle_get_map**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_map>`{.interpreted-text
role="ref"}

Returns the navigation map `RID<class_RID>`{.interpreted-text
role="ref"} the requested `obstacle` is currently assigned to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_paused}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**obstacle_get_paused**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_paused>`{.interpreted-text
role="ref"}

Returns `true` if the specified `obstacle` is paused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**obstacle_get_position**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_position>`{.interpreted-text
role="ref"}

Returns the position of the specified `obstacle` in world space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_radius}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**obstacle_get_radius**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_radius>`{.interpreted-text
role="ref"}

Returns the radius of the specified dynamic `obstacle`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**obstacle_get_velocity**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_velocity>`{.interpreted-text
role="ref"}

Returns the velocity of the specified dynamic `obstacle`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_get_vertices}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **obstacle_get_vertices**(obstacle:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_obstacle_get_vertices>`{.interpreted-text
role="ref"}

Returns the outline vertices for the specified `obstacle`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_avoidance_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_avoidance_enabled**(obstacle:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_avoidance_enabled>`{.interpreted-text
role="ref"}

If `enabled` is `true`, the provided `obstacle` affects avoidance using
agents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_avoidance_layers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_avoidance_layers**(obstacle:
`RID<class_RID>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_avoidance_layers>`{.interpreted-text
role="ref"}

Set the obstacles\'s `avoidance_layers` bitmask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_map**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"}, map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_map>`{.interpreted-text
role="ref"}

Sets the navigation map `RID<class_RID>`{.interpreted-text role="ref"}
for the obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_paused}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_paused**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"}, paused: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_paused>`{.interpreted-text
role="ref"}

If `paused` is `true` the specified `obstacle` will not be processed.
For example, it will no longer affect avoidance velocities.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_position**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_position>`{.interpreted-text
role="ref"}

Sets the position of the obstacle in world space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_radius**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"}, radius: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_radius>`{.interpreted-text
role="ref"}

Sets the radius of the dynamic obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_velocity**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"}, velocity: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_velocity>`{.interpreted-text
role="ref"}

Sets `velocity` of the dynamic `obstacle`. Allows other agents to better
predict the movement of the dynamic obstacle. Only works in combination
with the radius of the obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_obstacle_set_vertices}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**obstacle_set_vertices**(obstacle: `RID<class_RID>`{.interpreted-text
role="ref"}, vertices:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_obstacle_set_vertices>`{.interpreted-text
role="ref"}

Sets the outline vertices for the obstacle. If the vertices are winded
in clockwise order agents will be pushed in by the obstacle, else they
will be pushed out.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_parse_source_geometry_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**parse_source_geometry_data**(navigation_polygon:
`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"}, source_geometry_data:
`NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`{.interpreted-text
role="ref"}, root_node: `Node<class_Node>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable())
`🔗<class_NavigationServer2D_method_parse_source_geometry_data>`{.interpreted-text
role="ref"}

Parses the `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
for source geometry according to the properties of `navigation_polygon`.
Updates the provided `source_geometry_data` resource with the resulting
data. The resource can then be used to bake a navigation mesh with
`bake_from_source_geometry_data()<class_NavigationServer2D_method_bake_from_source_geometry_data>`{.interpreted-text
role="ref"}. After the process is finished the optional `callback` will
be called.

\*\*Note:\*\* This function needs to run on the main thread or with a
deferred call as the SceneTree is not thread-safe.

\*\*Performance:\*\* While convenient, reading data arrays from
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resources can affect
the frame rate negatively. The data needs to be received from the GPU,
stalling the `RenderingServer<class_RenderingServer>`{.interpreted-text
role="ref"} in the process. For performance prefer the use of e.g.
collision shapes or creating the data arrays entirely in code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_query_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**query_path**(parameters:
`NavigationPathQueryParameters2D<class_NavigationPathQueryParameters2D>`{.interpreted-text
role="ref"}, result:
`NavigationPathQueryResult2D<class_NavigationPathQueryResult2D>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable())
`🔗<class_NavigationServer2D_method_query_path>`{.interpreted-text
role="ref"}

Queries a path in a given navigation map. Start and target position and
other parameters are defined through
`NavigationPathQueryParameters2D<class_NavigationPathQueryParameters2D>`{.interpreted-text
role="ref"}. Updates the provided
`NavigationPathQueryResult2D<class_NavigationPathQueryResult2D>`{.interpreted-text
role="ref"} result object with the path among other results requested by
the query. After the process is finished the optional `callback` will be
called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **region_create**()
`🔗<class_NavigationServer2D_method_region_create>`{.interpreted-text
role="ref"}

Creates a new region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_bounds}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**region_get_bounds**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_bounds>`{.interpreted-text
role="ref"}

Returns the axis-aligned rectangle for the `region`\'s transformed
navigation mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_closest_point}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**region_get_closest_point**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, to_point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_closest_point>`{.interpreted-text
role="ref"}

Returns the navigation mesh surface point closest to the provided
`to_point` on the navigation `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_connection_pathway_end}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**region_get_connection_pathway_end**(region:
`RID<class_RID>`{.interpreted-text role="ref"}, connection:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_connection_pathway_end>`{.interpreted-text
role="ref"}

Returns the ending point of a connection door. `connection` is an index
between 0 and the return value of
`region_get_connections_count()<class_NavigationServer2D_method_region_get_connections_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_connection_pathway_start}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**region_get_connection_pathway_start**(region:
`RID<class_RID>`{.interpreted-text role="ref"}, connection:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_connection_pathway_start>`{.interpreted-text
role="ref"}

Returns the starting point of a connection door. `connection` is an
index between 0 and the return value of
`region_get_connections_count()<class_NavigationServer2D_method_region_get_connections_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_connections_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**region_get_connections_count**(region:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_connections_count>`{.interpreted-text
role="ref"}

Returns how many connections this `region` has with other regions in the
map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**region_get_enabled**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the specified `region` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_enter_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**region_get_enter_cost**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_enter_cost>`{.interpreted-text
role="ref"}

Returns the enter cost of this `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_iteration_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**region_get_iteration_id**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_iteration_id>`{.interpreted-text
role="ref"}

Returns the current iteration ID of the navigation region. Every time
the navigation region changes and synchronizes, the iteration ID
increases. An iteration ID of `0` means the navigation region has never
synchronized.

\*\*Note:\*\* The iteration ID will wrap around to `1` after reaching
its range limit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**region_get_map**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_map>`{.interpreted-text
role="ref"}

Returns the navigation map `RID<class_RID>`{.interpreted-text
role="ref"} the requested `region` is currently assigned to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_navigation_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**region_get_navigation_layers**(region:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_navigation_layers>`{.interpreted-text
role="ref"}

Returns the region\'s navigation layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_owner_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**region_get_owner_id**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_owner_id>`{.interpreted-text
role="ref"}

Returns the `ObjectID` of the object which manages this region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_random_point}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**region_get_random_point**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, navigation_layers: `int<class_int>`{.interpreted-text
role="ref"}, uniformly: `bool<class_bool>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_random_point>`{.interpreted-text
role="ref"}

Returns a random position picked from all region polygons with matching
`navigation_layers`.

If `uniformly` is `true`, all region polygons and faces are weighted by
their surface area (slower).

If `uniformly` is `false`, just a random polygon and face is picked
(faster).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**region_get_transform**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_transform>`{.interpreted-text
role="ref"}

Returns the global transformation of this `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_travel_cost}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**region_get_travel_cost**(region: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_travel_cost>`{.interpreted-text
role="ref"}

Returns the travel cost of this `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_use_async_iterations}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**region_get_use_async_iterations**(region:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_use_async_iterations>`{.interpreted-text
role="ref"}

Returns `true` if the `region` uses an async synchronization process
that runs on a background thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_get_use_edge_connections}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**region_get_use_edge_connections**(region:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_get_use_edge_connections>`{.interpreted-text
role="ref"}

Returns whether the navigation `region` is set to use edge connections
to connect with other navigation regions within proximity of the
navigation map edge connection margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_owns_point}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**region_owns_point**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationServer2D_method_region_owns_point>`{.interpreted-text
role="ref"}

Returns `true` if the provided `point` in world space is currently owned
by the provided navigation `region`. Owned in this context means that
one of the region\'s navigation mesh polygon faces has a possible
position at the closest distance to this point compared to all other
navigation meshes from other navigation regions that are also registered
on the navigation map of the provided region.

If multiple navigation meshes have positions at equal distance the
navigation region whose polygons are processed first wins the ownership.
Polygons are processed in the same order that navigation regions were
registered on the NavigationServer.

\*\*Note:\*\* If navigation meshes from different navigation regions
overlap (which should be avoided in general) the result might not be
what is expected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_enabled**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_enabled>`{.interpreted-text
role="ref"}

If `enabled` is `true` the specified `region` will contribute to its
current navigation map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_enter_cost}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_enter_cost**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, enter_cost: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_region_set_enter_cost>`{.interpreted-text
role="ref"}

Sets the `enter_cost` for this `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_map**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_map>`{.interpreted-text
role="ref"}

Sets the map for the region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_navigation_layers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_navigation_layers**(region:
`RID<class_RID>`{.interpreted-text role="ref"}, navigation_layers:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_navigation_layers>`{.interpreted-text
role="ref"}

Set the region\'s navigation layers. This allows selecting regions from
a path request (when using
`map_get_path()<class_NavigationServer2D_method_map_get_path>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_navigation_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_navigation_polygon**(region:
`RID<class_RID>`{.interpreted-text role="ref"}, navigation_polygon:
`NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_region_set_navigation_polygon>`{.interpreted-text
role="ref"}

Sets the `navigation_polygon` for the region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_owner_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_owner_id**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, owner_id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_owner_id>`{.interpreted-text
role="ref"}

Set the `ObjectID` of the object which manages this region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_transform**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_transform>`{.interpreted-text
role="ref"}

Sets the global transformation for the region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_travel_cost}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_travel_cost**(region: `RID<class_RID>`{.interpreted-text
role="ref"}, travel_cost: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_region_set_travel_cost>`{.interpreted-text
role="ref"}

Sets the `travel_cost` for this `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_use_async_iterations}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_use_async_iterations**(region:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_use_async_iterations>`{.interpreted-text
role="ref"}

If `enabled` is `true` the `region` uses an async synchronization
process that runs on a background thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_region_set_use_edge_connections}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**region_set_use_edge_connections**(region:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_region_set_use_edge_connections>`{.interpreted-text
role="ref"}

If `enabled` is `true`, the navigation `region` will use edge
connections to connect with other navigation regions within proximity of
the navigation map edge connection margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_active**(active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_set_active>`{.interpreted-text
role="ref"}

Control activation of this server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_set_debug_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_debug_enabled**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_set_debug_enabled>`{.interpreted-text
role="ref"}

If `true` enables debug mode on the NavigationServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_simplify_path}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **simplify_path**(path:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, epsilon: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_NavigationServer2D_method_simplify_path>`{.interpreted-text
role="ref"}

Returns a simplified version of `path` with less critical path points
removed. The simplification amount is in worlds units and controlled by
`epsilon`. The simplification uses a variant of Ramer-Douglas-Peucker
algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following
issues that can arise with certain agent types and script behaviors.
E.g. \"steering\" agents or avoidance in \"open fields\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_source_geometry_parser_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**source_geometry_parser_create**()
`🔗<class_NavigationServer2D_method_source_geometry_parser_create>`{.interpreted-text
role="ref"}

Creates a new source geometry parser. If a
`Callable<class_Callable>`{.interpreted-text role="ref"} is set for the
parser with
`source_geometry_parser_set_callback()<class_NavigationServer2D_method_source_geometry_parser_set_callback>`{.interpreted-text
role="ref"} the callback will be called for every single node that gets
parsed whenever
`parse_source_geometry_data()<class_NavigationServer2D_method_parse_source_geometry_data>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationServer2D_method_source_geometry_parser_set_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**source_geometry_parser_set_callback**(parser:
`RID<class_RID>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_NavigationServer2D_method_source_geometry_parser_set_callback>`{.interpreted-text
role="ref"}

Sets the `callback` `Callable<class_Callable>`{.interpreted-text
role="ref"} for the specific source geometry `parser`. The
`Callable<class_Callable>`{.interpreted-text role="ref"} will receive a
call with the following parameters:

- `navigation_mesh` - The
  `NavigationPolygon<class_NavigationPolygon>`{.interpreted-text
  role="ref"} reference used to define the parse settings. Do NOT edit
  or add directly to the navigation mesh.
- `source_geometry_data` - The
  `NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`{.interpreted-text
  role="ref"} reference. Add custom source geometry for navigation mesh
  baking to this object.
- `node` - The `Node<class_Node>`{.interpreted-text role="ref"} that is
  parsed.
