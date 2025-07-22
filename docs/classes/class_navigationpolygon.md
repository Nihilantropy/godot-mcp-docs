github_url
:   hide

# NavigationPolygon {#class_NavigationPolygon}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A 2D navigation mesh that describes a traversable surface for
pathfinding.

::: rst-class
classref-introduction-group
:::

## Description

A navigation mesh can be created either by baking it with the help of
the `NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"}, or by adding vertices and convex polygon indices arrays
manually.

To bake a navigation mesh at least one outline needs to be added that
defines the outer bounds of the baked area.

::::: tabs
::: code-tab
gdscript

var new_navigation_mesh = NavigationPolygon.new() var bounding_outline =
PackedVector2Array(\[Vector2(0, 0), Vector2(0, 50), Vector2(50, 50),
Vector2(50, 0)\]) new_navigation_mesh.add_outline(bounding_outline)
NavigationServer2D.bake_from_source_geometry_data(new_navigation_mesh,
NavigationMeshSourceGeometryData2D.new());
\$NavigationRegion2D.navigation_polygon = new_navigation_mesh
:::

::: code-tab
csharp

var newNavigationMesh = new NavigationPolygon(); Vector2\[\]
boundingOutline = \[new Vector2(0, 0), new Vector2(0, 50), new
Vector2(50, 50), new Vector2(50, 0)\];
newNavigationMesh.AddOutline(boundingOutline);
NavigationServer2D.BakeFromSourceGeometryData(newNavigationMesh, new
NavigationMeshSourceGeometryData2D());
GetNode\<NavigationRegion2D\>(\"NavigationRegion2D\").NavigationPolygon
= newNavigationMesh;
:::
:::::

Adding vertices and polygon indices manually.

::::: tabs
::: code-tab
gdscript

var new_navigation_mesh = NavigationPolygon.new() var new_vertices =
PackedVector2Array(\[Vector2(0, 0), Vector2(0, 50), Vector2(50, 50),
Vector2(50, 0)\]) new_navigation_mesh.vertices = new_vertices var
new_polygon_indices = PackedInt32Array(\[0, 1, 2, 3\])
new_navigation_mesh.add_polygon(new_polygon_indices)
\$NavigationRegion2D.navigation_polygon = new_navigation_mesh
:::

::: code-tab
csharp

var newNavigationMesh = new NavigationPolygon(); Vector2\[\] newVertices
= \[new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new
Vector2(50, 0)\]; newNavigationMesh.Vertices = newVertices; int\[\]
newPolygonIndices = \[0, 1, 2, 3\];
newNavigationMesh.AddPolygon(newPolygonIndices);
GetNode\<NavigationRegion2D\>(\"NavigationRegion2D\").NavigationPolygon
= newNavigationMesh;
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationMeshes <../tutorials/navigation/navigation_using_navigationmeshes>`{.interpreted-text
  role="doc"}
- [Navigation Polygon 2D
  Demo](https://godotengine.org/asset-library/asset/2722)

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

## Enumerations

:::: {#enum_NavigationPolygon_SamplePartitionType}
::: rst-class
classref-enumeration
:::
::::

enum **SamplePartitionType**:
`🔗<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPolygon_constant_SAMPLE_PARTITION_CONVEX_PARTITION}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_CONVEX_PARTITION** = `0`

Convex partitioning that yields navigation mesh with convex polygons.

:::: {#class_NavigationPolygon_constant_SAMPLE_PARTITION_TRIANGULATE}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_TRIANGULATE** = `1`

Triangulation partitioning that yields navigation mesh with triangle
polygons.

:::: {#class_NavigationPolygon_constant_SAMPLE_PARTITION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_MAX** = `2`

Represents the size of the
`SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NavigationPolygon_ParsedGeometryType}
::: rst-class
classref-enumeration
:::
::::

enum **ParsedGeometryType**:
`🔗<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPolygon_constant_PARSED_GEOMETRY_MESH_INSTANCES}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_MESH_INSTANCES** = `0`

Parses mesh instances as obstruction geometry. This includes
`Polygon2D<class_Polygon2D>`{.interpreted-text role="ref"},
`MeshInstance2D<class_MeshInstance2D>`{.interpreted-text role="ref"},
`MultiMeshInstance2D<class_MultiMeshInstance2D>`{.interpreted-text
role="ref"}, and `TileMap<class_TileMap>`{.interpreted-text role="ref"}
nodes.

Meshes are only parsed when they use a 2D vertices surface format.

:::: {#class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_STATIC_COLLIDERS** = `1`

Parses `StaticBody2D<class_StaticBody2D>`{.interpreted-text role="ref"}
and `TileMap<class_TileMap>`{.interpreted-text role="ref"} colliders as
obstruction geometry. The collider should be in any of the layers
specified by
`parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationPolygon_constant_PARSED_GEOMETRY_BOTH}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_BOTH** = `2`

