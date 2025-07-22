github_url
:   hide

# SpringBoneSimulator3D {#class_SpringBoneSimulator3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} to apply inertial wavering to bone chains.

::: rst-class
classref-introduction-group
:::

## Description

This `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} can be used to wiggle hair, cloth, and tails. This modifier
behaves differently from
`PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>`{.interpreted-text
role="ref"} as it attempts to return the original pose after
modification.

If you setup
`set_root_bone()<class_SpringBoneSimulator3D_method_set_root_bone>`{.interpreted-text
role="ref"} and
`set_end_bone()<class_SpringBoneSimulator3D_method_set_end_bone>`{.interpreted-text
role="ref"}, it is treated as one bone chain. Note that it does not
support a branched chain like Y-shaped chains.

When a bone chain is created, an array is generated from the bones that
exist in between and listed in the joint list.

Several properties can be applied to each joint, such as
`set_joint_stiffness()<class_SpringBoneSimulator3D_method_set_joint_stiffness>`{.interpreted-text
role="ref"},
`set_joint_drag()<class_SpringBoneSimulator3D_method_set_joint_drag>`{.interpreted-text
role="ref"}, and
`set_joint_gravity()<class_SpringBoneSimulator3D_method_set_joint_gravity>`{.interpreted-text
role="ref"}.

For simplicity, you can set values to all joints at the same time by
using a `Curve<class_Curve>`{.interpreted-text role="ref"}. If you want
to specify detailed values individually, set
`set_individual_config()<class_SpringBoneSimulator3D_method_set_individual_config>`{.interpreted-text
role="ref"} to `true`.

For physical simulation, **SpringBoneSimulator3D** can have children as
self-standing collisions that are not related to
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"},
see also
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* A scaled **SpringBoneSimulator3D** will likely not
behave as expected. Make sure that the parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} and its
bones are not scaled.

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

:::: {#enum_SpringBoneSimulator3D_BoneDirection}
::: rst-class
classref-enumeration
:::
::::

enum **BoneDirection**:
`🔗<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"}

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_PLUS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_PLUS_X** = `0`

Enumerated value for the +X axis.

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_MINUS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_MINUS_X** = `1`

Enumerated value for the -X axis.

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_PLUS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_PLUS_Y** = `2`

Enumerated value for the +Y axis.

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_MINUS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_MINUS_Y** = `3`

Enumerated value for the -Y axis.

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_PLUS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_PLUS_Z** = `4`

Enumerated value for the +Z axis.

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_MINUS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_MINUS_Z** = `5`

Enumerated value for the -Z axis.

:::: {#class_SpringBoneSimulator3D_constant_BONE_DIRECTION_FROM_PARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **BONE_DIRECTION_FROM_PARENT** = `6`

Enumerated value for the axis from a parent bone to the child bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_SpringBoneSimulator3D_CenterFrom}
::: rst-class
classref-enumeration
:::
::::

enum **CenterFrom**:
`🔗<enum_SpringBoneSimulator3D_CenterFrom>`{.interpreted-text
role="ref"}

:::: {#class_SpringBoneSimulator3D_constant_CENTER_FROM_WORLD_ORIGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`CenterFrom<enum_SpringBoneSimulator3D_CenterFrom>`{.interpreted-text
role="ref"} **CENTER_FROM_WORLD_ORIGIN** = `0`

The world origin is defined as center.

:::: {#class_SpringBoneSimulator3D_constant_CENTER_FROM_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`CenterFrom<enum_SpringBoneSimulator3D_CenterFrom>`{.interpreted-text
role="ref"} **CENTER_FROM_NODE** = `1`

The `Node3D<class_Node3D>`{.interpreted-text role="ref"} specified by
`set_center_node()<class_SpringBoneSimulator3D_method_set_center_node>`{.interpreted-text
role="ref"} is defined as center.

If `Node3D<class_Node3D>`{.interpreted-text role="ref"} is not found,
the parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
is treated as center.

:::: {#class_SpringBoneSimulator3D_constant_CENTER_FROM_BONE}
::: rst-class
classref-enumeration-constant
:::
::::

`CenterFrom<enum_SpringBoneSimulator3D_CenterFrom>`{.interpreted-text
role="ref"} **CENTER_FROM_BONE** = `2`

The bone pose origin of the parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} specified
by
`set_center_bone()<class_SpringBoneSimulator3D_method_set_center_bone>`{.interpreted-text
role="ref"} is defined as center.

