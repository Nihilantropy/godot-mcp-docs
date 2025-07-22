github_url
:   hide

# NavigationMesh {#class_NavigationMesh}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A navigation mesh that defines traversable areas and obstacles.

::: rst-class
classref-introduction-group
:::

## Description

A navigation mesh is a collection of polygons that define which areas of
an environment are traversable to aid agents in pathfinding through
complicated spaces.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationMeshes <../tutorials/navigation/navigation_using_navigationmeshes>`{.interpreted-text
  role="doc"}
- [3D Navigation Demo](https://godotengine.org/asset-library/asset/2743)

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

:::: {#enum_NavigationMesh_SamplePartitionType}
::: rst-class
classref-enumeration
:::
::::

enum **SamplePartitionType**:
`🔗<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"}

:::: {#class_NavigationMesh_constant_SAMPLE_PARTITION_WATERSHED}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_WATERSHED** = `0`

Watershed partitioning. Generally the best choice if you precompute the
navigation mesh, use this if you have large open areas.

:::: {#class_NavigationMesh_constant_SAMPLE_PARTITION_MONOTONE}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_MONOTONE** = `1`

Monotone partitioning. Use this if you want fast navigation mesh
generation.

:::: {#class_NavigationMesh_constant_SAMPLE_PARTITION_LAYERS}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_LAYERS** = `2`

Layer partitioning. Good choice to use for tiled navigation mesh with
medium and small sized tiles.

:::: {#class_NavigationMesh_constant_SAMPLE_PARTITION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"} **SAMPLE_PARTITION_MAX** = `3`

Represents the size of the
`SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NavigationMesh_ParsedGeometryType}
::: rst-class
classref-enumeration
:::
::::

enum **ParsedGeometryType**:
`🔗<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"}

:::: {#class_NavigationMesh_constant_PARSED_GEOMETRY_MESH_INSTANCES}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_MESH_INSTANCES** = `0`

Parses mesh instances as geometry. This includes
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"},
`CSGShape3D<class_CSGShape3D>`{.interpreted-text role="ref"}, and
`GridMap<class_GridMap>`{.interpreted-text role="ref"} nodes.

:::: {#class_NavigationMesh_constant_PARSED_GEOMETRY_STATIC_COLLIDERS}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_STATIC_COLLIDERS** = `1`

Parses `StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"}
colliders as geometry. The collider should be in any of the layers
specified by
`geometry_collision_mask<class_NavigationMesh_property_geometry_collision_mask>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationMesh_constant_PARSED_GEOMETRY_BOTH}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_BOTH** = `2`

Both
`PARSED_GEOMETRY_MESH_INSTANCES<class_NavigationMesh_constant_PARSED_GEOMETRY_MESH_INSTANCES>`{.interpreted-text
role="ref"} and
`PARSED_GEOMETRY_STATIC_COLLIDERS<class_NavigationMesh_constant_PARSED_GEOMETRY_STATIC_COLLIDERS>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationMesh_constant_PARSED_GEOMETRY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"} **PARSED_GEOMETRY_MAX** = `3`

Represents the size of the
`ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NavigationMesh_SourceGeometryMode}
::: rst-class
classref-enumeration
:::
::::

enum **SourceGeometryMode**:
`🔗<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"}

:::: {#class_NavigationMesh_constant_SOURCE_GEOMETRY_ROOT_NODE_CHILDREN}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_ROOT_NODE_CHILDREN** = `0`

Scans the child nodes of the root node recursively for geometry.

:::: {#class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN** = `1`

Scans nodes in a group and their child nodes recursively for geometry.
The group is specified by
`geometry_source_group_name<class_NavigationMesh_property_geometry_source_group_name>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_GROUPS_EXPLICIT** = `2`

Uses nodes in a group for geometry. The group is specified by
`geometry_source_group_name<class_NavigationMesh_property_geometry_source_group_name>`{.interpreted-text
role="ref"}.

:::: {#class_NavigationMesh_constant_SOURCE_GEOMETRY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"} **SOURCE_GEOMETRY_MAX** = `3`

Represents the size of the
`SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NavigationMesh_property_agent_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **agent_height** =
`1.5` `🔗<class_NavigationMesh_property_agent_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_agent_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_agent_height**()

The minimum floor to ceiling height that will still allow the floor area
to be considered walkable.

\*\*Note:\*\* While baking, this value will be rounded up to the nearest
multiple of
`cell_height<class_NavigationMesh_property_cell_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_agent_max_climb}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **agent_max_climb** =
`0.25`
`🔗<class_NavigationMesh_property_agent_max_climb>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_agent_max_climb**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_agent_max_climb**()

The minimum ledge height that is considered to still be traversable.

\*\*Note:\*\* While baking, this value will be rounded down to the
nearest multiple of
`cell_height<class_NavigationMesh_property_cell_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_agent_max_slope}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **agent_max_slope** =
`45.0`
`🔗<class_NavigationMesh_property_agent_max_slope>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_agent_max_slope**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_agent_max_slope**()

The maximum slope that is considered walkable, in degrees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_agent_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **agent_radius** =
`0.5` `🔗<class_NavigationMesh_property_agent_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_agent_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_agent_radius**()

The distance to erode/shrink the walkable area of the heightfield away
from obstructions.

\*\*Note:\*\* While baking, this value will be rounded up to the nearest
multiple of
`cell_size<class_NavigationMesh_property_cell_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The radius must be equal or higher than `0.0`. If the
radius is `0.0`, it won\'t be possible to fix invalid outline overlaps
and other precision errors during the baking process. As a result, some
obstacles may be excluded incorrectly from the final navigation mesh, or
may delete the navigation mesh\'s polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_border_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **border_size** =
`0.0` `🔗<class_NavigationMesh_property_border_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_border_size**()

The size of the non-navigable border around the bake bounding area.

In conjunction with the
`filter_baking_aabb<class_NavigationMesh_property_filter_baking_aabb>`{.interpreted-text
role="ref"} and a
`edge_max_error<class_NavigationMesh_property_edge_max_error>`{.interpreted-text
role="ref"} value at `1.0` or below the border size can be used to bake
tile aligned navigation meshes without the tile edges being shrunk by
`agent_radius<class_NavigationMesh_property_agent_radius>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If this value is not `0.0`, it will be rounded up to the
nearest multiple of
`cell_size<class_NavigationMesh_property_cell_size>`{.interpreted-text
role="ref"} during baking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_cell_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cell_height** =
`0.25` `🔗<class_NavigationMesh_property_cell_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_cell_height**()

The cell height used to rasterize the navigation mesh vertices on the Y
axis. Must match with the cell height on the navigation map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_cell_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cell_size** =
`0.25` `🔗<class_NavigationMesh_property_cell_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_cell_size**()

The cell size used to rasterize the navigation mesh vertices on the XZ
plane. Must match with the cell size on the navigation map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_detail_sample_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**detail_sample_distance** = `6.0`
`🔗<class_NavigationMesh_property_detail_sample_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_detail_sample_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_detail_sample_distance**()

The sampling distance to use when generating the detail mesh, in cell
unit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_detail_sample_max_error}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**detail_sample_max_error** = `1.0`
`🔗<class_NavigationMesh_property_detail_sample_max_error>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_detail_sample_max_error**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_detail_sample_max_error**()

The maximum distance the detail mesh surface should deviate from
heightfield, in cell unit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_edge_max_error}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **edge_max_error** =
`1.3`
`🔗<class_NavigationMesh_property_edge_max_error>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edge_max_error**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_edge_max_error**()

The maximum distance a simplified contour\'s border edges should deviate
the original raw contour.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_edge_max_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **edge_max_length** =
`0.0`
`🔗<class_NavigationMesh_property_edge_max_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edge_max_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_edge_max_length**()

The maximum allowed length for contour edges along the border of the
mesh. A value of `0.0` disables this feature.

\*\*Note:\*\* While baking, this value will be rounded up to the nearest
multiple of
`cell_size<class_NavigationMesh_property_cell_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_filter_baking_aabb}
::: rst-class
classref-property
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **filter_baking_aabb**
= `AABB(0, 0, 0, 0, 0, 0)`
`🔗<class_NavigationMesh_property_filter_baking_aabb>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_baking_aabb**(value: `AABB<class_AABB>`{.interpreted-text
  role="ref"})
- `AABB<class_AABB>`{.interpreted-text role="ref"}
  **get_filter_baking_aabb**()

If the baking `AABB<class_AABB>`{.interpreted-text role="ref"} has a
volume the navigation mesh baking will be restricted to its enclosing
area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_filter_baking_aabb_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**filter_baking_aabb_offset** = `Vector3(0, 0, 0)`
`🔗<class_NavigationMesh_property_filter_baking_aabb_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_baking_aabb_offset**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_filter_baking_aabb_offset**()

The position offset applied to the
`filter_baking_aabb<class_NavigationMesh_property_filter_baking_aabb>`{.interpreted-text
role="ref"} `AABB<class_AABB>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_filter_ledge_spans}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **filter_ledge_spans**
= `false`
`🔗<class_NavigationMesh_property_filter_ledge_spans>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_ledge_spans**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_filter_ledge_spans**()

If `true`, marks spans that are ledges as non-walkable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_filter_low_hanging_obstacles}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filter_low_hanging_obstacles** = `false`
`🔗<class_NavigationMesh_property_filter_low_hanging_obstacles>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_low_hanging_obstacles**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_filter_low_hanging_obstacles**()

If `true`, marks non-walkable spans as walkable if their maximum is
within
`agent_max_climb<class_NavigationMesh_property_agent_max_climb>`{.interpreted-text
role="ref"} of a walkable neighbor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_filter_walkable_low_height_spans}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filter_walkable_low_height_spans** = `false`
`🔗<class_NavigationMesh_property_filter_walkable_low_height_spans>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_walkable_low_height_spans**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_filter_walkable_low_height_spans**()

If `true`, marks walkable spans as not walkable if the clearance above
the span is less than
`agent_height<class_NavigationMesh_property_agent_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_geometry_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**geometry_collision_mask** = `4294967295`
`🔗<class_NavigationMesh_property_geometry_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The physics layers to scan for static colliders.

Only used when
`geometry_parsed_geometry_type<class_NavigationMesh_property_geometry_parsed_geometry_type>`{.interpreted-text
role="ref"} is
`PARSED_GEOMETRY_STATIC_COLLIDERS<class_NavigationMesh_constant_PARSED_GEOMETRY_STATIC_COLLIDERS>`{.interpreted-text
role="ref"} or
`PARSED_GEOMETRY_BOTH<class_NavigationMesh_constant_PARSED_GEOMETRY_BOTH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_geometry_parsed_geometry_type}
::: rst-class
classref-property
:::
::::

`ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
role="ref"} **geometry_parsed_geometry_type** = `2`
`🔗<class_NavigationMesh_property_geometry_parsed_geometry_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parsed_geometry_type**(value:
  `ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
  role="ref"})
- `ParsedGeometryType<enum_NavigationMesh_ParsedGeometryType>`{.interpreted-text
  role="ref"} **get_parsed_geometry_type**()

Determines which type of nodes will be parsed as geometry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_geometry_source_geometry_mode}
::: rst-class
classref-property
:::
::::

`SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
role="ref"} **geometry_source_geometry_mode** = `0`
`🔗<class_NavigationMesh_property_geometry_source_geometry_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source_geometry_mode**(value:
  `SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
  role="ref"})
