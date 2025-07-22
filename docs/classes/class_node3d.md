github_url
:   hide

::: {.meta keywords="spatial"}
:::

# Node3D {#class_Node3D}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioListener3D<class_AudioListener3D>`{.interpreted-text role="ref"},
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"},
`BoneAttachment3D<class_BoneAttachment3D>`{.interpreted-text
role="ref"}, `Camera3D<class_Camera3D>`{.interpreted-text role="ref"},
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"},
`CollisionPolygon3D<class_CollisionPolygon3D>`{.interpreted-text
role="ref"},
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}, `GridMap<class_GridMap>`{.interpreted-text role="ref"},
`ImporterMeshInstance3D<class_ImporterMeshInstance3D>`{.interpreted-text
role="ref"}, `Joint3D<class_Joint3D>`{.interpreted-text role="ref"},
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"},
`Marker3D<class_Marker3D>`{.interpreted-text role="ref"},
`NavigationLink3D<class_NavigationLink3D>`{.interpreted-text
role="ref"},
`NavigationObstacle3D<class_NavigationObstacle3D>`{.interpreted-text
role="ref"},
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"},
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"}, `OpenXRHand<class_OpenXRHand>`{.interpreted-text
role="ref"},
`OpenXRRenderModel<class_OpenXRRenderModel>`{.interpreted-text
role="ref"},
`OpenXRRenderModelManager<class_OpenXRRenderModelManager>`{.interpreted-text
role="ref"}, `Path3D<class_Path3D>`{.interpreted-text role="ref"},
`PathFollow3D<class_PathFollow3D>`{.interpreted-text role="ref"},
`RayCast3D<class_RayCast3D>`{.interpreted-text role="ref"},
`RemoteTransform3D<class_RemoteTransform3D>`{.interpreted-text
role="ref"}, `ShapeCast3D<class_ShapeCast3D>`{.interpreted-text
role="ref"}, `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"},
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"}, `SpringArm3D<class_SpringArm3D>`{.interpreted-text
role="ref"},
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"}, `VehicleWheel3D<class_VehicleWheel3D>`{.interpreted-text
role="ref"},
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"},
`XRFaceModifier3D<class_XRFaceModifier3D>`{.interpreted-text
role="ref"}, `XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"},
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"}

Base object in 3D space, inherited by all 3D nodes.

::: rst-class
classref-introduction-group
:::

## Description

The **Node3D** node is the base representation of a node in 3D space.
All other 3D nodes inherit from this class.

Affine operations (translation, rotation, scale) are calculated in the
coordinate system relative to the parent, unless the **Node3D**\'s
`top_level<class_Node3D_property_top_level>`{.interpreted-text
role="ref"} is `true`. In this coordinate system, affine operations
correspond to direct affine operations on the **Node3D**\'s
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"}. The term *parent space* refers to this coordinate system.
The coordinate system that is attached to the **Node3D** itself is
referred to as object-local coordinate system, or *local space*.

\*\*Note:\*\* Unless otherwise specified, all methods that need angle
parameters must receive angles in *radians*. To convert degrees to
radians, use
`@GlobalScope.deg_to_rad()<class_@GlobalScope_method_deg_to_rad>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In Godot 3 and older, **Node3D** was named *Spatial*.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Introduction to 3D <../tutorials/3d/introduction_to_3d>`{.interpreted-text
  role="doc"}
- [All 3D
  Demos](https://github.com/godotengine/godot-demo-projects/tree/master/3d)

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

:::: {#class_Node3D_signal_visibility_changed}
::: rst-class
classref-signal
:::
::::

**visibility_changed**()
`🔗<class_Node3D_signal_visibility_changed>`{.interpreted-text
role="ref"}

Emitted when this node\'s visibility changes (see
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
and
`is_visible_in_tree()<class_Node3D_method_is_visible_in_tree>`{.interpreted-text
role="ref"}).

This signal is emitted *after* the related
`NOTIFICATION_VISIBILITY_CHANGED<class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED>`{.interpreted-text
role="ref"} notification.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Node3D_RotationEditMode}
::: rst-class
classref-enumeration
:::
::::

enum **RotationEditMode**:
`🔗<enum_Node3D_RotationEditMode>`{.interpreted-text role="ref"}

