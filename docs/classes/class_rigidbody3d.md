github_url
:   hide

# RigidBody3D {#class_RigidBody3D}

**Inherits:** `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} **\<**
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `VehicleBody3D<class_VehicleBody3D>`{.interpreted-text
role="ref"}

A 3D physics body that is moved by a physics simulation.

::: rst-class
classref-introduction-group
:::

## Description

**RigidBody3D** implements full 3D physics. It cannot be controlled
directly, instead, you must apply forces to it (gravity, impulses,
etc.), and the physics simulation will calculate the resulting movement,
rotation, react to collisions, and affect other physics bodies in its
path.

The body\'s behavior can be adjusted via
`lock_rotation<class_RigidBody3D_property_lock_rotation>`{.interpreted-text
role="ref"},
`freeze<class_RigidBody3D_property_freeze>`{.interpreted-text
role="ref"}, and
`freeze_mode<class_RigidBody3D_property_freeze_mode>`{.interpreted-text
role="ref"}. By changing various properties of the object, such as
`mass<class_RigidBody3D_property_mass>`{.interpreted-text role="ref"},
you can control how the physics simulation acts on it.

A rigid body will always maintain its shape and size, even when forces
are applied to it. It is useful for objects that can be interacted with
in an environment, such as a tree that can be knocked over or a stack of
crates that can be pushed around.

If you need to directly affect the body, prefer
`_integrate_forces()<class_RigidBody3D_private_method__integrate_forces>`{.interpreted-text
role="ref"} as it allows you to directly access the physics state.

If you need to override the default physics behavior, you can write a
custom force integration function. See
`custom_integrator<class_RigidBody3D_property_custom_integrator>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Changing the 3D transform or
`linear_velocity<class_RigidBody3D_property_linear_velocity>`{.interpreted-text
role="ref"} of a **RigidBody3D** very often may lead to some
unpredictable behaviors. This also happens when a **RigidBody3D** is the
descendant of a constantly moving node, like another **RigidBody3D**, as
that will cause its global transform to be set whenever its ancestor
moves.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}
- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)
- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)

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

## Signals

:::: {#class_RigidBody3D_signal_body_entered}
::: rst-class
classref-signal
:::
::::

**body_entered**(body: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_signal_body_entered>`{.interpreted-text
role="ref"}

Emitted when a collision with another
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"} occurs. Requires
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"} to be set to `true` and
`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"} to be set high enough to detect all the collisions.
`GridMap<class_GridMap>`{.interpreted-text role="ref"}s are detected if
the `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"} has
Collision `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s.

`body` the `Node<class_Node>`{.interpreted-text role="ref"}, if it
exists in the tree, of the other
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_signal_body_exited}
::: rst-class
classref-signal
:::
::::

**body_exited**(body: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_signal_body_exited>`{.interpreted-text role="ref"}

Emitted when the collision with another
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"} ends. Requires
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"} to be set to `true` and
`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"} to be set high enough to detect all the collisions.
`GridMap<class_GridMap>`{.interpreted-text role="ref"}s are detected if
the `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"} has
Collision `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s.

`body` the `Node<class_Node>`{.interpreted-text role="ref"}, if it
exists in the tree, of the other
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_signal_body_shape_entered}
::: rst-class
classref-signal
:::
::::

**body_shape_entered**(body_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, body: `Node<class_Node>`{.interpreted-text role="ref"},
body_shape_index: `int<class_int>`{.interpreted-text role="ref"},
local_shape_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_signal_body_shape_entered>`{.interpreted-text
role="ref"}

Emitted when one of this RigidBody3D\'s
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s collides with
another `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} or `GridMap<class_GridMap>`{.interpreted-text role="ref"}\'s
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s. Requires
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"} to be set to `true` and
`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"} to be set high enough to detect all the collisions.
`GridMap<class_GridMap>`{.interpreted-text role="ref"}s are detected if
the `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"} has
Collision `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s.

`body_rid` the `RID<class_RID>`{.interpreted-text role="ref"} of the
other `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
or `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"}\'s
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.

`body` the `Node<class_Node>`{.interpreted-text role="ref"}, if it
exists in the tree, of the other
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"}.

`body_shape_index` the index of the
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} of the other
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"} used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
Get the `CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"} node with
`body.shape_owner_get_owner(body.shape_find_owner(body_shape_index))`.

`local_shape_index` the index of the
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} of this
RigidBody3D used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
Get the `CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"} node with
`self.shape_owner_get_owner(self.shape_find_owner(local_shape_index))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_signal_body_shape_exited}
::: rst-class
classref-signal
:::
::::

