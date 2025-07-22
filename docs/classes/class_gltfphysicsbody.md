github_url
:   hide

# GLTFPhysicsBody {#class_GLTFPhysicsBody}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF physics body.

::: rst-class
classref-introduction-group
:::

## Description

Represents a physics body as an intermediary between the
`OMI_physics_body` glTF data and Godot\'s nodes, and it\'s abstracted in
a way that allows adding support for different glTF physics extensions
in the future.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [OMI_physics_body glTF
  extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_body)

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

:::: {#class_GLTFPhysicsBody_property_angular_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**angular_velocity** = `Vector3(0, 0, 0)`
`🔗<class_GLTFPhysicsBody_property_angular_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_angular_velocity**()

The angular velocity of the physics body, in radians per second. This is
only used when the body type is \"rigid\" or \"vehicle\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_body_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **body_type** =
`"rigid"`
`🔗<class_GLTFPhysicsBody_property_body_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_body_type**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_body_type**()

The type of the body.

When importing, this controls what type of
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} node Godot should generate. Valid values are `"static"`,
`"animatable"`, `"character"`, `"rigid"`, `"vehicle"`, and `"trigger"`.

When exporting, this will be squashed down to one of `"static"`,
`"kinematic"`, or `"dynamic"` motion types, or the `"trigger"` property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_center_of_mass}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**center_of_mass** = `Vector3(0, 0, 0)`
`🔗<class_GLTFPhysicsBody_property_center_of_mass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_of_mass**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_center_of_mass**()

The center of mass of the body, in meters. This is in local space
relative to the body. By default, the center of the mass is the body\'s
origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_inertia_diagonal}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**inertia_diagonal** = `Vector3(0, 0, 0)`
`🔗<class_GLTFPhysicsBody_property_inertia_diagonal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inertia_diagonal**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_inertia_diagonal**()

The inertia strength of the physics body, in kilogram meter squared
(kg⋅m²). This represents the inertia around the principle axes, the
diagonal of the inertia tensor matrix. This is only used when the body
type is \"rigid\" or \"vehicle\".

When converted to a Godot
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} node, if
this value is zero, then the inertia will be calculated automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_inertia_orientation}
::: rst-class
classref-property
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**inertia_orientation** = `Quaternion(0, 0, 0, 1)`
`🔗<class_GLTFPhysicsBody_property_inertia_orientation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inertia_orientation**(value:
  `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
- `Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
  **get_inertia_orientation**()

The inertia orientation of the physics body. This defines the rotation
of the inertia\'s principle axes relative to the object\'s local axes.
This is only used when the body type is \"rigid\" or \"vehicle\" and
`inertia_diagonal<class_GLTFPhysicsBody_property_inertia_diagonal>`{.interpreted-text
role="ref"} is set to a non-zero value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_inertia_tensor}
::: rst-class
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **inertia_tensor** =
`Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)`
`🔗<class_GLTFPhysicsBody_property_inertia_tensor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inertia_tensor**(value: `Basis<class_Basis>`{.interpreted-text
  role="ref"})
- `Basis<class_Basis>`{.interpreted-text role="ref"}
  **get_inertia_tensor**()

**Deprecated:** This property may be changed or removed in future
versions.

The inertia tensor of the physics body, in kilogram meter squared
(kg⋅m²). This is only used when the body type is \"rigid\" or
\"vehicle\".

When converted to a Godot
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} node, if
this value is zero, then the inertia will be calculated automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_linear_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**linear_velocity** = `Vector3(0, 0, 0)`
`🔗<class_GLTFPhysicsBody_property_linear_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_linear_velocity**()

The linear velocity of the physics body, in meters per second. This is
only used when the body type is \"rigid\" or \"vehicle\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_property_mass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mass** = `1.0`
`🔗<class_GLTFPhysicsBody_property_mass>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mass**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_mass**()

The mass of the physics body, in kilograms. This is only used when the
body type is \"rigid\" or \"vehicle\".

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFPhysicsBody_method_from_dictionary}
::: rst-class
classref-method
:::
::::

`GLTFPhysicsBody<class_GLTFPhysicsBody>`{.interpreted-text role="ref"}
**from_dictionary**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsBody_method_from_dictionary>`{.interpreted-text
role="ref"}

Creates a new GLTFPhysicsBody instance by parsing the given
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} in the
`OMI_physics_body` glTF extension format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_method_from_node}
::: rst-class
classref-method
:::
::::

`GLTFPhysicsBody<class_GLTFPhysicsBody>`{.interpreted-text role="ref"}
**from_node**(body_node:
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsBody_method_from_node>`{.interpreted-text
role="ref"}

Creates a new GLTFPhysicsBody instance from the given Godot
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_method_to_dictionary}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**to_dictionary**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsBody_method_to_dictionary>`{.interpreted-text
role="ref"}

Serializes this GLTFPhysicsBody instance into a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}. It will be
in the format expected by the `OMI_physics_body` glTF extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsBody_method_to_node}
::: rst-class
classref-method
:::
::::

`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} **to_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsBody_method_to_node>`{.interpreted-text role="ref"}

Converts this GLTFPhysicsBody instance into a Godot
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} node.