:::: {#class_Node3D_constant_ROTATION_EDIT_MODE_EULER}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **ROTATION_EDIT_MODE_EULER** = `0`

The rotation is edited using a
`Vector3<class_Vector3>`{.interpreted-text role="ref"} in [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles).

:::: {#class_Node3D_constant_ROTATION_EDIT_MODE_QUATERNION}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **ROTATION_EDIT_MODE_QUATERNION** = `1`

The rotation is edited using a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}.

:::: {#class_Node3D_constant_ROTATION_EDIT_MODE_BASIS}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **ROTATION_EDIT_MODE_BASIS** = `2`

The rotation is edited using a `Basis<class_Basis>`{.interpreted-text
role="ref"}. In this mode, the raw
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}\'s
axes can be freely modified, but the
`scale<class_Node3D_property_scale>`{.interpreted-text role="ref"}
property is not available.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_TRANSFORM_CHANGED** = `2000`
`🔗<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this node\'s
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} changes, if
`is_transform_notification_enabled()<class_Node3D_method_is_transform_notification_enabled>`{.interpreted-text
role="ref"} is `true`. See also
`set_notify_transform()<class_Node3D_method_set_notify_transform>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Most 3D nodes such as
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
or `CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} automatically enable this to function correctly.

\*\*Note:\*\* In the editor, nodes will propagate this notification to
their children if a gizmo is attached (see
`add_gizmo()<class_Node3D_method_add_gizmo>`{.interpreted-text
role="ref"}).

:::: {#class_Node3D_constant_NOTIFICATION_ENTER_WORLD}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_ENTER_WORLD** = `41`
`🔗<class_Node3D_constant_NOTIFICATION_ENTER_WORLD>`{.interpreted-text
role="ref"}

Notification received when this node is registered to a new
`World3D<class_World3D>`{.interpreted-text role="ref"} (see
`get_world_3d()<class_Node3D_method_get_world_3d>`{.interpreted-text
role="ref"}).

:::: {#class_Node3D_constant_NOTIFICATION_EXIT_WORLD}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EXIT_WORLD** = `42`
`🔗<class_Node3D_constant_NOTIFICATION_EXIT_WORLD>`{.interpreted-text
role="ref"}

Notification received when this node is unregistered from the current
`World3D<class_World3D>`{.interpreted-text role="ref"} (see
`get_world_3d()<class_Node3D_method_get_world_3d>`{.interpreted-text
role="ref"}).

:::: {#class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_VISIBILITY_CHANGED** = `43`
`🔗<class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this node\'s visibility changes (see
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
and
`is_visible_in_tree()<class_Node3D_method_is_visible_in_tree>`{.interpreted-text
role="ref"}).

This notification is received *before* the related
`visibility_changed<class_Node3D_signal_visibility_changed>`{.interpreted-text
role="ref"} signal.

:::: {#class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_LOCAL_TRANSFORM_CHANGED** = `44`
`🔗<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this node\'s
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} changes, if
`is_local_transform_notification_enabled()<class_Node3D_method_is_local_transform_notification_enabled>`{.interpreted-text
role="ref"} is `true`. This is not received when a parent **Node3D**\'s
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} changes. See also
`set_notify_local_transform()<class_Node3D_method_set_notify_local_transform>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Some 3D nodes such as
`CSGShape3D<class_CSGShape3D>`{.interpreted-text role="ref"} or
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
automatically enable this to function correctly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Node3D_property_basis}
::: rst-class
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **basis**
`🔗<class_Node3D_property_basis>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_basis**(value: `Basis<class_Basis>`{.interpreted-text
  role="ref"})
- `Basis<class_Basis>`{.interpreted-text role="ref"} **get_basis**()

Basis of the
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} property. Represents the rotation, scale, and shear of this
node in parent space (relative to the parent node).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_basis}
::: rst-class
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **global_basis**
`🔗<class_Node3D_property_global_basis>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_basis**(value: `Basis<class_Basis>`{.interpreted-text
  role="ref"})
- `Basis<class_Basis>`{.interpreted-text role="ref"}
  **get_global_basis**()

Basis of the
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} property. Represents the rotation, scale, and shear of this
node in global space (relative to the world).

\*\*Note:\*\* If the node is not inside the tree, getting this property
fails and returns
`Basis.IDENTITY<class_Basis_constant_IDENTITY>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**global_position**
`🔗<class_Node3D_property_global_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_position**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_global_position**()

