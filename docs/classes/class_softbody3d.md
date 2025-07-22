github_url
:   hide

# SoftBody3D {#class_SoftBody3D}

**Inherits:** `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A deformable 3D physics mesh.

::: rst-class
classref-introduction-group
:::

## Description

A deformable 3D physics mesh. Used to create elastic or deformable
objects such as cloth, rubber, or other flexible materials.

Additionally, **SoftBody3D** is subject to wind forces defined in
`Area3D<class_Area3D>`{.interpreted-text role="ref"} (see
`Area3D.wind_source_path<class_Area3D_property_wind_source_path>`{.interpreted-text
role="ref"},
`Area3D.wind_force_magnitude<class_Area3D_property_wind_force_magnitude>`{.interpreted-text
role="ref"}, and
`Area3D.wind_attenuation_factor<class_Area3D_property_wind_attenuation_factor>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* It\'s recommended to use Jolt Physics when using
**SoftBody3D** instead of the default GodotPhysics3D, as Jolt Physics\'
soft body implementation is faster and more reliable. You can switch the
physics engine using the
`ProjectSettings.physics/3d/physics_engine<class_ProjectSettings_property_physics/3d/physics_engine>`{.interpreted-text
role="ref"} project setting.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `SoftBody <../tutorials/physics/soft_body>`{.interpreted-text
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

## Enumerations

:::: {#enum_SoftBody3D_DisableMode}
::: rst-class
classref-enumeration
:::
::::

enum **DisableMode**:
`🔗<enum_SoftBody3D_DisableMode>`{.interpreted-text role="ref"}

:::: {#class_SoftBody3D_constant_DISABLE_MODE_REMOVE}
::: rst-class
classref-enumeration-constant
:::
::::

`DisableMode<enum_SoftBody3D_DisableMode>`{.interpreted-text role="ref"}
**DISABLE_MODE_REMOVE** = `0`

When
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}, remove from the physics simulation to stop all physics
interactions with this **SoftBody3D**.

Automatically re-added to the physics simulation when the
`Node<class_Node>`{.interpreted-text role="ref"} is processed again.

:::: {#class_SoftBody3D_constant_DISABLE_MODE_KEEP_ACTIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`DisableMode<enum_SoftBody3D_DisableMode>`{.interpreted-text role="ref"}
**DISABLE_MODE_KEEP_ACTIVE** = `1`

When
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}, do not affect the physics simulation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SoftBody3D_property_collision_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_layer** = `1`
`🔗<class_SoftBody3D_property_collision_layer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_layer**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_layer**()

The physics layers this SoftBody3D **is in**. Collision objects can
exist in one or more of 32 different layers. See also
`collision_mask<class_SoftBody3D_property_collision_mask>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Object A can detect a contact with object B only if object
B is in any of the layers that object A scans. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_SoftBody3D_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The physics layers this SoftBody3D **scans**. Collision objects can scan
one or more of 32 different layers. See also
`collision_layer<class_SoftBody3D_property_collision_layer>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Object A can detect a contact with object B only if object
B is in any of the layers that object A scans. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_damping_coefficient}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**damping_coefficient** = `0.01`
`🔗<class_SoftBody3D_property_damping_coefficient>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_damping_coefficient**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_damping_coefficient**()

The body\'s damping coefficient. Higher values will slow down the body
more noticeably when forces are applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_disable_mode}
::: rst-class
classref-property
:::
::::

`DisableMode<enum_SoftBody3D_DisableMode>`{.interpreted-text role="ref"}
**disable_mode** = `0`
`🔗<class_SoftBody3D_property_disable_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_mode**(value:
  `DisableMode<enum_SoftBody3D_DisableMode>`{.interpreted-text
  role="ref"})
- `DisableMode<enum_SoftBody3D_DisableMode>`{.interpreted-text
  role="ref"} **get_disable_mode**()

Defines the behavior in physics when
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_drag_coefficient}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **drag_coefficient**
= `0.0`
`🔗<class_SoftBody3D_property_drag_coefficient>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_coefficient**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_drag_coefficient**()

The body\'s drag coefficient. Higher values increase this body\'s air
resistance.

\*\*Note:\*\* This value is currently unused by Godot\'s default physics
implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_linear_stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_stiffness**
= `0.5`
`🔗<class_SoftBody3D_property_linear_stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_stiffness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_linear_stiffness**()

Higher values will result in a stiffer body, while lower values will
increase the body\'s ability to bend. The value can be between `0.0` and
`1.0` (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_parent_collision_ignore}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**parent_collision_ignore** = `NodePath("")`
`🔗<class_SoftBody3D_property_parent_collision_ignore>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parent_collision_ignore**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_parent_collision_ignore**()

`NodePath<class_NodePath>`{.interpreted-text role="ref"} to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} this SoftBody3D should avoid clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_pressure_coefficient}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**pressure_coefficient** = `0.0`
`🔗<class_SoftBody3D_property_pressure_coefficient>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressure_coefficient**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pressure_coefficient**()

The pressure coefficient of this soft body. Simulate pressure build-up
from inside this body. Higher values increase the strength of this
effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_ray_pickable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ray_pickable** =
`true` `🔗<class_SoftBody3D_property_ray_pickable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ray_pickable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ray_pickable**()

