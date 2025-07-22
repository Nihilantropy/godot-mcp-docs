github_url
:   hide

::: {.meta keywords="ragdoll"}
:::

# PhysicalBone3D {#class_PhysicalBone3D}

**Inherits:** `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} **\<**
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics body used to make bones in a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} react to
physics.

::: rst-class
classref-introduction-group
:::

## Description

The **PhysicalBone3D** node is a physics body that can be used to make
bones in a `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
react to physics.

\*\*Note:\*\* In order to detect physical bones with raycasts, the
`SkeletonModifier3D.active<class_SkeletonModifier3D_property_active>`{.interpreted-text
role="ref"} property of the parent
`PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>`{.interpreted-text
role="ref"} must be `true` and the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}\'s bone
must be assigned to **PhysicalBone3D** correctly; it means that
`get_bone_id()<class_PhysicalBone3D_method_get_bone_id>`{.interpreted-text
role="ref"} should return a valid id (`>= 0`).

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

## Enumerations

:::: {#enum_PhysicalBone3D_DampMode}
::: rst-class
classref-enumeration
:::
::::

enum **DampMode**: `🔗<enum_PhysicalBone3D_DampMode>`{.interpreted-text
role="ref"}

:::: {#class_PhysicalBone3D_constant_DAMP_MODE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text role="ref"}
**DAMP_MODE_COMBINE** = `0`

In this mode, the body\'s damping value is added to any value set in
areas or the default value.

:::: {#class_PhysicalBone3D_constant_DAMP_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text role="ref"}
**DAMP_MODE_REPLACE** = `1`

In this mode, the body\'s damping value replaces any value set in areas
or the default value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicalBone3D_JointType}
::: rst-class
classref-enumeration
:::
::::

enum **JointType**:
`🔗<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}

:::: {#class_PhysicalBone3D_constant_JOINT_TYPE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**JOINT_TYPE_NONE** = `0`

No joint is applied to the PhysicsBone3D.

:::: {#class_PhysicalBone3D_constant_JOINT_TYPE_PIN}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**JOINT_TYPE_PIN** = `1`

A pin joint is applied to the PhysicsBone3D.

:::: {#class_PhysicalBone3D_constant_JOINT_TYPE_CONE}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**JOINT_TYPE_CONE** = `2`

A cone joint is applied to the PhysicsBone3D.

:::: {#class_PhysicalBone3D_constant_JOINT_TYPE_HINGE}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**JOINT_TYPE_HINGE** = `3`

A hinge joint is applied to the PhysicsBone3D.

:::: {#class_PhysicalBone3D_constant_JOINT_TYPE_SLIDER}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**JOINT_TYPE_SLIDER** = `4`

A slider joint is applied to the PhysicsBone3D.

:::: {#class_PhysicalBone3D_constant_JOINT_TYPE_6DOF}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**JOINT_TYPE_6DOF** = `5`

A 6 degrees of freedom joint is applied to the PhysicsBone3D.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PhysicalBone3D_property_angular_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angular_damp** =
`0.0` `🔗<class_PhysicalBone3D_property_angular_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_damp**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_angular_damp**()

Damps the body\'s rotation. By default, the body will use the
`ProjectSettings.physics/3d/default_angular_damp<class_ProjectSettings_property_physics/3d/default_angular_damp>`{.interpreted-text
role="ref"} project setting or any value override set by an
`Area3D<class_Area3D>`{.interpreted-text role="ref"} the body is in.
Depending on
`angular_damp_mode<class_PhysicalBone3D_property_angular_damp_mode>`{.interpreted-text
role="ref"}, you can set
`angular_damp<class_PhysicalBone3D_property_angular_damp>`{.interpreted-text
role="ref"} to be added to or to replace the body\'s damping value.

See
`ProjectSettings.physics/3d/default_angular_damp<class_ProjectSettings_property_physics/3d/default_angular_damp>`{.interpreted-text
role="ref"} for more details about damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_angular_damp_mode}
::: rst-class
classref-property
:::
::::

`DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text role="ref"}
**angular_damp_mode** = `0`
`🔗<class_PhysicalBone3D_property_angular_damp_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_damp_mode**(value:
  `DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text
  role="ref"})
- `DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text role="ref"}
  **get_angular_damp_mode**()

Defines how
`angular_damp<class_PhysicalBone3D_property_angular_damp>`{.interpreted-text
role="ref"} is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_angular_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**angular_velocity** = `Vector3(0, 0, 0)`
`🔗<class_PhysicalBone3D_property_angular_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_angular_velocity**()

The PhysicalBone3D\'s rotational velocity in *radians* per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_body_offset}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**body_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_PhysicalBone3D_property_body_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_body_offset**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_body_offset**()

Sets the body\'s transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_bounce}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bounce** = `0.0`
`🔗<class_PhysicalBone3D_property_bounce>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bounce**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bounce**()

The body\'s bounciness. Values range from `0` (no bounce) to `1` (full
bounciness).