**body_shape_exited**(body_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, body: `Node<class_Node>`{.interpreted-text role="ref"},
body_shape_index: `int<class_int>`{.interpreted-text role="ref"},
local_shape_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_signal_body_shape_exited>`{.interpreted-text
role="ref"}

Emitted when the collision between one of this RigidBody3D\'s
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s and another
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"}\'s
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s ends. Requires
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"} to be set to `true` and
`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"} to be set high enough to detect all the collisions.
`GridMap<class_GridMap>`{.interpreted-text role="ref"}s are detected if
the `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"} has
Collision `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s.

`body_rid` the `RID<class_RID>`{.interpreted-text role="ref"} of the
other `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
or `MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"}\'s
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
`GridMap<class_GridMap>`{.interpreted-text role="ref"}s are detected if
the Meshes have `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}s.

`body` the `Node<class_Node>`{.interpreted-text role="ref"}, if it
exists in the tree, of the other
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"}.

`body_shape_index` the index of the
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} of the other
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} or
`GridMap<class_GridMap>`{.interpreted-text role="ref"} used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
Get the `CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"} node with
`body.shape_owner_get_owner(body.shape_find_owner(body_shape_index))`.

`local_shape_index` the index of the
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} of this
RigidBody3D used by the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
Get the `CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"} node with
`self.shape_owner_get_owner(self.shape_find_owner(local_shape_index))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_signal_sleeping_state_changed}
::: rst-class
classref-signal
:::
::::

**sleeping_state_changed**()
`🔗<class_RigidBody3D_signal_sleeping_state_changed>`{.interpreted-text
role="ref"}

Emitted when the physics engine changes the body\'s sleeping state.

\*\*Note:\*\* Changing the value
`sleeping<class_RigidBody3D_property_sleeping>`{.interpreted-text
role="ref"} will not trigger this signal. It is only emitted if the
sleeping state is changed by the physics engine or
`emit_signal("sleeping_state_changed")` is used.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_RigidBody3D_FreezeMode}
::: rst-class
classref-enumeration
:::
::::

enum **FreezeMode**: `🔗<enum_RigidBody3D_FreezeMode>`{.interpreted-text
role="ref"}

