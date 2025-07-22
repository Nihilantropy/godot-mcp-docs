github_url
:   hide

# ConcavePolygonShape2D {#class_ConcavePolygonShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D polyline shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 2D polyline shape, intended for use in physics. Used internally in
`CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"} when it\'s in
`CollisionPolygon2D.BUILD_SEGMENTS<class_CollisionPolygon2D_constant_BUILD_SEGMENTS>`{.interpreted-text
role="ref"} mode.

Being just a collection of interconnected line segments,
**ConcavePolygonShape2D** is the most freely configurable single 2D
shape. It can be used to form polygons of any nature, or even shapes
that don\'t enclose an area. However, **ConcavePolygonShape2D** is
*hollow* even if the interconnected line segments do enclose an area,
which often makes it unsuitable for physics or detection.

\*\*Note:\*\* When used for collision, **ConcavePolygonShape2D** is
intended to work with static
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text role="ref"}
nodes like `StaticBody2D<class_StaticBody2D>`{.interpreted-text
role="ref"} and will likely not behave well for
`CharacterBody2D<class_CharacterBody2D>`{.interpreted-text role="ref"}s
or `RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"}s in a
mode other than Static.

\*\*Warning:\*\* Physics bodies that are small have a chance to clip
through this shape when moving fast. This happens because on one frame,
the physics body may be on the \"outside\" of the shape, and on the next
frame it may be \"inside\" it. **ConcavePolygonShape2D** is hollow, so
it won\'t detect a collision.

\*\*Performance:\*\* Due to its complexity, **ConcavePolygonShape2D** is
the slowest 2D collision shape to check collisions against. Its use
should generally be limited to level geometry. If the polyline is
closed, `CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"}\'s
`CollisionPolygon2D.BUILD_SOLIDS<class_CollisionPolygon2D_constant_BUILD_SOLIDS>`{.interpreted-text
role="ref"} mode can be used, which decomposes the polygon into convex
ones; see
`ConvexPolygonShape2D<class_ConvexPolygonShape2D>`{.interpreted-text
role="ref"}\'s documentation for instructions.

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

:::: {#class_ConcavePolygonShape2D_property_segments}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **segments** = `PackedVector2Array()`
`🔗<class_ConcavePolygonShape2D_property_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_segments**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_segments**()

The array of points that make up the **ConcavePolygonShape2D**\'s line
segments. The array (of length divisible by two) is naturally divided
into pairs (one pair for each segment); each pair consists of the
starting point of a segment and the endpoint of a segment.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.