\*\*Note:\*\* Even with
`bounce<class_PhysicalBone3D_property_bounce>`{.interpreted-text
role="ref"} set to `1.0`, some energy will be lost over time due to
linear and angular damping. To have a **PhysicalBone3D** that preserves
all its energy over time, set
`bounce<class_PhysicalBone3D_property_bounce>`{.interpreted-text
role="ref"} to `1.0`,
`linear_damp_mode<class_PhysicalBone3D_property_linear_damp_mode>`{.interpreted-text
role="ref"} to
`DAMP_MODE_REPLACE<class_PhysicalBone3D_constant_DAMP_MODE_REPLACE>`{.interpreted-text
role="ref"},
`linear_damp<class_PhysicalBone3D_property_linear_damp>`{.interpreted-text
role="ref"} to `0.0`,
`angular_damp_mode<class_PhysicalBone3D_property_angular_damp_mode>`{.interpreted-text
role="ref"} to
`DAMP_MODE_REPLACE<class_PhysicalBone3D_constant_DAMP_MODE_REPLACE>`{.interpreted-text
role="ref"}, and
`angular_damp<class_PhysicalBone3D_property_angular_damp>`{.interpreted-text
role="ref"} to `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_can_sleep}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_sleep** = `true`
`🔗<class_PhysicalBone3D_property_can_sleep>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_can_sleep**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_able_to_sleep**()

If `true`, the body is deactivated when there is no movement, so it will
not take part in the simulation until it is awakened by an external
force.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_custom_integrator}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **custom_integrator** =
`false`
`🔗<class_PhysicalBone3D_property_custom_integrator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_custom_integrator**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_custom_integrator**()

If `true`, the standard force integration (like gravity or damping) will
be disabled for this body. Other than collision response, the body will
only move as determined by the
`_integrate_forces()<class_PhysicalBone3D_private_method__integrate_forces>`{.interpreted-text
role="ref"} method, if that virtual method is overridden.

Setting this property will call the method
`PhysicsServer3D.body_set_omit_force_integration()<class_PhysicsServer3D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"} internally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_friction}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **friction** = `1.0`
`🔗<class_PhysicalBone3D_property_friction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_friction**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_friction**()

The body\'s friction, from `0` (frictionless) to `1` (max friction).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_gravity_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **gravity_scale** =
`1.0`
`🔗<class_PhysicalBone3D_property_gravity_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_gravity_scale**()

This is multiplied by
`ProjectSettings.physics/3d/default_gravity<class_ProjectSettings_property_physics/3d/default_gravity>`{.interpreted-text
role="ref"} to produce this body\'s gravity. For example, a value of
`1.0` will apply normal gravity, `2.0` will apply double the gravity,
and `0.5` will apply half the gravity to this body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_joint_offset}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**joint_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_PhysicalBone3D_property_joint_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_joint_offset**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_joint_offset**()

