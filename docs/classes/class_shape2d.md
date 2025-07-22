github_url
:   hide

# Shape2D {#class_Shape2D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CapsuleShape2D<class_CapsuleShape2D>`{.interpreted-text role="ref"},
`CircleShape2D<class_CircleShape2D>`{.interpreted-text role="ref"},
`ConcavePolygonShape2D<class_ConcavePolygonShape2D>`{.interpreted-text
role="ref"},
`ConvexPolygonShape2D<class_ConvexPolygonShape2D>`{.interpreted-text
role="ref"},
`RectangleShape2D<class_RectangleShape2D>`{.interpreted-text
role="ref"}, `SegmentShape2D<class_SegmentShape2D>`{.interpreted-text
role="ref"},
`SeparationRayShape2D<class_SeparationRayShape2D>`{.interpreted-text
role="ref"},
`WorldBoundaryShape2D<class_WorldBoundaryShape2D>`{.interpreted-text
role="ref"}

Abstract base class for 2D shapes used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for all 2D shapes, intended for use in physics.

\*\*Performance:\*\* Primitive shapes, especially
`CircleShape2D<class_CircleShape2D>`{.interpreted-text role="ref"}, are
fast to check collisions against.
`ConvexPolygonShape2D<class_ConvexPolygonShape2D>`{.interpreted-text
role="ref"} is slower, and
`ConcavePolygonShape2D<class_ConcavePolygonShape2D>`{.interpreted-text
role="ref"} is the slowest.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}

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

:::: {#class_Shape2D_property_custom_solver_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**custom_solver_bias** = `0.0`
`🔗<class_Shape2D_property_custom_solver_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_solver_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_custom_solver_bias**()

The shape\'s custom solver bias. Defines how much bodies react to
enforce contact separation when this shape is involved.

When set to `0`, the default value from
`ProjectSettings.physics/2d/solver/default_contact_bias<class_ProjectSettings_property_physics/2d/solver/default_contact_bias>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Shape2D_method_collide}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**collide**(local_xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
with_shape: `Shape2D<class_Shape2D>`{.interpreted-text role="ref"},
shape_xform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}) `🔗<class_Shape2D_method_collide>`{.interpreted-text
role="ref"}

Returns `true` if this shape is colliding with another.

This method needs the transformation matrix for this shape
(`local_xform`), the shape to check collisions with (`with_shape`), and
the transformation matrix of that shape (`shape_xform`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shape2D_method_collide_and_get_contacts}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **collide_and_get_contacts**(local_xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
with_shape: `Shape2D<class_Shape2D>`{.interpreted-text role="ref"},
shape_xform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`🔗<class_Shape2D_method_collide_and_get_contacts>`{.interpreted-text
role="ref"}

Returns a list of contact point pairs where this shape touches another.

If there are no collisions, the returned list is empty. Otherwise, the
returned list contains contact points arranged in pairs, with entries
alternating between points on the boundary of this shape and points on
the boundary of `with_shape`.

A collision pair A, B can be used to calculate the collision normal with
`(B - A).normalized()`, and the collision depth with `(B - A).length()`.
This information is typically used to separate shapes, particularly in
collision solvers.

This method needs the transformation matrix for this shape
(`local_xform`), the shape to check collisions with (`with_shape`), and
the transformation matrix of that shape (`shape_xform`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shape2D_method_collide_with_motion}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**collide_with_motion**(local_xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
local_motion: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
with_shape: `Shape2D<class_Shape2D>`{.interpreted-text role="ref"},
shape_xform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, shape_motion: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_Shape2D_method_collide_with_motion>`{.interpreted-text
role="ref"}

Returns whether this shape would collide with another, if a given
movement was applied.

This method needs the transformation matrix for this shape
(`local_xform`), the movement to test on this shape (`local_motion`),
the shape to check collisions with (`with_shape`), the transformation
matrix of that shape (`shape_xform`), and the movement to test onto the
other object (`shape_motion`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shape2D_method_collide_with_motion_and_get_contacts}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **collide_with_motion_and_get_contacts**(local_xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
local_motion: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
with_shape: `Shape2D<class_Shape2D>`{.interpreted-text role="ref"},
shape_xform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, shape_motion: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_Shape2D_method_collide_with_motion_and_get_contacts>`{.interpreted-text
role="ref"}

Returns a list of contact point pairs where this shape would touch
another, if a given movement was applied.

If there would be no collisions, the returned list is empty. Otherwise,
the returned list contains contact points arranged in pairs, with
entries alternating between points on the boundary of this shape and
points on the boundary of `with_shape`.

A collision pair A, B can be used to calculate the collision normal with
`(B - A).normalized()`, and the collision depth with `(B - A).length()`.
This information is typically used to separate shapes, particularly in
collision solvers.

This method needs the transformation matrix for this shape
(`local_xform`), the movement to test on this shape (`local_motion`),
the shape to check collisions with (`with_shape`), the transformation
matrix of that shape (`shape_xform`), and the movement to test onto the
other object (`shape_motion`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shape2D_method_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw**(canvas_item: `RID<class_RID>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Shape2D_method_draw>`{.interpreted-text role="ref"}

Draws a solid shape onto a
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} with the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
API filled with the specified `color`. The exact drawing method is
specific for each shape and cannot be configured.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shape2D_method_get_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Shape2D_method_get_rect>`{.interpreted-text
role="ref"}

Returns a `Rect2<class_Rect2>`{.interpreted-text role="ref"}
representing the shapes boundary.