Global position (translation) of this node in global space (relative to
the world). This is equivalent to the
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"}\'s
`Transform3D.origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If the node is not inside the tree, getting this property
fails and returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_rotation}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**global_rotation**
`🔗<class_Node3D_property_global_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_rotation**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_global_rotation**()

Global rotation of this node as [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles), in radians and in
global space (relative to the world). This value is obtained from
`global_basis<class_Node3D_property_global_basis>`{.interpreted-text
role="ref"}\'s rotation.

- The `Vector3.x<class_Vector3_property_x>`{.interpreted-text
  role="ref"} is the angle around the global X axis (pitch);
- The `Vector3.y<class_Vector3_property_y>`{.interpreted-text
  role="ref"} is the angle around the global Y axis (yaw);
- The `Vector3.z<class_Vector3_property_z>`{.interpreted-text
  role="ref"} is the angle around the global Z axis (roll).

\*\*Note:\*\* Unlike
`rotation<class_Node3D_property_rotation>`{.interpreted-text
role="ref"}, this property always follows the YXZ convention
(`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* If the node is not inside the tree, getting this property
fails and returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_rotation_degrees}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**global_rotation_degrees**
`🔗<class_Node3D_property_global_rotation_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_rotation_degrees**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_global_rotation_degrees**()

The
`global_rotation<class_Node3D_property_global_rotation>`{.interpreted-text
role="ref"} of this node, in degrees instead of radians.

\*\*Note:\*\* If the node is not inside the tree, getting this property
fails and returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_transform}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**global_transform**
`🔗<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_global_transform**()

The transformation of this node, in global space (relative to the
world). Contains and represents this node\'s
`global_position<class_Node3D_property_global_position>`{.interpreted-text
role="ref"},
`global_rotation<class_Node3D_property_global_rotation>`{.interpreted-text
role="ref"}, and global scale.

\*\*Note:\*\* If the node is not inside the tree, getting this property
fails and returns
`Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **position** =
`Vector3(0, 0, 0)`
`🔗<class_Node3D_property_position>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_position**()

Position (translation) of this node in parent space (relative to the
parent node). This is equivalent to the
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"}\'s
`Transform3D.origin<class_Transform3D_property_origin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_quaternion}
::: rst-class
classref-property
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**quaternion** `🔗<class_Node3D_property_quaternion>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_quaternion**(value:
  `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
- `Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
  **get_quaternion**()

Rotation of this node represented as a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} in parent
space (relative to the parent node). This value is obtained from
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}\'s
rotation.

\*\*Note:\*\* Quaternions are much more suitable for 3D math but are
less intuitive. Setting this property can be useful for interpolation
(see
`Quaternion.slerp()<class_Quaternion_method_slerp>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **rotation** =
`Vector3(0, 0, 0)`
`🔗<class_Node3D_property_rotation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_rotation**()

Rotation of this node as [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles), in radians and in
parent space (relative to the parent node). This value is obtained from
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}\'s
rotation.

- The `Vector3.x<class_Vector3_property_x>`{.interpreted-text
  role="ref"} is the angle around the local X axis (pitch);
- The `Vector3.y<class_Vector3_property_y>`{.interpreted-text
  role="ref"} is the angle around the local Y axis (yaw);
- The `Vector3.z<class_Vector3_property_z>`{.interpreted-text
  role="ref"} is the angle around the local Z axis (roll).

The order of each consecutive rotation can be changed with
`rotation_order<class_Node3D_property_rotation_order>`{.interpreted-text
role="ref"} (see
`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
constants). By default, the YXZ convention is used
(`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* This property is edited in degrees in the inspector. If
you want to use degrees in a script, use
`rotation_degrees<class_Node3D_property_rotation_degrees>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation_degrees}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**rotation_degrees**
`🔗<class_Node3D_property_rotation_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_degrees**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_rotation_degrees**()

The `rotation<class_Node3D_property_rotation>`{.interpreted-text
role="ref"} of this node, in degrees instead of radians.

\*\*Note:\*\* This is **not** the property available in the Inspector
dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation_edit_mode}
::: rst-class
classref-property
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **rotation_edit_mode** = `0`
`🔗<class_Node3D_property_rotation_edit_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_edit_mode**(value:
  `RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
  role="ref"})
- `RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
  role="ref"} **get_rotation_edit_mode**()