If `Node3D<class_Node3D>`{.interpreted-text role="ref"} is not found,
the parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
is treated as center.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_SpringBoneSimulator3D_RotationAxis}
::: rst-class
classref-enumeration
:::
::::

enum **RotationAxis**:
`🔗<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"}

:::: {#class_SpringBoneSimulator3D_constant_ROTATION_AXIS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **ROTATION_AXIS_X** = `0`

Enumerated value for the rotation of the X axis.

:::: {#class_SpringBoneSimulator3D_constant_ROTATION_AXIS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **ROTATION_AXIS_Y** = `1`

Enumerated value for the rotation of the Y axis.

:::: {#class_SpringBoneSimulator3D_constant_ROTATION_AXIS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **ROTATION_AXIS_Z** = `2`

Enumerated value for the rotation of the Z axis.

:::: {#class_SpringBoneSimulator3D_constant_ROTATION_AXIS_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **ROTATION_AXIS_ALL** = `3`

Enumerated value for the unconstrained rotation.

:::: {#class_SpringBoneSimulator3D_constant_ROTATION_AXIS_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **ROTATION_AXIS_CUSTOM** = `4`

Enumerated value for an optional rotation axis. See also
`set_joint_rotation_axis_vector()<class_SpringBoneSimulator3D_method_set_joint_rotation_axis_vector>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SpringBoneSimulator3D_property_external_force}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**external_force** = `Vector3(0, 0, 0)`
`🔗<class_SpringBoneSimulator3D_property_external_force>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_external_force**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_external_force**()

The constant force that always affected bones. It is equal to the result
when the parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} moves at this speed in the opposite direction.

This is useful for effects such as wind and anti-gravity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_property_setting_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **setting_count** = `0`
`🔗<class_SpringBoneSimulator3D_property_setting_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_setting_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_setting_count**()

The number of settings.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**are_all_child_collisions_enabled**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"}

Returns `true` if all child
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"}s are contained in the collision list at `index` in the
settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_clear_collisions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_collisions**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_clear_collisions>`{.interpreted-text
role="ref"}

Clears all collisions from the collision list at `index` in the settings
when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_clear_exclude_collisions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_exclude_collisions**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_clear_exclude_collisions>`{.interpreted-text
role="ref"}

Clears all exclude collisions from the collision list at `index` in the
settings when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_clear_settings}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_settings**()
`🔗<class_SpringBoneSimulator3D_method_clear_settings>`{.interpreted-text
role="ref"}

Clears all settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_center_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_center_bone**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_center_bone>`{.interpreted-text
role="ref"}

Returns the center bone index of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_center_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_center_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_center_bone_name>`{.interpreted-text
role="ref"}

Returns the center bone name of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_center_from}
::: rst-class
classref-method
:::
::::

`CenterFrom<enum_SpringBoneSimulator3D_CenterFrom>`{.interpreted-text
role="ref"} **get_center_from**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_center_from>`{.interpreted-text
role="ref"}

Returns what the center originates from in the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_center_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_center_node**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_center_node>`{.interpreted-text
role="ref"}

Returns the center node path of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_collision_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collision_count**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_collision_count>`{.interpreted-text
role="ref"}

Returns the collision count of the bone chain\'s collision list when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_collision_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_collision_path**(index: `int<class_int>`{.interpreted-text
role="ref"}, collision: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_collision_path>`{.interpreted-text
role="ref"}

Returns the node path of the
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} at `collision` in the bone chain\'s collision list when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_drag}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_drag**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_drag>`{.interpreted-text
role="ref"}

Returns the drag force damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_drag_damping_curve}
::: rst-class
classref-method
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**get_drag_damping_curve**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_drag_damping_curve>`{.interpreted-text
role="ref"}

Returns the drag force damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_end_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_end_bone**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_end_bone>`{.interpreted-text
role="ref"}

Returns the end bone index of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_end_bone_direction}
::: rst-class
classref-method
:::
::::

`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"} **get_end_bone_direction**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_end_bone_direction>`{.interpreted-text
role="ref"}

Returns the end bone\'s tail direction of the bone chain when
`is_end_bone_extended()<class_SpringBoneSimulator3D_method_is_end_bone_extended>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_end_bone_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_end_bone_length**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_end_bone_length>`{.interpreted-text
role="ref"}

Returns the end bone\'s tail length of the bone chain when
`is_end_bone_extended()<class_SpringBoneSimulator3D_method_is_end_bone_extended>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_end_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_end_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_end_bone_name>`{.interpreted-text
role="ref"}