:::: {#class_RigidBody3D_constant_FREEZE_MODE_STATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`FreezeMode<enum_RigidBody3D_FreezeMode>`{.interpreted-text role="ref"}
**FREEZE_MODE_STATIC** = `0`

Static body freeze mode (default). The body is not affected by gravity
and forces. It can be only moved by user code and doesn\'t collide with
other bodies along its path.

:::: {#class_RigidBody3D_constant_FREEZE_MODE_KINEMATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`FreezeMode<enum_RigidBody3D_FreezeMode>`{.interpreted-text role="ref"}
**FREEZE_MODE_KINEMATIC** = `1`

Kinematic body freeze mode. Similar to
`FREEZE_MODE_STATIC<class_RigidBody3D_constant_FREEZE_MODE_STATIC>`{.interpreted-text
role="ref"}, but collides with other bodies along its path when moved.
Useful for a frozen body that needs to be animated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RigidBody3D_CenterOfMassMode}
::: rst-class
classref-enumeration
:::
::::

enum **CenterOfMassMode**:
`🔗<enum_RigidBody3D_CenterOfMassMode>`{.interpreted-text role="ref"}

:::: {#class_RigidBody3D_constant_CENTER_OF_MASS_MODE_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`CenterOfMassMode<enum_RigidBody3D_CenterOfMassMode>`{.interpreted-text
role="ref"} **CENTER_OF_MASS_MODE_AUTO** = `0`

In this mode, the body\'s center of mass is calculated automatically
based on its shapes. This assumes that the shapes\' origins are also
their center of mass.

:::: {#class_RigidBody3D_constant_CENTER_OF_MASS_MODE_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`CenterOfMassMode<enum_RigidBody3D_CenterOfMassMode>`{.interpreted-text
role="ref"} **CENTER_OF_MASS_MODE_CUSTOM** = `1`

In this mode, the body\'s center of mass is set through
`center_of_mass<class_RigidBody3D_property_center_of_mass>`{.interpreted-text
role="ref"}. Defaults to the body\'s origin position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RigidBody3D_DampMode}
::: rst-class
classref-enumeration
:::
::::

enum **DampMode**: `🔗<enum_RigidBody3D_DampMode>`{.interpreted-text
role="ref"}

:::: {#class_RigidBody3D_constant_DAMP_MODE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"}
**DAMP_MODE_COMBINE** = `0`

In this mode, the body\'s damping value is added to any value set in
areas or the default value.

:::: {#class_RigidBody3D_constant_DAMP_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"}
**DAMP_MODE_REPLACE** = `1`

In this mode, the body\'s damping value replaces any value set in areas
or the default value.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RigidBody3D_property_angular_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angular_damp** =
`0.0` `🔗<class_RigidBody3D_property_angular_damp>`{.interpreted-text
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
`angular_damp_mode<class_RigidBody3D_property_angular_damp_mode>`{.interpreted-text
role="ref"}, you can set
`angular_damp<class_RigidBody3D_property_angular_damp>`{.interpreted-text
role="ref"} to be added to or to replace the body\'s damping value.

See
`ProjectSettings.physics/3d/default_angular_damp<class_ProjectSettings_property_physics/3d/default_angular_damp>`{.interpreted-text
role="ref"} for more details about damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_angular_damp_mode}
::: rst-class
classref-property
:::
::::

`DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"}
**angular_damp_mode** = `0`
`🔗<class_RigidBody3D_property_angular_damp_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_damp_mode**(value:
  `DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"})
- `DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"}
  **get_angular_damp_mode**()

Defines how
`angular_damp<class_RigidBody3D_property_angular_damp>`{.interpreted-text
role="ref"} is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_angular_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**angular_velocity** = `Vector3(0, 0, 0)`
`🔗<class_RigidBody3D_property_angular_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_angular_velocity**()

The RigidBody3D\'s rotational velocity in *radians* per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_can_sleep}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_sleep** = `true`
`🔗<class_RigidBody3D_property_can_sleep>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_can_sleep**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_able_to_sleep**()

If `true`, the body can enter sleep mode when there is no movement. See
`sleeping<class_RigidBody3D_property_sleeping>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_center_of_mass}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**center_of_mass** = `Vector3(0, 0, 0)`
`🔗<class_RigidBody3D_property_center_of_mass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_of_mass**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_center_of_mass**()

The body\'s custom center of mass, relative to the body\'s origin
position, when
`center_of_mass_mode<class_RigidBody3D_property_center_of_mass_mode>`{.interpreted-text
role="ref"} is set to
`CENTER_OF_MASS_MODE_CUSTOM<class_RigidBody3D_constant_CENTER_OF_MASS_MODE_CUSTOM>`{.interpreted-text
role="ref"}. This is the balanced point of the body, where applied
forces only cause linear acceleration. Applying forces outside of the
center of mass causes angular acceleration.

When
`center_of_mass_mode<class_RigidBody3D_property_center_of_mass_mode>`{.interpreted-text
role="ref"} is set to
`CENTER_OF_MASS_MODE_AUTO<class_RigidBody3D_constant_CENTER_OF_MASS_MODE_AUTO>`{.interpreted-text
role="ref"} (default value), the center of mass is automatically
computed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_center_of_mass_mode}
::: rst-class
classref-property
:::
::::

`CenterOfMassMode<enum_RigidBody3D_CenterOfMassMode>`{.interpreted-text
role="ref"} **center_of_mass_mode** = `0`
`🔗<class_RigidBody3D_property_center_of_mass_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_of_mass_mode**(value:
  `CenterOfMassMode<enum_RigidBody3D_CenterOfMassMode>`{.interpreted-text
  role="ref"})
- `CenterOfMassMode<enum_RigidBody3D_CenterOfMassMode>`{.interpreted-text
  role="ref"} **get_center_of_mass_mode**()

Defines the way the body\'s center of mass is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_constant_force}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**constant_force** = `Vector3(0, 0, 0)`
`🔗<class_RigidBody3D_property_constant_force>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant_force**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_constant_force**()

The body\'s total constant positional forces applied during each physics
update.

See
`add_constant_force()<class_RigidBody3D_method_add_constant_force>`{.interpreted-text
role="ref"} and
`add_constant_central_force()<class_RigidBody3D_method_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_constant_torque}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**constant_torque** = `Vector3(0, 0, 0)`
`🔗<class_RigidBody3D_property_constant_torque>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant_torque**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_constant_torque**()

The body\'s total constant rotational forces applied during each physics
update.

See
`add_constant_torque()<class_RigidBody3D_method_add_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_contact_monitor}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **contact_monitor** =
`false`
`🔗<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_contact_monitor**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_contact_monitor_enabled**()

If `true`, the RigidBody3D will emit signals when it collides with
another body.

\*\*Note:\*\* By default the maximum contacts reported is set to 0,
meaning nothing will be recorded, see
`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_continuous_cd}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **continuous_cd** =
`false` `🔗<class_RigidBody3D_property_continuous_cd>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_continuous_collision_detection**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_continuous_collision_detection**()

If `true`, continuous collision detection is used.

Continuous collision detection tries to predict where a moving body will
collide, instead of moving it and correcting its movement if it
collided. Continuous collision detection is more precise, and misses
fewer impacts by small, fast-moving objects. Not using continuous
collision detection is faster to compute, but can miss small,
fast-moving objects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_custom_integrator}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **custom_integrator** =
`false`
`🔗<class_RigidBody3D_property_custom_integrator>`{.interpreted-text
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
`_integrate_forces()<class_RigidBody3D_private_method__integrate_forces>`{.interpreted-text
role="ref"} method, if that virtual method is overridden.

Setting this property will call the method
`PhysicsServer3D.body_set_omit_force_integration()<class_PhysicsServer3D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"} internally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_freeze}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **freeze** = `false`
`🔗<class_RigidBody3D_property_freeze>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_freeze_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_freeze_enabled**()

If `true`, the body is frozen. Gravity and forces are not applied
anymore.

See
`freeze_mode<class_RigidBody3D_property_freeze_mode>`{.interpreted-text
role="ref"} to set the body\'s behavior when frozen.

For a body that is always frozen, use
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} or
`AnimatableBody3D<class_AnimatableBody3D>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_freeze_mode}
::: rst-class
classref-property
:::
::::

`FreezeMode<enum_RigidBody3D_FreezeMode>`{.interpreted-text role="ref"}
**freeze_mode** = `0`
`🔗<class_RigidBody3D_property_freeze_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_freeze_mode**(value:
  `FreezeMode<enum_RigidBody3D_FreezeMode>`{.interpreted-text
  role="ref"})
- `FreezeMode<enum_RigidBody3D_FreezeMode>`{.interpreted-text
  role="ref"} **get_freeze_mode**()

The body\'s freeze mode. Can be used to set the body\'s behavior when
`freeze<class_RigidBody3D_property_freeze>`{.interpreted-text
role="ref"} is enabled.

For a body that is always frozen, use
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} or
`AnimatableBody3D<class_AnimatableBody3D>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_gravity_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **gravity_scale** =
`1.0` `🔗<class_RigidBody3D_property_gravity_scale>`{.interpreted-text
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

:::: {#class_RigidBody3D_property_inertia}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **inertia** =
`Vector3(0, 0, 0)`
`🔗<class_RigidBody3D_property_inertia>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inertia**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_inertia**()

The body\'s moment of inertia. This is like mass, but for rotation: it
determines how much torque it takes to rotate the body on each axis. The
moment of inertia is usually computed automatically from the mass and
the shapes, but this property allows you to set a custom value.

If set to `Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}, inertia is automatically computed (default value).

\*\*Note:\*\* This value does not change when inertia is automatically
computed. Use `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} to get the computed inertia.

