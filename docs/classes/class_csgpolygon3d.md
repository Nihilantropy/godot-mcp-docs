github_url
:   hide

# CSGPolygon3D {#class_CSGPolygon3D}

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"} **\<** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Extrudes a 2D polygon shape to create a 3D mesh.

::: rst-class
classref-introduction-group
:::

## Description

An array of 2D points is extruded to quickly and easily create a variety
of 3D meshes. See also `CSGMesh3D<class_CSGMesh3D>`{.interpreted-text
role="ref"} for using 3D meshes as CSG nodes.

\*\*Note:\*\* CSG nodes are intended to be used for level prototyping.
Creating CSG nodes has a significant CPU cost compared to creating a
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
with a `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"}. Moving a CSG node within another CSG node also has a
significant CPU cost, so it should be avoided during gameplay.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Prototyping levels with CSG <../tutorials/3d/csg_tools>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CSGPolygon3D_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**: `🔗<enum_CSGPolygon3D_Mode>`{.interpreted-text
role="ref"}

:::: {#class_CSGPolygon3D_constant_MODE_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_CSGPolygon3D_Mode>`{.interpreted-text role="ref"}
**MODE_DEPTH** = `0`

The `polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} shape is extruded along the negative Z axis.

:::: {#class_CSGPolygon3D_constant_MODE_SPIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_CSGPolygon3D_Mode>`{.interpreted-text role="ref"}
**MODE_SPIN** = `1`

The `polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} shape is extruded by rotating it around the Y axis.

:::: {#class_CSGPolygon3D_constant_MODE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_CSGPolygon3D_Mode>`{.interpreted-text role="ref"}
**MODE_PATH** = `2`

The `polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} shape is extruded along the
`Path3D<class_Path3D>`{.interpreted-text role="ref"} specified in
`path_node<class_CSGPolygon3D_property_path_node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CSGPolygon3D_PathRotation}
::: rst-class
classref-enumeration
:::
::::

enum **PathRotation**:
`🔗<enum_CSGPolygon3D_PathRotation>`{.interpreted-text role="ref"}

:::: {#class_CSGPolygon3D_constant_PATH_ROTATION_POLYGON}
::: rst-class
classref-enumeration-constant
:::
::::

`PathRotation<enum_CSGPolygon3D_PathRotation>`{.interpreted-text
role="ref"} **PATH_ROTATION_POLYGON** = `0`

The `polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} shape is not rotated.

\*\*Note:\*\* Requires the path Z coordinates to continually decrease to
ensure viable shapes.

:::: {#class_CSGPolygon3D_constant_PATH_ROTATION_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`PathRotation<enum_CSGPolygon3D_PathRotation>`{.interpreted-text
role="ref"} **PATH_ROTATION_PATH** = `1`

The `polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} shape is rotated along the path, but it is not rotated
around the path axis.

\*\*Note:\*\* Requires the path Z coordinates to continually decrease to
ensure viable shapes.

:::: {#class_CSGPolygon3D_constant_PATH_ROTATION_PATH_FOLLOW}
::: rst-class
classref-enumeration-constant
:::
::::

`PathRotation<enum_CSGPolygon3D_PathRotation>`{.interpreted-text
role="ref"} **PATH_ROTATION_PATH_FOLLOW** = `2`

The `polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} shape follows the path and its rotations around the path
axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CSGPolygon3D_PathIntervalType}
::: rst-class
classref-enumeration
:::
::::

enum **PathIntervalType**:
`🔗<enum_CSGPolygon3D_PathIntervalType>`{.interpreted-text role="ref"}

:::: {#class_CSGPolygon3D_constant_PATH_INTERVAL_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PathIntervalType<enum_CSGPolygon3D_PathIntervalType>`{.interpreted-text
role="ref"} **PATH_INTERVAL_DISTANCE** = `0`

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is set to
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"},
`path_interval<class_CSGPolygon3D_property_path_interval>`{.interpreted-text
role="ref"} will determine the distance, in meters, each interval of the
path will extrude.

:::: {#class_CSGPolygon3D_constant_PATH_INTERVAL_SUBDIVIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`PathIntervalType<enum_CSGPolygon3D_PathIntervalType>`{.interpreted-text
role="ref"} **PATH_INTERVAL_SUBDIVIDE** = `1`

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is set to
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"},
`path_interval<class_CSGPolygon3D_property_path_interval>`{.interpreted-text
role="ref"} will subdivide the polygons along the path.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CSGPolygon3D_property_depth}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth** = `1.0`
`🔗<class_CSGPolygon3D_property_depth>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_depth**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_DEPTH<class_CSGPolygon3D_constant_MODE_DEPTH>`{.interpreted-text
role="ref"}, the depth of the extrusion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CSGPolygon3D_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