How this node\'s rotation and scale are displayed in the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation_order}
::: rst-class
classref-property
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**rotation_order** = `2`
`🔗<class_Node3D_property_rotation_order>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_order**(value:
  `EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text
  role="ref"})
- `EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text
  role="ref"} **get_rotation_order**()

The axis rotation order of the
`rotation<class_Node3D_property_rotation>`{.interpreted-text role="ref"}
property. The final orientation is calculated by rotating around the
local X, Y, and Z axis in this order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_scale}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **scale** =
`Vector3(1, 1, 1)` `🔗<class_Node3D_property_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_scale**()

Scale of this node in local space (relative to this node). This value is
obtained from `basis<class_Node3D_property_basis>`{.interpreted-text
role="ref"}\'s scale.

\*\*Note:\*\* The behavior of some 3D node types is not affected by this
property. These include `Light3D<class_Light3D>`{.interpreted-text
role="ref"}, `Camera3D<class_Camera3D>`{.interpreted-text role="ref"},
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"}, and more.

\*\*Warning:\*\* The scale\'s components must either be all positive or
all negative, and **not** exactly `0.0`. Otherwise, it won\'t be
possible to obtain the scale from the
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}. This
may cause the intended scale to be lost when reloaded from disk, and
potentially other unstable behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_top_level}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **top_level** = `false`
`🔗<class_Node3D_property_top_level>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_top_level**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_set_as_top_level**()

If `true`, the node does not inherit its transformations from its
parent. As such, node transformations will only be in global space,
which also means that
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} and
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} will be identical.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_transform}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_Node3D_property_transform>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_transform**()

The local transformation of this node, in parent space (relative to the
parent node). Contains and represents this node\'s
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"},
`rotation<class_Node3D_property_rotation>`{.interpreted-text
role="ref"}, and `scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_visibility_parent}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**visibility_parent** = `NodePath("")`
`🔗<class_Node3D_property_visibility_parent>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_parent**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_visibility_parent**()

Path to the visibility range parent for this node and its descendants.
The visibility parent must be a
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"}.

Any visual instance will only be visible if the visibility parent (and
all of its visibility ancestors) is hidden by being closer to the camera
than its own
`GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>`{.interpreted-text
role="ref"}. Nodes hidden via the
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
property are essentially removed from the visibility dependency tree, so
dependent instances will not take the hidden node or its descendants
into account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_Node3D_property_visible>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, this node can be visible. The node is only rendered when all
of its ancestors are visible, as well. That means
`is_visible_in_tree()<class_Node3D_method_is_visible_in_tree>`{.interpreted-text
role="ref"} must return `true`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Node3D_method_add_gizmo}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_gizmo**(gizmo: `Node3DGizmo<class_Node3DGizmo>`{.interpreted-text
role="ref"}) `🔗<class_Node3D_method_add_gizmo>`{.interpreted-text
role="ref"}

Attaches the given `gizmo` to this node. Only works in the editor.

\*\*Note:\*\* `gizmo` should be an
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}. The argument type is
`Node3DGizmo<class_Node3DGizmo>`{.interpreted-text role="ref"} to avoid
depending on editor classes in **Node3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_clear_gizmos}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_gizmos**()
`🔗<class_Node3D_method_clear_gizmos>`{.interpreted-text role="ref"}

Clears all
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} objects attached to this node. Only works in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_clear_subgizmo_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_subgizmo_selection**()
`🔗<class_Node3D_method_clear_subgizmo_selection>`{.interpreted-text
role="ref"}

Deselects all subgizmos for this node. Useful to call when the selected
subgizmo may no longer exist after a property change. Only works in the
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_force_update_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_transform**()
`🔗<class_Node3D_method_force_update_transform>`{.interpreted-text
role="ref"}

Forces the node\'s
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} to update, by sending
`NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}. Fails if the node is not inside the tree.

\*\*Note:\*\* For performance reasons, transform changes are usually
accumulated and applied *once* at the end of the frame. The update
propagates through **Node3D** children, as well. Therefore, use this
method only when you need an up-to-date transform (such as during
physics operations).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_gizmos}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node3DGizmo<class_Node3DGizmo>`{.interpreted-text
role="ref"}\] **get_gizmos**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_get_gizmos>`{.interpreted-text
role="ref"}

