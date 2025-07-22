github_url
:   hide

# ConcavePolygonShape3D {#class_ConcavePolygonShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D trimesh shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D trimesh shape, intended for use in physics. Usually used to provide
a shape for a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}.

Being just a collection of interconnected triangles,
**ConcavePolygonShape3D** is the most freely configurable single 3D
shape. It can be used to form polyhedra of any nature, or even shapes
that don\'t enclose a volume. However, **ConcavePolygonShape3D** is
*hollow* even if the interconnected triangles do enclose a volume, which
often makes it unsuitable for physics or detection.

\*\*Note:\*\* When used for collision, **ConcavePolygonShape3D** is
intended to work with static
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
nodes like `StaticBody3D<class_StaticBody3D>`{.interpreted-text
role="ref"} and will likely not behave well for
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"}s
or `RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}s in a
mode other than Static.

\*\*Warning:\*\* Physics bodies that are small have a chance to clip
through this shape when moving fast. This happens because on one frame,
the physics body may be on the \"outside\" of the shape, and on the next
frame it may be \"inside\" it. **ConcavePolygonShape3D** is hollow, so
it won\'t detect a collision.

\*\*Performance:\*\* Due to its complexity, **ConcavePolygonShape3D** is
the slowest 3D collision shape to check collisions against. Its use
should generally be limited to level geometry. For convex geometry,
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"} should be used. For dynamic physics bodies that need concave
collision, several
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"}s can be used to represent its collision by using convex
decomposition; see
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"}\'s documentation for instructions.

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

## Property Descriptions

:::: {#class_ConcavePolygonShape3D_property_backface_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **backface_collision**
= `false`
`🔗<class_ConcavePolygonShape3D_property_backface_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_backface_collision_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_backface_collision_enabled**()

If set to `true`, collisions occur on both sides of the concave shape
faces. Otherwise they occur only along the face normals.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ConcavePolygonShape3D_method_get_faces}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_faces**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConcavePolygonShape3D_method_get_faces>`{.interpreted-text
role="ref"}

Returns the faces of the trimesh shape as an array of vertices. The
array (of length divisible by three) is naturally divided into triples;
each triple of vertices defines a triangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConcavePolygonShape3D_method_set_faces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_faces**(faces:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})
`🔗<class_ConcavePolygonShape3D_method_set_faces>`{.interpreted-text
role="ref"}

Sets the faces of the trimesh shape from an array of vertices. The
`faces` array should be composed of triples such that each triple of
vertices defines a triangle.
