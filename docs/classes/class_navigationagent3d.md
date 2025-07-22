github_url
:   hide

# NavigationAgent3D {#class_NavigationAgent3D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D agent used to pathfind to a position while avoiding obstacles.

::: rst-class
classref-introduction-group
:::

## Description

A 3D agent used to pathfind to a position while avoiding static and
dynamic obstacles. The calculation can be used by the parent node to
dynamically move it along the path. Requires navigation data to work
correctly.

Dynamic obstacles are avoided using RVO collision avoidance. Avoidance
is computed before physics, so the pathfinding information can be used
safely in the physics step.

\*\*Note:\*\* After setting the
`target_position<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"} property, the
`get_next_path_position()<class_NavigationAgent3D_method_get_next_path_position>`{.interpreted-text
role="ref"} method must be used once every physics frame to update the
internal path logic of the navigation agent. The vector position it
returns should be used as the next movement position for the agent\'s
parent node.

\*\*Note:\*\* Several methods of this class, such as
`get_next_path_position()<class_NavigationAgent3D_method_get_next_path_position>`{.interpreted-text
role="ref"}, can trigger a new path calculation. Calling these in your
callback to an agent\'s signal, such as
`waypoint_reached<class_NavigationAgent3D_signal_waypoint_reached>`{.interpreted-text
role="ref"}, can cause infinite recursion. It is recommended to call
these methods in the physics step or, alternatively, delay their call
until the end of the frame (see
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"} or
`Object.CONNECT_DEFERRED<class_Object_constant_CONNECT_DEFERRED>`{.interpreted-text
role="ref"}).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationAgents <../tutorials/navigation/navigation_using_navigationagents>`{.interpreted-text
  role="doc"}

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

:::: {#class_NavigationAgent3D_signal_link_reached}
::: rst-class
classref-signal
:::
::::

**link_reached**(details:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_signal_link_reached>`{.interpreted-text
role="ref"}

Signals that the agent reached a navigation link. Emitted when the agent
moves within
`path_desired_distance<class_NavigationAgent3D_property_path_desired_distance>`{.interpreted-text
role="ref"} of the next position of the path when that position is a
navigation link.

The details dictionary may contain the following keys depending on the
value of
`path_metadata_flags<class_NavigationAgent3D_property_path_metadata_flags>`{.interpreted-text
role="ref"}:

- `position`: The start position of the link that was reached.
- `type`: Always
  `NavigationPathQueryResult3D.PATH_SEGMENT_TYPE_LINK<class_NavigationPathQueryResult3D_constant_PATH_SEGMENT_TYPE_LINK>`{.interpreted-text
  role="ref"}.
- `rid`: The `RID<class_RID>`{.interpreted-text role="ref"} of the link.
- `owner`: The object which manages the link (usually
  `NavigationLink3D<class_NavigationLink3D>`{.interpreted-text
  role="ref"}).
- `link_entry_position`: If `owner` is available and the owner is a
  `NavigationLink3D<class_NavigationLink3D>`{.interpreted-text
  role="ref"}, it will contain the global position of the link\'s point
  the agent is entering.
- `link_exit_position`: If `owner` is available and the owner is a
  `NavigationLink3D<class_NavigationLink3D>`{.interpreted-text
  role="ref"}, it will contain the global position of the link\'s point
  which the agent is exiting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_signal_navigation_finished}
::: rst-class
classref-signal
:::
::::

**navigation_finished**()
`🔗<class_NavigationAgent3D_signal_navigation_finished>`{.interpreted-text
role="ref"}

Signals that the agent\'s navigation has finished. If the target is
reachable, navigation ends when the target is reached. If the target is
unreachable, navigation ends when the last waypoint of the path is
reached. This signal is emitted only once per loaded path.

This signal will be emitted just after
`target_reached<class_NavigationAgent3D_signal_target_reached>`{.interpreted-text
role="ref"} when the target is reachable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_signal_path_changed}
::: rst-class
classref-signal
:::
::::

**path_changed**()
`🔗<class_NavigationAgent3D_signal_path_changed>`{.interpreted-text
role="ref"}

Emitted when the agent had to update the loaded path:

- because path was previously empty.
- because navigation map has changed.
- because agent pushed further away from the current path segment than
  the
  `path_max_distance<class_NavigationAgent3D_property_path_max_distance>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_signal_target_reached}
::: rst-class
classref-signal
:::
::::

**target_reached**()
`🔗<class_NavigationAgent3D_signal_target_reached>`{.interpreted-text
role="ref"}

Signals that the agent reached the target, i.e. the agent moved within
`target_desired_distance<class_NavigationAgent3D_property_target_desired_distance>`{.interpreted-text
role="ref"} of the
`target_position<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"}. This signal is emitted only once per loaded path.

This signal will be emitted just before
`navigation_finished<class_NavigationAgent3D_signal_navigation_finished>`{.interpreted-text
role="ref"} when the target is reachable.

It may not always be possible to reach the target but it should always
be possible to reach the final position. See
`get_final_position()<class_NavigationAgent3D_method_get_final_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_signal_velocity_computed}
::: rst-class
classref-signal
:::
::::

