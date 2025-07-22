github_url
:   hide

# CSGCombiner3D {#class_CSGCombiner3D}

**Inherits:** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CSG node that allows you to combine other CSG modifiers.

::: rst-class
classref-introduction-group
:::

## Description

For complex arrangements of shapes, it is sometimes needed to add
structure to your CSG nodes. The CSGCombiner3D node allows you to create
this structure. The node encapsulates the result of the CSG operations
of its children. In this way, it is possible to do operations on one set
of shapes that are children of one CSGCombiner3D node, and a set of
separate operations on a second set of shapes that are children of a
second CSGCombiner3D node, and then do an operation that takes the two
end results as its input to create the final shape.

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