- `SourceGeometryMode<enum_NavigationMesh_SourceGeometryMode>`{.interpreted-text
  role="ref"} **get_source_geometry_mode**()

The source of the geometry used when baking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_geometry_source_group_name}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**geometry_source_group_name** = `&"navigation_mesh_source_group"`
`🔗<class_NavigationMesh_property_geometry_source_group_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source_group_name**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_source_group_name**()

The name of the group to scan for geometry.

Only used when
`geometry_source_geometry_mode<class_NavigationMesh_property_geometry_source_geometry_mode>`{.interpreted-text
role="ref"} is
`SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN<class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN>`{.interpreted-text
role="ref"} or
`SOURCE_GEOMETRY_GROUPS_EXPLICIT<class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_region_merge_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **region_merge_size**
= `20.0`
`🔗<class_NavigationMesh_property_region_merge_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_merge_size**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_region_merge_size**()

Any regions with a size smaller than this will be merged with larger
regions if possible.

\*\*Note:\*\* This value will be squared to calculate the number of
cells. For example, a value of 20 will set the number of cells to 400.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_region_min_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **region_min_size** =
`2.0`
`🔗<class_NavigationMesh_property_region_min_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_min_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_region_min_size**()

The minimum size of a region for it to be created.

\*\*Note:\*\* This value will be squared to calculate the minimum number
of cells allowed to form isolated island areas. For example, a value of
8 will set the number of cells to 64.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_sample_partition_type}
::: rst-class
classref-property
:::
::::

`SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
role="ref"} **sample_partition_type** = `0`
`🔗<class_NavigationMesh_property_sample_partition_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sample_partition_type**(value:
  `SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
  role="ref"})
- `SamplePartitionType<enum_NavigationMesh_SamplePartitionType>`{.interpreted-text
  role="ref"} **get_sample_partition_type**()

Partitioning algorithm for creating the navigation mesh polys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_property_vertices_per_polygon}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**vertices_per_polygon** = `6.0`
`🔗<class_NavigationMesh_property_vertices_per_polygon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertices_per_polygon**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vertices_per_polygon**()

The maximum number of vertices allowed for polygons generated during the
contour to polygon conversion process.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationMesh_method_add_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_polygon**(polygon:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMesh_method_add_polygon>`{.interpreted-text
role="ref"}

Adds a polygon using the indices of the vertices you get when calling
`get_vertices()<class_NavigationMesh_method_get_vertices>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_NavigationMesh_method_clear>`{.interpreted-text role="ref"}

Clears the internal arrays for vertices and polygon indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_clear_polygons}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_polygons**()
`🔗<class_NavigationMesh_method_clear_polygons>`{.interpreted-text
role="ref"}

Clears the array of polygons, but it doesn\'t clear the array of
vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_create_from_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_from_mesh**(mesh: `Mesh<class_Mesh>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMesh_method_create_from_mesh>`{.interpreted-text
role="ref"}

Initializes the navigation mesh by setting the vertices and indices
according to a `Mesh<class_Mesh>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The given `mesh` must be of type
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"} and have an index array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_get_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMesh_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`geometry_collision_mask<class_NavigationMesh_property_geometry_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_get_polygon}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_polygon**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NavigationMesh_method_get_polygon>`{.interpreted-text
role="ref"}

Returns a `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"} containing the indices of the vertices of a created polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_get_polygon_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_polygon_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMesh_method_get_polygon_count>`{.interpreted-text
role="ref"}

Returns the number of polygons in the navigation mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_get_vertices}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_vertices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMesh_method_get_vertices>`{.interpreted-text
role="ref"}

Returns a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} containing all the vertices being used to create the
polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_set_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationMesh_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`geometry_collision_mask<class_NavigationMesh_property_geometry_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMesh_method_set_vertices}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertices**(vertices:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMesh_method_set_vertices>`{.interpreted-text
role="ref"}

Sets the vertices that can be then indexed to create polygons with the
`add_polygon()<class_NavigationMesh_method_add_polygon>`{.interpreted-text
role="ref"} method.