**velocity_computed**(safe_velocity:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_signal_velocity_computed>`{.interpreted-text
role="ref"}

Notifies when the collision avoidance velocity is calculated. Emitted
every update as long as
`avoidance_enabled<class_NavigationAgent3D_property_avoidance_enabled>`{.interpreted-text
role="ref"} is `true` and the agent has a navigation map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_signal_waypoint_reached}
::: rst-class
classref-signal
:::
::::

**waypoint_reached**(details:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_signal_waypoint_reached>`{.interpreted-text
role="ref"}

Signals that the agent reached a waypoint. Emitted when the agent moves
within
`path_desired_distance<class_NavigationAgent3D_property_path_desired_distance>`{.interpreted-text
role="ref"} of the next position of the path.

The details dictionary may contain the following keys depending on the
value of
`path_metadata_flags<class_NavigationAgent3D_property_path_metadata_flags>`{.interpreted-text
role="ref"}:

- `position`: The position of the waypoint that was reached.
- `type`: The type of navigation primitive (region or link) that
  contains this waypoint.
- `rid`: The `RID<class_RID>`{.interpreted-text role="ref"} of the
  containing navigation primitive (region or link).
- `owner`: The object which manages the containing navigation primitive
  (region or link).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NavigationAgent3D_property_avoidance_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **avoidance_enabled** =
`false`
`🔗<class_NavigationAgent3D_property_avoidance_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_avoidance_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_avoidance_enabled**()

If `true` the agent is registered for an RVO avoidance callback on the
`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}. When
`velocity<class_NavigationAgent3D_property_velocity>`{.interpreted-text
role="ref"} is set and the processing is completed a `safe_velocity`
Vector3 is received with a signal connection to
`velocity_computed<class_NavigationAgent3D_signal_velocity_computed>`{.interpreted-text
role="ref"}. Avoidance processing with many registered agents has a
significant performance cost and should only be enabled on agents that
currently require it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_avoidance_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **avoidance_layers** =
`1`
`🔗<class_NavigationAgent3D_property_avoidance_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_avoidance_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_avoidance_layers**()

A bitfield determining the avoidance layers for this NavigationAgent.
Other agents with a matching bit on the
`avoidance_mask<class_NavigationAgent3D_property_avoidance_mask>`{.interpreted-text
role="ref"} will avoid this agent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_avoidance_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **avoidance_mask** = `1`
`🔗<class_NavigationAgent3D_property_avoidance_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_avoidance_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_avoidance_mask**()

