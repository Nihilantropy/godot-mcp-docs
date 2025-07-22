github_url
:   hide

# StaticBody3D {#class_StaticBody3D}

**Inherits:** `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} **\<**
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimatableBody3D<class_AnimatableBody3D>`{.interpreted-text role="ref"}

A 3D physics body that can\'t be moved by external forces. When moved
manually, it doesn\'t affect other bodies in its path.

::: rst-class
classref-introduction-group
:::

## Description

A static 3D physics body. It can\'t be moved by external forces or
contacts, but can be moved manually by other means such as code,
`AnimationMixer<class_AnimationMixer>`{.interpreted-text role="ref"}s
(with
`AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"} set to
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>`{.interpreted-text
role="ref"}), and
`RemoteTransform3D<class_RemoteTransform3D>`{.interpreted-text
role="ref"}.

When **StaticBody3D** is moved, it is teleported to its new position
without affecting other physics bodies in its path. If this is not
desired, use
`AnimatableBody3D<class_AnimatableBody3D>`{.interpreted-text role="ref"}
instead.

\*\*StaticBody3D\*\* is useful for completely static objects like floors
and walls, as well as moving surfaces like conveyor belts and circular
revolving platforms (by using
`constant_linear_velocity<class_StaticBody3D_property_constant_linear_velocity>`{.interpreted-text
role="ref"} and
`constant_angular_velocity<class_StaticBody3D_property_constant_angular_velocity>`{.interpreted-text
role="ref"}).

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

:::: {#class_StaticBody3D_property_constant_angular_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**constant_angular_velocity** = `Vector3(0, 0, 0)`
`🔗<class_StaticBody3D_property_constant_angular_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant_angular_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_constant_angular_velocity**()

The body\'s constant angular velocity. This does not rotate the body,
but affects touching bodies, as if it were rotating.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StaticBody3D_property_constant_linear_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**constant_linear_velocity** = `Vector3(0, 0, 0)`
`🔗<class_StaticBody3D_property_constant_linear_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant_linear_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_constant_linear_velocity**()

The body\'s constant linear velocity. This does not move the body, but
affects touching bodies, as if it were moving.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StaticBody3D_property_physics_material_override}
::: rst-class
classref-property
:::
::::

`PhysicsMaterial<class_PhysicsMaterial>`{.interpreted-text role="ref"}
**physics_material_override**
`🔗<class_StaticBody3D_property_physics_material_override>`{.interpreted-text
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
