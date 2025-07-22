github_url
:   hide

# PhysicsBody2D {#class_PhysicsBody2D}

**Inherits:**
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} **\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CharacterBody2D<class_CharacterBody2D>`{.interpreted-text role="ref"},
`RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"},
`StaticBody2D<class_StaticBody2D>`{.interpreted-text role="ref"}

Abstract base class for 2D game objects affected by physics.

::: rst-class
classref-introduction-group
:::

## Description

**PhysicsBody2D** is an abstract base class for 2D game objects affected
by physics. All 2D physics bodies inherit from it.

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

## Method Descriptions

:::: {#class_PhysicsBody2D_method_add_collision_exception_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_collision_exception_with**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_PhysicsBody2D_method_add_collision_exception_with>`{.interpreted-text
role="ref"}

Adds a body to the list of bodies that this body can\'t collide with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody2D_method_get_collision_exceptions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text
role="ref"}\] **get_collision_exceptions**()
`🔗<class_PhysicsBody2D_method_get_collision_exceptions>`{.interpreted-text
role="ref"}

Returns an array of nodes that were added as collision exceptions for
this body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody2D_method_get_gravity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_gravity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsBody2D_method_get_gravity>`{.interpreted-text
role="ref"}

Returns the gravity vector computed from all sources that can affect the
body, including all gravity overrides from
`Area2D<class_Area2D>`{.interpreted-text role="ref"} nodes and the
global world gravity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody2D_method_move_and_collide}
::: rst-class
classref-method
:::
::::

`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"} **move_and_collide**(motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, test_only:
`bool<class_bool>`{.interpreted-text role="ref"} = false, safe_margin:
`float<class_float>`{.interpreted-text role="ref"} = 0.08,
recovery_as_collision: `bool<class_bool>`{.interpreted-text role="ref"}
= false)
`🔗<class_PhysicsBody2D_method_move_and_collide>`{.interpreted-text
role="ref"}

Moves the body along the vector `motion`. In order to be frame rate
independent in
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} or
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, `motion` should be computed using `delta`.

Returns a
`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"}, which contains information about the collision when
stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be
collision information is given.

`safe_margin` is the extra margin used for collision recovery (see
`CharacterBody2D.safe_margin<class_CharacterBody2D_property_safe_margin>`{.interpreted-text
role="ref"} for more details).

If `recovery_as_collision` is `true`, any depenetration from the
recovery phase is also reported as a collision; this is used e.g. by
`CharacterBody2D<class_CharacterBody2D>`{.interpreted-text role="ref"}
for improving floor detection during floor snapping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody2D_method_remove_collision_exception_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_collision_exception_with**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_PhysicsBody2D_method_remove_collision_exception_with>`{.interpreted-text
role="ref"}

Removes a body from the list of bodies that this body can\'t collide
with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody2D_method_test_move}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **test_move**(from:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, collision:
`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"} = null, safe_margin: `float<class_float>`{.interpreted-text
role="ref"} = 0.08, recovery_as_collision:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PhysicsBody2D_method_test_move>`{.interpreted-text role="ref"}

Checks for collisions without moving the body. In order to be frame rate
independent in
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} or
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, `motion` should be computed using `delta`.

Virtually sets the node\'s position, scale and rotation to that of the
given `Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
then tries to move the body along the vector `motion`. Returns `true` if
a collision would stop the body from moving along the whole path.

`collision` is an optional object of type
`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"}, which contains additional information about the collision
when stopped, or when touching another body along the motion.

`safe_margin` is the extra margin used for collision recovery (see
`CharacterBody2D.safe_margin<class_CharacterBody2D_property_safe_margin>`{.interpreted-text
role="ref"} for more details).

If `recovery_as_collision` is `true`, any depenetration from the
recovery phase is also reported as a collision; this is useful for
checking whether the body would *touch* any other bodies.