Returns all the
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} objects attached to this node. Only works in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_global_transform_interpolated}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_global_transform_interpolated**()
`🔗<class_Node3D_method_get_global_transform_interpolated>`{.interpreted-text
role="ref"}

When using physics interpolation, there will be circumstances in which
you want to know the interpolated (displayed) transform of a node rather
than the standard transform (which may only be accurate to the most
recent physics tick).

This is particularly important for frame-based operations that take
place in
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, rather than
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. Examples include
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}s focusing on a
node, or finding where to fire lasers from on a frame rather than
physics tick.

\*\*Note:\*\* This function creates an interpolation pump on the
**Node3D** the first time it is called, which can respond to physics
interpolation resets. If you get problems with \"streaking\" when
initially following a **Node3D**, be sure to call
`get_global_transform_interpolated()<class_Node3D_method_get_global_transform_interpolated>`{.interpreted-text
role="ref"} at least once *before* resetting the **Node3D** physics
interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_parent_node_3d}
::: rst-class
classref-method
:::
::::

`Node3D<class_Node3D>`{.interpreted-text role="ref"}
**get_parent_node_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_get_parent_node_3d>`{.interpreted-text
role="ref"}

Returns the parent **Node3D** that directly affects this node\'s
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"}. Returns `null` if no parent exists, the parent is not a
**Node3D**, or
`top_level<class_Node3D_property_top_level>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* This method is not always equivalent to
`Node.get_parent()<class_Node_method_get_parent>`{.interpreted-text
role="ref"}, which does not take
`top_level<class_Node3D_property_top_level>`{.interpreted-text
role="ref"} into account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_world_3d}
::: rst-class
classref-method
:::
::::