A bitfield determining what other avoidance agents and obstacles this
NavigationAgent will avoid when a bit matches at least one of their
`avoidance_layers<class_NavigationAgent3D_property_avoidance_layers>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_avoidance_priority}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**avoidance_priority** = `1.0`
`🔗<class_NavigationAgent3D_property_avoidance_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_avoidance_priority**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_avoidance_priority**()

The agent does not adjust the velocity for other agents that would match
the
`avoidance_mask<class_NavigationAgent3D_property_avoidance_mask>`{.interpreted-text
role="ref"} but have a lower
`avoidance_priority<class_NavigationAgent3D_property_avoidance_priority>`{.interpreted-text
role="ref"}. This in turn makes the other agents with lower priority
adjust their velocities even more to avoid collision with this agent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_debug_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **debug_enabled** =
`false`
`🔗<class_NavigationAgent3D_property_debug_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_debug_enabled**()

If `true` shows debug visuals for this agent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_debug_path_custom_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug_path_custom_color** = `Color(1, 1, 1, 1)`
`🔗<class_NavigationAgent3D_property_debug_path_custom_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_path_custom_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_debug_path_custom_color**()

If
`debug_use_custom<class_NavigationAgent3D_property_debug_use_custom>`{.interpreted-text
role="ref"} is `true` uses this color for this agent instead of global
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_debug_path_custom_point_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debug_path_custom_point_size** = `4.0`
`🔗<class_NavigationAgent3D_property_debug_path_custom_point_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_path_custom_point_size**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_debug_path_custom_point_size**()

If
`debug_use_custom<class_NavigationAgent3D_property_debug_use_custom>`{.interpreted-text
role="ref"} is `true` uses this rasterized point size for rendering path
points for this agent instead of global point size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_debug_use_custom}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **debug_use_custom** =
`false`
`🔗<class_NavigationAgent3D_property_debug_use_custom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_use_custom**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_debug_use_custom**()

If `true` uses the defined
`debug_path_custom_color<class_NavigationAgent3D_property_debug_path_custom_color>`{.interpreted-text
role="ref"} for this agent instead of global color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `1.0`
`🔗<class_NavigationAgent3D_property_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The height of the avoidance agent. Agents will ignore other agents or
obstacles that are above or below their current position + height in 2D
avoidance. Does nothing in 3D avoidance which uses radius spheres alone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_keep_y_velocity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **keep_y_velocity** =
`true`
`🔗<class_NavigationAgent3D_property_keep_y_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_y_velocity**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_keep_y_velocity**()

If `true`, and the agent uses 2D avoidance, it will remember the set
y-axis velocity and reapply it after the avoidance step. While 2D
avoidance has no y-axis and simulates on a flat plane this setting can
help to soften the most obvious clipping on uneven 3D geometry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_max_neighbors}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_neighbors** = `10`
`🔗<class_NavigationAgent3D_property_max_neighbors>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_neighbors**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_neighbors**()

The maximum number of neighbors for the agent to consider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_max_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_speed** =
`10.0`
`🔗<class_NavigationAgent3D_property_max_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_speed**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max_speed**()

The maximum speed that an agent can move.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_navigation_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **navigation_layers** =
`1`
`🔗<class_NavigationAgent3D_property_navigation_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_navigation_layers**()

A bitfield determining which navigation layers of navigation regions
this agent will use to calculate a path. Changing it during runtime will
clear the current navigation path and generate a new one, according to
the new navigation layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_neighbor_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **neighbor_distance**
= `50.0`
`🔗<class_NavigationAgent3D_property_neighbor_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_neighbor_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_neighbor_distance**()

The distance to search for other agents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_desired_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**path_desired_distance** = `1.0`
`🔗<class_NavigationAgent3D_property_path_desired_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_desired_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_desired_distance**()

The distance threshold before a path point is considered to be reached.
This allows agents to not have to hit a path point on the path exactly,
but only to reach its general area. If this value is set too high, the
NavigationAgent will skip points on the path, which can lead to it
leaving the navigation mesh. If this value is set too low, the
NavigationAgent will be stuck in a repath loop because it will
constantly overshoot the distance to the next point on each physics
frame update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_height_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**path_height_offset** = `0.0`
`🔗<class_NavigationAgent3D_property_path_height_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_height_offset**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_height_offset**()

