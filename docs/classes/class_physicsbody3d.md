github_url
:   hide

# PhysicsBody3D {#class_PhysicsBody3D}

**Inherits:**
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"},
`PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text role="ref"},
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"},
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"}

Abstract base class for 3D game objects affected by physics.

::: rst-class
classref-introduction-group
:::

## Description

**PhysicsBody3D** is an abstract base class for 3D game objects affected
by physics. All 3D physics bodies inherit from it.

\*\*Warning:\*\* With a non-uniform scale, this node will likely not
behave as expected. It is advised to keep its scale the same on all axes
and adjust its collision shape(s) instead.

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

:::: {#class_PhysicsBody3D_property_axis_lock_angular_x}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **axis_lock_angular_x**
= `false`
`🔗<class_PhysicsBody3D_property_axis_lock_angular_x>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"}, lock: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Lock the body\'s rotation in the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_property_axis_lock_angular_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **axis_lock_angular_y**
= `false`
`🔗<class_PhysicsBody3D_property_axis_lock_angular_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"}, lock: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Lock the body\'s rotation in the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_property_axis_lock_angular_z}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **axis_lock_angular_z**
= `false`
`🔗<class_PhysicsBody3D_property_axis_lock_angular_z>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"}, lock: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Lock the body\'s rotation in the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_property_axis_lock_linear_x}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **axis_lock_linear_x**
= `false`
`🔗<class_PhysicsBody3D_property_axis_lock_linear_x>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"}, lock: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Lock the body\'s linear movement in the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_property_axis_lock_linear_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **axis_lock_linear_y**
= `false`
`🔗<class_PhysicsBody3D_property_axis_lock_linear_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"}, lock: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Lock the body\'s linear movement in the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_property_axis_lock_linear_z}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **axis_lock_linear_z**
= `false`
`🔗<class_PhysicsBody3D_property_axis_lock_linear_z>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"}, lock: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_axis_lock**(axis:
  `BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Lock the body\'s linear movement in the Z axis.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicsBody3D_method_add_collision_exception_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_collision_exception_with**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_PhysicsBody3D_method_add_collision_exception_with>`{.interpreted-text
role="ref"}

Adds a body to the list of bodies that this body can\'t collide with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_get_axis_lock}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_axis_lock**(axis:
`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsBody3D_method_get_axis_lock>`{.interpreted-text
role="ref"}

Returns `true` if the specified linear or rotational `axis` is locked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_get_collision_exceptions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"}\] **get_collision_exceptions**()
`🔗<class_PhysicsBody3D_method_get_collision_exceptions>`{.interpreted-text
role="ref"}

Returns an array of nodes that were added as collision exceptions for
this body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_get_gravity}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_gravity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsBody3D_method_get_gravity>`{.interpreted-text
role="ref"}

Returns the gravity vector computed from all sources that can affect the
body, including all gravity overrides from
`Area3D<class_Area3D>`{.interpreted-text role="ref"} nodes and the
global world gravity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_move_and_collide}
::: rst-class
classref-method
:::
::::

`KinematicCollision3D<class_KinematicCollision3D>`{.interpreted-text
role="ref"} **move_and_collide**(motion:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, test_only:
`bool<class_bool>`{.interpreted-text role="ref"} = false, safe_margin:
`float<class_float>`{.interpreted-text role="ref"} = 0.001,
recovery_as_collision: `bool<class_bool>`{.interpreted-text role="ref"}
= false, max_collisions: `int<class_int>`{.interpreted-text role="ref"}
= 1) `🔗<class_PhysicsBody3D_method_move_and_collide>`{.interpreted-text
role="ref"}

Moves the body along the vector `motion`. In order to be frame rate
independent in
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} or
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, `motion` should be computed using `delta`.

The body will stop if it collides. Returns a
`KinematicCollision3D<class_KinematicCollision3D>`{.interpreted-text
role="ref"}, which contains information about the collision when
stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be
collision information is given.

`safe_margin` is the extra margin used for collision recovery (see
`CharacterBody3D.safe_margin<class_CharacterBody3D_property_safe_margin>`{.interpreted-text
role="ref"} for more details).

If `recovery_as_collision` is `true`, any depenetration from the
recovery phase is also reported as a collision; this is used e.g. by
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"}
for improving floor detection during floor snapping.

`max_collisions` allows to retrieve more than one collision result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_remove_collision_exception_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_collision_exception_with**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_PhysicsBody3D_method_remove_collision_exception_with>`{.interpreted-text
role="ref"}

Removes a body from the list of bodies that this body can\'t collide
with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_set_axis_lock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_lock**(axis:
`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"},
lock: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsBody3D_method_set_axis_lock>`{.interpreted-text
role="ref"}

Locks or unlocks the specified linear or rotational `axis` depending on
the value of `lock`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsBody3D_method_test_move}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **test_move**(from:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}, motion:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, collision:
`KinematicCollision3D<class_KinematicCollision3D>`{.interpreted-text
role="ref"} = null, safe_margin: `float<class_float>`{.interpreted-text
role="ref"} = 0.001, recovery_as_collision:
`bool<class_bool>`{.interpreted-text role="ref"} = false,
max_collisions: `int<class_int>`{.interpreted-text role="ref"} = 1)
`🔗<class_PhysicsBody3D_method_test_move>`{.interpreted-text role="ref"}

Checks for collisions without moving the body. In order to be frame rate
independent in
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} or
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, `motion` should be computed using `delta`.

Virtually sets the node\'s position, scale and rotation to that of the
given `Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
then tries to move the body along the vector `motion`. Returns `true` if
a collision would stop the body from moving along the whole path.

`collision` is an optional object of type
`KinematicCollision3D<class_KinematicCollision3D>`{.interpreted-text
role="ref"}, which contains additional information about the collision
when stopped, or when touching another body along the motion.

`safe_margin` is the extra margin used for collision recovery (see
`CharacterBody3D.safe_margin<class_CharacterBody3D_property_safe_margin>`{.interpreted-text
role="ref"} for more details).

If `recovery_as_collision` is `true`, any depenetration from the
recovery phase is also reported as a collision; this is useful for
checking whether the body would *touch* any other bodies.

`max_collisions` allows to retrieve more than one collision result.