Both
`PARSED_GEOMETRY_MESH_INSTANCES<class_NavigationPolygon_constant_PARSED_GEOMETRY_MESH_INSTANCES>`{.interpreted-text
role="ref"} and
`PARSED_GEOMETRY_STATIC_COLLIDERS<class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationPolygon_constant_PARSED_GEOMETRY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_MAX** = `3`

Represents the size of the
`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NavigationPolygon_SourceGeometryMode}
::: rst-class
classref-enumeration
:::
::::

enum **SourceGeometryMode**:
`🔗<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPolygon_constant_SOURCE_GEOMETRY_ROOT_NODE_CHILDREN}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_ROOT_NODE_CHILDREN** = `0`

Scans the child nodes of the root node recursively for geometry.

:::: {#class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN** = `1`

Scans nodes in a group and their child nodes recursively for geometry.
The group is specified by
`source_geometry_group_name<class_NavigationPolygon_property_source_geometry_group_name>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_GROUPS_EXPLICIT** = `2`

Uses nodes in a group for geometry. The group is specified by
`source_geometry_group_name<class_NavigationPolygon_property_source_geometry_group_name>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationPolygon_constant_SOURCE_GEOMETRY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_MAX** = `3`

Represents the size of the
`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NavigationPolygon_property_agent_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **agent_radius** =
`10.0`
`🔗<class_NavigationPolygon_property_agent_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_agent_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_agent_radius**()

The distance to erode/shrink the walkable surface when baking the
navigation mesh.

\*\*Note:\*\* The radius must be equal or higher than `0.0`. If the
radius is `0.0`, it won\'t be possible to fix invalid outline overlaps
and other precision errors during the baking process. As a result, some
obstacles may be excluded incorrectly from the final navigation mesh, or
may delete the navigation mesh\'s polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_baking_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **baking_rect** =
`Rect2(0, 0, 0, 0)`
`🔗<class_NavigationPolygon_property_baking_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_baking_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_baking_rect**()

If the baking `Rect2<class_Rect2>`{.interpreted-text role="ref"} has an
area the navigation mesh baking will be restricted to its enclosing
area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_baking_rect_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**baking_rect_offset** = `Vector2(0, 0)`
`🔗<class_NavigationPolygon_property_baking_rect_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_baking_rect_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_baking_rect_offset**()

The position offset applied to the
`baking_rect<class_NavigationPolygon_property_baking_rect>`{.interpreted-text
role="ref"} `Rect2<class_Rect2>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_border_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **border_size** =
`0.0`
`🔗<class_NavigationPolygon_property_border_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_border_size**()

The size of the non-navigable border around the bake bounding area
defined by the
`baking_rect<class_NavigationPolygon_property_baking_rect>`{.interpreted-text
role="ref"} `Rect2<class_Rect2>`{.interpreted-text role="ref"}.

In conjunction with the
`baking_rect<class_NavigationPolygon_property_baking_rect>`{.interpreted-text
role="ref"} the border size can be used to bake tile aligned navigation
meshes without the tile edges being shrunk by
`agent_radius<class_NavigationPolygon_property_agent_radius>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_cell_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cell_size** = `1.0`
`🔗<class_NavigationPolygon_property_cell_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_cell_size**()

The cell size used to rasterize the navigation mesh vertices. Must match
with the cell size on the navigation map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_parsed_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **parsed_collision_mask**
= `4294967295`
`🔗<class_NavigationPolygon_property_parsed_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parsed_collision_mask**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_parsed_collision_mask**()

The physics layers to scan for static colliders.

Only used when
`parsed_geometry_type<class_NavigationPolygon_property_parsed_geometry_type>`{.interpreted-text
role="ref"} is
`PARSED_GEOMETRY_STATIC_COLLIDERS<class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS>`{.interpreted-text
role="ref"} or
`PARSED_GEOMETRY_BOTH<class_NavigationPolygon_constant_PARSED_GEOMETRY_BOTH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_parsed_geometry_type}
::: rst-class
classref-property
:::
::::

`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
role="ref"} **parsed_geometry_type** = `2`
`🔗<class_NavigationPolygon_property_parsed_geometry_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parsed_geometry_type**(value:
  `ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
  role="ref"})
- `ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`{.interpreted-text
  role="ref"} **get_parsed_geometry_type**()

Determines which type of nodes will be parsed as geometry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_sample_partition_type}
::: rst-class
classref-property
:::
::::

`SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
role="ref"} **sample_partition_type** = `0`
`🔗<class_NavigationPolygon_property_sample_partition_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sample_partition_type**(value:
  `SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
  role="ref"})
- `SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>`{.interpreted-text
  role="ref"} **get_sample_partition_type**()

Partitioning algorithm for creating the navigation mesh polys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_source_geometry_group_name}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**source_geometry_group_name** =
`&"navigation_polygon_source_geometry_group"`
`🔗<class_NavigationPolygon_property_source_geometry_group_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source_geometry_group_name**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_source_geometry_group_name**()

The group name of nodes that should be parsed for baking source
geometry.

Only used when
`source_geometry_mode<class_NavigationPolygon_property_source_geometry_mode>`{.interpreted-text
role="ref"} is
`SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN<class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN>`{.interpreted-text
role="ref"} or
`SOURCE_GEOMETRY_GROUPS_EXPLICIT<class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_property_source_geometry_mode}
::: rst-class
classref-property
:::
::::

`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
role="ref"} **source_geometry_mode** = `0`
`🔗<class_NavigationPolygon_property_source_geometry_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source_geometry_mode**(value:
  `SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
  role="ref"})