`World3D<class_World3D>`{.interpreted-text role="ref"}
**get_world_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_get_world_3d>`{.interpreted-text
role="ref"}

Returns the `World3D<class_World3D>`{.interpreted-text role="ref"} this
node is registered to.

Usually, this is the same as the world used by this node\'s viewport
(see
`Node.get_viewport()<class_Node_method_get_viewport>`{.interpreted-text
role="ref"} and
`Viewport.find_world_3d()<class_Viewport_method_find_world_3d>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_global_rotate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_rotate**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_global_rotate>`{.interpreted-text role="ref"}

Rotates this node\'s
`global_basis<class_Node3D_property_global_basis>`{.interpreted-text
role="ref"} around the global `axis` by the given `angle`, in radians.
This operation is calculated in global space (relative to the world) and
preserves the
`global_position<class_Node3D_property_global_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_global_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_scale**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Node3D_method_global_scale>`{.interpreted-text
role="ref"}

Scales this node\'s
`global_basis<class_Node3D_property_global_basis>`{.interpreted-text
role="ref"} by the given `scale` factor. This operation is calculated in
global space (relative to the world) and preserves the
`global_position<class_Node3D_property_global_position>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is not to be confused with the
`scale<class_Node3D_property_scale>`{.interpreted-text role="ref"}
property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_global_translate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_translate**(offset: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_global_translate>`{.interpreted-text role="ref"}

Adds the given translation `offset` to the node\'s
`global_position<class_Node3D_property_global_position>`{.interpreted-text
role="ref"} in global space (relative to the world).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_hide}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **hide**()
`🔗<class_Node3D_method_hide>`{.interpreted-text role="ref"}

Prevents this node from being rendered. Equivalent to setting
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
to `false`. This is the opposite of
`show()<class_Node3D_method_show>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_local_transform_notification_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_local_transform_notification_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_local_transform_notification_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the node receives
`NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} changes. This is enabled with
`set_notify_local_transform()<class_Node3D_method_set_notify_local_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_scale_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_scale_disabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_scale_disabled>`{.interpreted-text
role="ref"}

Returns `true` if this node\'s
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} is automatically orthonormalized. This results in this node
not appearing distorted, as if its global scale were set to
`Vector3.ONE<class_Vector3_constant_ONE>`{.interpreted-text role="ref"}
(or its negative counterpart). See also
`set_disable_scale()<class_Node3D_method_set_disable_scale>`{.interpreted-text
role="ref"} and
`orthonormalize()<class_Node3D_method_orthonormalize>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} is not affected by this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_transform_notification_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_transform_notification_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_transform_notification_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the node receives
`NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} changes. This is enabled with
`set_notify_transform()<class_Node3D_method_set_notify_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_visible_in_tree}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_visible_in_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_visible_in_tree>`{.interpreted-text
role="ref"}

Returns `true` if this node is inside the scene tree and the
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
property is `true` for this node and all of its **Node3D** ancestors *in
sequence*. An ancestor of any other type (such as
`Node<class_Node>`{.interpreted-text role="ref"} or
`Node2D<class_Node2D>`{.interpreted-text role="ref"}) breaks the
sequence. See also
`Node.get_parent()<class_Node_method_get_parent>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method cannot take
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} into account, so even if this method returns `true`, the
node may not be rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_look_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**look_at**(target: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, up: `Vector3<class_Vector3>`{.interpreted-text role="ref"}
= Vector3(0, 1, 0), use_model_front:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Node3D_method_look_at>`{.interpreted-text role="ref"}

Rotates the node so that the local forward axis (-Z,
`Vector3.FORWARD<class_Vector3_constant_FORWARD>`{.interpreted-text
role="ref"}) points toward the `target` position. This operation is
calculated in global space (relative to the world).

The local up axis (+Y) points as close to the `up` vector as possible
while staying perpendicular to the local forward axis. The resulting
transform is orthogonal, and the scale is preserved. Non-uniform scaling
may not work correctly.

The `target` position cannot be the same as the node\'s position, the
`up` vector cannot be
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}. Furthermore, the direction from the node\'s position to the
`target` position cannot be parallel to the `up` vector, to avoid an
unintended rotation around the local Z axis.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as
forward (implies +X is left) and points toward the `target` position. By
default, the -Z axis (camera forward) is treated as forward (implies +X
is right).

\*\*Note:\*\* This method fails if the node is not in the scene tree. If
necessary, use
`look_at_from_position()<class_Node3D_method_look_at_from_position>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_look_at_from_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**look_at_from_position**(position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, target:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, up:
`Vector3<class_Vector3>`{.interpreted-text role="ref"} = Vector3(0, 1,
0), use_model_front: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_Node3D_method_look_at_from_position>`{.interpreted-text
role="ref"}

Moves the node to the specified `position`, then rotates the node to
point toward the `target` position, similar to
`look_at()<class_Node3D_method_look_at>`{.interpreted-text role="ref"}.
This operation is calculated in global space (relative to the world).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_orthonormalize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**orthonormalize**()
`🔗<class_Node3D_method_orthonormalize>`{.interpreted-text role="ref"}

Orthonormalizes this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}. This
method sets this node\'s
`scale<class_Node3D_property_scale>`{.interpreted-text role="ref"} to
`Vector3.ONE<class_Vector3_constant_ONE>`{.interpreted-text role="ref"}
(or its negative counterpart), but preserves the
`position<class_Node3D_property_position>`{.interpreted-text role="ref"}
and `rotation<class_Node3D_property_rotation>`{.interpreted-text
role="ref"}. See also
`Transform3D.orthonormalized()<class_Transform3D_method_orthonormalized>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate**(axis: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate>`{.interpreted-text role="ref"}

Rotates this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}
around the `axis` by the given `angle`, in radians. This operation is
calculated in parent space (relative to the parent) and preserves the
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_object_local}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_object_local**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_object_local>`{.interpreted-text
role="ref"}

Rotates this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}
around the `axis` by the given `angle`, in radians. This operation is
calculated in local space (relative to this node) and preserves the
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_x}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_x**(angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_x>`{.interpreted-text role="ref"}

Rotates this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}
around the X axis by the given `angle`, in radians. This operation is
calculated in parent space (relative to the parent) and preserves the
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_y}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_y**(angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_y>`{.interpreted-text role="ref"}

Rotates this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}
around the Y axis by the given `angle`, in radians. This operation is
calculated in parent space (relative to the parent) and preserves the
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_z}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_z**(angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_z>`{.interpreted-text role="ref"}

Rotates this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"}
around the Z axis by the given `angle`, in radians. This operation is
calculated in parent space (relative to the parent) and preserves the
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_scale_object_local}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scale_object_local**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_scale_object_local>`{.interpreted-text
role="ref"}

Scales this node\'s
`basis<class_Node3D_property_basis>`{.interpreted-text role="ref"} by
the given `scale` factor. This operation is calculated in local space
(relative to this node) and preserves the
`position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_disable_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_scale**(disable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_set_disable_scale>`{.interpreted-text
role="ref"}

If `true`, this node\'s
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} is automatically orthonormalized. This results in this node
not appearing distorted, as if its global scale were set to
`Vector3.ONE<class_Vector3_constant_ONE>`{.interpreted-text role="ref"}
(or its negative counterpart). See also
`is_scale_disabled()<class_Node3D_method_is_scale_disabled>`{.interpreted-text
role="ref"} and
`orthonormalize()<class_Node3D_method_orthonormalize>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} is not affected by this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_identity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_identity**()
`🔗<class_Node3D_method_set_identity>`{.interpreted-text role="ref"}

Sets this node\'s
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} to
`Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>`{.interpreted-text
role="ref"}, which resets all transformations in parent space
(`position<class_Node3D_property_position>`{.interpreted-text
role="ref"},
`rotation<class_Node3D_property_rotation>`{.interpreted-text
role="ref"}, and `scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_ignore_transform_notification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ignore_transform_notification**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_set_ignore_transform_notification>`{.interpreted-text
role="ref"}

If `true`, the node will not receive
`NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} or
`NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}.

It may useful to call this method when handling these notifications to
prevent infinite recursion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_notify_local_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_notify_local_transform**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_set_notify_local_transform>`{.interpreted-text
role="ref"}

