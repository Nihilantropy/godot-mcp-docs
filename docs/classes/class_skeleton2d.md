github_url
:   hide

# Skeleton2D {#class_Skeleton2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

The parent of a hierarchy of `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"}s, used to create a 2D skeletal animation.

::: rst-class
classref-introduction-group
:::

## Description

**Skeleton2D** parents a hierarchy of
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes. It holds a
reference to each `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"}\'s rest pose and acts as a single point of access to its
bones.

To set up different types of inverse kinematics for the given
Skeleton2D, a
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} should be created. The inverse kinematics be applied by
increasing
`SkeletonModificationStack2D.modification_count<class_SkeletonModificationStack2D_property_modification_count>`{.interpreted-text
role="ref"} and creating the desired number of modifications.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D skeletons <../tutorials/animation/2d_skeletons>`{.interpreted-text
  role="doc"}

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

:::: {#class_Skeleton2D_signal_bone_setup_changed}
::: rst-class
classref-signal
:::
::::

**bone_setup_changed**()
`🔗<class_Skeleton2D_signal_bone_setup_changed>`{.interpreted-text
role="ref"}

Emitted when the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"}
setup attached to this skeletons changes. This is primarily used
internally within the skeleton.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Skeleton2D_method_execute_modifications}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**execute_modifications**(delta: `float<class_float>`{.interpreted-text
role="ref"}, execution_mode: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton2D_method_execute_modifications>`{.interpreted-text
role="ref"}

Executes all the modifications on the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"}, if the Skeleton2D has one assigned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_get_bone}
::: rst-class
classref-method
:::
::::

`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} **get_bone**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Skeleton2D_method_get_bone>`{.interpreted-text role="ref"}

Returns a `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} from the
node hierarchy parented by Skeleton2D. The object to return is
identified by the parameter `idx`. Bones are indexed by descending the
node hierarchy from top to bottom, adding the children of each branch
before moving to the next sibling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_get_bone_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_bone_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton2D_method_get_bone_count>`{.interpreted-text
role="ref"}

Returns the number of `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} nodes in the node hierarchy parented by Skeleton2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_get_bone_local_pose_override}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_bone_local_pose_override**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Skeleton2D_method_get_bone_local_pose_override>`{.interpreted-text
role="ref"}

Returns the local pose override transform for `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_get_modification_stack}
::: rst-class
classref-method
:::
::::

`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} **get_modification_stack**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton2D_method_get_modification_stack>`{.interpreted-text
role="ref"}

Returns the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} attached to this skeleton, if one exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_get_skeleton}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton2D_method_get_skeleton>`{.interpreted-text role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of a
Skeleton2D instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_set_bone_local_pose_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_local_pose_override**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"}, override_pose:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
strength: `float<class_float>`{.interpreted-text role="ref"},
persistent: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Skeleton2D_method_set_bone_local_pose_override>`{.interpreted-text
role="ref"}

Sets the local pose transform, `override_pose`, for the bone at
`bone_idx`.

`strength` is the interpolation strength that will be used when applying
the pose, and `persistent` determines if the applied pose will remain.

\*\*Note:\*\* The pose transform needs to be a local transform relative
to the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node at
`bone_idx`!

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton2D_method_set_modification_stack}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_modification_stack**(modification_stack:
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton2D_method_set_modification_stack>`{.interpreted-text
role="ref"}

Sets the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} attached to this skeleton.