- `SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`{.interpreted-text
  role="ref"} **get_source_geometry_mode**()

The source of the geometry used when baking.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationPolygon_method_add_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_outline**(outline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationPolygon_method_add_outline>`{.interpreted-text
role="ref"}

Appends a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} that contains the vertices of an outline to the internal
array that contains all the outlines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_add_outline_at_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_outline_at_index**(outline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationPolygon_method_add_outline_at_index>`{.interpreted-text
role="ref"}

Adds a `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} that contains the vertices of an outline to the internal
array that contains all the outlines at a fixed position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_add_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_polygon**(polygon:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationPolygon_method_add_polygon>`{.interpreted-text
role="ref"}

Adds a polygon using the indices of the vertices you get when calling
`get_vertices()<class_NavigationPolygon_method_get_vertices>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_NavigationPolygon_method_clear>`{.interpreted-text role="ref"}

Clears the internal arrays for vertices and polygon indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_clear_outlines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_outlines**()
`🔗<class_NavigationPolygon_method_clear_outlines>`{.interpreted-text
role="ref"}

Clears the array of the outlines, but it doesn\'t clear the vertices and
the polygons that were created by them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_clear_polygons}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_polygons**()
`🔗<class_NavigationPolygon_method_clear_polygons>`{.interpreted-text
role="ref"}

Clears the array of polygons, but it doesn\'t clear the array of
outlines and vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_navigation_mesh}
::: rst-class
classref-method
:::
::::

`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
**get_navigation_mesh**()
`🔗<class_NavigationPolygon_method_get_navigation_mesh>`{.interpreted-text
role="ref"}

Returns the `NavigationMesh<class_NavigationMesh>`{.interpreted-text
role="ref"} resulting from this navigation polygon. This navigation mesh
can be used to update the navigation mesh of a region with the
`NavigationServer3D.region_set_navigation_mesh()<class_NavigationServer3D_method_region_set_navigation_mesh>`{.interpreted-text
role="ref"} API directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_outline}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_outline**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationPolygon_method_get_outline>`{.interpreted-text
role="ref"}

Returns a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} containing the vertices of an outline that was created in
the editor or by script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_outline_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_outline_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationPolygon_method_get_outline_count>`{.interpreted-text
role="ref"}

Returns the number of outlines that were created in the editor or by
script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_parsed_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_parsed_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationPolygon_method_get_parsed_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_polygon}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_polygon**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationPolygon_method_get_polygon>`{.interpreted-text
role="ref"}

Returns a `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"} containing the indices of the vertices of a created polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_polygon_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_polygon_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationPolygon_method_get_polygon_count>`{.interpreted-text
role="ref"}

Returns the count of all polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_get_vertices}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_vertices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationPolygon_method_get_vertices>`{.interpreted-text
role="ref"}

Returns a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} containing all the vertices being used to create the
polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_make_polygons_from_outlines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_polygons_from_outlines**()
`🔗<class_NavigationPolygon_method_make_polygons_from_outlines>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`NavigationServer2D.parse_source_geometry_data()<class_NavigationServer2D_method_parse_source_geometry_data>`{.interpreted-text
role="ref"} and
`NavigationServer2D.bake_from_source_geometry_data()<class_NavigationServer2D_method_bake_from_source_geometry_data>`{.interpreted-text
role="ref"} instead.

Creates polygons from the outlines added in the editor or by script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_remove_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_outline**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationPolygon_method_remove_outline>`{.interpreted-text
role="ref"}

Removes an outline created in the editor or by script. You have to call
`make_polygons_from_outlines()<class_NavigationPolygon_method_make_polygons_from_outlines>`{.interpreted-text
role="ref"} for the polygons to update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_set_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_outline**(idx: `int<class_int>`{.interpreted-text role="ref"},
outline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationPolygon_method_set_outline>`{.interpreted-text
role="ref"}

Changes an outline created in the editor or by script. You have to call
`make_polygons_from_outlines()<class_NavigationPolygon_method_make_polygons_from_outlines>`{.interpreted-text
role="ref"} for the polygons to update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_set_parsed_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_parsed_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationPolygon_method_set_parsed_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPolygon_method_set_vertices}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertices**(vertices:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationPolygon_method_set_vertices>`{.interpreted-text
role="ref"}

Sets the vertices that can be then indexed to create polygons with the
`add_polygon()<class_NavigationPolygon_method_add_polygon>`{.interpreted-text
role="ref"} method.