If `true`, the node will receive
`NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} changes.

\*\*Note:\*\* Some 3D nodes such as
`CSGShape3D<class_CSGShape3D>`{.interpreted-text role="ref"} or
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
automatically enable this to function correctly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_notify_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_notify_transform**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_set_notify_transform>`{.interpreted-text
role="ref"}

If `true`, the node will receive
`NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever
`global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} changes.

\*\*Note:\*\* Most 3D nodes such as
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
or `CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} automatically enable this to function correctly.

\*\*Note:\*\* In the editor, nodes will propagate this notification to
their children if a gizmo is attached (see
`add_gizmo()<class_Node3D_method_add_gizmo>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_subgizmo_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_subgizmo_selection**(gizmo:
`Node3DGizmo<class_Node3DGizmo>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_set_subgizmo_selection>`{.interpreted-text
role="ref"}

Selects the `gizmo`\'s subgizmo with the given `id` and sets its
transform. Only works in the editor.

\*\*Note:\*\* The gizmo object would typically be an instance of
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, but the argument type is kept generic to avoid creating a
dependency on editor classes in **Node3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_show}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **show**()
`🔗<class_Node3D_method_show>`{.interpreted-text role="ref"}

Allows this node to be rendered. Equivalent to setting
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
to `true`. This is the opposite of
`hide()<class_Node3D_method_hide>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_to_global}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**to_global**(local_point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_to_global>`{.interpreted-text
role="ref"}

Returns the `local_point` converted from this node\'s local space to
global space. This is the opposite of
`to_local()<class_Node3D_method_to_local>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_to_local}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**to_local**(global_point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_to_local>`{.interpreted-text
role="ref"}

Returns the `global_point` converted from global space to this node\'s
local space. This is the opposite of
`to_global()<class_Node3D_method_to_global>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_translate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**translate**(offset: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Node3D_method_translate>`{.interpreted-text
role="ref"}

Adds the given translation `offset` to the node\'s position, in local
space (relative to this node).

\*\*Note:\*\* Prefer using
`translate_object_local()<class_Node3D_method_translate_object_local>`{.interpreted-text
role="ref"}, instead, as this method may be changed in a future release.

\*\*Note:\*\* Despite the naming convention, this operation is **not**
calculated in parent space for compatibility reasons. To translate in
parent space, add `offset` to the
`position<class_Node3D_property_position>`{.interpreted-text role="ref"}
(`node_3d.position += offset`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_translate_object_local}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**translate_object_local**(offset:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_translate_object_local>`{.interpreted-text
role="ref"}

Adds the given translation `offset` to the node\'s position, in local
space (relative to this node).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_update_gizmos}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_gizmos**()
`🔗<class_Node3D_method_update_gizmos>`{.interpreted-text role="ref"}

Updates all the
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} objects attached to this node. Only works in the editor.
