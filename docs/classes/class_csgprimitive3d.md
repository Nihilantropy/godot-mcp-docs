github_url
:   hide

# CSGPrimitive3D {#class_CSGPrimitive3D}

**Inherits:** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `CSGBox3D<class_CSGBox3D>`{.interpreted-text
role="ref"}, `CSGCylinder3D<class_CSGCylinder3D>`{.interpreted-text
role="ref"}, `CSGMesh3D<class_CSGMesh3D>`{.interpreted-text role="ref"},
`CSGPolygon3D<class_CSGPolygon3D>`{.interpreted-text role="ref"},
`CSGSphere3D<class_CSGSphere3D>`{.interpreted-text role="ref"},
`CSGTorus3D<class_CSGTorus3D>`{.interpreted-text role="ref"}

Base class for CSG primitives.

::: rst-class
classref-introduction-group
:::

## Description

Parent class for various CSG primitives. It contains code and
functionality that is common between them. It cannot be used directly.
Instead use one of the various classes that inherit from it.

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

:::: {#class_CSGPrimitive3D_property_flip_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_faces** =
`false` `🔗<class_CSGPrimitive3D_property_flip_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flip_faces**()

If set, the order of the vertices in each triangle are reversed
resulting in the backside of the mesh being drawn.
