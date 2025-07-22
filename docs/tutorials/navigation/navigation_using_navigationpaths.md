# Using NavigationPaths {#doc_navigation_using_navigationpaths}

## Obtaining a NavigationPath

Navigation paths can be directly queried from the NavigationServer and
do not require any additional nodes or objects as long as the navigation
map has a navigation mesh to work with.

To obtain a 2D path, use
`NavigationServer2D.map_get_path(map, from, to, optimize, navigation_layers)`.

To obtain a 3D path, use
`NavigationServer3D.map_get_path(map, from, to, optimize, navigation_layers)`.

For more customizable navigation path queries that require additional
setup see
`doc_navigation_using_navigationpathqueryobjects`{.interpreted-text
role="ref"}.

One of the required parameters for the query is the RID of the
navigation map. Each game world has a default navigation map
automatically created. The default navigation maps can be retrieved with
`get_world_2d().get_navigation_map()` from any Node2D inheriting node or
`get_world_3d().get_navigation_map()` from any Node3D inheriting node.
The second and third parameters are the starting position and the target
position as Vector2 for 2D or Vector3 for 3D.

If the `optimized` parameter is `true`, path positions will be shortened
along polygon corners with an additional funnel algorithm pass. This
works well for free movement on navigation meshes with unequally sized
polygons as the path will hug around corners along the polygon corridor
found by the A\* algorithm. With small cells the A\* algorithm creates a
very narrow funnel corridor that can create ugly corner paths when used
with grids.

If the `optimized` parameter is `false`, path positions will be placed
at the center of each polygon edge. This works well for pure grid
movement on navigation meshes with equally sized polygons as the path
will go through the center of the grid cells. Outside of grids due to
polygons often covering large open areas with a single, long edge this
can create paths with unnecessary long detours.

:::::: tabs
.. code-tab:: gdscript 2D GDScript

extends Node2D

\# Basic query for a navigation path using the default navigation map.

func get_navigation_path(p_start_position: Vector2, p_target_position: Vector2) -\> PackedVector2Array:

:   

    if not is_inside_tree():

    :   return PackedVector2Array()

    var default_map_rid: RID = get_world_2d().get_navigation_map() var
    path: PackedVector2Array = NavigationServer2D.map_get_path(
    default_map_rid, p_start_position, p_target_position, true ) return
    path

::: code-tab
csharp 2D C#
:::

using Godot; using System;

public partial class MyNode2D : Node2D { // Basic query for a navigation
path using the default navigation map.

> private Vector2\[\] GetNavigationPath(Vector2 startPosition, Vector2
> targetPosition) { if (!IsInsideTree()) { return
> Array.Empty\<Vector2\>(); }
>
> > Rid defaultMapRid = GetWorld2D().NavigationMap; Vector2\[\] path =
> > NavigationServer2D.MapGetPath( defaultMapRid, startPosition,
> > targetPosition, true ); return path;
>
> }

}

::: code-tab
gdscript 3D GDScript
:::

extends Node3D

\# Basic query for a navigation path using the default navigation map.

func get_navigation_path(p_start_position: Vector3, p_target_position: Vector3) -\> PackedVector3Array:

:   

    if not is_inside_tree():

    :   return PackedVector3Array()

    var default_map_rid: RID = get_world_3d().get_navigation_map() var
    path: PackedVector3Array = NavigationServer3D.map_get_path(
    default_map_rid, p_start_position, p_target_position, true ) return
    path

::: code-tab
csharp 3D C#
:::

using Godot; using System;

public partial class MyNode3D : Node3D { // Basic query for a navigation
path using the default navigation map.

> private Vector3\[\] GetNavigationPath(Vector3 startPosition, Vector3
> targetPosition) { if (!IsInsideTree()) { return
> Array.Empty\<Vector3\>(); }
>
> > Rid defaultMapRid = GetWorld3D().NavigationMap; Vector3\[\] path =
> > NavigationServer3D.MapGetPath( defaultMapRid, startPosition,
> > targetPosition, true ); return path;
>
> }

}
::::::

A returned `path` by the NavigationServer will be a `PackedVector2Array`
for 2D or a `PackedVector3Array` for 3D. These are just a
memory-optimized `Array` of vector positions. All position vectors
inside the array are guaranteed to be inside a NavigationPolygon or
NavigationMesh. The path array, if not empty, has the navigation mesh
position closest to the starting position at the first index `path[0]`
position. The closest available navigation mesh position to the target
position is the last index `path[path.size()-1]` position. All indexes
between are the path points that an actor should follow to reach the
target without leaving the navigation mesh.