The height offset is subtracted from the y-axis value of any vector path
position for this NavigationAgent. The NavigationAgent height offset
does not change or influence the navigation mesh or pathfinding query
result. Additional navigation maps that use regions with navigation
meshes that the developer baked with appropriate agent radius or height
values are required to support different-sized agents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **path_max_distance**
= `5.0`
`🔗<class_NavigationAgent3D_property_path_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_max_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_max_distance**()

The maximum distance the agent is allowed away from the ideal path to
the final position. This can happen due to trying to avoid collisions.
When the maximum distance is exceeded, it recalculates the ideal path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_metadata_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>`{.interpreted-text
role="ref"}\] **path_metadata_flags** = `7`
`🔗<class_NavigationAgent3D_property_path_metadata_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_metadata_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>`{.interpreted-text
  role="ref"}\] **get_path_metadata_flags**()

Additional information to return with the navigation path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_postprocessing}
::: rst-class
classref-property
:::
::::

`PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>`{.interpreted-text
role="ref"} **path_postprocessing** = `0`
`🔗<class_NavigationAgent3D_property_path_postprocessing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_postprocessing**(value:
  `PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>`{.interpreted-text
  role="ref"})
- `PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>`{.interpreted-text
  role="ref"} **get_path_postprocessing**()

The path postprocessing applied to the raw path corridor found by the
`pathfinding_algorithm<class_NavigationAgent3D_property_pathfinding_algorithm>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_return_max_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**path_return_max_length** = `0.0`
`🔗<class_NavigationAgent3D_property_path_return_max_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_return_max_length**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_return_max_length**()

The maximum allowed length of the returned path in world units. A path
will be clipped when going over this length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_return_max_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**path_return_max_radius** = `0.0`
`🔗<class_NavigationAgent3D_property_path_return_max_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_return_max_radius**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_return_max_radius**()

The maximum allowed radius in world units that the returned path can be
from the path start. The path will be clipped when going over this
radius. Compared to
`path_return_max_length<class_NavigationAgent3D_property_path_return_max_length>`{.interpreted-text
role="ref"}, this allows the agent to go that much further, if they need
to walk around a corner.

\*\*Note:\*\* This will perform a sphere clip considering only the
actual navigation mesh path points with the first path position being
the sphere\'s center.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_search_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**path_search_max_distance** = `0.0`
`🔗<class_NavigationAgent3D_property_path_search_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_search_max_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_search_max_distance**()

The maximum distance a searched polygon can be away from the start
polygon before the pathfinding cancels the search for a path to the
(possibly unreachable or very far away) target position polygon. In this
case the pathfinding resets and builds a path from the start polygon to
the polygon that was found closest to the target position so far. A
value of `0` or below counts as unlimited. In case of unlimited the
pathfinding will search all polygons connected with the start polygon
until either the target position polygon is found or all available
polygon search options are exhausted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_path_search_max_polygons}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**path_search_max_polygons** = `4096`
`🔗<class_NavigationAgent3D_property_path_search_max_polygons>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_search_max_polygons**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_path_search_max_polygons**()

The maximum number of polygons that are searched before the pathfinding
cancels the search for a path to the (possibly unreachable or very far
away) target position polygon. In this case the pathfinding resets and
builds a path from the start polygon to the polygon that was found
closest to the target position so far. A value of `0` or below counts as
unlimited. In case of unlimited the pathfinding will search all polygons
connected with the start polygon until either the target position
polygon is found or all available polygon search options are exhausted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_pathfinding_algorithm}
::: rst-class
classref-property
:::
::::

`PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>`{.interpreted-text
role="ref"} **pathfinding_algorithm** = `0`
`🔗<class_NavigationAgent3D_property_pathfinding_algorithm>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pathfinding_algorithm**(value:
  `PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>`{.interpreted-text
  role="ref"})
- `PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>`{.interpreted-text
  role="ref"} **get_pathfinding_algorithm**()

The pathfinding algorithm used in the path query.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_NavigationAgent3D_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The radius of the avoidance agent. This is the \"body\" of the avoidance
agent and not the avoidance maneuver starting radius (which is
controlled by
`neighbor_distance<class_NavigationAgent3D_property_neighbor_distance>`{.interpreted-text
role="ref"}).

Does not affect normal pathfinding. To change an actor\'s pathfinding
radius bake `NavigationMesh<class_NavigationMesh>`{.interpreted-text
role="ref"} resources with a different
`NavigationMesh.agent_radius<class_NavigationMesh_property_agent_radius>`{.interpreted-text
role="ref"} property and use different navigation maps for each actor
size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_simplify_epsilon}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **simplify_epsilon**
= `0.0`
`🔗<class_NavigationAgent3D_property_simplify_epsilon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_simplify_epsilon**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_simplify_epsilon**()

The path simplification amount in worlds units.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_simplify_path}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **simplify_path** =
`false`
`🔗<class_NavigationAgent3D_property_simplify_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_simplify_path**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_simplify_path**()

If `true` a simplified version of the path will be returned with less
critical path points removed. The simplification amount is controlled by
`simplify_epsilon<class_NavigationAgent3D_property_simplify_epsilon>`{.interpreted-text
role="ref"}. The simplification uses a variant of Ramer-Douglas-Peucker
algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following
issues that can arise with certain agent types and script behaviors.
E.g. \"steering\" agents or avoidance in \"open fields\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_target_desired_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**target_desired_distance** = `1.0`
`🔗<class_NavigationAgent3D_property_target_desired_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_desired_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_target_desired_distance**()

The distance threshold before the target is considered to be reached. On
reaching the target,
`target_reached<class_NavigationAgent3D_signal_target_reached>`{.interpreted-text
role="ref"} is emitted and navigation ends (see
`is_navigation_finished()<class_NavigationAgent3D_method_is_navigation_finished>`{.interpreted-text
role="ref"} and
`navigation_finished<class_NavigationAgent3D_signal_navigation_finished>`{.interpreted-text
role="ref"}).

You can make navigation end early by setting this property to a value
greater than
`path_desired_distance<class_NavigationAgent3D_property_path_desired_distance>`{.interpreted-text
role="ref"} (navigation will end before reaching the last waypoint).

You can also make navigation end closer to the target than each
individual path position by setting this property to a value lower than
`path_desired_distance<class_NavigationAgent3D_property_path_desired_distance>`{.interpreted-text
role="ref"} (navigation won\'t immediately end when reaching the last
waypoint). However, if the value set is too low, the agent will be stuck
in a repath loop because it will constantly overshoot the distance to
the target on each physics frame update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_target_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**target_position** = `Vector3(0, 0, 0)`
`🔗<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_position**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_target_position**()

If set, a new navigation path from the current agent position to the
`target_position<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"} is requested from the NavigationServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_time_horizon_agents}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**time_horizon_agents** = `1.0`
`🔗<class_NavigationAgent3D_property_time_horizon_agents>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_time_horizon_agents**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_time_horizon_agents**()

The minimal amount of time for which this agent\'s velocities, that are
computed with the collision avoidance algorithm, are safe with respect
to other agents. The larger the number, the sooner the agent will
respond to other agents, but less freedom in choosing its velocities. A
too high value will slow down agents movement considerably. Must be
positive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_time_horizon_obstacles}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**time_horizon_obstacles** = `0.0`
`🔗<class_NavigationAgent3D_property_time_horizon_obstacles>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_time_horizon_obstacles**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_time_horizon_obstacles**()