::::: tabs
::: code-tab
gdscript

\@onready var ball = \$Ball

func get_ball_inertia():

:   return
    PhysicsServer3D.body_get_direct_state(ball.get_rid()).inverse_inertia.inverse()
:::

::: code-tab
csharp

private RigidBody3D [ball]{#ball};

public override void [Ready]{#ready}() { [ball]{#ball} =
GetNode\<RigidBody3D\>(\"Ball\"); }

private Vector3 GetBallInertia() { return
PhysicsServer3D.BodyGetDirectState([ball.GetRid]{#ball.getrid}()).InverseInertia.Inverse();
}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_linear_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_damp** =
`0.0` `🔗<class_RigidBody3D_property_linear_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_damp**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_linear_damp**()

Damps the body\'s movement. By default, the body will use the
`ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>`{.interpreted-text
role="ref"} project setting or any value override set by an
`Area3D<class_Area3D>`{.interpreted-text role="ref"} the body is in.
Depending on
`linear_damp_mode<class_RigidBody3D_property_linear_damp_mode>`{.interpreted-text
role="ref"}, you can set
`linear_damp<class_RigidBody3D_property_linear_damp>`{.interpreted-text
role="ref"} to be added to or to replace the body\'s damping value.

See
`ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>`{.interpreted-text
role="ref"} for more details about damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_linear_damp_mode}
::: rst-class
classref-property
:::
::::

`DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"}
**linear_damp_mode** = `0`
`🔗<class_RigidBody3D_property_linear_damp_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_damp_mode**(value:
  `DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"})
- `DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text role="ref"}
  **get_linear_damp_mode**()

Defines how
`linear_damp<class_RigidBody3D_property_linear_damp>`{.interpreted-text
role="ref"} is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_linear_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**linear_velocity** = `Vector3(0, 0, 0)`
`🔗<class_RigidBody3D_property_linear_velocity>`{.interpreted-text
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
`_integrate_forces()<class_RigidBody3D_private_method__integrate_forces>`{.interpreted-text
role="ref"} as your process loop for precise control of the body state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_lock_rotation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **lock_rotation** =
`false` `🔗<class_RigidBody3D_property_lock_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lock_rotation_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_lock_rotation_enabled**()

If `true`, the body cannot rotate. Gravity and forces only apply linear
movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_mass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mass** = `1.0`
`🔗<class_RigidBody3D_property_mass>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mass**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_mass**()

The body\'s mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_max_contacts_reported}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_contacts_reported**
= `0`
`🔗<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_contacts_reported**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_contacts_reported**()

The maximum number of contacts that will be recorded. Requires a value
greater than 0 and
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"} to be set to `true` to start to register contacts. Use
`get_contact_count()<class_RigidBody3D_method_get_contact_count>`{.interpreted-text
role="ref"} to retrieve the count or
`get_colliding_bodies()<class_RigidBody3D_method_get_colliding_bodies>`{.interpreted-text
role="ref"} to retrieve bodies that have been collided with.

\*\*Note:\*\* The number of contacts is different from the number of
collisions. Collisions between parallel edges will result in two
contacts (one at each end), and collisions between parallel faces will
result in four contacts (one at each corner).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_physics_material_override}
::: rst-class
classref-property
:::
::::

`PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"}
**physics_material_override**
`🔗<class_RigidBody3D_property_physics_material_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_material_override**(value:
  `PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text
  role="ref"})
- `PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"}
  **get_physics_material_override**()

The physics material override for the body.

If a material is assigned to this property, it will be used instead of
any other physics material, such as an inherited one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_property_sleeping}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sleeping** = `false`
`🔗<class_RigidBody3D_property_sleeping>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sleeping**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_sleeping**()

If `true`, the body will not move and will not calculate forces until
woken up by another body through, for example, a collision, or by using
the
`apply_impulse()<class_RigidBody3D_method_apply_impulse>`{.interpreted-text
role="ref"} or
`apply_force()<class_RigidBody3D_method_apply_force>`{.interpreted-text
role="ref"} methods.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RigidBody3D_private_method__integrate_forces}
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
`🔗<class_RigidBody3D_private_method__integrate_forces>`{.interpreted-text
role="ref"}

Called during physics processing, allowing you to read and safely modify
the simulation state for the object. By default, it is called before the
standard force integration, but the
`custom_integrator<class_RigidBody3D_property_custom_integrator>`{.interpreted-text
role="ref"} property allows you to disable the standard force
integration and do fully custom force integration for a body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_add_constant_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_constant_central_force**(force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_method_add_constant_central_force>`{.interpreted-text
role="ref"}

Adds a constant directional force without affecting rotation that keeps
being applied over time until cleared with
`constant_force = Vector3(0, 0, 0)`.

This is equivalent to using
`add_constant_force()<class_RigidBody3D_method_add_constant_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_add_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_constant_force**(force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_RigidBody3D_method_add_constant_force>`{.interpreted-text
role="ref"}

Adds a constant positioned force to the body that keeps being applied
over time until cleared with `constant_force = Vector3(0, 0, 0)`.

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_add_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_constant_torque**(torque:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_method_add_constant_torque>`{.interpreted-text
role="ref"}

Adds a constant rotational force without affecting position that keeps
being applied over time until cleared with
`constant_torque = Vector3(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_force**(force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_method_apply_central_force>`{.interpreted-text
role="ref"}

Applies a directional force without affecting rotation. A force is time
dependent and meant to be applied every physics update.

This is equivalent to using
`apply_force()<class_RigidBody3D_method_apply_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_impulse**(impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_method_apply_central_impulse>`{.interpreted-text
role="ref"}

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

This is equivalent to using
`apply_impulse()<class_RigidBody3D_method_apply_impulse>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_force**(force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_RigidBody3D_method_apply_force>`{.interpreted-text role="ref"}

Applies a positioned force to the body. A force is time dependent and
meant to be applied every physics update.

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_impulse**(impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_RigidBody3D_method_apply_impulse>`{.interpreted-text
role="ref"}

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_apply_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_torque**(torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_RigidBody3D_method_apply_torque>`{.interpreted-text
role="ref"}

Applies a rotational force without affecting position. A force is time
dependent and meant to be applied every physics update.

\*\*Note:\*\*
`inertia<class_RigidBody3D_property_inertia>`{.interpreted-text
role="ref"} is required for this to work. To have
`inertia<class_RigidBody3D_property_inertia>`{.interpreted-text
role="ref"}, an active
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
must be a child of the node, or you can manually set
`inertia<class_RigidBody3D_property_inertia>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_apply_torque_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_torque_impulse**(impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_method_apply_torque_impulse>`{.interpreted-text
role="ref"}

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

\*\*Note:\*\*
`inertia<class_RigidBody3D_property_inertia>`{.interpreted-text
role="ref"} is required for this to work. To have
`inertia<class_RigidBody3D_property_inertia>`{.interpreted-text
role="ref"}, an active
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
must be a child of the node, or you can manually set
`inertia<class_RigidBody3D_property_inertia>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_get_colliding_bodies}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node3D<class_Node3D>`{.interpreted-text role="ref"}\]
**get_colliding_bodies**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RigidBody3D_method_get_colliding_bodies>`{.interpreted-text
role="ref"}

Returns a list of the bodies colliding with this one. Requires
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"} to be set to `true` and
`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"} to be set high enough to detect all the collisions.

\*\*Note:\*\* The result of this test is not immediate after moving
objects. For performance, list of collisions is updated once per frame
and before the physics step. Consider using signals instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_get_contact_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_contact_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RigidBody3D_method_get_contact_count>`{.interpreted-text
role="ref"}

Returns the number of contacts this body has with other bodies. By
default, this returns 0 unless bodies are configured to monitor contacts
(see
`contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* To retrieve the colliding bodies, use
`get_colliding_bodies()<class_RigidBody3D_method_get_colliding_bodies>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_get_inverse_inertia_tensor}
::: rst-class
classref-method
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**get_inverse_inertia_tensor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RigidBody3D_method_get_inverse_inertia_tensor>`{.interpreted-text
role="ref"}

Returns the inverse inertia tensor basis. This is used to calculate the
angular acceleration resulting from a torque applied to the
**RigidBody3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RigidBody3D_method_set_axis_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_velocity**(axis_velocity:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RigidBody3D_method_set_axis_velocity>`{.interpreted-text
role="ref"}

Sets an axis velocity. The velocity in the given vector axis will be set
as the given vector length. This is useful for jumping behavior.
