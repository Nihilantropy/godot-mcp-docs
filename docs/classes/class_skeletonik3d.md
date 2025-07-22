github_url
:   hide

# SkeletonIK3D {#class_SkeletonIK3D}

**Deprecated:** This class may be changed or removed in future versions.

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node used to rotate all bones of a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} bone chain
a way that places the end bone at a desired 3D position.

::: rst-class
classref-introduction-group
:::

## Description

SkeletonIK3D is used to rotate all bones of a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} bone chain
a way that places the end bone at a desired 3D position. A typical
scenario for IK in games is to place a character\'s feet on the ground
or a character\'s hands on a currently held object. SkeletonIK uses
FabrikInverseKinematic internally to solve the bone chain and applies
the results to the `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} `bones_global_pose_override` property for all affected bones
in the chain. If fully applied, this overwrites any bone transform from
`Animation<class_Animation>`{.interpreted-text role="ref"}s or bone
custom poses set by users. The applied amount can be controlled with the
`SkeletonModifier3D.influence<class_SkeletonModifier3D_property_influence>`{.interpreted-text
role="ref"} property.

    # Apply IK effect automatically on every new frame (not the current)
    skeleton_ik_node.start()

    # Apply IK effect only on the current frame
    skeleton_ik_node.start(true)

    # Stop IK effect and reset bones_global_pose_override on Skeleton
    skeleton_ik_node.stop()

    # Apply full IK effect
    skeleton_ik_node.set_influence(1.0)

    # Apply half IK effect
    skeleton_ik_node.set_influence(0.5)

    # Apply zero IK effect (a value at or below 0.01 also removes bones_global_pose_override on Skeleton)
    skeleton_ik_node.set_influence(0.0)

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

:::: {#class_SkeletonIK3D_property_interpolation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **interpolation**
`🔗<class_SkeletonIK3D_property_interpolation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interpolation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_interpolation**()

**Deprecated:** Use
`SkeletonModifier3D.influence<class_SkeletonModifier3D_property_influence>`{.interpreted-text
role="ref"} instead.

Interpolation value for how much the IK results are applied to the
current skeleton bone chain. A value of `1.0` will overwrite all
skeleton bone transforms completely while a value of `0.0` will visually
disable the SkeletonIK.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_magnet}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **magnet** =
`Vector3(0, 0, 0)`
`🔗<class_SkeletonIK3D_property_magnet>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_magnet_position**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_magnet_position**()

Secondary target position (first is
`target<class_SkeletonIK3D_property_target>`{.interpreted-text
role="ref"} property or
`target_node<class_SkeletonIK3D_property_target_node>`{.interpreted-text
role="ref"}) for the IK chain. Use magnet position (pole target) to
control the bending of the IK chain. Only works if the bone chain has
more than 2 bones. The middle chain bone position will be linearly
interpolated with the magnet position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_max_iterations}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_iterations** = `10`
`🔗<class_SkeletonIK3D_property_max_iterations>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_iterations**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_iterations**()

Number of iteration loops used by the IK solver to produce more accurate
(and elegant) bone chain results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_min_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **min_distance** =
`0.01` `🔗<class_SkeletonIK3D_property_min_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_min_distance**()

The minimum distance between bone and goal target. If the distance is
below this value, the IK solver stops further iterations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_override_tip_basis}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **override_tip_basis**
= `true`
`🔗<class_SkeletonIK3D_property_override_tip_basis>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_override_tip_basis**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_override_tip_basis**()

If `true` overwrites the rotation of the tip bone with the rotation of
the `target<class_SkeletonIK3D_property_target>`{.interpreted-text
role="ref"} (or
`target_node<class_SkeletonIK3D_property_target_node>`{.interpreted-text
role="ref"} if defined).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_root_bone}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**root_bone** = `&""`
`🔗<class_SkeletonIK3D_property_root_bone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_bone**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_root_bone**()

The name of the current root bone, the first bone in the IK chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_target}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**target** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_SkeletonIK3D_property_target>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_target_transform**()

First target of the IK chain where the tip bone is placed and, if
`override_tip_basis<class_SkeletonIK3D_property_override_tip_basis>`{.interpreted-text
role="ref"} is `true`, how the tip bone is rotated. If a
`target_node<class_SkeletonIK3D_property_target_node>`{.interpreted-text
role="ref"} path is available the nodes transform is used instead and
this property is ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_target_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **target_node**
= `NodePath("")`
`🔗<class_SkeletonIK3D_property_target_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

Target node `NodePath<class_NodePath>`{.interpreted-text role="ref"} for
the IK chain. If available, the node\'s current
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} is used
instead of the
`target<class_SkeletonIK3D_property_target>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_tip_bone}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**tip_bone** = `&""`
`🔗<class_SkeletonIK3D_property_tip_bone>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tip_bone**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_tip_bone**()

The name of the current tip bone, the last bone in the IK chain placed
at the `target<class_SkeletonIK3D_property_target>`{.interpreted-text
role="ref"} transform (or
`target_node<class_SkeletonIK3D_property_target_node>`{.interpreted-text
role="ref"} if defined).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_property_use_magnet}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_magnet** =
`false` `🔗<class_SkeletonIK3D_property_use_magnet>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_magnet**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_magnet**()

If `true`, instructs the IK solver to consider the secondary magnet
target (pole target) when calculating the bone chain. Use the magnet
position (pole target) to control the bending of the IK chain.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonIK3D_method_get_parent_skeleton}
::: rst-class
classref-method
:::
::::

`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
**get_parent_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonIK3D_method_get_parent_skeleton>`{.interpreted-text
role="ref"}

Returns the parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} node that was present when SkeletonIK entered the scene
tree. Returns `null` if the parent node was not a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node when
SkeletonIK3D entered the scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_method_is_running}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_running**()
`🔗<class_SkeletonIK3D_method_is_running>`{.interpreted-text role="ref"}

Returns `true` if SkeletonIK is applying IK effects on continues frames
to the `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
bones. Returns `false` if SkeletonIK is stopped or
`start()<class_SkeletonIK3D_method_start>`{.interpreted-text role="ref"}
was used with the `one_time` parameter set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_method_start}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start**(one_time: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_SkeletonIK3D_method_start>`{.interpreted-text
role="ref"}

Starts applying IK effects on each frame to the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} bones but
will only take effect starting on the next frame. If `one_time` is
`true`, this will take effect immediately but also reset on the next
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonIK3D_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_SkeletonIK3D_method_stop>`{.interpreted-text role="ref"}

Stops applying IK effects on each frame to the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} bones and
also calls
`Skeleton3D.clear_bones_global_pose_override()<class_Skeleton3D_method_clear_bones_global_pose_override>`{.interpreted-text
role="ref"} to remove existing overrides on all bones.
