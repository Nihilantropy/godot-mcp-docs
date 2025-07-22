# Using NavigationMaps {#doc_navigation_using_navigationmaps}

![image](img/nav_maps.png)

A NavigationMap is an abstract navigation world on the NavigationServer
identified by a NavigationServer `RID<class_RID>`{.interpreted-text
role="ref"}.

A map can hold and connect a near infinite number of navigation regions
with navigation meshes to build the traversable areas of a game world
for pathfinding.

A map can contain avoidance agents. Collision avoidance will be
calculated based on the agents present in the map.

:::: note
::: title
Note
:::

Different NavigationMaps are completely isolated from each other but
navigation regions and avoidance agents can switch between different
maps. Switches will become effective on NavigationServer
synchronization.
::::

## Default navigation maps

By default Godot creates a navigation map for each
`World2D<class_World2D>`{.interpreted-text role="ref"} and
`World3D<class_World3D>`{.interpreted-text role="ref"} of the root
viewport.

The 2D default navigation map RID can be obtained with
`get_world_2d().get_navigation_map()` from any
`Node2D<class_Node2D>`{.interpreted-text role="ref"} inheriting Node.

The 3D default navigation map RID can be obtained with
`get_world_3d().get_navigation_map()` from any
`Node3D<class_Node3D>`{.interpreted-text role="ref"} inheriting Node.

:::::: tabs
.. code-tab:: gdscript 2D GDScript

extends Node2D

func [ready]{#ready}() -\> void:

:   var default_navigation_map_rid: RID =
    get_world_2d().get_navigation_map()

::: code-tab
csharp 2D C#
:::

public partial class MyNode2D : Node2D { public override void
[Ready]{#ready}() { Rid defaultNavigationMapRid =
GetWorld2D().NavigationMap; } }

::: code-tab
gdscript 3D GDScript
:::

extends Node3D

func [ready]{#ready}() -\> void:

:   var default_navigation_map_rid: RID =
    get_world_3d().get_navigation_map()

::: code-tab
csharp 3D C#
:::

public partial class MyNode3D : Node3D { public override void
[Ready]{#ready}() { Rid defaultNavigationMapRid =
GetWorld3D().NavigationMap; } }
::::::

## Creating new navigation maps

The NavigationServer can create and support as many navigation maps as
required for specific gameplay. Additional navigation maps are created
and handled by using the NavigationServer API directly e.g. to support
different avoidance agent or actor locomotion types.

For example uses of different navigation maps see
`doc_navigation_different_actor_types`{.interpreted-text role="ref"} and
`doc_navigation_different_actor_locomotion`{.interpreted-text
role="ref"}.

Each navigation map individually synchronizes queued changes to its
navigation regions and avoidance agents. A navigation map that has not
received changes will consume little to no processing time. Navigation
regions and avoidance agents can only be part of a single navigation map
but they can switch map at any time.

:::: note
::: title
Note
:::

A navigation map switch will take effect only after the next
NavigationServer synchronization.
::::

:::::: tabs
.. code-tab:: gdscript 2D GDScript

extends Node2D

func [ready]{#ready}() -\> void:

:   var new_navigation_map: RID = NavigationServer2D.map_create()
    NavigationServer2D.map_set_active(new_navigation_map, true)

::: code-tab
csharp 2D C#
:::

public partial class MyNode2D : Node2D { public override void
[Ready]{#ready}() { Rid newNavigationMap =
NavigationServer2D.MapCreate();
NavigationServer2D.MapSetActive(newNavigationMap, true); } }

::: code-tab
gdscript 3D GDScript
:::

extends Node3D

func [ready]{#ready}() -\> void:

:   var new_navigation_map: RID = NavigationServer3D.map_create()
    NavigationServer3D.map_set_active(new_navigation_map, true)

::: code-tab
csharp 3D C#
:::

public partial class MyNode3D : Node3D { public override void
[Ready]{#ready}() { Rid newNavigationMap =
NavigationServer3D.MapCreate();
NavigationServer3D.MapSetActive(newNavigationMap, true); } }
::::::

:::: note
::: title
Note
:::

There is no difference between navigation maps created with the
NavigationServer2D API or the NavigationServer3D API.
::::
