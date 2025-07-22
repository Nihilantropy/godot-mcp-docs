github_url
:   hide

# PointMesh {#class_PointMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Mesh with a single point primitive.

::: rst-class
classref-introduction-group
:::

## Description

A **PointMesh** is a primitive mesh composed of a single point. Instead
of relying on triangles, points are rendered as a single rectangle on
the screen with a constant size. They are intended to be used with
particle systems, but can also be used as a cheap way to render
billboarded sprites (for example in a point cloud).

In order to be displayed, point meshes must be used with a material that
has a point size. The point size can be accessed in a shader with the
`POINT_SIZE` built-in, or in a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"} by
setting the
`BaseMaterial3D.use_point_size<class_BaseMaterial3D_property_use_point_size>`{.interpreted-text
role="ref"} and
`BaseMaterial3D.point_size<class_BaseMaterial3D_property_point_size>`{.interpreted-text
role="ref"} properties.

\*\*Note:\*\* When using point meshes, properties that normally affect
vertices will be ignored, including
`BaseMaterial3D.billboard_mode<class_BaseMaterial3D_property_billboard_mode>`{.interpreted-text
role="ref"},
`BaseMaterial3D.grow<class_BaseMaterial3D_property_grow>`{.interpreted-text
role="ref"}, and
`BaseMaterial3D.cull_mode<class_BaseMaterial3D_property_cull_mode>`{.interpreted-text
role="ref"}.
