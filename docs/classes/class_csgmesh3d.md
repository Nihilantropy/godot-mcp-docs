github_url
:   hide

# CSGMesh3D {#class_CSGMesh3D}

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"} **\<** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CSG Mesh shape that uses a mesh resource.

::: rst-class
classref-introduction-group
:::

## Description

This CSG node allows you to use any mesh resource as a CSG shape,
provided it is *manifold*. A manifold shape is closed, does not
self-intersect, does not contain internal faces and has no edges that
connect to more than two faces. See also
`CSGPolygon3D<class_CSGPolygon3D>`{.interpreted-text role="ref"} for
drawing 2D extruded polygons to be used as CSG nodes.

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

## Property Descriptions

:::: {#class_CSGMesh3D_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CSGMesh3D_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The `Material<class_Material>`{.interpreted-text role="ref"} used in
drawing the CSG shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGMesh3D_property_mesh}
::: rst-class
classref-property
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **mesh**
`🔗<class_CSGMesh3D_property_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
- `Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_mesh**()

The `Mesh<class_Mesh>`{.interpreted-text role="ref"} resource to use as
a CSG shape.

\*\*Note:\*\* Some `Mesh<class_Mesh>`{.interpreted-text role="ref"}
types such as `PlaneMesh<class_PlaneMesh>`{.interpreted-text
role="ref"}, `PointMesh<class_PointMesh>`{.interpreted-text role="ref"},
`QuadMesh<class_QuadMesh>`{.interpreted-text role="ref"}, and
`RibbonTrailMesh<class_RibbonTrailMesh>`{.interpreted-text role="ref"}
are excluded from the type hint for this property, as these primitives
are non-*manifold* and thus not compatible with the CSG algorithm.

\*\*Note:\*\* When using an
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}, all vertex
attributes except
`Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>`{.interpreted-text
role="ref"},
`Mesh.ARRAY_NORMAL<class_Mesh_constant_ARRAY_NORMAL>`{.interpreted-text
role="ref"} and
`Mesh.ARRAY_TEX_UV<class_Mesh_constant_ARRAY_TEX_UV>`{.interpreted-text
role="ref"} are left unused. Only
`Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>`{.interpreted-text
role="ref"} and
`Mesh.ARRAY_TEX_UV<class_Mesh_constant_ARRAY_TEX_UV>`{.interpreted-text
role="ref"} will be passed to the GPU.

`Mesh.ARRAY_NORMAL<class_Mesh_constant_ARRAY_NORMAL>`{.interpreted-text
role="ref"} is only used to determine which faces require the use of
flat shading. By default, CSGMesh will ignore the mesh\'s vertex
normals, recalculate them for each vertex and use a smooth shader. If a
flat shader is required for a face, ensure that all vertex normals of
the face are approximately equal.