:::: note
::: title
Note
:::

If the target position is on a different navigation mesh that is not
merged or connected the navigation path will lead to the closest
possible position on the starting position navigation mesh.
::::

The following script moves a Node3D inheriting node along a navigation
path using the default navigation map by setting the target position
with `set_movement_target()`.

:::: tabs
.. code-tab:: gdscript GDScript

\@onready var default_3d_map_rid: RID =
get_world_3d().get_navigation_map()

var movement_speed: float = 4.0 var movement_delta: float var
path_point_margin: float = 0.5

var current_path_index: int = 0 var current_path_point: Vector3 var
current_path: PackedVector3Array

func set_movement_target(target_position: Vector3):

> var start_position: Vector3 = global_transform.origin
>
> current_path = NavigationServer3D.map_get_path(
>
> :   default_3d_map_rid, start_position, target_position, true
>
> )
>
> if not current_path.is_empty():
>
> :   current_path_index = 0 current_path_point = current_path\[0\]

func [physics_process]{#physics_process}(delta):

> 
>
> if current_path.is_empty():
>
> :   return
>
> movement_delta = movement_speed \* delta
>
> if global_transform.origin.distance_to(current_path_point) \<= path_point_margin:
>
> :   current_path_index += 1 if current_path_index \>=
>     current_path.size(): current_path = \[\] current_path_index = 0
>     current_path_point = global_transform.origin return
>
> current_path_point = current_path\[current_path_index\]
>
> var new_velocity: Vector3 =
> global_transform.origin.direction_to(current_path_point) \*
> movement_delta
>
> global_transform.origin =
> global_transform.origin.move_toward(global_transform.origin +
> new_velocity, movement_delta)

::: code-tab
csharp
:::

using Godot;

public partial class MyNode3D : Node3D { private Rid
[default3DMapRid]{#default3dmaprid};

> private float [movementSpeed]{#movementspeed} = 4.0f; private float
> [movementDelta]{#movementdelta}; private float
> [pathPointMargin]{#pathpointmargin} = 0.5f;
>
> private int [currentPathIndex]{#currentpathindex} = 0; private Vector3
> [currentPathPoint]{#currentpathpoint}; private Vector3\[\]
> [currentPath]{#currentpath};
>
> public override void [Ready]{#ready}() {
> [default3DMapRid]{#default3dmaprid} = GetWorld3D().NavigationMap; }
>
> private void SetMovementTarget(Vector3 targetPosition) { Vector3
> startPosition = GlobalTransform.Origin;
>
> > [currentPath]{#currentpath} =
> > NavigationServer3D.MapGetPath([default3DMapRid]{#default3dmaprid},
> > startPosition, targetPosition, true);
> >
> > if (!\_currentPath.IsEmpty()) {
> > [currentPathIndex]{#currentpathindex} = 0;
> > [currentPathPoint]{#currentpathpoint} =
> > [currentPath]{#currentpath}\[0\]; }
>
> }
>
> public override void [PhysicsProcess]{#physicsprocess}(double delta) {
> if ([currentPath.IsEmpty]{#currentpath.isempty}()) { return; }
>
> > [movementDelta]{#movementdelta} = [movementSpeed]{#movementspeed} \*
> > (float)delta;
> >
> > if
> > (GlobalTransform.Origin.DistanceTo([currentPathPoint]{#currentpathpoint})
> > \<= [pathPointMargin]{#pathpointmargin}) {
> > [currentPathIndex]{#currentpathindex} += 1; if
> > ([currentPathIndex]{#currentpathindex} \>=
> > [currentPath.Length]{#currentpath.length}) {
> > [currentPath]{#currentpath} = Array.Empty\<Vector3\>();
> > [currentPathIndex]{#currentpathindex} = 0;
> > [currentPathPoint]{#currentpathpoint} = GlobalTransform.Origin;
> > return; } }
> >
> > [currentPathPoint]{#currentpathpoint} =
> > [currentPath]{#currentpath}\[[currentPathIndex]{#currentpathindex}\];
> >
> > Vector3 newVelocity =
> > GlobalTransform.Origin.DirectionTo([currentPathPoint]{#currentpathpoint})
> > \* [movementDelta]{#movementdelta}; var globalTransform =
> > GlobalTransform; globalTransform.Origin =
> > globalTransform.Origin.MoveToward(globalTransform.Origin +
> > newVelocity, [movementDelta]{#movementdelta}); GlobalTransform =
> > globalTransform;
>
> }

}
::::
