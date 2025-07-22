github_url
:   hide

# KinematicCollision2D {#class_KinematicCollision2D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds collision data from the movement of a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Holds collision data from the movement of a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"},
usually from
`PhysicsBody2D.move_and_collide()<class_PhysicsBody2D_method_move_and_collide>`{.interpreted-text
role="ref"}. When a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} is
moved, it stops if it detects a collision with another body. If a
collision is detected, a **KinematicCollision2D** object is returned.

The collision data includes the colliding object, the remaining motion,
and the collision position. This data can be used to determine a custom
response to the collision.

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

:::: {#class_KinematicCollision2D_method_get_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_angle**(up_direction: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, -1))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_angle>`{.interpreted-text
role="ref"}

Returns the collision angle according to `up_direction`, which is
`Vector2.UP<class_Vector2_constant_UP>`{.interpreted-text role="ref"} by
default. This value is always positive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_collider}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"} **get_collider**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_collider>`{.interpreted-text
role="ref"}

Returns the colliding body\'s attached
`Object<class_Object>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_collider_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_collider_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_collider_id>`{.interpreted-text
role="ref"}

Returns the unique instance ID of the colliding body\'s attached
`Object<class_Object>`{.interpreted-text role="ref"}. See
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_collider_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_collider_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_collider_rid>`{.interpreted-text
role="ref"}

Returns the colliding body\'s `RID<class_RID>`{.interpreted-text
role="ref"} used by the
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_collider_shape}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_collider_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_collider_shape>`{.interpreted-text
role="ref"}

Returns the colliding body\'s shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_collider_shape_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collider_shape_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_collider_shape_index>`{.interpreted-text
role="ref"}

Returns the colliding body\'s shape index. See
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_collider_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_collider_velocity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_collider_velocity>`{.interpreted-text
role="ref"}

Returns the colliding body\'s velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_depth}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_depth**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_depth>`{.interpreted-text
role="ref"}

Returns the colliding body\'s length of overlap along the collision
normal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_local_shape}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_local_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_local_shape>`{.interpreted-text
role="ref"}

Returns the moving object\'s colliding shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_normal}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_normal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_normal>`{.interpreted-text
role="ref"}

Returns the colliding body\'s shape\'s normal at the point of collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_position>`{.interpreted-text
role="ref"}

Returns the point of collision in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_remainder}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_remainder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_remainder>`{.interpreted-text
role="ref"}

Returns the moving object\'s remaining movement vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_KinematicCollision2D_method_get_travel}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_travel**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_KinematicCollision2D_method_get_travel>`{.interpreted-text
role="ref"}

Returns the moving object\'s travel before collision.
