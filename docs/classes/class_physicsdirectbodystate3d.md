github_url
:   hide

# PhysicsDirectBodyState3D {#class_PhysicsDirectBodyState3D}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`PhysicsDirectBodyState3DExtension<class_PhysicsDirectBodyState3DExtension>`{.interpreted-text
role="ref"}

Provides direct access to a physics body in the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Provides direct access to a physics body in the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"},
allowing safe changes to physics properties. This object is passed via
the direct state callback of
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}, and is
intended for changing the direct state of that body. See
`RigidBody3D._integrate_forces()<class_RigidBody3D_private_method__integrate_forces>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}
- `Ray-casting <../tutorials/physics/ray-casting>`{.interpreted-text
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

:::: {#class_PhysicsDirectBodyState3D_property_angular_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**angular_velocity**
`🔗<class_PhysicsDirectBodyState3D_property_angular_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_angular_velocity**()

The body\'s rotational velocity in *radians* per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_center_of_mass}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**center_of_mass**
`🔗<class_PhysicsDirectBodyState3D_property_center_of_mass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_center_of_mass**()

The body\'s center of mass position relative to the body\'s center in
the global coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_center_of_mass_local}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**center_of_mass_local**
`🔗<class_PhysicsDirectBodyState3D_property_center_of_mass_local>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_center_of_mass_local**()

The body\'s center of mass position in the body\'s local coordinate
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_inverse_inertia}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**inverse_inertia**
`🔗<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_inverse_inertia**()

The inverse of the inertia of the body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_inverse_inertia_tensor}
::: rst-class
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**inverse_inertia_tensor**
`🔗<class_PhysicsDirectBodyState3D_property_inverse_inertia_tensor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Basis<class_Basis>`{.interpreted-text role="ref"}
  **get_inverse_inertia_tensor**()

The inverse of the inertia tensor of the body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_inverse_mass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **inverse_mass**
`🔗<class_PhysicsDirectBodyState3D_property_inverse_mass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_inverse_mass**()

The inverse of the mass of the body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_linear_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**linear_velocity**
`🔗<class_PhysicsDirectBodyState3D_property_linear_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_linear_velocity**()

The body\'s linear velocity in units per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_principal_inertia_axes}
::: rst-class
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"}
**principal_inertia_axes**
`🔗<class_PhysicsDirectBodyState3D_property_principal_inertia_axes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Basis<class_Basis>`{.interpreted-text role="ref"}
  **get_principal_inertia_axes**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_sleeping}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sleeping**
`🔗<class_PhysicsDirectBodyState3D_property_sleeping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sleep_state**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_sleeping**()

If `true`, this body is currently sleeping (not active).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **step**
`🔗<class_PhysicsDirectBodyState3D_property_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"} **get_step**()

The timestep (delta) used for the simulation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_total_angular_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**total_angular_damp**
`🔗<class_PhysicsDirectBodyState3D_property_total_angular_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_total_angular_damp**()

The rate at which the body stops rotating, if there are not any other
forces moving it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_total_gravity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **total_gravity**
`🔗<class_PhysicsDirectBodyState3D_property_total_gravity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_total_gravity**()

The total gravity vector being currently applied to this body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_total_linear_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **total_linear_damp**
`🔗<class_PhysicsDirectBodyState3D_property_total_linear_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_total_linear_damp**()

The rate at which the body stops moving, if there are not any other
forces moving it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_property_transform}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**transform**
`🔗<class_PhysicsDirectBodyState3D_property_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_transform**()

The body\'s transformation matrix.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicsDirectBodyState3D_method_add_constant_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_constant_central_force**(force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"} = Vector3(0, 0,
0))
`🔗<class_PhysicsDirectBodyState3D_method_add_constant_central_force>`{.interpreted-text
role="ref"}

Adds a constant directional force without affecting rotation that keeps
being applied over time until cleared with
`constant_force = Vector3(0, 0, 0)`.

This is equivalent to using
`add_constant_force()<class_PhysicsDirectBodyState3D_method_add_constant_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_add_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_constant_force**(force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicsDirectBodyState3D_method_add_constant_force>`{.interpreted-text
role="ref"}

Adds a constant positioned force to the body that keeps being applied
over time until cleared with `constant_force = Vector3(0, 0, 0)`.

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_add_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_constant_torque**(torque:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsDirectBodyState3D_method_add_constant_torque>`{.interpreted-text
role="ref"}

Adds a constant rotational force without affecting position that keeps
being applied over time until cleared with
`constant_torque = Vector3(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_force**(force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"} = Vector3(0, 0,
0))
`🔗<class_PhysicsDirectBodyState3D_method_apply_central_force>`{.interpreted-text
role="ref"}

Applies a directional force without affecting rotation. A force is time
dependent and meant to be applied every physics update.

This is equivalent to using
`apply_force()<class_PhysicsDirectBodyState3D_method_apply_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_impulse**(impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"} = Vector3(0, 0,
0))
`🔗<class_PhysicsDirectBodyState3D_method_apply_central_impulse>`{.interpreted-text
role="ref"}

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