Material to use for the resulting mesh. The UV maps the top half of the
material to the extruded shape (U along the length of the extrusions and
V around the outline of the
`polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"}), the bottom-left quarter to the front end face, and the
bottom-right quarter to the back end face.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_mode}
::: rst-class
classref-property
:::
::::

`Mode<enum_CSGPolygon3D_Mode>`{.interpreted-text role="ref"} **mode** =
`0` `🔗<class_CSGPolygon3D_property_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode**(value: `Mode<enum_CSGPolygon3D_Mode>`{.interpreted-text
  role="ref"})
- `Mode<enum_CSGPolygon3D_Mode>`{.interpreted-text role="ref"}
  **get_mode**()

The `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} used to extrude the
`polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_continuous_u}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **path_continuous_u**
`🔗<class_CSGPolygon3D_property_path_continuous_u>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_continuous_u**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_path_continuous_u**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, by default, the top half of the
`material<class_CSGPolygon3D_property_material>`{.interpreted-text
role="ref"} is stretched along the entire length of the extruded shape.
If `false` the top half of the material is repeated every step of the
extrusion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **path_interval**
`🔗<class_CSGPolygon3D_property_path_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_interval**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_interval**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, the path interval or ratio of path points to extrusions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_interval_type}
::: rst-class
classref-property
:::
::::

`PathIntervalType<enum_CSGPolygon3D_PathIntervalType>`{.interpreted-text
role="ref"} **path_interval_type**
`🔗<class_CSGPolygon3D_property_path_interval_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_interval_type**(value:
  `PathIntervalType<enum_CSGPolygon3D_PathIntervalType>`{.interpreted-text
  role="ref"})
- `PathIntervalType<enum_CSGPolygon3D_PathIntervalType>`{.interpreted-text
  role="ref"} **get_path_interval_type**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, this will determine if the interval should be by distance
(`PATH_INTERVAL_DISTANCE<class_CSGPolygon3D_constant_PATH_INTERVAL_DISTANCE>`{.interpreted-text
role="ref"}) or subdivision fractions
(`PATH_INTERVAL_SUBDIVIDE<class_CSGPolygon3D_constant_PATH_INTERVAL_SUBDIVIDE>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_joined}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **path_joined**
`🔗<class_CSGPolygon3D_property_path_joined>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_joined**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_path_joined**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, if `true` the ends of the path are joined, by adding an
extrusion between the last and first points of the path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_local}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **path_local**
`🔗<class_CSGPolygon3D_property_path_local>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_local**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_path_local**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, if `true` the
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} of the
**CSGPolygon3D** is used as the starting point for the extrusions, not
the `Transform3D<class_Transform3D>`{.interpreted-text role="ref"} of
the `path_node<class_CSGPolygon3D_property_path_node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **path_node**
`🔗<class_CSGPolygon3D_property_path_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_node**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_path_node**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, the location of the
`Path3D<class_Path3D>`{.interpreted-text role="ref"} object used to
extrude the
`polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_rotation}
::: rst-class
classref-property
:::
::::

`PathRotation<enum_CSGPolygon3D_PathRotation>`{.interpreted-text
role="ref"} **path_rotation**
`🔗<class_CSGPolygon3D_property_path_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_rotation**(value:
  `PathRotation<enum_CSGPolygon3D_PathRotation>`{.interpreted-text
  role="ref"})
- `PathRotation<enum_CSGPolygon3D_PathRotation>`{.interpreted-text
  role="ref"} **get_path_rotation**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, the path rotation method used to rotate the
`polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} as it is extruded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_rotation_accurate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**path_rotation_accurate**
`🔗<class_CSGPolygon3D_property_path_rotation_accurate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_rotation_accurate**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_path_rotation_accurate**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, if `true` the polygon will be rotated according to the
proper tangent of the path at the sampled points. If `false` an
approximation is used, which decreases in accuracy as the number of
subdivisions decreases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_simplify_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**path_simplify_angle**
`🔗<class_CSGPolygon3D_property_path_simplify_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_simplify_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_simplify_angle**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, extrusions that are less than this angle, will be merged
together to reduce polygon count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_path_u_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **path_u_distance**
`🔗<class_CSGPolygon3D_property_path_u_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_u_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_u_distance**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>`{.interpreted-text
role="ref"}, this is the distance along the path, in meters, the texture
coordinates will tile. When set to 0, texture coordinates will match
geometry exactly with no tiling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array(0, 0, 0, 1, 1, 1, 1, 0)`
`🔗<class_CSGPolygon3D_property_polygon>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

The point array that defines the 2D polygon that is extruded. This can
be a convex or concave polygon with 3 or more points. The polygon must
*not* have any intersecting edges. Otherwise, triangulation will fail
and no mesh will be generated.

\*\*Note:\*\* If only 1 or 2 points are defined in
`polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"}, no mesh will be generated.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_smooth_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **smooth_faces** =
`false` `🔗<class_CSGPolygon3D_property_smooth_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_smooth_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_smooth_faces**()

If `true`, applies smooth shading to the extrusions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_spin_degrees}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spin_degrees**
`🔗<class_CSGPolygon3D_property_spin_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spin_degrees**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_spin_degrees**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_SPIN<class_CSGPolygon3D_constant_MODE_SPIN>`{.interpreted-text
role="ref"}, the total number of degrees the
`polygon<class_CSGPolygon3D_property_polygon>`{.interpreted-text
role="ref"} is rotated when extruding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGPolygon3D_property_spin_sides}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **spin_sides**
`🔗<class_CSGPolygon3D_property_spin_sides>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spin_sides**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_spin_sides**()

When `mode<class_CSGPolygon3D_property_mode>`{.interpreted-text
role="ref"} is
`MODE_SPIN<class_CSGPolygon3D_constant_MODE_SPIN>`{.interpreted-text
role="ref"}, the number of extrusions made.
