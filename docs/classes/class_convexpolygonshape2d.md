github_url
:   hide

# ConvexPolygonShape2D {#class_ConvexPolygonShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D convex polygon shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 2D convex polygon shape, intended for use in physics. Used internally
in `CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"} when it\'s in
`CollisionPolygon2D.BUILD_SOLIDS<class_CollisionPolygon2D_constant_BUILD_SOLIDS>`{.interpreted-text
role="ref"} mode.

\*\*ConvexPolygonShape2D\*\* is *solid*, which means it detects
collisions from objects that are fully inside it, unlike
`ConcavePolygonShape2D<class_ConcavePolygonShape2D>`{.interpreted-text
role="ref"} which is hollow. This makes it more suitable for both
detection and physics.

\*\*Convex decomposition:\*\* A concave polygon can be split up into
several convex polygons. This allows dynamic physics bodies to have
complex concave collisions (at a performance cost) and can be achieved
by using several **ConvexPolygonShape2D** nodes or by using the
`CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"} node in
`CollisionPolygon2D.BUILD_SOLIDS<class_CollisionPolygon2D_constant_BUILD_SOLIDS>`{.interpreted-text
role="ref"} mode. To generate a collision polygon from a sprite, select
the `Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} node, go to
the **Sprite2D** menu that appears above the viewport, and choose
**Create Polygon2D Sibling**.

\*\*Performance:\*\* **ConvexPolygonShape2D** is faster to check
collisions against compared to
`ConcavePolygonShape2D<class_ConcavePolygonShape2D>`{.interpreted-text
role="ref"}, but it is slower than primitive collision shapes such as
`CircleShape2D<class_CircleShape2D>`{.interpreted-text role="ref"} and
`RectangleShape2D<class_RectangleShape2D>`{.interpreted-text
role="ref"}. Its use should generally be limited to medium-sized objects
that cannot have their collision accurately represented by primitive
shapes.

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

:::: {#class_ConvexPolygonShape2D_property_points}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **points** = `PackedVector2Array()`
`🔗<class_ConvexPolygonShape2D_property_points>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_points**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_points**()

The polygon\'s list of vertices that form a convex hull. Can be in
either clockwise or counterclockwise order.

\*\*Warning:\*\* Only set this property to a list of points that
actually form a convex hull. Use
`set_point_cloud()<class_ConvexPolygonShape2D_method_set_point_cloud>`{.interpreted-text
role="ref"} to generate the convex hull of an arbitrary set of points.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ConvexPolygonShape2D_method_set_point_cloud}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_cloud**(point_cloud:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_ConvexPolygonShape2D_method_set_point_cloud>`{.interpreted-text
role="ref"}

Based on the set of points provided, this assigns the
`points<class_ConvexPolygonShape2D_property_points>`{.interpreted-text
role="ref"} property using the convex hull algorithm, removing all
unneeded points. See
`Geometry2D.convex_hull()<class_Geometry2D_method_convex_hull>`{.interpreted-text
role="ref"} for details.