The minimal amount of time for which this agent\'s velocities, that are
computed with the collision avoidance algorithm, are safe with respect
to static avoidance obstacles. The larger the number, the sooner the
agent will respond to static avoidance obstacles, but less freedom in
choosing its velocities. A too high value will slow down agents movement
considerably. Must be positive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_use_3d_avoidance}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_3d_avoidance** =
`false`
`🔗<class_NavigationAgent3D_property_use_3d_avoidance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_3d_avoidance**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_3d_avoidance**()

If `true`, the agent calculates avoidance velocities in 3D
omnidirectionally, e.g. for games that take place in air, underwater or
space. Agents using 3D avoidance only avoid other agents using 3D
avoidance, and react to radius-based avoidance obstacles. They ignore
any vertex-based obstacles.

If `false`, the agent calculates avoidance velocities in 2D along the x
and z-axes, ignoring the y-axis. Agents using 2D avoidance only avoid
other agents using 2D avoidance, and react to radius-based avoidance
obstacles or vertex-based avoidance obstacles. Other agents using 2D
avoidance that are below or above their current position including
`height<class_NavigationAgent3D_property_height>`{.interpreted-text
role="ref"} are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_property_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **velocity** =
`Vector3(0, 0, 0)`
`🔗<class_NavigationAgent3D_property_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_velocity**()

Sets the new wanted velocity for the agent. The avoidance simulation
will try to fulfill this velocity if possible but will modify it to
avoid collision with other agents and obstacles. When an agent is
teleported to a new position, use
`set_velocity_forced()<class_NavigationAgent3D_method_set_velocity_forced>`{.interpreted-text
role="ref"} as well to reset the internal simulation velocity.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationAgent3D_method_distance_to_target}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_to_target**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_distance_to_target>`{.interpreted-text
role="ref"}

Returns the distance to the target position, using the agent\'s global
position. The user must set
`target_position<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"} in order for this to be accurate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_avoidance_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_avoidance_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_avoidance_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`avoidance_layers<class_NavigationAgent3D_property_avoidance_layers>`{.interpreted-text
role="ref"} bitmask is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_avoidance_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_avoidance_mask_value**(mask_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_avoidance_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified mask of the
`avoidance_mask<class_NavigationAgent3D_property_avoidance_mask>`{.interpreted-text
role="ref"} bitmask is enabled, given a `mask_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_current_navigation_path}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_current_navigation_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_current_navigation_path>`{.interpreted-text
role="ref"}

Returns this agent\'s current path from start to finish in global
coordinates. The path only updates when the target position is changed
or the agent requires a repath. The path array is not intended to be
used in direct path movement as the agent has its own internal path
logic that would get corrupted by changing the path array manually. Use
the intended
`get_next_path_position()<class_NavigationAgent3D_method_get_next_path_position>`{.interpreted-text
role="ref"} once every physics frame to receive the next path point for
the agents movement as this function also updates the internal path
logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_current_navigation_path_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_current_navigation_path_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_current_navigation_path_index>`{.interpreted-text
role="ref"}

Returns which index the agent is currently on in the navigation path\'s
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_current_navigation_result}
::: rst-class
classref-method
:::
::::

`NavigationPathQueryResult3D<class_NavigationPathQueryResult3D>`{.interpreted-text
role="ref"} **get_current_navigation_result**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_current_navigation_result>`{.interpreted-text
role="ref"}

Returns the path query result for the path the agent is currently
following.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_final_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_final_position**()
`🔗<class_NavigationAgent3D_method_get_final_position>`{.interpreted-text
role="ref"}

Returns the reachable final position of the current navigation path in
global coordinates. This position can change if the agent needs to
update the navigation path which makes the agent emit the
`path_changed<class_NavigationAgent3D_signal_path_changed>`{.interpreted-text
role="ref"} signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_navigation_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_navigation_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_navigation_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`navigation_layers<class_NavigationAgent3D_property_navigation_layers>`{.interpreted-text
role="ref"} bitmask is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_navigation_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_navigation_map>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map for this NavigationAgent node. This function returns
always the map set on the NavigationAgent node and not the map of the
abstract agent on the NavigationServer. If the agent map is changed
directly with the NavigationServer API the NavigationAgent node will not
be aware of the map change. Use
`set_navigation_map()<class_NavigationAgent3D_method_set_navigation_map>`{.interpreted-text
role="ref"} to change the navigation map for the NavigationAgent and
also update the agent on the NavigationServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_next_path_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_next_path_position**()
`🔗<class_NavigationAgent3D_method_get_next_path_position>`{.interpreted-text
role="ref"}

Returns the next position in global coordinates that can be moved to,
making sure that there are no static objects in the way. If the agent
does not have a navigation path, it will return the position of the
agent\'s parent. The use of this function once every physics frame is
required to update the internal path logic of the NavigationAgent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_path_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_path_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_path_length>`{.interpreted-text
role="ref"}

Returns the length of the currently calculated path. The returned value
is `0.0`, if the path is still calculating or no calculation has been
requested yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of this agent
on the `NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_is_navigation_finished}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_navigation_finished**()
`🔗<class_NavigationAgent3D_method_is_navigation_finished>`{.interpreted-text
role="ref"}

