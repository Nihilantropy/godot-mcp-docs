github_url
:   hide

# NavigationMeshGenerator {#class_NavigationMeshGenerator}

**Deprecated:** This class may be changed or removed in future versions.

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Helper class for creating and clearing navigation meshes.

::: rst-class
classref-introduction-group
:::

## Description

This class is responsible for creating and clearing 3D navigation meshes
used as `NavigationMesh<class_NavigationMesh>`{.interpreted-text
role="ref"} resources inside
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"}. The **NavigationMeshGenerator** has very limited to no use
for 2D as the navigation mesh baking process expects 3D node types and
3D source geometry to parse.

The entire navigation mesh baking is best done in a separate thread as
the voxelization, collision tests and mesh optimization steps involved
are very slow and performance-intensive operations.

Navigation mesh baking happens in multiple steps and the result depends
on 3D source geometry and properties of the
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
resource. In the first step, starting from a root node and depending on
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
properties all valid 3D source geometry nodes are collected from the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. Second, all
collected nodes are parsed for their relevant 3D geometry data and a
combined 3D mesh is build. Due to the many different types of parsable
objects, from normal
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}s to
`CSGShape3D<class_CSGShape3D>`{.interpreted-text role="ref"}s or various
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"}s, some operations to collect geometry data can trigger
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
and `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} synchronizations. Server synchronization can have a negative
effect on baking time or framerate as it often involves
`Mutex<class_Mutex>`{.interpreted-text role="ref"} locking for thread
security. Many parsable objects and the continuous synchronization with
other threaded Servers can increase the baking time significantly. On
the other hand only a few but very large and complex objects will take
some time to prepare for the Servers which can noticeably stall the next
frame render. As a general rule the total number of parsable objects and
their individual size and complexity should be balanced to avoid
framerate issues or very long baking times. The combined mesh is then
passed to the Recast Navigation Object to test the source geometry for
walkable terrain suitable to
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
agent properties by creating a voxel world around the meshes bounding
area.

The finalized navigation mesh is then returned and stored inside the
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"} for
use as a resource inside
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"} nodes.

\*\*Note:\*\* Using meshes to not only define walkable surfaces but also
obstruct navigation baking does not always work. The navigation baking
has no concept of what is a geometry \"inside\" when dealing with mesh
source geometry and this is intentional. Depending on current baking
parameters, as soon as the obstructing mesh is large enough to fit a
navigation mesh area inside, the baking will generate navigation mesh
areas that are inside the obstructing source geometry mesh.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationMeshes <../tutorials/navigation/navigation_using_navigationmeshes>`{.interpreted-text
  role="doc"}

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

:::: {#class_NavigationMeshGenerator_method_bake}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bake**(navigation_mesh:
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"},
root_node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshGenerator_method_bake>`{.interpreted-text
role="ref"}

**Deprecated:** This method is deprecated due to core threading changes.
To upgrade existing code, first create a
`NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>`{.interpreted-text
role="ref"} resource. Use this resource with
`parse_source_geometry_data()<class_NavigationMeshGenerator_method_parse_source_geometry_data>`{.interpreted-text
role="ref"} to parse the `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"} for nodes that should contribute to the navigation mesh
baking. The `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
parsing needs to happen on the main thread. After the parsing is
finished use the resource with
`bake_from_source_geometry_data()<class_NavigationMeshGenerator_method_bake_from_source_geometry_data>`{.interpreted-text
role="ref"} to bake a navigation mesh.

Bakes the `navigation_mesh` with source geometry collected starting from
the `root_node`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshGenerator_method_bake_from_source_geometry_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bake_from_source_geometry_data**(navigation_mesh:
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"},
source_geometry_data:
`NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable())
`🔗<class_NavigationMeshGenerator_method_bake_from_source_geometry_data>`{.interpreted-text
role="ref"}

Bakes the provided `navigation_mesh` with the data from the provided
`source_geometry_data`. After the process is finished the optional
`callback` will be called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshGenerator_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear**(navigation_mesh:
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshGenerator_method_clear>`{.interpreted-text
role="ref"}

Removes all polygons and vertices from the provided `navigation_mesh`
resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshGenerator_method_parse_source_geometry_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**parse_source_geometry_data**(navigation_mesh:
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"},
source_geometry_data:
`NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>`{.interpreted-text
role="ref"}, root_node: `Node<class_Node>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"} = Callable())
`🔗<class_NavigationMeshGenerator_method_parse_source_geometry_data>`{.interpreted-text
role="ref"}

Parses the `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
for source geometry according to the properties of `navigation_mesh`.
Updates the provided `source_geometry_data` resource with the resulting
data. The resource can then be used to bake a navigation mesh with
`bake_from_source_geometry_data()<class_NavigationMeshGenerator_method_bake_from_source_geometry_data>`{.interpreted-text
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
