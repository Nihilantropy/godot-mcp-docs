github_url
:   hide

# ConvexPolygonShape3D {#class_ConvexPolygonShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D convex polyhedron shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D convex polyhedron shape, intended for use in physics. Usually used
to provide a shape for a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}.

\*\*ConvexPolygonShape3D\*\* is *solid*, which means it detects
collisions from objects that are fully inside it, unlike
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} which is hollow. This makes it more suitable for both
detection and physics.

\*\*Convex decomposition:\*\* A concave polyhedron can be split up into
several convex polyhedra. This allows dynamic physics bodies to have
complex concave collisions (at a performance cost) and can be achieved
by using several **ConvexPolygonShape3D** nodes. To generate a convex
decomposition from a mesh, select the
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
node, go to the **Mesh** menu that appears above the viewport, and
choose **Create Multiple Convex Collision Siblings**. Alternatively,
`MeshInstance3D.create_multiple_convex_collisions()<class_MeshInstance3D_method_create_multiple_convex_collisions>`{.interpreted-text
role="ref"} can be called in a script to perform this decomposition at
run-time.

\*\*Performance:\*\* **ConvexPolygonShape3D** is faster to check
collisions against compared to
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"}, but it is slower than primitive collision shapes such as
`SphereShape3D<class_SphereShape3D>`{.interpreted-text role="ref"} and
`BoxShape3D<class_BoxShape3D>`{.interpreted-text role="ref"}. Its use
should generally be limited to medium-sized objects that cannot have
their collision accurately represented by primitive shapes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)

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

:::: {#class_ConvexPolygonShape3D_property_points}
::: rst-class
classref-property
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **points** = `PackedVector3Array()`
`🔗<class_ConvexPolygonShape3D_property_points>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_points**(value:
  `PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
  role="ref"})
- `PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
  role="ref"} **get_points**()

The list of 3D points forming the convex polygon shape.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} for more details.