Returns the end bone name of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_exclude_collision_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_exclude_collision_count**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_exclude_collision_count>`{.interpreted-text
role="ref"}

Returns the exclude collision count of the bone chain\'s exclude
collision list when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_exclude_collision_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_exclude_collision_path**(index: `int<class_int>`{.interpreted-text
role="ref"}, collision: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_exclude_collision_path>`{.interpreted-text
role="ref"}

Returns the node path of the
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} at `collision` in the bone chain\'s exclude collision list
when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_gravity}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_gravity**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_gravity>`{.interpreted-text
role="ref"}

Returns the gravity amount of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_gravity_damping_curve}
::: rst-class
classref-method
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**get_gravity_damping_curve**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_gravity_damping_curve>`{.interpreted-text
role="ref"}

Returns the gravity amount damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_gravity_direction}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_gravity_direction**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_gravity_direction>`{.interpreted-text
role="ref"}

Returns the gravity direction of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_joint_bone**(index:
`int<class_int>`{.interpreted-text role="ref"}, joint:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_bone>`{.interpreted-text
role="ref"}

Returns the bone index at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_joint_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_bone_name>`{.interpreted-text
role="ref"}

Returns the bone name at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_joint_count**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_count>`{.interpreted-text
role="ref"}

Returns the joint count of the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_drag}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_joint_drag**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_drag>`{.interpreted-text
role="ref"}

Returns the drag force at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_gravity}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_joint_gravity**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_gravity>`{.interpreted-text
role="ref"}

Returns the gravity amount at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_gravity_direction}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_joint_gravity_direction**(index:
`int<class_int>`{.interpreted-text role="ref"}, joint:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_gravity_direction>`{.interpreted-text
role="ref"}

Returns the gravity direction at `joint` in the bone chain\'s joint
list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_radius}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_joint_radius**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_radius>`{.interpreted-text
role="ref"}

Returns the radius at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_rotation_axis}
::: rst-class
classref-method
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **get_joint_rotation_axis**(index:
`int<class_int>`{.interpreted-text role="ref"}, joint:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_rotation_axis>`{.interpreted-text
role="ref"}

Returns the rotation axis at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_rotation_axis_vector}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_joint_rotation_axis_vector**(index:
`int<class_int>`{.interpreted-text role="ref"}, joint:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_rotation_axis_vector>`{.interpreted-text
role="ref"}

Returns the rotation axis vector for the specified joint in the bone
chain. This vector represents the axis around which the joint can
rotate. It is determined based on the rotation axis set for the joint.

If
`get_joint_rotation_axis()<class_SpringBoneSimulator3D_method_get_joint_rotation_axis>`{.interpreted-text
role="ref"} is
`ROTATION_AXIS_ALL<class_SpringBoneSimulator3D_constant_ROTATION_AXIS_ALL>`{.interpreted-text
role="ref"}, this method returns `Vector3(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_joint_stiffness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_joint_stiffness**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_joint_stiffness>`{.interpreted-text
role="ref"}

Returns the stiffness force at `joint` in the bone chain\'s joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_radius}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_radius**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_radius>`{.interpreted-text
role="ref"}

Returns the joint radius of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_radius_damping_curve}
::: rst-class
classref-method
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**get_radius_damping_curve**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_radius_damping_curve>`{.interpreted-text
role="ref"}

Returns the joint radius damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_root_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_root_bone**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_root_bone>`{.interpreted-text
role="ref"}

Returns the root bone index of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_root_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_root_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_root_bone_name>`{.interpreted-text
role="ref"}

Returns the root bone name of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_rotation_axis}
::: rst-class
classref-method
:::
::::

`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"} **get_rotation_axis**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_rotation_axis>`{.interpreted-text
role="ref"}

Returns the rotation axis of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_rotation_axis_vector}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_rotation_axis_vector**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_rotation_axis_vector>`{.interpreted-text
role="ref"}

Returns the rotation axis vector of the bone chain. This vector
represents the axis around which the bone chain can rotate. It is
determined based on the rotation axis set for the bone chain.

If
`get_rotation_axis()<class_SpringBoneSimulator3D_method_get_rotation_axis>`{.interpreted-text
role="ref"} is
`ROTATION_AXIS_ALL<class_SpringBoneSimulator3D_constant_ROTATION_AXIS_ALL>`{.interpreted-text
role="ref"}, this method returns `Vector3(0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_stiffness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_stiffness**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_stiffness>`{.interpreted-text
role="ref"}

Returns the stiffness force of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_get_stiffness_damping_curve}
::: rst-class
classref-method
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**get_stiffness_damping_curve**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_get_stiffness_damping_curve>`{.interpreted-text
role="ref"}

Returns the stiffness force damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_is_config_individual}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_config_individual**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"}

