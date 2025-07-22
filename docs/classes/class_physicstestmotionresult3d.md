github_url
:   hide

# PhysicsTestMotionResult3D {#class_PhysicsTestMotionResult3D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Describes the motion and collision result from
`PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Describes the motion and collision result from
`PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>`{.interpreted-text
role="ref"}.

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

:::: {#class_PhysicsTestMotionResult3D_method_get_collider}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_collider**(collision_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collider>`{.interpreted-text
role="ref"}

Returns the colliding body\'s attached
`Object<class_Object>`{.interpreted-text role="ref"} given a collision
index (the deepest collision by default), if a collision occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collider_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collider_id**(collision_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collider_id>`{.interpreted-text
role="ref"}

Returns the unique instance ID of the colliding body\'s attached
`Object<class_Object>`{.interpreted-text role="ref"} given a collision
index (the deepest collision by default), if a collision occurred. See
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collider_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_collider_rid**(collision_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collider_rid>`{.interpreted-text
role="ref"}

Returns the colliding body\'s `RID<class_RID>`{.interpreted-text
role="ref"} used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
given a collision index (the deepest collision by default), if a
collision occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collider_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collider_shape**(collision_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collider_shape>`{.interpreted-text
role="ref"}

Returns the colliding body\'s shape index given a collision index (the
deepest collision by default), if a collision occurred. See
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collider_velocity}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_collider_velocity**(collision_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collider_velocity>`{.interpreted-text
role="ref"}

Returns the colliding body\'s velocity given a collision index (the
deepest collision by default), if a collision occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_collision_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_count>`{.interpreted-text
role="ref"}

Returns the number of detected collisions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_depth}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_collision_depth**(collision_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_depth>`{.interpreted-text
role="ref"}

Returns the length of overlap along the collision normal given a
collision index (the deepest collision by default), if a collision
occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_local_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collision_local_shape**(collision_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_local_shape>`{.interpreted-text
role="ref"}

Returns the moving object\'s colliding shape given a collision index
(the deepest collision by default), if a collision occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_collision_normal**(collision_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_normal>`{.interpreted-text
role="ref"}

Returns the colliding body\'s shape\'s normal at the point of collision
given a collision index (the deepest collision by default), if a
collision occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_point}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_collision_point**(collision_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_point>`{.interpreted-text
role="ref"}

Returns the point of collision in global coordinates given a collision
index (the deepest collision by default), if a collision occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_collision_safe_fraction**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction>`{.interpreted-text
role="ref"}

Returns the maximum fraction of the motion that can occur without a
collision, between `0` and `1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_collision_unsafe_fraction**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction>`{.interpreted-text
role="ref"}

Returns the minimum fraction of the motion needed to collide, if a
collision occurred, between `0` and `1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_remainder}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_remainder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_remainder>`{.interpreted-text
role="ref"}

Returns the moving object\'s remaining movement vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionResult3D_method_get_travel}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_travel**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsTestMotionResult3D_method_get_travel>`{.interpreted-text
role="ref"}

Returns the moving object\'s travel before collision.
