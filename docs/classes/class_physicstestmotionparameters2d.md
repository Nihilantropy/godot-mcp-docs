github_url
:   hide

# PhysicsTestMotionParameters2D {#class_PhysicsTestMotionParameters2D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides parameters for
`PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

By changing various properties of this object, such as the motion, you
can configure the parameters for
`PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>`{.interpreted-text
role="ref"}.

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

:::: {#class_PhysicsTestMotionParameters2D_property_collide_separation_ray}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**collide_separation_ray** = `false`
`🔗<class_PhysicsTestMotionParameters2D_property_collide_separation_ray>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_separation_ray_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_separation_ray_enabled**()

If set to `true`, shapes of type
`PhysicsServer2D.SHAPE_SEPARATION_RAY<class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY>`{.interpreted-text
role="ref"} are used to detect collisions and can stop the motion. Can
be useful when snapping to the ground.

If set to `false`, shapes of type
`PhysicsServer2D.SHAPE_SEPARATION_RAY<class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY>`{.interpreted-text
role="ref"} are only used for separation when overlapping with other
bodies. That\'s the main use for separation ray shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionParameters2D_property_exclude_bodies}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**exclude_bodies** = `[]`
`🔗<class_PhysicsTestMotionParameters2D_property_exclude_bodies>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclude_bodies**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
  **get_exclude_bodies**()

Optional array of body `RID<class_RID>`{.interpreted-text role="ref"} to
exclude from collision. Use
`CollisionObject2D.get_rid()<class_CollisionObject2D_method_get_rid>`{.interpreted-text
role="ref"} to get the `RID<class_RID>`{.interpreted-text role="ref"}
associated with a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}-derived node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionParameters2D_property_exclude_objects}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
**exclude_objects** = `[]`
`🔗<class_PhysicsTestMotionParameters2D_property_exclude_objects>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclude_objects**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
  **get_exclude_objects**()

Optional array of object unique instance ID to exclude from collision.
See
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionParameters2D_property_from}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} **from**
= `Transform2D(1, 0, 0, 1, 0, 0)`
`🔗<class_PhysicsTestMotionParameters2D_property_from>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_from**(value: `Transform2D<class_Transform2D>`{.interpreted-text
  role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_from**()

Transform in global space where the motion should start. Usually set to
`Node2D.global_transform<class_Node2D_property_global_transform>`{.interpreted-text
role="ref"} for the current body\'s transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionParameters2D_property_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.08`
`🔗<class_PhysicsTestMotionParameters2D_property_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

Increases the size of the shapes involved in the collision detection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionParameters2D_property_motion}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **motion** =
`Vector2(0, 0)`
`🔗<class_PhysicsTestMotionParameters2D_property_motion>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_motion**()

Motion vector to define the length and direction of the motion to test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsTestMotionParameters2D_property_recovery_as_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**recovery_as_collision** = `false`
`🔗<class_PhysicsTestMotionParameters2D_property_recovery_as_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_recovery_as_collision_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_recovery_as_collision_enabled**()

If set to `true`, any depenetration from the recovery phase is reported
as a collision; this is used e.g. by
`CharacterBody2D<class_CharacterBody2D>`{.interpreted-text role="ref"}
for improving floor detection during floor snapping.

If set to `false`, only collisions resulting from the motion are
reported, which is generally the desired behavior.