Returns `true` if the config can be edited individually for each joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_is_end_bone_extended}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_end_bone_extended**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneSimulator3D_method_is_end_bone_extended>`{.interpreted-text
role="ref"}

Returns `true` if the end bone is extended to have the tail.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_reset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reset**()
`🔗<class_SpringBoneSimulator3D_method_reset>`{.interpreted-text
role="ref"}

Resets a simulating state with respect to the current bone pose.

It is useful to prevent the simulation result getting violent. For
example, calling this immediately after a call to
`AnimationPlayer.play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"} without a fading, or within the previous
`SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>`{.interpreted-text
role="ref"} signal if it\'s condition changes significantly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_center_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_center_bone**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_center_bone>`{.interpreted-text
role="ref"}

Sets the center bone index of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_center_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_center_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_center_bone_name>`{.interpreted-text
role="ref"}

Sets the center bone name of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_center_from}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_center_from**(index: `int<class_int>`{.interpreted-text
role="ref"}, center_from:
`CenterFrom<enum_SpringBoneSimulator3D_CenterFrom>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_center_from>`{.interpreted-text
role="ref"}

Sets what the center originates from in the bone chain.

Bone movement is calculated based on the difference in relative distance
between center and bone in the previous and next frames.

For example, if the parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} is used as
the center, the bones are considered to have not moved if the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} moves in
the world.

In this case, only a change in the bone pose is considered to be a bone
movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_center_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_center_node**(index: `int<class_int>`{.interpreted-text
role="ref"}, node_path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_center_node>`{.interpreted-text
role="ref"}

Sets the center node path of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_collision_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_count**(index: `int<class_int>`{.interpreted-text
role="ref"}, count: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_collision_count>`{.interpreted-text
role="ref"}

Sets the number of collisions in the collision list at `index` in the
settings when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_collision_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_path**(index: `int<class_int>`{.interpreted-text
role="ref"}, collision: `int<class_int>`{.interpreted-text role="ref"},
node_path: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_collision_path>`{.interpreted-text
role="ref"}

Sets the node path of the
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} at `collision` in the bone chain\'s collision list when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_drag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_drag**(index: `int<class_int>`{.interpreted-text role="ref"},
drag: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_drag>`{.interpreted-text
role="ref"}

Sets the drag force of the bone chain. The greater the value, the more
suppressed the wiggling.

The value is scaled by
`set_drag_damping_curve()<class_SpringBoneSimulator3D_method_set_drag_damping_curve>`{.interpreted-text
role="ref"} and cached in each joint setting in the joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_drag_damping_curve}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_drag_damping_curve**(index: `int<class_int>`{.interpreted-text
role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_drag_damping_curve>`{.interpreted-text
role="ref"}