Sets the joint\'s transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_joint_rotation}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**joint_rotation** = `Vector3(0, 0, 0)`
`🔗<class_PhysicalBone3D_property_joint_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_joint_rotation**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_joint_rotation**()

Sets the joint\'s rotation in radians.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_joint_type}
::: rst-class
classref-property
:::
::::

`JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text role="ref"}
**joint_type** = `0`
`🔗<class_PhysicalBone3D_property_joint_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_joint_type**(value:
  `JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text
  role="ref"})
- `JointType<enum_PhysicalBone3D_JointType>`{.interpreted-text
  role="ref"} **get_joint_type**()

Sets the joint type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_linear_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_damp** =
`0.0` `🔗<class_PhysicalBone3D_property_linear_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_damp**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_linear_damp**()

Damps the body\'s movement. By default, the body will use
`ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>`{.interpreted-text
role="ref"} or any value override set by an
`Area3D<class_Area3D>`{.interpreted-text role="ref"} the body is in.
Depending on
`linear_damp_mode<class_PhysicalBone3D_property_linear_damp_mode>`{.interpreted-text
role="ref"},
`linear_damp<class_PhysicalBone3D_property_linear_damp>`{.interpreted-text
role="ref"} may be added to or replace the body\'s damping value.

See
`ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>`{.interpreted-text
role="ref"} for more details about damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_linear_damp_mode}
::: rst-class
classref-property
:::
::::

`DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text role="ref"}
**linear_damp_mode** = `0`
`🔗<class_PhysicalBone3D_property_linear_damp_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_damp_mode**(value:
  `DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text
  role="ref"})
- `DampMode<enum_PhysicalBone3D_DampMode>`{.interpreted-text role="ref"}
  **get_linear_damp_mode**()

Defines how
`linear_damp<class_PhysicalBone3D_property_linear_damp>`{.interpreted-text
role="ref"} is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_linear_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**linear_velocity** = `Vector3(0, 0, 0)`
`🔗<class_PhysicalBone3D_property_linear_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_linear_velocity**()

The body\'s linear velocity in units per second. Can be used
sporadically, but **don\'t set this every frame**, because physics may
run in another thread and runs at a different granularity. Use
`_integrate_forces()<class_PhysicalBone3D_private_method__integrate_forces>`{.interpreted-text
role="ref"} as your process loop for precise control of the body state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_property_mass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mass** = `1.0`
`🔗<class_PhysicalBone3D_property_mass>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mass**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_mass**()

The body\'s mass.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicalBone3D_private_method__integrate_forces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_integrate_forces**(state:
`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicalBone3D_private_method__integrate_forces>`{.interpreted-text
role="ref"}

Called during physics processing, allowing you to read and safely modify
the simulation state for the object. By default, it is called before the
standard force integration, but the
`custom_integrator<class_PhysicalBone3D_property_custom_integrator>`{.interpreted-text
role="ref"} property allows you to disable the standard force
integration and do fully custom force integration for a body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_method_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_impulse**(impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicalBone3D_method_apply_central_impulse>`{.interpreted-text
role="ref"}

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_integrate_forces\"
functions otherwise).

This is equivalent to using
`apply_impulse()<class_PhysicalBone3D_method_apply_impulse>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_method_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_impulse**(impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicalBone3D_method_apply_impulse>`{.interpreted-text
role="ref"}

Applies a positioned impulse to the PhysicsBone3D.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_integrate_forces\"
functions otherwise).

`position` is the offset from the PhysicsBone3D origin in global
coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_method_get_bone_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_bone_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicalBone3D_method_get_bone_id>`{.interpreted-text
role="ref"}

Returns the unique identifier of the PhysicsBone3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_method_get_simulate_physics}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_simulate_physics**()
`🔗<class_PhysicalBone3D_method_get_simulate_physics>`{.interpreted-text
role="ref"}

Returns `true` if the PhysicsBone3D is allowed to simulate physics.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone3D_method_is_simulating_physics}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_simulating_physics**()
`🔗<class_PhysicalBone3D_method_is_simulating_physics>`{.interpreted-text
role="ref"}

Returns `true` if the PhysicsBone3D is currently simulating physics.
