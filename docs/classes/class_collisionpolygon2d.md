github_url
:   hide

# CollisionPolygon2D {#class_CollisionPolygon2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that provides a polygon shape to a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} parent.

::: rst-class
classref-introduction-group
:::

## Description

A node that provides a polygon shape to a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} parent and allows to edit it. The polygon can be concave or
convex. This can give a detection shape to an
`Area2D<class_Area2D>`{.interpreted-text role="ref"}, turn
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} into
a solid object, or give a hollow shape to a
`StaticBody2D<class_StaticBody2D>`{.interpreted-text role="ref"}.

\*\*Warning:\*\* A non-uniformly scaled **CollisionPolygon2D** will
likely not behave as expected. Make sure to keep its scale the same on
all axes and adjust its polygon instead.

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

:::: {#enum_CollisionPolygon2D_BuildMode}
::: rst-class
classref-enumeration
:::
::::

enum **BuildMode**:
`🔗<enum_CollisionPolygon2D_BuildMode>`{.interpreted-text role="ref"}

:::: {#class_CollisionPolygon2D_constant_BUILD_SOLIDS}
::: rst-class
classref-enumeration-constant
:::
::::

`BuildMode<enum_CollisionPolygon2D_BuildMode>`{.interpreted-text
role="ref"} **BUILD_SOLIDS** = `0`

Collisions will include the polygon and its contained area. In this mode
the node has the same effect as several
`ConvexPolygonShape2D<class_ConvexPolygonShape2D>`{.interpreted-text
role="ref"} nodes, one for each convex shape in the convex decomposition
of the polygon (but without the overhead of multiple nodes).

:::: {#class_CollisionPolygon2D_constant_BUILD_SEGMENTS}
::: rst-class
classref-enumeration-constant
:::
::::

`BuildMode<enum_CollisionPolygon2D_BuildMode>`{.interpreted-text
role="ref"} **BUILD_SEGMENTS** = `1`

Collisions will only include the polygon edges. In this mode the node
has the same effect as a single
`ConcavePolygonShape2D<class_ConcavePolygonShape2D>`{.interpreted-text
role="ref"} made of segments, with the restriction that each segment
(after the first one) starts where the previous one ends, and the last
one ends where the first one starts (forming a closed but hollow
polygon).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CollisionPolygon2D_property_build_mode}
::: rst-class
classref-property
:::
::::

`BuildMode<enum_CollisionPolygon2D_BuildMode>`{.interpreted-text
role="ref"} **build_mode** = `0`
`🔗<class_CollisionPolygon2D_property_build_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_build_mode**(value:
  `BuildMode<enum_CollisionPolygon2D_BuildMode>`{.interpreted-text
  role="ref"})
- `BuildMode<enum_CollisionPolygon2D_BuildMode>`{.interpreted-text
  role="ref"} **get_build_mode**()

Collision build mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon2D_property_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disabled** = `false`
`🔗<class_CollisionPolygon2D_property_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_disabled**()

If `true`, no collisions will be detected. This property should be
changed with
`Object.set_deferred()<class_Object_method_set_deferred>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon2D_property_one_way_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **one_way_collision** =
`false`
`🔗<class_CollisionPolygon2D_property_one_way_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_way_collision**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_one_way_collision_enabled**()

If `true`, only edges that face up, relative to
**CollisionPolygon2D**\'s rotation, will collide with other objects.

\*\*Note:\*\* This property has no effect if this **CollisionPolygon2D**
is a child of an `Area2D<class_Area2D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon2D_property_one_way_collision_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**one_way_collision_margin** = `1.0`
`🔗<class_CollisionPolygon2D_property_one_way_collision_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_way_collision_margin**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_one_way_collision_margin**()

The margin used for one-way collision (in pixels). Higher values will
make the shape thicker, and work better for colliders that enter the
polygon at a high velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon2D_property_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array()`
`🔗<class_CollisionPolygon2D_property_polygon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

The polygon\'s list of vertices. Each point will be connected to the
next, and the final point will be connected to the first.

\*\*Note:\*\* The returned vertices are in the local coordinate space of
the given **CollisionPolygon2D**.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.