This is equivalent to using
`apply_impulse()<class_PhysicsDirectBodyState3D_method_apply_impulse>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_force**(force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicsDirectBodyState3D_method_apply_force>`{.interpreted-text
role="ref"}

Applies a positioned force to the body. A force is time dependent and
meant to be applied every physics update.

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_impulse**(impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicsDirectBodyState3D_method_apply_impulse>`{.interpreted-text
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

:::: {#class_PhysicsDirectBodyState3D_method_apply_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_torque**(torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsDirectBodyState3D_method_apply_torque>`{.interpreted-text
role="ref"}

Applies a rotational force without affecting position. A force is time
dependent and meant to be applied every physics update.

\*\*Note:\*\*
`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"} is required for this to work. To have
`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"}, an active
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
must be a child of the node, or you can manually set
`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_apply_torque_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_torque_impulse**(impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsDirectBodyState3D_method_apply_torque_impulse>`{.interpreted-text
role="ref"}

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

\*\*Note:\*\*
`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"} is required for this to work. To have
`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"}, an active
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
must be a child of the node, or you can manually set
`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_constant_force}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_constant_force**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_constant_force>`{.interpreted-text
role="ref"}

Returns the body\'s total constant positional forces applied during each
physics update.

See
`add_constant_force()<class_PhysicsDirectBodyState3D_method_add_constant_force>`{.interpreted-text
role="ref"} and
`add_constant_central_force()<class_PhysicsDirectBodyState3D_method_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_constant_torque}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_constant_torque**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_constant_torque>`{.interpreted-text
role="ref"}

Returns the body\'s total constant rotational forces applied during each
physics update.

See
`add_constant_torque()<class_PhysicsDirectBodyState3D_method_add_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_collider}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_contact_collider**(contact_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider>`{.interpreted-text
role="ref"}

Returns the collider\'s `RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_collider_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_contact_collider_id**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_id>`{.interpreted-text
role="ref"}

Returns the collider\'s object id.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_collider_object}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_contact_collider_object**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_object>`{.interpreted-text
role="ref"}

Returns the collider object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_collider_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_contact_collider_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_position>`{.interpreted-text
role="ref"}

Returns the position of the contact point on the collider in the global
coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_collider_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_contact_collider_shape**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_shape>`{.interpreted-text
role="ref"}

Returns the collider\'s shape index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_collider_velocity_at_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_contact_collider_velocity_at_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_velocity_at_position>`{.interpreted-text
role="ref"}

Returns the linear velocity vector at the collider\'s contact point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_contact_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_count>`{.interpreted-text
role="ref"}

Returns the number of contacts this body has with other bodies.

\*\*Note:\*\* By default, this returns 0 unless bodies are configured to
monitor contacts. See
`RigidBody3D.contact_monitor<class_RigidBody3D_property_contact_monitor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_impulse}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_contact_impulse**(contact_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_impulse>`{.interpreted-text
role="ref"}

Impulse created by the contact.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_local_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_contact_local_normal**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_normal>`{.interpreted-text
role="ref"}

Returns the local normal at the contact point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_local_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_contact_local_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_position>`{.interpreted-text
role="ref"}

Returns the position of the contact point on the body in the global
coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_local_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_contact_local_shape**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_shape>`{.interpreted-text
role="ref"}

Returns the local shape index of the collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_contact_local_velocity_at_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_contact_local_velocity_at_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_velocity_at_position>`{.interpreted-text
role="ref"}

Returns the linear velocity vector at the body\'s contact point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_space_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"} **get_space_state**()
`🔗<class_PhysicsDirectBodyState3D_method_get_space_state>`{.interpreted-text
role="ref"}

Returns the current state of the space, useful for queries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_get_velocity_at_local_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_velocity_at_local_position**(local_position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState3D_method_get_velocity_at_local_position>`{.interpreted-text
role="ref"}

Returns the body\'s velocity at the given relative position, including
both translation and rotation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_integrate_forces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**integrate_forces**()
`🔗<class_PhysicsDirectBodyState3D_method_integrate_forces>`{.interpreted-text
role="ref"}

Updates the body\'s linear and angular velocity by applying gravity and
damping for the equivalent of one physics tick.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_set_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constant_force**(force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsDirectBodyState3D_method_set_constant_force>`{.interpreted-text
role="ref"}

Sets the body\'s total constant positional forces applied during each
physics update.

See
`add_constant_force()<class_PhysicsDirectBodyState3D_method_add_constant_force>`{.interpreted-text
role="ref"} and
`add_constant_central_force()<class_PhysicsDirectBodyState3D_method_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState3D_method_set_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constant_torque**(torque:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsDirectBodyState3D_method_set_constant_torque>`{.interpreted-text
role="ref"}

Sets the body\'s total constant rotational forces applied during each
physics update.

See
`add_constant_torque()<class_PhysicsDirectBodyState3D_method_add_constant_torque>`{.interpreted-text
role="ref"}.