Returns `true` if the agent\'s navigation has finished. If the target is
reachable, navigation ends when the target is reached. If the target is
unreachable, navigation ends when the last waypoint of the path is
reached.

\*\*Note:\*\* While `true` prefer to stop calling update functions like
`get_next_path_position()<class_NavigationAgent3D_method_get_next_path_position>`{.interpreted-text
role="ref"}. This avoids jittering the standing agent due to calling
repeated path updates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_is_target_reachable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_target_reachable**()
`🔗<class_NavigationAgent3D_method_is_target_reachable>`{.interpreted-text
role="ref"}

Returns `true` if
`get_final_position()<class_NavigationAgent3D_method_get_final_position>`{.interpreted-text
role="ref"} is within
`target_desired_distance<class_NavigationAgent3D_property_target_desired_distance>`{.interpreted-text
role="ref"} of the
`target_position<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_is_target_reached}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_target_reached**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationAgent3D_method_is_target_reached>`{.interpreted-text
role="ref"}

Returns `true` if the agent reached the target, i.e. the agent moved
within
`target_desired_distance<class_NavigationAgent3D_property_target_desired_distance>`{.interpreted-text
role="ref"} of the
`target_position<class_NavigationAgent3D_property_target_position>`{.interpreted-text
role="ref"}. It may not always be possible to reach the target but it
should always be possible to reach the final position. See
`get_final_position()<class_NavigationAgent3D_method_get_final_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_set_avoidance_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_avoidance_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_method_set_avoidance_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`avoidance_layers<class_NavigationAgent3D_property_avoidance_layers>`{.interpreted-text
role="ref"} bitmask, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_set_avoidance_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_avoidance_mask_value**(mask_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_method_set_avoidance_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified mask in the
`avoidance_mask<class_NavigationAgent3D_property_avoidance_mask>`{.interpreted-text
role="ref"} bitmask, given a `mask_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_set_navigation_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_method_set_navigation_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`navigation_layers<class_NavigationAgent3D_property_navigation_layers>`{.interpreted-text
role="ref"} bitmask, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_set_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(navigation_map:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_method_set_navigation_map>`{.interpreted-text
role="ref"}

Sets the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map this NavigationAgent node should use and also updates the
`agent` on the NavigationServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationAgent3D_method_set_velocity_forced}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_velocity_forced**(velocity:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_NavigationAgent3D_method_set_velocity_forced>`{.interpreted-text
role="ref"}

Replaces the internal velocity in the collision avoidance simulation
with `velocity`. When an agent is teleported to a new position this
function should be used in the same frame. If called frequently this
function can get agents stuck.