If `true`, the **SoftBody3D** will respond to
`RayCast3D<class_RayCast3D>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_shrinking_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **shrinking_factor**
= `0.0`
`🔗<class_SoftBody3D_property_shrinking_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shrinking_factor**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_shrinking_factor**()

Scales the rest lengths of **SoftBody3D**\'s edge constraints. Positive
values shrink the mesh, while negative values expand it. For example, a
value of `0.1` shortens the edges of the mesh by 10%, while `-0.1`
expands the edges by 10%.

\*\*Note:\*\*
`shrinking_factor<class_SoftBody3D_property_shrinking_factor>`{.interpreted-text
role="ref"} is best used on surface meshes with pinned points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_simulation_precision}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **simulation_precision**
= `5`
`🔗<class_SoftBody3D_property_simulation_precision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_simulation_precision**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_simulation_precision**()

Increasing this value will improve the resulting simulation, but can
affect performance. Use with care.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_property_total_mass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **total_mass** =
`1.0` `🔗<class_SoftBody3D_property_total_mass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_total_mass**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_total_mass**()

The SoftBody3D\'s mass.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SoftBody3D_method_add_collision_exception_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_collision_exception_with**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_SoftBody3D_method_add_collision_exception_with>`{.interpreted-text
role="ref"}

Adds a body to the list of bodies that this body can\'t collide with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_force**(force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_SoftBody3D_method_apply_central_force>`{.interpreted-text
role="ref"}

Distributes and applies a force to all points. A force is time dependent
and meant to be applied every physics update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_central_impulse**(impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_SoftBody3D_method_apply_central_impulse>`{.interpreted-text
role="ref"}

Distributes and applies an impulse to all points.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_force**(point_index: `int<class_int>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_SoftBody3D_method_apply_force>`{.interpreted-text
role="ref"}

Applies a force to a point. A force is time dependent and meant to be
applied every physics update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_impulse**(point_index: `int<class_int>`{.interpreted-text
role="ref"}, impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_SoftBody3D_method_apply_impulse>`{.interpreted-text
role="ref"}

Applies an impulse to a point.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_get_collision_exceptions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"}\] **get_collision_exceptions**()
`🔗<class_SoftBody3D_method_get_collision_exceptions>`{.interpreted-text
role="ref"}

Returns an array of nodes that were added as collision exceptions for
this body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_get_collision_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SoftBody3D_method_get_collision_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_layer<class_SoftBody3D_property_collision_layer>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_get_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SoftBody3D_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_mask<class_SoftBody3D_property_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_get_physics_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_physics_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SoftBody3D_method_get_physics_rid>`{.interpreted-text
role="ref"}

Returns the internal `RID<class_RID>`{.interpreted-text role="ref"} used
by the `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} for this body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_get_point_transform}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_point_transform**(point_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SoftBody3D_method_get_point_transform>`{.interpreted-text
role="ref"}

Returns local translation of a vertex in the surface array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_is_point_pinned}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_pinned**(point_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SoftBody3D_method_is_point_pinned>`{.interpreted-text
role="ref"}

Returns `true` if vertex is set to pinned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_remove_collision_exception_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_collision_exception_with**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_SoftBody3D_method_remove_collision_exception_with>`{.interpreted-text
role="ref"}

Removes a body from the list of bodies that this body can\'t collide
with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_set_collision_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SoftBody3D_method_set_collision_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_layer<class_SoftBody3D_property_collision_layer>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_set_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SoftBody3D_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_mask<class_SoftBody3D_property_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SoftBody3D_method_set_point_pinned}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_pinned**(point_index: `int<class_int>`{.interpreted-text
role="ref"}, pinned: `bool<class_bool>`{.interpreted-text role="ref"},
attachment_path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"} = NodePath(\"\"), insert_at:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_SoftBody3D_method_set_point_pinned>`{.interpreted-text
role="ref"}

Sets the pinned state of a surface vertex. When set to `true`, the
optional `attachment_path` can define a
`Node3D<class_Node3D>`{.interpreted-text role="ref"} the pinned vertex
will be attached to.
