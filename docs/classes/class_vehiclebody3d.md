github_url
:   hide

# VehicleBody3D {#class_VehicleBody3D}

**Inherits:** `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} **\<**
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
**\<** `CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D physics body that simulates the behavior of a car.

::: rst-class
classref-introduction-group
:::

## Description

This physics body implements all the physics logic needed to simulate a
car. It is based on the raycast vehicle system commonly found in physics
engines. Aside from a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
for the main body of the vehicle, you must also add a
`VehicleWheel3D<class_VehicleWheel3D>`{.interpreted-text role="ref"}
node for each wheel. You should also add a
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"} to
this node for the 3D model of the vehicle, but this model should
generally not include meshes for the wheels. You can control the vehicle
by using the
`brake<class_VehicleBody3D_property_brake>`{.interpreted-text
role="ref"},
`engine_force<class_VehicleBody3D_property_engine_force>`{.interpreted-text
role="ref"}, and
`steering<class_VehicleBody3D_property_steering>`{.interpreted-text
role="ref"} properties. The position or orientation of this node
shouldn\'t be changed directly.

\*\*Note:\*\* The local forward for this node is
`Vector3.MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The origin point of your VehicleBody3D will determine the
center of gravity of your vehicle. To make the vehicle more grounded,
the origin point is usually kept low, moving the
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
and `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
upwards.

\*\*Note:\*\* This class has known issues and isn\'t designed to provide
realistic 3D vehicle physics. If you want advanced vehicle physics, you
may have to write your own physics integration using
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"}
or `RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)

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

:::: {#class_VehicleBody3D_property_brake}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **brake** = `0.0`
`🔗<class_VehicleBody3D_property_brake>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_brake**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_brake**()

Slows down the vehicle by applying a braking force. The vehicle is only
slowed down if the wheels are in contact with a surface. The force you
need to apply to adequately slow down your vehicle depends on the
`RigidBody3D.mass<class_RigidBody3D_property_mass>`{.interpreted-text
role="ref"} of the vehicle. For a vehicle with a mass set to 1000, try a
value in the 25 - 30 range for hard braking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VehicleBody3D_property_engine_force}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **engine_force** =
`0.0` `🔗<class_VehicleBody3D_property_engine_force>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_engine_force**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_engine_force**()

Accelerates the vehicle by applying an engine force. The vehicle is only
sped up if the wheels that have
`VehicleWheel3D.use_as_traction<class_VehicleWheel3D_property_use_as_traction>`{.interpreted-text
role="ref"} set to `true` and are in contact with a surface. The
`RigidBody3D.mass<class_RigidBody3D_property_mass>`{.interpreted-text
role="ref"} of the vehicle has an effect on the acceleration of the
vehicle. For a vehicle with a mass set to 1000, try a value in the 25 -
50 range for acceleration.

\*\*Note:\*\* The simulation does not take the effect of gears into
account, you will need to add logic for this if you wish to simulate
gears.

A negative value will result in the vehicle reversing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VehicleBody3D_property_steering}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **steering** = `0.0`
`🔗<class_VehicleBody3D_property_steering>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_steering**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_steering**()

The steering angle for the vehicle. Setting this to a non-zero value
will result in the vehicle turning when it\'s moving. Wheels that have
`VehicleWheel3D.use_as_steering<class_VehicleWheel3D_property_use_as_steering>`{.interpreted-text
role="ref"} set to `true` will automatically be rotated.

\*\*Note:\*\* This property is edited in the inspector in degrees. In
code the property is set in radians.