Sets the drag force damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_enable_all_child_collisions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_enable_all_child_collisions**(index:
`int<class_int>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_enable_all_child_collisions>`{.interpreted-text
role="ref"}

If `enabled` is `true`, all child
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"}s are colliding and
`set_exclude_collision_path()<class_SpringBoneSimulator3D_method_set_exclude_collision_path>`{.interpreted-text
role="ref"} is enabled as an exclusion list at `index` in the settings.

If `enabled` is `false`, you need to manually register all valid
collisions with
`set_collision_path()<class_SpringBoneSimulator3D_method_set_collision_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_end_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_end_bone**(index: `int<class_int>`{.interpreted-text role="ref"},
bone: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_end_bone>`{.interpreted-text
role="ref"}

Sets the end bone index of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_end_bone_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_end_bone_direction**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone_direction:
`BoneDirection<enum_SpringBoneSimulator3D_BoneDirection>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_end_bone_direction>`{.interpreted-text
role="ref"}

Sets the end bone tail direction of the bone chain when
`is_end_bone_extended()<class_SpringBoneSimulator3D_method_is_end_bone_extended>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_end_bone_length}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_end_bone_length**(index: `int<class_int>`{.interpreted-text
role="ref"}, length: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_end_bone_length>`{.interpreted-text
role="ref"}

Sets the end bone tail length of the bone chain when
`is_end_bone_extended()<class_SpringBoneSimulator3D_method_is_end_bone_extended>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_end_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_end_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_end_bone_name>`{.interpreted-text
role="ref"}

Sets the end bone name of the bone chain.

\*\*Note:\*\* End bone must be the root bone or a child of the root
bone. If they are the same, the tail must be extended by
`set_extend_end_bone()<class_SpringBoneSimulator3D_method_set_extend_end_bone>`{.interpreted-text
role="ref"} to jiggle the bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_exclude_collision_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_exclude_collision_count**(index:
`int<class_int>`{.interpreted-text role="ref"}, count:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_exclude_collision_count>`{.interpreted-text
role="ref"}

Sets the number of exclude collisions in the exclude collision list at
`index` in the settings when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_exclude_collision_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_exclude_collision_path**(index: `int<class_int>`{.interpreted-text
role="ref"}, collision: `int<class_int>`{.interpreted-text role="ref"},
node_path: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_exclude_collision_path>`{.interpreted-text
role="ref"}

Sets the node path of the
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} at `collision` in the bone chain\'s exclude collision list
when
`are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_extend_end_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_extend_end_bone**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_extend_end_bone>`{.interpreted-text
role="ref"}

If `enabled` is `true`, the end bone is extended to have the tail.

The extended tail config is allocated to the last element in the joint
list.

In other words, if you set `enabled` is `false`, the config of last
element in the joint list has no effect in the simulated result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_gravity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gravity**(index: `int<class_int>`{.interpreted-text role="ref"},
gravity: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_gravity>`{.interpreted-text
role="ref"}

Sets the gravity amount of the bone chain. This value is not an
acceleration, but a constant velocity of movement in
`set_gravity_direction()<class_SpringBoneSimulator3D_method_set_gravity_direction>`{.interpreted-text
role="ref"}.

If `gravity` is not `0`, the modified pose will not return to the
original pose since it is always affected by gravity.

The value is scaled by
`set_gravity_damping_curve()<class_SpringBoneSimulator3D_method_set_gravity_damping_curve>`{.interpreted-text
role="ref"} and cached in each joint setting in the joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_gravity_damping_curve}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gravity_damping_curve**(index: `int<class_int>`{.interpreted-text
role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_gravity_damping_curve>`{.interpreted-text
role="ref"}

Sets the gravity amount damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_gravity_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gravity_direction**(index: `int<class_int>`{.interpreted-text
role="ref"}, gravity_direction:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_gravity_direction>`{.interpreted-text
role="ref"}

Sets the gravity direction of the bone chain. This value is internally
normalized and then multiplied by
`set_gravity()<class_SpringBoneSimulator3D_method_set_gravity>`{.interpreted-text
role="ref"}.

The value is cached in each joint setting in the joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_individual_config}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_individual_config**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_individual_config>`{.interpreted-text
role="ref"}

If `enabled` is `true`, the config can be edited individually for each
joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_drag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_drag**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"},
drag: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_drag>`{.interpreted-text
role="ref"}

Sets the drag force at `joint` in the bone chain\'s joint list when
`is_config_individual()<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_gravity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_gravity**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"},
gravity: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_gravity>`{.interpreted-text
role="ref"}

Sets the gravity amount at `joint` in the bone chain\'s joint list when
`is_config_individual()<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_gravity_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_gravity_direction**(index:
`int<class_int>`{.interpreted-text role="ref"}, joint:
`int<class_int>`{.interpreted-text role="ref"}, gravity_direction:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_gravity_direction>`{.interpreted-text
role="ref"}

Sets the gravity direction at `joint` in the bone chain\'s joint list
when
`is_config_individual()<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_radius**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"},
radius: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_radius>`{.interpreted-text
role="ref"}

Sets the joint radius at `joint` in the bone chain\'s joint list when
`is_config_individual()<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_rotation_axis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_rotation_axis**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"},
axis:
`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_rotation_axis>`{.interpreted-text
role="ref"}

Sets the rotation axis at `joint` in the bone chain\'s joint list when
`is_config_individual()<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"} is `true`.

The axes are based on the
`Skeleton3D.get_bone_rest()<class_Skeleton3D_method_get_bone_rest>`{.interpreted-text
role="ref"}\'s space, if `axis` is
`ROTATION_AXIS_CUSTOM<class_SpringBoneSimulator3D_constant_ROTATION_AXIS_CUSTOM>`{.interpreted-text
role="ref"}, you can specify any axis.

\*\*Note:\*\* The rotation axis and the forward vector shouldn\'t be
colinear to avoid unintended rotation since **SpringBoneSimulator3D**
does not factor in twisting forces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_rotation_axis_vector}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_rotation_axis_vector**(index:
`int<class_int>`{.interpreted-text role="ref"}, joint:
`int<class_int>`{.interpreted-text role="ref"}, vector:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_rotation_axis_vector>`{.interpreted-text
role="ref"}

Sets the rotation axis vector for the specified joint in the bone chain.

This vector is normalized by an internal process and represents the axis
around which the bone chain can rotate.

If the vector length is `0`, it is considered synonymous with
`ROTATION_AXIS_ALL<class_SpringBoneSimulator3D_constant_ROTATION_AXIS_ALL>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_joint_stiffness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_stiffness**(index: `int<class_int>`{.interpreted-text
role="ref"}, joint: `int<class_int>`{.interpreted-text role="ref"},
stiffness: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_joint_stiffness>`{.interpreted-text
role="ref"}

Sets the stiffness force at `joint` in the bone chain\'s joint list when
`is_config_individual()<class_SpringBoneSimulator3D_method_is_config_individual>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_radius**(index: `int<class_int>`{.interpreted-text role="ref"},
radius: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_radius>`{.interpreted-text
role="ref"}

Sets the joint radius of the bone chain. It is used to move and slide
with the
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} in the collision list.

The value is scaled by
`set_radius_damping_curve()<class_SpringBoneSimulator3D_method_set_radius_damping_curve>`{.interpreted-text
role="ref"} and cached in each joint setting in the joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_radius_damping_curve}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_radius_damping_curve**(index: `int<class_int>`{.interpreted-text
role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_radius_damping_curve>`{.interpreted-text
role="ref"}

Sets the joint radius damping curve of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_root_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_root_bone**(index: `int<class_int>`{.interpreted-text role="ref"},
bone: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_root_bone>`{.interpreted-text
role="ref"}

Sets the root bone index of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_root_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_root_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_root_bone_name>`{.interpreted-text
role="ref"}

Sets the root bone name of the bone chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_rotation_axis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_rotation_axis**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis:
`RotationAxis<enum_SpringBoneSimulator3D_RotationAxis>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_rotation_axis>`{.interpreted-text
role="ref"}

Sets the rotation axis of the bone chain. If set to a specific axis, it
acts like a hinge joint. The value is cached in each joint setting in
the joint list.

The axes are based on the
`Skeleton3D.get_bone_rest()<class_Skeleton3D_method_get_bone_rest>`{.interpreted-text
role="ref"}\'s space, if `axis` is
`ROTATION_AXIS_CUSTOM<class_SpringBoneSimulator3D_constant_ROTATION_AXIS_CUSTOM>`{.interpreted-text
role="ref"}, you can specify any axis.

\*\*Note:\*\* The rotation axis vector and the forward vector shouldn\'t
be colinear to avoid unintended rotation since **SpringBoneSimulator3D**
does not factor in twisting forces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_rotation_axis_vector}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_rotation_axis_vector**(index: `int<class_int>`{.interpreted-text
role="ref"}, vector: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_rotation_axis_vector>`{.interpreted-text
role="ref"}

Sets the rotation axis vector of the bone chain. The value is cached in
each joint setting in the joint list.

This vector is normalized by an internal process and represents the axis
around which the bone chain can rotate.

If the vector length is `0`, it is considered synonymous with
`ROTATION_AXIS_ALL<class_SpringBoneSimulator3D_constant_ROTATION_AXIS_ALL>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_stiffness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stiffness**(index: `int<class_int>`{.interpreted-text role="ref"},
stiffness: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_stiffness>`{.interpreted-text
role="ref"}

Sets the stiffness force of the bone chain. The greater the value, the
faster it recovers to its initial pose.

If `stiffness` is `0`, the modified pose will not return to the original
pose.

The value is scaled by
`set_stiffness_damping_curve()<class_SpringBoneSimulator3D_method_set_stiffness_damping_curve>`{.interpreted-text
role="ref"} and cached in each joint setting in the joint list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneSimulator3D_method_set_stiffness_damping_curve}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stiffness_damping_curve**(index:
`int<class_int>`{.interpreted-text role="ref"}, curve:
`Curve<class_Curve>`{.interpreted-text role="ref"})
`🔗<class_SpringBoneSimulator3D_method_set_stiffness_damping_curve>`{.interpreted-text
role="ref"}

Sets the stiffness force damping curve of the bone chain.
